# Complete grading traceability matrix (official brief)

**Source:** `docs/reference/CS4002_QuickPOS_Semester_Project_BCS9C_Fall2026.pdf`. 100 marks in five parts. Status is **NOT STARTED** unless an actual source, test, screenshot or link is verified.

| Task | Marks | Requirement / done condition | Required evidence | Owner | Status |
|---|---:|---|---|---|---|
| A1: UI & responsive | 23 | Consistent polished customized UI, product mockup, works 375/768/1280 | Desktop full page + representative mobile screenshots | Claude | PASS: LOCAL VERIFIED |
| A2: Six sections | 7 | Header, Hero, Features, Pricing, Contact, Footer; working links/CTAs | Screenshots + live click-through | Claude | PASS: LOCAL VERIFIED |
| A3: PHP validation | 10 | Name/Email/Message POST; server required/email validation; errors/success; local docs | Valid/invalid form demonstration, source | Claude | PASS: LOCAL VERIFIED |
| B4: Jira setup | 7 | New Scrum, 6+ functional Epics, 10+ Stories with description, acceptance, priority, points, assignee, tasks/subtasks | Epics/backlog + 2 detailed stories | Codex | BLOCKED: NO JIRA CONNECTION |
| B5: Two sprints | 7 | Exactly 23–29 Nov and 30 Nov–6 Dec; goals, realistic estimates, execution and closures | Planning/backlog, active boards, completed sprint summaries | Codex | PARTIAL: PLANS ONLY |
| B6: Bugs/retro | 6 | Genuine defects only, progress/burndown or equivalent report, retros x2 | Bug history, reports, retros | Codex | NOT VERIFIED: FUTURE EVENTS |
| C7: Repo & integration | 5 | Shared repo, full source/README, Jira-GitHub linked issue, accessible main | Repo URL, README, linked Jira issue | Codex | PARTIAL: REPO LIVE, JIRA BLOCKED |
| C8: Branch/commits | 5 | Focused feature/bug branches with issue key, incremental linked commits, real member history | Branches, commits, Jira links | Codex | PARTIAL: REAL BRANCH, NO JIRA KEYS |
| C9: PR/reviews | 7 | >=4 meaningful merged PRs; under normal team >=2 per student and other member reviews, feedback and CI | Four PR links/screenshots and real reviews | Codex + approved reviewer | BLOCKED: 1 OPEN PR; REVIEW APPROVAL NEEDED |
| C10: Balanced participation | 3 | Genuine contributions/understanding from approved member(s) | Accurate work division and contributions | Student | BLOCKED: SOLO APPROVAL |
| D11: CI workflow | 4 | Workflow in `.github/workflows`, feature/bug pushes and main PRs, passing main | YAML + Actions completed run | Codex | PASS: RUN 45043988754 |
| D12: PHP syntax lint | 3 | Lint all relevant PHP, errors fail job | YAML step, passing logs, optionally failure logs | Codex | PASS: 17 FILES |
| D13: PHP tests | 5 | >=4 executable cases: empty name, invalid email, empty message, valid; fails on assertions | `tests/`, command + CI logs | Codex | PASS: 13 TESTS |
| D14: CI fail/fix | 3 | Real failed development run, corrected run, stable main | Failed + passing URLs/screenshots, fix explanation | Codex | NOT VERIFIED: NO FAILURE OBSERVED |
| E15: ZIP/report | 2 | Source ZIP, PDF/Word evidence report with Parts A–E and Tasks 1–16, URL/access | Final real files, submission channel | Codex | PARTIAL: DRAFT ARTIFACTS IN PROGRESS |
| E16: Viva | 3 | Live PHP demo, Jira, PR, CI; everyone approved can explain work | Actual live evaluation (no recorded video) | Student | PARTIAL: PREPARATION ONLY |

## Totals
A 40 / B 20 / C 20 / D 15 / E 5 = **100 marks**. Original marking scheme further splits A1 into 15 visual + 8 responsive.

## Mandatory academic authorization
One-person groups permitted only with **prior approval**, with agreed contribution and review arrangements. Two accounts used by one person do **not** satisfy two actual students. Do not self-certify C9/C10 complete without documented exception.

## Evidence rules
- Each completed row needs an actual link/file/screenshot with creation date in `docs/EVIDENCE_CHECKLIST.md`.
- Never fill screenshots or links from assumptions.
- Keep failed test runs and real bug resolution links; don't manufacture history.
- Report unresolved gaps even if the code looks complete.
