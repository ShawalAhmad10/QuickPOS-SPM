# QuickPOS final technical audit draft

**Audit date:** 22 November 2026 (PKT)  
**Repository:** https://github.com/ShawalAhmad10/QuickPOS-SPM  
**Baseline commit:** `fe10bd36b1eb77907a222d8f74d9c28b7aad38f5`  
**Passing CI:** https://github.com/ShawalAhmad10/QuickPOS-SPM/actions/runs/45043988754

This is a factual pre-sprint acceptance audit, not a grade and not proof that future Scrum/review events occurred.

## Executive result

- Website: locally verified with real screenshots and live HTTP/browser checks.
- Tests: 13/13 pass; all 17 PHP files lint cleanly.
- Security: output encoding, input normalization, CSP and hardened short-lived session cookies verified.
- GitHub: new public repository, truthful single-author baseline and passing main CI verified.
- Jira: blocked because the Atlassian integration is not installed/connected and no Jira site is available.
- Review: blocked pending instructor approval for a solo-group review arrangement.

## Task 1-16 acceptance status

| Task | Status | Actual evidence | Missing criterion |
|---|---|---|---|
| 1. UI and responsive design | PASS | `docs/evidence/website/01-desktop-full-1280.png`, `02-mobile-full-375.png`; QA at 320/375/768/1280/1440 | Final evaluator judgment |
| 2. Six required sections | PASS | Screenshots 01-07; `docs/WEBSITE_FINAL_QA.md`; 23 internal links checked | Live evaluator demonstration |
| 3. PHP contact validation | PASS | Invalid/valid screenshots, HTTP 303/422 flow, `tests/run.php` | Final evaluator judgment |
| 4. Jira setup/backlog | BLOCKED | `docs/JIRA_BACKLOG.md` and import-ready CSV | Connected Jira project, actual keys/assignee |
| 5. Two sprints | PARTIAL | Fixed-date plans and report templates | Real start/track/close events and summaries |
| 6. Bugs/progress/retros | NOT VERIFIED | One real local wording defect documented in handoff | Jira bug history, reports, completed retrospectives |
| 7. Repository/README/integration | PARTIAL | Public repository and updated README | Jira-GitHub development link |
| 8. Branches/commits | PARTIAL | Baseline commit plus real documentation branch | Jira-key naming/linkage and further authentic commits |
| 9. Pull requests/reviews | BLOCKED | One real documentation PR planned/opened by this milestone | Four merged PRs and instructor-approved independent reviews |
| 10. Balanced participation | BLOCKED | Honest single-person disclosure | Instructor-approved solo exception/contribution arrangement |
| 11. CI workflow/triggers | PASS | `.github/workflows/ci.yml`; passing run 45043988754 | None for configured workflow; retain future run evidence |
| 12. PHP syntax checks | PASS | 17 files linted locally and remotely | None |
| 13. Contact-form tests | PASS | 13/13 locally and remotely; nonzero failure exit implemented | None |
| 14. CI failure/fix | NOT VERIFIED | Main is green | Authentic failed development run and corrected run |
| 15. Submission package/report | PARTIAL | Draft ZIP, PDF and evidence gap list generated locally | Group ID/roll number, final links, Jira/sprint/review evidence, LMS submission |
| 16. Live viva | PARTIAL | `docs/VIVA_PREPARATION.md` | Actual attended live evaluation |

## Verified commands and results

```text
php -l public/src/tests PHP files -> 17/17 PASS
php tests/run.php -> 13/13 PASS
GitHub Actions run 45043988754 -> success
Secret/key pattern scan -> no findings
GitHub target identity -> ShawalAhmad10
```

## Integrity disclosures

- `ShawalAhmad10` is the primary account. `ShawalAhmad97` is controlled by the same person and is not an independent student or reviewer.
- The initial source was already complete and uncommitted when Git history began. It was recorded truthfully as one baseline commit; no retroactive feature history was fabricated.
- No Jira keys, sprint transitions, reviewer approvals, Group ID, roll number or instructor decisions are invented.
- The report and ZIP are preparation artifacts only and have not been submitted to the university.

## Evidence gaps requiring later action

1. Connect an authorized Atlassian workspace and create/import the actual Scrum project.
2. Supply approved Group ID and roll number.
3. Obtain written solo-group and independent-review arrangements.
4. Execute the two sprints on their real dates and capture boards/reports/retrospectives.
5. Complete four meaningful PRs with legitimate reviews; do not count the second owned account as independent.
6. Preserve an authentic CI failure/fix pair if one occurs, or seek permission for a clearly labeled controlled demonstration.
7. Refresh the evidence PDF and source ZIP after final merges and Jira evidence exist.
