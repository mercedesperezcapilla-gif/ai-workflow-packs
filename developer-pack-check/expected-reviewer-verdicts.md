# Expected acceptance reviewer verdicts

Fictional worked practice. Keep this outside the working folder until checking.

## Good solution: PASS with scope evidence

src/lifecycle.ts in this check pack should pass all 15 tests. Check the REQ-1 and REQ-2 criteria and supplied safety infrastructure: ID-only sorted exclusive complete lists, changed amounts Continuing, immediate previous day, no-New sections, earlier sightings ignored, duplicate rejection and CLI failures without success output. Compare with the original starter to confirm only src/lifecycle.ts and the implementer's docs/handoff.md changed, apart from the lesson's explicitly allowed .claude skill and reviewer setup. If no history is available, state that scope could not be independently verified.

The untouched starter is deliberately incomplete: 12 Not implemented failures (7 REQ-1, 5 REQ-2) and 3 safety passes. Do not weaken tests.

## Planted candidate: FIX

Run npm run check-planted. It runs the same acceptance tests against extra/planted/lifecycle-planted.ts without changing src/ or fixtures. Expect nine passes, one EVAL-04 failure and five REQ-2 skips.

With eval-04-changed-r003-amount.json it wrongly gives New R003 to R007 and no Continuing IDs. REQ-1, EVAL-03 and EVAL-04 require R003 Continuing. same() compares whole JSON records, so changed amounts alter identity. Compare record_id membership only. Normal npm test checks src/ separately; npm run check-planted checks this alternative.

REQ-2 evidence: EVAL-04 flags R003 without changing identity; 15 October and EVAL-08 give None. Check either-side changes, sorted Continuing-only IDs, property-order independence, validation and CLI output. After REQ-1 alone, five REQ-2 failures are expected pending the second change.
