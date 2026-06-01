# Sprint — week van 2 juni 2026 (cyclus 14)

**PM beslissing genomen op:** 2026-06-01 11:15
**Doel deze sprint:** Paid Search en organische stad-pagina's laten landen op bewezen converters — Assen-UX fixen, prijsindicatie message-match ATF, defaults-JSON vastleggen; GSC/Ads-koppeling voorbereiden buiten developer-scope.
**Meetdoel:** in 4 weken (juni-fetch ~22 juni) — (a) `vloerverwarming-assen.html` bounce <70%, gem. duur >5 s; (b) `prijsindicatie.html` entry-bounce <45% bij ≥10 entry-sess; (c) Paid Search ≥1 conv. na RSA-landing + GA4↔Ads (PO/Admin); (d) GSC-fetch beschikbaar voor sprint-13 SEO-check.

---

## Goedgekeurde taken voor Developer Agent

### Taak 1: `vloerverwarming-assen.html` — layout-fix (Groningen-template) `[GOEDGEKEURD]`
**Bron:** Analytics Agent (#2) + Marketing Research Agent (#2) — diagnose cyclus 13
**Prioriteit:** Hoog
**Actie:**
- Verwijder `<p class="small project-hero__readnext">…</p>` uit de hero.
- Verwijder de hele `cta-band`-sectie "Volgende stap" direct ná de hero (vóór `#waarom-vlwarmte-assen`). De bestaande CTA-band onderaan de pagina blijft staan.
- Optioneel: hero-image vervangen door lichtere variant uit `beeldmateriaal/` als bestand ≤500 KB beschikbaar is; anders ongewijzigd.
- Geen andere stad-pagina's aanpassen.
**Succescriterium:** Mobiel (375×667): hero gaat direct over in waarom-content; bounce <70% en gem. duur >5 s binnen 4–6 weken (nu 86% / 0,7 s).

### Taak 2: `prijsindicatie.html` — ATF message-match `[GOEDGEKEURD]`
**Bron:** Marketing Research Agent — entry-bounce 58,3% op 12 sess; title belooft "richtbedrag in 2 minuten"
**Prioriteit:** Hoog (CTA/conversie)
**Actie:**
- Vervang de `page-hero` `.lead`-tekst door één korte zin die de title belofte spiegelt, bijv.: `In ongeveer twee minuten krijg je een vrijblijvend richtbedrag — eerst kies je wat je wilt laten prijzen, daarna de passende vragen.`
- Verwijder de lange FAQ-verwijzing uit de lead (FAQ-link mag in wizard-context of footer blijven, niet in hero-lead).
- Geen wijziging aan wizard-stappen of formulier.
**Succescriterium:** Hero-lead noemt expliciet "twee minuten" / richtbedrag; entry-bounce daalt richting <45% bij ≥10 entry-sess in juni-fetch.

### Taak 3: `prijsindicatie.html` — OG/Twitter meta aligneren `[GOEDGEKEURD]`
**Bron:** Marketing Research Agent (message-match paid/organic)
**Prioriteit:** Midden (SEO/social preview)
**Actie:**
- Zet `og:title` en `twitter:title` gelijk aan de bestaande `<title>` (Drenthe & Noord-NL — richtbedrag in 2 minuten).
- Zet `og:description` en `twitter:description` gelijk aan `<meta name="description">`.
- Geen body-wijziging.
**Succescriterium:** Social previews tonen dezelfde belofte als SERP-title; Lighthouse/HTML valid blijft OK.

### Taak 4: `index.html` — Assen-link in Drenthe-hub versterken `[GOEDGEKEURD]`
**Bron:** Analytics Agent (#2) — Assen 0 scrollers; hub bestaat al
**Prioriteit:** Midden (SEO intern)
**Actie:**
- In `#drenthe-hub`: pas alleen de Assen-regel aan naar ankertekst `Vloerverwarming Assen en omgeving` (href blijft `vloerverwarming-assen.html`).
- Geen nieuwe links, geen extra CTA-knoppen, geen hero-wijziging.
**Succescriterium:** Interne ankertekst bevat "Assen" + omgeving; hub-structuur ongewijzigd.

### Taak 5: `scripts/data/google_ads_lead_campaign_defaults.json` — commit RSA final_urls `[GOEDGEKEURD]`
**Bron:** Marketing Research Agent — reeds lokaal gewijzigd (2 final URLs)
**Prioriteit:** Hoog (betaald, repo-sync)
**Actie:**
- Bevestig dat `final_urls` alleen offerte-deeplink + `prijsindicatie.html` bevat (marketing heeft dit al gedaan).
- Geen `--apply` naar Ads API; noteer in Developer Rapport dat live RSA in Ads UI handmatig gesynchroniseerd moet worden.
**Succescriterium:** JSON in repo; geen secrets; Developer Rapport vermeldt handmatige Ads UI-stap voor PO.

---

## Uitgestelde voorstellen `[WACHT]`

- **GA4 ↔ Google Ads koppeling + auto-tagging** — Admin/PO in GA4 UI; geen HTML-werk. Blokkeert eerlijke Paid Search-interpretatie.
- **GSC OAuth** (`secrets/gsc.env` + refresh token) — PO/browser; nodig voor sprint-13 SEO-meetdoelen.
- **Live RSA final URLs in Ads UI** — campagne `23834672782`; handmatig na defaults-commit.
- **Heerenveen-pagina of keyword pauzeren** — na GSC-fetch; max. 1 city-pagina/sprint na Assen.
- **Drenthe-hub + prijsindicatie-title effect** — sprint 13 live 6 dagen; juni-fetch ~22 juni.
- **projecten.html hero-tweak** — entry-sample te klein (2 sess).
- **Facebook message-match** — social kalender cyclus 14; geen developer-werk.
- **deviceCategory in ga4_fetch.py** — cyclus 15.

---

## Afgewezen voorstellen `[AFGEWEZEN]`

- **Nieuwe pagina `vloerverwarming-heerenveen.html`** — discipline 1 city/sprint; Assen eerst.
- **Budgetverhoging Ads >€2/dag** — Paid Search nog 0 conv.
- **Hero-CTA homepage wijzigen** — Drenthe-hub effect eerst meten.
- **`over-ons.html` ATF-CTA** — geen entry in top-15.
- **Standalone `vloerverwarming-drenthe.html`** — thin-content-risico.

---

## Social Media
**Status:** Weekplanning in `docs/website-manager/social/weekly_calendar.md` (week van 2 juni 2026)
**Actie vereist:** Handmatige publicatie door VLWarmte team — message-match per post (één intentie, één link)

---

## Context voor volgende sprint

- GSC beschikbaar? → prijsindicatie CTR, Hoogeveen-rang, Drenthe-hub op `/`.
- GA4↔Ads gekoppeld + RSA op offerte-deeplink? → Paid Search conv. >0?
- Assen na layout-fix: bounce/duur/scrollers?
- Prijsindicatie entry-bounce na ATF?
- Juni-fetch ~22 juni is ijkpunt voor sprint-13 + 14 meetdoelen.

---

## Developer Rapport — 2026-06-01

- **Geïmplementeerde taken:**
  1. **`vloerverwarming-assen.html` layout-fix** — `project-hero__readnext` verwijderd; vroege `cta-band` "Volgende stap" direct na hero verwijderd. Hero-image ongewijzigd (bestaand bestand 433 KB, al ≤500 KB). Slot-CTA onderaan pagina behouden.
  2. **`prijsindicatie.html` ATF message-match** — hero `.lead` vervangen door zin met "twee minuten" + richtbedrag; FAQ-verwijzing uit hero-lead gehaald.
  3. **`prijsindicatie.html` OG/Twitter meta** — `og:title`, `og:description`, `twitter:title`, `twitter:description` gelijkgetrokken met `<title>` en `<meta name="description">`.
  4. **`index.html` Drenthe-hub** — ankertekst Assen-link: `Vloerverwarming Assen en omgeving` (alleen in `#drenthe-hub`).
  5. **`google_ads_lead_campaign_defaults.json`** — bevestigd: `final_urls` bevat alleen offerte-deeplink + `prijsindicatie.html` (reeds lokaal gewijzigd door marketing; geen developer-wijziging nodig).

- **Overgeslagen taken:** geen (alle 5 `[GOEDGEKEURD]` taken afgerond).

- **Bestanden gewijzigd door Developer Agent:**
  - `vloerverwarming-assen.html`
  - `prijsindicatie.html`
  - `index.html`
  - `docs/website-manager/sprint.md` (dit rapport)

- **Smoke-tests:**
  - `bash tests/smoke/navigation-links.sh` — **PASS**
  - `bash tests/smoke/form-behavior.sh` — **PASS**
  - Lokaal `curl` op `127.0.0.1:8765`: `/vloerverwarming-assen.html`, `/prijsindicatie.html`, `/index.html` → HTTP 200, body start `<!doctype html>`.

- **Deployment:** **Nog niet live** — PM voert commit + `git push origin main` uit; daarna: *(PM vult run-id / succes in)*

- **Live URL:** https://www.vlwarmte.nl

- **Aandachtspunten voor volgende sprint:**
  - **Handmatige Ads UI-stap (PO):** live RSA in campagne `23834672782` final URLs synchroniseren met repo-defaults (offerte-deeplink + prijsindicatie) — geen `--apply` via API uitgevoerd.
  - **`google_ads_lead_campaign_defaults.json`** staat al gewijzigd in working tree; PM moet meenemen in commit indien nog niet gecommit.
  - Meetdoelen Assen bounce/duur en prijsindicatie entry-bounce pas beoordelen na juni-fetch (~22 juni).
