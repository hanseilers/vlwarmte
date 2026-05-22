# Sprint — week van 22 mei 2026 (cyclus 12)

**PM beslissing genomen op:** 22-05-2026 (GA4-fetch `2026-05-22T17:32:56`, cyclus 11 ~2 dagen live)
**Doel deze sprint:** Meetvenster rustig houden voor cyclus 9–11, wél Drachten + social/Ads message-match versterken (interne links, diensten→projecten, defaults) — geen hero-retweak op pagina’s met open meetdoelen.
**Meetdoel:** binnen 4 weken (fetch ~15 juni): (a) harde beoordeling cyclus 9–11 meetdoelen; (b) ≥1 organisch sessie `vloerverwarming-drachten.html`; (c) `projecten.html` entry-bounce <90% bij ≥10 entry-sessies; (d) Paid Search attributie vastgelegd in PM-notitie; (e) `diensten.html` landing bounce/conv trend niet verslechteren t.o.v. 73%/3 conv.

---

## Goedgekeurde taken voor Developer Agent

### Taak 1: Interne links Drachten ↔ projecten `[GOEDGEKEURD]`
**Bron:** Analytics Agent (P1 SEO) + Marketing Research Agent (P1 Drachten)
**Prioriteit:** Midden — SEO / distributie
**Actie:**
1. Op `projecten.html`: in hero-lead één zin met link naar `vloerverwarming-drachten.html` (Friesland / Drachten & Heerenveen — nuchter, geen extra H2).
2. Op `vloerverwarming-drachten.html`: kort blok of zin vóór eerste grote sectie met link naar `projecten.html` (“Bekijk uitgevoerd werk in de regio” of vergelijkbaar).
3. `sitemap.xml`: `lastmod` voor `projecten.html` en `vloerverwarming-drachten.html` op **2026-05-22**.
**Succescriterium:** beide pagina’s linken naar elkaar; sitemap datums bijgewerkt; geen gebroken hrefs.

### Taak 2: `diensten.html` — hero-link naar projecten `[GOEDGEKEURD]`
**Bron:** Analytics Agent (P1 CRO) + Social Media Agent (post 3)
**Prioriteit:** Midden — conversie / message-match
**Actie:** In hero, onder de bestaande primaire knop (prijsindicatie), voeg in de bestaande `small`-regel een link toe: “Bekijk uitgevoerd werk” → `projecten.html` (max. één extra link; **geen** tweede hero-knop — conform `b040cea`).
**Succescriterium:** link zichtbaar in hero zonder scroll op desktop; mobiel plausibel ATF; geen dubbele primaire CTA’s.

### Taak 3: Google Ads defaults — projecten-URL + Meppel-keyword `[GOEDGEKEURD]`
**Bron:** Marketing Research Agent (P1 Ads prep)
**Prioriteit:** Laag — voorbereiding (geen API-run)
**Actie:**
1. Voeg `https://www.vlwarmte.nl/projecten.html` toe aan `final_urls` in `scripts/data/google_ads_lead_campaign_defaults.json`.
2. Verwijder keyword `vloerverwarming meppel` uit `keywords` (geen landingspagina); noteer in JSON-comment bij keywords dat Meppel backlog is.
3. **Geen** `google_ads_*`-scripts, geen `--apply`, geen `--go-live`.
**Succescriterium:** JSON geldig; projecten in `final_urls`; meppel niet meer in actieve keywords.

### Taak 4: `vloerverwarming-drachten.html` — OG-afbeelding `[GOEDGEKEURD]`
**Bron:** Marketing Research Agent (social/Drachten-post 7)
**Prioriteit:** Laag — SEO/social share
**Actie:** Vervang `og:image` / `twitter:image` van `og-default.png` naar `https://www.vlwarmte.nl/assets/img/og-projecten.jpg` (zelfde als projecten — echt werkbeeld).
**Succescriterium:** meta tags wijzen naar `og-projecten.jpg`; bestand bestaat al in repo.

### Taak 5: Opschonen werkmap `[GOEDGEKEURD]`
**Bron:** PM
**Prioriteit:** Laag
**Actie:** Herstel `diensten.html` naar alleen inhoudelijke wijzigingen (geen footer-whatsapp reformat-only diff). `git checkout` formatting-only wijzigingen indien nodig vóór taak 2.
**Succescriterium:** `git diff diensten.html` bevat alleen hero-link + eventueel taak-2 copy.

---

## Uitgestelde voorstellen `[WACHT]`

- **GA4 ↔ Ads + Paid Search-attributie (P0):** sessie ~1 juni — geen developer-code.
- **Cyclus 9–11 meetdoelen bijsturen:** tot juni-fetch (~1–15 juni).
- **`over-ons.html` ATF-CTA:** na juni-fetch bij 80% bounce / 0 conv.
- **`diensten.html` duo-CTA hero:** niet heropenen vóór juni-fetch.
- **RSA `--apply`:** na PO + attributiefix (`google_ads_add_rsa_variant.py`).
- **`vloerverwarming-renovatie-houten-vloer.html`:** volgende cyclus (max. 1 pagina/sprint).
- **Assen hero-herontwerp:** na juni-fetch.

---

## Afgewezen voorstellen `[AFGEWEZEN]`

- **Projecten entry-CTA’s opnieuw bouwen** — hero heeft al duo-CTA + trust-strip; afwachten data.
- **Nieuwe city-pagina Meppel** — keyword uit defaults; pagina later.
- **Ads live mutaties deze sprint** — alleen JSON-voorbereiding.

---

## Social Media
**Status:** Weekplanning in `docs/website-manager/social/weekly_calendar.md` (22–28 mei; Zeegse/Zuidlaren, projecten, diensten, Drachten).
**Actie vereist:** Handmatige publicatie door VLWarmte-team.

---

## Context voor volgende sprint
- **Juni-fetch:** harde beoordeling alle open meetdoelen; RSA sync; over-ons/Assen alleen bij falen.
- **Paid Search 0/13** blijft P0 tot attributiesessie.
- Social kalender gebruikt `projecten.html` en Drachten-URL — taak 1–2 ondersteunen die CTAs.

---

## Developer Rapport — 22-05-2026

- Geïmplementeerde taken: Taak 1 (kruislinks projecten↔Drachten + sitemap `lastmod`), Taak 2 (hero-link projecten op `diensten.html`), Taak 3 (`final_urls` + meppel-keyword uit defaults), Taak 4 (OG/twitter `og-projecten.jpg` op Drachten), Taak 5 (`diensten.html` formatting-only diff teruggedraaid).
- Overgeslagen taken: geen.
- Deployment: **Live** 22-05-2026 — commit `8fff9dd`; `git push origin main` geslaagd. GitHub Pages run **26297204197** (success, ~39s); E2E **26297205481** gestart na push.
- Live URL: https://www.vlwarmte.nl
- Aandachtspunten: RSA `--apply` en live Meppel-keyword in Ads UI nog handmatig/API na PO; juni-fetch bepaalt vervolg op projecten/over-ons/Assen.
