# Sprint — week van 9 juni 2026

**PM beslissing genomen op:** 08-05-2026 (cyclus 3 — archive vorige sprint; analytics op bestaande GA4-export; marketing korte WebSearch; developer + PM commit/push).  
**Doel deze sprint:** **Vorige sprint live zetten** én **organische snippet + lichte CTA’s** versterken (werkwijze/over-ons SEO, terugbel op diensten/FAQ, homepage-meta) zodat de funnel richting prijs/contact duidelijker wordt.  
**Meetdoel:** Per **5 juli 2026** in GA4: stijging `wizard_start` of `contact_submit` vanaf `/diensten.html` of `/faq.html`; bounce **werkwijze**-landing niet hoger dan nu; minstens één **Paid Search**-conversie óf duidelijk lagere bounce op `/prijsindicatie.html`-landing.

---

## Goedgekeurde taken voor Developer Agent

### Taak 0: Repo-sync vorige sprint `[GOEDGEKEURD]`

**Bron:** PM — vorige sprint stond geïmplementeerd maar niet op `origin/main`.  
**Prioriteit:** Hoog  
**Type:** release

**Actie:** Geen extra code — wijzigingen uit sprint week 2 juni (`prijsindicatie.html` CTA-band, `disclaimer.html` + `privacy.html` exits, `projecten.html` hero-soft-row, `google_ads_lead_campaign_defaults.json` indien nog niet op main) gaan **in dezelfde commit** mee als onderstaande taken.

**Succescriterium:** `git diff` toont die bestanden mee in de release-commit.

---

### Taak 1: `werkwijze.html` — lokale SEO in head `[GOEDGEKEURD]`

**Bron:** Analytics — korte sessies op werkwijze; snippet miste expliciete regio/traject-hint.  
**Prioriteit:** Hoog  
**Type:** SEO

**Actie:** Pas `<title>`, `<meta name="description">`, `og:title`, `og:description`, `twitter:title`, `twitter:description` aan: noem **Zuidlaren**, **Drenthe** (en waar passend Groningen/Friesland), en **zes stappen / traject vloerverwarming** — blijf binnen redelijke lengtes, geen keyword-stuffing.

**Succescriterium:** Eén duidelijke H1 blijft; canonical ongewijzigd; geen dubbele title-tags.

---

### Taak 2: `over-ons.html` — lokale SEO in head `[GOEDGEKEURD]`

**Bron:** Analytics — `/over-ons.html` als landing met bounce **0,78** en 0 conversies in entry-tabel.  
**Prioriteit:** Hoog  
**Type:** SEO

**Actie:** Zelfde patroon als Taak 1: title + meta + OG/Twitter met **vloerverwarmingsspecialist**, **Zuidlaren**, **Noord-Nederland** — nuchtere zin, geen superlatieven.

**Succescriterium:** H1 en inhoud ongewijzigd; alleen head-metadata.

---

### Taak 3: `diensten.html` + `faq.html` — terugbel in CTA-band `[GOEDGEKEURD]`

**Bron:** Marketing + analytics — diensten-landing bounce hoog; lichte derde stap naast prijs/FAQ.  
**Prioriteit:** Hoog  
**Type:** conversie / CTA

**Actie:** In de bestaande `cta-band-stack` (direct onder de hero) een **secundaire knop** toevoegen: tekst **„Terugbelverzoek”** of **„Laat mij terugbellen”**, link `contact.html?modus=bel#aanvraag`. Zelfde knop op **beide** pagina’s.

**Succescriterium:** Drie knoppen netjes gestapeld op smalle schermen (bestaande `.cta-band-stack`); geen tweede `h1`.

---

### Taak 4: `index.html` — meta SERP-clariteit `[GOEDGEKEURD]`

**Bron:** Analytics — homepage grootste instap; beschrijving kan **online prijsindicatie** expliciet maken voor zoeksnippet.  
**Prioriteit:** Midden  
**Type:** SEO

**Actie:** Verleng `meta name="description"` (en gelijk `og:description` + `twitter:description`) met één korte zin over **vrijblijvende online prijsindicatie** — max. ~320 tekens totaal voor description.

**Succescriterium:** Hero-HTML ongewijzigd; canonical blijft `/`.

---

## Uitgestelde voorstellen `[WACHT]`

- **Google Ads RSA live zetten / tweede RSA** — na deze deploy en met `secrets/google-ads.env` op de agent-machine.  
- **`systemen-producten.html` dieper uitmeten** — pagina heeft al vroege `cta-band`; eerst effect vorige releases meten.

---

## Afgewezen voorstellen `[AFGEWEZEN]`

- **Nieuwe landingspagina’s** — niet nodig; bestaande URL’s versterken.

---

## Social Media

**Status:** `docs/website-manager/social/weekly_calendar.md` — **week van 9 juni 2026**.  
**Actie vereist:** Handmatige publicatie door VLWarmte team.

---

## Pilot — weer-accent (workshop, `proposals.md` voorstel 10)

**Lopend:** start 8 mei 2026, evaluatie uiterlijk 4 juni 2026. Onveranderd t.o.v. vorige sprint.

---

## Context voor volgende sprint

- Verifiëren of **Paid Search** conversies oplopen na live copy + CTA’s.  
- `calculator_complete` / `wizard_calculate` in GA4 gebruiken voor wizard-funnel.

---

## Developer Rapport — 8 mei 2026 (cyclus 3)

### Geïmplementeerde taken

- **Taak 0 — vorige sprint mee in release:** `prijsindicatie.html` (CTA-band), `disclaimer.html` + `privacy.html` (exit onder hero), `projecten.html` (`hero-soft-row`); defaults JSON stond al op main.
- **Taak 1 — `werkwijze.html`:** title + meta + OG/Twitter met Zuidlaren/Drenthe en traject/prijsindicatie.
- **Taak 2 — `over-ons.html`:** title + meta + OG/Twitter met specialist Zuidlaren/Noord-Nederland.
- **Taak 3 — `diensten.html` + `faq.html`:** knop **Terugbelverzoek** → `contact.html?modus=bel#aanvraag`.
- **Taak 4 — `index.html`:** meta/og/twitter description met online prijsindicatie.

### Kwaliteit

- `tests/smoke/navigation-links.sh` — **PASS**
- `tests/smoke/form-behavior.sh` — **PASS**

### Deployment

- **Status:** door **Product Manager** — `git push origin main` voltooid. **GitHub Actions:** run **25554936393** (`pages-build-deployment`, succes). **Commit:** `1d6bc5e`. Live-check: `Terugbelverzoek` zichtbaar op `https://www.vlwarmte.nl/diensten.html`.
