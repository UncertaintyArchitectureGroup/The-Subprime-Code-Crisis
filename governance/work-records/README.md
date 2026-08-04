# Machine-readable work records

Each pull request must add exactly one TOML record in this directory. The record is the machine-readable counterpart to the human-readable pull request template and is validated by Repository Gate.

Required shape:

```toml
record_version = 1
title = "Short change title"
primary_flow = "Flow A-E or approved governance procedure"
human_decision = "Decision reference or Not applicable for strictly mechanical work"
independent_review = "Confirmed, Corrections required, Unresolved disagreement, or Review unavailable"

[changelog]
decision = "Updated" # or "Not required"
reason = "Specific reason"

[synchronization]
assessed_surfaces = ["history"]

[synchronization.non_applicable]
# surface = "Specific reason"
```

The changed-path classifier determines the minimum surfaces that must appear in `assessed_surfaces`. A surface may be assessed and then recorded as non-applicable with a specific reason. The record does not establish approval, verification, completion, or independent confirmation by itself.
