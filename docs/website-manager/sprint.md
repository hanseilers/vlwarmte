# Sprint — week van 29 juni 2026 (cyclus 19)

**PM beslissing genomen op:** 29 juni 2026, 06:15
**Doel deze sprint:** De twee dingen aanpakken die los van het verkeersvolume winst opleveren — de prijsindicatie-wizard écht laten converteren, en het organische fundament (8 stadspagina's + homepage-titel) zo afmaken dat het gaat ranken.
**Meetdoel (over ~4 weken in GA4/GSC):** eerste conversie(s) uit `prijsindicatie.html` (nu 0 over 90d / 68 sessies); GA4 toont nog maar één `<title>` voor pad `/` (nu 6 varianten); bij verse GSC: de 8 stadspagina's geïndexeerd met ≥2 interne inkomende links, en de top-3-termen (installateur/elektricien zuidlaren) van 0 naar >0 clicks.

---

## Belangrijkste databevinding deze cyclus (verse GA4, per 29 jun)

De fetch werkt; er is verse data. Het beeld is consistent met cyclus 18, maar scherper:

1. **Het probleem is instroom, niet conversiekwaliteit.** 30d: ~42 sessies / 40 gebruikers. Weektrend stortte in: 75/week (begin mei) → 1 (15–21 jun) → **5 (22–28 jun)**. De lichte opleving valt samen met terugkerend betaald verkeer.
2. **100% van de conversies komt uit `google/cpc`** (22 sessies / 2 conv). Direct (12) en organic (6) leveren samen **nul**. De betaalde campagne (id 23834672782, ~€2/dag) draait weer beperkt — gezonde ~9% conversieratio, maar veel te weinig volume.
3. **`prijsindicatie.html` is veruit de sterkste pagina** (307 s sessieduur, 25% bounce) maar levert **0 conversies** — ook 0 over 90d/68 sessies. Het lead-formulier ná het richtbedrag bestáát al (Formspree `xzdojzdk`); het lek zit dus in prominentie/frictie of in afhaken vóór het resultaat, niet in een ontbrekende CTA.
4. **Homepage-titelversnippering:** GA4 toont **6 verschillende `<title>`'s voor pad `/`** in 30d, waaronder één variant ("…richtbedrag in 2 min") met 5 sessies / 7,4 s / **100% bounce**. Verdund rankingsignaal + CTR-ruis.
5. **De 8 stadspagina's bestaan** (drenthe, assen, drachten, emmen, groningen, hoogeveen, leeuwarden, zuidlaren — cyclus 17–18) maar krijgen elk 0–2 sessies. Prioriteit verschuift van *bouwen* naar *laten ranken* via interne links.

Conclusie: deze sprint vol op (a) de wizard echt laten converteren en (b) het organische fundament afmaken — beide leveren winst op **onafhankelijk van het verkeersvolume**, dat we autonoom niet kunnen herstellen (Ads-budget ligt bij de eigenaar — zie escalatie onderaan).

---

## Goedgekeurde taken voor Developer Agent

### Taak 1: Prijsindicatie-wizard — conversiestap ná het richtbedrag versterken `[GOEDGEKEURD]`
**Bron:** Analytics Agent (voorstel 1) + Marketing Research Agent (grootste hefboom)
**Prioriteit:** Hoog (conversie)
**Context — niet dupliceren:** `prijsindicatie.html` heeft ná het resultaat (`#result` → `.lead-after`) al een volledig lead-formulier (`#calc-form`, Formspree `xzdojzdk`, knop "Offerte aanvragen"). Het probleem is dus **prominentie/frictie**, niet een ontbrekende CTA. Voeg geen tweede formulier toe.
**Actie:**
1. Maak het `.lead-after`-blok direct ónder de prijskaart visueel onmiskenbaar — duidelijke visuele scheiding/accent zodat wie het richtbedrag ziet meteen de vervolgstap ziet (geen pop-up, geen sticky-overlay; semantische HTML, styling via bestaande `styles.css`-klassen of een nieuwe klasse, geen inline styles).
2. Voeg náást "Offerte aanvragen" een **laagdrempelig alternatief** toe voor wie geen formulier wil invullen: een tweede, secundaire knop/link "Liever even bellen?" naar het telefoonnummer (`tel:`) en/of `contact.html?modus=bel#aanvraag`. Houd "Offerte aanvragen" de primaire actie.
3. Korte, geruststellende microcopy boven de knoppen ("Je krijgt binnen één werkdag antwoord — vrijblijvend"), in de tone of voice.
**Succescriterium:** lead-stap staat prominent en pal onder de prijskaart; er is een primaire (offerte) én secundaire (bellen) actie; pagina werkt zonder JavaScript; GA4 laat over ~4 weken eerste `wizard_lead_submit`- of `contact_submit`-conversie vanaf deze pagina zien (nu 0).

### Taak 2: Homepage `<title>` + meta description consolideren tot één definitieve, CTR-gerichte variant `[GOEDGEKEURD]`
**Bron:** Marketing Research Agent (taak 1) + Analytics Agent (voorstel 4)
**Prioriteit:** Hoog (SEO, traffic-onafhankelijk)
**Actie:** Stel op `index.html` één definitieve `<title>` en `<meta name="description">` vast (synchroon met de `og:`/`twitter:`-varianten) en houd die vast. Basis: de variant met de beste engagement (lage bounce / hogere sessieduur) — niet de "richtbedrag in 2 min"-variant die 100% bounct. Schrijf de snippet uitnodigend: USP + plaats (Zuidlaren / Drenthe-Groningen-Friesland) + concrete reden tot klikken, naar het patroon van de wél-klikkende snippets. Geen keyword-stuffing.
**Succescriterium:** GA4 toont over de komende periode nog maar één paginatitel voor pad `/`; bij verse GSC stijgt de home-CTR. Eén `<title>`/`<meta>` live, consistent met OG/Twitter-tags.

### Taak 3: Interne ankerlinks naar de 8 stadspagina's — Drenthe als hub `[GOEDGEKEURD]`
**Bron:** Marketing Research Agent (taak 2) + Analytics Agent
**Prioriteit:** Hoog (SEO)
**Actie:** Leg interne links met **exacte-zoekterm-ankertekst** (`vloerverwarming Drenthe`, `vloerverwarming Assen`, `vloerverwarming Emmen`, `vloerverwarming Groningen`, `vloerverwarming Hoogeveen`, `vloerverwarming Leeuwarden`, `vloerverwarming Drachten`, `vloerverwarming Zuidlaren`) vanuit `index.html` en `diensten.html` naar de juiste stadspagina. Maak `vloerverwarming-drenthe.html` de **hub**: die linkt naar alle stadspagina's en elke stadspagina linkt terug naar de Drenthe-hub. Doel: elke stadspagina ≥2 interne inkomende links met exacte ankertekst. Controleer dat elke stadspagina een correcte `canonical` heeft.
**Succescriterium:** elke stadspagina heeft ≥2 interne inkomende links met exacte ankertekst; bij verse GSC indexatie + positiewinst zichtbaar.

### Taak 4: CTR-/snippet-fix Zuidlaren + Friesland/Emmen-subdorpen intern aanhaken `[GOEDGEKEURD]`
**Bron:** Marketing Research Agent (taken 3 + 5)
**Prioriteit:** Midden (SEO)
**Actie:**
1. Herschrijf `<title>` + `<meta name="description">` van `vloerverwarming-zuidlaren.html` voor CTR (USP + plaats + concrete reden tot klikken), zodat de top-3-termen (installateur/elektricien/laren zuidlaren — nu top-3 met 0 clicks) clicks gaan trekken.
2. Haak met exacte-ankertekstlinks de zwakke Friese/Zuidoost-Drentse termen aan de juiste pagina: `vloerverwarming Heerenveen` / `vloerverwarming Friesland` → `vloerverwarming-leeuwarden.html` (of drachten-pagina waar passend); `vloerverwarming Schoonebeek` → `vloerverwarming-emmen.html`. Vanuit zuster-/hubpagina's.
**Succescriterium:** Zuidlaren-snippet herschreven; Leeuwarden- en Emmen-pagina hebben elk een extra interne link met exacte ankertekst; bij verse GSC schuiven die termen omhoog / krijgen clicks.

### Taak 5: Home boven de vouw — prijsindicatie-CTA prominent en kloppend met de titel-belofte `[GOEDGEKEURD]`
**Bron:** Analytics Agent (voorstel 4) + Marketing Research Agent (taak 4)
**Prioriteit:** Midden (CTA/conversie)
**Context — niet dupliceren:** eerdere cycli (17/18) plaatsten al een prijsindicatie-CTA op de home. Deze taak is **verifiëren en zo nodig versterken**, geen tweede CTA toevoegen.
**Actie:** Controleer of `index.html` boven de vouw een prominente, duidelijk zichtbare CTA naar `prijsindicatie.html` heeft die de belofte uit de (geconsolideerde) titel direct inlost — "Richtbedrag in 2 minuten" o.i.d. Staat die er al maar te onopvallend / te ver naar beneden: maak hem prominenter en hoger op de pagina. Staat hij goed: laat ongemoeid en noteer dat in het rapport. Conservatieve variant bij twijfel.
**Succescriterium:** home toont boven de vouw één heldere CTA naar de wizard; over ~4 weken meer doorklik-/entry-sessies op `prijsindicatie.html` + meer `wizard_start`-events; lagere bounce op de voormalige 100%-bounce home-variant.

---

## Uitgestelde voorstellen `[WACHT]`
- **Funnel-drop-off per wizard-stap uitlezen** (Analytics voorstel 3): vereist GA4-event-funnel-query (`wizard_start` → `calculator_result` → `wizard_lead_submit`). Kan niet in deze autonome modus (geen ad-hoc GA4-query-tooling); inplannen in een sessie mét data-toegang vóór een volgende, gerichtere wizard-ingreep. Taak 1 dicht nu het meest waarschijnlijke lek (prominentie/frictie) zonder die meting af te wachten.
- **`diensten.html` / `systemen-producten.html` overtuigender maken** (Analytics voorstel 6): 67% bounce maar slechts 3 sessies — te weinig data, te veel andere prioriteiten deze sprint. Volgende cyclus.
- **www-/non-www ranking-splitsing verifiëren** (Research taak 6): vereist verse GSC om te bevestigen; meenemen zodra GSC ontblokt is.

## Afgewezen voorstellen `[AFGEWEZEN]`
- **Nieuwe doelgroep-/dienst-splitsingspagina's** ("alleen schuimbeton", "aannemers"): nul vraagsignaal in de data; niet bouwen zonder bewijs van zoekvolume (max 1 nieuwe pagina-regel + kwaliteit boven kwantiteit).
- **`projecten.html` opwaarderen**: geblokkeerd op beeldmateriaal — geen nieuwe bouwfoto's aangeleverd. Geen dev-werk tot foto's er zijn.

---

## Social Media
**Status:** Weekplanning staat in `docs/website-manager/social/weekly_calendar.md` (7 posts: 3 LinkedIn, 4 Instagram + Facebook-varianten, week van 29 jun).
**Actie vereist:** Handmatige publicatie door VLWarmte-team. Elke post heeft één CTA met diepe link naar prijsindicatie of contact (`?modus=…#aanvraag`) — sluit aan op de sprint-prioriteit "meer instroom naar de wizard".
**Aandachtspunt:** beeldmateriaal is twee cycli op rij de bottleneck (zelfde 2 werkfoto's). Eigenaar: lever nieuwe foto's in `docs/website-manager/social/input/` (eindresultaat-vloer, verdeler-detail, teamfoto, Hoogeveen/Friesland-project).

---

## ESCALATIE — vereist eigenaar of sessie met permissies (NIET autonoom uit te voeren)

Deze acties kon de cyclus niet zelf draaien (Ads-scripts, GSC-OAuth en outbound mail zijn geblokkeerd in de autonome modus). Ze staan klaar met exacte commando's:

1. **Google Ads — volume + status (urgentst).** cpc is 100% van de conversies maar draait op ~€2/dag. Bevestig dat campagne `23834672782` ENABLED is en beoordeel budgetverhoging (gezonde ~9% conversieratio → lineair meer leads). Read-only check: `python scripts/google_ads_list_campaigns.py`. **Budget verhogen / `--go-live` alleen na expliciete spend-goedkeuring.**
2. **Google Ads — geo-lek dichten.** GA4-geo toont verkeer buiten kerngebied (Noord-/Zuid-Holland, Duitsland, zelfs Bangladesh/Canada) terwijl de defaults Drenthe/Groningen/Friesland zijn → live campagne staat vermoedelijk NL-breed. `python scripts/google_ads_update_campaign_geo.py --campaign-id 23834672782 --dry-run` dan `--apply`.
3. **GSC-fetch deblokkeren.** `gsc_report.json` is 5 weken oud (23 mei) → de cyclus-17/18-SEO (Drenthe-pagina, CTR-fix, internelinks) is **niet meetbaar**. Eigenaar: OAuth-refresh-token aanleveren (zie `secrets/gsc.env.example`) zodat `scripts/gsc_fetch.py` in de cyclus draait.
4. **Interne release-mail** (stap 8b) draait niet autonoom (outbound SMTP geblokkeerd): `python3 scripts/send_pm_release_notes_email.py` lokaal met `secrets/hostnet-mail.env`.

---

## Context voor volgende sprint
- **Eerst meten zodra mogelijk:** GSC ontblokken → toets de organische ingrepen van cyclus 17–19 (stadspagina-indexatie, CTR-fix, internelinks, home-titel). Tot die tijd sturen we blind op organisch.
- **Conversie-hefboom blijft `prijsindicatie.html`:** als taak 1 + 5 over 4 weken nog 0 conversies tonen ondanks instroom, dán de wizard-stap-events uitlezen (uitgesteld voorstel) om het exacte lek te vinden.
- **Betaald kanaal blijft levensader:** 100% van de conversies. Het volume-/budget- en geo-besluit ligt bij de eigenaar (escalatie 1–2).
- **Let op klein-volume-ruis:** bij 42 sessies/30d zijn enkelvoudige cijfers (100%-bounce-titel, 1 AI-sessie) signalen, geen harde trends.

---

## Developer Rapport — 29 juni 2026

### Geïmplementeerde taken

**Taak 1 — Prijsindicatie-wizard, conversiestap versterken** (`prijsindicatie.html`)
- Bestaand `.lead-after`-blok (Formspree `xzdojzdk`) prominenter gemaakt: accentrand boven (3px brand), volledige accentrand rondom, schaduw en een eyebrow-label "Volgende stap". Koptekst iets groter. Geen tweede formulier — het bestaande blok is hergebruikt.
- Geruststellende microcopy toegevoegd boven de knoppen: "Je krijgt binnen één werkdag antwoord — vrijblijvend, geen verkoper aan de deur."
- Secundair, laagdrempelig alternatief toegevoegd náást de primaire knop "Offerte aanvragen": "Liever even bellen?" met `tel:+31618817459` én `contact.html?modus=bel#aanvraag`. "Offerte aanvragen" blijft de primaire actie.
- Styling via nieuwe klassen in de bestaande inline `<style>` van de pagina; geen inline styles op elementen. Werkt zonder JavaScript (statische HTML-form en plain links).

**Taak 2 — Homepage `<title>` + meta consolideren** (`index.html`)
- Eén definitieve `<title>` vastgesteld: "Vloerverwarming in Drenthe, Groningen en Friesland — VLWarmte". De 100%-bounce-variant "richtbedrag in 2 min" is verwijderd uit de home-title.
- `<meta name="description">` herschreven met USP + plaats + concrete redenen (eigen ploeg, 10 jaar garantie buis, reactie binnen één werkdag).
- `og:title` / `og:description` / `twitter:title` / `twitter:description` synchroon gemaakt met de nieuwe titel/description.

**Taak 3 — Interne ankerlinks naar stadspagina's, Drenthe als hub** (`index.html`, `diensten.html`, `vloerverwarming-drenthe.html`)
- `index.html`: in de `#drenthe-hub`-sectie een `<ul>` met exacte-zoekterm-ankers toegevoegd naar alle 8 pagina's (Drenthe, Assen, Emmen, Hoogeveen, Zuidlaren, Groningen, Leeuwarden, Drachten).
- `diensten.html`: regio-cross-linkblok toegevoegd (`<ul>` met exacte ankers naar Drenthe-hub + 7 stadspagina's). Diensten had eerder alleen Zuidlaren + Drachten in de body.
- `vloerverwarming-drenthe.html`: hub-lijst "Per stad en streek" uitgebreid van 4 naar 7 stadspagina's met exacte ankertekst (Groningen, Leeuwarden, Drachten toegevoegd). Elke stadspagina linkt al terug naar de hub ("vloerverwarming in heel Drenthe").
- Resultaat: elke stadspagina heeft nu ruim ≥2 interne inkomende links met exacte ankertekst (home + diensten + hub + zusterpagina's). Canonicals gecontroleerd: alle stadspagina's hebben een correcte self-canonical.

**Taak 4 — CTR-fix Zuidlaren + Friese/Emmen-subdorpen aanhaken** (`vloerverwarming-zuidlaren.html`)
- `<title>` + meta herschreven richting de top-3-term "installateur": "Vloerverwarming Zuidlaren — installateur uit het dorp | VLWarmte"; description leidt met "Installateur voor vloerverwarming in Zuidlaren" + concrete reden (Verlengde Stationsweg, eigen ploeg, reactie binnen één werkdag). OG/Twitter synchroon.
- Exacte-ankertekstlinks toegevoegd vanaf de Zuidlaren-zusterpagina: `vloerverwarming Schoonebeek` → `vloerverwarming-emmen.html`, `vloerverwarming Friesland` → `vloerverwarming-leeuwarden.html`, `vloerverwarming Heerenveen` → `vloerverwarming-drachten.html`. Leeuwarden en Emmen krijgen hiermee elk een extra interne link met exacte ankertekst (de Drenthe-hub had deze ankers al).

**Taak 5 — Home boven de vouw: prijsindicatie-CTA** (`index.html`)
- **Stond al grotendeels goed:** de hero had al een primaire CTA naar `prijsindicatie.html` als eerste knop boven de vouw. **Wel versterkt:** de knoptekst was generiek ("Vrijblijvende prijsindicatie") en loste de titel-belofte niet in. Aangepast naar "Richtbedrag in 2 minuten →" zodat hij aansluit op de promise en consistent is met de stadspagina's. Geen tweede CTA toegevoegd.
- **Daarnaast een mismatch gecorrigeerd:** de sticky mobiele CTA was gelabeld "Vrijblijvende prijsindicatie / ~30 sec" maar linkte naar `contact.html?modus=offerte#aanvraag` in plaats van de wizard. Nu wijst hij naar `prijsindicatie.html` met label "Richtbedrag in 2 minuten / ~2 min" — label en bestemming kloppen nu en sturen mobiel verkeer naar de wizard.

### Overige
- `sitemap.xml`: `lastmod` bijgewerkt naar 2026-06-29 voor de gewijzigde pagina's (home, diensten, prijsindicatie, drenthe-hub, zuidlaren).
- Alle wijzigingen: semantische HTML, geen inline styles op elementen, leesbaar zonder JavaScript.

### Overgeslagen taken
- `[WACHT]`: funnel-drop-off uitlezen, diensten/systemen overtuigender, www-/non-www-splitsing — vereisen data-/GSC-toegang die in deze modus geblokkeerd is.
- `[AFGEWEZEN]`: nieuwe doelgroep-/dienstpagina's, projecten opwaarderen (geen beeldmateriaal).
- `[ESCALATIE]`: Google Ads volume/geo, GSC-fetch, release-mail — liggen bij de eigenaar.

### Deployment
- **Nog niet live** — PM voert commit + `git push origin main` uit; daarna: [PM vult run-id / succes in].
- Live URL: https://www.vlwarmte.nl

### Aandachtspunten voor volgende sprint
- De wizard-conversiemeting (taak 1) en home-CTA (taak 5) zijn pas over ~4 weken in GA4 te beoordelen; bij nog 0 conversies dan de wizard-stap-events uitlezen (uitgesteld voorstel).
- De interne-link- en titel-ingrepen (taak 2/3/4) zijn pas meetbaar zodra GSC ontblokt is.
- `diensten.html` heeft nu een regio-linklijst in de body; let bij toekomstige herschrijvingen op dat die niet sneuvelt.
