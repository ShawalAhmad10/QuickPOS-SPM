# QuickPOS — POS SaaS Landing Page

**CS4002 Fundamentals of Software Project Management | FAST-NUCES Chiniot-Faisalabad | Fall 2026**

> **Status: planning scaffold (22 Nov 2026), not yet a working product.** Claude will implement the site, Codex will manage tracked engineering/QA/evidence. Update this status **only after verifying** the actual implementation.

QuickPOS is a **fictional** point-of-sale SaaS product showcased through a responsive, custom-designed **PHP landing page**. This is **not a working POS application**. The semester project assesses the resulting website plus genuine Scrum, GitHub workflow, Jira integration, automated PHP testing and CI evidence.

## Team and governance
- Actual student/project owner: **Shawal Ahmad** (roll no. **[VERIFY BEFORE SUBMISSION]**).
- Group ID: **[APPROVED GROUP ID PENDING]**.
- Main GitHub: https://github.com/ShawalAhmad10
- Optional automation GitHub account: https://github.com/ShawalAhmad97 — controlled by the same person, not a separate enrolled member.
- Jira project and GitHub repository URLs: **[NOT CREATED/VERIFIED YET]**.
- Solo-group exception and alternate PR review arrangement: **[INSTRUCTOR APPROVAL PENDING]**.

## Scope
Six sections: Navigation/Header, Hero, Features, Pricing, Contact, Footer. PHP POST validation for Name/Email/Message with meaningful errors and success. Responsive at 375px/768px/1280px. No database, payment gateway, authentication or live-email delivery.

## Planned stack
PHP 8.2+, HTML5, CSS3, minimal vanilla JS, free Jira, GitHub and GitHub Actions; no UI framework or paid dependency required.

## Run locally **after implementation**
```powershell
php -v
php -S localhost:8000 -t public
```
Open `http://localhost:8000`. Form validation tests (when added): `php tests/run.php`.

## Project documents
- `START_HERE.md` — operator sequence.
- `docs/PRD.md` / `docs/DESIGN.md` / `docs/ARCHITECTURE.md` — product/UX/engineering contract.
- `docs/JIRA_BACKLOG.md` / `docs/SPRINT_PLAN.md` / `docs/GITHUB_WORKFLOW.md` — management plan.
- `docs/REQUIREMENTS_MATRIX.md` / `docs/TEST_PLAN.md` / `docs/EVIDENCE_CHECKLIST.md` — quality and evaluation traceability.
- `docs/AGENT_HANDOFF.md` — truthful state between Claude and Codex.
- `prompts/` — task-scoped, low-repetition agent prompts.

## Academic integrity
AI development is allowed, but the student must understand and demonstrate the code and workflow in the live viva. No invented human identities, synthetic peer reviews, fake sprints, fake PR history, or fabricated test results.

**Deadline:** December 10, 2026 at 11:59 PM PKT. **Official brief:** `docs/reference/CS4002_QuickPOS_Semester_Project_BCS9C_Fall2026.pdf`.
