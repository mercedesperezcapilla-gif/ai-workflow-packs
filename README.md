# AI workflow packs

Practice packs for the three role workflows on [mercedeslab.ai](https://www.mercedeslab.ai/ai-for-your-role). In each one you do a real piece of work with Claude, turn it into a **skill** that does the job the same way every time, and create a **reviewer agent** that checks it. Then you watch the reviewer catch a planted error. A person decides what happens next.

All people, organisations, clients and records are fictional. Everything here is free and educational.

## The skills and agents

| What | File | What it does |
|---|---|---|
| Skill | [skills/reconciliation](skills/reconciliation) | Runs the comparison script on a date folder and explains every difference with its records. The script does the sums. |
| Reviewer agent | [agents/reconciliation-reviewer.md](agents/reconciliation-reviewer.md) | Read-only. Checks every figure against the script's results. PASS or FIX. |
| Skill | [skills/write-testable-requirements](skills/write-testable-requirements) | Checks a request is ready, then drafts a brief, stories and test cases. Never invents decisions. |
| Reviewer agent | [agents/requirements-reviewer.md](agents/requirements-reviewer.md) | Read-only. Checks every criterion is testable, sourced and has a failure case. |
| Skill | [skills/implement-to-acceptance](skills/implement-to-acceptance) | Plans, builds one agreed change, runs the tests and writes the handover. |
| Reviewer agent | [agents/acceptance-reviewer.md](agents/acceptance-reviewer.md) | Checks the change against every criterion and runs the tests, without editing. |
| Agentic designs | [agentic/](agentic) | Coordinator skills that chain a skill and a reviewer, for scheduled or approved runs, with a person deciding. |

To use one, copy it into your project's `.claude/skills/` or `.claude/agents/` folder. The workflows teach you to build your own first; these are the worked versions to compare with.


| Role | Workflow | Starter pack | Answer key |
|---|---|---|---|
| Business and operations | [Compare two reconciliation processes](https://www.mercedeslab.ai/workflows/reconciliation) | [reconciliation-comparison](reconciliation-comparison) | [reconciliation-comparison-check](reconciliation-comparison-check) |
| Product managers and BAs | [From a need to testable requirements](https://www.mercedeslab.ai/workflows/product-ba) | [product-ba-pack](product-ba-pack) | [product-ba-pack-check](product-ba-pack-check) |
| Developers and engineers | [Build and review one change](https://www.mercedeslab.ai/workflows/development-engineering) | [developer-pack](developer-pack) | [developer-pack-check](developer-pack-check) |

## How to use a pack

1. Follow the workflow page. It takes about 30 minutes, with a first result in about 10 to 12.
2. Download the starter pack (from the workflow page, or this repository) and open its folder in the Code tab of the Claude desktop app.
3. Keep the answer key **outside** that folder until step 6, so Claude can't read it while you work.

Each answer key has a `reference/` folder with a finished skill and reviewer agent to compare against yours, plus `expected-reviewer-verdicts.md`.

## What you need

A Claude Pro, Max or Team plan with the desktop app's Code tab. The operations pack needs Python 3.10 or later; the developer pack needs Node.js 22.18 or later. No coding: Claude runs the scripts and you review.

## Licence

MIT. Built by [Mercedes Perez-Capilla](https://www.mercedeslab.ai/about). Views are her own, not her employer's.
