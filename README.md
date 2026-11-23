# QuickPOS — POS SaaS Landing Page

**CS4002 Fundamentals of Software Project Management | FAST-NUCES Chiniot-Faisalabad | Fall 2026**

> **Verified 23 November 2026:** the accepted PHP website is published; `main` is green; Jira project QPOS has 32 issues and Sprint 1 is active. Four genuine PRs are open and green, but none is merged because the required instructor-approved solo review arrangement is still unconfirmed.

QuickPOS is a responsive PHP marketing site for a fictional point-of-sale SaaS product. It is not a working POS backend. The project demonstrates the six required page sections, server-side contact validation, automated tests, GitHub Actions, Jira Scrum activity and evidence-backed engineering workflow.

## Team and governance

- Student/project owner: **Shawal Ahmad**. Roll number and approved Group ID have not been supplied.
- Primary GitHub account: `ShawalAhmad10`.
- `ShawalAhmad97` is controlled by the same person and is not a second student or independent reviewer.
- Repository: https://github.com/ShawalAhmad10/QuickPOS-SPM
- Jira project: https://shawalahmad97.atlassian.net/jira/software/projects/QPOS
- Solo-group and alternative-review approval: not yet evidenced; all PRs therefore remain open.

## Scope

Navigation/Header, Hero, Features, Pricing, Contact and Footer; PHP POST validation for Name/Email/Message; responsive layouts at 375px, 768px and 1280px. No database, payments, registration, authentication, real email or paid features.

## Run and verify locally

```powershell
php -S localhost:8000 -t public
php tests/run.php
$files = git ls-files '*.php'
foreach ($file in $files) { php -l $file }
```

The hardened test runner treats PHP warnings/notices as failures and includes exact maximum-length boundaries. The application uses output encoding, input normalization, baseline security headers and short-lived hardened session cookies for the one-time confirmation page.

## Continuous integration and pull requests

`.github/workflows/ci.yml` runs on `main`, `feature/**`, `bugfix/**` and pull requests to `main`. It uses Ubuntu and PHP 8.3, discovers every tracked PHP file, fails on lint errors and runs the 13-case validation suite.

- Stable main run: https://github.com/ShawalAhmad10/QuickPOS-SPM/actions/runs/45043988754
- Controlled failed run: https://github.com/ShawalAhmad10/QuickPOS-SPM/actions/runs/45110283311
- Corrected passing run: https://github.com/ShawalAhmad10/QuickPOS-SPM/actions/runs/45110435088
- PR #1: https://github.com/ShawalAhmad10/QuickPOS-SPM/pull/1
- PR #2 (QPOS-23): https://github.com/ShawalAhmad10/QuickPOS-SPM/pull/2
- PR #3 (QPOS-19): https://github.com/ShawalAhmad10/QuickPOS-SPM/pull/3
- PR #4 (QPOS-24): https://github.com/ShawalAhmad10/QuickPOS-SPM/pull/4

AI-assisted technical findings are recorded on each PR and explicitly are not independent human approvals. Safe merge order after genuine authorization is **#2 → #3 → #4 → refreshed #1**.

## Project documents

- `docs/AGENT_HANDOFF.md` — chronological verified execution record.
- `docs/REQUIREMENTS_MATRIX.md` — official Task 1–16 traceability.
- `docs/FINAL_TECHNICAL_AUDIT.md` — current engineering audit and gap list.
- `docs/TEST_PLAN.md` and `docs/EVIDENCE_CHECKLIST.md` — QA and evidence controls.
- `docs/SPRINT_PLAN.md`, `docs/SPRINT_1_REPORT.md`, `docs/SPRINT_2_REPORT.md` — truthful Scrum plan/status.
- `docs/EVIDENCE_REPORT_DRAFT.md` and `output/pdf/QuickPOS_Evidence_Report.pdf` — current report source/output.

## Academic integrity

No second contributor, independent approval, merge, sprint closure, Group ID, roll number or submission receipt is claimed without evidence. The student must understand and demonstrate the implementation and workflow in the live viva.

**Deadline:** 10 December 2026, 11:59 PM PKT. **Authoritative brief:** `docs/reference/CS4002_QuickPOS_Semester_Project_BCS9C_Fall2026.pdf`.
