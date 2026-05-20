# Analytics Rapport — 20 mei 2026

**Periode:** `30daysAgo` t/m `today` (GA4 property `properties/534641753`)
**Databron:** `docs/website-manager/ga4_report.json`, timestamp **`2026-05-20T13:06:34`**
**Vorige sprint:** cyclus 10 live sinds **18-05-2026** (commit `de6596b`); vorige fetch **18-05** was nog vóór/op rand van deploy. Deze fetch is de **eerste meting met cyclus 10 in het venster** (~2 dagen post-deploy) én bevat ~17 dagen cyclus-9-data.

**Vorige sprint effect (cyclus 10):** Te vroeg voor harde conclusies op de vijf meetdoelen. Drachten-pagina staat nog **niet** in GA4-tabellen (0 sessies). Offerte-deeplink, over-ons vervolg-CTA, projecten ATF-duo-CTA en interne links zijn live — bounce/scroll op projecten, over-ons entry en cold contact zijn **ongewijzigd** t.o.v. 18-05. Wel: Cross-network `google / cpc` groeit licht in conversies (5→9); Paid Search blijft **0/13**.

---

## Kerncijfers

| Metric | Waarde | Trend t.o.v. fetch 18-05 |
| ------ | ------ | ------------------------ |
| Sessies (30d, som devices) | **~322** | devices 172+139+11; homepage-pad `/` **182** (+11%) |
| Laatste volledige week (13–19 mei) | **44** sessies, **40** users | week ervoor (6–12 mei) **92** → **−52%** wow; piekweek 29/4–5/5 **170** |
| Homepage `/` (30d pad) | **182** sessies, bounce **59,9%** | was 164 / 57,3% — iets meer verkeer, bounce licht omhoog |
| `/prijsindicatie.html` (30d pad) | **51** sessies, bounce **29,4%** | was 50 / 30% — stabiel sterk; gem. duur **~101 s** |
| Direct | **219** sessies, **90** conversies | was 215 / 89 |
| Betaald totaal (`google / cpc`) | **55** sessies (42+13), **9** conv. | Cross-network **42** / **9** (was 29/5); Paid Search **13** / **0** (ongewijzigd) |
| Organic Search `google` | **8** sessies, **1** conv. | was 7 / 1 |

> GA4 telt sessies per dimensie; sommen zijn indicatief. Bij dalend weekvolume zijn landing-cijfers (6–17 sessies) ruis, geen sprint-falen.

---

## Top pagina's (30d, pagePath)

| Pagina | Sessies | Gem. sessieduur | Bounce |
| ------ | ------- | ---------------- | ------ |
| `/` | 182 | ~58 s | 59,9% |
| `/prijsindicatie.html` | 51 | **~101 s** | **29,4%** |
| `/contact.html` (beide titels) | 52 | ~58 s | mix — zie landings |
| `/diensten.html` | 25 | ~73 s | 52,4% (regio-titel 25%) |
| `/over-ons.html` | 21 | ~29 s | 38,9% |
| `/werkwijze.html` | 20 | ~63 s | 40% |
| `/systemen-producten.html` | 17 | mix | 46,2% |
| `/projecten.html` | 8 | **~7,5 s** | **75%** |
| `/vloerverwarming-groningen.html` | 8 | ~51 s | **75%** |
| `/vloerverwarming-assen.html` | 7 | **~0,7 s** | **85,7%** |

**Niet in top:** `vloerverwarming-drachten.html`, `vloerverwarming-hoogeveen.html`, `vloerverwarming-leeuwarden.html` — nog geen meetbaar verkeer in deze export.

---

## Landingspagina's (instappunten)

| Landing | Sessies | Bounce | Conv. | Opmerking |
| ------- | ------- | ------ | ----- | --------- |
| `/` | 155 | 62,6% | 47 | hoofdinstroom |
| `/prijsindicatie.html` | 17 | **64,7%** | **24** | entry-bounce ongewijzigd; conversiewaarde hoog |
| `/contact.html?modus=offerte` | 11 | **9,1%** | **10** | goudstandaard deeplink |
| `/contact.html` (zonder query) | 10 | **80%** | 12 | cold contact — intent-strip nog geen zichtbaar effect |
| `/diensten.html` | 14 | **78,6%** | 0 | zwakste commerciële landing |
| `/over-ons.html` | 10 | **80%** | 0 | entry ongewijzigd; onderaan-CTA helpt entry niet |
| `/projecten.html` | 6 | **100%** | 0 | ATF cyclus 10 nog **geen** effect (2d) |
| `/werkwijze.html` | 9 | 66,7% | 7 | redelijk |
| `/systemen-producten.html` | 8 | 75% | 0 | |
| `/vloerverwarming-assen.html` | 6 | **100%** | 0 | **0 scrollers (90d)** |

---

## Traffic bronnen (selectie)

| Kanaal | Source / medium | Sessies | Conversies |
| ------ | ----------------- | ------- | ---------- |
| Direct | `(direct) / (none)` | 219 | 90 |
| Cross-network | `google / cpc` | 42 | **9** |
| Organic Social | `m.facebook.com / referral` | 13 | 0 |
| Paid Search | `google / cpc` | 13 | **0** |
| Organic Social | `facebook.com / referral` | 12 | 0 |
| Organic Search | `google / organic` | 8 | 1 |
| Organic Search | `bing / organic` | 4 | 0 |

---

## Geografie (top)

| Regio | Sessies | Doelregio? |
| ----- | ------- | ---------- |
| NL — Drenthe | 168 | Ja, kern (+4 t.o.v. 18-05) |
| NL — North Holland | 34 | Buiten kern (+5) |
| NL — Groningen | 18 | Ja (+2) |
| NL — South Holland | 16 | Buiten kern (+2) |
| NL — Friesland | 4 | Ja — **sterk ondervertegenwoordigd** (ongewijzigd) |
| VS (Oregon/Colorado/NC/Iowa) | ~32 | Ruis/bots |

---

## Cyclus-10 meetdoelen — eerste post-deploy stand (~2 dagen)

| Meetdoel | Doel (4 wk) | Stand 20-05 | Oordeel |
| -------- | ----------- | ----------- | ------- |
| (a) Sessies `vloerverwarming-drachten.html` | >0 (org.) | **0** in export | Te vroeg — indexering + Ads-defaults pas live 18-05 |
| (b) Cold `/contact.html` + doorstroom offerte | lagere bounce | **80%** entry (10 ses) | Geen effect zichtbaar |
| (c) `over-ons.html` entry | <80% bounce, >0 conv | **80%**, **0** conv | Geen effect; vervolg-CTA staat onderaan |
| (d) `projecten.html` entry | <90% bounce, >0 scrollers | **100%** entry (6), **1** scroller 90d | Geen effect |
| (e) Ads-defaults zonder pagina | 0 mismatches | **voldaan in repo** | Drachten-URL in defaults; **meting** pas na `--apply`/live Ads |

### Cyclus-9 meetdoelen (nog in venster, ~17 dagen data)

| Meetdoel | Stand 20-05 | Oordeel |
| -------- | ----------- | ------- |
| Hoogeveen organisch | **0** | Nog geen index-traffic |
| Prijsindicatie entry-bounce | **64,7%** (17 ses) | Nog niet <64% |
| Assen scrollers 90d | **0** | Lees-verder nog zonder effect |
| Projecten entry | **100%** | Blijft kritiek |

---

## Observaties

1. **Cyclus 10 is ~2 dagen live — géén meetbaar effect op projecten, over-ons entry of cold contact.** Dat is verwacht bij 6–10 sessies per landing. Geen bijsturing op deze pagina's nu; volgende harde beoordeling **rond 1–15 juni** (sprint.md).
2. **Verkeer zakt verder week-op-week:** 44 sessies (13–19 mei) na 92 en 170 — kleine landing-samples blijven onbetrouwbaar voor sprint-A/B.
3. **Betaald: Cross-network converteert (9/42), Paid Search niet (0/13).** Split is **ongewijzigd** t.o.v. 18-05 maar Cross-network conv. steeg (5→9). P0 voor Marketing Research: attributie, Final URL's, conversie-import — zie `.cursor/skills/google-ads-marketing/SKILL.md`.
4. **`contact.html?modus=offerte` blijft de beste route:** 9,1% bounce, 10 conversies op 11 sessies. Cyclus-10 drawer-deeplink versterkt dit patroon; effect op **kale** `/contact.html` (80%) volgt pas in juni-data.
5. **`prijsindicatie.html` blijft de sterkste inhoudspagina** (29% pagina-bounce, ~101 s). Entry-bounce 64,7% is het enige zwakke punt — cyclus-9 kosten-sectie schaadt conversie niet.
6. **`diensten.html` als landing blijft zwak:** 78,6% bounce, 0 conversies op 14 sessies — keuzehulp/cyclus-9 nog zonder verbetering.
7. **Inbound projectbeelden (Zeegse + Zuidlaren) staan nog niet op de site** — `projecten.html` heeft placeholder-cards en een oud root-hero-beeld; **niet genoeg data** om te beoordelen of echte cases de bounce omlaag trekken, maar het huidige signaal (100% entry, ~7,5 s, 1 scroller) rechtvaardigt de PM-beslissing in sprint.md om placeholders te vervangen zodra privacy akkoord is.
8. **Drachten/Heerenveen:** pagina + sitemap + defaults live; **0 GA4-sessies** — normaal binnen 48 uur; betaald verkeer meetbaar pas na Ads `--apply` + spend.

---

## Betaald zoekverkeer — notities voor Marketing Research Agent

- **Paid Search `google / cpc`:** 13 sessies, **0** conversies (ongewijzigd).
- **Cross-network `google / cpc`:** 42 sessies, **9** conversies (+4 t.o.v. vorige fetch) — eerste consistente conversies op betaald, maar niet op het Paid Search-label.
- **Actie:** GA4 ↔ Ads conversiekoppeling en Search Terms-review **vóór** nieuwe spend; Final URL's voor Drachten/Heerenveen naar `vloerverwarming-drachten.html` staan in repo-defaults — **live campagne** pas na expliciete `--apply` + goedkeuring.
- **Deeplink:** campagnes met offerte-intent op `contact.html?modus=offerte#aanvraag` (niet kale `/contact.html`).

---

## Voorstellen voor Product Manager

Max. 8 items, gesorteerd op prioriteit. Tags: **CRO** / **SEO** / **Ads**.

| # | P | Tag | Voorstel | Onderbouwing | Actie |
| - | - | --- | -------- | ------------ | ----- |
| 1 | **P0** | Ads | **GA4 ↔ Ads + Paid Search-attributie** | 13 Paid Search-sessies / 0 conv vs 9 conv op Cross-network (42 ses); ~90 conv uit Direct | Geplande sessie ~1 juni: conversie-import, auto-tagging, Search Terms; geen `--apply` zonder spend-go |
| 2 | **P0** | CRO | **Cyclus 9+10 niet bijsturen — doorlaten meten** | Projecten entry 100%, over-ons entry 80%, cold contact 80% — ongewijzigd na 2d cyclus 10 | Vervolg-fetch juni; meetdoelen a–e hard beoordelen |
| 3 | **P0** | CRO | **Echte cases op `projecten.html` (Zeegse + Zuidlaren)** | 6 entry-sessies, 100% bounce, 1 scroller; placeholders + geen nav/sitemap | Na PO-akkoord plaatsnamen: 2 case-cards uit `beeldmateriaal/projecten/`; hero naar sterkste foto; optioneel nav/sitemap |
| 4 | **P1** | SEO | **Drachten indexering + interne distributie** | 0 sessies op nieuwe pagina; Friesland 4 vs Drenthe 168 | Search Console inspect; footer-city Drachten op overige root-pagina's (PM-voorstel sprint) |
| 5 | **P1** | CRO | **`over-ons.html` entry — ATF-CTA overwegen** | Entry 80% bounce, 0 conv; onderaan-CTA (cyclus 10) raakt instappers niet | Bij juni-fetch: als nog 80%/0 conv, compacte prijs/offerte-knop in hero of direct onder lead |
| 6 | **P1** | CRO | **`diensten.html` landing** | 78,6% bounce, 0 conv op 14 entry-sessies | Eerste scherm: duidelijke split kosten (`prijsindicatie#kosten-uitleg`) vs offerte-deeplink |
| 7 | **P1** | SEO | **Friesland-cluster na Drachten-meting** | Hoogeveen/Leeuwarden/Drachten zonder traffic in export | Juni: als Drachten >0 ses, volgende city (Leeuwarden of Heerenveen-eigen pagina) uit backlog |
| 8 | **P1** | Ads | **Live zetten Drachten Final URL's** | Keywords in defaults wijzen naar live pagina; repo-only tot `--apply` | Marketing: `google_ads_add_keywords_from_defaults.py` / campagne-update na spend-go |

**Uitgesteld (geen P0 nu):** Assen hero-herontwerp (0 scrollers 90d), NL-only GA4-segment, `logo-varianten.html`-ruis.

**Tone:** nuchter, direct — conform AGENTS.md.
