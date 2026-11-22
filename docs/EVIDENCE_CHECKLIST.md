# Evidence manifest — fill only from actual verified events

**Status:** local engineering evidence was verified on 22 Nov 2026. Required remote Jira/GitHub records and final grading screenshots have not yet been generated.

| Task | Evidence artifact / actual location or URL | Verified? | Date captured |
|---|---|---|---|
| A1 | Local browser inspection at 375/768/1280: no horizontal overflow; responsive mobile/tablet/desktop layouts rendered. Required screenshot files still pending. | PARTIAL | 2026-11-22 |
| A2 | Local live browser/DOM audit: Header, Hero, Features, Pricing, Contact and Footer present; 23 internal links/CTAs inspected with no missing fragment targets; mobile menu open/Escape behavior passed. Required demonstration screenshots still pending. | PARTIAL | 2026-11-22 |
| A3 | Local HTTP/browser verification: direct handler GET 303; invalid POST 422 with field errors and escaped retained input; valid POST 303 to one-time confirmation; confirmation GET 200 then refresh/direct reuse 303. Required screenshots still pending. | PARTIAL | 2026-11-22 |
| B4 | Jira epics/backlog + two detailed story screenshots | NO | — |
| B5 | Sprint 1 and 2 planned boards, active board, completed summaries | NO | — |
| B6 | Actual bugs if present, burndown/sprint reports, retrospectives | NO | — |
| C7 | Repo URL, README screenshot, Jira issue with development link | NO | — |
| C8 | Focused branches + issue-key commits + Jira-linked activity | NO | — |
| C9 | Four meaningful merged PRs, real review feedback/approval, CI | NO | — |
| C10 | Factual work division; documented solo exception | NO | — |
| D11 | `.github/workflows/ci.yml` implements required Ubuntu/PHP triggers and steps; embedded Bash lint script passed local syntax checking. Remote Actions run pending repository creation. | PARTIAL | 2026-11-22 |
| D12 | Local `php -l` run passed for all 17 PHP files under `public/`, `src/` and `tests/`. Remote Actions log pending. | PARTIAL | 2026-11-22 |
| D13 | `tests/run.php`: 13/13 dependency-free validation, normalization, boundary, non-string and escaping tests passed locally with failure-count/nonzero-exit handling. Remote Actions log pending. | PARTIAL | 2026-11-22 |
| D14 | Actual failed run + corrected passing run + explanation | NO | — |
| E15 | Source ZIP + PDF/Word labeled Parts A–E, Tasks #1–#16; URLs | NO | — |
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
