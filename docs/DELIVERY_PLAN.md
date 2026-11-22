# Delivery, report and viva plan

The official brief requires **one source ZIP** and **one PDF or Word evidence report**. The report must label **Part A–E and Task #1–#16**, with readable screenshots and Jira/GitHub URLs. Repo and Jira must be accessible to evaluator. A recorded video is **not** required. Deadline 10 December 2026, 11:59 PM PKT.

## Report outline (produce after genuine evidence exists)
- Cover: QuickPOS, course, verified actual student/group identities, instructor, submission date.
- Executive synopsis: scope of the fictional POS landing page and how development was managed.
- Part A: Task 1 UI & responsive / Task 2 six sections / Task 3 POST validation — actual desktop and mobile screenshots, test cases.
- Part B: Task 4 Jira Epics/backlog / Task 5 Sprint 1+2 reports / Task 6 bugs, burndown or equivalent, retros.
- Part C: Task 7 GitHub repo/README/Jira integration / Task 8 branch+commit traceability / Task 9 four PRs and approved reviews / Task 10 honest contribution summary.
- Part D: Task 11 Actions YAML and triggers / Task 12 lint logs / Task 13 tests / Task 14 failed→fixed→passing run.
- Part E: Task 15 ZIP/report/access confirmation / Task 16 brief viva demo sequence.
- Appendix: links matrix, project run instructions, screenshot manifest.

## Source ZIP contents
Include PHP, HTML/CSS/JS, local assets, `src/`, tests, `.github/workflows/`, README, necessary docs. Exclude secrets, caches and unneeded dependencies. ZIP must open correctly, paths not nested accidentally, and instructions must match code.

## Viva demo run order (live, no faked state)
1. Local `php -S localhost:8000 -t public` → show desktop and mobile.
2. Navigation and CTA tests, invalid/valid contact form.
3. Jira 7 Epics, two detailed stories, sprint reports and retrospective.
4. GitHub repo → branch/commit/PR, show approved review, Jira link.
5. Actions → lint/tests, failed and passing run explanation.
6. Explain true personal involvement, AI use, solo approval and lessons learned.

## Final gate
Codex verifies no placeholders remain in final report, all URLs open, source ZIP matches verified main, genuine review arrangement satisfied, no secrets, no claim of LMS submission unless done.
