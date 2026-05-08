# Sprint — week van 16 juni 2026

**PM beslissing genomen op:** 08-05-2026 (cyclus 4 — verse GA4-fetch; archive sprint week 9 juni; developer + PM commit/push).  
**Doel deze sprint:** **Landings-SERP en tweede stap** verbeteren waar bounce hoog blijft: **diensten**, **contact**, **systemen**, **projecten**, **FAQ** — alles binnen bestaande URL’s, met nadruk op **Zuidlaren** en **terugbelverzoek** naast prijs/FAQ.  
**Meetdoel:** Per **12 juli 2026** in GA4: lagere bounce op `/diensten.html`- en `/contact.html`-landing óf meer `contact_submit` / terugbel-gerelateerde sessies; Paid Search nog steeds monitoren (12 sessies / 0 conv in huidige export).

---

## Goedgekeurde taken voor Developer Agent

### Taak 1: `diensten.html` — head SEO `[GOEDGEKEURD]`

**Bron:** Analytics — landing bounce **~0,79** (14 sessies); snippet nog generiek.  
**Prioriteit:** Hoog  
**Type:** SEO

**Actie:** Pas `<title>`, `<meta name="description">`, `og:title`, `og:description`, `twitter:title`, `twitter:description` aan: **Zuidlaren**, **Drenthe** (en waar passend Groningen/Friesland), **traject** ondervloer–oplevering, **vrijblijvende prijsindicatie**, licht contact/terugbel (zonder overdrijven).

**Succescriterium:** H1 en body ongewijzigd; canonical blijft `diensten.html`.

---

### Taak 2: `contact.html` — head SEO `[GOEDGEKEURD]`

**Bron:** Analytics — landing bounce **0,86** (7 sessies); pagina heeft al sterke directe routes in de hero.  
**Prioriteit:** Hoog  
**Type:** SEO

**Actie:** Title + alle meta/OG/Twitter-descriptions: expliciet **informatie**, **offerte**, **terugbelverzoek**, **Zuidlaren**, **reactie binnen één werkdag** (nuchtere zin).

**Succescriterium:** Geen wijziging aan formulier of hero-body; alleen `<head>`.

---

### Taak 3: `systemen-producten.html` — head SEO + terugbel in CTA-band `[GOEDGEKEURD]`

**Bron:** Analytics + marketing — landing bounce **1,0** (kleine cohort); korte sessieduur op pagina-niveau.  
**Prioriteit:** Hoog  
**Type:** SEO + CTA

**Actie:** (1) Head: title + meta + OG/Twitter met **vergelijken vloerverwarmingssystemen**, **Zuidlaren/Noord-Nederland**, link naar **advies** en **prijsindicatie**. (2) In de bestaande vroege `cta-band-stack`: knop **Terugbelverzoek** → `contact.html?modus=bel#aanvraag`, naast prijsindicatie en FAQ.

**Succescriterium:** Geen tweede `h1`; knoppen gebruiken `.cta-band-stack`.

---

### Taak 4: `projecten.html` — terugbel in hero-soft-row `[GOEDGEKEURD]`

**Bron:** Analytics — projecten-landing bounce **1,0**.  
**Prioriteit:** Midden  
**Type:** CTA

**Actie:** In `hero-soft-row` naast **Informatie aanvragen** een tweede knop **Terugbelverzoek** (`contact.html?modus=bel#aanvraag`), zelfde button-stijl als andere soft-rows.

**Succescriterium:** Geen extra `h1`; mobiel leesbaar naast/in lijn met bestaande knop.

---

### Taak 5: `faq.html` — head SEO `[GOEDGEKEURD]`

**Bron:** Marketing — FAQ is inhoudelijk sterk; snippet kan **infrezen**, **warmtepomp**, **kosten** en route naar **prijsindicatie/terugbel** explicieter maken.  
**Prioriteit:** Midden  
**Type:** SEO

**Actie:** Title (indien nodig ingekort) + meta + OG/Twitter: bovenstaande onderwerpen + **Zuidlaren** waar natuurlijk.

**Succescriterium:** Accordion/FAQ-body ongewijzigd.

---

### Taak 6: `contact.html` — volgorde formulier vóór adreskaart `[GOEDGEKEURD]`

**Bron:** Product owner — betere flow: eerst aanvraag, daarna adres en bedrijfsgegevens.  
**Prioriteit:** Midden  
**Type:** UX / layout

**Actie:** In `<main>`: sectie met `#aanvraag` + leadformulier **boven** de sectie “Adres en bedrijfsgegevens”. `id="aanvraag"`, deep links (`?modus=…#aanvraag`, `#lead-form`) en formuliergedrag ongewijzigd.

**Succescriterium:** Geen wijziging aan velden of head; alleen volgorde van de twee secties.

---

## Uitgestelde voorstellen `[WACHT]`

- **Google Ads RSA / conversies** — na voldoende organische baseline deze sprint.  
- **Disclaimer/privacy** — exits staan live; cohort klein, pas opnieuw bijronden als volume stijgt.

---

## Afgewezen voorstellen `[AFGEWEZEN]`

- **Nieuwe pagina’s** — niet in deze sprint.

---

## Social Media

**Status:** `docs/website-manager/social/weekly_calendar.md` — **week van 16 juni 2026**.  
**Actie vereist:** Handmatige publicatie door VLWarmte team.

---

## Pilot — weer-accent (`proposals.md` voorstel 10)

**Lopend:** start 8 mei 2026, evaluatie uiterlijk **4 juni 2026**. Na die datum in `proposals.md` vastleggen: doorzetten, bijsturen of afronden.

---

## Context voor volgende sprint

- Paid Search 12 / 0 — koppeling GA4 ↔ Ads en RSA-sync blijven op de lijst.  
- Effect van snippet-wijzigingen in Search Console na 2–4 weken.

---

## Developer Rapport — 8 mei 2026 (cyclus 4)

### Geïmplementeerde taken

- **Taak 1 — `diensten.html`:** head SEO (Zuidlaren, Drenthe, traject, prijs/terugbel in snippet).
- **Taak 2 — `contact.html`:** head SEO (informatie, offerte, terugbel, Zuidlaren, werkdag).
- **Taak 3 — `systemen-producten.html`:** head SEO + **Terugbelverzoek** in vroege `cta-band`.
- **Taak 4 — `projecten.html`:** **Terugbelverzoek** in `hero-soft-row`.
- **Taak 5 — `faq.html`:** head SEO (infrezen, warmtepomp, kosten, routes).
- **Taak 6 — `contact.html`:** volgorde — leadblok (`#aanvraag`) boven “Adres en bedrijfsgegevens”.

### Kwaliteit

- `tests/smoke/navigation-links.sh` — **PASS**
- `tests/smoke/form-behavior.sh` — **PASS**

### Deployment

- **Status:** door **Product Manager** — `git push origin main` voltooid. **GitHub Actions:** run **25555351102** (`pages-build-deployment`, succes). **Commit:** `ff6c9b9`. Live-check: **Terugbelverzoek** op `https://www.vlwarmte.nl/systemen-producten.html`.
- **Taak 6 (contact volgorde):** commit **816f182**; **GitHub Actions** run **25556001845** (`pages-build-deployment`, succes). Live: `contact.html` — `#aanvraag` staat vóór “Adres en bedrijfsgegevens” (curl-check op `https://www.vlwarmte.nl/contact.html`).
