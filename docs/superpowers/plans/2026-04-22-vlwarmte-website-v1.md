# VLWarmte Website v1 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build and launch a modern static multi-page VLWarmte website that informs first, then converts visitors to information/offerte requests.

**Architecture:** Use a static HTML/CSS/JS architecture with one shared stylesheet and one shared script file. Pages share a reusable layout pattern (header, hero/page intro, content sections, CTA band, footer) while each page has unique SEO metadata and content tailored to the approved design specification.

**Tech Stack:** HTML5, CSS3, vanilla JavaScript, optional lightweight shell-based smoke checks.

---

## Planned File Structure

**Create**

- `index.html` - homepage with value proposition and conversion entry points
- `diensten.html` - services from underfloor prep to finishing
- `systemen-producten.html` - systems, materials, and selection guidance
- `werkwijze.html` - step-by-step project process
- `over-ons.html` - company story and trust content
- `projecten.html` - project listing templates/placeholders
- `contact.html` - information/offerte form flow
- `disclaimer.html` - legal disclaimer page
- `privacy.html` - privacy statement page
- `assets/css/styles.css` - global styles, layout, components, responsive rules
- `assets/js/main.js` - mobile nav toggle, FAQ accordion, form mode switch, inline validation
- `assets/img/` - image placeholder directory (real assets later)
- `tests/smoke/navigation-links.sh` - verifies links and key page markers
- `tests/smoke/form-behavior.sh` - checks required form states and fields

**Modify**

- `.gitignore` - ignore `.superpowers/` sessions if missing

---

### Task 1: Project Scaffold and Shared Layout Foundation

**Files:**

- Create: `index.html`
- Create: `assets/css/styles.css`
- Create: `assets/js/main.js`
- Modify: `.gitignore`
- Test: `tests/smoke/navigation-links.sh`

- [ ] **Step 1: Write the failing test**

```bash
#!/usr/bin/env bash
set -euo pipefail

test -f index.html
test -f assets/css/styles.css
test -f assets/js/main.js
rg -q "<header" index.html
rg -q "Informatie / Offerte aanvragen" index.html
```

- [ ] **Step 2: Run test to verify it fails**

Run: `bash tests/smoke/navigation-links.sh`  
Expected: FAIL because files do not exist yet.

- [ ] **Step 3: Write minimal implementation**

```html
<!-- index.html -->
<!doctype html>
<html lang="nl">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>VLWarmte | Vloerverwarming van ondervloer tot oplevering</title>
    <meta
      name="description"
      content="VLWarmte realiseert complete vloerverwarmingsoplossingen in Noord-Nederland: ondervloer, schuimbeton, installatie en afwerking."
    />
    <link rel="stylesheet" href="assets/css/styles.css" />
  </head>
  <body>
    <header class="site-header">...</header>
    <main>...</main>
    <footer class="site-footer">...</footer>
    <script src="assets/js/main.js"></script>
  </body>
</html>
```

```css
/* assets/css/styles.css */
:root {
  --brand: #d94a2b;
  --ink: #1e2430;
  --bg: #f7f8fb;
}
body {
  margin: 0;
  font-family: Inter, Arial, sans-serif;
  color: var(--ink);
  background: #fff;
}
.container {
  width: min(1120px, 92vw);
  margin: 0 auto;
}
```

```javascript
// assets/js/main.js
document.addEventListener("DOMContentLoaded", () => {
  const navToggle = document.querySelector("[data-nav-toggle]");
  const nav = document.querySelector("[data-nav]");
  if (navToggle && nav)
    navToggle.addEventListener("click", () => nav.classList.toggle("is-open"));
});
```

- [ ] **Step 4: Run test to verify it passes**

Run: `bash tests/smoke/navigation-links.sh`  
Expected: PASS.

- [ ] **Step 5: Commit**

```bash
git add index.html assets/css/styles.css assets/js/main.js tests/smoke/navigation-links.sh .gitignore
git commit -m "feat: scaffold vlwarmte static site foundation"
```

---

### Task 2: Build Core Content Pages and Global Navigation

**Files:**

- Create: `diensten.html`
- Create: `systemen-producten.html`
- Create: `werkwijze.html`
- Create: `over-ons.html`
- Create: `projecten.html`
- Create: `contact.html`
- Create: `disclaimer.html`
- Create: `privacy.html`
- Modify: `index.html`
- Test: `tests/smoke/navigation-links.sh`

- [ ] **Step 1: Write the failing test**

```bash
#!/usr/bin/env bash
set -euo pipefail

for f in index.html diensten.html systemen-producten.html werkwijze.html over-ons.html projecten.html contact.html disclaimer.html privacy.html; do
  test -f "$f"
done

rg -q 'href="diensten.html"' index.html
rg -q 'href="contact.html"' werkwijze.html
rg -q "<h1" contact.html
```

- [ ] **Step 2: Run test to verify it fails**

Run: `bash tests/smoke/navigation-links.sh`  
Expected: FAIL because pages/links are not complete.

- [ ] **Step 3: Write minimal implementation**

```html
<!-- diensten.html -->
<main>
  <section class="page-hero">
    <h1>Diensten van ondervloer tot oplevering</h1>
  </section>
  <section>
    <h2>Ondervloer voorbereiding</h2>
    ...
  </section>
  <section>
    <h2>Schuimbeton isolatie</h2>
    ...
  </section>
  <section>
    <h2>Vloerverwarming aanleg</h2>
    ...
  </section>
  <section>
    <h2>Dekvloer en afwerking</h2>
    ...
  </section>
</main>
```

```html
<!-- contact.html -->
<main>
  <section class="page-hero"><h1>Informatie of offerte aanvragen</h1></section>
  <form id="lead-form">...</form>
</main>
```

- [ ] **Step 4: Run test to verify it passes**

Run: `bash tests/smoke/navigation-links.sh`  
Expected: PASS.

- [ ] **Step 5: Commit**

```bash
git add index.html diensten.html systemen-producten.html werkwijze.html over-ons.html projecten.html contact.html disclaimer.html privacy.html tests/smoke/navigation-links.sh
git commit -m "feat: add vlwarmte multi-page structure and navigation"
```

---

### Task 3: Implement Approved Visual System and Responsive Components

**Files:**

- Modify: `assets/css/styles.css`
- Modify: `index.html`
- Modify: `diensten.html`
- Modify: `systemen-producten.html`
- Modify: `werkwijze.html`
- Modify: `over-ons.html`
- Modify: `projecten.html`
- Modify: `contact.html`
- Test: `tests/smoke/navigation-links.sh`

- [ ] **Step 1: Write the failing test**

```bash
#!/usr/bin/env bash
set -euo pipefail

rg -q -- "--brand" assets/css/styles.css
rg -q -- ".hero" assets/css/styles.css
rg -q -- "@media (max-width: 900px)" assets/css/styles.css
rg -q -- "Informatie / Offerte aanvragen" index.html
```

- [ ] **Step 2: Run test to verify it fails**

Run: `bash tests/smoke/navigation-links.sh`  
Expected: FAIL on missing design tokens/responsive rules/content markers.

- [ ] **Step 3: Write minimal implementation**

```css
/* assets/css/styles.css */
:root {
  --brand: #d94a2b;
  --brand-dark: #b63d24;
  --ink: #1f2937;
  --muted: #5b6677;
  --surface: #f6f7fb;
  --radius: 14px;
}
.hero {
  padding: 5rem 0 3rem;
  background: linear-gradient(180deg, #fff 0%, var(--surface) 100%);
}
.btn-primary {
  background: var(--brand);
  color: #fff;
  border-radius: 999px;
}
.card {
  border-radius: var(--radius);
  box-shadow: 0 8px 24px rgba(20, 32, 60, 0.08);
}
@media (max-width: 900px) {
  .nav {
    display: none;
  }
  .nav.is-open {
    display: block;
  }
}
```

```html
<!-- index.html -->
<section class="hero">
  <h1>Vloerverwarming van ondervloer tot afgewerkte oplevering</h1>
  <p>
    Een partner voor voorbereiding, schuimbeton, installatie en afwerking in
    Noord-Nederland.
  </p>
  <a class="btn-primary" href="contact.html">Informatie / Offerte aanvragen</a>
</section>
```

- [ ] **Step 4: Run test to verify it passes**

Run: `bash tests/smoke/navigation-links.sh`  
Expected: PASS.

- [ ] **Step 5: Commit**

```bash
git add assets/css/styles.css index.html diensten.html systemen-producten.html werkwijze.html over-ons.html projecten.html contact.html tests/smoke/navigation-links.sh
git commit -m "feat: apply approved hybrid visual direction and responsive ui"
```

---

### Task 4: Contact Flow Logic, Form Modes, and Validation

**Files:**

- Modify: `contact.html`
- Modify: `assets/js/main.js`
- Test: `tests/smoke/form-behavior.sh`

- [ ] **Step 1: Write the failing test**

```bash
#!/usr/bin/env bash
set -euo pipefail

rg -q 'data-mode="info"' contact.html
rg -q 'data-mode="offerte"' contact.html
rg -q 'name="m2"' contact.html
rg -q "validateLeadForm" assets/js/main.js
```

- [ ] **Step 2: Run test to verify it fails**

Run: `bash tests/smoke/form-behavior.sh`  
Expected: FAIL because mode toggles/validation are missing.

- [ ] **Step 3: Write minimal implementation**

```html
<!-- contact.html -->
<div class="mode-switch">
  <button type="button" data-lead-mode="info">Ik wil eerst informatie</button>
  <button type="button" data-lead-mode="offerte">Ik wil een offerte</button>
</div>
<form id="lead-form" novalidate>
  <input name="name" required />
  <input name="phone" required />
  <input name="email" type="email" required />
  <input name="m2" data-mode="offerte" />
  <select name="ondergrond" data-mode="offerte">
    ...
  </select>
</form>
```

```javascript
// assets/js/main.js
function validateLeadForm(form, mode) {
  const required = ["name", "phone", "email"];
  if (mode === "offerte") required.push("m2", "ondergrond");
  return required.every(
    (field) => form.elements[field] && form.elements[field].value.trim(),
  );
}
```

- [ ] **Step 4: Run test to verify it passes**

Run: `bash tests/smoke/form-behavior.sh`  
Expected: PASS.

- [ ] **Step 5: Commit**

```bash
git add contact.html assets/js/main.js tests/smoke/form-behavior.sh
git commit -m "feat: add information-offerte form flow with inline validation"
```

---

### Task 5: SEO, Accessibility, and Trust Content Hardening

**Files:**

- Modify: `index.html`
- Modify: `diensten.html`
- Modify: `systemen-producten.html`
- Modify: `werkwijze.html`
- Modify: `over-ons.html`
- Modify: `projecten.html`
- Modify: `contact.html`
- Modify: `disclaimer.html`
- Modify: `privacy.html`
- Modify: `assets/css/styles.css`
- Test: `tests/smoke/navigation-links.sh`

- [ ] **Step 1: Write the failing test**

```bash
#!/usr/bin/env bash
set -euo pipefail

for f in index.html diensten.html systemen-producten.html werkwijze.html over-ons.html projecten.html contact.html; do
  rg -q "<title>" "$f"
  rg -q 'meta name="description"' "$f"
  rg -q "<h1" "$f"
done

rg -q "aria-" contact.html
rg -q 'href="privacy.html"' index.html
rg -q 'href="disclaimer.html"' index.html
```

- [ ] **Step 2: Run test to verify it fails**

Run: `bash tests/smoke/navigation-links.sh`  
Expected: FAIL until metadata/accessibility/legal links are complete.

- [ ] **Step 3: Write minimal implementation**

```html
<!-- any core page -->
<title>Diensten vloerverwarming | VLWarmte Noord-Nederland</title>
<meta name="description" content="..." />
<h1>...</h1>
```

```html
<!-- footer snippet -->
<a href="privacy.html">Privacy</a>
<a href="disclaimer.html">Disclaimer</a>
```

- [ ] **Step 4: Run test to verify it passes**

Run: `bash tests/smoke/navigation-links.sh`  
Expected: PASS.

- [ ] **Step 5: Commit**

```bash
git add index.html diensten.html systemen-producten.html werkwijze.html over-ons.html projecten.html contact.html disclaimer.html privacy.html assets/css/styles.css tests/smoke/navigation-links.sh
git commit -m "feat: harden seo accessibility and legal trust content"
```

---

### Task 6: Final Verification and Delivery Readiness

**Files:**

- Modify: `README.md` (if needed; create if absent)
- Modify: `tests/smoke/navigation-links.sh`
- Modify: `tests/smoke/form-behavior.sh`

- [ ] **Step 1: Write the failing test**

```bash
#!/usr/bin/env bash
set -euo pipefail

test -f tests/smoke/navigation-links.sh
test -f tests/smoke/form-behavior.sh
test -f README.md
```

- [ ] **Step 2: Run test to verify it fails**

Run: `bash tests/smoke/navigation-links.sh && bash tests/smoke/form-behavior.sh`  
Expected: FAIL if docs/test run instructions are incomplete.

- [ ] **Step 3: Write minimal implementation**

```markdown
<!-- README.md -->

# VLWarmte Website

## Local usage

- Open `index.html` directly, or serve with a static server.

## Smoke checks

- `bash tests/smoke/navigation-links.sh`
- `bash tests/smoke/form-behavior.sh`
```

- [ ] **Step 4: Run test to verify it passes**

Run: `bash tests/smoke/navigation-links.sh && bash tests/smoke/form-behavior.sh`  
Expected: PASS.

- [ ] **Step 5: Commit**

```bash
git add README.md tests/smoke/navigation-links.sh tests/smoke/form-behavior.sh
git commit -m "chore: document runbook and finalize website smoke checks"
```

---

## Spec Coverage Check

- Site scope (multi-page core): covered by Tasks 1-2.
- Content model per page: covered by Task 2, refined in Task 5.
- Visual direction C (hybrid): covered by Task 3.
- Functional form flow (info vs offerte): covered by Task 4.
- SEO/accessibility/legal requirements: covered by Task 5.
- Delivery readiness and verification: covered by Task 6.

No uncovered spec requirements found.

## Placeholder Scan and Consistency Check

- No TODO/TBD placeholders in task instructions.
- All referenced paths are explicit.
- Commands and expectations are defined per task.
- Form function naming (`validateLeadForm`) is consistent within the plan.
