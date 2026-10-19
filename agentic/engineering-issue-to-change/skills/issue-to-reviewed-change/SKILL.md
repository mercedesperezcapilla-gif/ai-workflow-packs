---
name: issue-to-reviewed-change
description: Take one approved issue to a tested change with an independent review and a handover. Never commits, merges or deploys.
---

You coordinate one issue a person has approved for implementation. Work only on a branch or an isolated copy.

1. Confirm the issue has written acceptance criteria. If not, stop and ask for them: no criteria, no build.
2. Use the implement-to-acceptance skill: plan, wait for approval, implement only the agreed files, run the tests.
3. Ask the acceptance-reviewer agent to check every criterion and run the tests itself.
4. If FIX, correct only the listed points and review again. Stop after two unresolved rounds and hand over to a person.
5. Update the handover with files changed, real test results, reviewer verdict and anything unresolved.

No commits, merges, deploys or production credentials. A person accepts the change.
