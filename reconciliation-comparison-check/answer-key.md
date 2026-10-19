# Answer key

Actual compare.py outputs for the wholly fictional Aster Vale Simulation. Differences are B minus A. All amounts are GBP, 2 dp. These public answers are worked practice, not a blind evaluation.

## data/2026-10-14

### Comparison 2026-10-14

rules.md v1; definitions.md v1; B minus A; GBP; tolerance 0.00

Process B includes absent counterpart positions in Unmatched. Process A calls these Missing. This is not label normalisation.

| Category | A count | A GBP | B count | B GBP | B minus A count | B minus A GBP | Record references |
|---|---:|---:|---:|---:|---:|---:|---|
| Matched | 21 | 30975000.00 | 21 | 30975000.00 | 0 | 0.00 | None |
| Unmatched | 1 | 200000.00 | 2 | 500000.00 | 1 | 300000.00 | R003 |
| Missing | 1 | 300000.00 | 0 | 0.00 | -1 | -300000.00 | R003 |
| Position difference | 1 | 2400.00 | 1 | 2400.00 | 0 | 0.00 | None |

#### Record differences

##### Category-definition difference

| record_id | Account | Instrument | What differs | Process A value | Process B value |
|---|---|---|---|---|---|
| R003 | SIM-003 | FIC-0003 | category | Missing | Unmatched |

##### Record difference

| record_id | Account | Instrument | What differs | Process A value | Process B value |
|---|---|---|---|---|---|
| None | | | | | |


#### Source references

- data/2026-10-14/process-a/summary.csv
- data/2026-10-14/process-a/detail.csv
- data/2026-10-14/process-b/summary.csv
- data/2026-10-14/process-b/detail.csv

Missing inputs: none. All four files validated and both summaries cross-checked.

#### Unresolved questions

Are record differences caused by timing, mapping or source completeness? Confirm with the fictional process owner.

## data/2026-10-15

### Comparison 2026-10-15

rules.md v1; definitions.md v1; B minus A; GBP; tolerance 0.00

Process B includes absent counterpart positions in Unmatched. Process A calls these Missing. This is not label normalisation.

| Category | A count | A GBP | B count | B GBP | B minus A count | B minus A GBP | Record references |
|---|---:|---:|---:|---:|---:|---:|---|
| Matched | 21 | 30975000.00 | 22 | 31475000.00 | 1 | 500000.00 | R005 |
| Unmatched | 2 | 700000.00 | 3 | 1200000.00 | 1 | 500000.00 | R003, R005, R007 |
| Missing | 1 | 300000.00 | 0 | 0.00 | -1 | -300000.00 | R003 |
| Position difference | 2 | 6000.00 | 1 | 2750.00 | -1 | -3250.00 | R004, R006 |

#### Record differences

##### Category-definition difference

| record_id | Account | Instrument | What differs | Process A value | Process B value |
|---|---|---|---|---|---|
| R003 | SIM-003 | FIC-0003 | category | Missing | Unmatched |

##### Record difference

| record_id | Account | Instrument | What differs | Process A value | Process B value |
|---|---|---|---|---|---|
| R004 | SIM-004 | FIC-0004 | quantity | 1000 | 1200 |
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


#### Source references

- data/2026-10-15/process-a/summary.csv
- data/2026-10-15/process-a/detail.csv
- data/2026-10-15/process-b/summary.csv
- data/2026-10-15/process-b/detail.csv

Missing inputs: none. All four files validated and both summaries cross-checked.

#### Unresolved questions

Are record differences caused by timing, mapping or source completeness? Confirm with the fictional process owner.

## data/2026-10-16

STOP: Missing required file(s): process-b/summary.csv. No report written for this run.

No validated totals or differences available. No report written for this run.

## extra/duplicates/2026-10-15

STOP: Duplicate record_id: process-b/R002. No report written for this run.

No validated totals or differences available. No report written for this run.

## extra/inconsistent-labels/2026-10-15

### Comparison 2026-10-15

rules.md v1; definitions.md v1; B minus A; GBP; tolerance 0.00

Process B includes absent counterpart positions in Unmatched. Process A calls these Missing. This is not label normalisation.

| Category | A count | A GBP | B count | B GBP | B minus A count | B minus A GBP | Record references |
|---|---:|---:|---:|---:|---:|---:|---|
| Matched | 21 | 30975000.00 | 21 | 30975000.00 | 0 | 0.00 | None |
| Unmatched | 1 | 200000.00 | 2 | 500000.00 | 1 | 300000.00 | R003 |
| Missing | 1 | 300000.00 | 0 | 0.00 | -1 | -300000.00 | R003 |
| Position difference | 1 | 2400.00 | 1 | 2400.00 | 0 | 0.00 | None |

#### Record differences

##### Category-definition difference

| record_id | Account | Instrument | What differs | Process A value | Process B value |
|---|---|---|---|---|---|
| R003 | SIM-003 | FIC-0003 | category | Missing | Unmatched |

##### Record difference

| record_id | Account | Instrument | What differs | Process A value | Process B value |
|---|---|---|---|---|---|
| None | | | | | |


#### Source references

- extra/inconsistent-labels/2026-10-15/process-a/summary.csv
- extra/inconsistent-labels/2026-10-15/process-a/detail.csv
- extra/inconsistent-labels/2026-10-15/process-b/summary.csv
- extra/inconsistent-labels/2026-10-15/process-b/detail.csv

Missing inputs: none. All four files validated and both summaries cross-checked.

#### Unresolved questions

Are record differences caused by timing, mapping or source completeness? Confirm with the fictional process owner.

## extra/summary-mismatch/2026-10-15

STOP: Summary-detail mismatch: process-a. No report written for this run.

No validated totals or differences available. No report written for this run.

## Evaluation table and traceability

| Requirement / case | Fixture or test evidence | Expected result | Decision owner |
|---|---|---|---|
| Clean run | data/2026-10-14; test_clean_success | Success; only R003 differs | Learner as fictional process owner |
| Record differences | data/2026-10-15; test_expected_differences | Success; R003, R004, R005, R006, R007 | Learner |
| Missing files | data/2026-10-16; test_missing_file_stop | STOP exit 1; missing process-b/summary.csv | Learner |
| Duplicates and inconsistent labels | extra/duplicates; test_duplicates_stop | STOP exit 1; repeated R002 in Process B, even with permitted aliases | Learner |
| Inconsistent labels alone | extra/inconsistent-labels; test_label_normalisation | Success; same totals and differences as 14 October; zero false label differences | Learner |
| Summary-detail mismatch | extra/summary-mismatch; test_summary_mismatch_stop | STOP exit 1; Process A Matched summary 30976000.00 versus detail 30975000.00 | Learner |
| Intentional definition differences | R003 on both valid dates | Missing to Unmatched; +1 and +300000.00 in B Unmatched; -1 and -300000.00 in B Missing | Learner |
| Duplicate position key | test_duplicate_position_key | STOP even when record IDs differ | Learner |
| Invalid precision and boundary | test_precision_and_tolerance | Reject NaN, Infinity, integers and 3 dp amounts; 0.01 exceeds zero tolerance | Learner |
| Population and readable reports | test_population_and_tables | 24 to 26 records per process; plausible valuations; two difference tables, absent-side values, escaped cells and unchanged machine schema | Learner |
| Unknown category | test_label_normalisation | Reject lower-case unmatched; no inferred alias | Learner |

## Measurement

Differences found: expected record IDs correctly identified divided by expected IDs. Targets: 1/1 on 14 October and 5/5 on 15 October. False matches: different IDs or changed identity fields silently treated as equal; target zero. Unexpected reported record IDs are false positives; target zero. Completeness: all 4 source files and all 4 summary categories must be present. A 3/4 file set stops. The expected per-category tables and full A/B records above are generated by the script rather than retyped.

Source CSV SHA-256 hashes were unchanged after tests and all runs. Archive contents and bytes were checked against the source folders. Record human review time in minutes and actual AI cost per attempt separately. Neither was measured here. The script makes no paid API calls; do not claim cost or time savings. A future blind evaluation needs fresh cases held by a human outside Claude's folder, with rules frozen before running. Hypotheses about timing, mappings and completeness remain unconfirmed.
