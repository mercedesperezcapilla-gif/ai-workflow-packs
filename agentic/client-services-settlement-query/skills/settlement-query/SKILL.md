---
name: settlement-query
description: Handle one approved settlement query: draft with the drafter agent, check with the reviewer agent, hand to the service owner.
---

You coordinate one query. Nothing is sent to a client.

1. Confirm the query file is in queries/approved/. If not, stop: only approved queries are handled.
2. Ask the settlement-query-drafter agent to draft a reply for that query.
3. Ask the settlement-query-reviewer agent to check the draft.
4. If FIX: ask the drafter to correct only the listed points, then review again. Stop after two rounds and mark the draft "NEEDS SERVICE OWNER".
5. If PASS, or if the draft says Escalate: move nothing, send nothing. Write a one-line entry to review-log.md (query, outcome, reviewer verdict, time) and tell the service owner in chat where the draft is.

The named service owner approves every reply and does the sending. This design needs an engineer to connect a real query queue; locally, you start it by hand on one file.
