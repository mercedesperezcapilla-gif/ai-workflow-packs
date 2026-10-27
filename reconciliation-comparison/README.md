# Compare two reconciliation processes

All data is invented for Aster Vale Simulation. This local demonstration compares outputs from two reconciliation processes. Python 3.10 or later is required. No packages, credentials or network access are needed.

## Contents

- data/2026-10-14: a mostly clean case with an intentional definition difference.
- data/2026-10-15: realistic record and category differences.
- data/2026-10-16: deliberately missing Process B summary.
- extra/: duplicated records with inconsistent labels, a valid inconsistent-label case, and a summary-detail mismatch.
- definitions.md and rules.md: the calculation contract.
- compare.py and tests/test_compare.py: deterministic calculation and unittest checks.
- reports/: generated locally after a run; the download starts without reports.

## Run

Extract the input ZIP and open reconciliation-comparison in the Code tab. In the Code tab, ask Claude to run python compare.py data/2026-10-15.

For those who prefer a terminal, run these commands from reconciliation-comparison:

```text
python compare.py data/2026-10-15
python compare.py data/2026-10-14
python compare.py data/2026-10-16
python compare.py extra/duplicates/2026-10-15
python compare.py extra/inconsistent-labels/2026-10-15
python compare.py extra/summary-mismatch/2026-10-15
python -m unittest discover -s tests -v
```

Successful runs write reports/comparison-<date>.md and .json. Failed runs print STOP and return exit code 1. Check the current exit code before reading a report. Extra cases share a report date; run them individually.

## Ask Claude

Run the script for the chosen date. Read rules.md and definitions.md first. Explain only the calculated results, cite record_ids, distinguish definition differences from record differences, and suggest hypotheses clearly labelled as unconfirmed. Do not change numbers, source files or rules. If validation stops, explain the stop and ask the fictional owner for corrected inputs. Never fill gaps with invented values. A person reviews the findings and decides next steps.

Answers and recorded run evidence are in reconciliation-comparison-check.zip. Keep that ZIP and its extracted folder outside the project folder you give Claude. Public answers support practice, not a blind evaluation.

## Create your skill and reviewer

First do the job once with a prompt, following the role workflow page. Then ask Claude to save the procedure as a skill in .claude/skills/ and create a narrowly scoped reviewer in .claude/agents/. Read both before running them. The starter supplies inputs, existing code and planted errors, not finished skill or agent instructions.

Bundle a copy of compare.py in the skill's scripts/ folder and rules.md and definitions.md in references/. The bundled script must use the working folder, not its own scripts/ folder, as ROOT. Keep the original script unchanged. The script calculates; the skill tells Claude how to run it and explain the result.

Run the skill, then have the reviewer check the good output and extra/planted/ separately. Reviewers return PASS or evidence-backed FIX items in chat; the author corrects files. Keep the check pack outside this folder until checking. It contains reference skill and reviewer files plus expected-reviewer-verdicts.md. Start a fresh session if a newly created agent is not discovered.

A reviewer has no Edit or Write tool. Where Bash is allowed for checks, it can still write through commands: restrict parent-session command permissions to the stated checks. This is not an operating-system read-only sandbox.

Format references: https://code.claude.com/docs/en/skills and https://code.claude.com/docs/en/sub-agents.

## Core workflow

Do: compare 15 October. Reuse: save the skill with the bundled script and rules. Repeat: predict then compare 14 October; only R003 remains, with B Unmatched GBP 500000.00. Then 16 October must stop for process-b/summary.csv with report contents unchanged. Trust: create the read-only reviewer and check the good and planted reports. Setup is extra; Design your own is optional. Wider evaluation is optional.
