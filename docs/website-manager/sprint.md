# Sprint — week van 19 mei 2026

**PM beslissing genomen op:** 02-05-2026 (Product Manager Agent — volledige cyclus: Analytics Agent `ga4_fetch.py` + `analytics_report.md`, Marketing Research Agent + webcheck concurrentie, Social Media Agent `weekly_calendar.md`, synthese)  
**Doel deze sprint:** **Geen nieuwe URL’s** — wel betere **doorstroom** vanaf pagina’s met korte verblijftijd of hoge landingsbounce: vroege CTA op Systemen, FAQ zichtbaar gekoppeld vanaf diensten/projecten/contact/prijsindicatie, stadspagina’s + home deeplink schuimbeton.  
**Meetdoel:** Per **16 juni 2026** in GA4: stijging sessieduur op `/systemen-producten.html`; eerste sessies op `/faq.html` (ook klein); waar mogelijk tweede pagina per sessie vanaf stadspagina’s.

---

## Goedgekeurde taken voor Developer Agent

### Taak 1: Vroege CTA op `systemen-producten.html` `[GOEDGEKEURD]`

**Bron:** Analytics Agent (2 mei) — korte gemiddelde tijd op pagina  
**Prioriteit:** Hoog  
**Type:** conversie

**Actie:** Direct **onder** de `page-hero`, vóór de eerste inhoudssectie (`section-muted` met kaarten), een **`cta-band`** plaatsen: korte kop, korte tekst met optionele link naar `faq.html`, primaire knop naar `prijsindicatie.html`. Geen dubbele copy van de bestaande CTA onderaan — andere invalshoek (“past bij jouw vloer / twijfel tussen systemen”).

**Succescriterium:** Op desktop en mobiel zichtbare CTA zonder scroll op gangbare viewport; werkende links.

---

### Taak 2: Interne links naar `faq.html` + prijsindicatie-hub `[GOEDGEKEURD]`

**Bron:** Analytics + Marketing Research (update 2 mei)  
**Prioriteit:** Hoog  
**Type:** SEO / interne structuur

**Actie:**

- `diensten.html`: in de bestaande korte regio-/werkgebied-paragraaf (onder de kaarten) natuurlijke zin met link naar `faq.html` (ankertekst: “veelgestelde vragen” of gelijkwaardig).
- `projecten.html`: in de **hero** (bij de bestaande uitleg) één zin met links naar `faq.html` en `prijsindicatie.html`.
- `contact.html`: onder de **hero-lead** één regel (`small`) met link naar `faq.html` (voor bezoekers die eerst zelf willen lezen).
- `prijsindicatie.html`: in de **hero-lead** korte verwijzing naar `faq.html` (infrezen / warmtepomp / kosten — geen keyword-stuffing).

**Succescriterium:** Geen broken links; minimaal vier inkomende routes naar FAQ vanaf gezagdragende pagina’s (naast home/nav/footer).

---

### Taak 3: Stadspagina’s — FAQ-doorverwijzing onder hero `[GOEDGEKEURD]`

**Bron:** Analytics (landingsbounce stadspagina’s)  
**Prioriteit:** Midden  
**Type:** SEO / conversie

**Actie:** Op `vloerverwarming-groningen.html`, `vloerverwarming-assen.html` en `vloerverwarming-zuidlaren.html` direct onder het **hero-CTA-blok** één regel `small` met link naar `faq.html` (nuchtere formulering).

**Succescriterium:** Zichtbaar zonder scroll op gangbare telefoonviewport; consistente tone tussen de drie pagina’s.

---

### Taak 4: Home — deeplink schuimbeton in stap 2 `[GOEDGEKEURD]`

**Bron:** Marketing Research (schuimbeton als USP + bestaand anker `diensten.html#schuimbeton`)  
**Prioriteit:** Midden  
**Type:** SEO

**Actie:** Op `index.html` in de sectie “Onze aanpak in 4 stappen”, stap 2: het woord **schuimbeton** linken naar `diensten.html#schuimbeton` (alleen dat woord linken, geen hele zin).

**Succescriterium:** Link resolveert; geen visuele breuk.

---

## Uitgestelde voorstellen `[WACHT]`

- **Lege GA4-landing** (`landingPagePlusQueryString` leeg) — eerst segmentanalyse door Hans/PM; geen code tot oorzaak vaststaat.
- **`logo-varianten.html` / 301** — afhankelijk van hosting; geen GitHub-Pages-serverredirect in repo.
- **`calculator_complete`** apart event — eerst overlap met `wizard_calculate` / `calculator_result` uitzetten in GA4.

---

## Afgewezen voorstellen `[AFGEWEZEN]`

- **Nieuwe landingspagina deze sprint** — max. 1 nieuwe pagina-regel is recent gebruikt voor FAQ; kwaliteit boven extra URL’s.

---

## Social Media

**Status:** Weekplanning staat in `docs/website-manager/social/weekly_calendar.md` (week van 19 mei 2026)  
**Actie vereist:** Handmatige publicatie door VLWarmte team.

---

## Context voor volgende sprint

- Opnieuw GSC/GA4 kijken naar **`/faq.html`** query’s en CTR.  
- Wanneer projectfoto’s beschikbaar zijn: **`projecten.html`** en evt. stadspagina’s uitbreiden (materiaalafhankelijk).

---

## Developer Rapport — 2 mei 2026 (avond, PM-cyclus)

**Taak 1 — Vroege CTA `systemen-producten.html`:** klaar. `cta-band` direct onder `page-hero` met link naar FAQ en knop naar prijsindicatie.

**Taak 2 — Interne links FAQ + hub:** klaar. Aanpassingen op `diensten.html`, `projecten.html`, `contact.html`, `prijsindicatie.html`.

**Taak 3 — Stadspagina’s:** klaar. FAQ-regel onder hero op `vloerverwarming-groningen.html`, `vloerverwarming-assen.html`, `vloerverwarming-zuidlaren.html`.

**Taak 4 — Home schuimbeton-deeplink:** klaar. `index.html` stap 2: woord schuimbeton linkt naar `diensten.html#schuimbeton`.

**Analytics stack:** `.venv` in repo met `google-analytics-data`; `ga4_fetch.py` succesvol gedraaid (zie `ga4_report.json` timestamp).

**Tests:** `bash tests/smoke/navigation-links.sh` en `bash tests/smoke/form-behavior.sh` → PASS.
