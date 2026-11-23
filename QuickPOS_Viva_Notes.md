# QuickPOS viva notes

## One-sentence overview

QuickPOS is a responsive server-rendered PHP marketing page for a fictional POS SaaS product; it demonstrates six required sections, secure contact validation, automated tests, Jira traceability and GitHub Actions—not a real POS backend.

## Demonstration sequence

1. Open https://github.com/ShawalAhmad10/QuickPOS-SPM and identify stable `main`.
2. Run `php -S localhost:8000 -t public`; show desktop/mobile layouts and all six sections.
3. Submit invalid and valid contact data; explain 422 errors and 303 success redirect.
4. Run `php tests/run.php` and explain the 13 cases, warning handling and boundaries.
5. Show repository-wide PHP lint in the workflow and the 17-file result.
6. Show controlled failed run 45110283311 and corrected run 45110435088.
7. Show Jira QPOS, active Sprint 1, planned Sprint 2 and QPOS-23 Development linkage.
8. Show PRs #1–#4 and explain why they remain open.

## Governance disclosure

- Shawal Ahmad is the only identified student.
- `ShawalAhmad97` is the same person, not an independent reviewer.
- AI-assisted PR comments are technical findings, not approvals.
- No merge, Sprint 1/2 closure, Group ID, roll number, grade or LMS receipt is claimed without evidence.

## Key links

- Repository: https://github.com/ShawalAhmad10/QuickPOS-SPM
- Jira: https://shawalahmad97.atlassian.net/jira/software/projects/QPOS
- Main CI: https://github.com/ShawalAhmad10/QuickPOS-SPM/actions/runs/45043988754
- Failed/fixed CI: https://github.com/ShawalAhmad10/QuickPOS-SPM/actions/runs/45110283311 → https://github.com/ShawalAhmad10/QuickPOS-SPM/actions/runs/45110435088
- PRs: https://github.com/ShawalAhmad10/QuickPOS-SPM/pulls
