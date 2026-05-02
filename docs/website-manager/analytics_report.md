# Analytics Rapport — 2 mei 2026

**Periode:** laatste 30 dagen (GA4: `30daysAgo` → `today`)  
**Databron:** `docs/website-manager/ga4_report.json` (gegenereerd 2026-05-02T10:56:09)  
**Vorige sprint effect:** Homepage (`/`) laat **lagere bounce** (0,65) en **langere gemiddelde sessieduur** (~98 s) dan in het rapport van 1 mei (0,86 / ~84 s) — waarschijnlijk mix van UX/copy en extra FAQ-blok. `contact.html` en `over-ons.html` verbeteren eveneens op bounce t.o.v. eerdere export. Nieuwe URL **`/faq.html`** staat **nog niet** in de top-16 (normaal: net live / nog weinig volume).

---

## Kerncijfers

| Metric | Waarde | Toelichting |
| ------ | ------ | ----------- |
| Sessies (week in export) | 172 | `weekly_trend` met `week_start` 2026-04-25 |
| Actieve gebruikers (zelfde week) | 143 | |
| Traffic-kanalen (30 dagen, top) | Direct 150; Unassigned 18; Organic Social (Facebook) 17 totaal; Organic Search (Bing) 4 | Google organic blijft dun in deze bucket |
| Conversions (export) | o.a. 35 (direct), 8 (unassigned) | Custom events blijven funnel bruikbaar |

**Homepage-split:** `/` 76 sessies vs `/index.html` 15 — dubbele meetbaarheid blijft; canonical + interne links naar `/` blijven leidend.

---

## Top pagina’s (30 dagen)

| Pagina | Sessies | Actieve gebruikers | Gem. sessieduur (s) | Bounce (fractie) |
| ------ | ------- | ------------------ | ------------------- | ---------------- |
| `/` | 76 | 61 | ~98 | **0,65** |
| `/prijsindicatie.html` | 24 | 15 | ~292 | **0,33** |
| `/contact.html` | 20 | 16 | ~114 | **0,55** |
| `/over-ons.html` | 17 | 15 | ~49 | **0,53** |
| `/diensten.html` | 16 | 13 | ~154 | **0,75** |
| `/index.html` | 15 | 11 | ~1346* | **0,53** |
| `/werkwijze.html` | 13 | 12 | ~154 | **0,69** |
| `/systemen-producten.html` | 12 | 12 | **~4,5** | **0,67** |
| `/logo-varianten.html` | 9** | 7 | ~122 | **0,88** |
| `/vloerverwarming-groningen.html` | 7 | 7 | ~63 | **1,0** |
| `/projecten.html` | 7 | 7 | ~0,9 | **0,86** |

\*Extreme gemiddelde op `/index.html` wijst op enkele zeer lange sessies (tab open); mediana is waarschijnlijk lager — niet over-interpreteren.  
\**`logo-varianten.html` komt dubbel in ruwe export (deels als 404-titel); restverkeer blijft meetbaar.

---

## Landingspagina’s (instappunten)

| Landing | Sessies | Bounce | Conversions |
| ------- | ------- | ------ | ----------- |
| `/` | 56 | ~0,70 | 18 |
| *(leeg)* | 16 | **0,94** | 10 |
| `/index.html` | 11 | ~0,55 | 2 |
| `/prijsindicatie.html` | 11 | ~0,55 | 13 |
| `/diensten.html` | 10 | **0,90** | 0 |
| Overige o.a. contact, stadspagina’s, projecten | 6–8 | veelal 1,0 | laag |

**Datakwaliteit:** lege `landingPagePlusQueryString` blijft storend voor landingsanalyse — PM/Hans: segment in GA4 verfijnen.

---

## Traffic bronnen

| Kanaal | Sessies | Conversions |
| ------ | ------- | ----------- |
| Direct | 150 | 35 |
| Unassigned | 18 | 8 |
| Organic Social (Facebook) | 17 | 0 |
| Organic Search (Bing) | 4 | 0 |

---

## Apparaten & geo

- **Apparaten:** mobile 99, desktop 74 — mobiel blijft dominant.
- **Geo (sessies):** **Drenthe 116** — kernmarkt; Groningen NL 4; VS-sessies nog aanwezig (segment “NL + Drenthe/Groningen” voor lezen).

---

## Observaties

1. **Prijsindicatie en contact** — beide stijgen in sessies en hebben **relatief lage bounce**; dit zijn de sterkste commerciële routes na de home.
2. **`systemen-producten.html`** — veel sessies maar **zeer korte gemiddelde tijd (~4,5 s)** in deze slice: typisch “snel scan / geen tweede hit” of tab-weg; vraagt om **vroege, duidelijke CTA** naar prijsindicatie of FAQ.
3. **Stadspagina’s** — als **landingspagina** nog **bounce 1,0** en weinig tijd bij Assen; Groningen iets meer tijd. Interne doorverwijzing naar FAQ/wizard kan helpen naast bestaande hero-CTA.
4. **`projecten.html`** — dunne pagina, hoge bounce als landing; **vertrouwen + doorstroom** (naar prijsindicatie/FAQ) versterken tot echte cases binnen zijn.
5. **`logo-varianten.html`** — blijft in data; hosting/redirect blijft wenselijk, geen harde dev-prioriteit tenzij volume groeit.

---

## Voorstellen voor Product Manager

1. **Prioriteit: Hoog — Vroege CTA op `systemen-producten.html`**  
   - **Onderbouwing:** 12 sessies, gem. duur ~4,5 s — sterke hint op snelle exit.  
   - **Actie:** Direct onder de hero een compact CTA-blok (zelfde patroon als onderaan de pagina: prijsindicatie).  
   - **Verwacht effect:** meer `wizard_start` vanaf systemen-pagina.

2. **Prioriteit: Hoog — Interne links naar `faq.html` op drukke/supportpagina’s**  
   - **Onderbouwing:** FAQ is nieuw; nog geen meetpad in top-pages — indexering + interne links versnellen.  
   - **Actie:** Korte zinnen + links vanaf `diensten.html`, `projecten.html`, `contact.html` (en evt. `prijsindicatie.html` intro).  
   - **Verwacht effect:** sessies op `/faq.html`; lagere “orphan”-kans.

3. **Prioriteit: Midden — Stadspagina’s: doorstroom naar FAQ**  
   - **Onderbouwing:** 100% bounce als landing op Groningen/Assen in entry-tabel.  
   - **Actie:** Onder hero-CTA één regel met link naar `faq.html` (infrezen, warmtepomp, kosten).  
   - **Verwacht effect:** tweede hit-rate; langere sessies.

4. **Prioriteit: Midden — Home “4 stappen”: schuimbeton deeplink**  
   - **Onderbouwing:** USP-schuimbeton in stap 2 zonder link; sprint-deeplink `#schuimbeton` bestaat.  
   - **Actie:** Link `diensten.html#schuimbeton` op het woord schuimbeton in stap 2.  
   - **Verwacht effect:** betere interne verdeling en ankerverkeer.

5. **Prioriteit: Midden — `projecten.html` helderder maken als tussenstap**  
   - **Onderbouwing:** hoge bounce, weinig tijd.  
   - **Actie:** In hero-tekst expliciet verwijzen naar FAQ + prijsindicatie (één zin).  
   - **Verwacht effect:** minder doodlopende landingservaring.

6. **Prioriteit: Laag — Lege landing (16 sessies)**  
   - **Onderbouwing:** bounce ~0,94.  
   - **Actie:** GA4-exploratie (bron/medium/apparaat); geen sitecode tot oorzaak helder is.  
   - **Verwacht effect:** schonere rapportage.

7. **Prioriteit: Laag — `logo-varianten.html` resthits**  
   - **Onderbouwing:** 9 sessies in top_pages.  
   - **Actie:** 301/redirect via hosting indien mogelijk.  
   - **Verwacht effect:** schonere toplijst.

8. **Prioriteit: Laag — Search Console op “faq” en “vloerverwarming + plaats”**  
   - **Onderbouwing:** geen query-dimensie in JSON-export.  
   - **Actie:** over 2–4 weken impressies/CTR checken op nieuwe FAQ-URL.  
   - **Verwacht effect:** titel/description bijschaven op data.

---

## Data snapshot (top 5 sessies)

| pagePath | sessies |
| -------- | ------- |
| `/` | 76 |
| `/prijsindicatie.html` | 24 |
| `/contact.html` | 20 |
| `/over-ons.html` | 17 |
| `/diensten.html` | 16 |
