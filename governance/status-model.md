# Source status model

This playbook is a mandatory procedural extension of [`AGENTS.md`](../AGENTS.md) for Flows A–D. `AGENTS.md` is canonical and has precedence; resolve conflicts in its favor. Read it in full before this playbook.

## Independent dimensions

Every source has two independent states in `evidence/SOURCES.md`. Evidence review determines whether the source itself has been understood and documented accurately. Integration audit determines whether every repository use is accurate and synchronized. Neither state implies the other.

### Allowed Evidence review statuses

- `Registered`
- `Brief in progress`
- `Reviewed brief`
- `Needs re-review`

### Allowed Integration audit statuses

- `Not started`
- `In progress`
- `Corrections required`
- `Verified`
- `Needs re-verification`

No other values are allowed.

## Last verified

`Last verified` contains `YYYY-MM-DD` only when `Integration audit = Verified`. For every other integration status it must be `—`. The brief and registry must show the same final status and date.

## Transition rules

### Flow A — new source

1. Registration: `Evidence review = Registered`; `Integration audit = Not started`; `Last verified = —`.
2. Start evidence review: `Evidence review = Brief in progress`; integration remains `Not started`; date remains `—`.
3. Complete evidence review: `Evidence review = Reviewed brief`; this does not complete integration.
4. Start audit: `Integration audit = In progress`; date remains `—`.
5. Defects remaining: `Integration audit = Corrections required`; date remains `—`.
6. Only after corrections are merged, all completion checks pass, and independent review is `Confirmed`: `Integration audit = Verified`; populate `Last verified`.

### Flow B — legacy registered source

Confirm identity and existing states without creating a duplicate. If no current reviewed brief exists, follow the evidence-review transitions above. Keep integration `Not started` until the audit begins, then use the audit transitions above. Do not preserve or invent a verification date for an unverified state.

### Flow C — changed or superseded source

Immediately set `Evidence review = Needs re-review`, `Integration audit = Needs re-verification`, and `Last verified = —`; record the new version and preserve version history. When re-review starts, use `Brief in progress` while integration remains `Needs re-verification`. After the brief is complete, set `Reviewed brief`; when the complete re-audit starts, set integration to `In progress`. Restore `Verified` and its date only after the new version is fully processed, all corrections are merged, and independent review is `Confirmed`.

### Flow D — changed repository content

When the source is unchanged but relying repository content changes materially, keep `Evidence review = Reviewed brief` unless the brief is inadequate; set `Integration audit = Needs re-verification` and `Last verified = —`. If the brief is inadequate, route its evidence-review state through the applicable re-review work rather than assuming adequacy. Start the affected-source audit with `In progress`; use `Corrections required` for unresolved defects; restore `Verified` only after changed repository state is checked, merged, synchronized, and independently `Confirmed`.

## Prohibition on inferred verification

A citation, reviewed brief, corrected paragraph, completed or merged PR, prior verification, plausible result, or status in another artifact does not establish `Verified`. `Verified` is prohibited unless the applicable flow and audit completion conditions pass and independent review is `Confirmed`. `Review unavailable` and `Unresolved disagreement` never equal `Confirmed`.
