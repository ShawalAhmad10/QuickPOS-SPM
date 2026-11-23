# GitHub collaboration, traceability and review protocol

## Accounts and authorization
Primary repo owner: https://github.com/ShawalAhmad10. Secondary automation login: https://github.com/ShawalAhmad97, controlled by **the same individual**. Both accounts may be used transparently where provider rules permit; their activity cannot be passed off as independent students or peer reviews. Independent code reviews require an **approved real reviewer** or an instructor-approved equivalent. The original course requirement expects at least four meaningful merged PRs, with two per genuine student in a normal two-person group.

## Repository
Suggested: `ShawalAhmad10/QuickPOS-[APPROVED_GROUP_ID]`. Do **not** invent group ID. Public recommended by brief for GitHub Actions ease; ensure necessary instructor/TA access. Verify remote target and active authentication before any push.

## Branch names
`feature/<REAL-ISSUE-KEY>-header-nav`  
`feature/<REAL-ISSUE-KEY>-hero-mockup`  
`feature/<REAL-ISSUE-KEY>-features`  
`feature/<REAL-ISSUE-KEY>-pricing`  
`feature/<REAL-ISSUE-KEY>-contact-form`  
`bugfix/<REAL-ISSUE-KEY>-mobile-overflow`

## Commit messages
`<REAL-ISSUE-KEY>: Implement responsive header navigation`  
`<REAL-ISSUE-KEY>: Validate server-side contact inputs`  
`<REAL-ISSUE-KEY>: Add PHP lint and contact tests`

## Proposed PR slices (four is a minimum, not a cap)
1. **Sprint 1** — foundation, header, accessible navigation, Hero (real story keys).
2. **Sprint 1** — mockup, Feature cards, PHP skeleton.
3. **Sprint 2** — pricing, contact flow, Footer.
4. **Sprint 2** — automated tests, GitHub Actions, responsive fixes.

Exact PR boundaries should follow real Jira tasks and coding history; do not retroactively split a single already-merged change solely for appearances. PR titles must include real Jira keys; body contains purpose, tests and screenshots if applicable.

## Review and merge
- Push focused branch → open PR to `main` → CI → **review by instructor-approved reviewer** → address feedback → CI green → merge → Jira status Done.
- AI code analysis is useful but is **not independent human PR approval**.
- Never forge another student's authorship; no fake reviewers or retroactive review timestamps.
- Branch protection optional; free features suffice.

## GitHub–Jira integration
Connect the real repo to the new Jira Scrum project using supported integration. Use Jira issue keys in branch, commit, PR. Verify at least one Jira issue shows actual linked development activity. Screenshots/links go into evidence checklist.

### Development-link verification
For each traceability check, use the same real Jira key in the branch name, commit subject and pull-request title/body. After pushing and opening the PR, wait for GitHub Actions and Jira's GitHub backfill/sync, then record:

- the exact branch, commit, PR and Actions run URLs;
- which items Jira's Development panel actually displays;
- the observation time and whether CI passed; and
- any missing link as `NOT VERIFIED` rather than inferring it from repository connection status.

Keep the PR open until the approved review process is complete. A connected repository or finished backfill alone is not proof that a particular issue has linked development activity.

## Credential hygiene
Do not place PATs, `.env` secrets, cookies, tokens or passwords in project files, screenshots or reports. Prefer `gh auth login`/provider OAuth; never ask agents to post credentials in chat. If active account is unexpected, **stop before remote writes**.
