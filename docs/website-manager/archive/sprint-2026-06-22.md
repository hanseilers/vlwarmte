# Sprint — week van 22 juni 2026 (cyclus 18)

**PM beslissing genomen op:** 22 juni 2026, 08:15
**Doel deze sprint:** Organisch fundament verstevigen zodat leads niet langer volledig van betaald verkeer afhangen — want de Ads-leadmotor is feitelijk stilgevallen.
**Meetdoel (over ~4 weken in GA4/GSC):** "vloerverwarming drenthe" van pos ~66 richting pagina 2–3; eerste organische clicks op de zuidlaren-/installateur-termen (nu top-3 met 0 clicks); meer entry-sessies op `prijsindicatie.html` (nu 5–9, de 22%-bounce/362-sec-pagina).

---

## Belangrijkste databevinding deze cyclus (verse GA4, per 22 jun)

De fetch-blokkade van de afgelopen twee cycli is opgelost — er is **verse data**. Die laat een scherper en zorgwekkender beeld zien dan de bevroren 8-juni-cijfers:

1. **Verkeer is bijna volledig ingestort.** Weektrend: 27 apr 172 → … → 8 jun 15 → **15 jun = 1 sessie**. De laatste week is praktisch dood.
2. **Conversies 30d: 35 → 9** (google/cpc 6, direct 3, organic 0). De betaalde leadmotor levert nog maar een fractie.
3. **Conclusie:** de Google Ads-campagne (id 23834672782, "VLW-API-Leads NL auto", €2/dag) lijkt **gepauzeerd of zonder budget**. Dit is een live-account-kwestie die de PM-cyclus niet autonoom kan oplossen (Ads-scripts geblokkeerd + spend-besluit). **Zie escalatie onderaan — dit is de urgentste actie van de week en ligt bij de eigenaar.**

Omdat de leadstroom nu volledig afhankelijk blijkt van een kanaal dat stilstaat, zet deze sprint vol in op **organisch** (de enige kanaalbron die niet van dagbudget afhangt) plus conversie van het schaarse verkeer dat wél binnenkomt.

---

## Goedgekeurde taken voor Developer Agent

### Taak 1: Dedicated pagina `vloerverwarming-drenthe.html` `[GOEDGEKEURD]`
**Bron:** Analytics Agent (voorstel 2) + Marketing Research Agent (aanbeveling 2)
**Prioriteit:** Hoog
**Actie:** Maak één gefocuste provinciepagina naar exact model van de bestaande stadspagina's (bv. `vloerverwarming-assen.html`):
- `<title>`/meta gericht op "vloerverwarming Drenthe" + USP + plaats + CTA.
- Schema: `Service` met `areaServed = "Drenthe"`, plus `canonical` naar `https://www.vlwarmte.nl/vloerverwarming-drenthe.html`.
- Inhoud: kort, nuchter, concreet — wat VLWarmte doet in heel Drenthe, link naar prijsindicatie-wizard en offerte.
- **Interne links (cruciaal tegen cannibalisatie):** wederzijdse links van/naar alle Drentse stadspagina's (Assen, Hoogeveen, Emmen, Zuidlaren, Meppel indien aanwezig). Zet de bestaande Drenthe-vermeldingen op `index.html` om naar een korte teaser die naar deze nieuwe pagina linkt (niet de hele inhoud dupliceren).
**Succescriterium:** Pagina bestaat, valideert (schema, canonical), is opgenomen in interne navigatie/sitemap, en linkt wederzijds met de stadspagina's. Geen dubbele H1/title-conflicten met home.

### Taak 2: CTR-/snippet-fix top-3-termen (title + meta) `[GOEDGEKEURD]`
**Bron:** Marketing Research Agent (aanbeveling 3)
**Prioriteit:** Hoog
**Actie:** Herschrijf `<title>` + meta description van `index.html` (home) en `vloerverwarming-zuidlaren.html` zodat de SERP-snippet uitnodigt tot klikken. Data: "installateur zuidlaren" (pos 3,7), "elektricien zuidlaren" (2,2), "vloerverwarming laren" (3,0) staan top-3 maar leveren **0 clicks** — terwijl "warmtepomp zuidlaren" (pos 1,8) mét goede snippet 25% CTR haalt. De snippet is dus de bottleneck, niet de positie.
- Formule: USP + plaats + concrete reden om te klikken (bijv. "Vakman uit Zuidlaren · vrijblijvend richtbedrag in 2 min"). Onder 60 tekens title / 155 meta.
- Niet de Drenthe-/regiotermen kannibaliseren met taak 1 — home mag breder blijven, zuidlaren-pagina hyperlokaal.
**Succescriterium:** Beide pagina's hebben herschreven title+meta die natuurlijk de hoofdterm én een klik-trigger bevatten; lengtes binnen SERP-limieten.

### Taak 3: "Richtbedrag in 2 minuten"-CTA boven de vouw op stadspagina's `[GOEDGEKEURD]`
**Bron:** Analytics Agent (voorstel 5) + Marketing Research Agent (aanbeveling 5)
**Prioriteit:** Midden (conversie van bestaand verkeer)
**Actie:** `prijsindicatie.html` is veruit de sterkste pagina (verse data: 362 sec sessieduur, 22% bounce) maar krijgt te weinig instroom (5–9 entry-sessies). Home heeft sinds cyclus 17 al een boven-de-vouw-CTA hiernaartoe; trek dat door naar de stadspagina's. Voeg op de bestaande stadspagina's (Zuidlaren, Assen, Hoogeveen, Emmen, Groningen, Leeuwarden, Drachten) één prominente CTA-knop/link boven de vouw toe: **"Richtbedrag in 2 minuten →"** naar `prijsindicatie.html`. Hergebruik de bestaande knop-styling; geen pop-ups.
**Succescriterium:** Elke genoemde stadspagina heeft één duidelijke CTA boven de vouw die naar de prijsindicatie-wizard linkt, consistent vormgegeven.

### Taak 4: Interne links met exacte ankertekst — Zuidlaren afmaken + Friesland/Emmen aanhaken `[GOEDGEKEURD]`
**Bron:** Marketing Research Agent (aanbevelingen 1 + 6)
**Prioriteit:** Midden
**Actie:** Versterk de juiste pagina's met exacte-ankertekst interne links (geen nieuwe pagina's):
- **Zuidlaren-cannibalisatie afmaken:** vanuit `index.html`, `diensten.html`, `prijsindicatie.html` exact anker "vloerverwarming Zuidlaren" → `vloerverwarming-zuidlaren.html` (signaal staat nu versnipperd op pos 6,6 / 16,6 / 19,4).
- **Friesland:** exact anker "vloerverwarming Friesland" / "vloerverwarming Heerenveen" → `vloerverwarming-leeuwarden.html` resp. `vloerverwarming-drachten.html` vanuit zuster-/hubpagina's.
- **Emmen-omgeving:** exact anker "vloerverwarming Schoonebeek" / "vloerverwarming Elim" → `vloerverwarming-emmen.html`.
**Succescriterium:** De genoemde ankerteksten linken naar de bedoelde kanonieke pagina; geen kapotte links; ankertekst is exact de zoekterm (niet "lees meer").

---

## Uitgestelde voorstellen `[WACHT]`

- **Projecten-pagina overtuigender maken** (Analytics voorstel 6): zwakke engagement (verse data: 14 sec, projecten.html). Randvoorwaarde = nieuw beeldmateriaal van het team; sinds mei geen nieuwe bouwfoto's. Pas oppakken zodra foto's zijn aangeleverd. **Actie eigenaar:** lever projectfoto's aan in `docs/website-manager/social/input/` (geldt ook voor social — zie hieronder).
- **Friesland-pagina (eigen `vloerverwarming-friesland.html`)** (Analytics voorstel 8): eerst de Drenthe-provinciepagina (taak 1) bewijzen; daarna zelfde aanpak voor Friesland. Niet twee provinciepagina's tegelijk.
- **Funnel-drop-off-rapport prijsindicatie-wizard** (Research §calculator): per-stap uitlezen van `wizard_start` → `calculator_result` → `wizard_lead_submit`. Waardevol, maar vergt eerst meer instroom (taak 3) om betekenisvolle aantallen te hebben.

## Afgewezen voorstellen `[AFGEWEZEN]`

- **www-/non-www "fix"** (Research aanbeveling 4): bij diagnose blijkt de 301 van `vlwarmte.nl` → `www.vlwarmte.nl` al correct te staan en de canonical wijst naar www. Geen werk nodig; de GSC-split is historische data die vanzelf consolideert.
- **Nieuwe prijscalculator bouwen:** de wizard bestaat al op `prijsindicatie.html` en is de best converterende pagina. Niet bouwen — instroom verhogen (taak 3) is de juiste hefboom.
- **Aparte doelgroep-/dienstpagina's** ("alleen schuimbeton", "aannemers"): geen zoekvraag in GSC-data; niet bouwen zonder bewijs.

---

## Escalatie naar eigenaar (URGENT — geen developer-taak)

**1. Google Ads-campagne lijkt stilgevallen — leadstroom feitelijk stil.** Verse GA4 toont de laatste week (15–21 jun) slechts **1 sessie** en 30d-conversies gedaald van 35 → 9. De betaalde leadmotor is het hoofdkanaal; staat die uit, dan stoppen de leads. Te checken in een sessie mét Ads-permissies (of door eigenaar in Ads UI):
```
python scripts/google_ads_list_campaigns.py            # status ENABLED? budget op? geo?
python scripts/google_ads_update_campaign_geo.py --campaign-id 23834672782 --dry-run   # geo aanscherpen, dan --apply
```
Controleer: is de campagne gepauzeerd, is het dagbudget (€2) op, of is er een billing-/policy-blokkade? **Budget niet verhogen of `--go-live` zonder expliciete spend-goedkeuring.**

**2. GA4-fetch is gerepareerd** (`from __future__ import annotations`) — vanaf nu draait `python3 scripts/ga4_fetch.py` ook op systeem-Python 3.9. Geen actie nodig; ter info.

**3. Beeldmateriaal raakt structureel op.** Lever aan in `docs/website-manager/social/input/`: eindresultaat-vloer, verdeler-detail, teamfoto, en een Hoogeveen/Friesland-project. Blokkeert nu zowel de projecten-pagina als 2 van de 7 social-posts.

---

## Social Media
**Status:** Weekplanning staat in `docs/website-manager/social/weekly_calendar.md`
**Actie vereist:** Handmatige publicatie door VLWarmte-team. 7 posts (3 LinkedIn, 4 Instagram/Facebook), rode draad "zomer = hét moment om vloerverwarming aan te leggen, klaar vóór het stookseizoen", plaatsnamen expliciet in copy. 2 posts staan op `[FOTO NODIG]` (verdeler-detail, eindresultaat-vloer) en kunnen pas live na aanlevering.

---

## Context voor volgende sprint
- **Eerst checken:** is de Ads-campagne weer aan? Zo niet, dan blijft elke andere meting vertekend door bijna-nul verkeer.
- **Meten zodra GSC ververst is** (`scripts/gsc_fetch.py` — vergt nog OAuth, geblokkeerd in autonome modus): posities van zuidlaren-/installateur-termen (CTR-fix taak 2), "vloerverwarming drenthe" (nieuwe pagina taak 1), en of de internelinks-ankers (taak 4) de cannibalisatie hebben opgelost.
- **Prijsindicatie-instroom** is de centrale conversie-KPI: stijgt het aantal entry-sessies door taak 3?
- GA4-fetch werkt nu autonoom — verse data is vanaf nu de norm; stuur niet meer op bevroren momentopnames.

---

## Developer Rapport — 22 juni 2026

### Geïmplementeerde taken (alle 4 [GOEDGEKEURD])

**Taak 1 — Provinciepagina `vloerverwarming-drenthe.html`**
- Nieuwe pagina aangemaakt naar exact model van de stadspagina's (`project-hero`-layout, secties, footer, GA-snippet, favicons).
- `Service`-schema met `areaServed` = `{ "@type": "AdministrativeArea", "name": "Drenthe" }` + `canonical` → `https://www.vlwarmte.nl/vloerverwarming-drenthe.html`.
- Title/meta gericht op "vloerverwarming Drenthe" + USP + plaats + CTA ("richtbedrag in 2 minuten").
- Wederzijdse interne links: de pagina linkt naar Assen, Hoogeveen, Emmen, Zuidlaren (+ Groningen/Drachten/Leeuwarden over de grens); alle 7 stadspagina's linken nu met exacte anker "vloerverwarming in heel Drenthe" terug naar deze pagina (voorheen naar `index.html#drenthe-hub`).
- Home `#drenthe-hub`-sectie omgezet naar korte teaser die naar de nieuwe pagina linkt (volledige stedenlijst niet langer gedupliceerd op home).
- Opgenomen in `sitemap.xml` (priority 0.85, lastmod 2026-06-22). Geen dubbele H1/title met home (home-H1 = "Slim gelegd. Gelijkmatig warm.").

**Taak 2 — CTR-/snippet-fix title + meta**
- `index.html`: title → `Vloerverwarming Drenthe & Noord-NL — richtbedrag in 2 min` (57 tekens); meta → eigen-ploeg-USP + "Bekijk vrijblijvend je richtbedrag in 2 minuten" (144 tekens). Home blijft breed (Drenthe/Groningen/Friesland).
- `vloerverwarming-zuidlaren.html`: title → `Vloerverwarming Zuidlaren — vakman, richtbedrag in 2 min` (56 tekens); meta → "vakman uit het dorp" + klik-trigger (143 tekens). Hyperlokaal gehouden. Og/twitter-title meegetrokken voor consistentie.
- Beide titles <60 / metas <155.

**Taak 3 — "Richtbedrag in 2 minuten →"-CTA boven de vouw**
- Op alle 7 stadspagina's (Zuidlaren, Assen, Hoogeveen, Emmen, Groningen, Leeuwarden, Drachten) één `btn btn-primary`-knop direct onder de hero-lead (boven de trust-strip → boven de vouw) → `prijsindicatie.html`. Bestaande knop-styling (`hero-cta-row` / `btn-primary`), geen pop-ups. Precies 1 CTA per pagina geverifieerd.

**Taak 4 — Interne links met exacte ankertekst**
- "vloerverwarming Zuidlaren" → `vloerverwarming-zuidlaren.html`: stond al exact op `index.html`, `diensten.html` én `prijsindicatie.html` (geverifieerd, geen wijziging nodig).
- "vloerverwarming Friesland" → `vloerverwarming-leeuwarden.html` en "vloerverwarming Heerenveen" → `vloerverwarming-drachten.html`: toegevoegd op de Drenthe-hubpagina én op `index.html` (home-services-alinea herschreven naar exacte ankers).
- "vloerverwarming Schoonebeek" → `vloerverwarming-emmen.html`: toegevoegd op de Drenthe-hubpagina. "vloerverwarming Elim" → `vloerverwarming-emmen.html`: toegevoegd op `vloerverwarming-hoogeveen.html` (Elim ligt in de Hoogeveen–Emmen-corridor).

### Gewijzigde / toegevoegde bestanden
- **Toegevoegd:** `vloerverwarming-drenthe.html`
- **Gewijzigd:** `index.html`, `sitemap.xml`, `vloerverwarming-assen.html`, `vloerverwarming-drachten.html`, `vloerverwarming-emmen.html`, `vloerverwarming-groningen.html`, `vloerverwarming-hoogeveen.html`, `vloerverwarming-leeuwarden.html`, `vloerverwarming-zuidlaren.html`

### Smoke-test-uitkomst
- **HTML-validiteit:** nieuwe pagina heeft gebalanceerde tags (8× `<section>`/`</section>`, één `</main>`/`</footer>`/`</header>`/`</body>`/`</html>`); referentie-afbeelding bestaat.
- **Canonical:** aanwezig op nieuwe pagina (1×) en behouden op gewijzigde pagina's.
- **GA4-snippet:** aanwezig op nieuwe pagina (`ga-deferred.js`).
- **Geen kapotte links:** alle `*.html`-hrefs op de nieuwe pagina verwijzen naar bestaande bestanden; geen resterende verwijzingen naar `index.html#drenthe-hub`.
- **Title/meta-lengtes:** home 57/144, zuidlaren 56/143 — binnen SERP-limieten.
- **CTA boven de vouw:** exact 1 "Richtbedrag in 2 minuten" per stadspagina (7/7).

### Overgeslagen taken
- Geen. Alle `[WACHT]`- en `[AFGEWEZEN]`-voorstellen conform sprint niet aangeraakt.

### Deployment
- **Live** ✅ — PM-commit `ef6de99` gepusht naar `main` op 22-06-2026 06:22.
- GitHub Pages-build (run 27929371901, `pages-build-deployment`): **completed / success**.
- Live geverifieerd: `vloerverwarming-drenthe.html` → HTTP 200, title + canonical correct; GA-tag `G-0BB9M7HYSF` aanwezig in `ga-deferred.js`. Non-www → www 301 + canonical-naar-www al correct (geen fix nodig).
- Release notes gepusht in commit `6604e00`.
- Live URL: https://www.vlwarmte.nl

### Aandachtspunten voor volgende sprint
- Nieuwe pagina staat klaar voor meting in GSC ("vloerverwarming drenthe", nu pos ~66) — ververst GSC-data afwachten.
- Drenthe-pagina-title is 61 tekens (consistent met bestaande stadspagina's zoals Assen/Drachten die ook ~61 zijn); evt. later inkorten als CTR tegenvalt.
- Google Ads-escalatie (campagne lijkt gepauzeerd) blijft een eigenaar-actie buiten dit dev-werk.
