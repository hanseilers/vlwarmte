# Analytics Rapport — 7 juni 2026

**Periode:** `30daysAgo` t/m `today` (GA4 property `properties/534641753`; venster ca. 8 mei — 7 juni 2026)
**Databron:** `docs/website-manager/ga4_report.json`, timestamp **`2026-06-07T15:55:10`**
**GSC:** niet beschikbaar in deze fetch — SEO-doelen (CTR prijsindicatie, Hoogeveen-rang, organische queries) blijven **niet te toetsen**.
**Vorige sprint effect (cyclus 14):** Deploy **`0099874`** live **01-06-2026** (~6 dagen in meetvenster). Assen layout-fix, prijsindicatie ATF message-match, OG/Twitter meta, Drenthe-hub Assen-ankertekst en Ads-defaults JSON zijn **deels te vroeg** om hard te meten. Wel zichtbaar: prijsindicatie entry-bounce daalde licht (58,3% → 54,5%); homepage gem. duur steeg (35 s → 50 s). Assen 90d-data (**0,7 s**, **0 scrollers**) is nog **niet verbeterd** — sample te klein en fix te recent.

---

## Kerncijfers

| Metric | Waarde (30d) | Trend t.o.v. fetch 01-06 |
| ------ | ------------ | ------------------------ |
| Sessies (som devices) | **201** (113 desktop + 70 mobile + 18 tablet) | ↓ **−2%** (206 → 201) |
| Actieve gebruikers (devices) | **168** | ↓ (175 → 168)* |
| Homepage `/` sessies / bounce | **145 / 64,8%** | ↓ sessies (−2); bounce ↓ (66,0% → 64,8%) |
| Homepage `/` gem. duur | **50 s** | ↑ (35 s → 50 s) |
| `/prijsindicatie.html` | **33 sess / ~35% bounce / 73 s** | ↓ sessies (−2); engagement stabiel |
| Totaal conversies (kanalen) | **63** (Direct 41 + Cross-network 22) | ↓ (68 → 63) |
| Direct | **74 sess / 41 conv.** (55% conv-rate) | ↓ sess (−11); conv −6 |
| Cross-network `google/cpc` | **85 sess / 22 conv.** | ↑ sess (+6); conv +2 |
| Paid Search `google/cpc` | **11 / 0 conv.** | ↓ sess (−2); **nog steeds nul** |
| Organic Search `google/organic` | **9 / 0 conv.** | ↑ sess (+1); conv −1 |
| Facebook referrals (3 bronnen) | **20 / 0 conv.** | stabiel |

\*Actieve gebruikers per device-som; GA4 telt unieke users niet identiek aan sessies.

**Weekly trend (sessies/week):**

| Week | Sessies | Opmerking |
| ---- | ------- | --------- |
| 27 apr – 3 mei | 177 | Piek rolt uit venster |
| 4 – 10 mei | 73 | |
| 11 – 17 mei | 46 | |
| 18 – 24 mei | 60 | |
| 25 – 31 mei | 16 | Laag niveau |
| 1 – 6 jun | 16 | Stabiel laag; huidige week deels |

Stabiel niveau na campagne-piek: **~46–60 sess/week**; laatste twee weken **16 sess/week** — laag maar consistent (geen nieuwe piek).

---

## Top pagina's

| Pagina | Sessies | Bounce | Gem. duur | Opmerking |
| ------ | ------- | ------ | --------- | --------- |
| `/` (Home) | 145 | **64,8%** | 50 s | 90d: 232 sess, 31 scrollers (13,4%) |
| `/prijsindicatie.html` | 33 | **~35%** | **73 s** | Kroonjuweel; wizard houdt stand |
| `/contact.html` (nieuwe title) | 24 | **12,5%** | 59 s | Sterk |
| `/contact.html` (oude title) | 13 | **76,9%** | 30 s | Verouderde title-variant — cache/oude links |
| `/projecten.html` | 10 | **60%** | 20 s | 90d: 18 sess, **14 s** gem., 2 scrollers |
| `/werkwijze.html` | 7 | **0%** | 194 s | 90d: 22 sess; landing 2 sess / **4 conv.** |
| `/diensten.html` | 6 | **0%** | 27 s | Weinig volume |
| `/faq.html` | 6 | 17% | 11 s | Laag volume, korte sessies |
| `/over-ons.html` | 6 | 17% | 18 s | Geen entry in top-15 |
| `/systemen-producten.html` | 5 | **0%** | 377 s | Lange sessies bij betrokkenen |
| `/vloerverwarming-assen.html` | 1 (+ 7 in 90d) | — | 5 s | 90d: **0,7 s**, **0 scrollers** — nog rood |

---

## Landingspagina's (instappunten)

| Landing | Sessies | Bounce | Conv. | Opmerking |
| ------- | ------- | ------ | ----- | --------- |
| `/` | 136 | **66,2%** | **32** | Werkpaard; hoogste bounce onder grote instappers |
| `/contact.html?modus=offerte` | 11 | **9,1%** | **10** | Gouden deeplink — Ads/social match |
| `/prijsindicatie.html` | 11 | **54,5%** | **8** | Entry-bounce ↓ t.o.v. 58,3%; doel <45% **niet gehaald** |
| `/contact.html` (koud) | 3 | 67% | 9 | Conv. > sess = meerdere events per sess |
| `/diensten.html` | 2 | 50% | 0 | Sample te klein |
| `/projecten.html` | 2 | 50% | 0 | Sample te klein |
| `/werkwijze.html` | 2 | 0% | **4** | Sterk conv-signaal; volume laag |
| `/systemen-producten.html` | 2 | 0% | 0 | |
| Facebook `fbclid` op `/` | 1 | 100% | 0 | Social cold traffic |
| Facebook `fbclid` op `contact?modus=informatie` | 3 | 100% | 0 | Verkeerde intentie voor social-klik |

**Geen `gclid` zichtbaar** in landingPagePlusQueryString — waarschijnlijk auto-tagging of attributie-lek naar Direct/Cross-network. Wel **96 sessies `google/cpc`** totaal (85 Cross-network + 11 Paid Search).

---

## Traffic bronnen

| Kanaal | Sessies | Conv. | Conv. rate | Aanbeveling |
| ------ | ------- | ----- | ---------- | ----------- |
| Cross-network `google/cpc` | **85** | **22** | 26% | Meeste betaalde conv.; check GA4↔Ads koppeling |
| Direct `(direct) / (none)` | **74** | **41** | **55%** | Verdacht hoog — deels Ads-attributielek |
| Organic Social Facebook (3 vars) | **20** | **0** | **0%** | Bezoekers wel, leads niet |
| Paid Search `google/cpc` | **11** | **0** | **0%** | **P0 Marketing Research** |
| Organic Search `google/organic` | **9** | **0** | **0%** | Mager; GSC nodig voor queries |
| Cross-network `(data not available)` | **1** | **0** | — | Ruis |

### Betaald verkeer — aanbevelingen Marketing Research Agent

1. **Paid Search 0 conversies op 11 sessies** terwijl Cross-network (`google/cpc`) 22 conv. op 85 sessies levert — attributie split of verkeerde landing-URL's in Paid Search-adgroep.
2. **`gclid` ontbreekt** in entry-rapport — controleer **GA4 auto-tagging** + **Google Ads ↔ GA4 koppeling** (Admin UI; stond uitgesteld sprint 14).
3. **Live RSA final URLs** campagne `23834672782` handmatig syncen met repo-defaults (`contact.html?modus=offerte#aanvraag` + `prijsindicatie.html`) — Developer Rapport 01-06 meldde dit als open PO-stap.
4. **Direct 55% conv-rate** dekt waarschijnlijk deels betaald verkeer zonder kanaal-label — pas campagne-interpretatie aan tot koppeling staat.
5. Geen budgetverhoging (>€2/dag) zolang Paid Search **0 conv.** blijft (PM-besluit cyclus 14).

---

## Geografie

| Regio | Sessies | Opmerking |
| ----- | ------- | --------- |
| Drenthe | **57** | Doelregio — sterk |
| Groningen | **23** | Doelregio |
| Friesland | **10** | Doelregio |
| **Noord-NL totaal** | **~90** | ~45% van 201 sessies (excl. not set) |
| Noord-Holland | **27** | Buiten doel — organisch/betaald bereik |
| Zuid-Holland | **12** | Buiten doel |
| (not set) | **22** | Attributie-gap |
| VS (Oregon + Colorado) | **12** | Waarschijnlijk bots/scanners |

Doelregio Drenthe + Groningen + Friesland = **90 sessies** — gezond aandeel. Noord-Holland (27) en US-traffic (12) zijn ruis, geen prioriteit voor content.

---

## Devices

| Device | Sessies | % |
| ------ | ------- | - |
| Desktop | 113 | 56% |
| Mobile | 70 | 35% |
| Tablet | 18 | 9% |

Mobile is **35%** — relevant voor hero/wizard ATF-checks op prijsindicatie en Assen.

---

## Observaties

1. **Verkeer stabiel-laag, conversies iets omlaag.** 201 sessies (−2% t.o.v. vorige fetch), 63 kanaalconversies (−5). Geen nieuwe campagne-piek; laatste twee weken elk 16 sessies.

2. **Betaald verkeer domineert, maar Paid Search converteert niet.** 96 sessies via `google/cpc`; vrijwel alle conv. zit in Cross-network (22) en Direct (41, deels leak). Paid Search: **11 sess, 0 conv.** — sprint-14-meetdoel **niet gehaald** (≥1 conv.).

3. **Prijsindicatie ATF-fix werkt deels.** Entry-bounce daalde van 58,3% naar **54,5%** (11 sessies) — richting goed, maar meetdoel **<45%** nog niet gehaald. Pageview-bounce blijft gezond (~35%).

4. **Assen nog niet hersteld in data.** 90d: 7 sess, **0,7 s** gem. duur, **0 scrollers**. Layout-fix live sinds 01-06; 30d slechts 1 sessie — **te vroeg** voor harde uitspraak, maar geen verbetering zichtbaar in 90d-venster.

5. **Facebook levert bezoekers, geen leads.** 20 sessies, 0 conv.; `fbclid`-entries op contact `modus=informatie` bounce'en 100%. Social posts linken waarschijnlijk naar verkeerde intentie.

6. **Organisch zoeken blijft mager.** 9 sessies, 0 conv. — GSC-fetch ontbreekt nog; Heerenveen-keyword zonder landingspagina blijft SEO-gap (AGENTS.md).

7. **Contact offerte-deeplink blijft topconverter.** `/contact.html?modus=offerte`: 11 sess, 9,1% bounce, 10 conv. — bevestigt RSA-defaults-keuze.

---

## Content- & CTA-analyse (HTML)

| Pagina | CTA-sterkte | Opmerking |
| ------ | ----------- | --------- |
| `index.html` | Sterk | Hero: prijsindicatie + werkwijze; sticky mobile CTA offerte; Drenthe-hub met Assen-link (cyclus 14) |
| `prijsindicatie.html` | Sterk | ATF lead noemt "twee minuten" + richtbedrag; wizard direct onder hero |
| `contact.html` | Sterk | Drie modi + direct bellen/WhatsApp; geen hero-CTA overload |
| `diensten.html` | Matig | Hero: één primary (prijsindicatie); offerte pas onderaan — bewust (CTA-dichtheid) |
| `werkwijze.html` | Matig | Twee CTA-banden met prijsindicatie + FAQ — geen offerte-primary; past bij vertrouwen-fase |
| `projecten.html` | Matig | Hero offerte + prijsindicatie; lange lead met interne links; 60% bounce suggereert mismatch verwachting/beeld |
| `over-ons.html` | Matig | Prijsindicatie + informatie; geen entry-traffic — laag prioriteit |
| `vloerverwarming-assen.html` | Verbeterd | Vroege CTA-band verwijderd (cyclus 14); hero nog 3 knoppen — minder dan voorheen |

**Lokale SEO:** Stad-pagina's (Assen, Groningen, Leeuwarden, Zuidlaren) bestaan; **Heerenveen** ontbreekt nog. Drenthe-hub op homepage versterkt interne linking.

---

## Voorstellen voor Product Manager

### 1. GA4 ↔ Google Ads koppeling + auto-tagging afronden
- **Prioriteit:** Hoog
- **Onderbouwing:** Paid Search **11 sess / 0 conv.**; geen `gclid` in entry-rapport; Direct **55% conv-rate** (41/74) wijst op attributielek. Cross-network levert wél 22 conv.
- **Actie:** PO/Admin — GA4 property koppelen aan Ads-account, auto-tagging aan, live RSA final URLs syncen (campagne `23834672782`). Geen developer-werk.
- **Verwacht effect:** Eerlijke Paid Search-rapportage; basis voor campagne-optimalisatie; meetdoel sprint 14 (≥1 Paid Search conv.) testbaar.

### 2. Marketing Research: Paid Search landing-URL's en RSA audit
- **Prioriteit:** Hoog
- **Onderbouwing:** Cross-network `google/cpc` 85 sess / 22 conv. vs Paid Search 11 / 0 — zelfde medium, andere uitkomst. Offerte-deeplink presteert als landing (9,1% bounce, 10 conv.).
- **Actie:** Marketing Research Agent — controleer welke final URLs live staan per adgroep; align met `google_ads_lead_campaign_defaults.json`; overweeg negatives op verkeerde queries.
- **Verwacht effect:** Paid Search conv. > 0 binnen 4 weken na sync.

### 3. Prijsindicatie entry-bounce verder omlaag (mobile ATF)
- **Prioriteit:** Hoog
- **Onderbouwing:** Entry-bounce **54,5%** (11 sess) — verbeterd t.o.v. 58,3%, maar meetdoel **<45%** niet gehaald. Pageview-bounce ~35% — koude instappers haken af vóór wizard.
- **Actie:** Developer — op mobile (375×667) wizard-stap 0 zichtbaar maken zonder scroll (compactere hero of wizard omhoog); geen extra CTA's.
- **Verwacht effect:** Entry-bounce <45% bij ≥10 entry-sess in volgende fetch (~22 juni).

### 4. Assen follow-up meten — eventueel LCP/hero-image
- **Prioriteit:** Hoog (monitoring) / Midden (actie pas na juni-fetch)
- **Onderbouwing:** 90d nog **0,7 s** gem. duur, **0 scrollers** op 7 sessies. Layout-fix live 6 dagen; 30d sample = 1 sess.
- **Actie:** Wacht tot fetch ~22 juni. Als bounce >70% en duur <5 s blijft: hero-image optimaliseren (lichter bestand uit `beeldmateriaal/`) of LCP-check. Geen wijziging andere stad-pagina's.
- **Verwacht effect:** Bounce <70%, gem. duur >5 s, ≥1 scroller in 90d.

### 5. Homepage entry-bounce verlagen voor betaald/organisch verkeer
- **Prioriteit:** Midden
- **Onderbouwing:** `/` als landing: **136 sess, 66,2% bounce** — hoogste instap met meeste verlies. Gem. duur steeg naar 50 s (betrokkenen blijven wel).
- **Actie:** Marketing + Developer — overweeg RSA/homepage-split: betaald verkeer naar offerte-deeplink of prijsindicatie i.p.v. `/`; geen hero-CTA-wijziging (PM cyclus 14 afgewezen) tenzij data na Ads-koppeling anders zegt.
- **Verwacht effect:** Minder bounce op grootste instapper; meer conv. via proven landings.

### 6. GSC OAuth afronden voor SEO-meetdoelen
- **Prioriteit:** Midden
- **Onderbouwing:** Organic Search **9 sess / 0 conv.**; GSC ontbreekt — CTR prijsindicatie, Hoogeveen-rang en Drenthe-hub niet te toetsen (uitgesteld sprint 13–14).
- **Actie:** PO — `secrets/gsc.env` + refresh token via `scripts/gsc_get_refresh_token.py`.
- **Verwacht effect:** Query-level data voor SEO-voorstellen; Heerenveen-gap onderbouwd.

### 7. Facebook message-match: één intentie per post
- **Prioriteit:** Midden
- **Onderbouwing:** 20 Facebook-sessies, **0 conv.**; 3× `fbclid` op contact `modus=informatie` met **100% bounce**.
- **Actie:** Social kalender cyclus 15 — posts linken naar offerte-deeplink of prijsindicatie (niet informatie-tab); één CTA per post.
- **Verwacht effect:** Social conv. > 0 of lagere bounce op social-entries.

### 8. `projecten.html` engagement verbeteren
- **Prioriteit:** Midden
- **Onderbouwing:** 10 sess / **60% bounce** / 20 s gem.; 90d **14 s** gem. op 18 sess, 2 scrollers. Hero is copy-heavy met veel links.
- **Actie:** Developer — verkort hero-lead (behoud trust-strip); eventueel één projectfoto prominenter ATF op mobile. Geen extra CTA-knoppen.
- **Verwacht effect:** Bounce <50%, gem. duur >30 s bij ≥10 sess.

### 9. Oude contact-title variant (77% bounce) opschonen
- **Prioriteit:** Laag
- **Onderbouwing:** 13 sess met title "Contact en offerte | VLWarmte" — **76,9% bounce** vs 12,5% op nieuwe title.
- **Actie:** Check externe links/bookmarks; geen HTML-wijziging nodig (title al geüpdatet). Monitor of oude variant uitsterft.
- **Verwacht effect:** Bounce-contact overall omlaag na verloop.

### 10. Heerenveen: pagina of keyword pauzeren (na GSC)
- **Prioriteit:** Laag (blokkeert op GSC)
- **Onderbouwing:** Ads-keyword `vloerverwarming heerenveen` zonder dedicated page (AGENTS.md); organische groei beperkt (9 organic sess totaal).
- **Actie:** Na GSC-fetch — bouw `vloerverwarming-heerenveen.html` **of** pauzeer keyword in Ads. Max. 1 city-pagina/sprint (discipline na Assen).
- **Verwacht effect:** Betere message-match voor Heerenveen-queries; minder verspilde Ads-spend.

---

## Meetmoment volgende cyclus

- **Juni-fetch ~22 juni** — ijkpunt voor sprint 13 + 14 meetdoelen (Assen bounce/duur, prijsindicatie entry-bounce <45%, Paid Search conv.).
- **GSC beschikbaar?** → prijsindicatie CTR, Hoogeveen-rang, hub op `/`.
- **GA4↔Ads gekoppeld?** → Paid Search conv. interpretabel.

---

*Rapport gegenereerd door Analytics Agent — geen website-wijzigingen doorgevoerd.*
