# QuickPOS viva notes

**Student:** Shawal Ahmad
**Roll number:** 22F-3303
**Section:** BCS-9C
**Course:** CS4002 - Fundamentals of Software Project Management
**Submitted to:** Miss Maham Saleem
**Group description:** Approved Solo Project (student-reported; documentary proof is not included)

## One-sentence overview

QuickPOS is a responsive server-rendered PHP marketing page for a fictional point-of-sale SaaS product; it demonstrates six required sections, secure contact validation, automated tests, Jira traceability and GitHub Actions, not a real POS backend.

## Eight-minute demonstration

1. Open the repository and identify stable `main` plus the separate integration candidate.
2. Run `php -S localhost:8000 -t public`; show desktop/mobile layouts and all six sections.
3. Submit invalid contact data; explain HTTP 422 and safe retained values.
4. Submit valid data; explain the HTTP 303 redirect and one-time confirmation session.
5. Run `php tests/run.php`; explain the 13 cases, warning handling and exact boundaries.
6. Show repository-wide lint in CI and the 17-file result.
7. Show Jira QPOS, board 35, active Sprint 1, planned Sprint 2 and QPOS-23 development linkage.
8. Show PRs #1-#4, the controlled failed/fixed runs, and why merges remain pending.

## Architecture explanation

- `public/` is the web root with PHP entry points and static assets.
- `src/` contains bootstrap, helpers, reusable validation and view components.
- `tests/run.php` exercises validation without a browser or database.
- `.github/workflows/ci.yml` runs on Ubuntu/PHP 8.3, discovers all tracked PHP files and executes tests.
- Contact submissions are validated and simulated only; no database, payment, registration, real email or authentication exists.

## Likely viva questions

**Why PHP rather than static HTML?**
The assignment requires meaningful backend behavior. PHP performs server-side validation and controls the invalid/success HTTP flow.

**How does invalid input fail?**
The validator normalizes inputs, checks required fields, email format and length boundaries, then the contact entry point returns HTTP 422 with encoded field errors.

**How is success handled?**
A valid POST stores only a short-lived one-time confirmation payload in a hardened session and redirects with HTTP 303.

**How does CI cover all PHP files?**
The workflow uses `git ls-files -z -- '*.php'`, fails if no PHP files are found, and runs `php -l` for every tracked path.

**What proves failed-to-fixed CI?**
Run 45110283311 failed with an explicitly labeled sentinel assertion; the corrective commit removed only that sentinel and run 45110435088 passed.

**Why are the PRs still open?**
All four are green and mergeable, but no qualifying independent review is present. AI-assisted comments are technical findings, not approvals.

## Governance disclosure

- Shawal Ahmad (22F-3303) is the only enrolled student represented.
- `ShawalAhmad10` and `ShawalAhmad97` are two work identities of the same student.
- Approved Solo Project status is reported by the student; documentary proof is not included.
- No independent review, merge, Sprint 1/2 closure, grade or LMS receipt is claimed without evidence.

## Key links

- Repository: https://github.com/ShawalAhmad10/QuickPOS-SPM
- Jira: https://shawalahmad97.atlassian.net/jira/software/projects/QPOS
- Stable main CI: https://github.com/ShawalAhmad10/QuickPOS-SPM/actions/runs/45043988754
- Failed CI: https://github.com/ShawalAhmad10/QuickPOS-SPM/actions/runs/45110283311
- Corrected CI: https://github.com/ShawalAhmad10/QuickPOS-SPM/actions/runs/45110435088
- Pull requests: https://github.com/ShawalAhmad10/QuickPOS-SPM/pulls
