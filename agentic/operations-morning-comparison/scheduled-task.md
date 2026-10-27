# Scheduled task: morning comparison

Set this up in the Claude desktop app (Code tab, scheduled tasks), pointed at your copy of the reconciliation pack, daily at 08:00 Europe/London, including weekends. That matches Riley's answer and RECON-104: every calendar morning.

**Task prompt**

> Use the morning-reconciliation skill for today. Do not send anything. Stop and leave a failure note if any file is missing or the review fails.

**Before you switch it on**

- Copy `skills/morning-reconciliation`, plus `skills/reconciliation` and `agents/reconciliation-reviewer.md` from the top of this repository, into the pack's `.claude/` folder.
- Test it by hand first. The pack's data is for 14 to 16 October 2026, so "today" will find nothing. In the Code tab, paste each of these and check the result:
  - "Use the morning-reconciliation skill for 15 October 2026." You should get a reviewed draft in `reports/`.
  - "Use the morning-reconciliation skill for 16 October 2026." A file is missing, so you should get a failure note in `failures/` and no new report.
  - "Use the reconciliation-reviewer agent to check extra/planted/comparison-2026-10-15-planted.md against reports/comparison-2026-10-15.json." You should get FIX.
- Then switch the schedule on. Its prompt keeps "today", so it only produces a draft on days that have a data folder.
- Scheduled tasks run only while the app is open and the computer is awake. A run can start late. It is a helper, not a guaranteed 08:00 service.
- Give it permission only to read the pack and write to `reports/` and `failures/`.
