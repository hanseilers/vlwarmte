# Sprint — week van 18 mei 2026 (cyclus 10)

**PM beslissing genomen op:** 18-05-2026 (verse GA4-fetch `2026-05-18T06:05:10`, eerste meting ná cyclus-9-deploy)
**Doel deze sprint:** Friesland-lek op betaald verkeer dichten (Drachten/Heerenveen), de bewezen offerte-deeplink site-breed afdwingen, en de zwakste instappunten (over-ons, projecten) naar de offerte-/prijsroute laten doorstromen.
**Meetdoel:** binnen 4 weken in GA4 (fetch rond 15 juni): (a) eerste organische sessies op `vloerverwarming-drachten.html`; (b) lagere bounce op cold `/contact.html` mét hogere doorstroom naar `?modus=offerte`; (c) `over-ons.html` entry-bounce <80% en >0 conversies; (d) `projecten.html` entry-bounce <90% en >0 scrollers; (e) géén keyword in Ads-defaults meer zonder bijpassende landingspagina.

---

## Goedgekeurde taken voor Developer Agent

### Taak 1: Nieuwe stadspagina `vloerverwarming-drachten.html` `[GOEDGEKEURD]`
**Bron:** Marketing Research Agent (P0/Hoog), Analytics Agent (Friesland sterk ondervertegenwoordigd: 4 vs Drenthe 164)
**Prioriteit:** Hoog — SEO + sluit betaald message-match-lek
**Actie:** Maak `vloerverwarming-drachten.html` exact volgens het patroon van `vloerverwarming-leeuwarden.html` (zelfde structuur, meta, schema, hero, trust-band, CTA's). Inhoud toegespitst op Drachten én de directe omgeving (Heerenveen, Friesland-zuidoost) — noem Heerenveen expliciet in de copy/koppen zodat het Ads-keyword `vloerverwarming heerenveen` message-match houdt. Voeg de pagina toe aan `sitemap.xml` en aan de footer-citylijst (zelfde plek als de andere city-pagina's). Pas in `scripts/data/google_ads_lead_campaign_defaults.json` de `final_urls` zo aan dat de keywords `vloerverwarming drachten` en `vloerverwarming heerenveen` naar `https://www.vlwarmte.nl/vloerverwarming-drachten.html` wijzen. **Géén `--go-live`, geen spend, geen Ads-mutatiescript draaien** — alleen het defaults-JSON-bestand in de repo bijwerken.
**Succescriterium:** pagina is lokaal valide HTML, staat in sitemap + footer, deeplinkt naar `contact.html?modus=offerte#aanvraag`; defaults-JSON heeft geen keyword meer zonder bijpassende live URL.

### Taak 2: Offerte-deeplink site-breed afdwingen `[GOEDGEKEURD]`
**Bron:** Analytics Agent (Hoog/CTA) + Marketing Research Agent
**Prioriteit:** Hoog — conversie
**Actie:** Loop alle pagina's in de repo-root na op knoppen/links met offerte-/aanvraag-intentie ("Offerte aanvragen", "Vraag offerte", "Aanvragen", primaire CTA's) die nu naar kale `contact.html` of `contact.html#aanvraag` linken. Laat al die offerte-intentie-links hard naar `contact.html?modus=offerte#aanvraag` wijzen. Links met expliciet informatie-/bel-intentie ongemoeid laten. Niet de cyclus-9 contact-intent-strip zelf herschrijven — alleen verwijzende links elders op de site.
**Succescriterium:** geen enkele offerte-CTA op de site linkt nog naar kale `contact.html`; alle naar `?modus=offerte#aanvraag` (data: 9,1% bounce / 10 conv vs 80% kaal).

### Taak 3: `over-ons.html` vervolg-CTA-blok `[GOEDGEKEURD]`
**Bron:** Analytics Agent (Midden/CRO — nieuw signaal: entry 80% bounce, 0 conv, ~32 s)
**Prioriteit:** Midden — conversie
**Actie:** Voeg onderaan `over-ons.html` (vóór de footer) een duidelijk, nuchter vervolg-CTA-blok toe in dezelfde stijl als andere pagina's: korte regel + twee knoppen — "Bekijk prijsindicatie" → `prijsindicatie.html#kosten-uitleg` en "Vraag offerte aan" → `contact.html?modus=offerte#aanvraag`.
**Succescriterium:** CTA-blok staat live onderaan over-ons, links kloppen, stijl consistent met de rest van de site.

### Taak 4: `projecten.html` ATF compacter + duo-CTA `[GOEDGEKEURD]`
**Bron:** Marketing Research Agent (Hoog/CRO) + Analytics Agent (entry ~100% bounce, ~7,5 s — persistent sinds cyclus 7/8)
**Prioriteit:** Midden — conversie
**Actie:** Maak het eerste scherm van `projecten.html` compacter zodat er binnen één beeldhoogte een primaire duo-CTA zichtbaar is vóór de zware projectgalerij: "Bekijk prijsindicatie" → `prijsindicatie.html#kosten-uitleg` en "Vraag offerte aan" → `contact.html?modus=offerte#aanvraag`. Galerij eronder intact laten; geen nieuwe pagina, geen zware LCP-elementen toevoegen.
**Succescriterium:** duo-CTA zichtbaar boven de vouw op `projecten.html`; pagina laadt normaal; galerij ongewijzigd.

### Taak 5: Interne contextuele links naar kosten-sectie + city-pagina's `[GOEDGEKEURD]`
**Bron:** Marketing Research Agent (interne linkstructuur) + Analytics Agent (homepage trekt 164/30d — distributiepunt)
**Prioriteit:** Midden — SEO/funnel, versterkt taken 1, 2 en 4
**Actie:** Voeg vanaf `index.html` en `diensten.html` enkele contextuele tekstlinks toe (binnen bestaande content, geen nieuwe blokken forceren) naar `prijsindicatie.html#kosten-uitleg` ("wat kost vloerverwarming per m²") en naar de city-pagina's inclusief de nieuwe `vloerverwarming-drachten.html`. Natuurlijke ankerteksten, geen keyword-stuffing, max 2–3 links per pagina.
**Succescriterium:** relevante interne links live op homepage + diensten, ankerteksten lopen natuurlijk, alle hrefs valide.

---

## Uitgestelde voorstellen `[WACHT]`

- **GA4 ↔ Ads conversiekoppeling (P0):** kernprobleem blijft (betaald ~42 ses, Paid Search 0 conv). Vereist een sessie mét Ads-script- en GA4-accountrechten; deze automatische run kon `google_ads_*`-scripts niet draaien en GA4-admin niet wijzigen. **Plannen rond 1 juni** samen met de vervolg-fetch — geen developer-code-taak.
- **Cyclus-9 meetdoelen niet bijsturen:** contact-intent-strip, Assen lees-verder-anker, prijsindicatie `#kosten-uitleg`, projecten offerte-CTA — 3 dagen post-deploy is ruis. Hard beoordelen bij de juni-fetch; nu bewust niet hertweaken (op projecten doen we alleen een aanvullende ATF-ingreep, taak 4, geen herziening van de cyclus-9-CTA).
- **`vloerverwarming-assen.html` hero-herontwerp:** 0 scrollers 90d, maar cyclus-9-anker eerst 30 dagen laten meten. Bij juni-fetch beslissen.
- **`vloerverwarming-renovatie-houten-vloer.html`:** zinvolle contentgap, maar max 1 nieuwe pagina/sprint (Drachten heeft voorrang: betaald lek). Volgende cyclus.
- **NL-only GA4-rapportagesegment / bot-filter:** GA4-config, geen repo-code; backlog voor de meet-sessie van 1 juni.

---

## Afgewezen voorstellen `[AFGEWEZEN]`

- **Keywords Drachten/Heerenveen uit defaults verwijderen:** afgewezen ten gunste van taak 1 — een landingspagina draagt direct bij aan leadgeneratie, het schrappen van keywords doet het tegenovergestelde (PM-regel: bij twijfel de leadgen-positieve variant).
- **`logo-varianten.html` herontwerp:** geen sprintwaarde; alleen een low-prio technische redirect-/Search Console-check, hoort niet in een developer-sprint thuis.

---

## Social Media
**Status:** Weekplanning staat in `docs/website-manager/social/weekly_calendar.md` (7 posts: 3 LinkedIn di–do, 4 Instagram wo/vr/za). CTA's sturen kosten-intent naar `prijsindicatie.html` en offerte-intent naar `contact.html?modus=offerte#aanvraag`. Drachten/Heerenveen bewust geen city-claim tot de pagina live is.
**Actie vereist:** Handmatige publicatie door VLWarmte-team.

---

## Context voor volgende sprint
- **Plan een GA4-fetch + Ads-verificatiesessie rond 1 juni 2026** in een omgeving waar de `google_ads_*`-scripts én WebSearch mogen draaien. Dan pas: (1) cyclus-9 meetdoelen a–e hard beoordelen, (2) GA4↔Ads-koppeling sluiten, (3) verse zoekvolumes/SERP toevoegen.
- Verkeer daalt drie weken op rij (48 ses laatste volle week vs piek 172) — kleine landing-volumes maken sprint-effecten traag meetbaar; beoordeel op trend, niet op absolute weekcijfers.
- Na Drachten: Friesland-cluster verder uitbouwen (Heerenveen eigen pagina of Assen-herontwerp) afhankelijk van juni-data.

---

## Developer Rapport — 18-05-2026 (automatische run)

- **Geïmplementeerde taken:** Taak 1, 2, 3, 4, 5 (alle 5 `[GOEDGEKEURD]`).
- **Overgeslagen taken:** alle `[WACHT]` en `[AFGEWEZEN]` voorstellen (buiten scope, conform opdracht).

### Per taak

**Taak 1 — `vloerverwarming-drachten.html` — GELUKT**
- Bestanden: `vloerverwarming-drachten.html` (nieuw, exact patroon van `vloerverwarming-leeuwarden.html`), `sitemap.xml` (regel toegevoegd, lastmod 2026-05-18, priority 0.8), `scripts/data/google_ads_lead_campaign_defaults.json` (`final_urls` uitgebreid met de Drachten-URL — géén script gedraaid, géén `--go-live`, géén spend).
- Copy toegespitst op Drachten én Heerenveen (Heerenveen expliciet in title, meta, H1 en koppen → message-match voor Ads-keyword `vloerverwarming heerenveen`). Footer-citylijst van de nieuwe pagina bevat Drachten op de vaste plek.
- Smoke: GA4 `ga-deferred.js` aanwezig (1×); Drachten 1× in sitemap; 1× in JSON `final_urls`; JSON- en XML-blok syntactisch correct (komma/sluittags gecontroleerd); noscript CSS-fallback aanwezig (leesbaar zonder JS); hero deeplinkt naar `contact.html?modus=offerte#aanvraag`. Keywords `vloerverwarming drachten` + `vloerverwarming heerenveen` hebben nu een live landingspagina.
- Aandachtspunt: Drachten staat nog niet in de footer-citylijst van de ANDERE bestaande pagina's (die lijsten zijn niet uniform en de sprint vroeg expliciet alleen om opname op "dezelfde plek als de andere city-pagina's" + sitemap + JSON). Footer-citylijst van overige pagina's is bewust ongemoeid gelaten (conservatieve variant; geen scope-creep). PM kan dit als losse vervolgtaak oppakken indien gewenst.

**Taak 2 — Offerte-deeplink site-breed — GELUKT**
- Bestanden: alle 19 root-HTML-pagina's (`404, contact, diensten, disclaimer, faq, index, over-ons, prijsindicatie, privacy, projecten, systemen-producten, werkwijze, vloerverwarming-{assen,emmen,groningen,hoogeveen,leeuwarden,zuidlaren}` + nieuwe `drachten`).
- Wijziging: de site-brede primaire CTA `<a class="drawer-cta">Informatie / Offerte aanvragen</a>` wees naar kale `contact.html` → nu hard `contact.html?modus=offerte#aanvraag`. Dit was de enige offerte-intentie-link site-breed die nog naar kaal contact ging.
- Bewust ongemoeid (informatie-/bel-intentie of ambigu, conform sprintregel): `diensten.html` "Plan een informatiegesprek", `index.html` "Ja, graag" (copy zegt expliciet "informatie aan of direct een offerte" → mixed/ambigu, conservatief gelaten), `404.html` "Contact", alle nav-/footer-/inline "Contact"-tekstlinks (info-intentie), `tel:`-links, `?modus=bel`/`?modus=informatie`-links. De cyclus-9 contact-intent-strip zelf is niet herschreven.
- Smoke: 0 resterende `drawer-cta` met kale `contact.html`; 19/19 deeplinked.

**Taak 3 — `over-ons.html` vervolg-CTA-blok — GELUKT**
- Bestanden: `over-ons.html`. Nieuw `cta-band`-blok vóór de footer, zelfde stijl als de rest van de site: regel + twee knoppen — "Bekijk prijsindicatie" → `prijsindicatie.html#kosten-uitleg`, "Vraag offerte aan" → `contact.html?modus=offerte#aanvraag`.
- Smoke: blok staat ná de laatste content-sectie en vóór `</main>`/footer; `#kosten-uitleg`-anchor bestaat in `prijsindicatie.html`; semantische HTML, geen inline styles.

**Taak 4 — `projecten.html` ATF compacter + duo-CTA — GELUKT**
- Bestanden: `projecten.html`. Hero ingekort: kortere lead, eyebrow → "Uitgevoerd werk", de note-regel verwijderd, CTA-rij teruggebracht tot een primaire duo-CTA ("Bekijk prijsindicatie" → `prijsindicatie.html#kosten-uitleg`, "Vraag offerte aan" → `contact.html?modus=offerte#aanvraag`) — zichtbaar binnen het eerste scherm vóór de projectgalerij.
- Galerij ("Typische uitdaging, passende oplossing" + cards) volledig ongewijzigd; geen nieuwe zware/LCP-elementen toegevoegd (hero-afbeelding ongewijzigd).
- Smoke: duo-CTA staat boven de galerij-sectie; pagina-structuur intact.

**Taak 5 — Interne contextuele links — GELUKT**
- Bestanden: `index.html`, `diensten.html`. Binnen bestaande `<p class="small">`-content (geen nieuwe blokken):
  - `index.html`: link "Wat kost vloerverwarming per m²" → `prijsindicatie.html#kosten-uitleg`, plus regel met links naar `vloerverwarming-drachten.html` en `vloerverwarming-leeuwarden.html`.
  - `diensten.html`: regio-alinea aangevuld met `vloerverwarming-drachten.html` en "wat vloerverwarming per m² kost" → `prijsindicatie.html#kosten-uitleg`.
- Natuurlijke ankerteksten, geen keyword-stuffing, ≤3 links per pagina. Alle hrefs verwijzen naar bestaande bestanden/anchors.

### Overig
- **Deployment:** **Nog niet live** — geen `git commit`/`git push` uitgevoerd (conform developer-agent.md; PM voert commit + `git push origin main` uit). [PM vult run-id / succes in]
- **Live URL:** https://www.vlwarmte.nl
- **Geen** credentials/secrets/service-account-JSON/`node_modules` aangeraakt. Alleen `scripts/data/google_ads_lead_campaign_defaults.json` (defaults, geen geheimen). Géén `google_ads_*`-scripts gedraaid.
- **Aandachtspunten volgende sprint:** (1) footer-citylijsten van de bestaande root-pagina's zijn niet uniform en bevatten Drachten nog niet — overweeg een uniformerings-taak; (2) `index.html` "Ja, graag" en `diensten.html` "Plan een informatiegesprek" zijn bewust niet ge-deeplinkt (mixed/info-intentie) — herijken bij juni-data indien conversie tegenvalt.
