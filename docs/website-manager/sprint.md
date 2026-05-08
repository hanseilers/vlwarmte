# Sprint — week van 2 juni 2026

**PM beslissing genomen op:** 08-05-2026 (tweede volledige cyclus dezelfde dag: Analytics-fetch → rapporten → social → sprint → developer → **PM commit+push**).  
**Doel deze sprint:** **Paid + organische funnel naar prijsindicatie/contact versterken** — wizard zichtbaarder vóór scroll; juridische pagina’s geen dood spoor; projecten-page lichte informatie-route; RSA-headlines in defaults afgestemd op richtbedrag.  
**Meetdoel:** Per **12 juni 2026** in GA4: bounce op `/prijsindicatie.html`-landing ≤0,65 óf ≥1 **Paid Search**-conversie; disclaimer/privacy-landings <1,0 bounce of duidelijk tweede hit.

---

## Goedgekeurde taken voor Developer Agent

### Taak 1: `prijsindicatie.html` — CTA-band boven de wizard `[GOEDGEKEURD]`

**Bron:** Analytics — prijsindicatie converteert sterk; extra vertrouwen + **anker `#wizard`** helpt scroll-gedrag en koppelt offerte-route (cpc).  
**Prioriteit:** Hoog  
**Type:** conversie

**Actie:** Direct onder `page-hero`, vóór de wizard-sectie: een **`section` + `cta-band`** met korte uitleg (geen account), knoppen **Start de wizard** (`href="#wizard"`) en **Direct offerte aanvragen** (`contact.html?modus=offerte#aanvraag`), plus link naar informatieformulier in de tekst.

**Succescriterium:** Eerste viewport toont duidelijk pad naar wizard én offerte; geen dubbele `h1`; wizard-ID `#wizard` blijft werken.

---

### Taak 2: `scripts/data/google_ads_lead_campaign_defaults.json` — RSA-headlines prijsfokus `[GOEDGEKEURD]`

**Bron:** Marketing — Paid Search 11 sessies, 0 conversies; headlines moeten **prijsindicatie** en **richtbedrag** expliciet noemen (binnen 30 tekens).  
**Prioriteit:** Hoog  
**Type:** betaald / copy in repo

**Actie:** Vervang drie bestaande headlines door: **"Online prijsindicatie"**, **"Richtbedrag in minuten"**, **"Eerst prijs dan offerte"** (uniek, ≤30 tekens). Geen wijziging aan `final_urls` in deze taak.

**Succescriterium:** JSON blijft valide; `python -m json.tool` slaagt; eventueel `google_ads_create_search_campaign.py --dry-run` alleen als er een test-campagne wordt aangemaakt (niet verplicht voor bestaande campagne — wijziging is voor **volgende** API-deploy of handmatige RSA-sync).

---

### Taak 3: `disclaimer.html` + `privacy.html` — exitlinks onder hero `[GOEDGEKEURD]`

**Bron:** Analytics — beide als landing **bounce 1,0**, 6–7 sessies; snelle exit naar homepage/prijs/contact verlaagt doodlopend gevoel.

**Actie:** Onder `page-hero`, vóór de bestaande content-sectie: compacte **`<section class="section">`** met links naar `/`, `prijsindicatie.html`, `contact.html?modus=informatie#aanvraag`.

**Succescriterium:** Geen wijziging aan juridische tekst zelf; alleen navigatiehulp; geen tweede `h1`.

---

### Taak 4: `projecten.html` — `hero-soft-row` informatie-CTA `[GOEDGEKEURD]`

**Bron:** Analytics — landing bounce **1,0**; pagina heeft al knoppen maar mist expliciet **licht** contactpad zoals op stadspagina’s.

**Actie:** Onder `hero-cta-row` een **`hero-soft-row`** met korte intro + knop **Informatie aanvragen** naar `contact.html?modus=informatie#aanvraag`.

**Succescriterium:** Zelfde CSS-patroon als stadspagina’s; geen conflicterende `h1`.

---

## Uitgestelde voorstellen `[WACHT]`

- **Bestaande Search-campagne RSA’s bijwerken in Google Ads** — na defaults-wijziging: agent draait mutatie of UI; niet in deze HTML-sprint.
- **Stadspagina’s** — cohort klein; meten na live push.

---

## Afgewezen voorstellen `[AFGEWEZEN]`

- **Nieuwe landingspagina’s** — niet nodig; bestaande URL’s versterken.

---

## Social Media

**Status:** `docs/website-manager/social/weekly_calendar.md` — **week van 2 juni 2026**.  
**Actie vereist:** Handmatige publicatie door VLWarmte team.

---

## Pilot — weer-accent (workshop, `proposals.md` voorstel 10)

**Start:** **8 mei 2026** (vandaag). **Eind (evaluatie):** **4 juni 2026** (vier weken, 28 dagen).  
**Afspraken:** koel-story **A**; homepage-teaser **B** (handmatig per week); max. **1** post/week met weer-hook; **°C** uit openbaar weerbericht toegestaan. Volledige onderbouwing en checklist: `docs/website-manager/proposals.md`.

---

## Context voor volgende sprint

- Controleren of Paid Search conversies verschijnen na copy + live CTA’s.
- `calculator_complete` data gebruiken voor wizard-drop-off.

---

## Developer Rapport — 8 mei 2026 (avond, cyclus 2)

### Geïmplementeerde taken

- **Taak 1 — `prijsindicatie.html`:** CTA-band boven wizard met ankers en offerte/informatie-links.
- **Taak 2 — `google_ads_lead_campaign_defaults.json`:** Drie prijsgerichte RSA-headlines.
- **Taak 3 — `disclaimer.html` + `privacy.html`:** Navigatie-exit onder hero.
- **Taak 4 — `projecten.html`:** `hero-soft-row` met informatie-aanvraag.

### Kwaliteit

- `tests/smoke/navigation-links.sh` — **PASS**
- `tests/smoke/form-behavior.sh` — **PASS**

### Deployment

- **Status:** door **Product Manager** — `git commit` + `git push origin main` (stap 7b playbook). **Commit:** `bab08a8` — GitHub Actions-run: na `git push` controleren met `gh run list`.
