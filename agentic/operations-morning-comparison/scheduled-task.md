# Scheduled task: morning comparison

Set this up in the Claude desktop app (Code tab, scheduled tasks), pointed at your copy of the reconciliation pack, every weekday at 08:00.

**Task prompt**

> Use the morning-reconciliation skill for today. Do not send anything. Stop and leave a failure note if any file is missing or the review fails.

**Before you switch it on**

- Copy `skills/morning-reconciliation`, plus `skills/reconciliation` and `agents/reconciliation-reviewer.md` from the top of this repository, into the pack's `.claude/` folder.
- Click **Run now** on a good day, on a day with a missing file, and on the planted report. Check you get a draft, a failure note, and a FIX.
- Scheduled tasks run only while the app is open and the computer is awake. A run can start late. It is a helper, not a guaranteed 08:00 service.
- Give it permission only to read the pack and write to `reports/` and `failures/`.
