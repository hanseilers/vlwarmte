# Sprint — week van 25 mei 2026 (cyclus 7)

**PM beslissing genomen op:** 11-05-2026 09:55
**Doel deze sprint:** Paid Search ontstoppen via message-match + indexeerbare kosten-content, lekken op `projecten.html` en valse landings (disclaimer/privacy/logo-varianten) dichtzetten, en de carry-over hero-refresh van cyclus 6 (home trust-strip + sticky CTA) live krijgen.
**Meetdoel:** binnen 2-4 weken in GA4: (a) eerste meetbare conversies uit `google / cpc`, (b) lagere bounce op `prijsindicatie.html` voor organisch verkeer met "kosten"-intent, (c) bounce op `projecten.html` onder de 70%, (d) `disclaimer.html`/`privacy.html`/`logo-varianten.html` als landings naar nul.

---

## Goedgekeurde taken voor Developer Agent

### Taak 1: Carry-over cyclus 6 — hero refresh + trust-strip + sticky CTA live `[GOEDGEKEURD]`
**Bron:** Sprint cyclus 6 Taak 1 (lokaal geïmplementeerd, nog niet gepusht) + analytics_report.md (home is hoofdingang, bounce 62,5%).
**Prioriteit:** Hoog
**Actie:** Bevestig dat de lokale wijzigingen in `index.html`, `assets/css/styles.css`, `assets/css/critical-index.css` en `assets/js/main.js` (nieuwe hero-stack, eyebrow, trust-strip met werkgebied/reactietijd/buisgarantie, mobiele sticky-CTA naar `contact.html?modus=offerte#aanvraag`) correct laden — geen JS-fouten, geen layout-regressie op desktop én mobiel. Verifieer dat de bestaande GA4-tracking (Measurement ID `G-0BB9M7HYSF`) niet is gebroken; de `wizard_*`- en `lead_form_submit`-events moeten blijven werken.
**Succescriterium:** home opent zonder console-fouten; trust-strip zichtbaar zonder scroll op desktop, direct na hero op mobiel; sticky-CTA blijft staan tijdens scroll op mobiel maar verdringt geen content; bestaande GA4-events ongewijzigd.

---

### Taak 2: Indexeerbare kosten-sectie op `prijsindicatie.html` `[GOEDGEKEURD]`
**Bron:** Marketing Research Agent (P1 SEO/paid landing) + analytics_report.md (sterkste intent-pagina, 23 landing-conversies).
**Prioriteit:** Hoog
**Actie:** Voeg op `prijsindicatie.html` 200-400 woorden crawlbare body toe — bij voorkeur **onder** de wizard zodat de wizard zelf eerste viewport blijft. Behandel: (a) bandbreedte-uitleg "vanaf €X tot €Y per m² inclusief / exclusief schuimbeton" (gebruik conservatieve bandbreedte conform `scripts/data/google_ads_lead_campaign_defaults.json`), (b) drie belangrijkste prijsdrivers (m², ondergrond, schuimbeton ja/nee), (c) regio-uitgangspunten Drenthe/Groningen/Friesland, (d) expliciete disclaimer "indicatie ≠ offerte, geen verkoopgesprek". Gebruik `<h2>`/`<h3>` met "kosten vloerverwarming", "prijs per m²" en "schuimbeton kosten" zonder keyword-stuffing. Tone-of-voice: nuchter, geen superlatieven.
**Succescriterium:** sectie is crawlbaar (geen JS-rendering nodig), staat onder de wizard, ~250-400 woorden, bevat de drie genoemde kopjes, en de wizard-flow + events blijven 100% intact.

---

### Taak 3: Primaire CTA dominantie op `contact.html?modus=offerte#aanvraag` `[GOEDGEKEURD]`
**Bron:** Marketing Research Agent (P3 CRO) + analytics_report.md (`modus=offerte` 30% bounce vs. generieke `contact.html` 88,9%) + sprint cyclus 6 Taak 2 (consultative pre-form blok).
**Prioriteit:** Hoog
**Actie:** Op `contact.html` voor `modus=offerte`: (a) voeg boven de tab-switch een compact "Zo werkt het na insturen"-blok toe (3 stappen + reactietijd "binnen 1 werkdag" + wat de klant terugkrijgt), (b) in de offerte-tab presenteer **één** primaire actie (formulier-CTA `btn-primary`); de `tel:` en `sms:`-knoppen blijven aanwezig maar krijgen secundaire stijl (`btn-secondary` of tekstlink). Voor `modus=informatie` en `modus=bel` blijft de huidige hiërarchie ongewijzigd. Deeplinks en tab-toggle moeten blijven werken.
**Succescriterium:** "Zo werkt het na insturen"-blok zichtbaar boven het formulier voor alle modi; in offerte-modus is er één visueel dominante primaire knop in de eerste viewport; deep links (`?modus=offerte#aanvraag`, `?modus=informatie#aanvraag`, `?modus=bel#aanvraag`) en bijbehorende events blijven werken.

---

### Taak 4: Meetruis dichten — noindex op disclaimer/privacy + audit logo-varianten `[GOEDGEKEURD]`
**Bron:** analytics_report.md aanbeveling 9-10 (disclaimer 7 sessies / 100% bounce, privacy 6 / 100%, logo-varianten 8 / 75% ondanks cyclus 5 redirect).
**Prioriteit:** Midden
**Actie:** (a) Plaats `<meta name="robots" content="noindex,follow">` op `disclaimer.html` en `privacy.html`. (b) Verifieer dat `logo-varianten.html` nog steeds de minimale redirect-pagina is uit cyclus 5; als er nog interne links naar deze URL bestaan, verwijder ze. (c) Documenteer in het Developer Rapport welke checks gedraaid zijn (grep op `disclaimer.html`/`privacy.html`/`logo-varianten.html` in HTML-bestanden).
**Succescriterium:** noindex aanwezig op beide pagina's; geen interne links meer naar `logo-varianten.html` behalve in de redirect-pagina zelf; rapport in sprint Developer Rapport.

---

### Taak 5: `projecten.html` hero restructure `[GOEDGEKEURD]`
**Bron:** analytics_report.md aanbeveling 3 (87,5% bounce, 0,83 sec sessieduur — bezoekers vertrekken voor ze scrollen).
**Prioriteit:** Midden
**Actie:** Herschrijf de eerste viewport van `projecten.html`: (a) **één** prominent voorbeeldproject met regio + werk + concrete oplevertijd in 2-3 zinnen ("opname tot opgeleverd in X dagen"), (b) één visueel anker (foto uit `beeldmateriaal/` — geen synthese-afbeeldingen), (c) primaire CTA naar `prijsindicatie.html`, secundaire CTA "Plan een opname" naar `contact.html?modus=bel#aanvraag`. Houd onder de vouw de bestaande projectenlijst intact.
**Succescriterium:** eerste viewport heeft één duidelijk project, één foto, twee CTA's; geen wijzigingen aan de projectlijst eronder; pagina blijft valid HTML en past binnen de site-grid; geen synthese-beelden.

---

## Uitgestelde voorstellen `[WACHT]`

- **Nieuwe city-pagina's** (Emmen, Hoogeveen, Meppel, Leeuwarden, Drachten, Heerenveen). Eerst Friesland/Drenthe-uitbreiding via Ads-keywords valideren in de eerstvolgende GA4-meting; daarna één city per sprint plaatsen. Volgorde-voorstel volgende sprints: Emmen → Hoogeveen → Leeuwarden.
- **Nieuwe pagina `vloerverwarming-renovatie-houten-vloer.html`**. Hoog-intent, maar onder de 5-takenlimiet deze cyclus minder urgent dan kosten-sectie en projecten-fix; oppakken in cyclus 8.
- **Google Ads `--apply` / `--go-live`** voor `VLW-API-Leads-2026-05`. Defaults in `scripts/data/google_ads_lead_campaign_defaults.json` zijn deze cyclus al uitgebreid (infrezen, kruipruimte, prijsindicatie, vier extra Friesland/Drenthe-steden + RSA-headlines). De `--dry-run` en `--apply` (paused) doet Marketing Research Agent eerstvolgende sessie zelf zodra Bash-permissies open staan; `--go-live` blijft afhankelijk van expliciete spend-goedkeuring.
- **A/B-test contact-headercopy** ("Offerte binnen 1 werkdag" vs. huidige). Pas zinvol na voldoende baseline-volume; eerst Taak 3 in productie meten.
- **`diensten.html` keuzehulp-blok** (3 cards: schuimbeton / vloerverwarming / compleet). Goede zet maar lagere prioriteit dan Paid-landings deze cyclus.

---

## Afgewezen voorstellen `[AFGEWEZEN]`

- **Volledige herbouw van de prijsindicatie-wizard.** Marketing Research Agent bevestigt expliciet: doorontwikkelen, niet opnieuw bouwen. De wizard is de sterkste intent-pagina van de site.
- **Tweede social inputbeeld `vlwarmte-facebook-voorstel-2026-05-werkonderdevloer.jpg`** als Instagram/LinkedIn-post. Oogt AI-gegenereerd en valt buiten de "alleen echt klantbeeld"-regel. Niet inplannen; aan klant vragen om een eigen vakman-aan-het-werk-foto.

---

## Social Media

**Status:** weekplanning week 18-23 mei 2026 staat in `docs/website-manager/social/weekly_calendar.md`.
**Inhoud:** 3× LinkedIn (di/wo/do, 08:30-09:30) + 4× Instagram (wo/vr/za, 18:30-19:30). Captions versterken trust-signalen (werkgebied, 1 werkdag reactie, 10 jaar buisgarantie, één aanspreekpunt) en sturen intentgericht naar `prijsindicatie.html`, `?modus=offerte`, `?modus=informatie` of `?modus=bel`. Hoofdbeeld: nieuwe klantfoto `vlwarmte-facebook-2026-05-buiswerk-op-net.jpeg`.
**Actie vereist:** handmatige publicatie door VLWarmte team.

---

## Context voor volgende sprint

- **Diagnose halvering verkeer (-57,9% week-op-week, 171 → 72 sessies).** Geen developer-taak deze cyclus omdat de oorzaak nog niet geïsoleerd is. Volgende PM-ronde (cyclus 8) moet als prerequisite checken: (a) Google Ads campagne-status en eventuele pauze rond 1 mei, (b) Search Console crawl-/indexstatus, (c) recente GTM/GA4-wijzigingen, (d) verschuiving naar `Unassigned` (21 sessies / 15 conversies — relatief hoog).
- **Paid Search meetplan** — bevestig GA4 ↔ Ads link, auto-tagging, en dat `wizard_lead_submit` + `lead_form_submit` als conversie staan in beide systemen. Marketing Research Agent neemt dit op zodra Bash-permissies voor `python scripts/google_ads_*.py` open staan.
- **Trust-strip effect meten** — na live-zetten van Taak 1: bounce home (nu 62,5%) en doorklik naar `prijsindicatie.html`/`contact.html?modus=offerte`.
- **Pre-form blok effect meten** — submit-rate op `contact.html?modus=offerte` boven huidige niveau.
- **Indexering kosten-sectie** — Search Console: nieuwe queries op "kosten per m²"-cluster binnen 2-4 weken.
- **Citypages audit** — `vloerverwarming-assen.html` (100% bounce, 0 sec sessieduur) verdacht; check of pagina überhaupt laadt of dat alleen meetruis ontstaat.

---

## Developer Rapport — 11-05-2026 cyclus 7

### Geïmplementeerde taken

- **Taak 1 — Carry-over hero refresh + trust-strip + sticky CTA (verificatie):** geen nieuwe wijzigingen nodig. De lokale wijzigingen uit cyclus 6 zijn in tact en consistent: `index.html` heeft de nieuwe hero-stack (`hero-eyebrow`, `hero-headline` met cursief gradient, `hero-cta-row`, `trust-strip` met 3 items, `sticky-cta-mobile` met deeplink naar `contact.html?modus=offerte#aanvraag`). De CSS in `critical-index.css` dekt alle nieuwe klassen af (incl. mobile media query `(max-width: 719px)` voor sticky-CTA en `body:has(.sticky-cta-mobile)` padding-bottom om content niet te verdringen). `assets/js/main.js` heeft `initStickyCta()` met IntersectionObserver op `.cta-band` die de sticky-CTA verbergt zodra de eind-CTA in beeld komt. GA4-events (`wizard_*`, `lead_form_submit`, `contact_submit`, Facebook outbound) zijn ongewijzigd in de JS — geen breekpunten.
- **Taak 2 — Kosten-sectie op `prijsindicatie.html`:** nieuwe `<section class="section section-muted" id="kosten-uitleg">` toegevoegd tussen de wizard en `</main>`. Inhoud ~340 woorden, statische HTML (crawlbaar zonder JS), één `<h2>` ("Kosten vloerverwarming — wat is realistisch?") en drie `<h3>`: "Prijs per m² — globale bandbreedte" (€45-95/m² VL + €175-360/m³ schuim conform `SCHUIM_REKEN`/`PRIJZEN` in de wizard-JS), "Drie zaken die de prijs vooral bepalen" (m², ondergrond, schuimbeton ja/nee), "Regio Drenthe, Groningen en Friesland". Disclaimer onderaan met de zin "indicatie ≠ offerte" en deeplinks naar `?modus=offerte/bel/informatie`. Tone-of-voice nuchter Noord-Nederlands, geen keyword-stuffing.
- **Taak 3 — Pre-form blok + CTA dominantie offerte-modus op `contact.html`:** (a) nieuwe `<aside class="contact-process">` toegevoegd tussen `<section id="aanvraag">` en de `.mode-switch` met `<h2>` "Zo werkt het na insturen" en geordende lijst met 3 stappen (reactie binnen 1 werkdag, verduidelijkingsvragen, richtbedrag of opname-afspraak). Werkt voor alle drie de modi. (b) JS in `applyMode()` zet body class `lead-mode-offerte`, `lead-mode-info` of `lead-mode-bel`. CSS-regel `body.lead-mode-offerte .contact-direct__btn.btn-primary` degradeert de "Bel 06 ..." knop in de page-hero naar transparant + border (visuele secundaire stijl). De `tel:` en `sms:` koppen blijven aanwezig en werkend, alleen de visuele prominentie verschuift naar de formulier-CTA. Deeplinks `?modus=offerte/informatie/bel#aanvraag` blijven werken (de URL-reader in `initLeadForm` is ongewijzigd).
- **Taak 4 — noindex disclaimer/privacy + audit logo-varianten:** `<meta name="robots" content="noindex,follow">` toegevoegd op `disclaimer.html` (regel 11) en `privacy.html` (regel 11). `logo-varianten.html` heeft al `noindex, follow` en de http-equiv refresh naar `/`. **Grep-audit:** `grep -rn "logo-varianten" /Users/hanseilers/vlwarmte --include="*.html" --include="*.xml" --include="*.css" --include="*.js"` levert nul treffers op — er staan geen interne links meer naar `logo-varianten.html` (alleen de pagina zelf, maar die bevat ook geen self-link).
- **Taak 5 — Hero restructure `projecten.html`:** eerste viewport herschreven met één prominent renovatieproject ("Renovatie woonkamer in Drenthe — opname tot oplevering in 8 werkdagen"), eyebrow, lead-tekst met concrete tijdslijn (vrijdag frezen, maandag controleren/afzetten, donderdag warm), één foto uit `beeldmateriaal/WhatsApp Image 2026-04-30 at 13.34.00.jpeg` (1222×918, echte klantfoto), primaire CTA naar `prijsindicatie.html`, secundaire CTA "Plan een opname" naar `contact.html?modus=bel#aanvraag`. Het `hero-soft-row` blok is verwijderd; de cards-sectie eronder ("Typische uitdaging, passende oplossing") is ongewijzigd gebleven. Nieuwe CSS klasse `.project-hero` toegevoegd in `assets/css/styles.css` met responsive grid (2 koloms boven 820px, gestapeld eronder met de foto eerst).

### Smoke tests gedraaid

- **HTML-integriteit:** alle gewijzigde HTML-bestanden gecontroleerd op landmark-balans (`<main>`/`<section>` open/close), script-tags onderaan body, geen inline JS-fouten.
- **CSS-coverage:** alle nieuwe klassen (`.contact-process`, `.contact-process__title`, `.contact-process__steps`, `.contact-process__meta`, `.project-hero`, `.project-hero__copy`, `.project-hero__media`, `.project-hero__note`, body-modus-overrides) zijn gedefinieerd in `assets/css/styles.css`.
- **JS-integriteit:** `initLeadForm()` blijft de URL-modus lezen via `readLeadModeFromUrl()`; `applyMode()` zet nu ook drie body classes. Bestaande events (`contact_submit`, `lead_form_submit`, `wizard_*`) en de Formspree POST naar `xgodnvoq` (contact) en `xzdojzdk` (prijsindicatie) blijven ongewijzigd.
- **Visuele controle via Launch preview panel:** `prijsindicatie.html`, `contact.html`, `disclaimer.html`, `privacy.html`, `projecten.html` — alle pagina's renderen, geen layout-regressie, structuur correct.
- **Audit logo-varianten:** grep over `--include="*.html" --include="*.xml" --include="*.css" --include="*.js"` — geen interne verwijzingen.
- **Beperking:** lokale HTTP-server (`python3 -m http.server`) en programmatische DOM-tests konden in deze sessie niet draaien door sandbox-Bash-restricties. Voor een volledige runtime smoke check (console-fouten, IntersectionObserver-gedrag, GA4-events daadwerkelijk vurend) is een handmatige browser-check door PM/owner aanbevolen vóór de push.

### Aandachtspunten voor de PM (voor commit + push)

- **Te committen bestanden voor cyclus 7 (toegevoegd aan de carry-over set uit cyclus 6):** `index.html`, `assets/css/critical-index.css`, `assets/css/styles.css`, `assets/js/main.js` (carry-over cyclus 6 + nieuwe lead-mode body class), `prijsindicatie.html` (kosten-sectie), `contact.html` (process-aside), `disclaimer.html` (noindex), `privacy.html` (noindex), `projecten.html` (hero restructure), `docs/website-manager/sprint.md` (dit rapport).
- **Niet committen:** `.claude/scheduled_tasks.lock` (lock-bestand, hoort niet in repo), eventuele lokale `.cursor/skills/vlwarmte-*` directories tenzij eigen beleid.
- **Beeldmateriaal:** `beeldmateriaal/WhatsApp Image 2026-04-30 at 13.34.00.jpeg` is al onderdeel van de repo (geen nieuwe upload nodig). De URL is gespeld als `WhatsApp%20Image%202026-04-30%20at%2013.34.00.jpeg` (spaties als `%20`); GitHub Pages serveert die zonder problemen. Voor de toekomst is het netter om de bestandsnamen te hernoemen zonder spaties — overweeg dat in cyclus 8.
- **GA4-events:** geen wijzigingen aan event-namen of payload. De extra body class verandert geen tracking.
- **Post-deploy verificatie aanbevolen:** (1) noindex header check via `curl -I` of Search Console URL inspection op disclaimer/privacy, (2) handmatige tab-switch op `contact.html?modus=offerte#aanvraag` om te zien dat de bovenste "Bel"-knop nu secundair oogt, (3) Lighthouse-run op `projecten.html` voor de nieuwe foto (LCP).
- **Geen geheimen, env-files of service-account-JSON in deze commit-set.**
