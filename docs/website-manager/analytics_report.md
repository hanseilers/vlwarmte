# Analytics Rapport — 1 juli 2026 (cyclus 20)

**Periode:** 30 dagen (2 jun – 1 jul 2026), GA4 property `properties/534641753`, gegenereerd 2026-07-01
**Vorige sprint effect:** Cyclus 19 (live 29 jun) versterkte de wizard-leadstap op `prijsindicatie.html`, consolideerde de home-`<title>`, legde interne ankerlinks naar 8 stadspagina's en fixte de mobiele sticky-CTA naar de wizard. **Te vroeg om hard te meten** — slechts 2–3 dagen in deze 30d-export. Wel zichtbaar: `vloerverwarming-drachten.html` en `vloerverwarming-zuidlaren.html` halen elk 2 sessies met 0% bounce; de nieuwe home-titel ("Vloerverwarming in Drenthe, Groningen en Friesland — VLWarmte") staat nog maar op **1 sessie** (100% bounce, 0 s — ruis). Oudere title-varianten domineren nog in het 30d-venster. `prijsindicatie.html` blijft de sterkste pagina (307 s, 25% bounce) maar levert **nog steeds 0 conversies** (ook 0 over 90d / 68 sessies). Verkeer licht gedaald (38 vs 42 sessies vorige cyclus) — binnen ruis bij dit volume.

> **GSC ontbreekt opnieuw.** `gsc_report.json` dateert nog van 23 mei 2026. De SEO-ingrepen van cyclus 17–19 (interne links, CTR-fix Zuidlaren, home-titel) zijn in Search Console **niet te toetsen** tot OAuth werkt.

---

## Kerncijfers

| Metric                    | Waarde (30d) | Trend                                              |
| ------------------------- | ------------ | -------------------------------------------------- |
| Sessies                   | 38           | ↓ ~10% (was 42 cyclus 19) — ruis bij klein n     |
| Actieve gebruikers        | ~34*         | ↓ licht                                            |
| Conversies                | 2            | gelijk (was 2)                                     |
| Conversies uit cpc        | 2 van 2      | **100%** uit Google Ads (`google / cpc`, 19 sess.) |
| Conversies uit organisch  | 0            | organisch: 6 sessies, 0 conv.                      |
| Conversies uit direct     | 0            | direct: 12 sessies, 0 conv.                        |
| Mobiel / desktop / tablet | 20 / 16 / 2  | mobiel 53% — vergelijkbaar met vorige cyclus       |

\*GA4 rapporteert gebruikers per kanaal met overlap; ~34 is een schatting op basis van kanaaldata.

### Weektrend (sessies per week)

| Week       | Sessies | Gebruikers |
| ---------- | ------- | ---------- |
| 6–12 mei   | 92      | 69         |
| 13–19 mei  | 47      | 43         |
| 20–26 mei  | 42      | 36         |
| 27 mei–2 jun | 14    | 13         |
| 3–9 jun    | 20      | 19         |
| 10–16 jun  | 7       | 6          |
| 17–23 jun  | 3       | 3          |
| 24–30 jun  | **4**   | 4          |

Het dieptepunt (3 sessies/week half juni) blijft zichtbaar. De laatste volle week telt 4 sessies — minimaal beter dan 3, maar ver onder het niveau van mei (~42–92/week). De lichte opleving valt samen met terugkerend betaald verkeer (cpc 19 sessies / 2 conv.).

---

## Top pagina's (30d)

| Pagina / pad                     | Sessies | Gem. duur | Bounce  | Opmerking                                      |
| -------------------------------- | ------- | --------- | ------- | ---------------------------------------------- |
| `/` (alle title-varianten)       | 30      | wisselend | 14–100% | nog 6 verschillende `<title>`'s in 30d         |
| `/prijsindicatie.html`           | 8       | **307 s** | **25%** | sterkste engagement, 0 conversies              |
| `/contact.html`                  | 5       | 141 s     | 0%      | goede betrokkenheid                            |
| `/diensten.html`                 | 3       | 17 s      | 33%     | korte sessies                                  |
| `/systemen-producten.html`       | 3       | 18 s      | 67%     | zwak als landing                               |
| `/vloerverwarming-drachten.html` | 2       | 107 s     | 0%      | eerste verkeer na interne links                |
| `/vloerverwarming-zuidlaren.html`| 2       | 39 s      | 0%      | 2× als landing, 0% bounce                      |
| `/over-ons.html`                 | 2       | 16 s      | 0%      | korte duur                                     |
| `/faq.html`                      | 1       | 92 s      | 0%      | te weinig volume                               |
| `/werkwijze.html`                | 1       | 13 s      | 0%      | te weinig volume                               |

**Homepage-title-fragmentatie blijft zichtbaar** in het 30d-venster (historische data + cache):

| Title op `/`                                              | Sessies | Duur  | Bounce |
| --------------------------------------------------------- | ------- | ----- | ------ |
| "VLWarmte \| Vloerverwarming van ondervloer tot oplevering" | 15    | 166 s | 53%    |
| "Vloerverwarming Zuidlaren & Noord-NL — installateur"     | 7     | 45 s  | 14%    |
| "Vloerverwarming Drenthe & Noord-NL — richtbedrag in 2 min" | 5   | 7 s   | **80%** |
| "Vloerverwarming in Drenthe, Groningen en Friesland — VLWarmte" (nieuw) | 1 | 0 s | 100% |

De geconsolideerde titel (live sinds 29 jun) moet de komende weken domineren; de "richtbedrag in 2 min"-variant (80% bounce, 7 s) is precies waarom die uit de home-title is gehaald.

---

## Zwakste pagina's (hoge bounce / lage betrokkenheid)

| Pagina                       | Sessies | Gem. duur | Bounce | Signaal                                        |
| ---------------------------- | ------- | --------- | ------ | ---------------------------------------------- |
| `/` (richtbedrag-title)      | 5       | 7 s       | 80%    | oude title-variant; verdwijnt uit venster    |
| `/systemen-producten.html`   | 3       | 18 s      | 67%    | 3× landing, geen conversie                     |
| `/prijsindicatie.html` (als landing) | 3 | —     | 67%    | directe instap presteert slechter dan site-bezoek |
| `/diensten.html` (als landing) | 2     | —         | 50%    | hero-CTA naar wizard, cta-band primair contact |

**90d-context:** `prijsindicatie.html` — 68 sessies, 130 s gem. duur, **0 conversies**. `projecten.html` — 18 sessies, 14 s (bewust dun). `vloerverwarming-assen.html` — 7 sessies 90d, 0,7 s gem. duur (bot/crawl-verdacht).

---

## Traffic bronnen

| Kanaal          | Bron / medium        | Sessies | Gebruikers | Conversies |
| --------------- | -------------------- | ------- | ---------- | ---------- |
| Cross-network   | google / cpc         | 19      | 17         | **2**      |
| Direct          | (direct) / (none)    | 12      | 12         | 0          |
| Organic Search  | google / organic     | 6       | 6          | 0          |
| AI Assistant    | chatgpt.com          | 1       | 1          | 0          |

**Betaald blijft de enige conversiebron** (~10,5% conversieratio op cpc — gezond, maar veel te weinig volume). Organisch groeit niet meetbaar (6 sessies, stabiel t.o.v. cyclus 19). Direct (12 sessies) levert geen conversies — herkenning zonder omzetting.

### Landingspagina's

| Landing                        | Sessies | Bounce | Conv. |
| ------------------------------ | ------- | ------ | ----- |
| `/`                            | 26      | 54%    | 2     |
| `/prijsindicatie.html`         | 3       | 67%    | 0     |
| `/systemen-producten.html`     | 3       | 67%    | 0     |
| `/diensten.html`               | 2       | 50%    | 0     |
| `/vloerverwarming-zuidlaren.html` | 2    | 0%     | 0     |

Beide conversies komen binnen via homepage-landing (`/`). De wizard krijgt weinig directe instap (3 landings) en converteert niet.

### Geografie

| Regio              | Sessies | In doelgebied? |
| ------------------ | ------- | -------------- |
| Drenthe            | 8       | ja             |
| Friesland          | 6       | ja             |
| Groningen          | 3       | ja             |
| NL (not set)       | 6       | onduidelijk    |
| Noord-Holland      | 4       | **nee**        |
| Zuid-Holland       | 3       | **nee**        |
| Ned.-Saksen (DE)   | 2       | **nee**        |
| Bangladesh, Canada | 1+1     | **nee**        |

Kernregio (DR+FR+GR) = 17 van 38 sessies (~45%). Randstad en buitenland wijzen op **brede NL-targeting in Ads** of botverkeer.

---

## Observaties

1. **Het knelpunt is instroom, niet conversiekwaliteit op cpc.** Met 19 betaalde sessies en 2 conversies (~10,5%) presteert Ads gezond — maar het absolute aantal leads (2/30d) is te laag om de business te dragen. Direct en organisch leveren samen 18 sessies zonder enige conversie.

2. **Cyclus-19-ingrepen zijn te vers om te beoordelen, maar de wizard blijft het grootste interne lek.** De leadstap is visueel versterkt (live 29 jun), maar over 90 dagen en 68 sessies op `prijsindicatie.html` staat de teller nog op 0 `wizard_lead_submit`. Over 4 weken opnieuw meten; als dan nog 0: wizard-stap-events uitlezen (`wizard_start` → `calculator_result` → `wizard_lead_submit`).

3. **Homepage-title-consolidatie moet nog doorwerken.** GA4 toont nog 6 title-varianten op `/` in 30d; de nieuwe definitieve titel heeft 1 sessie. Verwacht dat het beeld over 2–4 weken schoner wordt — controleer of er geen oude variant via cache, bookmark of externe link terugkomt.

4. **Stadspagina's krijgen eerste verkeer.** Drachten (2 sessies, 107 s, 0% bounce) en Zuidlaren (2× landing, 0% bounce) zijn vroege signalen dat interne links werken — maar bij n=2 is dit geen trend. GSC blijft nodig om indexatie en posities te bevestigen.

5. **`systemen-producten.html` en `diensten.html` presteren zwak als landing** (67% en 50% bounce). Als Ads-verkeer hierop landt, is dat een mismatch; de pagina's hebben wel CTAs naar de wizard, maar de hero en copy overtuigen niet binnen 17–18 seconden.

---

## Aanbevelingen voor Marketing Research Agent (betaald verkeer)

- **Campagne `23834672782` — volume:** 100% van conversies uit cpc bij ~€2/dag. Read-only check: `python scripts/google_ads_list_campaigns.py`. Budgetverhoging alleen na expliciete spend-goedkeuring.
- **Geo-lek dichten:** Noord-/Zuid-Holland, Duitsland, Bangladesh en Canada in GA4 terwijl doelregio DR/GR/FR is → `python scripts/google_ads_update_campaign_geo.py --campaign-id 23834672782 --dry-run` dan `--apply`.
- **Landingsafstemming:** beide conversies komen via `/`, niet via `prijsindicatie.html`. Overweeg aparte Ads-landings of sitelinks die direct naar de wizard sturen — de wizard heeft sterke engagement (307 s) maar 67% bounce als directe landing.
- **Keyword-gap `vloerverwarming heerenveen`:** nog geen dedicated pagina (alleen Drachten noemt Heerenveen) — pauseer keyword of bouw pagina.

---

## Voorstellen voor Product Manager

### 1. Wizard-conversie opnieuw meten over 4 weken — daarna funnel-events uitlezen

- **Prioriteit:** Hoog
- **Onderbouwing:** 68 sessies / 90d op `prijsindicatie.html`, 307 s gem. duur, 25% bounce — maar **0 conversies**. Cyclus 19 versterkte `.lead-after` (29 jun); te vroeg voor effect.
- **Actie:** Geen nieuwe wizard-ingreep deze cyclus. Plan in sprint week 27 jul een GA4-check op `wizard_lead_submit` en `wizard_start`. Bij nog 0: ad-hoc funnel-query (`wizard_start` → `calculator_result` → `wizard_lead_submit`) om het exacte lek te vinden.
- **Verwacht effect:** Gerichte fix i.p.v. gissen; eerste wizard-conversie binnen 4–8 weken na cyclus 19.

### 2. Google Ads volume + geo — escalatie naar eigenaar

- **Prioriteit:** Hoog
- **Onderbouwing:** 19 cpc-sessies / 2 conv. (100% van leads). Geo toont 7 sessies buiten kernregio (NH, ZH, DE, BD, CA).
- **Actie:** Eigenaar: campagne-status bevestigen, budget beoordelen, geo-targeting aanscherpen (zie commando's hierboven). Niet autonoom zonder spend-goedkeuring.
- **Verwacht effect:** Meer leads bij gelijke conversieratio; schoner geo-profiel.

### 3. GSC-fetch deblokkeren

- **Prioriteit:** Hoog
- **Onderbouwing:** GSC-data 5+ weken oud. Interne links, CTR-fix Zuidlaren en home-titel van cyclus 17–19 zijn niet meetbaar in Search Console.
- **Actie:** OAuth-refresh-token aanleveren (`secrets/gsc.env`, `scripts/gsc_get_refresh_token.py`). Daarna `scripts/gsc_fetch.py` in elke cyclus.
- **Verwacht effect:** Eerste harde data over indexatie stadspagina's en CTR op "installateur zuidlaren"-termen.

### 4. Homepage-title: monitor of oude varianten terugkomen

- **Prioriteit:** Midden
- **Onderbouwing:** Nog 6 title-varianten in 30d; "richtbedrag in 2 min" (5 sessies, 80% bounce) is verwijderd maar nog zichtbaar in het venster. Nieuwe titel: 1 sessie.
- **Actie:** Over 2–4 weken in GA4 controleren of pad `/` nog maar één `pageTitle` toont. Zo niet: zoeken naar externe links, oude social posts of CDN-cache die oude snippets serveren.
- **Verwacht effect:** Eén rankingsignaal; lagere bounce op home-landings.

### 5. `systemen-producten.html` — landingervaring verbeteren

- **Prioriteit:** Midden
- **Onderbouwing:** 3 landings, 67% bounce, 18 s gem. duur. Pagina heeft CTAs naar wizard maar overtuigt niet snel genoeg.
- **Actie:** Hero scherper maken (concrete belofte + plaatsnaam + primaire CTA "Richtbedrag in 2 minuten"); korte trust-regel (10 jaar garantie buis, reactie één werkdag). Geen tweede formulier.
- **Verwacht effect:** Lagere bounce bij Ads-organische landings op laagopbouw-termen.

### 6. `diensten.html` — primaire CTA naar wizard i.p.v. contact

- **Prioriteit:** Midden
- **Onderbouwing:** 3 sessies, 17 s duur; hero wijst naar wizard maar onderste `cta-band` heeft "Offerte aanvragen" als primair naar `contact.html` — inconsistent met wizard-first strategie.
- **Actie:** In `cta-band`: primaire knop naar `prijsindicatie.html` ("Richtbedrag in 2 minuten"), secundair naar contact. Hero blijft zoals hij is.
- **Verwacht effect:** Meer doorklik naar wizard; lagere bounce op diensten-landings.

### 7. Stadspagina's — eerste verkeer versterken via social

- **Prioriteit:** Midden
- **Onderbouwing:** Drachten en Zuidlaren elk 2 sessies met goede engagement na interne-link-sprint. Overige stadspagina's (Assen, Emmen, Groningen, Hoogeveen, Leeuwarden, Drenthe-hub) nog 0 sessies in 30d.
- **Actie:** Social posts deze week expliciet linken naar 1–2 stadspagina's (niet alleen home/wizard). Past bij `weekly_calendar.md`.
- **Verwacht effect:** Eerste meetbare sessies op hub + zusterpagina's; GSC-posities volgen later.

### 8. `projecten.html` — wachten op beeldmateriaal

- **Prioriteit:** Laag
- **Onderbouwing:** 18 sessies / 90d maar 14 s gem. duur — pagina overtuigt niet. Geblokkeerd op foto's (afgewezen cyclus 19).
- **Actie:** Geen dev-werk tot eigenaar projectfoto's levert in `beeldmateriaal/projecten/`. Dan cases met plaatsnaam.
- **Verwacht effect:** Langere sessies, meer vertrouwen — vooral voor direct-verkeer.

### 9. Organisch — FAQ en stadspagina's laten rijpen

- **Prioriteit:** Laag
- **Onderbouwing:** 6 organische sessies, 0 conversies. FAQ (1 sessie / 30d) en stadspagina's zijn gebouwd maar hebben tijd nodig.
- **Actie:** Geen nieuwe pagina's bouwen zonder GSC-signaal. Eerst GSC ontblokken (voorstel 3), dan beslissen over Heerenveen-pagina of laagopbouw-H2.
- **Verwacht effect:** Organische instroom na indexatie; conversie volgt via wizard-routing.

### 10. GA4-rapportage: segment NL-doelregio

- **Prioriteit:** Laag
- **Onderbouwing:** 21% sessies buiten DR/GR/FR (NH, ZH, buitenland) vervuilt lokaal beslissingsbeeld bij klein n.
- **Actie:** In toekomstige `ga4_fetch.py`-runs optioneel een NL-doelregio-filter toevoegen (DR+GR+FR+Overijssel) naast totaalrapport.
- **Verwacht effect:** Schonere cyclus-tot-cyclus vergelijking voor PM.

---

*Fetch: geslaagd — `docs/website-manager/ga4_report.json` (2026-07-01T21:23). Credentials: `secrets/vlwarmte-ga-service-account.json`.*
