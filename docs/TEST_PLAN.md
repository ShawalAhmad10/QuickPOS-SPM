# QuickPOS test strategy and CI acceptance

## PHP tests (automated, plain PHP)
Test the pure `validateContact(array $input): array` function from `src/ContactValidator.php`.

| ID | Input | Expected result |
|---|---|---|
| T01 | Name empty, valid email/message | `valid=false`, field error `name` |
| T02 | Name/message valid, malformed email | `valid=false`, field error `email` |
| T03 | Name/email valid, message empty | `valid=false`, field error `message` |
| T04 | All fields valid | `valid=true`, no errors |
| T05 (extra) | Whitespace-only name/message | required errors |
| T06 (extra) | Oversized values | length errors if implemented |
| T07 (extra) | HTML-like input reflected in form | no unintended HTML injection (integration/manual test) |

Run `php tests/run.php`. Assertions must cause **nonzero** exit on failure. Include tests under `tests/` and exact local command in README.

## PHP syntax lint
Run `php -l` against **all relevant** `.php` files, including `public/`, `src/`, and `tests/`. CI must fail if any file has a syntax error. Avoid pipes or commands that hide failures.

## GitHub Actions
CI triggers: pushes to `feature/**`, `bugfix/**`, and `main`, and `pull_request` targeting `main`. Use Ubuntu runner, checkout and setup PHP. Steps: display PHP version; lint all PHP; run tests. Keep green main and authentic failed→fixed evidence.

## Browser manual/agent verification
| Width | Required inspection |
|---|---|
| 375px | Mobile nav toggle, vertical layouts, no x-overflow, button sizes, contact form |
| 768px | Tablet responsive layout, CTA labels, feature/pricing grids, mockup fits |
| 1280px | Polished complete desktop, visual hierarchy, all section links, mockup |

Also click all primary/secondary/pricing CTAs; test empty name/email/message; test valid POST; verify back/refresh behavior; inspect console errors where browser tooling is available; use browser screenshots of actual running app, not fabricated renderings.

## CI failure-fix evidence
When a genuine branch CI run fails, preserve run URL, error log and correction commit, then the next passing run. If no natural failure occurs, request approval for an explicitly labeled **controlled negative-test demonstration**, never represented as an accidental defect. No failed checks on final `main`.

## QA definition of complete
All 16 rubric tasks have source/evidence links or documented approved exception; tests pass, actual screenshots exist, README commands are accurate and student can explain the implementation.
