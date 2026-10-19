# Decisions

Identity is record_id only. Values, fields, amounts, categories and row order are not identity. Include category-definition differences.

Use the immediately previous calendar day, including weekends. Never search older history. Stop on missing baseline and ask Riley for a baseline decision.

Fixtures are immutable. EVAL-04 is a report-level amount variant, not a claim that a source integration test ran. EVAL-11 repeats a grouped JSON record, rather than a Markdown field row.

Node 22.6 to 22.17 needs type stripping enabled: set NODE_OPTIONS=--experimental-strip-types before using the scripts. Node 22.18 or later runs them directly by default. No dependencies or install step.
