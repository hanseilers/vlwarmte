# Analytics Rapport — 26 mei 2026

**Periode:** `30daysAgo` t/m `today` (GA4 property `properties/534641753`, 28-dagen-export 25 apr — 22 mei)
**Databron:** `docs/website-manager/ga4_report.json`, timestamp **`2026-05-23T10:37:33`** (3 dagen oud — fetch via venv niet mogelijk in deze sessie; sandbox blokkeerde `Bash`)
**Vorige sprint effect (cyclus 12):** Deploy `8fff9dd` ging live **22-05-2026**; laagopbouw-cluster (cyclus 12 addendum) **23-05-2026**. Beide volledig **buiten het GA4-meetvenster** (1–2 dagen post-deploy). Effect op `projecten.html` / `diensten.html`-hero-link / Drachten kruislinks / `#laagopbouw` is **niet meetbaar deze fetch** — juni-fetch (~15 juni) blijft de harde checkpoint.

---

## Kerncijfers

| Metric | Waarde (28d) | Trend t.o.v. fetch 22-05 |
| ------ | ------------ | ------------------------ |
| Sessies (som devices) | **352** (186 desktop + 150 mobile + 16 tablet) | +~3% (343 → 352) |
| Actieve gebruikers (top NL) | ~178 (Drenthe 124 + GR 19 + FR 6 + NH 29) | stabiel |
| Homepage `/` sessies / bounce | **202 / 60,9%** | +4 sess, bounce stabiel |
| Homepage `/` entry | 174 sess / **63,2%** / **47 conv.** | onveranderd |
| `/prijsindicatie.html` | **56 sess / 94 s / bounce 32%** | stabiel sterk |
| Direct verkeer | **223 sess / 90 conv.** | +1 sess |
| Cross-network `google/cpc` | **64 / 9 conv.** | +3 sess, +0 conv |
| Paid Search `google/cpc` | **13 / 0 conv.** | onveranderd — **P0 blijft** |
| Organic Search `google/organic` | **8 / 1 conv.** | stabiel mager |
| Facebook referrals (3 bronnen samen) | **32 / 0 conv.** | dorre kant |

**Weekly trend (sessies/week):**
- 25 apr – 1 mei: **171**
- 2 – 8 mei: **73**
- 9 – 15 mei: **48** (laagpunt)
- 16 – 22 mei: **57** (+19% w/w; herstel, maar nog ver onder 25 apr)

> Conclusie: het ‘piek-en-uitdoof’-patroon na week 25 apr ziet er campagne-gedreven uit (Cross-network 64 / Paid 13 in 30d, vrijwel alle conversies via Direct = post-click attributie-bug, zie verderop).

---

## Top pagina's

| Pagina | Sessies | Bounce | Gem. duur | Opmerking |
| ------ | ------- | ------ | --------- | --------- |
| `/` (Home) | 202 | 60,9% | 60,8 s | enige pagina met schaal; werkpaard |
| `/prijsindicatie.html` | 56 | **32,1%** | **94,4 s** | beste engagement — wizard werkt |
| `/contact.html` (incl. modus-varianten) | 53 (33+20) | 55% / **15%** | 54-78 s | offerte-deeplink trekt rustige bezoekers |
| `/diensten.html` (2 titels gecomb.) | 26 | 52-0% | 81 / 22 s | nieuwe Zuidlaren-titel-variant heeft 0% bounce op 5 sess |
| `/index.html` (legacy redirect) | 18 | 33% | **370 s** (bot/uitschieter) | 1 sess `index.html` direct, vermoedelijk gekruipte URL — laten staan |
| `/over-ons.html` (2 titels) | 22 | 35-25% | 31-56 s | als landing **80%** bounce — kloof tussen herhaalbezoek en koude entry |
| `/werkwijze.html` (2 titels) | 21 | 40-17% | 81 s | Zuidlaren-titel 17% bounce, **7 conv.** als landing — sterk |
| `/systemen-producten.html` (2 titels) | 18 | 46-20% | 7-384 s | Zuidlaren-titel 384 s = scroll & lezen; `#laagopbouw` net live |
| `/projecten.html` (Drenthe-titel + algemene) | 14 | 75-100% | **4,3 s gem.** | echt zwak — 1 scroller op 14 sess |
| `/vloerverwarming-groningen.html` | 8 | 75% | 50,6 s | 1 scroller; lokale-pagina-patroon zwak |
| `/vloerverwarming-assen.html` | 7 | **86%** | **0,7 s** | **0 scrollers** op 7 sess — bezoeker stuitert direct |
| `/faq.html` | 3 | n.v.t. | 35 s | 0 scrollers; te weinig instroom om hard te oordelen |

---

## Landingspagina's (instappunten)

| Landing | Sessies | Bounce | Conv. | Opmerking |
| ------- | ------- | ------ | ----- | --------- |
| `/` | 174 | 63,2% | **47** | het werkpaard — 27% conversie als entry |
| `/prijsindicatie.html` | 20 | 65% | **24** | conv. > sess = meerdere conv-events per sess (wizard + form) |
| `/diensten.html` | 15 | **73,3%** | 3 | onveranderd; hero-link effect nog niet meetbaar |
| `/contact.html?modus=offerte` | 11 | **9,1%** | **10** | gouden deeplink — bevestigt offerte-modus is sterk |
| `/contact.html` (koud) | 10 | 80% | 12 | koude entry — intent-strip-effect niet zichtbaar (klein sample) |
| `/index.html` | 10 | 40% | 0 | redirect-tijdperk, geen actie |
| `/over-ons.html` | 10 | **80%** | **0** | sprint-12 koos: geen ATF-CTA-wijziging — bevestigd zwak |
| `/systemen-producten.html` | 9 | **78%** | 0 | net `#laagopbouw` live; afwachten juni |
| `/werkwijze.html` | 9 | 67% | **7** | hoge conv. uit lage entry — landing-CTA werkt |
| `/projecten.html` | 7 | **100%** | 0 | 1 sess scrolt; cases live maar gefnuikt door entry-mismatch |
| `/vloerverwarming-assen.html` | 6 | **100%** | 0 | 0 scrollers / 0,7 s — pagina laadt en sluit direct |
| `/logo-varianten.html` | 7 | 86% | 0 | zou noindex-redirect moeten zijn — toch 7 entry-sess |
| `/disclaimer.html`, `/privacy.html` | 7 + 6 | 100% | 0 | footer-typ-verkeer; geen actie |
| `(not set)` | 9 | 100% | 0 | tracker-ruis |

---

## Traffic bronnen

| Kanaal | Sessies | Conv. | Conv. rate | Aanbeveling |
| ------ | ------- | ----- | ---------- | ----------- |
| Direct `(direct) / (none)` | **223** | **90** | **40%** | post-click attributie-bug (Ads klikken vallen in Direct als gclid niet gesync) — zie Marketing-blok |
| Cross-network `google/cpc` | 64 | 9 | 14% | PMax/Demand-mix? — pre-Ads-sessie inzoomen |
| Organic Social Facebook (3 vars) | 32 | 0 | **0%** | bezoekers wel, leads niet — landing-mismatch of cold |
| Paid Search `google/cpc` | **13** | **0** | **0%** | **P0** — zie Marketing-blok |
| Organic Search `google/organic` | 8 | 1 | 12% | héél laag bereik; GSC: vooral installateur/elektricien Zuidlaren-impressies (niet vloerverwarming) |
| Unassigned `(not set)` | 5 | 4 | 80% | grote conv. uit ruis — verdacht; check GA4 conversion-defs |
| Organic Search `bing/organic` | 4 | 0 | 0% | te klein |
| Cross-network `(data not available)` | 2 | 3 | 150% | privacy-modus / consentless attribution; conv. doortellen klopt |

---

## Geografie

| Regio | Sessies | Aandeel doelgroep |
| ----- | ------- | ----------------- |
| Drenthe (NL) | **174** | kern — past |
| North Holland (NL) | 36 | buiten doelgebied; Amsterdam-omgeving? |
| Groningen (NL) | 21 | doelgebied; ondervertegenwoordigd t.o.v. Drenthe |
| `(not set)` (NL of proxy) | 25 | tracker-ruis / privacy |
| South Holland (NL) | 18 | buiten doelgebied |
| **United States** (OR + CO + IA) | **29** | bots/proxies — niet meetellen |
| North Brabant (NL) | 9 | buiten |
| **Friesland (NL)** | **6** | doelgebied — Drachten/Heerenveen nog dor |

> Drenthe domineert (49% van NL-sessies); Friesland blijft de zwakke plek waar cyclus 12 op inzet (kruislinks + Drachten OG).

---

## Mobile vs Desktop

| Device | Sessies | Aandeel |
| ------ | ------- | ------- |
| Desktop | 186 | 53% |
| Mobile | 150 | **43%** |
| Tablet | 16 | 4% |

> Mobiel is bijna helft — hero/intent-strips moeten op telefoon ATF blijven. `vloerverwarming-assen.html` 100% bounce + 0 scrollers vraagt om mobiele inspectie.

---

## Betaald verkeer (Marketing Research Agent)

| Kanaal | Sessies | Conv. | Aanbeveling |
| ------ | ------- | ----- | ----------- |
| Cross-network `google/cpc` | 64 | 9 | **P1** Pre-Ads-sessie: welk campagnetype zit hierachter? Demand Gen / PMax? RSA-sync na PO. |
| Paid Search `google/cpc` | **13** | **0** | **P0** GA4 ↔ Ads sessie ~1 juni (zoals gepland in sprint). 13 sess / 0 conv = of conv-tag mist of landing past niet. Eerst tag-controle, dan landingsanalyse per ad. |
| Direct (vermoedelijk Ads-leak) | **223 / 90** | **P0** | 90 conv via "Direct" = klassiek attributiegat. Klikken zonder `gclid` of GA4-Ads-link valt in Direct. Zonder GA4 ↔ Ads link is **ROAS niet te lezen**. |

> **Hypothese:** zonder GA4-Ads-link en zonder `auto-tagging` op de Ads-account vallen alle Ads-conversies onder Direct. Dat verklaart de 40% conv-rate op Direct (onrealistisch hoog voor warm verkeer alleen). Onderbouwing: laagst-converterende kanalen (Paid Search 0/13, Facebook 0/32) hebben wél een logisch lage rate — dus de teller staat goed; de **attributie** is het probleem.

---

## Observaties

1. **Direct-kanaal vertekent het hele beeld.** 223 sess en 90 conv "Direct" is te hoog voor een nieuwe site zonder grote merkbekendheid. Vrijwel zeker rapporteert GA4 Ads-clicks die geen `gclid`-doorgifte hebben als Direct. **Conclusie:** alle conv-rate-vergelijkingen per kanaal staan op losse schroeven tot GA4 ↔ Ads-koppeling rond is. Dit is identiek het signaal van vorige fetch — sprint-12 stelde de fix terecht op ~1 juni.

2. **`/projecten.html` blijft het zwakste werkpaard.** 14 sess in 90 dagen, gem. duur **4,3 s**, **1 scroller**. Cyclus 11 cases en cyclus 12 kruislinks zijn live maar buiten meetvenster. Pas oordelen bij juni-fetch — maar als bounce/scroll niet verbetert, is de hero of het eerste scherm de oorzaak (niet de cases).

3. **`/vloerverwarming-assen.html` is technisch verdacht.** 7 sess in 90d, **gem. 0,7 s**, **0 scrollers**, 86% bounce, 0 conv. Dit lijkt geen content-probleem maar een laadprobleem of redirect-loop op mobiel — pagina laadt en bezoeker is meteen weg, geen scroll geregistreerd. **Voorstel:** handmatige check (devtools-throttling op 3G + iPhone-viewport) vóór nieuwe city-pagina’s.

4. **`/werkwijze.html` is een verborgen winnaar.** 9 entry-sess, 67% bounce, **7 conv.** = 78% conv-rate als landing (zelfs als helft Direct-bug is, blijft het sterk). Lijkt te conversie-leverend via diepere journey. **Voorstel:** intern verkeer naar werkwijze duwen vanaf `/diensten.html` en `/projecten.html` (nu loopt het andersom).

5. **Facebook 32 sess / 0 conv.** = social brengt nieuwsgierige bezoekers maar geen leads. Social cyclus 12 stuurde verkeer naar `projecten.html`/Drachten — exact de pagina’s met 100% bounce. **Hypothese:** message-match valt droog: feed-zin verkoopt project, landing toont gallerij zonder CTA hoog in beeld.

6. **Organic Search 8/1.** Bijna nul SEO-traffic. GSC laat zien dat top-impressies (`installateur/elektricien/installatiebedrijf zuidlaren`) niet vloerverwarming-intent zijn. Vloerverwarming-keywords scoren nog onder positie 10. Sprint-12 laagopbouw-cluster is de SEO-zet — verwacht effect pas over 4–8 weken.

7. **`/prijsindicatie.html` blijft kroonjuweel.** 56 sess / 94 s / 32% bounce / 24 conv. als landing. Wizard-route werkt. Bewaakt deze sprint geen wijzigingen — terecht.

8. **`/logo-varianten.html` lekt 7-8 sessies.** AGENTS.md zegt `noindex` redirect-stub naar `/`. Toch krijgt hij nog entry-verkeer (86% bounce). Mogelijk oude social-share-links of canonical-cache. Klein maar verspilt sessies.

---

## Voorstellen voor Product Manager (max. 10)

### 1. GA4 ↔ Google Ads koppelen — bevestigen voor 1 juni
- **Prioriteit:** **Hoog (P0)**
- **Onderbouwing:** Direct 223 sess / 90 conv staat haaks op Paid Search 13/0 en Cross-network 64/9. Vrijwel zeker attributiegat. Sprint-12 plande deze sessie al ~1 juni — bevestig deze week dat de afspraak staat.
- **Actie:** GA4 ↔ Ads link (UI: Admin → Product Links → Google Ads), auto-tagging aan in Ads, verificatie via `gclid` debug-view; daarna alle conv-rates herinterpreteren.
- **Verwacht effect:** Bruikbare ROAS-uitspraak per Ads-campagne; budget-beslissingen mogelijk.

### 2. `/vloerverwarming-assen.html` — handmatige mobiele inspectie
- **Prioriteit:** **Hoog**
- **Onderbouwing:** 7 sess in 90d, 0,7 s gem. duur, **0 scrollers**, 86% bounce. Dat is geen content-issue — bezoeker krijgt vermoedelijk niets te zien op mobiel of belandt op een 404/redirect-pad.
- **Actie:** Developer Agent: open `vloerverwarming-assen.html` op iPhone SE-viewport + Chrome devtools throttling 3G; check hero-rendering, JS-errors, CLS-spike. Vergelijk met `vloerverwarming-groningen.html` (8 sess, 50 s, 1 scroller — werkt wél).
- **Verwacht effect:** Concrete bug-diagnose óf bevestiging dat content moet veranderen vóór nieuwe city-pagina’s.

### 3. `/projecten.html` — hero-tweak na juni-fetch alleen bij bevestiging zwakte
- **Prioriteit:** **Midden** (uitgesteld tot juni-fetch)
- **Onderbouwing:** 14 sess 90d / 4,3 s / 1 scroller / 100% entry-bounce. Cyclus 12-kruislinks moeten eerst gemeten worden.
- **Actie:** **Geen aanpassing deze sprint.** Bij juni-fetch indien `bounce > 90%` of `scrolledUsers/sessions < 15%` blijft: hero-foto-cropping + eerste-scherm-tekst herzien (nu vermoedelijk te veel intro vóór de gallerij).
- **Verwacht effect:** Beslisbasis in juni; voorkomt voortijdige roer-omgooi.

### 4. Interne links `werkwijze.html` voeden — zacht uitbouwen
- **Prioriteit:** **Midden**
- **Onderbouwing:** 9 entry / 7 conv. = sterkste werkpagina na home/prijsindicatie. Maar krijgt nu weinig intern verkeer. Op `diensten.html` ontbreekt een prominente verwijzing en op `projecten.html` is werkwijze pas onderaan zichtbaar.
- **Actie:** Eén tekstlink (geen extra CTA-knop) in `diensten.html`-uitleg-blok: "Zo gaat het in z’n werk — bekijk de werkwijze." Idem in `projecten.html`-intro één zin met link.
- **Verwacht effect:** +20–30% internal-flow naar werkwijze; verwachte +2-4 extra conv./30d.

### 5. Facebook landing match — Drachten/projecten gericht maken
- **Prioriteit:** **Midden** (Social/Marketing-onderwerp, geen developer-werk)
- **Onderbouwing:** 32 Facebook-sess / 0 conv. Bezoekers komen via social-posts op `projecten.html` (100% bounce) en `vloerverwarming-drachten.html`. Feed-belofte (foto + zin) en eerste scherm op desktop/mobiel passen niet samen.
- **Actie:** Marketing Research Agent: review van social-kalender vs landing-hero copy. Geen wijziging op de pagina — wel content-match op Facebook-posts (zelfde foto, zelfde regel, expliciete CTA in caption “Bekijk de prijsindicatie”).
- **Verwacht effect:** Conv-rate Facebook van 0% naar 2–4%, ofwel 1-2 leads per 30 social-sess.

### 6. `/logo-varianten.html` — verifieer noindex-redirect
- **Prioriteit:** **Laag**
- **Onderbouwing:** 7 entry-sess, 86% bounce, 0 conv. AGENTS.md zegt: noindex redirect-stub naar `/`. Toch krijgt hij organic entry — vermoedelijk oude social-share of cache.
- **Actie:** Developer Agent: bevestigen `<meta name="robots" content="noindex">` + `<link rel="canonical" href="https://www.vlwarmte.nl/">` aanwezig; check `Disallow: /logo-varianten.html` in `robots.txt` (optioneel). Eventueel 301 op server-niveau via Pages-redirect-file als beschikbaar.
- **Verwacht effect:** 7–10 sess/30d teruggeleid naar `/` (lichte uplift homepage-conv).

### 7. GA4 conv-definitie audit — "Unassigned 5 sess / 4 conv"
- **Prioriteit:** **Laag**
- **Onderbouwing:** 80% conv-rate op een niet-toegewezen kanaal is verdacht; vermoedelijk dubbel-tellen of test-events.
- **Actie:** Analytics Agent (zelf, volgende fetch): kort overzicht maken van welke conversion-events GA4 telt (`contact_submit`, `wizard_lead_submit`, `lead_form_submit`, `wizard_calculate`, `calculator_result`). Voorstel: alleen `lead_form_submit` + `contact_submit` als hard "lead", rest als event.
- **Verwacht effect:** Schonere conv-cijfers; vergelijkingen kanalen kloppen.

### 8. Friesland-bereik — wacht op cyclus 12 effect, daarna pas Heerenveen-pagina
- **Prioriteit:** **Laag** (geblokkeerd tot juni-fetch)
- **Onderbouwing:** Friesland 6 sess (was 6 vorige fetch). Drachten-pagina staat live, cyclus 12 kruislinks net live. Heerenveen heeft geen pagina maar staat in Ads-keywords (zie AGENTS.md). Niet nóg een pagina bouwen vóór de huidige werkt.
- **Actie:** Juni-fetch afwachten. Indien Drachten ≥1 organic sess én Heerenveen-keyword nog hangt onder positie 10 in GSC: pas dán `vloerverwarming-heerenveen.html` plannen. Anders Heerenveen-keyword pauzeren in Ads.
- **Verwacht effect:** Discipline (max. 1 city-pagina per cyclus); voorkomt thin-content-stapel.

### 9. Mobiel-bouncepercentage breakdown — toevoegen aan ga4_fetch.py
- **Prioriteit:** **Laag** (script-onderhoud)
- **Onderbouwing:** Mobile 43% van sessies, maar de huidige fetch geeft geen mobile-vs-desktop bounce/conv per landing. Zonder die uitsplitsing blijft Assen-diagnose deels gokken.
- **Actie:** Volgende cyclus: extra block in `scripts/ga4_fetch.py` met `dimensions=[deviceCategory, landingPagePlusQueryString]`, `metrics=[sessions, bounceRate, conversions]`, top 15.
- **Verwacht effect:** Snel zien welke landings specifiek op mobiel falen — basis voor gerichte fixes.

### 10. Sessie-fetch automatiseren — geen GA4-fetch in deze sandbox-sessie mogelijk
- **Prioriteit:** **Laag** (operationeel)
- **Onderbouwing:** Bash was geblokkeerd in deze sessie (`don't ask mode`), waardoor `.venv/bin/python scripts/ga4_fetch.py` niet kon draaien. Rapport bouwt op data van 23-05. Geen drama — venster is hetzelfde — maar de fetch-stap viel uit.
- **Actie:** PM beslist of er een whitelist nodig is voor `.venv/bin/python scripts/ga4_fetch.py` in de analytics-agent-flow. Eenvoudige oplossing: PM draait fetch handmatig, dán pas analytics-agent triggeren.
- **Verwacht effect:** Volgende analytics-cyclus heeft sowieso verse data.

---

## Afgewezen / niet voorgesteld deze cyclus

- **`/over-ons.html` ATF-CTA** — sprint-12 expliciet doorgeschoven naar juni-fetch (80% bounce / 0 conv signaal aanhoudend, maar pas bijsturen ná juni-fetch).
- **`/diensten.html` hero retweak** — net live (22-05); pas oordelen bij juni-fetch.
- **Nieuwe city- of dienst-pagina’s** — discipline van max. 1 pagina per sprint; laagopbouw-cluster is cyclus 12’s grote zet.
- **RSA-`--apply`** — wacht op GA4↔Ads-koppeling + PO-akkoord.

---

## Context volgende fetch (~15 juni)

Harde checks die de juni-fetch moet beantwoorden:
- GA4 ↔ Ads gekoppeld? → herinterpreteer Direct vs Paid/Cross.
- `projecten.html`: bounce <90% op ≥10 entry-sess én ≥15% scrollers?
- `vloerverwarming-drachten.html`: ≥1 organic sess (cyclus 12 doel).
- `diensten.html` landing: bounce niet verslechterd t.o.v. 73% en ≥3 conv. behouden?
- `vloerverwarming-assen.html`: na mobiele inspectie — verbeterd of pagina-rebuild nodig?
- `#laagopbouw` op `systemen-producten.html`: ≥1 organic sess met query laagopbouw/droog in GSC?
- Paid Search `google/cpc`: nog steeds 0 conv. na attributiefix? → landing-/ad-mismatch i.p.v. tag-issue.
