# Analytics Rapport — 11 mei 2026

**Periode:** `30daysAgo` t/m `today` (GA4 property `properties/534641753`)
**Vorige sprint effect:** Sprintcyclus 5 (week 18 mei 2026) is afgerond; sprintcyclus 6 (week 19 mei 2026) is goedgekeurd op 09-05-2026 maar nog niet in productie. De data in dit rapport vormen de **uitgangssituatie** voor sprintcyclus 6: trust-strip op home, consultative pre-form op contact, premium prijswizard, message-match paid landings en trackinghygiëne.

**Gebruikte data-fetch:** `.venv/bin/python scripts/ga4_fetch.py` — output in `docs/website-manager/ga4_report.json` met fetch-timestamp `2026-05-09T09:23:32`. Een verse fetch op 11-05 lukte niet in deze sessie (sandbox blokkeerde uitvoer); de data zijn 2 dagen oud, dus het 30-daags venster verschuift hooguit licht en de conclusies blijven leidend.

## Kerncijfers

| Metric | Waarde | Trend |
| ------ | ------ | ----- |
| Sessies (30d) | 258 (som top_pages) | week-op-week 171 → 72 (-57,9%) |
| Actieve gebruikers | 205 (som top_pages) | week-op-week 143 → 54 (-62,2%) |
| Gem. sessieduur | ~81 sec (gewogen) | beïnvloed door enkele pagina's met ~0 sec |
| Bouncepercentage | ~57% (gewogen) | meerdere landings boven 80% |
| Conversies (alle bronnen) | 74 (som traffic_sources) | Direct: 58, Unassigned: 15, Organic Search: 1 |

> Let op: GA4 telt sessies per dimensiecombinatie; absolute totalen wijken af van een eigen sommatie. Trendrichtingen zijn betrouwbaar, exacte percentages duiden indicatief.

## Top pagina's

| Pagina | Sessies | Gem. sessieduur | Bounce | Opmerking |
| ------ | ------- | --------------- | ------ | --------- |
| `/` | 112 | 73,3 sec | 62,5% | hoofdingang; 29 conversies als landing — sterk volume, bounce moet omlaag |
| `/prijsindicatie.html` | 37 | 130,3 sec | 37,8% | beste intent-pagina; 23 conversies als landing |
| `/contact.html` | 33 | 81,8 sec | 63,6% | volume oké, landings zonder `?modus=` performen slecht |
| `/diensten.html` | 21 | 81,5 sec | 52,4% | redelijke leestijd, maar landingsbounce 80% |
| `/over-ons.html` | 18 | 31,5 sec | 38,9% | korte leestijd; bouwt nauwelijks vertrouwen op |
| `/index.html` (los pad) | 17 | 314,4 sec | 35,3% | sessies via expliciete index.html — sterke engagement, klein volume |
| `/werkwijze.html` | 15 | 81,1 sec | 46,7% | redelijke pagina; 3 conversies als landing |
| `/systemen-producten.html` | 13 | 7,2 sec | 46,2% (top) / 100% (landing) | inhoud sluit niet aan op landingsintentie |

## Zwakste pagina's (hoge bounce / lage engagement)

| Pagina | Sessies | Gem. sessieduur | Bounce | Observatie |
| ------ | ------- | --------------- | ------ | ---------- |
| `/projecten.html` | 8 | 0,83 sec | 87,5% | bezoekers vertrekken vrijwel direct; geen vervolgstap zichtbaar |
| `/vloerverwarming-groningen.html` | 7 | 56,4 sec | 85,7% | citypage trekt regio binnen, maar haakt af voor CTA |
| `/vloerverwarming-assen.html` | 6 | 0 sec | 100% | landings zonder enige engagement — content of laadgedrag verdacht |
| `/disclaimer.html` (landing) | 7 | 0 sec | 100% | wordt als landing geserveerd; oneigenlijke instap |
| `/privacy.html` (landing) | 6 | 0 sec | 100% | idem; ruis in entry-data |
| `/logo-varianten.html` | 8 | 4,5 sec | 75% | restverkeer op oude/intern route, vervuilt rapportage |

## Traffic bronnen

| Kanaal | Source / Medium | Sessies | Actieve gebruikers | Conversies |
| ------ | --------------- | ------- | ------------------ | ---------- |
| Direct | `(direct) / (none)` | 190 | 146 | 58 |
| Unassigned | `(not set)` | 21 | 13 | 15 |
| Organic Social | `m.facebook.com / referral` | 13 | 13 | 0 |
| Organic Social | `facebook.com / referral` | 12 | 11 | 0 |
| Paid Search | `google / cpc` | 12 | 12 | 0 |
| Organic Search | `bing / organic` | 4 | 4 | 0 |
| Organic Social | `lm.facebook.com / referral` | 3 | 3 | 0 |
| Organic Social | `l.facebook.com / referral` | 2 | 2 | 0 |
| Organic Search | `google / organic` | 1 | 1 | 1 |

## Geografie

| Regio | Sessies | Doelregio? |
| ----- | ------- | ---------- |
| Netherlands — Drenthe | 147 | Ja, kerngebied |
| Netherlands — North Holland | 17 | Buiten doel |
| (geen waarde) | 14 | Onbekend — meetruis |
| United States — Oregon | 11 | Bot/proxy-verkeer (waarschijnlijk) |
| Netherlands — South Holland | 9 | Buiten doel |
| United States — Colorado | 8 | Bot/proxy-verkeer |
| United States — North Carolina | 5 | Bot/proxy-verkeer |
| Netherlands — Groningen | 4 | Ja, doel — laag volume |
| Friesland | niet in top 10 | Doel — ondervertegenwoordigd |

## Observaties

1. **Sessies vallen hard terug**: week 25 april–1 mei = 171 sessies, week 2–8 mei = 72 sessies (-57,9%). Dit is de scherpste trendbreuk. Oorzaak nog niet geïsoleerd: kan campagne-pauze, Search Console-issue, of tracking-regressie zijn (zie sprint Taak 5).
2. **Paid Search levert nul conversies**: 12 sessies via `google / cpc`, 0 conversies, terwijl Direct 58 conversies op 190 sessies haalt. Dit bevestigt de noodzaak van sprint Taak 4 (message-match op paid landings) en wijst op tracking- of mapping-gaten richting Google Ads.
3. **`contact.html?modus=offerte` werkt aantoonbaar beter** dan kale `contact.html` als landing: bounce 30% versus 88,9% bij vergelijkbaar volume (10 vs 9 sessies). Deeplinks zijn de juiste richting voor paid en interne CTA's.
4. **Citypages presteren slecht**: `vloerverwarming-groningen.html` 85,7% bounce, `vloerverwarming-assen.html` 100% bounce / 0 sec. De pagina's trekken doelregio binnen (Drenthe = 147 sessies), maar zetten dat niet om in interactie. Content of CTA in eerste viewport is te zwak.
5. **`projecten.html` is een lek**: 8 sessies, 0,83 sec gem. sessieduur, 87,5% bounce. Hero plaatst een algemene H1 en CTA naar prijsindicatie, maar bezoekers zien blijkbaar geen reden om door te scrollen — bewijs en concreetheid ontbreken bovenaan.
6. **Disclaimer en privacy als landings** (samen 13 sessies, 100% bounce, 0 sec) horen niet als instap te verschijnen. Dit duidt op verkeerde indexering of verkeerd geconfigureerde campagne-URL's; vervuilt entry-data.
7. **Unassigned kanaal** met 21 sessies en 15 conversies is opvallend: relatief veel conversies, geen kanaal-attributie. Dat ondergraaft besluitvorming over kanaalwaarde. Direct relevant voor sprint Taak 5 (trackinghygiëne).
8. **Logo-varianten-pagina** trekt nog 8 sessies (75% bounce). Vorige sprint (cyclus 5) had opschoning van logo-varianten als doel; effect is nog niet zichtbaar in deze 30-daags meting.

## Aanbevelingen voor Marketing Research Agent

Op basis van bovenstaande Paid Search / `gclid` / `google/cpc` signalen — zie `.cursor/skills/google-ads-marketing/SKILL.md` (sectie GA4 ↔ Ads):

- **Campagne-conversie-mapping controleren** in Google Ads: zijn de GA4-conversie-acties (form_submit, phone_click, prijsindicatie_complete) gekoppeld én "Conversions" geüpload? Nul conversies op 12 Paid Search sessies is ofwel tracking, ofwel intent-mismatch.
- **Landingsafstemming**: stuur intentcampagnes (kosten, offerte, schuimbeton) niet naar `/` maar naar `/prijsindicatie.html` of `/contact.html?modus=offerte#aanvraag`. Direct test op de twee URL's met dezelfde adgroup.
- **Searchterm-uitsluitingen**: controleer of er termen ranken die geen lead leveren (informatieve, niet-commerciële zoekwoorden of out-of-region).
- **GCLID-passering**: verifieer dat de gclid-parameter behouden blijft bij interne redirects en de URL-rewrites.

## Voorstellen voor Product Manager

1. **Prioriteit: Hoog**
   **Onderbouwing:** Week-op-week daling van 171 naar 72 sessies (-57,9%) zonder duidelijke oorzaak.
   **Actie:** Isoleer de oorzaak in één PM-checklist: (a) Google Ads campagne-status en budget op 1 mei, (b) Search Console crawl-/indexstatus, (c) eventuele GTM/GA4 wijziging, (d) verschuiving naar `Unassigned`. Plan dit als prerequisite voor sprint Taak 5.
   **Verwacht effect:** Oorzaak binnen 1 sprint scherp; gerichte hersteltaak voor Developer of Marketing Research Agent.

2. **Prioriteit: Hoog**
   **Onderbouwing:** Paid Search 12 sessies, 0 conversies — terwijl Direct 58 conversies op 190 sessies haalt. Dat is geen leadprobleem, het is een kanaalprobleem.
   **Actie:** Stuur Marketing Research Agent op: (a) GA4-Ads conversiekoppeling herstellen, (b) landings primair naar `prijsindicatie.html` en `contact.html?modus=offerte#aanvraag`, (c) searchterm-rapport doornemen voor uitsluitingen. Combineren met sprint Taak 4 (message-match).
   **Verwacht effect:** Eerste meetbare Paid Search conversies binnen 2–4 weken; betere CPA-zichtbaarheid.

3. **Prioriteit: Hoog**
   **Onderbouwing:** `projecten.html` heeft 8 sessies, 0,83 sec gem. sessieduur, 87,5% bounce. Bezoekers vertrekken voor ze scrollen.
   **Actie:** Herschrijf hero met (a) één concreet projectvoorbeeld (regio + werk + resultaat), (b) één visueel anker boven de vouw, (c) zachte CTA "Plan een opname" naast de primaire prijsindicatie-CTA. Past binnen tone-of-voice (concrete vakman-taal).
   **Verwacht effect:** Bounce naar onder 70%, gem. sessieduur naar minimaal 20 sec.

4. **Prioriteit: Hoog**
   **Onderbouwing:** Citypages (`vloerverwarming-groningen.html` 85,7% bounce, `vloerverwarming-assen.html` 100% bounce / 0 sec) trekken doelregio binnen maar converteren niet.
   **Actie:** Audit eerste viewport per citypage: harde regio-claim, reactietijd, contactnummer of WhatsApp-CTA direct zichtbaar. Verifieer ook of de Assen-pagina niet stuk laadt (0 sec sessieduur is een rode vlag).
   **Verwacht effect:** Bounce citypages naar onder 75%; ten minste 1 meetbare lead per maand uit citypage-verkeer.

5. **Prioriteit: Midden**
   **Onderbouwing:** Generieke `contact.html` als landing: 88,9% bounce. `contact.html?modus=offerte`: 30% bounce. Hetzelfde formulier, andere instap.
   **Actie:** Verifieer dat alle interne CTA's en advertenties deeplinks gebruiken (`?modus=offerte#aanvraag`, `?modus=informatie#aanvraag`, `?modus=bel#aanvraag`). Sprint Taak 2 (consultative pre-form) versterkt dit verder.
   **Verwacht effect:** Lagere bounce op contact-instappen; hogere formulierstart.

6. **Prioriteit: Midden**
   **Onderbouwing:** `diensten.html` 80% bounce als landing bij 15 sessies; pagina trekt verkeer maar verliest het.
   **Actie:** Maak eerste scherm een keuzehulp: "Welke dienst past bij jouw situatie?" met 3 cards (renovatie, nieuwbouw, schuimbeton) elk met directe doorklik. Past bij bestaande structuur, geen architectuurwijziging.
   **Verwacht effect:** Bounce naar onder 65%; meer doorstroom naar prijsindicatie.

7. **Prioriteit: Midden**
   **Onderbouwing:** `Unassigned` kanaal heeft 21 sessies en 15 conversies — relatief de hoogste conversieratio, maar zonder herkomst. Dat verbergt waar de waarde vandaan komt.
   **Actie:** In het kader van sprint Taak 5: controleer UTM-tagging op alle externe touchpoints (Facebook posts, e-mailhandtekening, partner-links). Documenteer in developer-rapport.
   **Verwacht effect:** Unassigned aandeel onder 5% van totaal binnen 4 weken; correctere kanaaltoewijzing.

8. **Prioriteit: Midden**
   **Onderbouwing:** `systemen-producten.html` heeft als landing 100% bounce bij 7 sessies — content sluit niet aan op landingsintentie.
   **Actie:** Beoordeel of deze pagina überhaupt als landing geserveerd moet worden. Zo nee: noindex of redirect intern. Zo ja: hero met direct vergelijkbare productspecificatie en CTA.
   **Verwacht effect:** Schonere entry-data of een nuttige landingspagina; geen wegglippend verkeer.

9. **Prioriteit: Laag**
   **Onderbouwing:** `disclaimer.html` en `privacy.html` worden 13× samen als landing geserveerd, 100% bounce, 0 sec. Dit is geen contentprobleem maar indexering.
   **Actie:** Plaats `<meta name="robots" content="noindex">` op beide pagina's; verifieer in Search Console dat indexering wordt teruggedraaid.
   **Verwacht effect:** Schonere entry-rapportages; geen meetruis meer op deze pagina's.

10. **Prioriteit: Laag**
    **Onderbouwing:** `logo-varianten.html` trekt nog 8 sessies (75% bounce) ondanks opschoning in sprintcyclus 5.
    **Actie:** Bevestig dat alle interne verwijzingen weg zijn en zet noindex + 410 of redirect naar `/`. Past in trackinghygiëne (sprint Taak 5).
    **Verwacht effect:** Verkeer naar `logo-varianten.html` daalt naar nul binnen 4 weken.
