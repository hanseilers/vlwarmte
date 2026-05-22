# Analytics Rapport — 22 mei 2026

**Periode:** `30daysAgo` t/m `today` (GA4 property `properties/534641753`)
**Databron:** `docs/website-manager/ga4_report.json`, timestamp **`2026-05-22T17:32:56`**
**Vorige sprint:** cyclus 11 live sinds **20-05-2026** (`dc3d2de`); deze fetch is **~2 dagen post-deploy** — te vroeg voor harde beoordeling van sprint-11-meetdoelen (juni-fetch ~1–15 juni).

**Vorige sprint effect (cyclus 11):** `projecten.html` zichtbaar in GA4 (8 sessies pad / 7 entry) maar entry-bounce nog **100%** (7 sessies) — sample te klein. `diensten.html` landing **73,3%** bounce maar **3 conv.** op 15 entry (positief teken, niet bijsturen). Drachten nog **0** sessies in export. Offerte-deeplink ongewijzigd sterk. Paid Search **13 / 0** conv. vs Cross-network **61 / 9**.

---

## Kerncijfers

| Metric | Waarde | Trend t.o.v. fetch 20-05 |
| ------ | ------ | ------------------------ |
| Sessies (30d, som devices) | **~343** (181+149+13) | +~6% |
| Homepage `/` | **198** sessies, bounce **60,1%** | +16 sessies, bounce licht omhoog |
| `/prijsindicatie.html` | **56** sessies, **~94 s**, bounce **32,1%** | stabiel sterk |
| Direct | **222** sessies, **90** conv. | +3 sessies |
| Betaald `google / cpc` | Cross-network **61 / 9**; Paid Search **13 / 0** | meer Cross-sessies, Paid ongewijzigd |
| Organic `google` | **8** sessies, **1** conv. | stabiel laag |
| NL — Drenthe / Groningen / Friesland | **172 / 20 / 6** | Friesland +2 |

> Week 15–21 mei: **49** sessies — landing-cijfers blijven ruis tot juni-fetch.

---

## Landingspagina's (instappunten)

| Landing | Sessies | Bounce | Conv. | Opmerking |
| ------- | ------- | ------ | ----- | --------- |
| `/contact.html?modus=offerte` | 11 | **9,1%** | 10 | goudstandaard — ongewijzigd |
| `/contact.html` (koud) | 10 | **80%** | 12 | intent-strip live; effect nog niet meetbaar |
| `/diensten.html` | 15 | **73,3%** | **3** | duo-CTA hero verwijderd in `b040cea`; 3 conv. klein sample |
| `/projecten.html` | 7 | **100%** | 0 | cases live; afwachten juni |
| `/over-ons.html` | 10 | **80%** | 0 | geen entry-CTA-wijziging deze cyclus |
| `/vloerverwarming-assen.html` | 6 | **100%** | 0 | 0 scrollers (90d) |
| `/prijsindicatie.html` | 20 | 65% | 24 | sterk conv., bounce als landing hoger dan pad-bounce |

---

## Betaald verkeer (Marketing Research Agent)

| Kanaal | Sessies | Conv. | Aanbeveling |
| ------ | ------- | ----- | ----------- |
| Cross-network `google / cpc` | 61 | 9 | attributie + RSA-sync na PO |
| Paid Search `google / cpc` | 13 | 0 | **P0** GA4↔Ads-sessie ~1 juni — geen budget↑ |

---

## Prioriteiten voor Product Manager (max. 5)

| P | Tag | Voorstel | Onderbouwing |
| - | --- | -------- | ------------ |
| **P0** | Meet | **Geen bijsturing** projecten / over-ons / Assen / diensten-hero vóór juni-fetch | Cyclus 11 ~2d in venster; sprint-11 meetdoelen expliciet |
| **P0** | Ads | **GA4 ↔ Ads + Paid Search-attributie** (~1 juni) | 13 Paid / 0 conv vs 61 Cross / 9 |
| **P1** | SEO | **Drachten interne links** + sitemap `lastmod` | 0 GA4-sessies; footer/sitemap al live |
| **P1** | CRO | **`diensten.html` hero-link** naar `projecten.html` | Social cyclus 12 + message-match; geen tweede hero-knop (bewust na `b040cea`) |
| **P1** | Ads prep | **Defaults:** `projecten.html` in `final_urls`, **meppel**-keyword eruit | Geen landingspagina; geen `--apply` zonder PO |
| **P2** | CRO | **`over-ons.html` ATF-CTA** | alleen na juni-fetch als 80% bounce / 0 conv aanhoudt |

---

## Afgewezen deze cyclus

- **Duo-CTA terug op `diensten.html` hero** — bewust verwijderd; 3 conv. op landing te vroeg om te heropenen.
- **Nieuwe pagina renovatie houten vloer** — max. 1 pagina/sprint; backlog P2.
- **RSA `--apply` / spend** — na PO + attributiefix.

---

## Context volgende fetch (juni)

Harde check cyclus 9–11 meetdoelen: `projecten.html` entry-bounce, Drachten organisch, cold `contact.html`, `diensten.html` landing, Paid vs Cross conversies.
