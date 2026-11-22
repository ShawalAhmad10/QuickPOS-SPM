# QuickPOS evidence report draft

**Course:** CS4002 Fundamentals of Software Project Management  
**Institution:** FAST-NUCES Chiniot-Faisalabad Campus  
**Student:** Shawal Ahmad  
**Roll number:** not supplied  
**Approved Group ID:** not supplied  
**Prepared:** 22 November 2026  
**Repository:** https://github.com/ShawalAhmad10/QuickPOS-SPM

This pre-submission draft covers Parts A-E and Tasks 1-16 using evidence that actually exists. It is not a university submission and does not claim instructor approval, completed future sprints or independent review.

## Contributor disclosure

Shawal Ahmad is the only identified student contributor. `ShawalAhmad10` is the primary GitHub account. `ShawalAhmad97` is operated by the same person and is not a second student or independent reviewer. AI tools assisted development and documentation; the student remains responsible for correctness, understanding and the live viva.

# Part A - QuickPOS website development

## Task 1 - Product design and responsive UI - PASS locally

The custom PHP landing page uses a consistent visual system, an original HTML/CSS/SVG POS dashboard, responsive layouts and accessible interaction states. Real captures exist at desktop and mobile widths. Automated browser checks found no horizontal overflow at 320, 375, 768, 1280 or 1440 pixels.

Evidence: `docs/evidence/website/01-desktop-full-1280.png`, `02-mobile-full-375.png`, `03-pricing-1280.png`, `03b-pricing-375.png`, and `docs/WEBSITE_FINAL_QA.md`.

## Task 2 - Six required sections - PASS locally

Header/Navigation, Hero, Features, Pricing, Contact and Footer are implemented. Navigation, hero CTAs, plan CTAs and footer links have meaningful destinations. The mobile menu updates `aria-expanded`, closes on Escape and restores focus.

Evidence: website captures 01-07 and the live-link audit in `docs/WEBSITE_FINAL_QA.md`.

## Task 3 - PHP contact form and validation - PASS locally

The POST form validates name, email and message on the server. Invalid input returns HTTP 422 with field errors and escaped retained values. Valid input uses a 303 redirect to a one-time confirmation backed by a short-lived hardened session. Nothing is emailed or saved permanently.

Evidence: screenshots 05 and 06, `src/ContactValidator.php`, `public/contact.php`, `public/thank-you.php`, and 13/13 automated tests.

# Part B - Jira Scrum planning and execution

## Task 4 - Jira setup, Epics and backlog - BLOCKED

Seven Epics, fifteen Stories, technical Tasks and Subtasks are prepared in `docs/JIRA_BACKLOG.md` and `docs/jira/quickpos-backlog-import.csv`. No Jira records or keys exist because the Atlassian integration is not installed/connected and no authorized Jira site is available.

## Task 5 - Two sprints - PARTIAL

The required dates, goals and candidate allocations are prepared. Sprint 1 is scheduled for 23-29 November 2026 and Sprint 2 for 30 November-6 December 2026. Neither future sprint is claimed started or completed. See `docs/SPRINT_1_REPORT.md` and `docs/SPRINT_2_REPORT.md`.

## Task 6 - Bugs, progress and retrospectives - NOT VERIFIED

No Jira bug history, reports or completed retrospectives exist. One genuine local defect - inaccurate temporary-session wording - was corrected and recorded in the handoff. Future reports must use actual Jira events.

# Part C - GitHub collaboration and Jira integration

## Task 7 - Repository, README and integration - PARTIAL

The public repository is live at https://github.com/ShawalAhmad10/QuickPOS-SPM. Baseline commit `fe10bd36b1eb77907a222d8f74d9c28b7aad38f5` contains the complete source, tests, workflow and evidence. Jira integration remains blocked.

## Task 8 - Branches and meaningful commits - PARTIAL

The already-complete uncommitted source was recorded as one truthful baseline rather than fake feature history. A real `feature/project-documentation` branch contains subsequent documentation/delivery work. Jira-key linkage is unavailable.

## Task 9 - Pull requests and code review - BLOCKED

A genuine documentation PR is open at https://github.com/ShawalAhmad10/QuickPOS-SPM/pull/1 and its pull-request CI run 45044977813 passed. It remains unmerged for legitimate review. Four merged PRs and independent review cannot be claimed. Instructor approval for the one-person arrangement and reviewer is required.

## Task 10 - Balanced participation - BLOCKED

Only Shawal Ahmad is identified. The secondary GitHub account is not a separate person. Contribution/review requirements depend on the instructor-approved solo exception.

# Part D - Automated tests and continuous integration

## Task 11 - Workflow and triggers - PASS

`.github/workflows/ci.yml` uses Ubuntu and PHP 8.3 and runs on main, feature branches, bugfix branches and PRs targeting main. Passing run: https://github.com/ShawalAhmad10/QuickPOS-SPM/actions/runs/45043988754

## Task 12 - Automated syntax checks - PASS

The workflow discovers and lints every PHP file under `public`, `src` and `tests`. All 17 files passed locally and in GitHub Actions.

## Task 13 - Automated contact tests - PASS

`tests/run.php` covers the four required cases plus whitespace, missing/non-string fields, exact/over maximum lengths, normalization and escaping. Result: 13/13 locally and remotely. Any failure produces a nonzero exit.

## Task 14 - Failure, fix and passing evidence - NOT VERIFIED

No genuine CI failure has occurred. Main is green. A controlled negative demonstration must not be run or described as accidental without explicit approval.

# Part E - Submission and live evaluation

## Task 15 - Submission package and evidence report - PARTIAL

A source ZIP, evidence-report PDF draft and viva notes are generated locally and verified. They require refresh after Jira, sprint, review and final-merge evidence exists. They have not been submitted to the university.

## Task 16 - Live viva - PARTIAL

Viva preparation exists in `docs/VIVA_PREPARATION.md`. The actual live evaluation has not occurred.

# Explicit evidence gaps

- Approved Group ID and roll number.
- Connected Jira project, actual issue keys, backlog/board/report screenshots and GitHub development link.
- Real sprint start/track/closure evidence and retrospectives.
- Instructor-approved solo-group and independent-review arrangements.
- Four meaningful merged PRs with legitimate reviews.
- Authentic failed-to-fixed GitHub Actions pair.
- Final repository state and refreshed package after all approved merges.
- University submission receipt and live-viva outcome.
