# Sprint — week van 18 mei 2026 (cyclus 5)

**PM beslissing genomen op:** 08-05-2026 (cyclus 5 — verse GA4-fetch; cyclus 4 staat gearchiveerd; vorige sprint-deploys zijn live).  
**Doel deze sprint:** **Restverkeer opruimen** (logo-varianten) en **interne klikpaden + lokale CTA's** versterken op pagina's die nog single-page bounce **1,0** laten zien (stadspagina Assen, systemen, projecten). Snippet `over-ons` aanscherpen voor lokale relevantie.  
**Meetdoel:** Per **15 juni 2026** in GA4: minder sessies op `/logo-varianten.html` (richting 0), lagere single-page bounce op `/vloerverwarming-assen.html` en `/over-ons.html`, meer secundaire pageviews via interne links vanaf `/` en `/diensten.html` naar `/systemen-producten.html` en `/projecten.html`.

---

## Goedgekeurde taken voor Developer Agent

### Taak 1: `logo-varianten.html` — vervangen door redirect-pagina `[GOEDGEKEURD]`

**Bron:** Analytics — nog **7** sessies/30 dagen op `/logo-varianten.html` (bounce **0,86**) ondanks dat de pagina geen functie meer heeft. Marketing: opschonen + GBP/SEO-ruis weg.  
**Prioriteit:** Hoog  
**Type:** SEO / cleanup

**Actie:** Vervang de inhoud van `logo-varianten.html` door een **minimale redirect-pagina** naar `/`:
- `<title>` en `<meta name="description">`: kort en feitelijk (bijv. *"VLWarmte — pagina verplaatst"*).
- `<link rel="canonical" href="https://www.vlwarmte.nl/">`.
- `<meta http-equiv="refresh" content="0; url=/">`.
- `<noscript>` + zichtbare link "Ga naar de homepage".
- `robots`: `noindex, follow`.
- GA4-snippet behouden (huidig template) zodat eventueel restverkeer nog gemeten wordt.

**Succescriterium:** `curl -sI https://www.vlwarmte.nl/logo-varianten.html` levert 200 (GitHub Pages), maar de body bevat een meta-refresh + canonical naar `/`; geen verwijzingen naar de pagina in `sitemap.xml` of navigatie (nog steeds afwezig).

---

### Taak 2: `over-ons.html` — head SEO refresh `[GOEDGEKEURD]`

**Bron:** Analytics — landing bounce **0,78** op 9 sessies, 0 conversies; snippet kan beter regio + traject + ervaring laten zien.  
**Prioriteit:** Hoog  
**Type:** SEO

**Actie:** Pas in `<head>` aan: `<title>`, `<meta name="description">`, `og:title`, `og:description`, `twitter:title`, `twitter:description`. Verwerk:
- **Zuidlaren** als thuisbasis, werkgebied **Drenthe / Groningen / Friesland**.
- **Compleet traject** (ondervloer, schuimbeton, installatie, dekvloer) — **één partij** voor het hele traject.
- Korte, nuchtere toonzetting (geen "marktleider", geen "beste").

**Succescriterium:** H1, hero en body ongewijzigd; canonical blijft `over-ons.html`.

---

### Taak 3: `vloerverwarming-assen.html` — vroege CTA-band + interne link `[GOEDGEKEURD]`

**Bron:** Analytics — landing bounce **1,0** op 6 sessies, 0 conversies. Stadspagina krijgt verkeer maar geen vervolgstap.  
**Prioriteit:** Hoog  
**Type:** CTA + interne linking

**Actie:**
1. Voeg vroeg in de pagina (boven of vlak na de hero) dezelfde **`cta-band-stack`**-component toe als op `systemen-producten.html` (cyclus 4): drie knoppen — **Prijsindicatie**, **FAQ**, **Terugbelverzoek** (`contact.html?modus=bel#aanvraag`).
2. Voeg in de body één korte zin toe met interne link naar `werkwijze.html` ("Lees onze werkwijze"). Houd de bestaande tekstuele inhoud verder ongewijzigd.

**Succescriterium:** Geen tweede `<h1>`; knoppen gebruiken bestaande `.cta-band-stack` styling; mobiel leesbaar.

---

### Taak 4: Stadspagina-cluster — onderlinge kruisverwijzing `[GOEDGEKEURD]`

**Bron:** Marketing/Analytics — `vloerverwarming-assen.html`, `vloerverwarming-groningen.html`, `vloerverwarming-zuidlaren.html` zijn afzonderlijke landings; onderling niet zichtbaar gelinkt → geen secundaire klik bij een mismatch in regio.  
**Prioriteit:** Midden  
**Type:** Interne linking / SEO

**Actie:** Voeg op alle drie stadspagina's onderaan (boven footer of in laatste sectie) een klein blok **"Ook actief in:"** met links naar de twee zusterstadspagina's. Korte zin ervoor, bijv.: *"Werkt vanuit Zuid-Laren door heel Noord-Nederland — bekijk ook onze pagina's voor [zusterstad 1] en [zusterstad 2]."*

**Succescriterium:** Geen extra `<h1>`; consistent in alle drie pagina's; werkt op mobiel.

---

### Taak 5: Interne links — `index.html` en `diensten.html` naar systemen + projecten `[GOEDGEKEURD]`

**Bron:** Analytics — `systemen-producten.html` (7 sessies, bounce 1,0) en `projecten.html` (6 sessies, bounce 1,0) zijn als landing zwak. Vanaf homepage en `diensten.html` wordt er weinig naartoe geklikt.  
**Prioriteit:** Midden  
**Type:** Interne linking / CTA

**Actie:**
1. Op `index.html`: zoek de bestaande sectie waar diensten of werkwijze worden genoemd. Voeg twee duidelijke tekstlinks of kleine knoppen toe: **"Bekijk onze systemen"** → `systemen-producten.html`, **"Bekijk projecten"** → `projecten.html`. Niet als CTA-balk; geïntegreerd in lopende tekst of als secundair link-rijtje.
2. Op `diensten.html`: in de sectie waar de aanpak/traject beschreven staat, voeg dezelfde twee links toe (één keer per pagina, ergens halverwege en/of onderaan voor de footer-CTA).

**Succescriterium:** Geen wijziging aan hero of head; links zichtbaar maar niet opdringerig; bestaande conversie-CTA's (prijsindicatie, contact) blijven dominant.

---

## Uitgestelde voorstellen `[WACHT]`

- **Tweede RSA (`google_ads_add_rsa_variant.py --apply`)** — dry-run is OK; wacht op expliciete chat-goedkeuring vóór `--apply`. Geen spend-go-live nodig (campagne staat al ENABLED), wel mutatie.
- **GA4 ↔ Google Ads koppeling + conversieacties** — vereist admin in GA4 en Ads UI. Niet via developer-script; agendeer als losse PM-actie zodra admin-toegang gevalideerd is.
- **WoW-sessiedaling 134 → 54** — PM-hypothesetabel (seizoen, indexering, Ads-budget) volgt buiten developer-sprint; één correctieve actie volgende cyclus.
- **Disclaimer/privacy bounce 1,0** — verwacht patroon, klein cohort. Pas opnieuw kijken bij hoger volume.
- **`scripts/ga4_fetch.py` uitbreiden met eventnamen + exit-pages** — geeft volgende cyclus rijkere analyse, maar geen directe leadimpact deze week.

---

## Afgewezen voorstellen `[AFGEWEZEN]`

- **Nieuwe pagina's** — niet deze sprint.
- **Nieuwe prijscalculator** — bestaande `prijsindicatie.html` voldoet (bevestigd in research-rapport).

---

## Social Media

**Status:** `docs/website-manager/social/weekly_calendar.md` — **week van 11 mei 2026** (3× LinkedIn, 4× Instagram).  
**Actie vereist:** Handmatige publicatie door VLWarmte team.

---

## Pilot — weer-accent (`proposals.md` voorstel 10)

**Lopend:** start 8 mei 2026, evaluatie uiterlijk **4 juni 2026**. Resultaat dan in `proposals.md` vastleggen: doorzetten, bijsturen of afronden.

---

## Context voor volgende sprint

- Effect van cyclus 4 SEO-snippets en CTA's pas na 2–4 weken zichtbaar in GA4 en Search Console.
- Paid Search **12 / 0** blijft op de monitor; volgende cyclus uitsluitsel over GA4 ↔ Ads-koppeling.
- Logo-varianten-redirect: meten of sessies daadwerkelijk dalen of dat externe links blijven aanvoeren.
- Interne linkhervorming → kijken of secundaire pageviews stijgen op systemen/projecten en stadspagina's.

---

## Developer Rapport — 2026-05-08

- **Geïmplementeerde taken:** Taak 1 t/m 5 (alle `[GOEDGEKEURD]` in cyclus 5).
- **Overgeslagen taken:** geen.
- **Deployment:** **Nog niet live** — PM voert `git commit` + `git push origin main` uit; daarna GitHub Actions / Pages.
- **Live URL (na deploy):** https://www.vlwarmte.nl
- **Smoke-tests:** `tests/smoke/navigation-links.sh` — **PASS**; `tests/smoke/form-behavior.sh` — **PASS**.
- **Aandachtspunten:** Geen secrets in deze wijzigingen. `logo-varianten.html` is bewust minimaal (geen volledige site-nav); staat ook niet in de smoke-lijst met pagina’s.

### Per taak

| Taak | Bestand(en) | Wat gedaan | Smoke |
| --- | --- | --- | --- |
| 1 | `logo-varianten.html` | Minimale doorverwijspagina: `noindex,follow`, canonical naar homepage, `meta http-equiv="refresh"` naar `/`, zichtbare link + `noscript`, GA4 (`ga-deferred.js`) behouden. Geen wijziging `sitemap.xml` (URL stond er al niet in). | Zie repo-smoke (PASS) |
| 2 | `over-ons.html` | Alleen `<head>`: `title`, meta description, `og:*`, `twitter:*` — Zuidlaren, werkgebied drie provincies, compleet traject (ondervloer t/m dekvloer), één partij; H1/body ongewijzigd. | Zie repo-smoke (PASS) |
| 3 | `vloerverwarming-assen.html` | Direct na hero: `cta-band` + `cta-band-stack` (prijsindicatie, FAQ, terugbelverzoek). In eerste body-sectie: zin met link naar `werkwijze.html`. | Zie repo-smoke (PASS) |
| 4 | `vloerverwarming-assen.html`, `vloerverwarming-groningen.html`, `vloerverwarming-zuidlaren.html` | Sectie **Ook actief in:** met kruislinks naar de twee andere stadspagina’s, vóór de slot-CTA, `h2` (geen extra `h1`). | Zie repo-smoke (PASS) |
| 5 | `index.html`, `diensten.html` | Secundaire tekstlinks *Bekijk onze systemen* / *Bekijk projecten* (geen hero-/head-wijziging). | Zie repo-smoke (PASS) |
