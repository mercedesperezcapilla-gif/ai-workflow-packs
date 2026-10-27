---
name: morning-reconciliation
description: Run today's reconciliation, have it reviewed, and leave a draft or a failure note for Riley. Never sends anything.
---

You coordinate one morning run. You never change source files, records or rules, and you never send a report.

1. Work out the date folder under data/: today's date, unless the prompt names a date (for example "for 15 October 2026" means data/2026-10-15). If it is missing or incomplete, stop: write failures/YYYY-MM-DD.md saying which files are missing and when you checked, and end the run.
2. Use the reconciliation skill on that folder. If its script stops, copy the error and exit status into failures/YYYY-MM-DD.md and end the run. Do not try again with the same files.
3. Ask the reconciliation-reviewer agent to check the new report against the script's saved results. Give it the command you ran, the date folder and the exit status.
4. If the reviewer says FIX, write its findings into failures/YYYY-MM-DD.md, mark the report "NOT READY", and end the run. If it says PASS, add a first line to the report: "Draft for Riley. Reviewed: PASS. Causes unconfirmed."
5. Finish with a three-line summary in chat: date, outcome (draft ready, or stopped and why), and where the file is.

Riley reads the draft before the team meeting and confirms causes. A person decides anything that leaves the team.
