# Evidence manifest — fill only from actual verified events

**Status:** local website evidence and the first real GitHub/CI evidence were verified on 22 Nov 2026. Jira, sprint, review and final submission-channel evidence remain unavailable.

| Task | Evidence artifact / actual location or URL | Verified? | Date captured |
|---|---|---|---|
| A1 | `docs/evidence/website/01-desktop-full-1280.png`, `02-mobile-full-375.png`, pricing desktop/mobile captures; measured no overflow at 320/375/768/1280/1440. | YES | 2026-11-22 |
| A2 | Website screenshots 01–07 plus live audit in `docs/WEBSITE_FINAL_QA.md`; all six sections, internal links/CTAs and mobile menu verified. | YES | 2026-11-22 |
| A3 | `05-validation-errors-1280.png`, `06-thank-you-1280.png`; HTTP/browser verification and 13 automated tests documented in `docs/WEBSITE_FINAL_QA.md`. | YES | 2026-11-22 |
| B4 | Jira epics/backlog + two detailed story screenshots | NO | — |
| B5 | Sprint 1 and 2 planned boards, active board, completed summaries | NO | — |
| B6 | Actual bugs if present, burndown/sprint reports, retrospectives | NO | — |
| C7 | Public repository and stable baseline: https://github.com/ShawalAhmad10/QuickPOS-SPM . Jira development link still blocked. | PARTIAL | 2026-11-22 |
| C8 | Baseline commit `fe10bd3` and real `feature/project-documentation` branch. Jira keys/linkage unavailable. | PARTIAL | 2026-11-22 |
| C9 | Open documentation PR with passing CI: https://github.com/ShawalAhmad10/QuickPOS-SPM/pull/1 and run 45044977813. No review or merge claimed; four merged PR requirement remains blocked. | PARTIAL | 2026-11-22 |
| C10 | Factual work division; documented solo exception | NO | — |
| D11 | Workflow plus successful main run: https://github.com/ShawalAhmad10/QuickPOS-SPM/actions/runs/45043988754 | YES | 2026-11-22 |
| D12 | All 17 PHP files linted successfully locally and in run 45043988754. | YES | 2026-11-22 |
| D13 | `tests/run.php`: 13/13 passed locally and in run 45043988754; failure-count/nonzero-exit handling is implemented. | YES | 2026-11-22 |
| D14 | Actual failed run + corrected passing run + explanation | NO | — |
| E15 | Draft PDF at `output/pdf/QuickPOS_Evidence_Report.pdf`; source ZIP and exact viva notes generated locally after the final branch commit. Not submitted. | PARTIAL | 2026-11-22 |
| E16 | Live viva: verification done by instructor during evaluation | NO | — |

## Recommended physical evidence layout (create when evidence exists)
```text
docs/evidence/
  part-a-website/
  part-b-jira/
  part-c-github/
  part-d-ci/
  part-e-submission/
```
Screenshots must come from **actual app, Jira or GitHub UI** and remain readable. Capture file origin/URL and date, don't paste fabricated progress or invented grader feedback. The final report should embed images and link to real sources.
