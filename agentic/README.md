# Agentic designs: the agent files

The four designs on [mercedeslab.ai/workflows/agentic](https://www.mercedeslab.ai/workflows/agentic), as files you can copy into a project's `.claude/` folder. Each one has a **coordinator skill** that runs the job, calls a **reviewer agent**, stops on bad input and hands the decision to a person. Nothing here sends, publishes, merges or deploys.

| Design | Coordinator | Also uses (from the top of this repo) | Starts by |
|---|---|---|---|
| [Operations: morning comparison](operations-morning-comparison) | `morning-reconciliation` skill, plus [scheduled-task.md](operations-morning-comparison/scheduled-task.md) | `skills/reconciliation`, `agents/reconciliation-reviewer.md` | A scheduled task at 08:00 |
| [Client services: settlement query](client-services-settlement-query) | `settlement-query` skill, with its own drafter and reviewer agents | none | You, on one approved query (a live queue needs an engineer) |
| [Product: change-request triage](product-change-request-triage) | `change-request-triage` skill | `skills/write-testable-requirements`, `agents/requirements-reviewer.md` | James approving a request |
| [Engineering: issue to reviewed change](engineering-issue-to-change) | `issue-to-reviewed-change` skill | `skills/implement-to-acceptance`, `agents/acceptance-reviewer.md` | A person approving one issue |

**How to try one:** start with its role workflow on the site, so you have the pack and know the skill and reviewer work. Then copy the coordinator (and any agents) into the same `.claude/` folder and ask Claude to use the coordinator skill. Test a good case, a bad input and the planted error before you schedule anything.

These are fictional designs for learning, not deployed systems. The client services design has no practice pack yet: it shows the agents and the rules.
