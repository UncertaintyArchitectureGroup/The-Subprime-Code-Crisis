"""Bounded producer checks; real Quartz rendering runs in Report web package CI."""
import copy
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from tools.report_web.report_web import (
    ROOT, OWNER, canonical, digest, fingerprint, inventory, load_manifest, safe_path,
    setup, split_frontmatter, verify_package, verify_site,
)


class ReportWebTests(unittest.TestCase):
    def test_current_allowlist_has_no_article_drafts_or_governance(self):
        data = load_manifest(ROOT)
        self.assertEqual(len(data["pages"]), 43)
        self.assertEqual(sum(p["group"] == "Report" for p in data["pages"]), 3)
        self.assertFalse(any(p["source"].startswith(("governance/", "report/articles/")) for p in data["pages"]))

    def test_duplicate_and_traversal_routes_are_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / OWNER).mkdir(parents=True)
            data = load_manifest(ROOT)
            for p in data["pages"]:
                target = root / p["source"]
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_text("# Fixture\n")
            for a in data["assets"]:
                (root / a).parent.mkdir(parents=True, exist_ok=True)
                (root / a).write_bytes(b"fixture")
            for malicious in ["report/the-illusion", "../escape", "evidence", "report", "media"]:
                bad = copy.deepcopy(data)
                # Preserve index, so collision cases cannot pass merely because
                # an unrelated mandatory-homepage check rejects the fixture.
                bad["pages"][1]["slug"] = malicious
                (root / OWNER / "publication.json").write_text(json.dumps(bad))
                expected = "clean-URL collision or reserved route" if malicious in {"evidence", "report", "media"} else "Duplicate/invalid"
                with self.assertRaisesRegex(ValueError, expected):
                    load_manifest(root)

    def test_source_paths_reject_traversal_and_symlink(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "alias").symlink_to(root, target_is_directory=True)
            for path in ["../outside", "/absolute", "a//b", "a/./b", "alias/input", "a\\b"]:
                with self.subTest(path=path), self.assertRaises(ValueError):
                    safe_path(root, path)

    def test_toml_projection_preserves_states_and_body(self):
        text = '+++\nsource_ids = ["P-2026-01"]\nintegration_audit = "In progress"\nlast_verified = "—"\n+++\n\n# A\n\n```mermaid\nA --> B\n```\n'
        meta, body = split_frontmatter(text)
        self.assertEqual(meta["integration_audit"], "In progress")
        self.assertEqual(meta["last_verified"], "—")
        self.assertEqual(body, '# A\n\n```mermaid\nA --> B\n```\n')
        with self.assertRaises(ValueError):
            split_frontmatter("+++\nsource_ids = []")

    def test_resource_versioning_preserves_research_code_and_old_resources(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "static").mkdir()
            for file in ["index.css", "prescript.js", "postscript.js", "static/contentIndex.json"]:
                (root / file).write_text("{}")
            html = '<head><link rel="stylesheet" href="../index.css"/><script src="../prescript.js"></script><script>const fetchData = fetch("../static/contentIndex.json").then(d=>d.json())</script></head><article><code>"index.css"</code></article><script src="../postscript.js"></script>'
            (root / "page.html").write_text(html)
            resources = fingerprint(root, "/subprime/")
            output = (root / "page.html").read_text()
            self.assertIn('<code>"index.css"</code>', output)
            self.assertNotIn('href="../index.css"', output)
            for target in resources.values():
                self.assertIn(target, output)
                self.assertTrue((root / target.removeprefix("/subprime/")).is_file())
            old = root / resources["index.css"].removeprefix("/subprime/")
            self.assertEqual(old.read_text(), "{}")

    def fixture(self, root):
        (root / "_assets").mkdir()
        (root / "_assets/search.json").write_text(json.dumps({"index": {"title": "Fixture"}}))
        (root / "index.html").write_text('<head><link rel="canonical" href="https://vitaliioborskyi.ai/subprime/"/><meta name="robots" content="noindex, nofollow"/></head><article id="heading"><a href="#heading">Jump</a></article>')
        return {"mount": "/subprime/", "canonical_base": "https://vitaliioborskyi.ai/subprime/", "mode": "preview", "pages": [{"slug": "index", "route": "/subprime/"}], "resources": {"static/contentIndex.json": "/subprime/_assets/search.json"}}

    def test_real_output_validation_rejects_missing_page_bad_fragment_and_excluded_search(self):
        for defect in ["omitted", "fragment", "search", "extra", "escaping-resource"]:
            with self.subTest(defect=defect), tempfile.TemporaryDirectory() as tmp:
                root = Path(tmp)
                record = self.fixture(root)
                self.assertEqual(verify_site(root, record)["pages"], 1)
                if defect == "omitted":
                    (root / "index.html").unlink()
                elif defect == "fragment":
                    p = root / "index.html"
                    p.write_text(p.read_text().replace('href="#heading"', 'href="#missing"'))
                elif defect == "search":
                    (root / "_assets/search.json").write_text('{"private-draft": {}}')
                elif defect == "extra":
                    (root / "excluded.html").write_text("draft")
                else:
                    p = root / "index.html"
                    p.write_text(p.read_text() + '<script src="/author.js"></script>')
                with self.assertRaises(ValueError):
                    verify_site(root, record)

    def test_package_inventory_rejects_actual_added_changed_or_symlinked_files(self):
        for defect in ["changed", "added-payload", "added-root", "sibling-tree", "manifest-symlink", "root-symlink"]:
            with self.subTest(defect=defect), tempfile.TemporaryDirectory() as tmp:
                package = Path(tmp) / "package"
                root = package / "subprime"
                root.mkdir(parents=True)
                record = self.fixture(root)
                files = inventory(root)
                record.update(schema_version=1, files=files, payload_sha256=digest(canonical(files).encode()))
                (package / "manifest.json").write_text(json.dumps(record))
                self.assertEqual(verify_package(package)["pages"], 1)
                if defect == "changed":
                    (root / "index.html").write_text("changed")
                elif defect == "added-payload":
                    (root / "extra.txt").write_text("unexpected")
                elif defect == "added-root":
                    (package / "index.html").write_text("would replace the author root")
                elif defect == "sibling-tree":
                    (package / "outside").mkdir()
                    (package / "outside/secret.txt").write_text("unexpected")
                elif defect == "manifest-symlink":
                    original = package / "manifest.json"
                    external = Path(tmp) / "manifest.json"
                    original.rename(external)
                    original.symlink_to(external)
                else:
                    alias = Path(tmp) / "alias"
                    alias.symlink_to(package, target_is_directory=True)
                    package = alias
                with self.assertRaises(ValueError):
                    verify_package(package)

    def test_setup_validates_source_before_any_npm_execution(self):
        with tempfile.TemporaryDirectory() as tmp:
            with patch("tools.report_web.report_web.git", return_value="989fc1398fc221ffca4e1f7a141b2c03bfc7cfb3"), patch("tools.report_web.report_web.verify_engine", side_effect=ValueError("modified lockfile")) as verify, patch("tools.report_web.report_web.run") as execute:
                with self.assertRaisesRegex(ValueError, "modified lockfile"):
                    setup(Path(tmp))
                verify.assert_called_once_with(Path(tmp), require_dependencies=False)
                execute.assert_not_called()


if __name__ == "__main__":
    unittest.main()
