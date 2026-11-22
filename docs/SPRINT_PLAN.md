# Scrum calendar and execution protocol — QuickPOS

**Dates are fixed by assignment.** Today for initial planning: 22 Nov 2026. All activity logs must use real timestamps; no backdating.

| Period | Goal | Product scope | Process/evidence |
|---|---|---|---|
| Nov 22 | Preflight and sprint preparation | Requirements, style, architecture | Permissions, new Jira/repo, actual assignees, backlog, sprint 1 goal |
| Sprint 1: Nov 23–29 | Establish a credible landing page foundation | Header/nav, Hero, custom POS mockup, Features, PHP skeleton | Start/track/complete sprint; actual issues, branches, PRs, boards, report, retro |
| Sprint 2: Nov 30–Dec 6 | Ship the complete verified site | Pricing, Contact + PHP validation, Footer, responsive fixes | Tests, CI, remaining PRs, actual bug issues, board/report, retro |
| Dec 7–10 | Acceptance and submission | Fix genuine leftovers only | Final QA, screenshots, documentation, CI, report, ZIP, viva |
| Dec 10, 23:59 PKT | Deadline | Submit before cutoff | Final ZIP in official channel; repo/Jira access verified |

## Sprint goals (draft in Jira before start)
**Sprint 1:** Deliver a recognizable, responsive QuickPOS marketing foundation with accessible navigation, Hero, original mockup and Features, integrated into the shared repo via traceable work.  
**Sprint 2:** Complete all required page sections and PHP validation; prove correctness through executable tests, GitHub Actions and evidence-backed review.

## Daily rhythm (real events only)
Before coding: check sprint board and select story. During implementation: move issue To Do → In Progress, focus branch, incremental commits with real Jira key. After verification + approved review + CI + merge: issue Done. Save links, screenshots and test commands in `docs/EVIDENCE_CHECKLIST.md`. At sprint end close it in Jira and write factual retrospective: went well / challenges / one concrete improvement.

## Risk register
| Risk | Impact | Mitigation |
|---|---|---|
| Solo group not approved | High evaluation risk | Ask instructor before relying on dual-account plan; document approved alternate reviewer |
| GitHub account mismatch | Wrong owner/contributions | Check `gh auth status`, remote and git identity before pushes |
| Jira connection unavailable | Backlog/traceability blocked | Setup official Atlassian connection or authorized browser workflow |
| One-shot code loses PR traceability | C marks reduced | Phase implementation by Jira stories, not one giant dump |
| No CI failure captured | D14 marks at risk | Monitor authentic failures; use transparent controlled negative test only with approval |
| Screenshots collected too late | E report incomplete | Capture actual evidence per milestone |
| Short time around final exam work | Late submission | Aim technical completion by Dec 6 and report by Dec 9 |

## Retrospective templates (do NOT fill with fictional claims)
### Sprint 1 retrospective — to be written after 29 Nov
- What went well: [actual observations]
- What went wrong / risks: [actual observations]
- One improvement for Sprint 2: [concrete action]
- Sprint report URL: [real]

### Sprint 2 retrospective — to be written after 6 Dec
- What went well: [actual observations]
- What went wrong / risks: [actual observations]
- One improvement for future work: [concrete action]
- Sprint report URL: [real]
