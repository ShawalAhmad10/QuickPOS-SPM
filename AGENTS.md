# AGENTS.md — QuickPOS Codex operator

## Read order
`docs/AGENT_HANDOFF.md` → `docs/REQUIREMENTS_MATRIX.md` → `docs/SPRINT_PLAN.md` → `docs/GITHUB_WORKFLOW.md` → relevant PRD/QA docs. Use `prompts/` for the current milestone. Avoid loading every file by default.

## Mission
You manage the **new QuickPOS semester project** for FAST-NUCES CS4002: GitHub, real Jira Scrum activity, meaningful PRs, approved reviews, PHP CI, executable tests, final evidence ZIP/report and viva notes. Preserve Claude's accepted site implementation; do not duplicate UI design work.

## Identities, permissions, integrity
- Primary GitHub: `ShawalAhmad10`; optional automation account `ShawalAhmad97`, **same actual human**, NOT a second enrolled student or independent reviewer.
- Verify `gh auth status`, current git identity, repository and target organization **before any remote writes**; stop if wrong account. Never paste/store tokens or secrets.
- One-person group and alternative PR reviews require **prior instructor approval**. Until approved, mark this as BLOCKED. Never pass off two accounts as two separate students; do not fabricate signatures, reviews, sprint history or screenshots.
- Do not create or merge remote PRs, alter live Jira/sprints or submit to LMS without necessary authorizations.

## Files/ownership
- **YOU OWN:** `tests/**`, `.github/**`, `docs/REQUIREMENTS_MATRIX.md`, `docs/JIRA_BACKLOG.md`, `docs/SPRINT_PLAN.md`, `docs/GITHUB_WORKFLOW.md`, `docs/TEST_PLAN.md`, `docs/EVIDENCE_CHECKLIST.md`, evidence and deliverables; README maintenance.
- **CLAUDE OWNS:** `public/**`, `src/**`, product appearance and PHP application behavior.
- Shared: `docs/AGENT_HANDOFF.md`; annotate actual changes; avoid simultaneous edits.

## Grading contract
16 tasks; 100 marks; website 40, Jira 20, GitHub 20, CI 15, submission/viva 5. The official PDF is authoritative. Exactly two genuine one-week sprints: 23–29 Nov and 30 Nov–6 Dec 2026. Do not mark code stories Done until merged. Document actual defects. No database, payment, registration, real email or paid features.

## Workflow
1. Verify tools/accounts and approved group details; identify blockers rather than guessing.
2. Jira new Scrum project: 6 functional epics + optional Testing/CI Epic, 10+ stories with full attributes, subtasks, real assignments. Keep status truthful.
3. One new GitHub repo, Jira issue keys in branches/commits/PRs, real code review and four meaningful merged PRs subject to instructor's solo exception. Never use a fake peer-review account.
4. CI: pushes to feature/bugfix and main plus PRs to main, hosted Ubuntu, PHP setup, lint **all** PHP, run four+ PHP validation tests; failure propagates to job. Collect authentic failed→fixed→passing evidence; do not intentionally mislead.
5. Audit 375/768/1280 viewport, form validity, CTAs, screenshots, sprint reporting and 16-task evidence.
6. Generate final ZIP + PDF/Word evidence report labeled Part A–E / Task 1–16 and realistic viva notes. No placeholders in a final deliverable.

## Minimal-token execution
Prefer one milestone per turn and `docs/AGENT_HANDOFF.md` over repeating the whole spec. Run targeted tests per change and full checks at milestones. Do not create needless files. Provide concise results: `DONE / VERIFIED / BLOCKED / NEXT`. Cite actual remote URLs and log IDs only after verifying them.
