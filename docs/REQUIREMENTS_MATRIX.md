# Complete grading traceability matrix

**Authoritative source:** `docs/reference/CS4002_QuickPOS_Semester_Project_BCS9C_Fall2026.pdf`
**Evidence cutoff:** 23 November 2026 (PKT). A passing engineering check does not imply a grade or completion of future Scrum/review events.

| Task | Marks | Verified evidence | Current status / gap |
|---|---:|---|---|
| 1. UI and responsive design | 23 | Desktop/mobile screenshots; QA at 375/768/1280 and additional widths | **PASS locally**; evaluator judgment remains |
| 2. Six required sections | 7 | Header, Hero, Features, Pricing, Contact, Footer; internal links checked | **PASS locally**; live demonstration remains |
| 3. PHP contact validation | 10 | Real POST flows, 303/422 behavior, `tests/run.php` | **PASS locally**; live demonstration remains |
| 4. Jira setup and backlog | 7 | QPOS Scrum project; 32 issues QPOS-1–QPOS-32; 7 epics, 15 stories, 5 tasks, 5 subtasks | **VERIFIED setup**; final screenshots/two detailed-story evidence remain |
| 5. Exactly two sprints | 7 | Sprint 1 active 23–29 Nov with 6 Done and 3 In Progress; Sprint 2 planned 30 Nov–6 Dec | **IN PROGRESS**; both real closures/summaries remain |
| 6. Bugs, reports, retrospectives | 6 | 13 issues Done overall; QPOS-14–QPOS-18 have factual pre-sprint evidence comments and remain To Do | **PARTIAL**; reports and two completed retros remain future |
| 7. Repository and Jira integration | 5 | Public repo; QPOS-23 Development shows an open GitHub PR | **VERIFIED linkage**; final merged baseline remains |
| 8. Jira-keyed branches and commits | 5 | QPOS-23, QPOS-19 and QPOS-24 branches/commits/PRs | **VERIFIED development evidence** |
| 9. Four PRs and reviews | 7 | Four genuine open PRs, green CI, preserved AI-assisted technical findings | **BLOCKED**; 0/4 merged and no qualifying independent approval |
| 10. Balanced participation | 3 | Honest single-person disclosure; Approved Solo Project reported by Shawal Ahmad (22F-3303) | **PARTIAL**; documentary approval and qualifying review arrangement are not included |
| 11. CI workflow and triggers | 4 | `.github/workflows/ci.yml`; main run 45043988754 | **PASS** |
| 12. PHP syntax checks | 3 | Repository-wide discovery; 17/17 tracked PHP files pass | **PASS on PR #4**; merge to main remains |
| 13. Automated PHP tests | 5 | 13/13 tests; warnings/notices fail; exact 254-character email boundary | **PASS on PR #3/#4**; merge to main remains |
| 14. Failed→fixed CI | 3 | Failed run 45110283311; corrective run 45110435088; main stayed green | **VERIFIED controlled exercise** |
| 15. ZIP and evidence report | 2 | Shawal Ahmad, 22F-3303, BCS-9C; refreshed candidate PDF/ZIP and Task 1–16 audit | **PARTIAL**; final merges and LMS submission remain |
| 16. Live viva | 3 | Preparation notes and demonstration sequence | **PARTIAL**; actual live evaluation remains |

## Mandatory authorization

The student reports that solo-project approval has been received; this repository does not contain documentary proof. `ShawalAhmad97` is the same human as `ShawalAhmad10` and cannot provide independent review evidence. Do not merge or self-certify Task 9 without the qualifying approved review arrangement.

## Evidence discipline

- Mark code stories Done only after acceptance criteria are met and the work is integrated.
- Preserve real failed and corrected runs; never manufacture contributors, reviews, dates or screenshots.
- Refresh this matrix after each authorized merge and after each sprint closes.
