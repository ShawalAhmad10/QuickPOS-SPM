# QuickPOS evidence report — current draft

**Evidence cutoff:** 23 November 2026 (PKT)
**Repository:** https://github.com/ShawalAhmad10/QuickPOS-SPM
**Jira:** https://shawalahmad97.atlassian.net/jira/software/projects/QPOS
**Student:** Shawal Ahmad — 22F-3303 — BCS-9C
**Group description:** Approved Solo Project (student-reported; documentary proof not included)
**Submitted to:** Miss Maham Saleem

## Contributor and review disclosure

`ShawalAhmad10` is the primary account. `ShawalAhmad97` is controlled by the same person and is not a second student or independent reviewer. Four PRs are open with passing CI, but no qualifying approval or merge is claimed.

# Part A — Website development

## Task 1 — Product design and responsive UI — PASS locally

The accepted custom QuickPOS PHP landing page was verified at 375px, 768px and 1280px, with additional 320px and 1440px checks. Evidence is under `docs/evidence/website/`.

## Task 2 — Six required sections — PASS locally

Header/navigation, Hero, Features, Pricing, Contact and Footer are present. Internal links and CTA destinations were checked without changing the accepted appearance.

## Task 3 — PHP validation — PASS locally

The contact form validates required Name/Email/Message fields and email format on the server. Real error and success flows, normalization and output encoding were checked. The automated suite passes 13/13.

# Part B — Jira Scrum

## Task 4 — Jira backlog — VERIFIED setup

QPOS is a real Scrum project with 32 issues (QPOS-1–QPOS-32): 7 Epics, 15 Stories, 5 Tasks and 5 Subtasks. An authenticated isolated Jira UI session was unavailable, so readable backlog/Epic/two-story and sprint screenshots still remain; no simulated UI was created.

As of 23 November 2026, 14 issues are Done, 5 In Progress and 13 To Do. QPOS-32 is Done; QPOS-26 and QPOS-27 are In Progress. Sprint 1 contains 6 Done and 3 In Progress. QPOS-14 through QPOS-18 contain factual pre-sprint implementation and QA comments but remain To Do pending real Sprint 2 reverification.

## Task 5 — Two sprints — IN PROGRESS

Sprint 1 is active for 23–29 November 2026. Sprint 2 is planned for 30 November–6 December 2026. Neither sprint is falsely reported closed; final summaries remain future work.

## Task 6 — Bugs, reports and retrospectives — PARTIAL

Only genuine issue activity is recorded. Sprint reports and both retrospectives must be completed after the real sprint events.

# Part C — GitHub collaboration and Jira integration

## Task 7 — Repository and integration — VERIFIED

The public repository is live. Jira QPOS-23’s Development field exposes one open GitHub pull request, establishing actual integration.

## Task 8 — Jira-keyed branches and commits — VERIFIED

PR #2 uses QPOS-23, PR #3 uses QPOS-19 and PR #4 uses QPOS-24. The original completed source was retained as one truthful baseline instead of fabricated historical commits.

## Task 9 — PRs and reviews — BLOCKED

PRs #1–#4 are genuine and green. The report now includes a genuine four-PR capture. Same-owner AI-assisted review comments are labeled accurately and do not count as independent approvals. Their public permalink did not render in the isolated headless browser, so a readable review-discussion capture remains. No PR is merged. The prepared order is #2 → #3 → #4 → refreshed #1.

## Task 10 — Participation — BLOCKED

Solo-project approval is reported by the student. Documentary approval and the qualifying PR-review arrangement are not included.

# Part D — Tests and CI

## Task 11 — Workflow — PASS

GitHub Actions runs on main, feature/bugfix pushes and pull requests to main using Ubuntu and PHP 8.3. Stable main run: https://github.com/ShawalAhmad10/QuickPOS-SPM/actions/runs/45043988754

## Task 12 — PHP lint — PASS on open PR

PR #4 discovers every tracked `*.php` path and passes 17/17 files.

## Task 13 — PHP validation tests — PASS on open PR

The dependency-free runner passes 13/13, treats warnings/notices as failures and proves exact maximum-length fixtures.

## Task 14 — Failed→fixed CI — VERIFIED

The explicitly labeled controlled exercise failed truthfully at https://github.com/ShawalAhmad10/QuickPOS-SPM/actions/runs/45110283311 (13/14, nonzero). Corrective commit removed only the sentinel and https://github.com/ShawalAhmad10/QuickPOS-SPM/actions/runs/45110435088 passed. Genuine Actions captures for the failure, correction and current PR #1 passing run 45160271783 are under `docs/evidence/github/`. Main stayed green.

# Part E — Submission and viva

## Task 15 — ZIP and report — PARTIAL

The local integration-candidate ZIP, this Task 1–16 report and the rendered PDF use the confirmed academic identity. Final merge/sprint proof and the LMS receipt are still absent.

## Task 16 — Live viva — PARTIAL

Demonstration notes exist; the live evaluation has not occurred.

# Remaining blockers

1. Documentary solo-project approval if available and the qualifying PR-review arrangement.
2. Four legitimate reviews and authorized merges, then final main CI/Jira verification.
3. Real completion of both sprints, reports and retrospectives.
4. Authenticated Jira UI captures, a readable real GitHub review-discussion capture and the LMS submission receipt.
