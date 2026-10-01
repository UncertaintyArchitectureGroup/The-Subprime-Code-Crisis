# Local Repository Intelligence adapter

## Authority and implemented subset

This is an informative local navigation adapter adapted from [UA RI architecture](https://github.com/UncertaintyArchitectureGroup/uncertainty-architecture/blob/345c8f50745e5fde1303d0d7952634f7899220c9/.github/REPOSITORY-INTELLIGENCE.md)
and producer pattern at that pinned revision. It is not a full UA RI transplant:
no graph view, impact traversal, trusted candidate/tested-merge comparison,
remote caches or live PR overlay are implemented. No measured productivity or
comprehension improvement is claimed; UA's evaluation remains its own evidence.

The local config explicitly maps concerns/query aliases to owning files. The
producer inventories all admitted local text paths, glossary headings, applicable
AGENTS scopes and configured source-registry rows before lookup. Lexical matches
are explainable candidates; read their owning text. Cross-repo links are navigation
only. In Subprime, the registry's evidence/audit/date fields are copied exactly,
never inferred or promoted.

## Bootstrap and use

Read root/nested instructions first. A connector-only agent can read the committed
surface and owning files at the inspected ref, but cannot claim to have run local
verification. Compare source/config/producer identities through actual retrieved
files if available; otherwise fall back to direct repository search. Live GitHub
PRs/reviews/checks/approvals must be fetched separately.

From the repository root (Python 3.11+ standard library only):

```bash
python3 tools/repository_intelligence.py --config governance/repository-intelligence-config.json build
python3 tools/repository_intelligence.py --config governance/repository-intelligence-config.json verify
python3 tools/repository_intelligence.py --config governance/repository-intelligence-config.json query 'ішью'
python3 -m unittest discover -s tests -p 'test_*.py'
```

The committed surface is [agent-context.json](repository-intelligence/agent-context.json).
Reuse it only for the verified same source state. Missing/stale/altered context
exits nonzero with a direct-reading fallback. Read complete inventories before
creating a new term or maintained owner. A miss, untranslated query or multiple
candidates is not proof of absence or authority.

## Identity and bounds

- Admitted text suffixes: Markdown, JSON, TOML, YAML, Python, CFF, TXT. Content
  hashes bind every represented input, including config, producer, docs and tests.
- Other files are inventory/existence-only; binary changes need separate artifact
  digest/rights checks. This adapter cannot verify a deck/PDF content edition.
- Git/build/cache directories and temporary Python/build files are excluded
  explicitly by the producer; the generated surface excludes itself.
- Addition/deletion/content changes invalidate the text projection. Config and
  producer changes also invalidate it. Generation is deterministic and atomic.
- Bounds: 5,000 represented files, 2 MB per text file, 50 MB total text.
  Exceeding bounds fails visibly; do not silently truncate inventories.
- Repository paths reject traversal and symlinks, including inside-root aliases.
  Markdown extraction supports fenced/indented examples and balanced single-line
  code spans. Comment-bearing multiline/unmatched code spans fail visibly as
  unsupported; use direct source reading rather than a partial inventory.
  Local execution is an ordinary reviewed developer operation, **not** trusted
  interpretation of an arbitrary PR snapshot. Never run candidate code to
  establish its own trusted comparison.

## Maintenance and cross-repository coordination

After any represented source/config/producer change, regenerate and verify before
committing. Tests and CI exercise freshness/path/input safety; they do not replace
content, editorial or independent review. This small component has no runtime
service and no external Python dependencies.

Keep the pinned upstream reference and Apache-2.0 notices in
[RI-NOTICE](../tools/RI-NOTICE.md). Upgrade by an issue/PR with a named need and
regression checks; manual synchronized patches are deliberate until a shared
package is justified. Future publication/migration harnesses remain
[personal #6](https://github.com/oborskyivitalii/oborskyivitalii/issues/6).
