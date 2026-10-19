# Comparison 2026-10-15

rules.md v1; definitions.md v1; B minus A; GBP; tolerance 0.00

Process B includes absent counterpart positions in Unmatched. Process A calls these Missing. This is not label normalisation.

| Category | A count | A GBP | B count | B GBP | B minus A count | B minus A GBP | Record references |
|---|---:|---:|---:|---:|---:|---:|---|
| Matched | 21 | 30975000.00 | 22 | 31475000.00 | 1 | 500000.00 | R005 |
| Unmatched | 2 | 700000.00 | 3 | 1250000.00 | 1 | 500000.00 | R003, R005, R007 |
| Missing | 1 | 300000.00 | 0 | 0.00 | -1 | -300000.00 | R003 |
| Position difference | 2 | 6000.00 | 1 | 2750.00 | -1 | -3250.00 | R004, R006 |

## Record differences

### Category-definition difference

| record_id | Account | Instrument | What differs | Process A value | Process B value |
|---|---|---|---|---|---|
| R003 | SIM-003 | FIC-0003 | category | Missing | Unmatched |

### Record difference

| record_id | Account | Instrument | What differs | Process A value | Process B value |
|---|---|---|---|---|---|
|  | SIM-004 | FIC-0004 | quantity | 1000 | 1200 |
| R004 | SIM-004 | FIC-0004 | amount_gbp | 2,400.00 | 2,750.00 |
| R005 | SIM-005 | FIC-0005 | category | Unmatched | Matched |
| R005 | SIM-005 | FIC-0005 | status | Open | Closed |
| R006 | SIM-006 | FIC-0006 | account | SIM-006 | Absent |
| R006 | SIM-006 | FIC-0006 | instrument_code | FIC-0006 | Absent |
| R006 | SIM-006 | FIC-0006 | category | Position difference | Absent |
| R006 | SIM-006 | FIC-0006 | quantity | 1000 | Absent |
| R006 | SIM-006 | FIC-0006 | amount_gbp | 3,600.00 | Absent |
| R006 | SIM-006 | FIC-0006 | status | Open | Absent |
| R007 | SIM-007 | FIC-0007 | account | Absent | SIM-007 |
| R007 | SIM-007 | FIC-0007 | instrument_code | Absent | FIC-0007 |
| R007 | SIM-007 | FIC-0007 | category | Absent | Unmatched |
| R007 | SIM-007 | FIC-0007 | quantity | Absent | 1000 |
| R007 | SIM-007 | FIC-0007 | amount_gbp | Absent | 700,000.00 |
| R007 | SIM-007 | FIC-0007 | status | Absent | Open |


## Source references

- data/2026-10-15/process-a/summary.csv
- data/2026-10-15/process-a/detail.csv
- data/2026-10-15/process-b/summary.csv
- data/2026-10-15/process-b/detail.csv

Missing inputs: none. All four files validated and both summaries cross-checked.

## Unresolved questions

Are record differences caused by timing, mapping or source completeness? Confirm with the fictional process owner.
