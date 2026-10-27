# One approved criterion: REQ-1

Given validated reports for consecutive calendar days, when classify(yesterday, today) runs, then partition the union of record_id values into sorted, exclusive, complete New (today only), Continuing (both) and Resolved (yesterday only) lists. Amounts, fields, kind and row order never determine identity. Resolved does not mean business closure. Reuse validateReport and reject any baseline other than the immediately preceding calendar day.

Evidence: EVAL-01 and EVAL-03 expect New R004 to R007, Continuing R003 and no Resolved IDs. EVAL-04 changes R003 amounts: it stays Continuing. EVAL-08 expects no New, Continuing R003 and no Resolved. EVAL-16 checks that earlier history cannot prevent a returning ID being New.

Existing infrastructure, not additional implementation work: report.ts validates dates, schema and duplicates; cli.ts loads inputs, prints all sections and 'No new differences', and stops on errors without success output. EVAL-10, EVAL-11 and CLI tests protect those behaviours. Missing baseline requires Riley's decision, no older fallback. Source CSV validation remains upstream; JSON cannot prove its referenced CSVs reconcile.

Implement only classify() in src/lifecycle.ts. Keep all fixtures, tests and other source unchanged. Record concise evidence in docs/handoff.md.
