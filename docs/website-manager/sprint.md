# Sprint — week van 18 mei 2026

**PM beslissing genomen op:** 07-05-2026 (Product Manager Agent — verse `ga4_report.json` 7 mei, synthese met bestaand `research_report.md` 6 mei, social kalender vernieuwd)
**Doel deze sprint:** **Dode URL’s dichten en eerste scherm op diensten/werkwijze versterken** — contact- en prijsindicatie-paden uit sprint 11 mei geven al eerste positieve signalen; nu focus op restverkeer naar verwijderde logo-URL en op landings die nog 0 conversies en hoge bounce tonen (`diensten.html`, korte sessies op `werkwijze.html`). Geen nieuwe stads-URL’s.
**Meetdoel:** Per **4 juni 2026** in GA4: bounce `diensten.html`-landing <0,70; `werkwijze.html` gem. sessieduur >25 s of hogere scrolledUsers; sessies op `/logo-varianten.html` lopen via redirect (bounce daar lager of verdwenen als aparte dead-end). *(Script-fix: `weekly_trend` heeft nu structureel 8 weken — zie taak 4.)*

---

## Goedgekeurde taken voor Developer Agent

### Taak 1: `logo-varianten.html` — lichte redirect-landingspagina `[GOEDGEKEURD]`

**Bron:** Analytics 7 mei — oude URL trekt nog ~9 sessies; deels inconsistente paginatitel (404) in export.
**Prioriteit:** Hoog
**Type:** SEO / technisch

**Actie:** Voeg opnieuw een **minimale** `logo-varianten.html` toe in de site-root (GitHub Pages heeft geen server-side 301):

- `<link rel="canonical" href="https://www.vlwarmte.nl/">`
- `<meta http-equiv="refresh" content="0;url=https://www.vlwarmte.nl/">` **of** `content="3;url=..."` als je liever een klikbare fallback toont (kies één; 0 is strakker).
- In `<body>`: één zin + zichtbare link “Ga naar de homepage” voor gebruikers zonder meta-refresh.
- Geen zware styling — mag hergebruik maken van bestaande `critical-index`/`styles` indien nodig voor leesbaarheid; geen nieuwe marketingcopy.

**Succescriterium:** Bezoek van `/logo-varianten.html` eindigt op homepage; geen broken asset; Lighthouse/validator: geen errors; GA4 telt nog hooguit korte sessie op die URL daarna (acceptabel).

---

### Taak 2: `diensten.html` — compact CTA-blok direct onder hero `[GOEDGEKEURD]`

**Bron:** Analytics — landing `diensten.html`: 13 sessies, bounce **0,77**, **0 conversions**.
**Prioriteit:** Hoog
**Type:** conversie / SEO-gedrag

**Actie:** Direct onder `page-hero` (vóór de kaarten-sectie) een **`cta-band`** plaatsen analoog aan `systemen-producten.html`:

- Primair: `prijsindicatie.html` (richtbedrag).
- Secundair: `faq.html` (snelle antwoorden).
- Korte nuchtere regel copy, mobile-eerst.

**Succescriterium:** Op iPhone-viewport (375 breed) zijn beide paden zichtbaar zonder scroll; geen dubbele CTA’s die bestaande onderste bands overbodig maken — onderaan mag blijven zoals het is.

---

### Taak 3: `werkwijze.html` — vroege CTA onder hero `[GOEDGEKEURD]`

**Bron:** Analytics — gemiddelde sessieduur **~15 s**, `scrolledUsers` laag t.o.v. andere pagina’s; eerste `cta-band` staat nu pas na het zes-stappen-grid.
**Prioriteit:** Hoog
**Type:** conversie

**Actie:** Direct onder `page-hero` een compacte **`cta-band`** toevoegen (zelfde bouwstenen als taak 2: prijsindicatie + FAQ, eventueel derde zachte link `contact.html?modus=informatie#aanvraag`). De bestaande `cta-band` halverwege de pagina **blijft staan** (dubbele herinnering is acceptabel op lange pagina).

**Succescriterium:** Bezoeker ziet binnen eerste scherm een duidelijke vervolgstap; markup en heading-hiërarchie blijven logisch (`h1` in hero, daarna `h2` in cta-band).

---

### Taak 4: `scripts/ga4_fetch.py` — `weekly_trend` altijd 8 datapunten `[GOEDGEKEURD]` *(code reeds 7 mei — developer bevestigt)*

**Bron:** Analytics — oude export had soms <8 weken doordat GA4 geen rij teruggeeft bij 0 sessies.
**Prioriteit:** Midden
**Type:** data-pijplijn

**Actie:** In de loop die de acht weken opbouwt: bij lege `rows` een rij met `"sessions": "0"`, `"activeUsers": "0"` plus `week_start`/`week_end` appenden. **Status 7 mei:** wijziging staat in `scripts/ga4_fetch.py`; `ga4_report.json` is opnieuw gegenereerd met **8** weken.

**Succescriterium:** Na pull: `jq '.weekly_trend | length' docs/website-manager/ga4_report.json` → `8` (reeds waar na laatste fetch).

---

### Taak 5: `over-ons.html` — compact CTA-blok direct onder hero `[GOEDGEKEURD]`

**Bron:** Analytics — 18 sessies op `/over-ons.html`; eerste inhoud is pas het tweekoloms-blok na de hero — vergelijkbaar met `werkwijze.html` mist een vroege vervolgstap.
**Prioriteit:** Midden
**Type:** conversie

**Actie:** Direct onder `page-hero` een **`cta-band`** plaatsen: primair `prijsindicatie.html`, secundair `contact.html?modus=informatie#aanvraag` (lichtere stap dan offerte). Korte copy in tone-of-voice (nuchter, Noord-Nederlands).

**Succescriterium:** Zichtbaar op eerste scherm mobiel; geen conflicterende dubbele `h1`; bestaande secties daaronder ongewijzigd qua inhoud.

---

## Uitgestelde voorstellen `[WACHT]`

- **Stadspagina’s als landing (bounce 1,00)** — eerst meten na vorige sprint-CTA’s; geen extra copy voordat cohort groot genoeg is.
- **`projecten.html` met echte cases** — wacht op klant-akkoord (Marketing Research #3).
- **Google Search Console service account + Search Console API** — te groot voor deze sprint; blijft prio voor volgende ronde.
- **Google Bedrijfsprofiel** — off-site, eigenaar.

---

## Afgewezen voorstellen `[AFGEWEZEN]`

- **Nieuwe stad/dorp-pagina** — zelfde beleid: pas bij GSC-signaal.
- **Wizard aanpassen** — converteert sterk; alleen meten en monitoren (`calculator_complete`).

---

## Social Media

**Status:** Weekplanning staat in `docs/website-manager/social/weekly_calendar.md` (week van **18 mei 2026**).
**Actie vereist:** Handmatige publicatie door VLWarmte team.

---

## Context voor volgende sprint

- **Effect contact-CTA’s en stadspagina-soft-row** afwachten in GA4 (2–3 weken na 7 mei).
- **`calculator_complete`** data opbouwen voor funnel-analyse.
- **GSC-koppeling** blijft grootste SEO-blocker voor organische interpretatie.

---

## Developer Rapport — 7 mei 2026 (avond)

### Geïmplementeerde taken
- **Taak 1 — `logo-varianten.html`:** Nieuwe minimale pagina met `noindex`, canonical naar `https://www.vlwarmte.nl/`, `meta refresh` 0 naar homepage, header/footer-structuur zoals andere pagina’s, zichtbare knop “Ga naar de homepage”.
- **Taak 2 — `diensten.html`:** `cta-band` direct onder `page-hero` met prijsindicatie (primair) en FAQ (secundair) via `.cta-band-stack`.
- **Taak 3 — `werkwijze.html`:** Zelfde patroon onder de hero met prijsindicatie, FAQ en `contact.html?modus=informatie#aanvraag`; bestaande `cta-band` halverwege de pagina ongewijzigd.
- **Taak 4 — `scripts/ga4_fetch.py`:** Backfill van lege weekresponses met `sessions`/`activeUsers` `"0"`; lokaal gevalideerd met `jq '.weekly_trend | length'` → **8**.
- **Taak 5 — `over-ons.html`:** `cta-band` onder de hero met prijsindicatie en informatie-dieplink naar contact.

### Aanvullend
- **`assets/css/styles.css`:** class `.cta-band-stack` voor verticale knoppenrij in `cta-band`.

### Overgeslagen taken
- Geen — alle `[GOEDGEKEURD]` taken zijn uitgevoerd.

### Kwaliteit
- `tests/smoke/navigation-links.sh` — **PASS**
- `tests/smoke/form-behavior.sh` — **PASS**

### Deployment
- **Status:** na `git push origin main` — GitHub Pages workflow (run-id volgt in release-notes bij eerste groene run).
- **Live URL:** https://www.vlwarmte.nl

### Aandachtspunten volgende sprint
- In GA4 monitoren of `/logo-varianten.html` nog als aparte landings-URL voorkomt en of bounce op `diensten.html`/`werkwijze.html` daalt.
- Eventueel tweede commit om release-notes deploymentregel aan te vullen met exacte GitHub Actions run-id (indien nog placeholder bij merge).
