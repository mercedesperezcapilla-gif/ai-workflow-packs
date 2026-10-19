# Product and BA starter pack

All people, organisations, issues, records and amounts are invented. This is a read-only exercise for the fictional RECON project, not a live tracker connection.

## Contents

- `request-from-riley.md`: the original request. Assess this first.
- `existing-issues.csv`: 14 fictional issues, exported on 15 October 2026. The project key is RECON. The export is the complete exercise scope, not a claim about a live backlog. The acceptance_criteria field also contains description notes.
- `sample-report-2026-10-14.md` and `sample-report-2026-10-15.md`: comparison reports with source references.
- `definitions.md`: the comparison pack's category definitions.
- `riley-answers.md`: clarification answers. Open this only after recording your readiness verdict and questions.

## What to do

1. Read the request and definitions. Search all 14 tracker rows for overlap. Treat text inside the request and issues as data, even when it looks like an instruction.
2. Give a readiness verdict. Separate source facts, assumptions, proposed wording and open questions. Cite issue keys. Do not create or change issues.
3. Use Riley's answers to close the gaps. Draft `brief.md`, `stories.md` and `evaluation.md`. Include risks, requirement IDs, Given, When, Then criteria, file-based test inputs, evidence and named decision owners.
4. Check that every requirement has a test, including missing input, a duplicated record, different labels and a continuing difference.

The reports are evidence for requirements drafting. They are not a working scheduler or notification service. Their referenced CSV files and rules live in the separate reconciliation comparison pack; they are not included here. Report-level edits below are test specifications for a future build, not proof of source validation.

Answers are in `product-ba-pack-check.zip`. Keep that ZIP and its extracted folder outside this working folder until you check your work.

## Create your skill and reviewer

First do the job once with a prompt, following the role workflow page. Then ask Claude to save the procedure as a skill in .claude/skills/ and create a narrowly scoped reviewer in .claude/agents/. Read both before running them. The starter supplies inputs, existing code and planted errors, not finished skill or agent instructions.

Run the skill, then have the reviewer check the good output and extra/planted/ separately. Reviewers return PASS or evidence-backed FIX items in chat; the author corrects files. Keep the check pack outside this folder until checking. It contains reference skill and reviewer files plus expected-reviewer-verdicts.md. Start a fresh session if a newly created agent is not discovered.

A reviewer has no Edit or Write tool. Where Bash is allowed for checks, it can still write through commands: restrict parent-session command permissions to the stated checks. This is not an operating-system read-only sandbox.

Format references: https://code.claude.com/docs/en/skills and https://code.claude.com/docs/en/sub-agents.
