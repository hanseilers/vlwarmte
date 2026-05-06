# Analytics Rapport — 6 mei 2026

**Periode:** laatste 30 dagen (GA4: `30daysAgo` → `today`)
**Databron:** `docs/website-manager/ga4_report.json` (gegenereerd 2026-05-02T10:56:09; 4 dagen oud)
**Fetch-status:** `python3 scripts/ga4_fetch.py` kon in deze sessie niet uitgevoerd worden — Bash-permissies in deze run staan geen Python-execution toe. Bestaande JSON is geanalyseerd conform fallback-instructie. PM/Hans: handmatig opnieuw runnen voor verse cijfers vóór sprintplanning.
**Vorige sprint effect:** Sprint 19 mei (uitvoer 2 mei avond) leverde concrete bouwsteentjes: vroege CTA op `systemen-producten.html`, FAQ-inlinks vanaf `diensten`/`projecten`/`contact`/`prijsindicatie`, FAQ-regel onder hero op de drie stadspagina’s en `schuimbeton`-deeplink op de home. **Effect in data is nog niet meetbaar** in deze JSON: het bestand is van 2 mei, vóór deployment-impact. Volgende fetch (na 12 mei) is het eerste echte meetmoment.

---

## Kerncijfers

| Metric | Waarde | Toelichting |
| ------ | ------ | ----------- |
| Sessies (week 25 apr → 2 mei) | 172 | enige beschikbare week in `weekly_trend` |
| Actieve gebruikers (zelfde week) | 143 | ratio 0,83 sessies/gebruiker |
| Sessies top-pagina (`/`, 30d) | 76 | dominant instappunt |
| Bounce homepage | 0,65 | net onder de 70%-grens |
| Direct vs. al-de-rest | 150 vs. 23 | merknaam-/lokaal-effect |
| Mobile vs. desktop | 99 vs. 74 | mobiel = 57% sessies |

**Trend t.o.v. vorige periode:** beperkt vergelijkbaar — `weekly_trend` bevat slechts één week (script-bug: loop start `i=0` overschrijft eerdere weken doordat `end_date - timedelta(weeks=i)` voor `i=0` gelijk is aan vandaag). Week-over-week conclusies zijn op deze data **niet hard te maken**; dit is in zichzelf een bevinding voor de developer.

---

## Top pagina’s (30 dagen)

| Pagina | Sessies | Gebruikers | Gem. duur (s) | Bounce |
| ------ | ------- | ---------- | ------------- | ------ |
| `/` | 76 | 61 | 98 | 0,65 |
| `/prijsindicatie.html` | 24 | 15 | **292** | **0,33** |
| `/contact.html` | 20 | 16 | 114 | 0,55 |
| `/over-ons.html` | 17 | 15 | 49 | 0,53 |
| `/diensten.html` | 16 | 13 | 154 | **0,75** |
| `/index.html` | 15 | 11 | 1346* | 0,53 |
| `/werkwijze.html` | 13 | 12 | 154 | **0,69** |
| `/systemen-producten.html` | 12 | 12 | **4,5** | **0,67** |
| `/logo-varianten.html` | 8 | 7 | 137 | **0,88** |
| `/projecten.html` | 7 | 7 | **0,9** | **0,86** |
| `/vloerverwarming-groningen.html` | 7 | 7 | 63 | **1,00** |
| `/vloerverwarming-assen.html` | 6 | 6 | 0 | **1,00** |
| `/disclaimer.html` | 7 | 7 | 0 | 1,00 |
| `/privacy.html` | 6 | 6 | 0 | 1,00 |

\*Waarde wordt vertekend door enkele zeer lange sessies (tab open). Niet over-interpreteren — de getalswaarde komt uit `pagePath="/index.html"` wat extra hits van interne tools/preview’s opvangt.

---

## Zwakste pagina’s — verkeer × gedrag

Pagina’s met substantieel verkeer (≥6 sessies) en bounce ≥0,67 of duur ≤30s:

| Pagina | Sessies | Bounce | Duur | Diagnose |
| ------ | ------- | ------ | ---- | -------- |
| `/systemen-producten.html` | 12 | 0,67 | **4,5s** | Bezoeker scant en is weg — sprint 19 mei adresseert dit met vroege CTA. |
| `/projecten.html` | 7 | 0,86 | **0,9s** | Dunne content, geen vertrouwenshaak. |
| `/diensten.html` | 16 | **0,75** | 154s | Bounce hoog ondanks redelijke tijd: bezoekers lezen, klikken niet door. |
| `/werkwijze.html` | 13 | 0,69 | 154s | Idem — eindstation. |
| `/vloerverwarming-groningen.html` | 7 | **1,00** | 63s | Lokale landing leest, maar geen tweede hit. |
| `/vloerverwarming-assen.html` | 6 | **1,00** | 0s | Geen interactie geregistreerd. |

---

## Landingspagina’s (instappunten)

| Landing | Sessies | Bounce | Conversions |
| ------- | ------- | ------ | ----------- |
| `/` | 56 | 0,70 | **18** |
| *(leeg)* | 16 | 0,94 | 10 |
| `/prijsindicatie.html` | 11 | 0,55 | **13** |
| `/index.html` | 11 | 0,55 | 2 |
| `/diensten.html` | 10 | 0,90 | 0 |
| `/over-ons.html` | 9 | 0,78 | 0 |
| `/contact.html` | 8 | **1,00** | 0 |
| `/werkwijze.html` | 6 | 1,00 | 0 |
| `/projecten.html` | 6 | 1,00 | 0 |
| `/systemen-producten.html` | 6 | 1,00 | 0 |
| `/vloerverwarming-groningen.html` | 6 | 1,00 | 0 |
| `/vloerverwarming-assen.html` | 6 | 1,00 | 0 |

**Conversiefunnel — kwantitatief:** prijsindicatie levert per session veruit de meeste conversions: `13/11 = 1,18 conv/sessie` versus home `18/56 = 0,32`. Direct verkeer naar contact als landing geeft **0 conversions** — de pagina wordt blijkbaar bereikt maar de aanvraagflow start niet vanuit die context. Dit is de scherpste lead-generatie kans in dit rapport.

---

## Traffic bronnen

| Kanaal | Sessies | Conversions | Conv-rate |
| ------ | ------- | ----------- | --------- |
| Direct | 150 | 35 | 0,23 |
| Unassigned | 18 | 8 | 0,44 |
| Organic Social — Facebook (totaal 4 referrers) | 17 | 0 | 0,00 |
| Organic Search — Bing | 4 | 0 | 0,00 |

**Observatie:** Google organic ontbreekt volledig in deze export. Twee mogelijke oorzaken: (a) GSC-koppeling levert geen organic-attributie hier, (b) reëel: de site krijgt nu nog vrijwel geen Google-clicks. Voor PM betekent dit dat lokale SEO (stadspagina’s, FAQ) **nog steeds onbewezen** is — alleen Direct draagt. Facebook-verkeer komt binnen maar converteert niet.

---

## Apparaten & geo

- **Apparaten:** mobile 99, desktop 74. Mobiel domineert maar minder zwaar dan landelijk gemiddelde.
- **Geo (NL):** Drenthe **116** sessies = doelregio. Groningen **4** is laag, gegeven dat er een eigen stadspagina is. Friesland en Overijssel ontbreken in de top-10.
- **Ruis:** Noord-Holland 12, Zuid-Holland 7 — buiten doelregio. VS-sessies (Colorado, Oregon, Iowa, NC, Virginia samen 23) zijn vrijwel zeker bot- of bouncerverkeer en moeten **uit het PM-segment**.

---

## Observaties

1. **Prijsindicatie is de motor van conversies** — 24 sessies, bounce 0,33, gem. 292s en **13 conversions** als landing op 11 sessies. Geen andere pagina komt in de buurt.
2. **Contact is een zwart gat** — 8 directe landingen, **bounce 1,00**, **0 conversions** als landing. Sterke disconnect tussen verwachting (call/aanvraag) en uitvoering. Deeplinks `?modus=` / `?tab=` / `#aanvraag` werden ingebouwd; de data toont nog geen onderscheid omdat de query-string niet in de pagePath-export staat.
3. **Stadspagina’s converteren niet** — drie pagina’s, alle drie 1,00 bounce als landing. Sprint 19 mei voegt een FAQ-link toe; zonder lokale projectcases blijft het waarschijnlijk dun.
4. **Google organic = nul in export** — alle SEO-werk landt momenteel onbewezen. Search Console-data is parallel kanaal, vereist apart.
5. **Drenthe domineert, Groningen nauwelijks aanwezig** — Drenthe 116 vs. Groningen 4 sessies. Stadspagina-strategie voor Groningen presteert nog niet.
6. **Facebook-verkeer 17 sessies, 0 conversions** — bron komt door, maar landingsflow vangt het niet op. Past bij observatie 2 (contact-flow).
7. **`weekly_trend` is kapot** — de loop in `ga4_fetch.py` levert maar één week. Trend-analyse is daardoor onmogelijk in deze export.

---

## Voorstellen voor Product Manager

### 1. `[Hoog]` Contact-landing repareren als conversiepad

- **Onderbouwing:** 8 directe landingen op `/contact.html` met bounce 1,00 en 0 conversions. Tegelijk: prijsindicatie levert 13 conversions op 11 landingen. Het verschil is overtuigend genoeg om hier prioriteit te geven.
- **Actie:** Bovenaan `contact.html` (boven de form) **direct zichtbare keuze** tussen: (a) bel nu, (b) WhatsApp/sms, (c) prijsindicatie eerst. Form blijft, maar is niet langer enige route. Test: clickable phone-link bovenaan voor mobile (57% sessies).
- **Verwacht effect:** ≥1 conversion uit contact-landing in volgende 30d-window; bounce <0,80.

### 2. `[Hoog]` `weekly_trend`-bug in `ga4_fetch.py` fixen

- **Onderbouwing:** Loop genereert `end_date = today - i*week` met start `i=0`, wat `start=today-7d, end=today` betekent voor i=0 en bij overlap één week wegschrijft. JSON-export bevat nu één week — week-over-week-analyse kan niet.
- **Actie:** In `scripts/ga4_fetch.py` regel ~198: loop herzien zodat acht **niet-overlappende** weken worden weggeschreven (gebruik `weeks=i+1` voor start, `weeks=i` voor end, of een datum-array vooraf).
- **Verwacht effect:** Trend-tabel in volgend rapport, kan groei/krimp pas aantonen.

### 3. `[Hoog]` Google Search Console naast GA4 ophalen

- **Onderbouwing:** Organic Google = niet zichtbaar in GA4-export. Sprint 19 mei zet vol in op SEO (FAQ-inlinks, deeplinks); zonder GSC-data is succes onmeetbaar.
- **Actie:** GSC API koppelen aan service account, fetch-script uitbreiden met top queries / pages / impressies / CTR voor `vlwarmte.nl`. Aparte JSON of toevoegen aan bestaande report.
- **Verwacht effect:** Eerste meetbare SEO-rapportage in 2-4 weken; vooral op `faq.html` en `vloerverwarming-{stad}` URL’s.

### 4. `[Midden]` `projecten.html` tijdelijk vermageren tot doorstroom

- **Onderbouwing:** 7 sessies, bounce 0,86, gem. 0,9s. Pagina is een dood spoor.
- **Actie:** Tot er echte projectfoto’s zijn: hero-tekst herschrijven naar één eerlijke alinea ("nog geen cases gepubliceerd, neem contact op voor referenties") + twee duidelijke knoppen (FAQ + prijsindicatie). Geen lege placeholders.
- **Verwacht effect:** Bounce <0,70; gem. duur >20s.

### 5. `[Midden]` GA4-segment opschonen: alleen NL + doelregio

- **Onderbouwing:** ~23 VS-sessies en 19 NL-sessies buiten doelregio (NH+ZH) vertroebelen alle bounce/duur-cijfers in deze export.
- **Actie:** In GA4 standaardrapport een PM-segment "Drenthe + Groningen + Friesland + Overijssel + NH/ZH" inrichten en `ga4_fetch.py` daar laten filteren via `dimensionFilter` op `region`.
- **Verwacht effect:** Realistischere bouncerates op stadspagina’s; betere besluitvorming.

---

## Bijlage — top 5 sessies snapshot

| pagePath | sessies |
| -------- | ------- |
| `/` | 76 |
| `/prijsindicatie.html` | 24 |
| `/contact.html` | 20 |
| `/over-ons.html` | 17 |
| `/diensten.html` | 16 |
