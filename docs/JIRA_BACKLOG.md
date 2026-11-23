# Jira Scrum backlog — proposal (not yet created in Jira)

Actual Jira project: `QuickPOS - SPM`, key `QPOS`, board 35. Group description: `Approved Solo Project` (student-reported). Assignee: Shawal Ahmad (22F-3303). Do not create a fictional second student; both GitHub accounts belong to Shawal Ahmad.

## Epics (7)
EP-01 Navigation & Header; EP-02 Hero; EP-03 Features; EP-04 Pricing; EP-05 Contact; EP-06 Footer; EP-07 Testing & CI.

## Proposed 15 stories
Create real Jira issues; **TBD** below is NOT a Jira issue key. Each story includes acceptance criteria, priority, points and suggested sprint. Add technical subtasks for each story as relevant. Initial estimates may be adjusted before sprint planning.

| Temp ID | Epic | User story | Acceptance criteria (minimum) | Priority | SP | Sprint |
|---|---|---|---|---|---:|---|
| S01 | EP-01 | As visitor I can use desktop nav | Logo visible; Features/Pricing/Contact jump to sections; Sign Up CTA works | High | 3 | 1 |
| S02 | EP-01 | As mobile visitor I can open nav | Menu toggles; focus and `aria-expanded` behave; no overflow | High | 3 | 1 |
| S03 | EP-02 | As visitor I understand product value | Exact hero headline, subcopy, Get Started/Explore Features CTA work | High | 3 | 1 |
| S04 | EP-02 | As visitor I can see a credible POS mockup | Custom visual with stock/sales/analytics representation; responsive; sample data fictional | High | 5 | 1 |
| S05 | EP-03 | As visitor I see core features | 4 icon cards for Inventory/Analytics/Customers/Integrations | High | 3 | 1 |
| S06 | EP-05 | As maintainer I have testable PHP entry points | Clear `public/` and `src/`, validator signature agreed, local PHP starts | High | 3 | 1 |
| S07 | EP-04 | As visitor I can compare plans | Basic/Pro/Enterprise with illustrative prices/benefits, CTAs work | High | 3 | 2 |
| S08 | EP-05 | As visitor I can fill a contact form | Name/Email/Message, accessible labels, POST submission | High | 3 | 2 |
| S09 | EP-05 | As visitor I see accurate form validation | Empty name/message and invalid email rejected on server, field-specific errors | Highest | 5 | 2 |
| S10 | EP-05 | As visitor I get confirmation | Valid form shows simulated success, no false mail claim | High | 2 | 2 |
| S11 | EP-06 | As visitor I can navigate from footer | Copyright, meaningful section links, explicit social placeholders | Medium | 2 | 2 |
| S12 | EP-07 | As maintainer I have PHP validation tests | >=4 executable tests; test failures exit nonzero | Highest | 3 | 2 |
| S13 | EP-07 | As maintainer I have running CI | Branch push/main PR/main triggers, PHP lint all files, tests; green main | Highest | 5 | 2 |
| S14 | EP-07 | As visitor I have a responsive reliable page | Screenshot/test at 375/768/1280; no overflow; CTAs work | High | 3 | 2 |
| S15 | EP-07 | As evaluator I can inspect documentation | Honest README, local steps, links, updated evidence inventory | Medium | 2 | 2 |

Approximate story points: Sprint 1 **20 SP**; Sprint 2 **28 SP**. Re-estimate for real capacity instead of pretending two human developers are available.

## Assignments / rules
All Jira stories must have an **actual person** as assignee and full acceptance criteria/description/priority/SP; use the real approved group setup. Link tasks/subtasks under story/task parents properly. Record agent-generated code in notes but do not count AI as another student. Jira issue states must reflect actual transitions after work/PR merges.

## Sample Jira description format
**As a** visitor, **I want** the pricing comparison to be easy to scan, **so that** I can choose an appropriate plan.  
**Acceptance:** Basic, Pro and Enterprise differentiated; price/period visible; meaningful feature differences; Pro visually distinguished; CTA scrolls to Contact; mobile pricing does not overflow.  
**Priority:** High. **SP:** 3. **Assignee:** actual approved member. **Sprint:** 2.

## Separate technical tasks / bugs
Under EP-07 add Tasks for GitHub/Jira integration, README, lint, screenshot capture, evidence packaging. Real defects get Jira Bug issues with reproduction, expected/actual, fix PR and verification. Never invent Bug issues to meet a quota.
