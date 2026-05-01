# Sprint — week van 5 mei 2026

**PM beslissing genomen op:** 01-05-2026 (Product Manager Agent — synthese `analytics_report.md` 1 mei, `research_report.md` Zuidlaren-sectie 1 mei, vorige sprint-status)  
**Doel deze sprint:** Hyperlokale vindbaarheid voor Zuidlaren-installateur-intentie vangen **en** de bestaande stadspagina’s bruikbaarder maken voor conversie — zonder de site te overspoelen met nieuwe URL’s.  
**Meetdoel:** Per **29 mei 2026** in GA4: zichtbare sessies op `/vloerverwarming-zuidlaren.html` (ook al klein); in Search Console (zodra token live): query’s met `zuidlaren` of `installateur` die de nieuwe URL raken. Geen harde drempel op conversies — volume blijft beperkt — wel bewijs dat de URL indexeert en landt.

---

## Goedgekeurde taken voor Developer Agent

### Taak 1: Locatiepagina `vloerverwarming-zuidlaren.html` `[GOEDGEKEURD]`

**Bron:** Analytics Agent (voorstel 1 mei) + Marketing Research (Zuidlaren-verdieping 1 mei)  
**Prioriteit:** Hoog  
**Type:** SEO (nieuwe pagina — **enige** nieuwe pagina deze sprint)

**Actie:** Nieuwe pagina, zelfde technische kapstok als `vloerverwarming-groningen.html` / `vloerverwarming-assen.html`:

- `<title>`: primair **Zuidlaren + vloerverwarming**; secundair installateur (bijv. "Vloerverwarming Zuidlaren — installateur VLWarmte | VLWarmte" — exacte bewoording in lijn met bestaande titels, geen schreeuwerige superlatieven).
- `<meta name="description">`: vloerverwarming, complete trajecten (ondervloer tot oplevering), schuimbeton waar passend, werkgebied Tynaarlo/Paterswolde/Bunne kort noemen, CTA prijsindicatie.
- `<link rel="canonical" href="https://www.vlwarmte.nl/vloerverwarming-zuidlaren.html">`
- H1: **Vloerverwarming Zuidlaren** (plaats centraal — dit was de gap t.o.v. Groningen/Assen-pagina’s).
- H2: **Installateur in Zuidlaren** (1 korte sectie: vestigingsadres, één aanspreekpunt, reistijd naar Groningen/Assen in één zin — sluit aan op query "installateur Zuidlaren").
- H2: **Vloerverwarming infrezen en renovatie** (2–3 alinea’s; long-tail t.o.v. concurrent Lemmers — nuchtere vaktaal).
- 300–500 woorden totaal, lokale plaatsnamen (Tynaarlo, Paterswolde, Bunne, Zuidwolde, evt. Gieten) waar natuurlijk.
- Schema.org `Service` met `areaServed` = **Zuidlaren** (City) en `provider` naar bestaande `LocalBusiness` op `index.html`.
- **CTA (conversie):** direct onder de hero/lead-regel een compact blok: telefoon + link `prijsindicatie.html` + link `contact.html?modus=offerte#aanvraag` (zelfde patroon als andere stadspagina’s maar **boven de vouw** zichtbaar zonder te scrollen op gangbare viewport).
- Google Search Console-placeholder in `<head>` (zelfde `REPLACE_WITH_TOKEN` + TODO als andere pagina’s).
- GA4-snippet mee.
- **Niet** in hoofdnav. **Wel:** footer Regio-blok op **alle** HTML-pagina’s in de repo-root uitbreiden met linktekst "Vloerverwarming Zuidlaren" (alfabetisch of logisch gegroepeerd naast Groningen/Assen).
- `sitemap.xml`: url-entry met actuele `lastmod`, `priority` 0,8.

**Succescriterium:** Pagina lokaal en live bereikbaar na deploy; Rich Results / schema zonder fouten; footer-link overal consistent; geen dubbele `index.html`/`/` issue op deze pagina.

---

### Taak 2: Sterker CTA-blok op bestaande stadspagina’s Groningen en Assen `[GOEDGEKEURD]`

**Bron:** Analytics Agent (bounce/sessieduur stadspagina’s 1 mei)  
**Prioriteit:** Hoog  
**Type:** conversie (geen nieuwe URL)

**Actie:** Op `vloerverwarming-groningen.html` en `vloerverwarming-assen.html` hetzelfde **compacte CTA-blok** als bij taak 1 onder de intro plaatsen (telefoon + prijsindicatie + offerte-contactdieplink), zodat een bezoeker zonder scroll een duidelijke volgende stap ziet. Geen herschrijven van de hele pagina — alleen structuur/duplicatie van CTA bovenin.

**Succescriterium:** Visueel op desktop en mobiel (browser devtools viewport) eerste CTA zichtbaar zonder scroll; geen broken links.

---

### Taak 3: Canonieke homepage en dubbele URL’s `[GOEDGEKEURD]`

**Bron:** Analytics Agent (`/` vs `/index.html`, 66 vs 12 sessies)

**Actie:**

- Zet op `index.html` een `<link rel="canonical" href="https://www.vlwarmte.nl/">` (root-URL, **niet** `/index.html`).
- Loop alle root-HTML door: waar de home-link nu naar `index.html` wijst, wijzig naar **`/`** (of naar `https://www.vlwarmte.nl/` alleen als dat al zo elders gebruikt wordt — kies **één** consistente relatieve stijl: bij voorkeur `/` voor home). Footer en header brand-link meenemen.
- Controleer dat lokale `file://` openen nog acceptabel is voor Hans; als `/` lokaal breekt, documenteer in één regel comment in `README` of in sprint-context hieronder — voorkeur blijft online gedrag.

**Succescriterium:** Geen gemixte home-href’s meer; canonical op `index.html` wijst naar root; na deploy geven `curl -I` op `/` en `/index.html` geen tegenstrijdige SEO-signalen die de developer kan verklaren (indien hosting beide 200 blijft geven: canonical is leidend).

---

### Taak 4: Interne links naar Zuidlaren-pagina `[GOEDGEKEURD]`

**Bron:** Marketing Research (aanbeveling 4 mei-sectie)

**Actie:**

- `index.html`: één natuurlijke zin in bestaande regio- of USP-blok met link naar `vloerverwarming-zuidlaren.html` (ankertekst bijv. "vloerverwarming in Zuidlaren" — niet keyword-stuffing).
- `over-ons.html`: waar het adres Zuidlaren genoemd wordt, een link naar de nieuwe pagina toevoegen.
- Optioneel, als het past zonder rommel: één link vanaf `diensten.html` waar regio/werkgebied aan bod komt.

**Succescriterium:** Minimaal twee inkomende interne links vanaf gezagdragende pagina’s; geen orphan URL.

---

### Taak 5: Wizard/prijs-CTA op `werkwijze.html` en `systemen-producten.html` `[GOEDGEKEURD]`

**Bron:** Marketing Research (uitgesteld "interne wizard-links", april-sprint) + PM (conversie-eis)

**Actie:** Op beide pagina’s één kort blok of zin **met knop/link** naar `prijsindicatie.html` (liefst met herkenbare tekst: "Prijsindicatie" / "indicatie aanvragen"), logisch geplaatst na het stuk waar de lezer over traject of systemen nadenkt. Geen volledige herstructuur van de pagina.

**Succescriterium:** Beide pagina’s hebben een werkende link naar de wizard; geen visuele breuk met bestaande typografie (hergebruik bestaande button/ link-classes).

---

## Uitgestelde voorstellen `[WACHT]`

- **`faq.html`** — Blijft eerste kandidaat **volgende** sprint. Nu niet: regel *max. 1 nieuwe pagina* is al benut door Zuidlaren.
- **Google Bedrijfsprofiel + reviews op homepage** — Handwerk door Hans; blokkeert geen dev-taken. Zodra profiel live is: nieuwe sprint-taak voor embed/sectie.
- **GA4 "lege" landingspagina (`landingPagePlusQueryString` leeg)** — Analyse in GA4-exploratie; geen code-change tot oorzaak bekend. Hans/PM: segment checken.
- **`logo-varianten.html` restverkeer** — Als URL niet meer bestaat: geen dev-prioriteit. Eventueel later 301 via hosting indien mogelijk.
- **Volledige interne link-uitrol wizard** op alle overige pagina’s — Deels opgelost met taak 5; `diensten.html` verder uitdiepen volgende sprint.
- **Projectfoto’s op stadspagina’s** — Wacht op materiaal van Hans (zie vorig sprint-rapport).

---

## Afgewezen voorstellen `[AFGEWEZEN]`

- **Tweede nieuwe pagina naast Zuidlaren in dezelfde sprint** (bijv. FAQ + Zuidlaren tegelijk) — breekt de PM-regel kwaliteit/volume; FAQ schuift door.

---

## Social Media

**Status:** Weekplanning staat in `docs/website-manager/social/weekly_calendar.md`  
**Actie vereist:** Handmatige publicatie door VLWarmte team. **Suggestie deze week:** één post of story met link naar `vloerverwarming-zuidlaren.html` zodra live — ondersteunt indexering en lokale signalen.

---

## Context voor volgende sprint

- Eerste check GSC-query’s op "zuidlaren" **2–4 weken** na live + token.
- GA4-fetch eind mei blijft het moment voor funnel-beslissingen (zie eerder sprint-akkoord rond 24–29 mei).
- **Volgende dev-prioriteit na deze sprint:** `faq.html`, daarna schuimbeton-anker en resterende interne wizard-links.

---

## Referentie vorige sprint (27 april 2026)

Volledige goedgekeurde taken en developer rapport staan gearchiveerd onder `docs/website-manager/archive/sprint-2026-04-27.md` en in git history.

**Open punten Hans (blijven gelden):** Search Console-token vervangen, sitemap indienen, conversies markeren in GA4, mobiele handtest wizard/contact, GBP activeren.

---

## Developer Rapport — 1 mei 2026

**Taak 1 — `vloerverwarming-zuidlaren.html`:** klaar. Nieuwe landingspagina met H1 Zuidlaren, H2 installateur en infrezen/renovatie, schema `Service` + `areaServed` Zuidlaren, hero-CTA (prijsindicatie + bel + offerte-dieplink), GA4-snippet, Search Console-placeholder, footer Regio op alle root-HTML-pagina’s uitgebreid met link naar Zuidlaren, `sitemap.xml` bijgewerkt.

**Taak 2 — CTA Groningen/Assen:** klaar. Hero-blokken gebruiken `hero-cta-row` met drie acties (Prijsindicatie, bellen, offerte).

**Taak 3 — Canonieke home:** klaar. Alle `href="index.html"` voor logo en Home-nav vervangen door `href="/"`. `index.html` had al `<link rel="canonical" href="https://www.vlwarmte.nl/">`. Toelichting `file://` vs. `/` in `README.md`.

**Taak 4 — Interne links:** klaar. `index.html` (hero-lead), `over-ons.html` (bezoekadres), `diensten.html` (korte sectie) wijzen naar Zuidlaren-pagina.

**Taak 5 — Wizard-CTA:** klaar. `werkwijze.html` en `systemen-producten.html` hebben elk een `cta-band` naar `prijsindicatie.html`.

**Tests:** `bash tests/smoke/navigation-links.sh` en `form-behavior.sh` PASS. Lokaal: `curl` naar `/` en `/vloerverwarming-zuidlaren.html` op `python3 -m http.server` → 200, HTML `<!doctype`.
