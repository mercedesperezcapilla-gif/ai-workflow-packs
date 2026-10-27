# Riley's clarification answers

All names and decisions in this exercise are fictional. These are answers given after the initial readiness check, not facts supplied by the original request.

## Meaning of new

REQ-1: Compare today's validated report with the immediately preceding calendar day's validated report. Use stable record_id as the difference identity. A record is New when it appears in today's Record differences and not yesterday's. It is Continuing when it appears in both, even if its values or differing fields have changed. It is Resolved when it appears only yesterday. Resolved means the difference is no longer reported, not that the business position has been closed. Keep the three lists separate. Flag only New for fresh attention; do not hide Continuing or Resolved. A record returning after an absent day is New again. Do not use amounts, category totals or row order as identity.

## Information to retain

REQ-2: Retain today's category counts, signed GBP amounts, B minus A differences, record references, source references, comparison date and rules version. Keep each record's kind, differing fields and both process values as supplied. The reports group field rows under Category-definition difference or Record difference; group rows by record_id for lifecycle membership, not one item per field row. Preserve Absent for a missing process side. Preserve the previous record evidence for Resolved entries. Keep category-definition differences visible. An accepted label alias alone must not create a difference; the Missing versus Unmatched definition difference must remain visible. Do not infer the cause of any break or add amounts across categories.

## Who receives the result

REQ-3: Riley is the sole pilot recipient and operations decision owner. Place a dated internal draft report in the pilot review folder for Riley to inspect before the 08:30 team meeting. No email, chat delivery or external distribution in this increment. James owns scope approval; Dan owns implementation and technical failure investigation. A successful report with no New records must say 'No new differences' and still show Continuing and Resolved.

## Missing or invalid input

REQ-4: Both days must be validated and present. If any required source file is missing, duplicated records are found, or summary and detail disagree, stop classification and produce a dated failure notice in the same review folder for Riley and Dan. Name the failed date, missing file or validation error. Do not report zero differences, resolve yesterday's differences, reuse an older baseline or replace the last successful result. Missing yesterday's report, including the first run, also requires a stop and an explicit baseline decision from Riley. A report's 'validated' text is not a substitute for checking its inputs in the implementation.

## Existing work, scope and timing

REQ-5: RECON-104 already owns the daily 08:00 Europe/London scheduled run, including daylight saving changes. Reuse it as a dependency, not a second scheduling story. The pilot runs every calendar morning, including weekends. The New column was only a suggestion; separate sections are fine. RECON-109 is about new positions within Process A, not new differences between Process A and B. Leave it separate. Before any issue is created, James must recheck the backlog and approve the exact proposed issue and dependency. The export stays read-only.

REQ-6: The pilot target is 4 December 2026, conditional on James accepting scope and RECON-104 being available. Riley accepts it only when the evaluation cases pass, every difference record belongs to exactly one lifecycle section, no continuing record is flagged New, and all required evidence is retained. The measured false-new count for the supplied two-day pair must be zero. Record failed cases and unresolved risks; do not claim an unattended service has been delivered by this exercise. A runtime, monitoring and recovery design are Dan's implementation work before a pilot is enabled. Live tracker writes, business record changes and automatic exception closure are excluded.
