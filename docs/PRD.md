# Product Requirements Document — QuickPOS

**Version:** planning baseline 1.0 | **Date:** 22 Nov 2026 | **Status:** proposed, not implemented.  
**Course:** CS4002 Fundamentals of Software Project Management | **Deadline:** 10 Dec 2026, 23:59 PKT.

## 1. Problem and outcome
Small-business owners need a clear way to understand what a modern POS software product offers. QuickPOS is a **fictional** SaaS concept. Build a polished **marketing landing page** showing its benefits and invite visitors to contact the product team. Primary assessment value: product quality plus authentic Agile/Jira, GitHub and CI practice.

## 2. Intended audiences
- Independent retail shop owner wanting to see sales and stock in one place.
- Small restaurant/café manager evaluating clear, affordable software plans.
- Instructor/TA evaluating responsive UX, PHP behavior and project process.

## 3. Scope
**In scope:** original responsive one-page site; six sections; four POS features; Basic/Pro/Enterprise pricing; active CTAs; working PHP POST contact handler and server validation; simulated success; accurate local run instructions; accessibility basics; QA and automation.

**Out of scope:** fully operational POS, shopping cart, payment processing, subscriptions, sign-in, actual product analytics backend, database, real email, paid hosting and real customer data.

## 4. User journeys
1. Visitor lands on Hero → understands value proposition → clicks *Explore Features* → reads feature cards.
2. Visitor clicks Pricing navigation → compares Basic/Pro/Enterprise → chooses CTA → scrolls to Contact; optionally include selected plan in visible contact context.
3. Visitor enters invalid email/empty required field → sees understandable per-field server error → retains safely rendered values.
4. Visitor enters valid Name/Email/Message → gets a clear thank-you confirmation **without claim of email being delivered**.
5. Mobile visitor opens accessible menu, navigates sections, completes contact without horizontal scrolling.

## 5. Functional requirements (FR)
| ID | Requirement | Testable acceptance |
|---|---|---|
| FR-01 | Header | Original QuickPOS brand; Features, Pricing, Contact links scroll correctly; Sign Up CTA acts sensibly. |
| FR-02 | Hero | Clear headline/subtitle, primary Get Started, second CTA, high-quality original POS mockup. |
| FR-03 | Features | 3–4 distinct POS feature cards with icon, name and one-sentence benefit. Choose 4: Inventory, Analytics, Customers, Integrations. |
| FR-04 | Pricing | Three visibly different Basic, Pro, Enterprise plans; illustrative price/features and CTAs; no payment collection. |
| FR-05 | Contact | Name/Email/Message inputs, accessible labels, PHP POST and submit control. |
| FR-06 | Validation | Server rejects empty name, invalid email, empty message; returns understandable errors. |
| FR-07 | Success | Valid submission displays or redirects to success; no DB/email delivery. |
| FR-08 | Footer | Copyright, meaningful links, social placeholders or valid profiles. |
| FR-09 | CTAs | Every navigation and CTA has a sensible, working destination. |
| FR-10 | Run | `php -S localhost:8000 -t public` starts working app once implemented. |

## 6. Nonfunctional requirements (NFR)
| ID | Criterion |
|---|---|
| NFR-01 | No unintended horizontal scrollbar at widths ~375, 768, 1280px. |
| NFR-02 | Readable typography, coherent spacing, sufficient contrast; keyboard/focus operation. |
| NFR-03 | Original visual treatment; not a stock unmodified landing-page template. |
| NFR-04 | Secure output escaping for user-reflected values; sensible maximum input lengths. |
| NFR-05 | Clear separation between validation logic and web request handler for automated tests. |
| NFR-06 | No required database, email provider, framework or paid software. |
| NFR-07 | Four+ executable contact validation tests plus PHP lint all relevant sources. |

## 7. Content and proposed pricing
Headline: **Everything your business needs, at one point of sale.**  
Subhead: **Track sales, stay ahead of inventory, and understand customers—all from one streamlined workspace.**  
Primary button: **Get Started** → `#contact`. Secondary: **Explore Features** → `#features`.

Four features: Inventory Management, Sales Analytics, Customer Insights, Seamless Integrations.

Pricing to be clearly labeled **illustrative / fictional**. Suggested: Basic $19/mo (small shops); Pro $49/mo (growing teams, highlighted); Enterprise **Custom** (larger operations). These are design copy, not actual real-world offers. Pro/Basic CTAs go to Contact; Enterprise CTA goes to Contact as well. Do not implement billing or fake checkout.

## 8. Success criteria / Definition of Done
- All FRs and NFRs demonstrably pass; real screenshots at 375/768/1280.
- Form tested for required inputs and valid submission; no false delivery claims.
- Four automated PHP tests (minimum) and lint run in CI; `main` passes.
- Jira/GitHub activity links are authentic; exactly two real sprints are properly reported.
- Evidence report covers Task #1–#16 and URLs are accessible to evaluator.
- Student can demonstrate and explain the implementation and workflow in a live viva.

## 9. Dependencies / unresolved decisions
- **CONFIRMED BY STUDENT:** Approved Solo Project; documentary approval is not stored in the repository.
- **VERIFIED:** GitHub repository `ShawalAhmad10/QuickPOS-SPM`, Jira project `QPOS`, and board 35.
- **VERIFIED:** Shawal Ahmad, roll number 22F-3303, BCS-9C.
- **BLOCKED:** qualifying PR-review arrangement and independent review evidence.

**Authority:** official course PDF in `docs/reference/`. If there is a conflict, the original document prevails; do not reinterpret requirements without approval.
