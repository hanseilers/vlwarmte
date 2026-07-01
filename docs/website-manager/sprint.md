# Sprint — week van 1 juli 2026 (cyclus 20)

**PM beslissing genomen op:** 1 juli 2026, 21:45
**Doel deze sprint:** De Heerenveen-gap dichten (Ads + organisch), en twee zwakke landingspagina's (`diensten`, `systemen-producten`) wizard-first maken — zonder de cyclus-19-wizard opnieuw aan te raken (die moet eerst 4 weken rijpen).
**Meetdoel (over ~4 weken in GA4/GSC):** eerste sessies op `vloerverwarming-heerenveen.html`; meer `wizard_start` vanaf `diensten.html` en `systemen-producten.html`; bij verse GSC: Heerenveen-term geïndexeerd; wizard nog steeds meten — bij 0 `wizard_lead_submit` op week 27 jul funnel-events uitlezen.

---

## Belangrijkste databevinding deze cyclus (verse GA4, per 1 jul)

1. **Instroom blijft het knelpunt.** 38 sessies/30d (↓10% t.o.v. cyclus 19), 2 conversies — beide uit `google/cpc` (~10,5% ratio). Direct (12) + organisch (6) = 0 conv.
2. **Cyclus-19-ingrepen te vers om te beoordelen** (live 29 jun). Wizard-leadstap, home-titel, stadlinks — geen nieuwe wizard-ingreep deze cyclus.
3. **`prijsindicatie.html` blijft 0 conversies** over 90d/68 sessies — maar 307 s engagement. Afwachten tot week ~27 jul.
4. **Eerste stadspagina-signalen:** Drachten (2 sessies, 0% bounce) en Zuidlaren (2× landing, 0% bounce) — vroeg, n=2.
5. **Heerenveen-gap:** Ads-keyword `vloerverwarming heerenveen` actief, geen dedicated pagina; concurrenten wel.
6. **GSC nog steeds 5+ weken oud** (`invalid_grant` op refresh token) — SEO-effect cyclus 17–19 niet meetbaar.
7. **Ads geo al correct** (DR+GR+FR) — geo-lek in GA4 waarschijnlijk historisch/rest 30d-venster; geen geo-mutatie nodig.

Conclusie: deze sprint focust op **Heerenveen-pagina** (enige toegestane nieuwe pagina), **landing-fixes** op diensten + systemen, en **contact-routing** naar de wizard — alles traffic-onafhankelijke winst.

---

## Goedgekeurde taken voor Developer Agent

### Taak 1: `vloerverwarming-heerenveen.html` — nieuwe stadspagina + interne links `[GOEDGEKEURD]`
**Bron:** Marketing Research Agent (voorstel 4) + Analytics Agent (Ads-keyword-gap)
**Prioriteit:** Hoog (SEO + Ads-alignment)
**Actie:**
1. Nieuwe pagina op patroon `vloerverwarming-drachten.html` / `vloerverwarming-leeuwarden.html`: H1 met plaatsnaam, werkgebied Friesland/Heerenveen, compleet traject, wizard-CTA boven de vouw ("Richtbedrag in 2 minuten →"), contact-secundair, canonical `https://www.vlwarmte.nl/vloerverwarming-heerenveen.html`, OG/Twitter synchroon.
2. Voeg toe aan navigatie (footer-regio-links indien dat het patroon is op andere stadspagina's), `sitemap.xml`, en interne links met exacte ankertekst `vloerverwarming Heerenveen` vanaf `vloerverwarming-leeuwarden.html`, `vloerverwarming-drachten.html`, `vloerverwarming-drenthe.html` (hub-sectie) en `diensten.html` (regio-blok).
3. Tone of voice: Noord-Nederlands (`je`/`jij`), geen "gevestigd"/"werkzaam", reactie **één werkdag**, 10 jaar garantie buis (geen "fabrieksgarantie").
**Succescriterium:** pagina live met correcte meta/canonical; ≥2 interne inkomende links met exacte ankertekst; in sitemap en nav; Ads-keyword `vloerverwarming heerenveen` heeft een passende landings-URL.

### Taak 2: `diensten.html` — cta-band primair naar wizard `[GOEDGEKEURD]`
**Bron:** Analytics Agent (voorstel 6) + Marketing Research Agent (voorstel 5)
**Prioriteit:** Hoog (CTA/conversie)
**Context:** hero wijst al naar wizard; onderste `cta-band` heeft primair "Offerte aanvragen" naar `contact.html?modus=offerte` — inconsistent met wizard-first.
**Actie:** In de `cta-band` onderaan: primaire knop naar `prijsindicatie.html` met label "Richtbedrag in 2 minuten →"; secundaire knop/link naar `contact.html?modus=offerte#aanvraag` ("Liever direct offerte aanvragen" o.i.d.). Geen derde primaire CTA toevoegen.
**Succescriterium:** cta-band toont wizard als primaire actie, contact als secundair; hero ongewijzigd of alleen als inconsistentie zichtbaar is.

### Taak 3: `systemen-producten.html` — hero en trust aanscherpen voor landings `[GOEDGEKEURD]`
**Bron:** Analytics Agent (voorstel 5) + Marketing Research Agent (voorstel 6)
**Prioriteit:** Midden (CTA/landing)
**Onderbouwing:** 3 landings, 67% bounce, 18 s gem. duur — laagopbouw-keywords in Ads landen hier.
**Actie:**
1. Hero: concrete belofte + regio (Drenthe/Groningen/Friesland) + primaire CTA naar `prijsindicatie.html` ("Richtbedrag in 2 minuten →").
2. Korte trust-regel onder hero of in intro (10 jaar garantie buis, reactie binnen één werkdag).
3. Geen tweede formulier; bestaande `#laagopbouw`-sectie intact laten.
**Succescriterium:** hero overtuigt binnen één scherm met duidelijke wizard-CTA; lagere bounce meetbaar over 4 weken (nu 67%).

### Taak 4: `contact.html` — wizard-teaser boven het aanvraagblok `[GOEDGEKEURD]`
**Bron:** Analytics Agent (contact 141 s engagement, 0 conv.) + wizard-first strategie
**Prioriteit:** Midden (CTA/conversie)
**Actie:** Voeg boven `#aanvraag` / het lead-formulier een compact, niet-opdringerig blok toe: "Wil je eerst een richtbedrag zonder gegevens in te vullen?" met link/knop naar `prijsindicatie.html`. Zichtbaar in alle modi (informatie/offerte/bel) — niet verbergen per tab. Verticaal veldpatroon respecteren; geen side-by-side label+input chaos.
**Succescriterium:** bezoeker op contact ziet vóór het formulier een duidelijke uitweg naar de wizard; geen extra primair CTA die het formulier overschaduwt.

### Taak 5: `werkwijze.html` — contextueel wizard-blok halverwege `[GOEDGEKEURD]`
**Bron:** Analytics Agent (interne routing) + Marketing Research (wizard-first)
**Prioriteit:** Midden (CTA)
**Actie:** Halverwege de pagina (na het stappen-overzicht, vóór de slot-CTA): compact `cta-band`-achtig blok met "Benieuwd wat het ongeveer kost?" + primaire knop naar `prijsindicatie.html`. Eén blok, geen dubbele hero-CTA.
**Succescriterium:** mid-page wizard-CTA aanwezig; pagina blijft leesbaar zonder JavaScript.

---

## Uitgestelde voorstellen `[WACHT]`
- **Wizard-funnel opnieuw meten** (Analytics/Marketing voorstel 1/2): cyclus-19 live 29 jun — geen nieuwe wizard-ingreep tot week ~27 jul; dan `wizard_lead_submit` check + eventueel funnel-query.
- **Homepage-title monitoren** (Analytics voorstel 4): geen dev-werk; over 2–4 weken in GA4 controleren of oude title-varianten uit het venster verdwijnen.
- **Google Ads budget verhogen** (Marketing voorstel 1): campagne ENABLED @ €2/dag, gezonde ratio — alleen na expliciete spend-goedkeuring eigenaar.
- **GSC OAuth vernieuwen** (Marketing voorstel 3): `invalid_grant` — eigenaar moet `scripts/gsc_get_refresh_token.py` draaien.
- **Ads-landing homepage vs. wizard monitoren** (Marketing voorstel 8): geen site-wijziging; over 4 weken GA4 landing-conv vergelijken.
- **`projecten.html` opwaarderen**: geblokkeerd op beeldmateriaal.

## Afgewezen voorstellen `[AFGEWEZEN]`
- **Prijscalculator opnieuw bouwen**: `prijsindicatie.html` ís de calculator; 307 s engagement bewijst waarde — focus op instroom, niet herbouw.
- **Nieuwe dienst-splitsingspagina's** ("alleen schuimbeton", aannemers): nul vraagsignaal.
- **Ads geo `--apply`**: geo staat al op DR+GR+FR; dry-run bevestigde geen wijziging nodig.
- **Heerenveen-keyword pauzeren i.p.v. pagina bouwen**: pagina bouwen is beter voor QS + organisch (max 1 nieuwe pagina-regel ingezet).

---

## Social Media
**Status:** Weekplanning in `docs/website-manager/social/weekly_calendar.md` (7 posts, week van 1 jul).
**Actie vereist:** Handmatige publicatie door VLWarmte-team. Focus: wizard (2× prijsindicatie) + stadspagina's (Zuidlaren, Drachten, Drenthe-hub).
**Materiaal:** 5 unieke beelden deze week (verbetering t.o.v. cyclus 18–19); eindresultaat-, verdeler- en teamfoto ontbreken nog.

---

## ESCALATIE — vereist eigenaar (NIET autonoom)

1. **Google Ads budget** — ~€2/dag levert 2 leads/30d bij ~10,5% ratio. Verhoging (bijv. €5–10/dag) is de snelste schaalhefboom. `python scripts/google_ads_update_campaign_budget.py` alleen na jouw spend-goedkeuring.
2. **GSC OAuth** — refresh token verlopen (`invalid_grant`). Run: `python scripts/gsc_get_refresh_token.py` met verified owner-account, daarna `gsc_fetch.py` in volgende cyclus.
3. **Beeldmateriaal** — lever eindresultaat-, verdeler- en teamfoto in `beeldmateriaal/projecten/` of `docs/website-manager/social/input/`.
4. **Release-mail** (stap 8b) — `python3 scripts/send_pm_release_notes_email.py` met `secrets/hostnet-mail.env`.

---

## Context voor volgende sprint
- **Week ~27 jul:** wizard `wizard_lead_submit` meten — bij nog 0: funnel-events uitlezen.
- **GSC:** zodra OAuth werkt, SEO-effect cyclus 17–20 toetsen (stadindexatie, Heerenveen, Zuidlaren-CTR).
- **Betaald kanaal:** 100% van conversies; budgetbesluit bij eigenaar.
- **Heerenveen:** na livegang Ads Quality Score en eerste GSC-impressies volgen.

---

## Developer Rapport — 1 juli 2026, 22:15

- **Geïmplementeerde taken:**
  1. `vloerverwarming-heerenveen.html` — nieuwe stadspagina (patroon Leeuwarden/Drachten), wizard-CTA boven de vouw, trust-strip, structured data, sitemap, footer-regio-links op alle pagina's; interne links met ankertekst `vloerverwarming Heerenveen` vanaf `vloerverwarming-leeuwarden.html`, `vloerverwarming-drachten.html`, `vloerverwarming-drenthe.html`, `diensten.html` en `index.html`.
  2. `diensten.html` — onderste `cta-band`: primair wizard (`Richtbedrag in 2 minuten →`), secundair contact-offerte.
  3. `systemen-producten.html` — hero met regio-belofte (DR/GR/FR), trust-strip (10 jaar buis, één werkdag), primaire wizard-CTA.
  4. `contact.html` — compact wizard-teaser (`contact-process`) boven `#aanvraag`, zichtbaar in alle modi, secundaire knop.
  5. `werkwijze.html` — mid-page `cta-band` na stappen-overzicht, vóór slot-offerte-CTA.
- **Overgeslagen taken:** geen — alle `[GOEDGEKEURD]`-taken uitgevoerd; `[WACHT]`/`[AFGEWEZEN]` niet aangeraakt.
- **Deployment:** **Live** — PM commit `d31b738` + push naar `main` op 01-07-2026 21:29. GitHub Pages-run `28542479046` (pages build and deployment): **success** in 37s. Heerenveen-pagina geverifieerd (HTTP 200). GA4-tag `G-0BB9M7HYSF` in `assets/js/ga-deferred.js`.
- **Live URL:** https://www.vlwarmte.nl/vloerverwarming-heerenveen.html
- **Aandachtspunten voor volgende sprint:** `vloerverwarming-drachten.html` combineert nog steeds Drachten+Heerenveen in title/H1/meta — overweeg Drachten-only refactor als Heerenveen-pagina geïndexeerd is; Ads-landing-URL voor keyword `vloerverwarming heerenveen` handmatig naar nieuwe pagina wijzen indien nog op homepage/drachten; GSC OAuth nog steeds `invalid_grant`.

---
