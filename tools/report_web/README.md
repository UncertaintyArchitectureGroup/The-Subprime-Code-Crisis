# Subprime browser report

Owner: [Subprime #74](https://github.com/UncertaintyArchitectureGroup/The-Subprime-Code-Crisis/issues/74).
Author consumer: [author #116](https://github.com/oborskyivitalii/oborskyivitalii/issues/116).

Canonical Markdown stays in place. `publication.json` is an explicit allowlist and
route map, not a research-state registry. It currently selects 43 documents,
including three report parts, their appendices, evidence and protocols. The small
landing page quotes the existing repository description and explains edition
boundaries. Publication eligibility is distinct from scientific verification.

## Edit and preview

Requirements: Python 3.11+, Git, Node 22+, npm 10.9.2+. From the repository root:

```sh
python3 tools/report_web/report_web.py check
python3 -m unittest discover -s tests -p 'test_report_web.py' -v
python3 tools/report_web/report_web.py setup
python3 tools/report_web/report_web.py build
python3 tools/report_web/report_web.py verify --package tools/report_web/public/preview/package
node tools/report_web/projection-check.mjs
python3 -m http.server 8080 --directory tools/report_web/public/preview/package
```

Open `http://localhost:8080/subprime/`. Python's simple server is sufficient for
the index/assets; use `.html` for deep documents during this elementary preview,
or a static server that implements Pages' extensionless `.html` behavior. Actual
GitHub Pages routing/redirect/cache evidence is still required by the consumer.
Opening `index.html` directly as `file://` cannot exercise `/subprime/` resources.

`setup` is the explicit network/package-install step and executes pinned
third-party npm installation code. Its engine cache defaults outside this repo,
under `~/.cache/subprime-quartz/<commit>`. Set `SUBPRIME_QUARTZ_ENGINE` to select a
different dedicated cache. Do not share that mutable build workspace between
concurrent producer processes. HTML builds do not install browsers, run PDF
exports, invoke an author renderer or contact a production deployment API.

The renderer pin is UA commit `989fc1398fc221ffca4e1f7a141b2c03bfc7cfb3`, Quartz
4.5.2, the same inspected engine used by draft PR #46. We reuse its pinned engine
and lockfile, not the draft article, restricted article adapter or export toolchain.
Upstream Quartz (MIT), UA changes and dependencies retain their own notices;
new contributions here retain the repository's CC BY-SA 4.0 unless stated otherwise.
The payload includes Quartz's original MIT notice from the exact upstream
4.5.2 baseline and the pinned UA Apache-2.0 code license, with an explicit runtime
notice/source map. These are distinct from the report's CC BY-SA text license.
The manifest keeps final rights-inventory acceptance pending; copied licenses
do not imply that the independent/human rights gate has passed.
The author palette/system typography is selected from author main `ca70a66`;
no author runtime, scenes, template or copied author code is required.

## Rendering contract

The Python adapter parses canonical TOML without writing it. The Node preparation
step uses the pinned Markdown AST to change link destinations by source positions,
preserving prose, fences, code and Mermaid contents. It records the original
SHA-256 of every document. Local links resolve through the single route map;
unselected existing support files use explicit immutable GitHub source links.
Missing files/anchors and unlisted images fail visibly. Raw active HTML, unsafe
URL schemes and active Mermaid click/configuration directives are rejected.

GitHub headings/anchors, GFM tables, code and footnotes use Quartz's configured
transformers. Mermaid is the pinned Quartz client enhancement, which loads
Mermaid 11.4.0 from the explicitly recorded CDN module URL. Without JavaScript
or that network resource, diagram source remains readable as code; text and
navigation remain native HTML. External research links stay external. Math/YAML
source frontmatter and new active embeds need an explicit compatible extension
if introduced; they must not silently disappear. Current selected inputs have no
math markup requiring a renderer.

Only one small emitter extension handles explicitly selected directory indexes:
Quartz ContentPage otherwise skips them, while FolderPage would synthesize
unlisted pages. No upstream implementation is patched. The dedicated cache
receives only the adapter's declared config/layout/style/components/extensions.
The rest of the pinned engine and dependency manifests must remain unchanged.

Source modification is read from Git history, never staging mtimes. A shallow
checkout displays unknown rather than assigning the head date to every file.
Evidence review, integration audit and `Last verified` are projected verbatim
from the selected source metadata. Rendering never certifies them. No publication
date is invented. Preview pages are visibly marked and noindex; a clean public
candidate can be generated with `build --mode public`. Neither mode authorizes
external publication or resolves the editorial/research backlog.

## Package contract for the author consumer

Successful output is `public/<mode>/package/`:

- `subprime/`: the only mounted payload, including its scoped sitemap.
- `manifest.json`: schema version, repository/source SHA/tree, dirty-worktree
  disposition, optional Actions run/attempt, engine pin, adapter/input hashes,
  explicit pages/routes, source metadata and hashes, link/fallback graph,
  content license, external runtime, per-file SHA-256/bytes/MIME and payload digest.

The digest covers the canonical sorted file inventory, not a self-referential
manifest. Manifest/build evidence still needs authentication against the actual
repository/workflow/run in the author consumer. Local dirty previews cannot be
admitted as clean public candidates; a self-declared JSON hash is not provenance.
The adapter verifies generated pages, local output links/fragments/assets,
canonicals, indexing mode, search membership and source immutability. `verify`
rejects added/missing/changed files and mismatched inventory/digests. It is a
producer check, not the trusted author admission implementation.

CSS, pre/post scripts and search JSON use content-addressed `/_assets/` URLs
within the mount; source images use content-addressed `/media/` URLs. This removes
stable-filename dependency replacement for cached HTML. **The consumer still
must retain prior referenced immutable resources** for its declared recovery and
compatibility window, and test cached/open readers across updates, route removal
and component rollback on the actual host. No custom cache-control header,
instantaneous expiry or automatic browser security sandbox is assumed. Admitted
report JavaScript shares the author origin; it is trusted site code. Local
preferences use only `subprime.theme`; this adapter creates no cookies or service
worker. Analytics is disabled pending the scoped author-consumer decision.

Report document canonicals are extensionless without a trailing slash; directory
index routes end with `/`. Native `.html` host aliases are not independent
canonical editions. Never rename a public slug/anchor without an alias or an
explicit compatibility decision. The report is three parts with chapter anchors;
adding a file does not publish it until the allowlist is deliberately updated.

## Delivery, failure and recovery

The read-only `Report web package` workflow retains review packages for 14 days.
This is a CI review retention period, **not** the durable production recovery
strategy. It does not deploy Pages, send dispatches, modify DNS, create releases
or use author production credentials. Draft PR previews remain private review
artifacts. Main builds may also create a public candidate for separately admitted
selection. Source changes trigger the producer; PDF remains a separate #55 concern.

A failing generation is discarded before replacing the previous successful local
package. Fix the specific failure, rerun affected checks, obtain independent
review and select a new immutable source/package. Do not hand-edit HTML or source
statuses to satisfy rendering. The author publisher must compose the whole site,
preserve the report across author updates and retain its complete identity tuple.
PR #79's admitted content-release contract remains an unresolved prerequisite.

For rollback, the author owner selects a retained approved Subprime artifact and
composes it with the **current** author component through its existing serialized
publisher. Do not upload a partial report over the live domain or restore an old
whole-site package as if it were a component rollback. Missing/corrupt retained
inputs must fail before activation. Hosted/cached-reader/recovery acceptance and
real author-generation reuse cannot be claimed from a local producer build.

Upgrade the engine only through an owning issue/PR with the exact new commit,
dependency/license review, real-content compatibility and current render/link
checks. Do not move to Quartz 5 merely because newer documentation exists.
