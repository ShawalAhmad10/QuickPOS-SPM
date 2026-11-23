# QuickPOS viva preparation

## Accurate project statement

QuickPOS is a fictional POS SaaS marketing landing page, not a complete POS system. It uses server-rendered PHP, custom CSS and minimal JavaScript. It has no database, payment processing, authentication or email delivery.

## Five-minute demonstration order

1. Open the public GitHub repository and identify the truthful baseline commit.
2. Run `php -S localhost:8000 -t public` and show all six sections.
3. Demonstrate desktop and mobile navigation plus Basic/Pro/Enterprise plan selection.
4. Submit empty/invalid inputs and explain the 422 error rerender and escaped retained values.
5. Submit valid input and explain POST/Redirect/GET plus the one-time PHP session confirmation.
6. Run `php tests/run.php` and explain how failures make the process exit nonzero.
7. Open `.github/workflows/ci.yml` and the passing Actions run.
8. Show Jira backlog/sprints only after they actually exist; identify any remaining blockers honestly.

## Code topics to explain

- `validateContact(array $input): array`: normalization, required fields, email validation and length limits.
- `e()`: contextual HTML escaping using `ENT_QUOTES | ENT_SUBSTITUTE` and UTF-8.
- `normalize_plan()`: allow-listing untrusted plan values.
- `send_security_headers()`: CSP, frame denial, MIME sniffing and referrer policy.
- `start_confirmation_session()`: HttpOnly, SameSite=Lax, HTTPS-only Secure flag and ephemeral cookie.
- `contact.php`: method guard, 422 invalid response and 303 valid redirect.
- `thank-you.php`: consumes and unsets one-time session state, then redirects direct/repeated visits.
- CI lint loop: discovers every PHP file and propagates any nonzero exit.

## Testing answers

- Required four cases: empty name, invalid email, empty message and valid input.
- Additional cases: whitespace, missing fields, arrays/non-string input, exact/over maximum lengths, normalization and escaping boundary.
- Current result: 13/13 local and remote; all 17 PHP files lint cleanly.
- CI run: https://github.com/ShawalAhmad10/QuickPOS-SPM/actions/runs/45043988754

## Governance answers

- Actual contributor: Shawal Ahmad, assisted by AI tools. The student remains responsible for understanding and demonstrating the code.
- `ShawalAhmad10` and `ShawalAhmad97` are accounts controlled by the same person; they are not two students and cannot provide independent peer review.
- The initial application existed before Git history and was committed as one truthful baseline rather than split into fake historical feature commits.
- The student reports Approved Solo Project status; documentary proof is not included. The qualifying PR-review arrangement and review evidence remain required.

## Questions to rehearse

1. Why is validation separated from the request handler?
2. Why are normalized values still escaped at render time?
3. Why return 422 for invalid input and 303 after success?
4. What does CSP prevent, and why are Google Fonts explicitly allowed?
5. How does the mobile menu maintain `aria-expanded` and keyboard behavior?
6. Why is the CI lint loop preferable to linting a single hard-coded file?
7. Which evidence is complete, and which Scrum/review evidence cannot yet be claimed?
