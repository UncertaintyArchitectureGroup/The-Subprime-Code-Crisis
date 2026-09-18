#!/usr/bin/env python3
"""Render explicitly listed articles through a commit-pinned Quartz workspace.

Canonical Markdown and evidence state are read-only inputs. Network installation
is explicit (setup); build and PDF commands only use the installed workspace.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
import subprocess
import tempfile
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
REL = Path('tools/publishing')
SLUG = re.compile(r'[a-z0-9]+(?:-[a-z0-9]+)*\Z')
SHA = re.compile(r'[0-9a-f]{40}\Z')
UPSTREAM = 'https://github.com/UncertaintyArchitectureGroup/uncertainty-architecture.git'


def safe_path(root: Path, relative: str | Path) -> Path:
    """Reject traversal and symlinks, including symlinked ancestor directories."""
    root = root.resolve()
    part = Path(relative)
    if part.is_absolute() or '..' in part.parts or not part.parts:
        raise ValueError(f'Unsafe relative path: {relative}')
    result = root
    for component in part.parts:
        result = result / component
        if result.is_symlink():
            raise ValueError(f'Symlinks are not publication inputs or outputs: {result}')
    if not result.resolve().is_relative_to(root):
        raise ValueError(f'Path escapes repository: {relative}')
    return result


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def run(args: list[str], cwd: Path) -> None:
    subprocess.run(args, cwd=cwd, check=True)


def git_head(root: Path) -> str:
    result = subprocess.run(['git', 'rev-parse', 'HEAD'], cwd=root,
                            text=True, capture_output=True, check=False)
    return result.stdout.strip() if result.returncode == 0 else 'unavailable'


def load_manifest(root: Path) -> dict[str, Any]:
    data = json.loads(safe_path(root, REL / 'publications.json').read_text())
    if data.get('schema_version') != 1:
        raise ValueError('Unsupported publication manifest schema')
    engine = data.get('engine', {})
    if (not isinstance(engine, dict) or engine.get('repository') != UPSTREAM
            or not isinstance(engine.get('commit'), str) or not SHA.fullmatch(engine['commit'])):
        raise ValueError('Quartz must use the declared repository and an immutable commit')
    seen: set[str] = set()
    paths: set[str] = set()
    if not isinstance(data.get('articles'), list):
        raise ValueError('articles must be a list')
    for item in data['articles']:
        if not isinstance(item, dict):
            raise ValueError('Each article must be an object')
        slug = item.get('slug', '')
        if not isinstance(slug, str) or not SLUG.fullmatch(slug) or slug in seen:
            raise ValueError(f'Invalid or duplicate slug: {slug}')
        seen.add(slug)
        source = item.get('source', '')
        if not isinstance(source, str):
            raise ValueError('Manuscript source must be a path string')
        path = safe_path(root, source)
        if (not source.startswith('report/articles/') or path.suffix != '.md'
                or source.endswith('.blueprint.md') or source in paths):
            raise ValueError(f'Invalid or duplicate manuscript: {source}')
        paths.add(source)
        if not path.is_file():
            raise ValueError(f'Manuscript missing: {source}')
        if item.get('status') not in {'draft', 'published'}:
            raise ValueError('Article status must be draft or published')
        for field in ('title', 'author', 'description'):
            if not isinstance(item.get(field), str) or not item[field].strip():
                raise ValueError(f'Missing article {field}')
        # This initial transport supports text, GFM tables and code, not a silent
        # downgrade of figures, raw HTML, relative assets or Obsidian embeds.
        text = path.read_text(encoding='utf-8')
        if text.startswith('---\n') or text.startswith('+++\n'):
            raise ValueError('Keep rendition metadata in publications.json, not a second front matter')
        if re.search(r'^\s*(?:`{3,}|~{3,})\s*mermaid\b|!\[|!\[\[|<[A-Za-z/]', text, re.M):
            raise ValueError('Figures/HTML need a reviewed renderer extension before export')
        if re.search(r'\]\((?!https?://|#)[^)]+\)', text):
            raise ValueError('Manuscript links must be absolute HTTPS/HTTP or local headings')
    return data


def select_articles(data: dict[str, Any], include_drafts: bool) -> list[dict[str, Any]]:
    return [a for a in data['articles'] if include_drafts or a['status'] == 'published']


def stage(root: Path, include_drafts: bool = False) -> tuple[Path, list[dict[str, Any]]]:
    data = load_manifest(root)
    mode = 'preview' if include_drafts else 'public'
    output = safe_path(root, REL / '_build' / mode)
    content = safe_path(root, REL / '_build' / mode / 'content')
    if output.exists():
        # Refuse malicious output trees rather than following a symlink on cleanup.
        for child in output.rglob('*'):
            if child.is_symlink():
                raise ValueError(f'Symlink in staging directory: {child}')
        shutil.rmtree(output)
    content.mkdir(parents=True)
    selected = select_articles(data, include_drafts)
    rendered: list[dict[str, Any]] = []
    index = ['# The Subprime Code Crisis — articles', '',
             'Research manuscripts and their publication renditions.', '',
             'Preview — drafts are not approved report conclusions.' if include_drafts
             else 'Only explicitly published editions appear here.', '']
    for item in selected:
        source = safe_path(root, item['source'])
        source_bytes = source.read_bytes()
        metadata = {key: item[key] for key in ('title', 'author', 'description')}
        # Draft filtering happens before staging. The visible status is retained
        # in every preview; Quartz's default RemoveDrafts is not used to hide it.
        header = '---\n' + ''.join(f'{k}: {json.dumps(v, ensure_ascii=False)}\n'
                                      for k, v in metadata.items()) + '---\n\n'
        status = ('DRAFT — conceptual argument; independent review and evidence work pending.'
                  if item['status'] == 'draft' else 'Published edition')
        body = source_bytes.decode('utf-8')
        lines = body.splitlines(keepends=True)
        if not lines or lines[0].strip() != '# ' + item['title']:
            raise ValueError('Manuscript H1 must match the manifest title')
        banner = f'\n\n*{item["author"]}*\n\n> {status}\n\n'
        manuscript = header + lines[0].rstrip() + banner + ''.join(lines[1:]).lstrip()
        (content / f'{item["slug"]}.md').write_text(manuscript, encoding='utf-8')
        index.append(f'- [{item["title"]}]({item["slug"]}.md) — {item["status"]}')
        rendered.append({**item, 'source_sha256': hashlib.sha256(source_bytes).hexdigest()})
    (content / 'index.md').write_text('\n'.join(index) + '\n', encoding='utf-8')
    record = {'schema_version': 1, 'repository_commit': git_head(root),
              'mode': mode, 'engine': data['engine'], 'articles': rendered,
              'note': 'Source digests identify actual worktree bytes; a commit alone does not.',
              'tool_sha256': {p: digest(safe_path(root, REL / p)) for p in
                              ('publish.py', 'export-pdf.mjs', 'quartz.config.ts', 'quartz.layout.ts')}}
    (output / 'manifest.json').write_text(json.dumps(record, indent=2) + '\n')
    return output, rendered


def verify_engine(engine: Path, commit: str) -> None:
    if not engine.is_dir() or git_head(engine) != commit:
        raise ValueError('Run setup first; Quartz engine is absent or at the wrong commit')
    run(['git', 'diff', '--exit-code', 'HEAD', '--', '.',
         ':(exclude)quartz.config.ts', ':(exclude)quartz.layout.ts'], engine)


def setup(root: Path) -> None:
    data = load_manifest(root)
    engine = safe_path(root, REL / '_engine')
    commit = data['engine']['commit']
    if not engine.exists():
        engine.mkdir(parents=True)
        run(['git', 'init', '--quiet'], engine)
        run(['git', 'remote', 'add', 'origin', UPSTREAM], engine)
        run(['git', 'fetch', '--depth=1', 'origin', commit], engine)
        run(['git', 'checkout', '--detach', 'FETCH_HEAD'], engine)
    if git_head(engine) != commit:
        raise ValueError('Engine checkout does not match pin; remove _engine and run setup again')
    # Cached configs are deliberate overrides; all engine implementation and
    # dependency manifests must still match the pinned source commit.
    verify_engine(engine, commit)
    run(['npm', 'ci', '--no-audit', '--no-fund'], engine)
    run(['node', 'node_modules/playwright/cli.js', 'install', 'chromium'], engine)


def build(root: Path, include_drafts: bool = False) -> tuple[Path, list[dict[str, Any]]]:
    data = load_manifest(root)
    engine = safe_path(root, REL / '_engine')
    verify_engine(engine, data['engine']['commit'])
    before = {a['source']: digest(safe_path(root, a['source'])) for a in data['articles']}
    output, selected = stage(root, include_drafts)
    for name in ('quartz.config.ts', 'quartz.layout.ts'):
        target = safe_path(root, REL / '_engine' / name)
        shutil.copyfile(safe_path(root, REL / name), target)
    site = safe_path(root, output.relative_to(root) / 'site')
    # Quartz cleans its output. Reject symlinks before handing it that authority.
    if site.exists():
        for child in site.rglob('*'):
            if child.is_symlink():
                raise ValueError(f'Symlink in site output: {child}')
    # Quartz/globby honors ancestor .gitignore files. Render a disposable copy
    # outside the ignored _build tree; never relax repository ignore rules or
    # mutate the pinned engine just to expose generated input.
    with tempfile.TemporaryDirectory(prefix='subprime-quartz-') as temporary:
        render_input = Path(temporary) / 'content'
        shutil.copytree(output / 'content', render_input)
        run(['node', 'quartz/bootstrap-cli.mjs', 'build', '-d', str(render_input),
             '-o', str(site)], engine)
    validate_site(site, selected)
    for source, expected in before.items():
        if digest(safe_path(root, source)) != expected:
            raise RuntimeError(f'Canonical manuscript changed during build: {source}')
    return output, selected


def validate_site(site: Path, selected: list[dict[str, Any]]) -> None:
    # A zero-input Quartz build exits successfully. Require every intended page.
    for slug in ['index', *[item['slug'] for item in selected]]:
        page = safe_path(site, slug + '.html')
        if not page.is_file() or '<article' not in page.read_text(encoding='utf-8'):
            raise RuntimeError(f'Quartz omitted the required article page: {slug}')


def pdf(root: Path, include_drafts: bool = False) -> None:
    output, selected = build(root, include_drafts)
    if not selected:
        raise ValueError('No published articles; pass --include-drafts for an explicit preview')
    engine = safe_path(root, REL / '_engine')
    script = safe_path(root, REL / '_engine' / 'subprime-export.mjs')
    shutil.copyfile(safe_path(root, REL / 'export-pdf.mjs'), script)
    pdf_dir = safe_path(root, output.relative_to(root) / 'pdf')
    pdf_dir.mkdir(exist_ok=True)
    for item in selected:
        target = safe_path(root, pdf_dir.relative_to(root) / f'{item["slug"]}.pdf')
        run(['node', str(script), str(output / 'site'), item['slug'], str(target)], engine)
    for item in selected:
        if digest(safe_path(root, item['source'])) != item['source_sha256']:
            raise RuntimeError('Canonical manuscript changed during PDF rendering')


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('command', choices=('check', 'setup', 'stage', 'build', 'pdf'))
    parser.add_argument('--include-drafts', action='store_true', help='Use isolated preview output')
    args = parser.parse_args()
    try:
        if args.command == 'check':
            load_manifest(ROOT)
            print('Publication manifest and manuscript inputs: OK')
        elif args.command == 'setup':
            setup(ROOT)
        elif args.command == 'stage':
            print(stage(ROOT, args.include_drafts)[0])
        elif args.command == 'build':
            print(build(ROOT, args.include_drafts)[0])
        else:
            pdf(ROOT, args.include_drafts)
    except (OSError, ValueError, RuntimeError, subprocess.CalledProcessError) as exc:
        parser.exit(1, f'Publication error: {exc}\n')


if __name__ == '__main__':
    main()
