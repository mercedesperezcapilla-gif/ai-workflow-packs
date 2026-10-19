# Comparison 2026-10-14

rules.md v1; definitions.md v1; B minus A; GBP; tolerance 0.00

Process B includes absent counterpart positions in Unmatched. Process A calls these Missing. This is not label normalisation.

| Category | A count | A GBP | B count | B GBP | B minus A count | B minus A GBP | Record references |
|---|---:|---:|---:|---:|---:|---:|---|
| Matched | 21 | 30975000.00 | 21 | 30975000.00 | 0 | 0.00 | None |
| Unmatched | 1 | 200000.00 | 2 | 500000.00 | 1 | 300000.00 | R003 |
| Missing | 1 | 300000.00 | 0 | 0.00 | -1 | -300000.00 | R003 |
| Position difference | 1 | 2400.00 | 1 | 2400.00 | 0 | 0.00 | None |

## Record differences

### Category-definition difference

| record_id | Account | Instrument | What differs | Process A value | Process B value |
|---|---|---|---|---|---|
| R003 | SIM-003 | FIC-0003 | category | Missing | Unmatched |

### Record difference

| record_id | Account | Instrument | What differs | Process A value | Process B value |
|---|---|---|---|---|---|
| None | | | | | |


## Source references

- data/2026-10-14/process-a/summary.csv
- data/2026-10-14/process-a/detail.csv
- data/2026-10-14/process-b/summary.csv
- data/2026-10-14/process-b/detail.csv

Missing inputs: none. All four files validated and both summaries cross-checked.

## Unresolved questions

Are record differences caused by timing, mapping or source completeness? Confirm with the fictional process owner.
