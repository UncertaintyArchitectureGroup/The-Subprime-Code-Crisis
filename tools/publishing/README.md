# Article and PDF renditions

This is a small Subprime-specific adapter around the Quartz engine already maintained in Uncertainty Architecture. It does not copy UA doctrine, research states, Repository Intelligence, platform-specific figure rewriting, or its agent-checkpoint machinery.

## Ownership and inputs

Read the root [AGENTS.md](../../AGENTS.md), then the scoped [AGENTS.md](AGENTS.md). Manuscripts and editorial blueprints live under [report/articles](../../report/articles/README.md). Markdown stays in place and is never an output target. [publications.json](publications.json) owns the rendition allowlist, author, title, description and distribution status; it is not an evidence-status registry.

The initial transport supports text, ordinary GFM tables and code. Figures, Mermaid, embedded HTML, relative assets and Obsidian embeds fail explicitly rather than silently becoming broken output. Supporting them requires a separately tested renderer extension. This is not the full UA publication package or a general exporter for the existing illustrated report.

## Commands

Requirements: Python 3.11+, Git, Node 22+ and npm 10.9.2+. Run from the repository root:

```sh
python3 tools/publishing/publish.py check
python3 -m unittest discover -s tests -p 'test_publication_pipeline.py' -v
python3 tools/publishing/publish.py setup
python3 tools/publishing/publish.py build
python3 tools/publishing/publish.py pdf --include-drafts
```

`setup` is the explicit network/dependency-install step. It fetches the exact UA commit in the manifest, installs that commit's npm lockfile with `npm ci`, and installs its Playwright Chromium. Installation executes third-party package installation code: use a disposable development environment or the read-only CI job. The pin is reproducible source selection, not a claim of a complete dependency security audit. A changed engine pin requires a fresh `_engine` workspace and compatibility review.

`build` includes only entries explicitly marked `published`. `--include-drafts` selects a separate preview tree and inserts a visible draft notice. `pdf` builds HTML first, then prints each selected article through Chromium. With no published entries, public PDF export fails clearly; it never silently includes drafts. `stage` prepares Markdown and the provenance manifest without installing Quartz or making network requests.

Outputs are isolated below `tools/publishing/_build/public/` or `_build/preview/`: `content/`, `site/`, `pdf/`, and `manifest.json`. Each mode is cleared before staging to prevent stale or withdrawn articles leaking into a later bundle. `_engine/` and `_build/` are ignored by Git. The source SHA-256, actual repository commit and engine commit are recorded; source digests describe actual worktree bytes, including uncommitted changes.

## Safety and publication boundary

The tool rejects path traversal, symlinked source/output paths, mutable engine references, unlisted articles and unsupported input features. It checks source digests after build and PDF export. PDF rendering permits only the local rendition server and data resources, and writes a checked temporary PDF before replacing its destination.

The workflow runs on `pull_request`, not privileged candidate execution through `pull_request_target`. It has read-only repository permissions and uploads review artifacts. It does not deploy GitHub Pages, create a release, publish externally, change source statuses or approve a manuscript. Public-mode output is not automatic publication authorization.

Before publishing an edition, review the argument and source use under the root protocol, record the maintainer's publication decision, and inspect every rendered PDF page. A nonempty PDF and green CI do not demonstrate acceptable typography, sound reasoning or independent review.

## Provenance and maintenance

The bootstrap and two-document drafting pattern are adapted from UA at commit `989fc1398fc221ffca4e1f7a141b2c03bfc7cfb3`. The same commit supplies the installed Quartz engine and lockfile. This adapter is an original Subprime implementation, not a copy of UA's research-specific PDF scripts. Upstream code and dependencies retain their own notices and licenses in the fetched checkout; the adapter does not relicense them. Do not distribute upstream font files as repository artifacts.

The upstream source is `https://github.com/UncertaintyArchitectureGroup/uncertainty-architecture`. Quartz's original project is `https://github.com/jackyzha0/quartz`. Subprime's existing license applies to new repository contributions unless a file explicitly states otherwise.
