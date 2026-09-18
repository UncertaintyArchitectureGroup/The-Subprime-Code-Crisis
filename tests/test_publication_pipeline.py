"""Offline tests for the publication boundary, not a substitute for Chromium CI."""
import copy
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest

MODULE = Path(__file__).resolve().parents[1] / 'tools/publishing/publish.py'
SPEC = importlib.util.spec_from_file_location('subprime_publish', MODULE)
pub = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(pub)


class PublicationBoundaryTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        (self.root / 'tools/publishing').mkdir(parents=True)
        (self.root / 'report/articles').mkdir(parents=True)
        for name in ('publish.py', 'export-pdf.mjs', 'quartz.config.ts', 'quartz.layout.ts'):
            (self.root / 'tools/publishing' / name).write_text('fixture')
        self.source = self.root / 'report/articles/example.md'
        self.source.write_text('# Example\n\nA conceptual argument.\n')
        self.data = {'schema_version': 1, 'engine': {'repository': pub.UPSTREAM,
            'commit': 'a' * 40}, 'articles': [{'slug': 'example',
            'source': 'report/articles/example.md', 'title': 'Example',
            'author': 'Vitalii Oborskyi', 'description': 'An example', 'status': 'draft'}]}
        self.save()

    def save(self):
        (self.root / 'tools/publishing/publications.json').write_text(json.dumps(self.data))

    def test_manifest_valid(self):
        self.assertEqual(pub.load_manifest(self.root), self.data)

    def test_public_excludes_draft(self):
        output, items = pub.stage(self.root)
        self.assertEqual(items, [])
        self.assertFalse((output / 'content/example.md').exists())
        self.assertEqual(output.name, 'public')

    def test_explicit_preview_keeps_status_and_source(self):
        before = self.source.read_bytes()
        output, items = pub.stage(self.root, True)
        text = (output / 'content/example.md').read_text()
        self.assertIn('DRAFT', text)
        self.assertIn('Vitalii Oborskyi', text)
        self.assertEqual(self.source.read_bytes(), before)
        self.assertEqual(items[0]['source_sha256'], pub.digest(self.source))
        self.assertEqual(output.name, 'preview')

    def test_published_in_public_output(self):
        self.data['articles'][0]['status'] = 'published'
        self.save()
        output, items = pub.stage(self.root)
        self.assertEqual(len(items), 1)
        self.assertNotIn('DRAFT', (output / 'content/example.md').read_text())

    def test_output_modes_are_separate(self):
        public, _ = pub.stage(self.root)
        preview, _ = pub.stage(self.root, True)
        self.assertNotEqual(public, preview)
        self.assertTrue((public / 'content/index.md').exists())

    def test_digest_tracks_changed_worktree(self):
        _, first = pub.stage(self.root, True)
        self.source.write_text('# Example\n\nChanged argument.\n')
        _, second = pub.stage(self.root, True)
        self.assertNotEqual(first[0]['source_sha256'], second[0]['source_sha256'])

    def test_duplicate_slug_rejected(self):
        self.data['articles'].append(copy.deepcopy(self.data['articles'][0]))
        self.save()
        with self.assertRaises(ValueError): pub.load_manifest(self.root)

    def test_unsafe_slug_rejected(self):
        self.data['articles'][0]['slug'] = '../escape'
        self.save()
        with self.assertRaises(ValueError): pub.load_manifest(self.root)

    def test_unknown_status_rejected(self):
        self.data['articles'][0]['status'] = 'verified'
        self.save()
        with self.assertRaises(ValueError): pub.load_manifest(self.root)

    def test_mutable_engine_ref_rejected(self):
        self.data['engine']['commit'] = 'main'
        self.save()
        with self.assertRaises(ValueError): pub.load_manifest(self.root)

    def test_source_traversal_rejected(self):
        self.data['articles'][0]['source'] = 'report/articles/../../../outside.md'
        self.save()
        with self.assertRaises(ValueError): pub.load_manifest(self.root)

    def test_symlink_source_rejected(self):
        self.source.unlink()
        self.source.symlink_to(self.root / 'outside.md')
        with self.assertRaises(ValueError): pub.load_manifest(self.root)

    def test_symlink_output_rejected(self):
        (self.root / 'outside').mkdir()
        (self.root / 'tools/publishing/_build').symlink_to(self.root / 'outside', target_is_directory=True)
        with self.assertRaises(ValueError): pub.stage(self.root, True)

    def test_unsupported_figure_fails_instead_of_disappearing(self):
        self.source.write_text('# Example\n\n```mermaid\ngraph TD; A --> B\n```\n')
        with self.assertRaises(ValueError): pub.load_manifest(self.root)

    def test_missing_author_rejected(self):
        self.data['articles'][0]['author'] = ''
        self.save()
        with self.assertRaises(ValueError): pub.load_manifest(self.root)

    def test_title_mismatch_rejected(self):
        self.source.write_text('# Wrong title\n')
        with self.assertRaises(ValueError): pub.stage(self.root, True)

    def test_blueprint_cannot_be_a_manuscript(self):
        target = self.root / 'report/articles/example.blueprint.md'
        target.write_text('# Example\n')
        self.data['articles'][0]['source'] = 'report/articles/example.blueprint.md'
        self.save()
        with self.assertRaises(ValueError): pub.load_manifest(self.root)

    def test_relative_link_rejected(self):
        self.source.write_text('# Example\n\n[An owner](../../GLOSSARY.md)\n')
        with self.assertRaises(ValueError): pub.load_manifest(self.root)

    def test_stale_outputs_removed_on_restage(self):
        output, _ = pub.stage(self.root, True)
        stale = output / 'pdf' / 'withdrawn.pdf'
        stale.parent.mkdir()
        stale.write_bytes(b'%PDF-stale')
        pub.stage(self.root, True)
        self.assertFalse(stale.exists())

    def test_tilde_mermaid_rejected(self):
        self.source.write_text('# Example\n\n~~~mermaid\nflowchart LR\n A-->B\n~~~\n')
        with self.assertRaises(ValueError): pub.load_manifest(self.root)


if __name__ == '__main__':
    unittest.main()
