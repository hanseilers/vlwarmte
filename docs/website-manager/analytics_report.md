# Analytics Rapport — 15 mei 2026

**Periode:** `30daysAgo` t/m `today` (GA4 property `properties/534641753`)  
**Vorige sprint effect:** Sprint cyclus 8 (live ca. 13-05-2026) leverde o.a. `project-hero` op `vloerverwarming-assen.html` en `vloerverwarming-groningen.html`, keuzehulp op `diensten.html`, lander-copy + offerte-knop op `systemen-producten.html`, en nieuwe `vloerverwarming-emmen.html`. Deze export overlapt de live-datum: effect op stadspagina’s en diensten is **nog beperkt zichtbaar** in 30d-aggregaten; 90d-scroll op Assen blijft **0** — eerst post-deploy meten, daarna bijsturen.

**Data-fetch:** `.venv/bin/python scripts/ga4_fetch.py` — `docs/website-manager/ga4_report.json`, timestamp **`2026-05-15T12:48:01`**.

## Kerncijfers

| Metric | Waarde | Trend / context |
| ------ | ------ | ---------------- |
| Sessies (laatste volledige week in export) | **100** (week 8–14 mei) | week ervoor 1–7 mei: **54** → **+85%** week-op-week (herstel na lage week) |
| Homepage `/` (30d pad) | **153** sessies, bounce **58,2%** | licht meer verkeer dan vorig rapport (141); engagement scroll 90d: **25** scrolled users op 153 sessies |
| Paid Search (`google / cpc`) | **13** sessies, **0** conversies | ongewijzigd patroon |
| Cross-network (`google / cpc`) | **20** sessies, **0** conversies | iets hoger volume dan vorige export (+8) |
| Unassigned `(not set)` | **2** sessies, **1** conversie | blijft laag — attributie relatief stabiel |

> GA4 telt sessies per dimensie; sommen over tabellen zijn indicatief. Trendrichting gaat voor.

## Top pagina's (30d, pagePath)

| Pagina | Sessies | Gem. sessieduur | Bounce |
| ------ | ------- | ---------------- | ------ |
| `/` | 153 | ~65 s | 58,2% |
| `/prijsindicatie.html` | 46 | ~84 s | **32,6%** |
| `/contact.html` (beide titels samen) | 51 | ~59 s | mix — zie landings |
| `/diensten.html` | 21 | ~81 s | **52,4%** |
| `/over-ons.html` | 18 | ~32 s | 38,9% |
| `/werkwijze.html` | 20 | ~63 s | 40% |
| `/systemen-producten.html` | 17* | wisselend† | wisselend† |
| `/projecten.html` | 8 | ~7,5 s | **75%** |
| `/vloerverwarming-groningen.html` | 8 | ~51 s | **75%** |
| `/vloerverwarming-assen.html` | 7 | **~0,7 s** | **85,7%** |

\* Twee titelvarianten in GA4: korte sessies op hoofd-URL (13 sessies, ~7 s gem.) versus diepe vergelijk-sessies op oudere titel (4 sessies, langere duur, 0% bounce).  
† Geaggregeerd in export als aparte rijen; interpretatie: **landingprobleem vs. diep onderzoek** naast elkaar.

## Zwakste signalen (landings + engagement)

| Landing / pad | Sessies | Bounce | Opmerking |
| --------------- | ------- | ------ | --------- |
| `/contact.html?modus=offerte` | 11 | **9,1%** | **10 conversies** — deeplink blijft de goudstandaard |
| `/contact.html` (zonder query) | 10 | **80%** | koud landen zonder intentie-keuze blijft zwaar |
| `/diensten.html` | 14 | **78,6%** | als landing: keuzehulp staat kort live — volgende export bepalen of bounce daalt |
| `/systemen-producten.html` | 8 | **75%** | als landing: nog steeds hoog na hero-aanpassing |
| `/projecten.html` | 6 | **100%** (entry) | hero cyclus 7/8 nog geen doorbraak op entry-bounce |
| `/vloerverwarming-assen.html` | 6 | **100%** | **0 scrolled users (90d)** — eerste scherm nog geen scroll-traction |
| `/disclaimer.html` / `/privacy.html` | 7 + 6 | 100%, 0 s | `noindex` live — historische landings; blijven monitoren |
| `/logo-varianten.html` | 7 | **85,7%** | stub/redirect-verkeer blijft binnenkomen — SEO-technische check nuttig |

## Traffic bronnen (selectie)

| Kanaal | Source / medium | Sessies | Conversies |
| ------ | ----------------- | ------- | ---------- |
| Direct | `(direct) / (none)` | 212 | 87 |
| Cross-network | `google / cpc` | 20 | 0 |
| Paid Search | `google / cpc` | 13 | 0 |
| Organic Social | Facebook-varianten | ~28 | 0 |
| Organic Search | `google / organic` | 5 | 1 |
| Unassigned | `(not set)` | 2 | 1 |

## Geografie (top)

| Regio | Sessies | Doelregio? |
| ----- | ------- | ---------- |
| NL — Drenthe | 161 | Ja, kern |
| NL — Groningen | 16 | Ja — groei t.o.v. vorige export (11) |
| NL — North Holland | 23 | Buiten kern |
| NL — Friesland | 4 | Ja — ondervertegenwoordigd |
| VS (diverse) | ~28 totaal | waarschijnlijk ruis |

## Observaties

1. **Weekvolume herstelt duidelijk** (100 vs 54 vorige week) — goed teken na dip; volhouden met meetplan.
2. **Paid + cross-network samen 33 sessies, 0 conversies** — conversiekoppeling en message-match blijven P0 voor Marketing Research (Ads + GA4).
3. **`contact.html?modus=offerte` blijft extreem sterk** — alle betaalde en social routes met offerte-intentie deze URL laten gebruiken.
4. **`vloerverwarming-assen.html`:** bounce iets lager dan 100%, maar **gemiddelde duur ~0,7 s** en **0 scrollers (90d)** — viewport/vertrouwen nog niet “sticky” genoeg; meet na volle 14 dagen post-live.
5. **`diensten.html` als landing** blijft op **78,6%** bounce — effect keuzehulp pas volgende cyclus hard beoordelen.
6. **`systemen-producten.html`:** mix van “snelle exit” en “diep vergelijken” — landingsegment verder helpen met duidelijke **volgende stap** boven de vouw.

## Aanbevelingen voor Marketing Research Agent

- **Google Ads:** herbevestig campagne-status, zoektermen, final URL’s en **conversie-import** (GA4 → Ads) — 0 conversies op betaald blijft het kernprobleem.
- **GA4 ↔ Ads:** auto-tagging, conversie-acties (`wizard_lead_submit`, `lead_form_submit`, `contact_submit`) en landings-URL’s nalopen tegen `.cursor/skills/google-ads-marketing/SKILL.md`.
- **Content:** crawlbare kosten-uitleg op `prijsindicatie.html` en volgende city-gap (**Hoogeveen** na Emmen) blijven hoog renderen in SEO-wachtrij.

## Voorstellen voor Product Manager

1. **Prioriteit: Hoog (SEO)** — **Onderbouwing:** city-cluster na Emmen; Friesland/Drenthe-corridor. **Actie:** `vloerverwarming-hoogeveen.html` (max. 1 nieuwe pagina), gelijkwaardig aan Emmen/Assen, sitemap + footer + kruislinks. **Verwacht:** eerste organische sessies binnen 4–8 weken.

2. **Prioriteit: Hoog (CTA)** — **Onderbouwing:** `projecten.html` entry **100%** bounce (6 sessies), 90d **1** scrolled user op 8 pagina-sessies. **Actie:** eerste scherm compacter + **duidelijke primaire duo-CTA** (prijsindicatie + offerte-deeplink) vóór zware galerij. **Verwacht:** landingsbounce <85%, meer scroll.

3. **Prioriteit: Hoog (SEO)** — **Onderbouwing:** `prijsindicatie.html` sterk als sessie-pagina, maar **als landing** bounce **64,7%** op 17 sessies — zoekers met “kosten”-intent missen crawlbare uitleg boven wizard. **Actie:** 200–400 woorden statische uitleg (drivers: m², ondergrond, schuimbeton), interne links naar FAQ/contact. **Verwacht:** betere SEO-match + lagere landingbounce.

4. **Prioriteit: Midden (CTA)** — **Onderbouwing:** `/contact.html` zonder query: **80%** bounce als landing. **Actie:** boven het modus-blok een korte **intentie-keuze** (info / offerte / bel) met links naar dezelfde tabs — geen dubbele formulieren. **Verwacht:** lagere bounce op cold contact-landings.

5. **Prioriteit: Midden** — **Onderbouwing:** Assen **0 scrollers (90d)** ondanks nieuwe hero. **Actie:** visuele **“lees verder”**/anchor naar eerste contentblok of compact trust-bandje direct onder hero-afbeelding (geen extra zware LCP). **Verwacht:** >0 scrollers binnen 30d.

6. **Prioriteit: Laag** — **Onderbouwing:** `logo-varianten.html` blijft verkeer trekken. **Actie:** Search Console + server redirect controleren; geen nieuwe features tenzij indexatie aanhoudt.

**Tone:** nuchter, direct, geen superlatieven — conform AGENTS.md.
