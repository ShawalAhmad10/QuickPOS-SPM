# Jira import readiness - QuickPOS

**Current status:** BLOCKED on connection. The Atlassian integration is available but not installed/connected, and no authorized Jira site URL or project context is available. No Jira project, key, issue URL, sprint or transition is claimed.

`docs/jira/quickpos-backlog-import.csv` contains seven Epics, fifteen Stories, five technical Tasks and five Subtasks. Its numeric `Issue ID` and `Parent ID` values are import-only relationship identifiers, not Jira issue keys.

## Before importing

1. Connect the authorized Atlassian workspace.
2. Confirm the approved Group ID, actual Jira project name/key and Shawal Ahmad's Jira account identifier.
3. Create a new Jira Software Scrum project accessible to the instructor/TA.
4. Map CSV fields to Jira fields. Map `Parent ID` to Parent where supported; for company-managed projects, the importer may require mapping Story-to-Epic relationships through Epic Link instead.
5. Map `Story Points` to the project's estimation field and replace blank assignees only with actual approved account identifiers.

## Sprints to create in Jira

- Sprint 1: 23-29 November 2026. Do not start before 23 November.
- Sprint 2: 30 November-6 December 2026. Do not start before 30 November.

The CSV's Sprint values are planning labels. Confirm the Jira importer supports Sprint mapping; otherwise create both future sprints and move the imported stories manually. Do not close sprints or mark code stories Done before actual work, approved review and merge.

## GitHub connection

Connect `https://github.com/ShawalAhmad10/QuickPOS-SPM` through the authorized Jira GitHub integration after real issue keys exist. Future branch, commit and PR titles should use those keys. The existing baseline commit intentionally has no Jira key because Jira was unavailable when the already-complete local source was first published.
