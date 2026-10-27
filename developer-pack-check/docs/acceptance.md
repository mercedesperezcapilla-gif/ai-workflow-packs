# Approved criteria

Given validated reports for consecutive calendar days, when classify(yesterday, today) runs, then partition the union of record_id values into sorted, exclusive, complete New (today only), Continuing (both) and Resolved (yesterday only) lists. Amounts, fields, kind and row order never determine identity. Resolved does not mean business closure. Reuse validateReport and reject any baseline other than the immediately preceding calendar day.

Evidence: EVAL-01 and EVAL-03 expect New R004 to R007, Continuing R003 and no Resolved IDs. EVAL-04 changes R003 amounts: it stays Continuing. EVAL-08 expects no New, Continuing R003 and no Resolved. EVAL-16 checks that earlier history cannot prevent a returning ID being New.

Existing infrastructure, not additional implementation work: report.ts validates dates, schema and duplicates; cli.ts loads inputs, prints all sections and 'No new differences', and stops on errors without success output. EVAL-10, EVAL-11 and CLI tests protect those behaviours. Missing baseline requires Riley's decision, no older fallback. Source CSV validation remains upstream; JSON cannot prove its referenced CSVs reconcile.

For REQ-1 implement classify() in src/lifecycle.ts. Keep all fixtures, tests and other source unchanged. Record concise evidence in docs/handoff.md.

## REQ-2: Changed since yesterday (approved)

Given validated reports for consecutive calendar days, changedContinuing(yesterday, today) returns sorted Continuing record IDs whose process_a or process_b values differ between days. Compare complete side values structurally, ignoring object property order. Metadata (kind, fields and row order) does not count. New and Resolved records are excluded. REQ-1 identity rules stay unchanged. Reuse validation and the immediately preceding calendar day guard.

Evidence: EVAL-04 gives R003, still Continuing. The 15 October report and EVAL-08 give None. The supplied CLI prints one extra line: Changed since yesterday: R003, or Changed since yesterday: None. It calculates both results before printing, so errors produce no success output.

Implement changedContinuing() in src/lifecycle.ts only. CLI wiring and tests are supplied. Keep fixtures, tests and other source unchanged.
