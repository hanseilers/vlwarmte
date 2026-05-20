# Sprint — week van 20 mei 2026 (cyclus 11)

**PM beslissing genomen op:** 20-05-2026 (GA4-fetch `2026-05-20T13:06:34`, cyclus 10 ~2 dagen live)
**Doel deze sprint:** Eerste echte projectcases live zetten op `projecten.html` (vertrouwen + doorstroom), Drachten beter vindbaar maken, en `diensten.html` als zwakke landing versterken — zonder premature bijsturing op cyclus-9/10-meetpunten of Ads-spend.
**Meetdoel:** binnen 4 weken in GA4 (fetch rond 15 juni): (a) `projecten.html` entry-bounce <90% en ≥2 scrollers (90d); (b) ≥1 sessie op `vloerverwarming-drachten.html`; (c) `diensten.html` landing-bounce <70% of ≥1 conversie; (d) cold `/contact.html` bounce daalt t.o.v. 80% entry; (e) juni-fetch hard beoordelen cyclus 9–10 meetdoelen (geen extra tweaks vóór die fetch).

---

## Goedgekeurde taken voor Developer Agent

### Taak 1: Echte projectcases op `projecten.html` `[GOEDGEKEURD]`
**Bron:** Product owner inbound (20-05) + Marketing Research Agent (P0) + Analytics Agent (P0 CRO)
**Prioriteit:** Hoog — conversie / vertrouwen
**Akkoord:** PO heeft beeldmateriaal en README-metadata aangeleverd in `beeldmateriaal/projecten/` (Zeegse, Zuidlaren) — dat geldt als akkoord voor publicatie van deze twee plaatsnamen en werkbeelden op de site.
**Actie:**
1. Vervang de drie generieke kaarten (Groningen/Friesland/Drenthe) door **twee case-cards** op basis van de README’s:
   - **Zeegse:** 100 m² vloerverwarming; souterrain + begaande grond (kort, nuchter: situatie / oplossing / resultaat).
   - **Zuidlaren:** 50 m² op draadstaalnetten; benedenverdieping.
2. Kopieer de projectfoto’s naar `assets/img/projecten/` (hernoem naar korte webvriendelijke namen, bijv. `zeegse-1.jpeg`, `zuidlaren-1.jpeg`); gebruik in HTML **alleen** die paden (geen `beeldmateriaal/` in `src`).
3. Hero: vervang het huidige root-beeld door het sterkste Zuidlaren- of Zeegse-foto uit de nieuwe assets; passende `alt`-tekst met plaats + werkfase.
4. Voeg per case-card een link toe: Zuidlaren → `vloerverwarming-zuidlaren.html`; Zeegse → `contact.html?modus=offerte#aanvraag` (geen city-pagina).
5. ATF duo-CTA (prijsindicatie + offerte) **ongewijzigd** laten.
6. **Geen** `projecten` in hoofdnavigatie (nog <3 cases); wel op `index.html` en `diensten.html` één contextuele tekstlink “Bekijk uitgevoerd werk” → `projecten.html` (max. 1 link per pagina, binnen bestaande copy).
**Succescriterium:** twee echte cases met foto + metadata live; hero uit projectassets; geen placeholder-cards meer; interne links kloppen; pagina laadt normaal.

### Taak 2: `projecten.html` in sitemap + footer-distributie Drachten `[GOEDGEKEURD]`
**Bron:** Analytics Agent (P1 SEO) + Marketing Research Agent
**Prioriteit:** Midden — SEO
**Actie:**
1. Zet `projecten.html` in `sitemap.xml` met `lastmod` 2026-05-20 en passende `priority` (0.7).
2. Voeg op **alle root-HTML-pagina’s** in de footer-citylijst (zelfde `<ul>` als andere stadspagina’s) een link toe naar `vloerverwarming-drachten.html` (“Vloerverwarming Drachten”), op dezelfde positie als op `vloerverwarming-drachten.html` zelf (na Leeuwarden of logische alfabetische volgorde — consistent houden).
**Succescriterium:** sitemap bevat `projecten.html`; elke root-pagina footer linkt naar Drachten; geen gebroken hrefs.

### Taak 3: `diensten.html` — compacte keuze-CTA boven de vouw `[GOEDGEKEURD]`
**Bron:** Analytics Agent (P1 CRO — 78,6% landing-bounce, 0 conv)
**Prioriteit:** Midden — conversie
**Actie:** Direct onder de hero-lead (vóór de eerste grote contentblokken) een korte regel + duo-CTA in bestaande site-stijl (`hero-cta-row` of `cta-band`): “Eerst een bandbreedte of meteen offerte?” — knoppen naar `prijsindicatie.html#kosten-uitleg` en `contact.html?modus=offerte#aanvraag`. Geen nieuwe zware afbeeldingen.
**Succescriterium:** duo-CTA zichtbaar zonder scroll op desktop; op mobiel plausibel in eerste scherm; links kloppen.

### Taak 4: Ads-defaults copy — referenties naar live projecten `[GOEDGEKEURD]`
**Bron:** Marketing Research Agent (P1 Ads)
**Prioriteit:** Laag — voorbereiding (geen live Ads-mutatie)
**Actie:** Pas in `scripts/data/google_ads_lead_campaign_defaults.json` onder `extra_rsa` (of equivalent) minstens één headline/description aan van “Referenties op aanvraag” naar copy die verwijst naar uitgevoerd werk op `https://www.vlwarmte.nl/projecten.html` (bijv. “Bekijk uitgevoerd werk in Drenthe”). **Geen** `google_ads_*`-scripts draaien, geen `--apply`, geen `--go-live`.
**Succescriterium:** JSON syntactisch geldig; RSA-tekst sluit aan op live projectenpagina na taak 1.

### Taak 5: Commit `beeldmateriaal/projecten/` + README’s `[GOEDGEKEURD]`
**Bron:** Product owner inbound
**Prioriteit:** Laag — bronnen behouden
**Actie:** Zorg dat `beeldmateriaal/projecten/` (submappen, README’s, bron-JPEG’s) in de repo staat voor social/PM — geen secrets. Als al getrackt: alleen controleren; anders toevoegen aan git in PM-commit.
**Succescriterium:** beide projectmappen + README’s versioneerbaar in repo na deploy.

---

## Uitgestelde voorstellen `[WACHT]`

- **GA4 ↔ Ads + Paid Search-attributie (P0):** 13 Paid Search-sessies / 0 conv vs Cross-network 9/42 — account/skill-sessie rond **1 juni**, geen developer-code.
- **Cyclus 9–10 meetdoelen bijsturen:** projecten/over-ons/cold contact/prijsindicatie entry — **niet** hertweaken vóór juni-fetch (~15 juni); cyclus-11 projectcases zijn inhoud, geen rollback van ATF/deeplinks.
- **`over-ons.html` entry ATF-CTA:** pas als juni-fetch nog 80% bounce / 0 conv.
- **`vloerverwarming-assen.html` hero-herontwerp:** 0 scrollers 90d — juni-fetch.
- **`vloerverwarming-renovatie-houten-vloer.html`:** max 1 nieuwe pagina/sprint — volgende cyclus.
- **`vloerverwarming-meppel.html`:** alleen bij zoekterm-signaal.
- **Ads `--apply` / Final URL-sync / `--go-live`:** na spend-goedkeuring + attributiefix.
- **`projecten` in hoofdnav:** pas bij ≥3 echte cases.

---

## Afgewezen voorstellen `[AFGEWEZEN]`

- **Wachten op meer cases vóór publicatie:** afgewezen — twee cases vervangen drie placeholders; PO-materiaal is voldoende voor deze sprint.
- **Aparte referrals-URL of city-pagina Zeegse:** afgewezen — geen extra pagina; case op `projecten.html` volstaat.
- **RSA live pushen via API deze sprint:** afgewezen — alleen defaults-JSON; PM/owner beslist over `--apply`.

---

## Social Media
**Status:** Weekplanning in `docs/website-manager/social/weekly_calendar.md` (7 posts; Zeegse/Zuidlaren-foto’s, Drachten-pagina, projecten-route). **Na taak 1 live:** LinkedIn post 2 en Instagram-posts met Zeegse/Zuidlaren mogen plaatsnamen gebruiken; post 3 CTA naar `projecten.html` toont dan echte cases.
**Actie vereist:** Handmatige publicatie door VLWarmte-team.

---

## Context voor volgende sprint
- **Juni-fetch (~1–15 juni):** harde beoordeling cyclus 9–10 + 11 meetdoelen; Paid Search vs Cross-network; Drachten organisch.
- **Na live projectcases:** RSA `--apply` overwegen; social “referenties”-posts hergebruiken met site-URL.
- Verkeer blijft laag (44 sessies/week 13–19 mei) — trend meten, niet overreageren op kleine samples.

---

## Developer Rapport — 20-05-2026

- Geïmplementeerde taken: Taak 1 (Zeegse + Zuidlaren cases op `projecten.html`, hero + assets), Taak 2 (`sitemap.xml` + Drachten in footer op alle root-HTML), Taak 3 (duo-CTA onder hero op `diensten.html`), Taak 4 (`extra_rsa` copy in `google_ads_lead_campaign_defaults.json`), Taak 5 (`beeldmateriaal/projecten/` bronmappen aanwezig en versioneerbaar).
- Overgeslagen taken: geen — alle `[GOEDGEKEURD]` taken uitgevoerd; `[WACHT]` en `[AFGEWEZEN]` niet aangeraakt.
- Deployment: **Nog niet live** — PM voert commit + `git push origin main` uit; daarna: [PM vult run-id / succes in]
- Live URL: https://www.vlwarmte.nl
- Aandachtspunten voor volgende sprint: `logo-varianten.html` heeft geen footer (redirect-stub). RSA `--apply` nog niet gedraaid (bewust). Optioneel: `zeegse-2.jpeg` later als tweede beeld in case-card; OG-image `projecten.html` nog `og-default.png`.
