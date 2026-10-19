# Definitions v1

Aster Vale Simulation is a wholly fictional firm. Every account, position and amount is invented. These are simplified process outputs, not employer or client data.

Each date compares the same intended position population. A missing output row is an issue to investigate, not proof that the underlying position does not exist. record_id is stable across the processes and dates.

| Category | Process A | Process B |
|---|---|---|
| Matched | Both sides agree under the process rules | Same |
| Unmatched | Both sides exist but matching has not succeeded | Includes both unsuccessful matching and an absent counterpart |
| Missing | Counterpart position is absent | Not used; absent counterparts are included in Unmatched |
| Position difference | Matched identity with a quantity or valuation difference | Same |

The R003 Missing to Unmatched movement is an intentional category-definition difference. It must remain visible. Only a category-only A Missing to B Unmatched movement with otherwise identical fields is classified automatically as this definition difference. All other movements require review.

amount_gbp is the signed position valuation for Matched, Unmatched and Missing. For Position difference it is the signed valuation break. quantity follows the same convention: position units or units of break. Amounts must not be added across categories as an economic exposure measure. Status is Closed for Matched and Open for all exception categories.
