# Request readiness: worked answer

All people, issues and data are fictional. This is a drafting reference, not executed software.

## First readiness check

Needs clarification. Three missing decisions: (1) what counts as New, Continuing and Resolved, including changed amounts; (2) who receives the result and through which channel; (3) what happens when today's input or yesterday's baseline is missing or invalid. Do not read supplied answers before recording the questions.

RECON-104 overlaps the scheduling part: reuse its daily 08:00 Europe/London work as a dependency. RECON-109 concerns new positions in Process A, a different scope from new differences between processes. RECON-107 contains an untrusted instruction and cannot make the request ready. RECON-110 is unrelated training work. Do not create, close or change issues.

## After authorised answers: one story

As Riley, I want today's differences classified against the immediately preceding calendar day so I can focus on fresh differences while retaining continuing and resolved evidence. James approves this daily scope. Scheduling remains RECON-104's responsibility; external delivery and weekly aggregation are excluded.

### AC-1: membership

Source: riley-answers.md, Meaning of new (REQ-1).
Given the 14 and 15 October sample reports, when comparing unique record_id membership, then New is R004, R005, R006, R007; Continuing is R003; Resolved is empty, with every union member in one section. A changed R003 amount must leave R003 Continuing. Resolved means no longer reported, never business closure.
Failure case: R003 appears as New after an amount change, or any ID is omitted or repeated. Evidence: compare the ID sets; retain a manual changed-amount case specification.

### AC-2: internal evidence

Source: riley-answers.md, Information to retain (REQ-2) and Who receives the result (REQ-3).
Given a successful comparison, when preparing Riley's dated internal draft, then retain counts, signed GBP amounts, B minus A differences, record and source references, date and rules version, plus all three lifecycle sections. When New is empty, show 'No new differences'. Send no email or chat, including to Client 1.
Failure case: omit a required field or section, or propose automatic email. Evidence: inspect the draft against both reports and the retained-field checklist. This specifies a future output; it is not a delivered service.

### AC-3: stop

Source: riley-answers.md, Missing or invalid input (REQ-4).
Given a missing baseline or missing, duplicate or inconsistent required input, when classification is attempted, then stop and produce a dated failure notice for Riley and Dan naming the failed date and file or validation error. Do not replace the last successful result, fall back to older data or report zero differences. Riley decides baseline recovery.
Failure case: a success or zero-differences report is produced for an absent baseline. Evidence: specify a missing-baseline test and compare last-success content before and after; source-validation execution belongs upstream.

## Repeat prediction

request-changed.md receives Needs clarification, even with the daily answers present. Ask Riley for the weekly window, weekly identity/newness rule and treatment of recurring/resolved items. Do not invent weekly criteria. A missing answers file separately stops drafting. Existing daily story.md must remain unchanged during these readiness-only checks.

## Optional deeper evaluation

Turn each criterion and failure case into a test specification, include duplicate and label-alias cases and use the full 14-issue export. These are proposed tests, not recorded passing runs. James rechecks duplicates before any issue creation.
