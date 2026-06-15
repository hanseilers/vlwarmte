# Sprint — week van 15 juni 2026 (cyclus 17)

**PM beslissing genomen op:** 15 juni 2026, 06:30
**Doel deze sprint:** Gratis organisch verkeer aanboren door termen die nét buiten pagina 1 hangen over de streep te trekken, en tegelijk de homepage beter laten converteren — zodat we minder afhankelijk worden van betaald verkeer.
**Meetdoel (over 4 weken in GA4 + GSC):**
- GSC: "vloerverwarming zuidlaren" van pos 9,3 → pagina 1 (<8); "installatiebedrijf zuidlaren" van 6,5 → top 5; "vloerverwarming hoogeveen" van 10,6 → <10; eerste organische clicks > 0 op deze termen.
- GA4: organic search van 0 → minstens enkele conversies; home-bounce onder 67%; meer instroom op prijsindicatie.html.

---

## Datawaarschuwing

De GA4-data is van **8 juni** en GSC van **23 mei** — deze cyclus **niet ververst**. Oorzaak: systeem-Python is 3.9, `scripts/ga4_fetch.py` vereist 3.10+, en de venv-runner mag niet starten in de autonome modus. Beslissingen hieronder zijn gebaseerd op richting, niet op vandaag-actuele cijfers. **Fix voor volgende cyclus staat als escalatie onderaan.**

---

## Goedgekeurde taken voor Developer Agent

### Taak 1: Zuidlaren-cannibalisatie oplossen (interne links + ankertekst) `[GOEDGEKEURD]`
**Bron:** Marketing Research Agent (Taak 1) + Analytics Agent
**Prioriteit:** Hoog
**Actie:**
- In `index.html`: maak de bestaande link naar `vloerverwarming-zuidlaren.html` voorzien van exacte ankertekst, bv. "vloerverwarming Zuidlaren" i.p.v. alleen "Zuidlaren".
- Voeg op `diensten.html` en `prijsindicatie.html` elk één regel toe met een expliciete link + ankertekst "vloerverwarming Zuidlaren" naar `vloerverwarming-zuidlaren.html`, zodat Google die pagina als kanoniek voor de term gaat zien (niet die pagina's zelf).
- In `vloerverwarming-zuidlaren.html`: neem in de eerste alinea de exacte combinatie "vloerverwarming in Zuidlaren" op.
**Succescriterium:** GSC-ranking van de dedicated pagina voor "vloerverwarming zuidlaren" stijgt richting <8; homepage zakt voor die term. Geen nieuwe gebroken interne links (smoke test).

### Taak 2: Contentblok "Installatiebedrijf in Zuidlaren" op de homepage `[GOEDGEKEURD]`
**Bron:** Marketing Research Agent (Taak 2)
**Prioriteit:** Hoog
**Actie:**
- Voeg op `index.html` een kort contentblok toe (H2 + 1 alinea), in de nuchtere VLWarmte-toon, bv.:
  - H2: "Installatiebedrijf in Zuidlaren"
  - Tekst: "VLWarmte is het installatiebedrijf in Zuidlaren voor complete vloerverwarming — van ondervloer en schuimbeton tot dekvloer en oplevering. Eén aanspreekpunt, eigen ploeg, reactie binnen één werkdag."
- Controleer dat de bestaande `LocalBusiness`-schema een logisch `name`/`address` in Zuidlaren bevat (niet wijzigen als het al klopt).
**Succescriterium:** "installatiebedrijf zuidlaren" beweegt van 6,5 richting top 5; blok staat semantisch correct (één H2, valide HTML).

### Taak 3: Hoogeveen over de pagina-1-grens duwen (interne links + FAQ-schema) `[GOEDGEKEURD]`
**Bron:** Marketing Research Agent (Taak 3) + Analytics Agent
**Prioriteit:** Midden
**Actie:**
- Voeg minstens 2 interne links met exacte ankertekst "vloerverwarming Hoogeveen" toe naar `vloerverwarming-hoogeveen.html`: één vanuit `index.html` (maak de bestaande Drenthe-hub-link exact) en één vanuit een zusterpagina (bv. Assen/Emmen "Ook actief in").
- Voeg onderaan `vloerverwarming-hoogeveen.html` een korte FAQ toe (2–3 vragen, bv. "Werken jullie ook in Hollandscheveld en Fluitenberg?", "Wat kost vloerverwarming in Hoogeveen?") en markeer met geldig `FAQPage`-schema (JSON-LD, consistent met de bestaande schema-stijl op de site).
**Succescriterium:** "vloerverwarming hoogeveen" beweegt van 10,6 → <10; FAQPage-schema valideert (geen syntaxfouten in JSON-LD).

### Taak 4: Title/meta-CTR-fix homepage + zuidlaren, "Drenthe" warm houden `[GOEDGEKEURD]`
**Bron:** Analytics Agent (aanbeveling 2) + Marketing Research Agent (Taak 4) — SEO + snippet-CTR
**Prioriteit:** Hoog
**Actie:**
- Herschrijf de meta `title` en `description` van `index.html` zodat ze (a) uitnodigen tot klikken in de SERP en (b) "Drenthe" expliciet bevatten zolang er nog geen dedicated Drenthe-pagina is. Bv. description-opening: "Vloerverwarming in Drenthe, Groningen en Friesland — het hele traject van ondervloer tot oplevering, vanuit Zuidlaren."
- Controleer/optimaliseer title + description van `vloerverwarming-zuidlaren.html` op kliklust (concrete belofte: richtbedrag, eigen ploeg, reactie binnen één werkdag) zonder keyword-stuffing.
- Houd titles ≤ ~60 tekens en descriptions ≤ ~155 tekens.
**Succescriterium:** Geen lege/dubbele meta-tags; "vloerverwarming drenthe" en de zuidlaren-termen tonen na 2–4 weken eerste organische clicks (CTR > 0).

### Taak 5: Homepage beter laten converteren — prijsindicatie-CTA boven de vouw `[GOEDGEKEURD]`
**Bron:** Analytics Agent (aanbevelingen 3 + 4) — CTA/conversie
**Prioriteit:** Hoog
**Actie:**
- Zorg dat op `index.html` een duidelijke, primaire CTA naar `prijsindicatie.html` (kosten-intentie) én naar de offerte-deeplink (`contact.html?modus=offerte#aanvraag`) boven de vouw zichtbaar is — prijsindicatie converteert ~44% vs home ~23%, dus stuur twijfelaars daar gericht heen.
- Houd het sober en in stijl met de bestaande hero; voeg géén pop-ups of agressieve elementen toe. Doel: home-bounce (67%) verlagen door bezoekers een directe volgende stap te geven.
- Werkt op desktop én mobiel (mobile = 40% van het verkeer); test dat de knop niet onder de fold valt op mobiel.
**Succescriterium:** Primaire CTA naar prijsindicatie zichtbaar zonder scrollen op desktop + mobiel; geen layout-breuk; over 4 weken lagere home-bounce en meer prijsindicatie-instroom.

---

## Uitgestelde voorstellen `[WACHT]`

- **Dedicated `vloerverwarming-drenthe.html` aanmaken** (Marketing Research Taak 5, Analytics aanbeveling 1). Dit is de grootste latente kans ("vloerverwarming drenthe": 82 impr @ pos 66, versnipperd over 4 pagina's), maar het is >1 sprintdag inclusief content en interne-link-architectuur. Verdient een eigen, gefocuste sprint zodat het kwalitatief goed gebeurt (model van bestaande stadspagina's, `Service` + `areaServed` = Drenthe, canonical, wederzijdse interne links naar alle stadspagina's, en de home-Drenthe-hub omzetten naar een teaser om nieuwe cannibalisatie te voorkomen). **Taak 4 (Drenthe in home-title/description) houdt de term ondertussen warm.** → Plannen voor cyclus 18.
- **www vs non-www canonical/redirect controleren** (Analytics Agent). GSC toont `vlwarmte.nl/` (pos 5,6) en `www.vlwarmte.nl/` (pos 52,8) als losse rijen — mogelijk verdunnen de signalen. Vergt eerst diagnose (canonical-tags + redirect-gedrag GitHub Pages/DNS) voordat we ingrijpen. → Onderzoek in cyclus 18.

---

## Afgewezen voorstellen `[AFGEWEZEN]`

- Geen voorstellen afgewezen deze cyclus. De Friesland-zwakte ("vloerverwarming friesland" 87,7) is reëel maar telt mee in de bredere Drenthe/regio-aanpak en de Leeuwarden-pagina; aparte actie nu niet rendabel genoeg t.o.v. de bijna-pagina-1-kansen.

---

## Escalaties (handmatig — geblokkeerd in autonome modus)

Deze acties kan de autonome cyclus **niet** zelf uitvoeren (live-account-mutaties, OAuth, SMTP, of Python-versie). Voor de eigenaar / een interactieve sessie:

1. **GA4-fetch repareren (hoogste prioriteit volgende cyclus).** `scripts/ga4_fetch.py` gebruikt 3.10+-syntax (`Path | None`) maar de toegestane interpreter is systeem-Python 3.9. Oplossing: óf het script 3.9-compatibel maken (`Optional[Path]`), óf de venv-runner (`python3.12` / `.venv/bin/python`) toestaan in de cyclus-permissies. Zonder fix blijft de data elke week verouderen.
2. **Google Ads geo aanscherpen (budgetlek).** Live campagne "VLW-API-Leads NL auto" (id 23834672782, €2/dag) draait NL-breed; GA4 toont ~44 sessies (28%) buiten het kerngebied (North Holland 25, South Holland 11, Brabant 8). Geo-defaults zijn al Drenthe/Groningen/Friesland. Eigenaar kan handmatig draaien:
   ```
   python scripts/google_ads_update_campaign_geo.py --campaign-id 23834672782 --dry-run
   python scripts/google_ads_update_campaign_geo.py --campaign-id 23834672782 --apply
   ```
3. **Ads-status/budget van eind mei controleren** — verkeer daalde >90% sinds piek 27 apr (172 → ~15/week). Plausibel: lager Ads-budget en/of zomerseizoen. Verifiëren of dit bewust is.
4. **Release-mail** (`scripts/send_pm_release_notes_email.py`) — SMTP is geblokkeerd in autonome modus; mail handmatig versturen indien gewenst.

---

## Social Media
**Status:** Weekplanning staat in `docs/website-manager/social/weekly_calendar.md` (cyclus 17).
**Actie vereist:** Handmatige publicatie door VLWarmte-team. 3 Facebook-posts (di 16/6, do 18/6, za 20/6), rode draad "zomer = hét moment, klaar vóór het stookseizoen".
**Let op:** beeldmateriaal raakt op — sinds mei geen nieuwe foto's. Voor cyclus 18 graag aanleveren: afgewerkte vloer/interieur, échte teamfoto, Hoogeveen/Friesland-project, detailfoto verdeler.

---

## Context voor volgende sprint
- **Meten:** posities in GSC voor zuidlaren-/hoogeveen-/installatiebedrijf-termen + eerste organische clicks; home-bounce en prijsindicatie-instroom in GA4.
- **Volgende grote stap:** dedicated `vloerverwarming-drenthe.html` (nu [WACHT]) — de structurele fix voor de grootste regioterm.
- **Randvoorwaarde:** GA4-fetch werkend krijgen, anders blijft de cyclus op verouderde data sturen.
- **Ads:** controleren of geo-fix is doorgevoerd en of de verkeersdaling verklaard is.

---

## Developer Rapport — 15 juni 2026 (cyclus 17)

Alle 5 goedgekeurde taken geïmplementeerd. Taken met `[WACHT]`/escalatie zijn niet aangeraakt. Geen commit/push gedaan — dat doet de PM.

### Taak 1: Zuidlaren-cannibalisatie — **GEDAAN**
- `index.html`: hero-lead-link omgezet van ankertekst "Zuidlaren" naar "vloerverwarming Zuidlaren".
- `diensten.html`: bestaande regel-link naar zuidlaren-pagina kreeg exacte ankertekst "vloerverwarming Zuidlaren" (was "vloerverwarming in Zuidlaren en omgeving").
- `prijsindicatie.html`: één nieuwe regel toegevoegd onderaan de sectie "Regio Drenthe, Groningen en Friesland" met link + ankertekst "vloerverwarming Zuidlaren".
- `vloerverwarming-zuidlaren.html`: eerste alinea (hero-lead) bevat nu de exacte combinatie "vloerverwarming in Zuidlaren".

### Taak 2: Contentblok "Installatiebedrijf in Zuidlaren" — **GEDAAN**
- `index.html`: nieuwe `section section-muted` met H2 "Installatiebedrijf in Zuidlaren" + 1 alinea, vóór de FAQ-sectie. Tekst conform sprint. Geen twee `section-muted` direct naast elkaar (Drenthe-hub ervoor is plain `section`).
- LocalBusiness-schema gecontroleerd: `name` VLWarmte, address Verlengde Stationsweg 58 / 9471 PM Zuidlaren, `addressRegion` Drenthe — klopt, **niet gewijzigd**.

### Taak 3: Hoogeveen over pagina-1-grens — **GEDAAN**
- Interne link 1: `index.html` Drenthe-hub-lijst kreeg exacte ankertekst "vloerverwarming Hoogeveen" (was "Vloerverwarming Hoogeveen e.o.").
- Interne link 2: `vloerverwarming-zuidlaren.html` sectie "Ook actief in" — Hoogeveen-link kreeg ankertekst "vloerverwarming Hoogeveen".
- FAQ toegevoegd op `vloerverwarming-hoogeveen.html` (3 vragen: Hollandscheveld/Fluitenberg, kosten, infrezen) met bestaande `faq-item`/`faq-question`/`faq-answer`-markup, plus geldig `FAQPage` JSON-LD in de `<head>` (single-line stijl, consistent met homepage). Zichtbare tekst en JSON-LD-tekst komen overeen.

### Taak 4: Title/meta-CTR + Drenthe warm houden — **GEDAAN**
- `index.html` title: "Vloerverwarming Drenthe, Groningen & Friesland | VLWarmte" (~57 tekens). Description bevat expliciet "Drenthe" en opent zoals voorgesteld (~152 tekens).
- `vloerverwarming-zuidlaren.html` title: "Vloerverwarming Zuidlaren — eigen ploeg | VLWarmte" (~50 tekens, dubbele "VLWarmte" verwijderd). Description ~152 tekens met concrete belofte (eigen ploeg, reactie binnen één werkdag, richtbedrag), geen keyword-stuffing. OG/Twitter-titles op zuidlaren meegetrokken voor consistentie.

### Taak 5: Prijsindicatie-CTA boven de vouw — **GEDAAN**
- `index.html` hero-CTA-rij: primaire knop blijft "Vrijblijvende prijsindicatie" → `prijsindicatie.html`; tweede knop omgezet van `werkwijze.html` naar de offerte-deeplink `contact.html?modus=offerte#aanvraag` ("Offerte of info aanvragen"). Beide staan in de hero, boven de fold op desktop én mobiel. Bestaande `btn`/`hero-cta-row`-stijl hergebruikt, geen pop-ups, geen layout-wijziging. Mobiele sticky-CTA wees al naar de offerte-deeplink.

### Overgeslagen
- `[WACHT]`-items (dedicated Drenthe-pagina, www/non-www canonical) en alle escalaties (GA4-fetch, Ads-geo/budget, release-mail) — niet aangeraakt, conform opdracht.

### Risico's / te verifiëren door PM
- **Verificatie buiten autonome modus:** Bash/scripts geblokkeerd, dus geen smoke test of JSON-validator gedraaid. PM graag draaien: HTML/linkcheck + JSON-LD-validatie (Rich Results Test) op `vloerverwarming-hoogeveen.html` (nieuw FAQPage) en homepage.
- **Meta-lengtes** handmatig geteld (alle binnen ~60/~155); PM kan in de SERP-preview dubbelchecken.
- Taak 5 verlegt de tweede hero-knop weg van "Bekijk onze werkwijze"; werkwijze blijft bereikbaar via nav, FAQ-link en de kaart "Werkwijze" lager op de pagina — geen verweesde pagina.

### Gewijzigde bestanden (voor `git add`)
- `index.html`
- `diensten.html`
- `prijsindicatie.html`
- `vloerverwarming-zuidlaren.html`
- `vloerverwarming-hoogeveen.html`
- `docs/website-manager/sprint.md` (dit rapport)

**Deployment:** Nog niet live — PM voert commit + `git push origin main` uit.
