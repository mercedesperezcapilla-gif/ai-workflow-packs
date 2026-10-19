# Expected comparison reviewer verdicts

Fictional worked practice. Keep this outside the working folder until checking.

## Good output: PASS

Require a successful python compare.py data/2026-10-15 run, source_folder data/2026-10-15 and exit 0. Markdown and JSON agree: B Unmatched GBP 1200000.00; B minus A GBP 500000.00; references R003, R005, R007. R003 is a category-definition difference; R004 to R007 are record differences. R004 quantity is 1000 versus 1200 and amount GBP 2400.00 versus 2750.00. Check every other row too. Causes remain open questions.

## Planted output: FIX

extra/planted/comparison-2026-10-15-planted.md has two deliberate defects:

1. Unmatched B GBP is 1250000.00 but JSON categories[1].process_b.amount_gbp is 1200000.00. Correct from the calculation, never change sources. The displayed delta also conflicts with this altered cell; that is a consequence of the same defect.
2. The quantity-difference row has an empty record_id. JSON record_differences identifies R004, quantity 1000 versus 1200. Account and instrument are not substitutes for the required reference.

## Stopped run

For data/2026-10-16, PASS requires exit 1 naming process-b/summary.csv and before/after evidence of no new or overwritten report. An earlier report is not a new result. Missing run evidence means FIX.

The reference skill invokes .claude/skills/reconciliation/scripts/compare.py from the working folder. It must produce the same JSON and Markdown as the original root compare.py on the same inputs. Do not run from the scripts/ folder.

The reference/ folder contains the worked skill and read-only reviewer. The reviewer has Read, Grep and Glob only; the caller supplies calculation and stop evidence.
