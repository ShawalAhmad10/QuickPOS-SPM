# QuickPOS — DESIGN.md | Clean Commerce UI System

**Visual direction:** clean, credible, modern **B2B POS SaaS**. Original design, not a downloaded template. This file is the visual contract for Claude.

## 1. Reference strategy
Study presentation patterns, **not copy** illustrations/layout/assets:
- Shopify POS: https://www.shopify.com/pos — clear product-led SaaS storytelling and mockups.
- Square POS: https://squareup.com/us/en/point-of-sale — crisp benefits and simple CTAs.
- Sentrik POS: https://pos.sentrik.co/ — additional inspiration (availability not guaranteed).
- ClaPos concept: https://dribbble.com/shots/25337789-ClaPos-Landing-Page-POS-Restaurant-Apps — optional visual exploration.

Never reproduce competitor branding, logos, screenshots, graphic assets or distinctive layouts verbatim. Create a new original QuickPOS identity and render an illustrative POS product interface with HTML/CSS/SVG.

## 2. Design personality
**Keywords:** premium, calm, confident, modern, purposeful, spacious, easy-to-scan, credible.  
**Must not become:** flashy AI SaaS, purple gradient, neon/glow, glassmorphism overload, parallax festival, template clone, heavy stock photography, full-screen hero video.

## 3. Color palette
| Token | Hex | Usage |
|---|---|---|
| `--qp-white` | `#FFFFFF` | main canvas, card fill |
| `--qp-surface` | `#F5F7F8` | alternating sections, dashboard surround |
| `--qp-ink` | `#111827` | headings, strong buttons |
| `--qp-body` | `#475569` | supporting copy |
| `--qp-muted` | `#64748B` | meta text |
| `--qp-cyan` | `#0891B2` | primary CTA, charts, active states |
| `--qp-cyan-hover` | `#0E7490` | CTA hover/focus |
| `--qp-cyan-soft` | `#DBF4F8` | badges, subtle highlights |
| `--qp-border` | `#E2E8F0` | separators, inputs, quiet cards |
| `--qp-success` | `#15803D` | real form success states |
| `--qp-error` | `#B91C1C` | validation error states |

Use tokenized color variables in CSS; avoid arbitrary new palette colors unless accessibility requires it. Cyan buttons need sufficient contrast with their text — test; if uncertain, prefer dark text on pale cyan or white on dark charcoal.

## 4. Typography
Headings: **Manrope**, fallback `Inter, ui-sans-serif, system-ui, sans-serif`. Body: **Inter**, fallback system UI; no dependency on remote font loading for functionality.  
- H1 desktop: clamp(2.75rem, 5vw, 4.5rem), line-height ~1.1, weight 700–800, letter-spacing negative but legible.
- H1 mobile: ~2.4rem maximum, natural 3–5 lines; no clipped words.
- H2: clamp(2rem, 3.5vw, 3rem), line-height ~1.15.
- Body: 16–18px; card body 15–16px; labels 14px minimum unless decorative.
- Limit major copy widths to 58–70ch for comfortable reading.

## 5. Layout / rhythm
- Content max-width: **1180–1200px**, centered.
- Outer gutters: desktop 32px, tablet 24px, mobile 20px (minimum 16px).
- Header: ~76px desktop, compact accessible mobile.
- Sections: desktop vertical padding 88–112px; mobile 56–72px.
- Design tokens for spacing: 4, 8, 12, 16, 24, 32, 48, 64, 96px.
- Card corners: 16–20px; form controls 10–12px; button radius 10–12px.
- Borders: 1px neutral, shadows subdued. No ubiquitous backdrop blur.
- Icons: unified stroke width using inline SVG/local icon set; no emoji feature cards.

## 6. Desktop wireframe (1280px)
```text
+--------------------------------------------------------------------------+
| QuickPOS                  Features   Pricing   Contact      [Sign Up]     |
+--------------------------------------------------------------------------+
|                                                                          |
|  [SMARTER RETAIL OPERATIONS]          +-------------------------------+   |
|  Everything your business needs,     | [Illustrative POS Dashboard]  |   |
|  at one point of sale.               | Sales | Orders | Inventory     |   |
|  Strong subheadline.                 | chart, products, transactions  |   |
|  [Get Started] [Explore Features]    +-------------------------------+   |
|                                                                          |
+--------------------------------------------------------------------------+
| Feature heading / introduction                                           |
| [Inventory] [Analytics] [Customers] [Integrations]                      |
+--------------------------------------------------------------------------+
| Simple, transparent pricing                                              |
| [Basic $19]        [Pro $49: Recommended]     [Enterprise: Custom]       |
+--------------------------------------------------------------------------+
| Contact: title + reassurance          [Name | Email | Message | Send]   |
+--------------------------------------------------------------------------+
| QuickPOS | section links | social placeholders | copyright               |
+--------------------------------------------------------------------------+
```
Wireframe establishes hierarchy, **not exact pixel composition**. Claude may improve layout while maintaining the six-section structure.

## 7. Hero dashboard mockup (high priority)
- Build **original CSS/HTML/SVG mockup**, not copied screenshots; subtle layered 3D perspective is optional if it does not harm readability.
- Show left-side nav/rail and main dashboard surface, with a header and 3 KPI cards (e.g. illustrative revenue, orders, stock), a line/bar trend, top products / recent sales rows.
- Use believable but **clearly illustrative** fictional sample metrics. Do not imply an actual working POS backend.
- Mockup must be visibly designed at 1280px, adapt gracefully at 768px, and stack/crop **intentionally, never overflow** at 375px.
- Avoid recreating an actual competitor UI. Accessibility: decorative chart markup can be labeled as illustrative.

## 8. Exact section treatments
**Navbar:** wordmark with abstract square/scan mark, links, high-contrast Sign Up CTA; mobile menu uses a real button with `aria-expanded` and keyboard close support.

**Hero:** left copy / right original dashboard at desktop, stacked text then dashboard at mobile. Kicker + H1 + subheadline + two active buttons. Background mostly white, quiet cyan accent only.

**Features:** four 2x2 or four-column cards depending width, line icon + heading + concise benefit; consistent height but no empty filler.

**Pricing:** Basic, Pro, Enterprise. Pro highlighted through border and header chip, **not** neon fill. Uniform plan feature rows, clear currency/period labels, accessible CTAs; mark prices *illustrative*. Use $19/$49/Custom as PRD defaults.

**Contact:** split layout with intro and clean form, useful error messages directly below fields. POST validation required; thanks UI not misleading. No fake form success in JavaScript.

**Footer:** calm charcoal or pale neutral section, anchored links and explicit placeholders if social URLs unavailable; do not link to `#` without telling users placeholder.

## 9. Motion and states
- Hover transforms up to ~2px and color/border changes 160–220ms. Respect `prefers-reduced-motion: reduce`.
- Button hover/focus/disabled, input default/focus/error, navigation mobile open/closed, form error/success are deliberately designed.
- No scroll-jacking, long entrance animations, autoplay motion or heavy JS libraries.

## 10. Breakpoints / audit criteria
- **375px**: narrow mobile, no horizontal scroll, 44px-ish comfortable tap targets, single-column forms/cards and sensible dashboard treatment.
- **768px**: tablet, no overflow, adaptive card columns and nav that fits.
- **1280px**: desktop, complete balanced Hero and clear pricing comparison.
- Also spot-check ~320px and 1440px if time allows.
- Zoom 200%, keyboard tab, contrast/focus, labels, form errors, CTA targets.

## 11. Quick anti-template quality gate
Does the result look like *QuickPOS* rather than generic SaaS? Is the POS mockup custom and realistic? Can a visitor understand the benefit in 5 seconds? Are mobile pages actually composed, not only shrunk? Are all buttons functional? Is copy specific and typo-free? If not, iterate in the QA phase.
