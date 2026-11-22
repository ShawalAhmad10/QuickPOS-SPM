# QuickPOS — POS SaaS Landing Page

**CS4002 Fundamentals of Software Project Management | FAST-NUCES Chiniot-Faisalabad | Fall 2026**

> **Status (22 Nov 2026): the local PHP website is implemented, audited and published.** The verified `main` baseline passes GitHub Actions. Jira, sprint execution and independent review remain blocked on institutional access/approval.

QuickPOS is a **fictional** point-of-sale SaaS product showcased through a responsive, custom-designed **PHP landing page**. This is **not a working POS application**. The semester project assesses the resulting website plus genuine Scrum, GitHub workflow, Jira integration, automated PHP testing and CI evidence.

## Team and governance
- Actual student/project owner: **Shawal Ahmad**. Roll number has not yet been supplied for the final report.
- Approved Group ID: not yet supplied. The authorized provisional repository name is `QuickPOS-SPM`.
- Main GitHub: https://github.com/ShawalAhmad10
- Optional automation GitHub account: https://github.com/ShawalAhmad97 — controlled by the same person, not a separate enrolled member.
- GitHub repository: https://github.com/ShawalAhmad10/QuickPOS-SPM
- Jira project: not created because no Atlassian workspace is connected.
- Solo-group exception and alternate PR review arrangement: instructor approval not yet confirmed.

## Scope
Six sections: Navigation/Header, Hero, Features, Pricing, Contact, Footer. PHP POST validation for Name/Email/Message with meaningful errors and success. Responsive at 375px/768px/1280px. No database, payment gateway, authentication or live-email delivery.

## Stack
PHP 8.2+, HTML5, CSS3, minimal vanilla JS, free Jira, GitHub and GitHub Actions; no UI framework or paid dependency required.

## Run locally
```powershell
php -v
php -S localhost:8000 -t public
```
Open `http://localhost:8000`.

Run the dependency-free validation suite:

```powershell
php tests/run.php
```

Lint every PHP file locally:

```powershell
Get-ChildItem public,src,tests -Recurse -Filter *.php | ForEach-Object { php -l $_.FullName }
```

The application sets baseline CSP, clickjacking, MIME-sniffing and referrer headers. The valid contact flow uses a short-lived, hardened PHP session only for the one-time confirmation page; it does not send email or save submissions permanently.

## Continuous integration

`.github/workflows/ci.yml` runs on `main`, `feature/**`, `bugfix/**`, and pull requests targeting `main`. It uses Ubuntu and PHP 8.3, lints all PHP files and runs `php tests/run.php`.

- Latest verified baseline run: https://github.com/ShawalAhmad10/QuickPOS-SPM/actions/runs/45043988754
- Verified documentation PR run: https://github.com/ShawalAhmad10/QuickPOS-SPM/actions/runs/45044977813
- Workflow page: https://github.com/ShawalAhmad10/QuickPOS-SPM/actions/workflows/ci.yml

Current real PR: https://github.com/ShawalAhmad10/QuickPOS-SPM/pull/1 . It remains open for a legitimate instructor-approved review and is not counted as merged/reviewed evidence.

## Project documents
- `START_HERE.md` — operator sequence.
- `docs/PRD.md` / `docs/DESIGN.md` / `docs/ARCHITECTURE.md` — product/UX/engineering contract.
- `docs/JIRA_BACKLOG.md` / `docs/SPRINT_PLAN.md` / `docs/GITHUB_WORKFLOW.md` — management plan.
- `docs/REQUIREMENTS_MATRIX.md` / `docs/TEST_PLAN.md` / `docs/EVIDENCE_CHECKLIST.md` — quality and evaluation traceability.
- `docs/AGENT_HANDOFF.md` — truthful state between Claude and Codex.
- `docs/FINAL_TECHNICAL_AUDIT.md` — factual Task 1–16 acceptance status.
- `docs/SPRINT_1_REPORT.md` / `docs/SPRINT_2_REPORT.md` — future-dated execution templates; no invented outcomes.
- `docs/VIVA_PREPARATION.md` — live demonstration and explanation notes.
- `prompts/` — task-scoped, low-repetition agent prompts.

## Academic integrity
AI development is allowed, but the student must understand and demonstrate the code and workflow in the live viva. No invented human identities, synthetic peer reviews, fake sprints, fake PR history, or fabricated test results.

**Deadline:** December 10, 2026 at 11:59 PM PKT. **Official brief:** `docs/reference/CS4002_QuickPOS_Semester_Project_BCS9C_Fall2026.pdf`.
