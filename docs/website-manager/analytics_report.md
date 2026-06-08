# Analytics Rapport — 8 juni 2026 (cyclus 16)

**Periode:** `30daysAgo` t/m `today` (GA4 property `properties/534641753`; venster ca. 9 mei — 8 juni 2026)
**Databron:** `docs/website-manager/ga4_report.json`, **verse fetch** timestamp **`2026-06-08T06:05:51`** (door PM gedraaid)
**GSC:** nog steeds niet beschikbaar — SEO-doelen (CTR prijsindicatie, Heerenveen/Hoogeveen-rang, organische queries) blijven **niet te toetsen**.

**Vorige sprint effect (cyclus 15):** Deploy **`c284662`** live **07-06-2026 ~16:06**. Deze fetch (08-06 06:05) bevat dus **~14 uur post-deploy-verkeer** — eerste meting mogelijk, maar nog een **klein** post-deploy-sample (avond/nacht/weekend). Behandel de cyclus-15-toetsing hieronder als **eerste signaal**; hard oordeel pas bij de juni-fetch (~22 juni).

### Toetsing cyclus-15-meetdoelen

| Doel | Norm | Verse meting | Status |
| ---- | ---- | ------------ | ------ |
| (a) `prijsindicatie.html` entry-bounce | <45% bij ≥10 entry-sess | **66,7%** op **9** entry-sess | **NIET gehaald** — bounce omhoog (was 54,5%); sample <10 |
| (b) `projecten.html` bounce | <50% bij ≥10 sess | **60%** op 10 sess (pageview) | **NIET gehaald** — onveranderd t.o.v. 07-06 |
| (c) Paid Search conv. | ≥1 conv. (na GA4↔Ads + RSA-sync) | **1 sess, 0 conv.** | **NIET gehaald** — Paid Search-volume ingestort (11→1) |

Belangrijke nuance: de post-deploy-window is pas ~14 uur. De entry-cijfers voor prijsindicatie/projecten zijn nog grotendeels pre-deploy-verkeer. De **echte** test van de cyclus-15-fixes komt bij de juni-fetch.

---

## Kerncijfers

| Metric | Waarde (30d, 08-06) | Trend t.o.v. fetch 07-06 |
| ------ | ------------------- | ------------------------ |
| Sessies (som devices) | **149** (72 desktop + 59 mobile + 18 tablet) | ↓ **−26%** (201 → 149) |
| Actieve gebruikers (devices) | **129** | ↓ (168 → 129) |
| Homepage `/` sessies / bounce | **121 / 66,9%** | ↓ sess (145 → 121); bounce ↑ (64,8% → 66,9%) |
| Homepage `/` gem. duur | **48 s** | ↓ licht (50 s → 48 s) |
| `/prijsindicatie.html` (pageview) | **22 sess / 31,8% bounce / 100 s** | ↓ sess (31 → 22); bounce ↓ (35,5% → 31,8%); duur ↑ (73 → 100 s) |
| Totaal conversies (kanalen) | **35** (Cross-network 22 + Direct 13) | ↓ **−44%** (63 → 35) |
| Direct | **42 sess / 13 conv.** (31% conv-rate) | ↓ sess (74 → 42); conv ↓ (41 → 13); **conv-rate gezakt 55% → 31%** |
| Cross-network `google/cpc` | **85 sess / 22 conv.** (26%) | = (onveranderd) |
| Paid Search `google/cpc` | **1 / 0 conv.** | ↓ **sterk** (11 → 1 sess); nog steeds 0 conv. |
| Organic Search `google/organic` | **9 / 0 conv.** | = |
| Facebook referrals (3 bronnen) | **7 / 0 conv.** | ↓ (20 → 7) |

**Weekly trend (sessies/week):**

| Week | Sessies | Opmerking |
| ---- | ------- | --------- |
| 20 – 26 apr | 8 | Aanloop |
| 27 apr – 3 mei | 172 | Campagne-piek |
| 4 – 10 mei | 75 | |
| 11 – 17 mei | 49 | |
| 18 – 24 mei | 56 | |
| 25 – 31 mei | 15 | Laag niveau |
| 1 – 7 jun | 16 | Stabiel laag |

De daling naar 149 sessies komt vooral doordat de campagne-piek-week (27 apr – 3 mei) deels uit het 30d-venster rolt. Onderliggend niveau blijft stabiel-laag: **~15–16 sess/week** de laatste twee volle weken (gelijk aan 07-06).

---

## Top pagina's

| Pagina | Sessies | Bounce | Gem. duur | Opmerking |
| ------ | ------- | ------ | --------- | --------- |
| `/` (Home) | 121 | **66,9%** | 48 s | 90d: 235 sess, 31 scrollers (13,2%) |
| `/prijsindicatie.html` | 22 | **31,8%** | **100 s** | Kroonjuweel; engagement gestegen (duur ↑) |
| `/contact.html` (nieuwe title) | 11 | **27,3%** | 30 s | Bounce iets op (was 12,5%); duur omlaag |
| `/projecten.html` | 10 | **60%** | 20 s | Onveranderd; 90d: 18 sess, 14 s, 2 scrollers |
| `/diensten.html` | 5 | **0%** | 32 s | Weinig volume |
| `/faq.html` | 5 | 20% | 13 s | Laag volume |
| `/over-ons.html` | 5 | 20% | 20 s | Geen entry-traffic |
| `/werkwijze.html` | 5 | **0%** | **266 s** | Zeer lange sessies; sterke engagement |
| `/prijsindicatie.html` (nieuwe title) | 3 | 33% | **866 s** | Diepe sessies bij betrokkenen |
| `/systemen-producten.html` | 3 | **0%** | 348 s | Lange sessies |
| `/vloerverwarming-assen.html` | 1 (+ 7 in 90d) | — | 5 s | 90d: **0,7 s**, **0 scrollers** — nog rood |

**Let op:** de oude contact-title variant ("Contact en offerte | VLWarmte", 76,9% bounce) komt **niet meer voor** in de top — die lijkt uit te sterven. Goed teken.

---

## Zwakste pagina's (hoge bounce / laag verkeer / lage engagement)

| Pagina | Signaal | Probleem |
| ------ | ------- | -------- |
| `/` als landing | 115 sess / **67,8% bounce** | Grootste instapper, hoogste verlies; bounce iets op t.o.v. 66,2% |
| `/prijsindicatie.html` als landing | 9 sess / **66,7% bounce** | Entry-bounce **omhoog** (was 54,5%); sample klein, deels pre-deploy |
| `/vloerverwarming-assen.html` | 90d **0,7 s** / **0 scrollers** op 7 sess | Layout-fix cyclus 14 nog geen effect in 90d |
| `/projecten.html` | 90d **14 s** gem. / 2 scrollers op 18 sess | Lage engagement; hero-verkorting nog niet gemeten |
| `/disclaimer.html`, `/privacy.html` | 90d 0 s / 0 scrollers | Funnel-ruis, geen actie |

---

## Landingspagina's (instappunten)

| Landing | Sessies | Bounce | Conv. | Opmerking |
| ------- | ------- | ------ | ----- | --------- |
| `/` | 115 | **67,8%** | **27** | Werkpaard; hoogste bounce onder grote instappers |
| `/prijsindicatie.html` | 9 | **66,7%** | **4** | Entry-bounce **omhoog** t.o.v. 54,5%; sample <10 |
| `/werkwijze.html` | 2 | 0% | **4** | Sterk conv-signaal; volume laag |
| `/contact.html` | 2 | 100% | 0 | Klein sample |
| `/projecten.html` | 2 | 50% | 0 | Sample te klein |
| `/contact.html?modus=offerte` | 1 | 100% | 0 | **Volume ingestort** (was 11 sess / 10 conv.) — Ads/social stuurt nauwelijks nog hierheen |
| `/diensten.html` | 1 | 0% | 0 | |
| `/over-ons.html` | 1 | 100% | 0 | |
| Facebook `fbclid` op `/` | 1 | 100% | 0 | Social cold traffic |
| Facebook `fbclid` op `/projecten.html` | 1 | 100% | 0 | Social cold traffic, verkeerde intentie |

**Belangrijk:** de gouden offerte-deeplink `/contact.html?modus=offerte` is teruggevallen van **11 sess / 10 conv.** naar **1 sess / 0 conv.** Dit volgt het instorten van het Paid Search-kanaal (11→1) — de campagne die hierheen stuurde lijkt vrijwel stilgevallen. **`fbclid` op `modus=informatie` is verdwenen**, maar nieuw is een `fbclid` op `/projecten.html` (100% bounce).

**Geen `gclid` zichtbaar** in entry-rapport — auto-tagging/attributielek staat nog open. Totaal `google/cpc`: **86 sessies** (85 Cross-network + 1 Paid Search).

---

## Traffic bronnen

| Kanaal | Sessies | Conv. | Conv. rate | Aanbeveling |
| ------ | ------- | ----- | ---------- | ----------- |
| Cross-network `google/cpc` | **85** | **22** | 26% | Onveranderd; alle betaalde conv. zit hier |
| Direct `(direct) / (none)` | **42** | **13** | **31%** | Conv-rate gezakt 55% → 31% — leak kleiner, of minder warm verkeer |
| Organic Search `google/organic` | **9** | **0** | **0%** | Mager; GSC nodig |
| Organic Social Facebook (3 vars) | **7** | **0** | **0%** | Volume gehalveerd; nog steeds geen leads |
| Cross-network `(data not available)` | **3** | **0** | — | Ruis |
| Unassigned `(not set)` | **3** | **0** | — | Attributie-gap |
| Paid Search `google/cpc` | **1** | **0** | **0%** | **Volume ingestort** — campagne lijkt vrijwel stil |

### Betaald verkeer — aanbevelingen Marketing Research Agent

1. **Paid Search ingestort: 11 → 1 sessie.** Het Paid Search-kanaal levert nu vrijwel geen verkeer meer. Cross-network (`google/cpc`) blijft stabiel op 85/22 — het meeste betaalde verkeer wordt daar geboekt. **Controleer of de campagne nog actief/gebudgetteerd is** (campagne `23834672782`): is budget op, gepauzeerd, of attributie verschoven naar Cross-network?
2. **Offerte-deeplink-verkeer verdwenen.** `/contact.html?modus=offerte` viel terug van 11/10 naar 1/0. Dit hangt direct samen met punt 1 — de RSA die hierheen stuurde draait niet meer of nauwelijks. Controleer live RSA final URLs en campagnestatus.
3. **`gclid` ontbreekt nog** — GA4 auto-tagging + Google Ads ↔ GA4-koppeling staat sinds sprint 14 open. Zonder dit blijft Paid Search-attributie onbetrouwbaar.
4. **Direct conv-rate 55% → 31%.** De gedaalde conv-rate kan betekenen dat het Ads-attributielek kleiner is geworden, óf dat de warmere (campagne-)bezoekers zijn weggevallen met het Paid Search-volume.
5. Geen budgetverhoging vóór de koppeling staat — maar **eerst uitzoeken waarom Paid Search-volume is ingestort** (P0).

---

## Geografie

| Regio | Sessies | Opmerking |
| ----- | ------- | --------- |
| Drenthe | **33** | Doelregio — sterk, maar omlaag (was 57) |
| Groningen | **24** | Doelregio — stabiel (was 23) |
| Friesland | **11** | Doelregio — stabiel (was 10) |
| **Noord-NL totaal** | **~68** | ~46% van 149 sessies |
| Noord-Holland | **25** | Buiten doel — organisch/betaald bereik |
| Zuid-Holland | **11** | Buiten doel |
| Noord-Brabant | **8** | Buiten doel |
| (not set) | **8 + 7** | Attributie-gap |
| VS (Colorado) | **4** | Bots/scanners |
| Duitsland (Nedersaksen) | **2** | Grensregio — klein |

Doelregio Drenthe + Groningen + Friesland = **68 sessies** (~46%) — aandeel gezond gebleven ondanks totale daling. Groningen en Friesland stabiel; Drenthe daalt mee met het wegvallende campagnevolume.

---

## Devices

| Device | Sessies | % | Trend |
| ------ | ------- | - | ----- |
| Desktop | 72 | 48% | ↓ (113 → 72) |
| Mobile | 59 | **40%** | ↓ licht (70 → 59), aandeel ↑ |
| Tablet | 18 | 12% | = |

Mobile-aandeel groeit naar **40%** — de cyclus-15 prijsindicatie wizard-ATF-fix (juist op mobile) blijft relevant; effect nog niet hard meetbaar.

---

## Observaties

1. **Totaal verkeer −26%, conversies −44%.** 149 sessies (was 201), 35 conv. (was 63). De daling komt grotendeels doordat de campagne-piek-week uit het 30d-venster rolt — maar de **conversie-daling is scherper dan de sessie-daling**, gedreven door wegvallend betaald verkeer.

2. **Paid Search-kanaal ingestort: 11 → 1 sessie.** Dit is het scherpste signaal deze cyclus. Het offerte-deeplink-verkeer viel mee terug (11/10 → 1/0). Wijst op een gepauzeerde/uitgeputte campagne of attributieverschuiving. **Vereist directe check door Marketing Research / PO** (campagne `23834672782`).

3. **Cyclus-15-meetdoelen (eerste signaal): geen gehaald, maar window is pas ~14 uur.** Prijsindicatie entry-bounce 66,7% (omhoog, sample 9), projecten 60% (onveranderd), Paid Search 0 conv. (volume weg). Te vroeg voor een hard oordeel — de fixes staan live, het post-deploy-verkeer is minimaal. IJkpunt blijft de juni-fetch.

4. **Prijsindicatie pageview-engagement verbetert wél.** Pageview-bounce 35,5% → **31,8%**, gem. duur 73 s → **100 s**, 90d-duur 106 s → **132 s**. Wie de pagina ópent blijft langer en scrollt dieper — positief signaal. Het probleem zit in de **entry** (koude instappers, 66,7%), niet in de pagina zelf.

5. **Werkwijze blijft sterkste conv-pagina per sessie.** Landing 2 sess / **4 conv.**, 0% bounce, gem. duur **266 s**. De cyclus-15 mid-page offerte-CTA past hierbij; volume blijft het knelpunt.

6. **Oude contact-title (77% bounce) lijkt uitgestorven.** Komt niet meer voor in top-pagina's — de title-update werkt na verloop. Geen actie meer nodig.

7. **Direct conv-rate gezakt 55% → 31%.** Minder warme (campagne-)bezoekers in Direct, óf kleiner attributielek. Hangt samen met het wegvallende Paid Search-volume.

8. **Facebook gehalveerd (20 → 7), nog steeds 0 conv.** `fbclid` op `modus=informatie` is verdwenen (goed), maar nieuw is een `fbclid` op `/projecten.html` met 100% bounce. Social blijft bezoekers zonder leads leveren.

9. **Assen onveranderd rood.** 90d: 7 sess, 0,7 s, 0 scrollers. Geen herstel zichtbaar. Afwachten tot juni-fetch, dan beslissen over hero-image/LCP.

---

## Content- & CTA-analyse (HTML, huidige staat)

| Pagina | CTA-sterkte | Opmerking |
| ------ | ----------- | --------- |
| `index.html` | Sterk | Hero: prijsindicatie + werkwijze; sticky mobile CTA offerte; Drenthe-hub met Assen-link |
| `prijsindicatie.html` | Sterk | `page-hero--wizard-entry`: wizard-stap 0 ATF op mobile (cyclus 15); pageview-engagement gestegen |
| `contact.html` | Sterk | Drie modi + direct bellen/WhatsApp; geen hero-CTA-overload |
| `werkwijze.html` | Verbeterd | Mid-page offerte-CTA (cyclus 15); sterkste conv-pagina per sessie |
| `systemen-producten.html` | Sterk | Laagopbouw-H2 + interne link naar prijsindicatie (cyclus 15) |
| `vloerverwarming-drachten.html` | Verbeterd | Heerenveen-H2 + body (cyclus 15) — Ads-landing voor Heerenveen-keyword |
| `diensten.html` | Matig | Eén primary (prijsindicatie); offerte pas onderaan — bewust |
| `projecten.html` | Verbeterd | Hero-lead verkort tot ~139 tekens (cyclus 15); bounce nog 60% — effect onbewezen |
| `over-ons.html` | Matig | Geen entry-traffic — laag prioriteit |
| `vloerverwarming-assen.html` | Verbeterd | Vroege CTA-band weg (cyclus 14); 90d-data nog rood |

**Lokale SEO:** Stad-pagina's aanwezig (Assen, Groningen, Leeuwarden, Zuidlaren, Drachten, Emmen, Hoogeveen). Heerenveen via de Drachten-pagina (discipline 1 city/sprint). Geen nieuwe gaps t.o.v. cyclus 15.

---

## Voorstellen voor Product Manager

### 1. Marketing Research: waarom is Paid Search-volume ingestort? (P0)
- **Prioriteit:** Hoog
- **Onderbouwing:** Paid Search **11 → 1 sessie**; offerte-deeplink `/contact.html?modus=offerte` viel terug van 11/10 conv. naar 1/0. Conversies totaal −44% (63 → 35). Cross-network onveranderd (85/22).
- **Actie:** Marketing Research Agent / PO — controleer campagnestatus `23834672782`: budget op, gepauzeerd, of attributie verschoven? Check live RSA final URLs en dagbudget. Herstel verkeer naar de proven offerte-deeplink.
- **Verwacht effect:** Paid Search-volume + offerte-deeplink-conv. terug op niveau; totale conv. herstelt.

### 2. GA4 ↔ Google Ads koppeling + auto-tagging afronden
- **Prioriteit:** Hoog
- **Onderbouwing:** Geen `gclid` in entry-rapport; Direct conv-rate 31% (13/42) bevat waarschijnlijk nog Ads-verkeer zonder label. Staat sinds sprint 14 open. Zonder koppeling is het Paid Search-instorten (#1) niet zuiver te diagnosticeren.
- **Actie:** PO/Admin — GA4 property koppelen aan Ads-account, auto-tagging aan, live RSA final URLs syncen. Geen developer-werk.
- **Verwacht effect:** Eerlijke Paid Search-rapportage; #1 zuiver te analyseren; meetdoel ≥1 Paid Search conv. testbaar.

### 3. Prijsindicatie: entry-bounce blijft het knelpunt
- **Prioriteit:** Hoog
- **Onderbouwing:** Pageview-engagement verbeterde (bounce 35,5% → 31,8%, duur 73 → 100 s) — de pagina zelf werkt. Maar **entry**-bounce ging **omhoog** naar 66,7% (9 sess). Koude instappers haken af vóór de wizard. De mobile-ATF-fix is pas ~14 uur live.
- **Actie:** Eerst meten bij juni-fetch (≥10 entry-sess nodig). Als entry-bounce >50% blijft: message-match van de bron (Ads/social) naar de pagina aanscherpen, niet de pagina zelf verder verbouwen.
- **Verwacht effect:** Entry-bounce <45% bij ≥10 entry-sess in juni-fetch.

### 4. Meet cyclus-15-fixes hard bij juni-fetch (monitoring)
- **Prioriteit:** Hoog (monitoring)
- **Onderbouwing:** Prijsindicatie mobile-ATF, projecten-hero, werkwijze mid-CTA staan live maar het post-deploy-sample is nog ~14 uur. Projecten onveranderd op 60%; prijsindicatie-entry omhoog. Te vroeg voor go/no-go.
- **Actie:** Bij juni-fetch toetsen tegen meetdoelen (prijsindicatie entry <45%, projecten <50% / >30 s). Pas dan bijsturen of afronden.
- **Verwacht effect:** Onderbouwde go/no-go per pagina.

### 5. Homepage entry-bounce verlagen voor groot instapverkeer
- **Prioriteit:** Midden
- **Onderbouwing:** `/` als landing: **115 sess, 67,8% bounce** (iets op t.o.v. 66,2%) — grootste instapper met meeste verlies, 27 conv.
- **Actie:** Marketing + Developer — stuur betaald verkeer naar offerte-deeplink/prijsindicatie i.p.v. `/` (zodra Paid Search hersteld is, #1). Geen hero-CTA-wijziging (cyclus 14 afgewezen) tenzij data na Ads-koppeling anders zegt.
- **Verwacht effect:** Minder bounce op grootste instapper; meer conv. via proven landings.

### 6. Assen follow-up — hero-image/LCP overwegen
- **Prioriteit:** Midden
- **Onderbouwing:** 90d nog **0,7 s** gem. duur, **0 scrollers** op 7 sessies. Layout-fix cyclus 14 toont nog geen herstel.
- **Actie:** Bij juni-fetch: als bounce >70% en duur <5 s blijft, hero-image optimaliseren (lichter bestand uit `beeldmateriaal/`) of LCP-check. Geen wijziging andere stad-pagina's.
- **Verwacht effect:** Bounce <70%, gem. duur >5 s, ≥1 scroller in 90d.

### 7. GSC OAuth afronden voor SEO-meetdoelen
- **Prioriteit:** Midden
- **Onderbouwing:** Organic Search **9 sess / 0 conv.**; GSC ontbreekt — CTR prijsindicatie, Heerenveen-rang op Drachten-URL en Drenthe-hub niet te toetsen (uitgesteld sinds sprint 13).
- **Actie:** PO — `secrets/gsc.env` + refresh token via `scripts/gsc_get_refresh_token.py` (`invalid_grant` oplossen).
- **Verwacht effect:** Query-level data voor SEO-voorstellen; Heerenveen-H2 onderbouwd.

### 8. Facebook message-match: één intentie per post (effect meten)
- **Prioriteit:** Midden
- **Onderbouwing:** Facebook gehalveerd (20 → 7 sess), **0 conv.** `fbclid` op `modus=informatie` verdween (goed), maar nieuw `fbclid` op `/projecten.html` (100% bounce).
- **Actie:** Social Media Agent — borgen dat posts naar offerte-deeplink/prijsindicatie linken (niet naar projecten/informatie als koude instap). Eén CTA per post.
- **Verwacht effect:** Social conv. > 0 of lagere bounce op social-entries.

### 9. Direct-attributie monitoren na Ads-koppeling
- **Prioriteit:** Laag
- **Onderbouwing:** Direct conv-rate zakte 55% → 31% (13/42). Onduidelijk of dit komt door kleiner attributielek of door wegvallend warm verkeer.
- **Actie:** Na GA4↔Ads-koppeling (#2) opnieuw lezen; geen actie tot dan.
- **Verwacht effect:** Zuiver beeld van Direct vs. betaald.

### 10. Heerenveen: dedicated pagina pas na GSC-bewijs
- **Prioriteit:** Laag (blokkeert op GSC)
- **Onderbouwing:** Heerenveen-H2 staat op Drachten-pagina als tijdelijke Ads-landing. Aparte pagina afgewezen (1 city/sprint; thin-content-risico).
- **Actie:** Na GSC-fetch — als Heerenveen-queries volume tonen op de Drachten-URL: dan pas `vloerverwarming-heerenveen.html` overwegen of keyword herzien.
- **Verwacht effect:** Datagedreven keuze i.p.v. gokken; minder verspilde Ads-spend.

---

## Meetmoment volgende cyclus

- **Juni-fetch ~22 juni** — ijkpunt voor cyclus 13–15-meetdoelen met vol post-deploy-sample (Assen bounce/duur, prijsindicatie entry-bounce <45%, projecten bounce <50%, Paid Search conv.).
- **Paid Search hersteld?** → is de campagne weer actief, levert de offerte-deeplink weer conv.?
- **GSC beschikbaar?** → prijsindicatie CTR, Heerenveen-rang op Drachten-URL, hub op `/`.
- **GA4↔Ads gekoppeld?** → Paid Search conv. + Direct-attributie interpretabel.

---

*Rapport gegenereerd door Analytics Agent op basis van verse fetch (08-06 06:05). Geen website-wijzigingen doorgevoerd.*
