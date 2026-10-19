# Recorded runs

Actual local runs. No live automation claim.

## Tests

```text
test_clean_success (test_compare.ComparisonTests.test_clean_success) ... ok
test_duplicate_position_key (test_compare.ComparisonTests.test_duplicate_position_key) ... ok
test_duplicates_stop (test_compare.ComparisonTests.test_duplicates_stop) ... ok
test_expected_differences (test_compare.ComparisonTests.test_expected_differences) ... ok
test_label_normalisation (test_compare.ComparisonTests.test_label_normalisation) ... ok
test_missing_file_stop (test_compare.ComparisonTests.test_missing_file_stop) ... ok
test_population_and_tables (test_compare.ComparisonTests.test_population_and_tables) ... ok
test_precision_and_tolerance (test_compare.ComparisonTests.test_precision_and_tolerance) ... ok
test_summary_mismatch_stop (test_compare.ComparisonTests.test_summary_mismatch_stop) ... ok

----------------------------------------------------------------------
Ran 9 tests in 0.411s

OK

```

## data/2026-10-14

```text
python compare.py data/2026-10-14
OK 2026-10-14: 4 files validated; 1 record differences; reports/comparison-2026-10-14.md and .json
exit code: 0
```

## data/2026-10-15

```text
python compare.py data/2026-10-15
OK 2026-10-15: 4 files validated; 5 record differences; reports/comparison-2026-10-15.md and .json
exit code: 0
```

## data/2026-10-16

```text
python compare.py data/2026-10-16
STOP: Missing required file(s): process-b/summary.csv. No report written for this run.
exit code: 1
```

## extra/duplicates/2026-10-15

```text
python compare.py extra/duplicates/2026-10-15
STOP: Duplicate record_id: process-b/R002. No report written for this run.
exit code: 1
```

## extra/inconsistent-labels/2026-10-15

```text
python compare.py extra/inconsistent-labels/2026-10-15
OK 2026-10-15: 4 files validated; 1 record differences; reports/comparison-2026-10-15.md and .json
exit code: 0
```

## extra/summary-mismatch/2026-10-15

```text
python compare.py extra/summary-mismatch/2026-10-15
STOP: Summary-detail mismatch: process-a. No report written for this run.
exit code: 1
```
