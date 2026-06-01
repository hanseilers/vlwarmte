# Analytics Rapport — 1 juni 2026

**Periode:** `30daysAgo` t/m `today` (GA4 property `properties/534641753`; venster ca. 2 mei — 1 juni 2026)
**Databron:** `docs/website-manager/ga4_report.json`, timestamp **`2026-06-01T11:03:46`** (verse fetch via `.venv/bin/python scripts/ga4_fetch.py`)
**GSC:** niet beschikbaar — `secrets/gsc.env` ontbreekt; SEO-doelen sprint 13 (CTR prijsindicatie, Hoogeveen-rang, Drenthe-hub) zijn **niet te toetsen** deze cyclus.
**Vorige sprint effect (cyclus 13):** Deploy **`47a9583`** live **26-05-2026** (~6 dagen in meetvenster). Title/meta prijsindicatie, Drenthe-hub op `/`, Hoogeveen-dorpen, werkwijze-links op diensten/projecten en Assen-diagnose zijn **te vroeg** om hard te meten. Eén sessie met nieuwe prijsindicatie-title zichtbaar; GSC/organisch effect verwacht pas **juni-fetch ~22 juni**.

---

## Kerncijfers

| Metric | Waarde (30d) | Trend t.o.v. fetch 23-05 |
| ------ | ------------ | ------------------------ |
| Sessies (som devices) | **206** (119 desktop + 70 mobile + 17 tablet) | ↓ **−41%** (352 → 206)* |
| Homepage `/` sessies / bounce | **147 / 66,0%** | ↓ sessies; bounce ↑ (60,9% → 66%) |
| Homepage `/` gem. duur | **35 s** | ↓ (61 s → 35 s) |
| `/prijsindicatie.html` | **35 sess / 34% bounce / 86 s** | ↓ sessies; engagement stabiel |
| Totaal conversies (kanalen) | **68** (Direct 47 + Cross-network 20 + Organic 1) | ↓ absoluut; mix verschoven |
| Direct | **85 sess / 47 conv.** (55% conv-rate) | ↓ sess (−62%); conv −48% |
| Cross-network `google/cpc` | **79 sess / 20 conv.** | ↑ sess (+23%); conv +122% |
| Paid Search `google/cpc` | **13 / 0 conv.** | onveranderd — **P0 blijft** |
| Organic Search `google/organic` | **8 / 1 conv.** | stabiel mager |
| Facebook referrals (3 bronnen) | **20 / 0 conv.** | ↓ sess (−38%); conv nog steeds nul |

\*De daling is deels **meetvenster-effect**: de piekweek 27 apr – 3 mei (172 sessies, campagne-spike) rolt uit het 30-dagenvenster. Stabiel niveau na piek: **~49–56 sess/week** (11–24 mei); laatste week **15 sess** (25–31 mei) — laag, maar gedeeltelijk huidige week.

**Weekly trend (sessies/week):**

| Week | Sessies |
| ---- | ------- |
| 27 apr – 3 mei | 172 (piek — rolt uit venster) |
| 4 – 10 mei | 75 |
| 11 – 17 mei | 49 |
| 18 – 24 mei | 56 (+14% w/w) |
| 25 – 31 mei | 15 |

---

## Top pagina's

| Pagina | Sessies | Bounce | Gem. duur | Opmerking |
| ------ | ------- | ------ | --------- | --------- |
| `/` (Home) | 147 | **66,0%** | 35 s | 90d: 222 sess, 28 scrollers (12,6%) — veel verkeer, matige betrokkenheid |
| `/prijsindicatie.html` | 35 | **34,3%** | **86 s** | Kroonjuweel; wizard houdt stand |
| `/contact.html` (2 titels) | 23 + 13 | 17% / **77%** | 61 / 30 s | Oudere title-variant 77% bounce — titel-migratie |
| `/projecten.html` | 10 + 1 | 60% / 0% | 20 / 54 s | 90d: 18 sess, **14 s** gem., 2 scrollers — zwak |
| `/werkwijze.html` | 7 + 2 | 0% / 0% | 194 / 506 s | 90d: 22 sess; als landing 2 sess / **4 conv.** |
| `/diensten.html` | 5 + 5 | 60% / 0% | 13 / 23 s | Weinig volume; landing-sample te klein |
| `/systemen-producten.html` | 5 + 1 | 0% | 377 / 36 s | Lange sessies bij betrokkenen |
| `/over-ons.html` | 5 + 2 | 20% / 0% | 18 / 22 s | Geen entry in top-15 deze fetch |
| `/faq.html` | 6 | 17% | 11 s | Laag volume |
| `/vloerverwarming-groningen.html` | 1 (+ 8 in 90d) | — | 10 s | 90d: 51 s, 1 scroller |
| `/vloerverwarming-assen.html` | 1 (+ 7 in 90d) | — | 5 s | 90d: **0,7 s**, **0 scrollers** — nog steeds rood |

---

## Landingspagina's (instappunten)

| Landing | Sessies | Bounce | Conv. | Opmerking |
| ------- | ------- | ------ | ----- | --------- |
| `/` | 138 | **67,4%** | **37** | 27% conv-rate als entry — werkpaard |
| `/prijsindicatie.html` | 12 | **58,3%** | **8** | Hogere entry-bounce dan pageview (34%) — koude instappers |
| `/contact.html?modus=offerte` | 11 | **9,1%** | **10** | Gouden deeplink — campagne/social match |
| `/diensten.html` | 4 | **75,0%** | 0 | Hero-link projecten + werkwijze-link net live; te vroeg |
| `/contact.html` (koud) | 3 | 67% | 9 | Conv. > sess = meerdere events per sess |
| `/projecten.html` | 2 | 50% | 0 | Sample te klein; 90d-data nog zwak |
| `/werkwijze.html` | 2 | 0% | **4** | Sterk conv-signaal; volume nog laag |
| `/systemen-producten.html` | 2 | 0% | 0 | `#laagopbouw` nog niet meetbaar |
| Facebook `fbclid`-entries op `/` en contact | 3 | 100% | 0 | Social cold traffic bounce't direct |

---

## Traffic bronnen

| Kanaal | Sessies | Conv. | Conv. rate | Aanbeveling |
| ------ | ------- | ----- | ---------- | ----------- |
| Direct `(direct) / (none)` | **85** | **47** | **55%** | Nog steeds verdacht hoog — deels Ads-leak |
| Cross-network `google/cpc` | **75** | **20** | 27% | Meeste betaalde conv. zit hier; attributie deels verschoven t.o.v. Direct |
| Paid Search `google/cpc` | **13** | **0** | **0%** | **P0** — zie Marketing-blok |
| Organic Social Facebook (3 vars) | **20** | **0** | **0%** | Bezoekers wel, leads niet |
| Organic Search `google/organic` | **8** | **1** | 12% | SEO-instroom blijft mager |
| Cross-network `(data not available)` | 4 | 0 | 0% | Privacy/consentless |
| Unassigned `(not set)` | 1 | 0 | 0% | Geen uitschieter meer |

---

## Geografie

| Regio | Sessies | Opmerking |
| ----- | ------- | --------- |
| Drenthe (NL) | **62** | Kern — 30% van totaal |
| North Holland (NL) | **29** | Buiten doelgebied |
| `(not set)` | **24** | Tracker-ruis / privacy |
| Groningen (NL) | **23** | Doelgebied — redelijk |
| South Holland (NL) | **13** | Buiten doelgebied |
| Friesland (NL) | **8** | Doelgebied — nog dun |
| **VS** (OR + CO) | **12** | Bots/proxies — niet meetellen |
| North Brabant (NL) | **8** | Buiten |

> Drenthe + Groningen + Friesland samen **93 sess** (~45% van 206) — past bij Noord-NL-focus. Friesland (8) blijft onderbenut t.o.v. Drachten/Heerenveen-ambities.

---

## Mobile vs Desktop

| Device | Sessies | Aandeel |
| ------ | ------- | ------- |
| Desktop | 119 | 58% |
| Mobile | 70 | **34%** |
| Tablet | 17 | 8% |

> Geen bounce/conv per device in fetch — Assen-diagnose (mobiel-layout) blijft op content-analyse steunen tot device-breakdown er is.

---

## Betaald verkeer (Marketing Research Agent)

| Kanaal | Sessies | Conv. | Aanbeveling |
| ------ | ------- | ----- | ----------- |
| Cross-network `google/cpc` | 79 | 20 | **P1** — welk campagnetype (PMax/Demand Gen)? Landings-URL's per ad controleren. |
| Paid Search `google/cpc` | **13** | **0** | **P0** — GA4 ↔ Ads-sessie ~1 juni (gepland sprint 12/13). Tag + landing vóór budget/bid-wijzigingen. |
| Direct (vermoedelijk Ads-leak) | 85 / 47 | **P0** | 55% conv-rate op Direct is onrealistisch zonder merkbekendheid. Deels verschoven naar Cross-network (+11 conv.), maar Paid Search blijft 0/13. |

**Expliciet voor Marketing Research Agent:**

1. **`contact.html?modus=offerte#aanvraag`** als final URL voor offerte-intent — data bevestigt 9% bounce / 10 conv. op 11 sess.
2. **Paid Search 0/13** — na GA4↔Ads-link: per keyword/ad controleren of landings-URL matcht (homepage 67% bounce is geen ideale Search-landing).
3. **Facebook 20 sess / 0 conv.** — posts moeten één intentie + één link (`?modus=offerte`, `?modus=bel` of `prijsindicatie.html`); geen `/` of `projecten.html` als cold landing zonder CTA-match.
4. **RSA-variant + sitelinks `--apply`** — pas na attributiefix en PO-akkoord; eerst `google_ads_list_campaigns.py` + `--dry-run`.

Zie `.cursor/skills/google-ads-marketing/SKILL.md` (GA4 ↔ Ads-koppeling).

---

## Observaties

1. **Verkeersniveau normaliseert na campagne-piek.** 206 sess vs 352 vorige fetch klinkt hard, maar de piekweek (172 sess) zit grotendeels buiten het venster. Stabiel post-piek: ~50 sess/week. Geen paniek — wel realistischer baseline voor juni.

2. **Attributie verschuift deels van Direct naar Cross-network** (Direct conv. 90→47; Cross-network 9→20). Dat kan een begin van GA4↔Ads-sync of vensterverschil zijn. **Paid Search 0/13 is onveranderd** — dat is het echte probleem, niet het totaal aantal conversies.

3. **`/contact.html?modus=offerte` blijft de beste campagne-landing.** 11 entry-sess, 9% bounce, 10 conv. Alle paid/social deeplinks moeten hierop of op `prijsindicatie.html` landen — niet op homepage of projecten.

4. **Homepage bounce stijgt (67% entry, 35 s duur).** Sprint-13 Drenthe-hub (`#drenthe-hub`) is 6 dagen live — te vroeg voor SEO-effect, maar homepage als instap blijft zwaar. Bezoekers die via `/` binnenkomen scrollen weinig (28/222 scrollers in 90d = 13%).

5. **`/vloerverwarming-assen.html` — diagnose bevestigd, fix uitgesteld.** 90d: 7 sess, 0,7 s, 0 scrollers. Developer Rapport cyclus 13 wijst op extra readnext-link + CTA-band vóór content (niet in lijn met Groningen). Geen code-fix live — meting blijft rood.

6. **`/projecten.html` engagement blijft zwak in 90d.** 18 sess, gem. **14 s**, 2 scrollers. Werkwijze-link in hero is net live; social/post-traffic naar projecten moet message-match krijgen. Pas oordelen entry-bounce na ≥10 entry-sess in juni-fetch.

7. **Organisch zoekverkeer flat (8 sess / 1 conv.).** Zonder GSC geen CTR/rang-check op sprint-13 doelen (prijsindicatie, Hoogeveen, Drenthe-hub). **GSC-setup is blocker** voor SEO-sprintevaluatie.

8. **Facebook 20 sess / 0 conv.** — social kalender cyclus 13 stuurde op message-match; effect nog niet zichtbaar (6 dagen). fbclid-landings op `/` en contact bounce'en 100%.

---

## Voorstellen voor Product Manager (max. 10)

### 1. GA4 ↔ Google Ads koppeling — deze week afronden
- **Prioriteit:** **Hoog (P0)**
- **Onderbouwing:** Paid Search **13 sess / 0 conv.** ongewijzigd t.o.v. vorige fetch. Direct nog **55% conv-rate** (47/85) — te hoog voor puur merkverkeer. Cross-network pakte +11 conv. op, maar Search-campagne zelf rapporteert nul.
- **Actie:** Admin GA4 → Product Links → Google Ads; auto-tagging aan; `gclid`-test op `contact.html?modus=offerte#aanvraag`. Notitie in sprint.md of proposals.md.
- **Verwacht effect:** Eerlijke ROAS per campagne; Paid Search 0/13 wordt interpreteerbaar (tag vs landing).

### 2. `vloerverwarming-assen.html` — layout-fix cyclus 14
- **Prioriteit:** **Hoog**
- **Onderbouwing:** 90d **7 sess / 0,7 s / 0 scrollers / 86% bounce**. Diagnose cyclus 13: readnext-link + extra CTA-band tussen hero en content (vs Groningen-template).
- **Actie:** Developer: verwijder `<p class="project-hero__readnext">` en CTA-band direct na hero (~10 regels HTML); optioneel hero-image lichter (13.34.00.jpeg). Geen andere stad-pagina's aanpassen.
- **Verwacht effect:** Bounce <70%, gem. duur >5 s, ≥1 scroller binnen 4–6 weken.

### 3. GSC OAuth inrichten — blocker voor sprint-13 SEO-evaluatie
- **Prioriteit:** **Hoog**
- **Onderbouwing:** Sprint 13 meetdoelen (prijsindicatie CTR >0,5%, Hoogeveen rang <10, `/` op _vloerverwarming drenthe_) vereisen GSC. `secrets/gsc.env` ontbreekt; fetch overgeslagen.
- **Actie:** `cp secrets/gsc.env.example secrets/gsc.env`; `scripts/gsc_get_refresh_token.py` met verified owner-account; `.venv/bin/python scripts/gsc_fetch.py` vóór juni-fetch ~22 juni.
- **Verwacht effect:** Harde SEO-check op cyclus-13-wijzigingen; geen gokwerk meer op title/meta-effect.

### 4. Paid Search landings audit — Marketing Research Agent
- **Prioriteit:** **Hoog**
- **Onderbouwing:** **0 conv. op 13 Paid Search-sess** terwijl offerte-deeplink **10 conv. op 11 sess** haalt. Vermoedelijk landen Search-ads op `/` (67% bounce) of verkeerde URL.
- **Actie:** Marketing: per actieve ad/ad group final URL controleren; verschuif offerte-intent naar `contact.html?modus=offerte#aanvraag` of `prijsindicatie.html`. Na GA4↔Ads-link opnieuw meten.
- **Verwacht effect:** Paid Search conv-rate van 0% naar 5–15% (= 1–2 leads/30d bij huidig volume).

### 5. Facebook message-match — social kalender aanscherpen
- **Prioriteit:** **Midden**
- **Onderbouwing:** **20 Facebook-sess / 0 conv.**; fbclid-entries op `/` en contact met 100% bounce. Sprint 13 social-plan noemde dit expliciet.
- **Actie:** Marketing/Social: één intentie + één link per post (`?modus=offerte#aanvraag`, `?modus=bel#aanvraag` of prijsindicatie); zelfde belofte in caption als op landings-hero. Geen developer-werk.
- **Verwacht effect:** 1–2 leads per 30 social-sess (2–5% conv-rate).

### 6. `projecten.html` — pas hero-tweak na juni-fetch bij aanhoudende zwakte
- **Prioriteit:** **Midden** (uitgesteld)
- **Onderbouwing:** 90d **18 sess / 14 s gem. / 2 scrollers** (11% scroll-rate). Entry-sample deze fetch: 2 sess — te klein. Werkwijze-link net toegevoegd.
- **Actie:** **Geen wijziging nu.** Juni-fetch: als entry-bounce >90% bij ≥10 entry-sess én scroll-rate <15%: hero compacter / case-gallery hoger.
- **Verwacht effect:** Data-gedreven beslissing; voorkomt voortijdige roer-omgooi.

### 7. Homepage entry-bounce monitoren — Drenthe-hub effect afwachten
- **Prioriteit:** **Midden**
- **Onderbouwing:** Entry bounce **67,4%** (138 sess); gem. duur **35 s** (was 61 s). Hub-sectie live sinds 26-05 — SEO en scroll-gedrag pas over 4–6 weken zichtbaar.
- **Actie:** Geen hero-CTA-wijziging. Juni-fetch: check of `#drenthe-hub` doorkliks oplevert (eventueel `navigation`-event toevoegen in latere cyclus). GSC: rang _vloerverwarming drenthe_ op `/`.
- **Verwacht effect:** Hub-sectie als SEO-anker; bounce kan dalen als bezoekers sneller stad-link vinden.

### 8. Heerenveen — juni-fetch afwachten, anders keyword pauzeren
- **Prioriteit:** **Laag**
- **Onderbouwing:** Geen dedicated pagina; keyword in Ads-defaults. Friesland **8 sess** (was 6). Drachten nog geen aparte entry in top-15.
- **Actie:** Na GSC-fetch: Drachten ≥1 organic sess? Heerenveen-rang? Zo niet: pauzeer `vloerverwarming heerenveen` in Ads óf plan pagina cyclus 15 — niet parallel met Assen-fix.
- **Verwacht effect:** Geen budgetlek naar pagina-loze keyword; discipline max. 1 city-pagina/sprint.

### 9. Device-breakdown toevoegen aan `ga4_fetch.py`
- **Prioriteit:** **Laag**
- **Onderbouwing:** Mobile **34%** van sessies; Assen-fix is mobiel-gedreven maar fetch geeft geen bounce/conv per device×landing.
- **Actie:** Volgende cyclus: extra query `dimensions=[deviceCategory, landingPagePlusQueryString]`, top 15 rijen.
- **Verwacht effect:** Sneller bewijs dat Assen-fix werkt op mobiel.

### 10. Conversie-definitie audit — dubbeltelling contact
- **Prioriteit:** **Laag**
- **Onderbouwing:** `/contact.html` landing: **3 sess / 9 conv.** — meerdere events per sess (`contact_submit` + `lead_form_submit`?). Unassigned-ruis is kleiner geworden (1 sess).
- **Actie:** Analytics: in GA4 Admin controleren welke events als key events tellen; alleen `contact_submit` + `wizard_lead_submit` als harde leads (conform AGENTS.md).
- **Verwacht effect:** Schonere conv-cijfers per landing; betere vergelijking kanalen.

---

## Afgewezen / niet voorgesteld deze cyclus

- **`over-ons.html` ATF-CTA** — pagina heeft al hero-CTA's; geen entry in top-15 deze fetch. Afwachten juni.
- **Nieuwe pagina `vloerverwarming-drenthe.html`** — hub-sectie op `/` net live; thin-content-risico.
- **Budgetverhoging Ads >€2/dag** — Paid Search nog 0 conv.; eerst attributie + landing.
- **`logo-varianten.html` redirect** — 9 sess/90d; laag prio (sprint 13 afgewezen).

---

## Context volgende fetch (~22 juni 2026)

Harde checks:

- GA4 ↔ Ads gekoppeld? → herinterpreteer Direct vs Paid/Cross.
- GSC beschikbaar? → prijsindicatie CTR, Hoogeveen-rang, Drenthe-hub op `/`.
- `werkwijze.html` entry ≥11 sess (+20% t.o.v. 9 baseline)?
- `projecten.html` entry-bounce <90% bij ≥10 entry-sess?
- `vloerverwarming-assen.html` na layout-fix: bounce <70%, duur >5 s?
- `vloerverwarming-drachten.html` ≥1 organic sess?
- Paid Search: nog 0 conv. na attributiefix? → ad-level landing-mismatch.
- Facebook: conv. >0 na message-match kalender?
