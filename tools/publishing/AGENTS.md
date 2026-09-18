# Publishing implementation scope

[Root AGENTS.md](../../AGENTS.md) remains canonical. This file supplements its Article and publishing boundaries section for renderer code only. Read the [guide](README.md), manifest, changed implementation and tests before editing.

Keep canonical manuscript Markdown and evidence state read-only. Derive HTML/PDF into isolated ignored outputs. Public staging must exclude drafts; explicit previews retain their draft notice. Never make successful rendering a publication or source-verification decision.

Keep the Quartz source commit immutable and review dependency/engine changes explicitly. Do not copy UA doctrine, graph emitters, research registers or platform-specific scripts merely because the engine contains them. Limit candidate-executing CI to read-only pull_request jobs without deployment credentials.

Use small functions, standard-library Python orchestration and explicit subprocess argument arrays. Comment non-obvious invariants and failure boundaries rather than narrating syntax. Test both normal execution and rejection paths. A new supported Markdown feature requires representative HTML/PDF coverage; do not silently flatten unsupported figures or links.

Run offline tests, manifest validation, real Quartz/Chromium smoke builds and visual page inspection as applicable. Report each separately, including unavailable checks. Do not call primary-agent self-review independent confirmation.
