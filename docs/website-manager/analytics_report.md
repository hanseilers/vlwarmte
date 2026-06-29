# Analytics Rapport — 29 juni 2026 (cyclus 19)

**Periode:** 30 dagen (30 mei – 29 jun 2026), GA4 property `properties/534641753`, gegenereerd 2026-06-29
**Vorige sprint effect:** Cyclus 18 (22 jun) bouwde de Drenthe-provinciepagina, herschreef title/meta van home + Zuidlaren voor CTR, zette een "Richtbedrag in 2 minuten"-CTA boven de vouw op alle 7 stadspagina's, en legde exacte-ankertekst interne links. Effect is in deze GA4-data **nog niet meetbaar** — het verkeer is te laag (5 sessies de hele afgelopen week) en de GSC-data om CTR/posities te toetsen is verouderd (zie hieronder). De pagina's staan live en correct; het meten moet wachten op (a) herstel van het verkeer en (b) verse GSC-data.

> **GSC ontbreekt deze week.** `docs/website-manager/gsc_report.json` dateert van 23 mei 2026 (periode 25 apr – 22 mei) — de GSC-fetch is geblokkeerd (OAuth in autonome modus). Alle uitspraken over zoekposities/CTR hieronder zijn dus gebaseerd op 5 weken oude data en onder voorbehoud. De CTR-fix en internelinks van cyclus 18 kunnen pas getoetst worden zodra GSC ververst is.

---

## Kerncijfers

| Metric                    | Waarde (30d) | Trend                                          |
| ------------------------- | ------------ | ---------------------------------------------- |
| Sessies                   | 42           | ↓ zwaar — weektrend stortte in (zie hieronder) |
| Actieve gebruikers        | 40           | ↓                                              |
| Conversies                | 2            | ↓ (was 9 vorige cyclus, 35 cyclus ervoor)      |
| Conversies uit cpc        | 2 van 2      | 100% van conversies komt uit Google Ads        |
| Conversies uit organisch  | 0            | organisch levert al cycli lang nul             |
| Mobiel / desktop / tablet | 24 / 16 / 2  | mobiel blijft hoofdkanaal (57%)                |

### Weektrend (sessies per week)

| Week       | Sessies | Gebruikers |
| ---------- | ------- | ---------- |
| 4–10 mei   | 75      | 56         |
| 11–17 mei  | 49      | 42         |
| 18–24 mei  | 56      | 49         |
| 25–31 mei  | 15      | 14         |
| 1–7 jun    | 16      | 16         |
| 8–14 jun   | 15      | 13         |
| 15–21 jun  | **1**   | 1          |
| 22–28 jun  | **5**   | 5          |

Het verkeer is van ~49–75/week begin mei ingestort naar 1 (15 jun) en 5 (laatste week). De lichte opleving naar 5 valt samen met het terugkeren van betaald verkeer (cpc, 22 sessies / 2 conversies over 30d) — Google Ads lijkt **weer beperkt te draaien**, maar op een fractie van het oude niveau.

---

## Top pagina's (30d)

| Pagina                           | Sessies | Gem. duur | Bounce  |
| -------------------------------- | ------- | --------- | ------- |
| `/` (home, alle title-varianten) | 33      | wisselend | 0,14–1  |
| `/prijsindicatie.html`           | 8       | **307 s** | **25%** |
| `/contact.html`                  | 5+1     | 114 s     | 0%      |
| `/diensten.html`                 | 3       | 16 s      | 67%     |
| `/systemen-producten.html`       | 3       | 18 s      | 67%     |
| `/faq.html`                      | 2       | 47 s      | 50%     |
| `/over-ons.html`                 | 2       | 16 s      | 0%      |
| `/vloerverwarming-drachten.html` | 2       | 107 s     | 0%      |
| `/vloerverwarming-zuidlaren.html`| 2       | 39 s      | 0%      |

**`prijsindicatie.html` is opnieuw veruit de sterkste pagina:** 307 s gemiddelde sessieduur en 25% bounce — bezoekers die er komen, blijven en rekenen. Maar de pagina is **entry-punt voor slechts 3 sessies en levert 0 conversies** (wizard wordt wel gestart/gebruikt maar niet afgerond, of bezoekers haken na het richtbedrag af zonder offerte-aanvraag).

De home heeft één zwakke variant: title "Vloerverwarming Drenthe & Noord-NL — richtbedrag in 2 min" — 5 sessies, 7,4 s duur, **100% bounce**. Dit is de cyclus-18-title-herschrijving op één van de home-varianten; die trekt nu verkeer dat meteen weer wegklikt. Let op: dit kan ook ruis zijn (5 sessies).

## Zwakste pagina's (hoge bounce / lage betrokkenheid)

| Pagina                       | Sessies | Gem. duur | Bounce | Signaal                        |
| ---------------------------- | ------- | --------- | ------ | ------------------------------ |
| `/` (Drenthe-title-variant)  | 5       | 7,4 s     | 100%   | mismatch verwachting/inhoud?   |
| `/diensten.html`             | 3       | 16 s      | 67%    | overtuigt niet, korte sessies  |
| `/systemen-producten.html`   | 3       | 18 s      | 67%    | idem                           |
| `/projecten.html` (90d-data) | 18      | 14 s      | —      | structureel zwak; foto's nodig |

In de 90d-engagementdata vallen `projecten.html` (14 s), `over-ons.html` (28 s) en `faq.html` (22 s) op als pagina's waar bezoekers niet blijven hangen. `werkwijze.html` (112 s) en `systemen-producten.html` (97 s) doen het in 90d juist goed.

## Traffic bronnen (30d)

| Kanaal         | Source/Medium              | Sessies | Gebruikers | Conversies |
| -------------- | -------------------------- | ------- | ---------- | ---------- |
| Cross-network  | google / cpc               | **22**  | 20         | **2**      |
| Direct         | (direct) / (none)          | 12      | 12         | 0          |
| Organic Search | google / organic           | 6       | 6          | 0          |
| AI Assistant   | chatgpt.com / ai-assistant | 1       | 1          | 0          |
| Unassigned     | (not set)                  | 1       | 1          | 0          |

**Alle conversie komt uit betaald (cpc).** Direct (12) en organisch (6) leveren samen nul conversies. Het betaalde kanaal is — net als vorige cycli — de enige werkende leadmotor, nu op laag volume (22 sessies, 2 conversies = ~9% conversieratio op cpc, wat op zich gezond is).

## Geografie (30d)

| Regio                   | Sessies | In doelregio? |
| ----------------------- | ------- | ------------- |
| Drenthe                 | 9       | ✅ kern        |
| (not set) NL            | 7       | NL            |
| Friesland               | 6       | ✅            |
| Groningen               | 5       | ✅            |
| Noord-Holland           | 4       | buiten        |
| Zuid-Holland            | 3       | buiten        |
| Duitsland (Nedersaksen) | 2       | grens         |
| Bangladesh / Canada     | 1+1     | ruis          |

De doelregio wordt goed bediend: **Drenthe 9, Friesland 6, Groningen 5** — samen 20 van de 42 sessies (48%) zit in Noord-Nederland, plus 7 (not set) NL. De geo-targeting van het betaalde kanaal lijkt op orde. Randverkeer (NH/ZH 7 sessies, buitenland 4) is beperkt en grotendeels ruis.

---

## Observaties

1. **Het verkeer is bijna dood, maar het betaalde kanaal komt voorzichtig terug.** Van 75/week (begin mei) naar 1 (15 jun) en 5 (laatste week). De opleving valt samen met 22 cpc-sessies over 30d — Google Ads draait weer, maar op laag volume. Dit blijft de bottleneck: zonder verkeer is geen enkele on-page optimalisatie meetbaar.

2. **100% van de conversies komt uit cpc; organisch en direct leveren nul.** 2 conversies, beide uit Google Ads. De afhankelijkheid van het betaalde kanaal is totaal — exact het risico dat cyclus 18 al benoemde. De organische investeringen (Drenthe-pagina, internelinks) hebben nog geen leads opgeleverd, maar dat is ook niet te verwachten bij 6 organische sessies/30d.

3. **`prijsindicatie.html` overtuigt inhoudelijk (307 s, 25% bounce) maar converteert niet en krijgt te weinig instroom.** 3 entry-sessies, 0 conversies. De cyclus-18-CTA's op de stadspagina's moeten de instroom verhogen — nog niet zichtbaar bij dit lage volume. Belangrijker: zelfs wie de wizard gebruikt, vraagt geen offerte aan. Dit wijst op een **funnel-lek ná het richtbedrag** (geen duidelijke vervolgstap naar offerte/contact).

4. **Eén home-title-variant trekt verkeer dat 100% bounct** (Drenthe-title, 7,4 s, 5 sessies). Mogelijk een snippet/verwachting-mismatch van de cyclus-18-herschrijving, mogelijk ruis. Houd in de gaten; nog te klein om hard op te sturen.

5. **De doelregio wordt goed geraakt (Drenthe/Friesland/Groningen = 48%).** Geo-targeting cpc is op orde; het probleem is volume en funnel-afronding, niet het verkeerde publiek.

6. **GSC-blinde vlek.** De enige bron om de cyclus-18-SEO-ingrepen (CTR-fix, internelinks, Drenthe-pagina) te toetsen is GSC, en die data is 5 weken oud. We weten dus niet of "vloerverwarming drenthe" (was pos ~66) is bewogen of de top-3 zuidlaren-termen nu wél clicks krijgen.

---

## Voorstellen voor Product Manager (max 10, op prioriteit)

### 1. Funnel-afronding `prijsindicatie.html`: vervolgstap na het richtbedrag `[HOOG]`
- **Onderbouwing:** 307 s sessieduur / 25% bounce (sterkste pagina) maar 3 entry-sessies / **0 conversies**, ook in 90d (68 sessies, 0 zichtbare leads). Bezoekers rekenen wél maar vragen géén offerte.
- **Actie:** Direct na het getoonde richtbedrag een prominente, niet te missen vervolg-CTA ("Vraag vrijblijvend een offerte aan" / "Laat je terugbellen") richting `contact.html` met de juiste deep-link (`?modus=` / `#aanvraag`). Geen pop-up. Developer-taak.
- **Verwacht effect:** eerste organische/direct-conversies; van 0 naar meetbaar op de best-converterende pagina.

### 2. Escaleren naar eigenaar — Google Ads volume verhogen (binnen spend-mandaat) `[HOOG]`
- **Onderbouwing:** cpc = 22 sessies / 2 conversies (100% van alle conversies), maar het volume is een fractie van begin mei. Conversieratio cpc ~9% is gezond; het probleem is té weinig impressies/klikken (dagbudget ~€2).
- **Actie:** **Eigenaar-beslissing, geen autonome dev-taak.** Bevestig dat campagne 23834672782 weer ENABLED is en beoordeel of het dagbudget omhoog mag nu de conversieratio gezond is. Zie ook aanbevelingen voor Marketing Research Agent hieronder.
- **Verwacht effect:** lineair meer leads bij gelijkblijvende ~9% conversieratio.

### 3. Onderzoek funnel-drop-off prijsindicatie-wizard (nu, niet uitstellen) `[HOOG]`
- **Onderbouwing:** voorstel 1 lost het symptoom op, maar we weten niet wáár bezoekers afhaken: bij `wizard_start`, na `calculator_result`, of bij `wizard_lead_submit`. 90d: 68 sessies op de pagina, 0 leads.
- **Actie:** Analytics-/dev-taak: lees de wizard-events per stap uit GA4 (event-funnel) zodat voorstel 1 gericht het juiste lek dicht. Dit kon vorige cyclus niet door te weinig instroom, maar 68 sessies/90d is genoeg voor een eerste signaal.
- **Verwacht effect:** weten welke stap het lek is i.p.v. blind een CTA toevoegen.

### 4. Title-variant home met 100% bounce verifiëren en zo nodig fixen `[MIDDEN]`
- **Onderbouwing:** home-variant "Vloerverwarming Drenthe & Noord-NL — richtbedrag in 2 min": 5 sessies, 7,4 s, **100% bounce**. Dit is de cyclus-18-herschrijving; mogelijk snippet-belofte ("richtbedrag in 2 min") die de home zelf niet direct waarmaakt boven de vouw.
- **Actie:** Controleer of de home boven de vouw de belofte uit de title direct inlost (zichtbare prijsindicatie-CTA bovenaan). Zo niet: CTA naar `prijsindicatie.html` prominenter maken, of title-belofte temperen. Klein volume — eerst bevestigen, niet overhaast.
- **Verwacht effect:** lagere bounce op betaald/organisch home-verkeer.

### 5. Direct-verkeer (12 sessies, 0 conversies) activeren `[MIDDEN]`
- **Onderbouwing:** 12 direct-sessies, nul conversies. Direct is vaak merkbekend verkeer (visitekaartje, mond-tot-mond, herhaalbezoek) met hoge intentie — dat het 0 oplevert wijst op een conversie-/CTA-probleem, niet op publiek.
- **Actie:** Zorg dat elke entry-pagina (home, contact, diensten) één heldere primaire CTA boven de vouw heeft. Deels al gedaan cyclus 17/18 op home/stadspagina's; controleer `diensten.html` (67% bounce, 16 s) en `contact.html`.
- **Verwacht effect:** eerste conversies uit direct-kanaal.

### 6. `diensten.html` en `systemen-producten.html` overtuigender maken `[MIDDEN]`
- **Onderbouwing:** beide 3 sessies, ~16–18 s, **67% bounce** (30d). Bezoekers haken snel af. In 90d doet `systemen-producten` het wel beter (97 s), dus mogelijk pagina-specifiek instappunt-probleem.
- **Actie:** Korte, concrete intro boven de vouw + duidelijke CTA naar prijsindicatie/contact; geen muur van tekst. Developer-taak, laag risico.
- **Verwacht effect:** lagere bounce, meer doorklik naar conversiepagina's.

### 7. GSC-fetch deblokkeren (eigenaar/infra) `[MIDDEN]`
- **Onderbouwing:** zonder verse GSC kunnen we de hele cyclus-18-SEO-inzet (Drenthe-pagina, CTR-fix, internelinks) niet meten. We sturen nu blind op organisch.
- **Actie:** Eigenaar: OAuth-refresh-token voor `scripts/gsc_fetch.py` aanleveren (zie `secrets/gsc.env.example`) zodat de fetch in de PM-cyclus draait. Geen dev-feature, wel blokkerend voor meting.
- **Verwacht effect:** organische voortgang weer meetbaar; voorstellen op feiten i.p.v. mei-data.

### 8. Wederkerige link prijsindicatie → contact met intentie-deep-link `[MIDDEN]`
- **Onderbouwing:** `contact.html` heeft 0% bounce en 114 s (sterke, intentievolle pagina) maar krijgt weinig instroom (5+1 sessies). De sterke prijsindicatie-pagina linkt nog niet gericht door.
- **Actie:** Samen met voorstel 1: gebruik de `?modus=offerte` / `#aanvraag` deep-links zodat wie via de wizard komt direct in de juiste contactmodus landt. Developer-taak.
- **Verwacht effect:** kortere weg van richtbedrag naar offerte-aanvraag.

### 9. `projecten.html` blijft geblokkeerd op beeldmateriaal `[LAAG]`
- **Onderbouwing:** 90d: 18 sessies, 14 s — structureel zwak. Randvoorwaarde (nieuwe bouwfoto's) is sinds mei niet ingevuld.
- **Actie:** Geen dev-werk tot foto's er zijn. Eigenaar: lever eindresultaat-vloer, verdeler-detail, teamfoto, Hoogeveen/Friesland-project in `docs/website-manager/social/input/` (blokkeert ook social).
- **Verwacht effect:** pas na aanlevering; nu geen actie.

### 10. AI Assistant-verkeer (chatgpt.com) signaleren, nog niet op sturen `[LAAG]`
- **Onderbouwing:** 1 sessie via `chatgpt.com / ai-assistant`. Klein maar nieuw kanaal; relevant om te volgen nu AI-antwoorden steeds vaker doorverwijzen.
- **Actie:** Nog niets implementeren. Volgende cycli monitoren of dit groeit; zorg dat schema/feitelijke inhoud (FAQ, prijsindicatie) goed leesbaar blijft voor LLM's.
- **Verwacht effect:** vroege signalering van een opkomend kanaal.

---

## Expliciete aanbevelingen voor de Marketing Research Agent (betaald kanaal / cpc)

Het cpc-kanaal is **de enige bron van conversies** (2 van 2) en levert ~9% conversieratio op 22 sessies — gezond, maar veel te laag in volume. Aandachtspunten voor het Ads-onderzoek deze cyclus:

1. **Volume is de bottleneck, niet kwaliteit.** Conversieratio cpc is gezond (~9%). Onderzoek of het dagbudget (~€2) de beperkende factor is en of opschalen binnen het spend-mandaat verantwoord is. Lever de eigenaar een onderbouwd budget-advies (verwachte extra leads bij gelijkblijvende ratio).
2. **Landingsafstemming klopt grotendeels — home + prijsindicatie zijn de bestemming.** De best-converterende on-site pagina is `prijsindicatie.html` (307 s, 25% bounce). Overweeg om cpc-verkeer (deels) rechtstreeks naar `prijsindicatie.html` te sturen i.p.v. alleen home, en meet of dat de conversie verhoogt. Stem dit af met voorstel 1 (funnel-afronding) — anders landt betaald verkeer op een pagina die nog 0 converteert.
3. **Geo-targeting is op orde** (Drenthe/Friesland/Groningen = 48% van verkeer). Geen verbreding naar NH/ZH nodig; die leveren ruis. Houd de campagne strak op Noord-Nederland.
4. **Conversiemeting GA4 ↔ Ads verifiëren.** 2 conversies zijn correct toegeschreven aan cpc — controleer of de conversie-import (GA4-conversies → Google Ads) volledig en zonder dubbeltelling loopt, zodat budgetbeslissingen op betrouwbare cijfers rusten. Zie `.cursor/skills/google-ads-marketing/SKILL.md`, sectie GA4 ↔ Ads.
5. **Bevestig campagnestatus.** GA4 suggereert dat de campagne (id 23834672782) weer beperkt draait. Verifieer ENABLED-status, budget-benutting en eventuele policy-/billing-rem in een sessie mét Ads-permissies of door de eigenaar.

---

## Context voor volgende sprint

- **Eerst meten zodra mogelijk:** GSC ververst (voorstel 7) → toets cyclus-18-SEO (Drenthe-pagina pos, zuidlaren-CTR, internelinks). Tot die tijd sturen we blind op organisch.
- **Conversie-hefboom van de week = funnel-afronding op `prijsindicatie.html`** (voorstel 1 + 3 + 8). Dit is de enige plek waar het schaarse verkeer wél engagement toont maar niet converteert — daar valt nu de meeste winst te halen, onafhankelijk van het verkeersvolume.
- **Betaald kanaal blijft levensader:** 100% van de conversies. Het volume-/budgetbesluit ligt bij de eigenaar; Marketing Research onderbouwt het advies.
- **Let op klein-volume-ruis:** bij 42 sessies/30d zijn enkelvoudige cijfers (100%-bounce-title, 1 AI-sessie) signalen, geen harde trends. Niet overhaast op sturen.
