# QuickPOS viva notes

## One-sentence overview

QuickPOS is a responsive, server-rendered PHP marketing page for a fictional POS SaaS product; it demonstrates six required sections, server-side contact validation, automated tests and GitHub Actions, not a real POS backend.

## Demonstration sequence

1. Repository: `https://github.com/ShawalAhmad10/QuickPOS-SPM` and baseline commit `fe10bd3`.
2. Start: `php -S localhost:8000 -t public`.
3. Show Header, Hero, Features, Pricing, Contact and Footer at desktop/mobile widths.
4. Show mobile menu keyboard/Escape behavior and plan CTA selection.
5. Submit invalid input: explain HTTP 422, error summary, field messages and escaped retained values.
6. Submit valid input: explain 303 POST/Redirect/GET and one-time PHP session confirmation.
7. Run `php tests/run.php`: 13/13 expected.
8. Explain `.github/workflows/ci.yml` and open Actions run 45043988754.
9. Show Jira only after it actually exists; state present connection and approval blockers honestly.

## Key technical explanations

- `validateContact()` normalizes strings, rejects missing/invalid/overlong values and returns values/errors without rendering.
- `e()` performs output encoding at the HTML boundary; normalization alone does not make text HTML-safe.
- `normalize_plan()` allow-lists Basic, Pro or Enterprise and ignores hostile values.
- Invalid requests return 422; valid requests return 303 to prevent refresh resubmission.
- The confirmation session uses HttpOnly, SameSite=Lax and Secure on HTTPS, then unsets its one-time payload.
- CSP restricts scripts/assets/form targets; frame denial and MIME/referrer headers add baseline protection.
- CI discovers all PHP files instead of linting one hard-coded path; any lint/test failure stops the job.

## Governance disclosure

- Student: Shawal Ahmad. Roll number and approved Group ID are not yet supplied.
- `ShawalAhmad10` and `ShawalAhmad97` are controlled by the same person. They are not two students and cannot create independent review evidence.
- The complete local application existed before Git history. It was committed once as a truthful baseline, not split into fake historical feature commits.
- PR 1 is real and green but remains open pending legitimate instructor-approved review.
- Jira, future sprint outcomes, failed-CI evidence, approval and submission receipt are not claimed.

## Current verified links

- Repository: https://github.com/ShawalAhmad10/QuickPOS-SPM
- Main CI: https://github.com/ShawalAhmad10/QuickPOS-SPM/actions/runs/45043988754
- Documentation PR: https://github.com/ShawalAhmad10/QuickPOS-SPM/pull/1
- PR CI: https://github.com/ShawalAhmad10/QuickPOS-SPM/actions/runs/45044977813
