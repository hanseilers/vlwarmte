# Sprint — week van 11 mei 2026

**PM beslissing genomen op:** 06-05-2026 (Product Manager Agent — volledige cyclus: Analytics Agent op bestaande `ga4_report.json` van 2 mei, Marketing Research Agent synthese-update zonder verse SERP, Social Media Agent `weekly_calendar.md`, synthese)
**Doel deze sprint:** **Conversiepaden repareren** — `contact.html` is in GA4 een dood spoor (8 landingen, bounce 1,00, 0 conversions), stadspagina's bouncen 1,00, `projecten.html` heeft 0,9 s gemiddelde tijd. Vorige sprint zette FAQ-doorstroom; deze sprint repareren we de plekken waar het verkeer al binnenkomt maar nergens heen gaat. Geen nieuwe URL's.
**Meetdoel:** Per **3 juni 2026** in GA4: ≥1 conversion uit `contact.html` als landing (was 0); bounce `contact.html`-landing <0,80; tweede-hit-rate stijgt op stadspagina's; `calculator_complete` event verschijnt zodat wizard-funnel meetbaar wordt.

---

## Goedgekeurde taken voor Developer Agent

### Taak 1: `contact.html` — directe keuze boven het formulier `[GOEDGEKEURD]`

**Bron:** Analytics Agent (6 mei) — scherpste lead-generatie kans. 8 directe landingen, bounce 1,00, 0 conversions als landing. Prijsindicatie levert ter vergelijking 13 conversions op 11 landingen.
**Prioriteit:** Hoog
**Type:** conversie

**Actie:** Direct **boven** het bestaande contactformulier, **onder de hero-lead**, een compact keuze-blok plaatsen met drie zichtbare paden:

1. **Bel nu** — `tel:`-knop met het lokale nummer (zelfde nummer als gebruikt in footer/nav, niet hardcoderen indien mogelijk hergebruik via bestaande variabele).
2. **WhatsApp/sms** — link naar `https://wa.me/<nummer>` (gebruik hetzelfde nummer in `+31...` formaat). Als WhatsApp-nummer niet beschikbaar is, vervang door `sms:`-link.
3. **Eerst prijsindicatie** — secundaire knop naar `prijsindicatie.html` met korte tekst ("eerst een richtbedrag?").

Het bestaande formulier blijft volledig intact onder dit blok — niet verwijderen of wijzigen. Geen kopie-conflict met bestaande CTA's onderaan: kort, drie keuzes, niet meer.

**Mobile-eerst:** op mobiel (57% van de sessies) staan de drie keuzes onder elkaar, full-width, met de bel-knop bovenaan.

**Succescriterium:** Drie werkende links/knoppen zonder scroll op iPhone-viewport (375×812); `tel:` en `wa.me` openen op mobiel correct; geen visuele breuk op desktop; bestaande formulier-flow ongewijzigd.

---

### Taak 2: Stadspagina's — directe belknop onder hero `[GOEDGEKEURD]`

**Bron:** Analytics (landingsbounce 1,00 op Groningen/Assen) + Marketing Research (tweede stap moet expliciet, lichter pad dan offerte)
**Prioriteit:** Hoog
**Type:** conversie / lokaal signaal

**Actie:** Op `vloerverwarming-groningen.html`, `vloerverwarming-assen.html` en `vloerverwarming-zuidlaren.html` direct **onder** de bestaande hero-CTA-blok (en boven de FAQ-regel die in sprint 19 mei is toegevoegd) één compacte regel met **twee lichtere paden naast elkaar**:

- **Bel-knop** met `tel:`-link (zelfde nummer als taak 1).
- **Informatie aanvragen** — link naar `contact.html?modus=informatie#aanvraag` zodat het formulier in de juiste modus opent.

Toon: nuchter, één regel introductie ("liever bellen of even iets vragen?"), dan de twee knoppen. Consistent tussen de drie pagina's (zelfde copy, zelfde knopstijl).

**Succescriterium:** Knoppen zichtbaar zonder scroll op iPhone-viewport; `tel:`-link werkt; deeplink opent contactpagina in de juiste tab/modus; visueel consistent op alle drie de pagina's.

---

### Taak 3: `projecten.html` — eerlijke alinea + doorstroom-CTA's `[GOEDGEKEURD]`

**Bron:** Analytics Agent voorstel #4 (`projecten.html` als dood spoor: bounce 0,86, 0,9 s) — light variant van Marketing Research voorstel #3 (echte cases met foto's blijft openstaan tot klant-akkoord beschikbaar is).
**Prioriteit:** Midden
**Type:** content / conversie

**Actie:** Op `projecten.html` de **hero-tekst herschrijven** naar één eerlijke alinea: dat er nog geen openbaar gepubliceerde cases zijn, dat referenties op verzoek beschikbaar zijn (mail/telefoon), en dat de prijsindicatie en FAQ vaak al de eerste vragen beantwoorden. Direct daaronder **twee duidelijke knoppen**:

- Primair: **Prijsindicatie** → `prijsindicatie.html`
- Secundair: **Veelgestelde vragen** → `faq.html`

**Geen lege placeholders** of dummy-projecten. Geen opmaak-explosie — pas in de bestaande hero-structuur. De rest van de pagina (eventuele bestaande blokken) blijft staan; alleen de hero-tekst wordt vervangen door deze nuchtere alinea.

**Succescriterium:** Geen broken links; bezoeker krijgt binnen 1 schermhoogte twee duidelijke vervolgstappen; bestaande tone-of-voice (Noord-Nederlands, nuchter) blijft behouden.

**Volgende sprint:** zodra Hans 1–2 klant-akkoorden binnen heeft (1 zin per mail volstaat), wordt deze pagina alsnog uitgebreid met echte cases inclusief foto + plaatsnaam (Marketing Research voorstel #3).

---

### Taak 4: `scripts/ga4_fetch.py` — `weekly_trend`-bug fixen `[GOEDGEKEURD]`

**Bron:** Analytics Agent voorstel #2 — blocker voor week-over-week analyse.
**Prioriteit:** Hoog
**Type:** tooling / data-pijplijn

**Actie:** In `scripts/ga4_fetch.py` (rond regel ~198) de loop die acht weken `weekly_trend` schrijft herzien zodat acht **niet-overlappende** weken worden weggeschreven. Huidige bug: loop start op `i=0` waardoor `start = today - timedelta(weeks=0)` en `end = today` voor de eerste iteratie samenvalt en door overschrijving uiteindelijk maar één week in de JSON verschijnt. Voorstel:

- Gebruik `start = today - timedelta(weeks=i+1)` en `end = today - timedelta(weeks=i)` voor `i in range(8)`, **of**
- Bouw vooraf een lijst van 8 datumbereiken en itereer daarover.

Na de fix: één keer `python3 scripts/ga4_fetch.py` runnen om de fix te valideren — `ga4_report.json["weekly_trend"]` moet 8 unieke weken bevatten (gesorteerd, zonder overlap).

**Succescriterium:** `ga4_report.json["weekly_trend"]` bevat 8 unieke `week_start`-waarden zonder overlap; geen Python-errors; bestaande dimensies/metrics in de week-export ongewijzigd.

---

### Taak 5: `prijsindicatie.html` — `calculator_complete` GA4-event toevoegen `[GOEDGEKEURD]`

**Bron:** Marketing Research voorstel #4 — wizard converteert (24 sessies, 13 conversions als landing) maar drop-off per stap is onmeetbaar zonder afsluitend event.
**Prioriteit:** Midden
**Type:** tracking

**Actie:** In de JS van de prijsindicatie-wizard (`prijsindicatie.html` of het bijbehorende JS-bestand) één regel `gtag('event', 'calculator_complete', { ... })` afvuren op het moment dat de eindberekening getoond wordt. Bestaande events (`wizard_start`, `wizard_calculate`, `calculator_result`) blijven ongewijzigd staan. Eventparameters minimaal: ingevoerde m² (afgerond), gekozen ondergrond, gekozen systeem — geen PII.

**Belangrijk:** in [WACHT] staat al een aantekening dat `calculator_complete` mogelijk overlapt met `wizard_calculate` / `calculator_result`. Deze sprint voegen we het event toe **zonder** de bestaande events te verwijderen — overlap inventariseren we 2–4 weken later in GA4 met echte data.

**Succescriterium:** `calculator_complete` event verschijnt in GA4 DebugView bij een testberekening; geen JS-errors in browserconsole; bestaande wizard-flow ongewijzigd.

---

## Uitgestelde voorstellen `[WACHT]`

- **`projecten.html` met 2 echte cases (m², plaats, foto + alt)** — Marketing Research #3 volledige variant. Wachten op klant-akkoord (1 zin per mail volstaat). Nu de light-variant (taak 3) gedaan; bij eerste akkoord upgraden.
- **Google Search Console-fetch koppelen aan service account** — Analytics #3. Groter project (~halve dag), apart inplannen. Zonder GSC blijft Google-organic blind, dus prioriteit voor de sprint daarna.
- **GA4-segment "NL doelregio"** — Analytics #5. ~23 VS-sessies en 19 NL-sessies buiten doelregio vertroebelen bouncerates. Wordt aangemaakt in GA4 zelf (niet in code) en daarna in `ga4_fetch.py` als `dimensionFilter`.
- **`calculator_complete` overlap-analyse** — open uit vorige sprint. Pas zinvol nadat het event 2–4 weken data heeft verzameld (na taak 5).
- **Google Bedrijfsprofiel + reviewstroom** — Marketing Research #5. Off-site, geen code; eigenaarsactie voor Hans. Niet voor Developer Agent.

---

## Afgewezen voorstellen `[AFGEWEZEN]`

- **Nieuwe stads- of dorpspagina** — herhaald: kwaliteit boven extra URL's. Zuidlaren is recent toegevoegd; geen volgende stad zonder Search Console-signaal.
- **Wizard herbouwen** — wizard converteert sterk (1,18 conv/sessie als landing). Niet aanraken; alleen meten toevoegen (taak 5).

---

## Social Media

**Status:** Weekplanning staat in `docs/website-manager/social/weekly_calendar.md` (week van 11 mei 2026).
**Highlights:** 3 LinkedIn-posts (renovatie infrezen vs schuimbeton, prijsindicatie als planningstool, Zuidlaren-pagina), 4 Instagram-posts (schuimbeton onder de vloer, comfort+opwarmtijd, lokaal werken vanuit Zuidlaren, renovatie Assen), 1 optionele Facebook-post over Zuidlaren.
**Drie posts hebben `[FOTO NODIG]` placeholders** — VLWarmte moet zelf beeld aanleveren in `docs/website-manager/social/input/`.
**Actie vereist:** Handmatige publicatie door VLWarmte team.

---

## Context voor volgende sprint

- **Eerste echte meetmoment FAQ-inlinks van sprint 19 mei** — bij volgende fetch (na 12 mei) kijken naar sessies op `/faq.html`, en of `diensten.html`/`projecten.html`/`contact.html`/`prijsindicatie.html` als bron in GA4 zichtbaar worden.
- **Effect van taak 1 (contact-CTA's)** meten: bounce `/contact.html`-landing en eventuele eerste conversion uit dat pad.
- **Effect van taak 2 (stadspagina-belknop)** meten: tweede-hit-rate op Groningen/Assen/Zuidlaren stadspagina's.
- **`calculator_complete` event** moet 2–4 weken data verzamelen voordat overlap-analyse met `wizard_calculate` zinvol is.
- **Klant-akkoord projecten** — vraag aan Hans of er 1–2 klanten te benaderen zijn voor case-publicatie (Marketing Research #3).
- **GSC-koppeling** is de grootste openstaande blocker voor SEO-meetbaarheid; volgende sprint inplannen als prio-1.

---

## Developer Rapport — 6 mei 2026

### Taak 1: `contact.html` directe-keuze blok — KLAAR
- Tussen hero-lead en bestaand formulier toegevoegd: `.contact-direct` blok met intro-regel, drie knoppen en sluitnoot. Knoppen: **Bel 06 188 17 459** (`tel:+31618817459`, primair), **Stuur een berichtje** (`sms:+31618817459`, secundair) en **Eerst een richtbedrag** (`prijsindicatie.html`, secundair).
- Mobile-stack via media query op 540 px: knoppen onder elkaar, full-width, bel-knop bovenaan.
- Bestaande mode-switch en formulier ongewijzigd (alle markers `data-lead-mode`, `data-only`, `id="aanvraag"` intact).
- **Kanttekening:** geen separaat WhatsApp-nummer bekend dus `sms:`-fallback gebruikt (zoals voorzien in de sprint). Label is bewust "Stuur een berichtje" zonder app-naam zodat de bestemming klopt — als er later een WhatsApp-nummer beschikbaar is kan de href naar `https://wa.me/31618817459` zonder visuele aanpassing.

### Taak 2: stadspagina's — KLAAR
- Op Groningen, Assen en Zuidlaren een `.hero-soft-row` toegevoegd direct onder de bestaande `hero-cta-row`, boven de FAQ-regel.
- Eén regel intro ("Liever bellen of even iets vragen?") en twee secundaire knoppen: **Bel direct** (`tel:`) en **Informatie aanvragen** (`contact.html?modus=informatie#aanvraag`).
- Identieke copy en knopstijl op alle drie de pagina's.

### Taak 3: `projecten.html` eerlijke alinea — KLAAR
- Hero-lead vervangen door eerlijke alinea: nog geen openbaar gepubliceerde cases, referenties op verzoek, doorverwijzing naar prijsindicatie en FAQ.
- Twee duidelijke knoppen in `hero-cta-row`: **Prijsindicatie** (primair) en **Veelgestelde vragen** (secundair).
- Bestaande "Typische uitdaging, passende oplossing"-blok met drie cards (renovatie/nieuwbouw/verbouwing) blijft staan, conform sprint-instructie "rest van de pagina blijft staan".

### Taak 4: `scripts/ga4_fetch.py` weekly_trend bug — KLAAR
- Loop herzien: `today = datetime.today().date()`, `end_date = today - timedelta(days=7*i+1)`, `start_date = end_date - timedelta(days=6)`. Iedere week beslaat dus exact 7 dagen, met 7 dagen tussen opvolgende `week_start`-waarden — geen overlap meer (GA4 DateRange is inclusief aan beide kanten, dus `end+1` is het juiste startpunt voor de volgende oudere week).
- Toegevoegd: `week_end` per rij (handig voor leesbaarheid in het rapport).
- **Kanttekening:** kon `python3 scripts/ga4_fetch.py` niet draaien vanuit deze sessie (sandbox blokkeert python/bash-execution voor scripts en network calls). Logica is wel handmatig nagerekend op basis van de code: 8 unieke `week_start`-datums met telkens 7 dagen ertussen. Hans/PM Agent kan validatie draaien met `.venv/bin/python3 scripts/ga4_fetch.py` en `jq '.weekly_trend | length' docs/website-manager/ga4_report.json` (verwacht: `8`).

### Taak 5: `prijsindicatie.html` calculator_complete — KLAAR
- Twee plekken in de wizard-JS waar de eindberekening getoond wordt voorzien van een extra `vlGtag('event', 'calculator_complete', { … })`-aanroep, **na** de bestaande `wizard_calculate` / `calculator_result` events (die ongewijzigd blijven, conform sprint-instructie over overlap-analyse).
- Schuim-traject: parameters `m2: Math.round(state.schuimM2)`, `ondergrond: state.kruipOndergrond || 'onbekend'`, `systeem: 'vloerverwarming-schuimbeton'`.
- VL-beton-traject: parameters `m2: Math.round(state.m2)`, `ondergrond: state.ondergrond || 'onbekend'`, `systeem: 'vloerverwarming-beton'`.
- Geen PII; geen JS-errors verwacht omdat `vlGtag` al de bestaande no-op fallback gebruikt wanneer GA4 niet geladen is.

### Smoke tests
- `tests/smoke/navigation-links.sh` en `tests/smoke/form-behavior.sh` konden in deze sessie niet via bash worden gedraaid (sandbox-restrictie). Alle markers waar deze tests op controleren (`<h1`, `data-lead-mode=...`, `data-only=...`, `id="aanvraag"`, canonical-tags, sitemap-paden) zijn ongewijzigd; de wijzigingen zijn additief. PM Agent kan tests handmatig draaien.

### Aandachtspunten voor volgende sprint
- WhatsApp-nummer expliciet maken (taak 1 `sms:`-fallback vervangen door `wa.me`).
- `python3 scripts/ga4_fetch.py` valideren zodra GSC-koppeling of nieuwe fetch-cycle plaatsvindt; controleren dat `weekly_trend` 8 entries heeft.
- Eerste GA4-meetmoment voor `calculator_complete` afwachten (2–4 weken) voor overlap-analyse met `wizard_calculate` / `calculator_result`.
