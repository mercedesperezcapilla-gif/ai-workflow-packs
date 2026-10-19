---
name: implement-to-acceptance
description: Implement the bounded lifecycle requirement against acceptance criteria and record actual test evidence.
---

Read AGENTS.md and docs/. Plan against every criterion in docs/acceptance.md with the matching EVAL case and any ambiguity. Show the plan in chat, not in a file, and wait for approval. Stop for unresolved business decisions.

After the reader approves the plan, implement src/lifecycle.ts only. Keep fixtures and existing tests unchanged. Identity is record_id only; use the immediately preceding calendar day. Changed amounts never mean a new identity. Scheduling and upstream CSV validation are outside this job.

Run npm test from the pack root and report actual exit status and case results, including failures. Inspect the diff; if the folder has no git history, compare with the original download and say so. Ask acceptance-reviewer to check every criterion and run tests independently. Supply the criteria, changed-file scope and test command, not a preselected verdict.

Correct supported findings within scope and rerun tests. At most two implementation and review cycles; escalate unresolved findings to a person.

Update docs/handoff.md yourself: files changed, test evidence, findings and resolutions, unresolved limits, next action and source revision. The reviewer returns findings in chat and never edits. Do not commit, merge, publish or enable a pilot. A person accepts the change.
