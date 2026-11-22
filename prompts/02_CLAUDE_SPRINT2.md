# PROMPT — Claude Sprint 2: full website completion

Resume QuickPOS in `D:\projects\QuickPOS-SPM`. Read `CLAUDE.md`, `docs/AGENT_HANDOFF.md` and only relevant sections of `docs/PRD.md`, `docs/DESIGN.md`, `docs/ARCHITECTURE.md`. **Preserve accepted Sprint 1 work.**

Implement Sprint 2 scope during the actual 30 Nov–6 Dec 2026 sprint:
1. Pricing (Basic $19/mo, Pro $49/mo highlighted, Enterprise Custom; all illustrative; meaningful CTAs to Contact).
2. Contact form Name/Email/Message via PHP POST, field errors, valid simulated success; validation `validateContact(array $input): array` exactly matching documented return contract and test seam. Required/format checks on server; trim, length limits, escape reflected values. No email delivery or DB.
3. Thank-you confirmation with accurate no-email claim.
4. Footer with copyright, working links and clearly marked placeholders for unavailable social profiles.
5. Make all six sections consistent, responsive at 375/768/1280; fix actual overflow, focus and mobile menu issues.
6. Keep site original, visually refined, production-like, no arbitrary framework/dependencies.

Do not touch `tests/`, `.github/`, remote GitHub/Jira, or fabricate evidence. Use actual local PHP/browser checks available. Update `docs/AGENT_HANDOFF.md` with exact results and outstanding issues for Codex. Respond concise DONE / VERIFIED / BLOCKED / CODEX HANDOFF.
