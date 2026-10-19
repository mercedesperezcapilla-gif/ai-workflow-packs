# Acceptance criteria

REQ-1: compare consecutive calendar days by record_id only. Only today means New; both means Continuing; only yesterday means Resolved. Every union member appears once. Resolved does not mean business closure. Sort each list by ID for predictable output.

EVAL-01: New R004, R005, R006, R007; Continuing R003; Resolved empty. EVAL-03: zero false-new IDs. EVAL-04: changing R003 amounts leaves it Continuing. EVAL-08: unchanged differences on the next date give no New IDs, say No new differences, and retain all sections. EVAL-16: an earlier sighting on 13 October does not affect classification on 15 October against 14 October.

REQ-4: stop for missing or invalid JSON, duplicate record_id, or a baseline other than the immediately previous calendar day. EVAL-10: missing baseline, including first run, stops; Riley decides recovery. EVAL-11: duplicate R004 JSON objects are rejected. JSON already groups multiple differing fields into one record; these fields are legitimate.

CLI failures name the file (or, for a wrong-day baseline, both dates), exit 1 and produce no successful lists. No output files are overwritten. Source-level duplicate and summary-detail cases still require upstream tests; this local project cannot validate absent source CSVs.
