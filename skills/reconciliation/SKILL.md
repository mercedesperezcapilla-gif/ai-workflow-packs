---
name: reconciliation
description: Reconcile two fictional process outputs for one date and explain every difference.
---

Run from the pack working folder. Read README.md and this skill's references/rules.md and references/definitions.md. Confirm the working folder's rules.md and definitions.md agree with these references; stop for any conflict. Ask which dated folder to compare if none is supplied.

Run python .claude/skills/reconciliation/scripts/compare.py data/2026-10-15, replacing the folder with the selected one. Check the exit status before reading a report. If Python is unavailable, stop and explain the setup needed.

If the script stops, quote its error and exit status. Do not draft a comparison or read an old report as this run's result. Ask for corrected input. Never change numbers, records, rules or code to make a run succeed.

On success, read this run's JSON and Markdown under reports/. Check source_folder matches the selected folder. Explain every difference as a definition or record difference, citing record_ids and both process values. Preserve counts, signed GBP amounts, category references and source paths exactly. Mark possible causes as unconfirmed; only the process owner can confirm them. Do not add amounts across categories.

Return report paths, exit status and a short explanation in chat. Only compare.py may write its derived reports. A person decides follow-up; send nothing.

The bundled script calculates; these instructions tell Claude how to run it and explain the result. The script uses the current working folder for inputs and reports. Keep the skill folder, script and reference rules together when reusing it. Adapt and test them together if rules change.
