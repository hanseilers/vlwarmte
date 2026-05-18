# Analytics Rapport — 18 mei 2026

**Periode:** `30daysAgo` t/m `today` (GA4 property `properties/534641753`)
**Databron:** verse export `docs/website-manager/ga4_report.json`, timestamp **`2026-05-18T06:05:10`** — dit is de **eerste meting ná de cyclus-9-deploy** van 15-05 (commit `d2bea47`). Data loopt nu ~3 dagen post-deploy.

**Vorige sprint effect (cyclus 9):** Te vroeg voor harde conclusies — 3 dagen post-deploy is binnen ruis. Alle vijf taken zijn opnieuw bevestigd live in de HTML (Hoogeveen-pagina + sitemap, prijsindicatie `#kosten-uitleg` boven wizard, contact-intent-strip, Assen-anker, projecten offerte-CTA). De vroege signalen op de vier meetdoelen zijn echter **vlak**: geen van de bounce-cijfers is meetbaar bewogen, geen organische Hoogeveen-sessies, Assen nog steeds 0 scrollers. Volledig oordeel pas bij de meting over 2–3 weken.

## Kerncijfers

| Metric | Waarde | Trend / context |
| ------ | ------ | ---------------- |
| Sessies laatste **volledige** week (11–17 mei) | **48** | week ervoor (4–10 mei) **75** → **−36%** wow; piekweek 27/4–3/5 was 172 |
| Actieve gebruikers (laatste volle week) | **41** | volgt sessiedaling |
| Homepage `/` (30d pad) | **164** sessies, bounce **57,3%** | gem. duur ~62 s; 26 scrolled users (90d) op 164 |
| `/prijsindicatie.html` (30d pad) | **50** sessies, bounce **30%** | gem. duur **104 s** — sterkste inhoudspagina |
| Direct | **215** sessies, **89** conversies | conversies vrijwel volledig uit Direct |
| Betaald totaal (`google / cpc`, beide groupings) | **42** sessies, **5** conversies | Cross-network 29 ses / **5 conv**; Paid Search 13 ses / **0 conv** |

> GA4 telt sessies per dimensie; sommen over tabellen zijn indicatief. Trendrichting gaat voor absolute optelsom.

## Top pagina's (30d, pagePath)

| Pagina | Sessies | Gem. sessieduur | Bounce |
| ------ | ------- | ---------------- | ------ |
| `/` | 164 | ~62 s | 57,3% |
| `/prijsindicatie.html` | 50 | **~104 s** | **30%** |
| `/contact.html` (beide titels) | 52 | ~58 s | mix — zie landings |
| `/diensten.html` | 21 | ~81 s | 52,4% |
| `/over-ons.html` | 18 | ~32 s | 38,9% |
| `/werkwijze.html` | 15 | ~81 s | 40% |
| `/systemen-producten.html` | 13 | ~7 s (hoofdtitel) | 46,2% |
| `/projecten.html` | 8 | **~7,5 s** | **75%** |
| `/vloerverwarming-groningen.html` | 8 | ~51 s | **75%** |
| `/vloerverwarming-assen.html` | 7 | **~0,7 s** | **85,7%** |

## Zwakste signalen (landings + engagement)

| Landing / pad | Sessies | Bounce | Conv. | Opmerking |
| --------------- | ------- | ------ | ----- | --------- |
| `/contact.html?modus=offerte` | 11 | **9,1%** | **10** | deeplink blijft de goudstandaard |
| `/contact.html` (zonder query) | 10 | **80%** | 12 | koud landen; intent-strip nog **geen** zichtbaar effect (3d post-deploy) |
| `/diensten.html` | 14 | **78,6%** | 0 | als landing; keuzehulp staat live — nog niet bewogen |
| `/over-ons.html` (entry) | 10 | **80%** | 0 | hoog als instappunt; weinig doorstroom |
| `/systemen-producten.html` (entry) | 8 | **75%** | 0 | als landing nog hoog |
| `/projecten.html` (entry) | 6 | **100%** | 0 | offerte-CTA cyclus 9 nog **geen** effect — kritiek blijven volgen |
| `/vloerverwarming-assen.html` (entry) | 6 | **100%** | 0 | **0 scrolled users (90d)**; lees-verder-link nog **geen** effect |
| `/prijsindicatie.html` (entry) | 17 | **64,7%** | **24** | bounce **ongewijzigd** vs 64% pre-deploy; conversiewaarde blijft hoog |
| `/disclaimer.html` / `/privacy.html` | 7 + 6 | 100%, 0 s | 0 | `noindex` live — historische landings/ruis |
| `/logo-varianten.html` | 7 | **85,7%** | 0 | stub-verkeer blijft binnenkomen — SEO-tech check nuttig |

## Traffic bronnen (selectie)

| Kanaal | Source / medium | Sessies | Conversies |
| ------ | ----------------- | ------- | ---------- |
| Direct | `(direct) / (none)` | 215 | 89 |
| Cross-network | `google / cpc` | 29 | **5** |
| Organic Social | `m.facebook.com / referral` | 13 | 0 |
| Paid Search | `google / cpc` | 13 | **0** |
| Organic Social | `facebook.com / referral` | 12 | 0 |
| Organic Search | `google / organic` | 7 | 1 |
| Organic Search | `bing / organic` | 4 | 0 |
| Organic Social | `l.`/`lm.facebook.com` | 6 | 0 |
| Unassigned | `(not set)` | 3 | 1 |

## Geografie (top)

| Regio | Sessies | Doelregio? |
| ----- | ------- | ---------- |
| NL — Drenthe | 164 | Ja, kern |
| NL — North Holland | 29 | Buiten kern |
| NL — Groningen | 16 | Ja — kern |
| NL — South Holland | 14 | Buiten kern |
| NL — Friesland | 4 | Ja — sterk ondervertegenwoordigd |
| VS (Oregon/Colorado/NC/Iowa) | ~30 | Ruis (bots/crawlers) |

## Cyclus-9 meetdoelen — eerste post-deploy stand (3 dagen)

| Meetdoel | Doel | Stand 18-05 | Oordeel |
| -------- | ---- | ----------- | ------- |
| (a) Organische sessies `vloerverwarming-hoogeveen.html` | >0 | **0** (pagina nog niet in top/entry/engagement) | Te vroeg — indexering loopt; herbeoordelen over 2–4 wk |
| (b) `projecten.html` landingsbounce | <90% | **100%** (6 ses) | **Geen effect** zichtbaar; volumes klein |
| (c) Cold `/contact.html` bounce | lager | **80%** (10 ses) | **Geen effect** zichtbaar |
| (d) `prijsindicatie.html` landingsbounce | <64% | **64,7%** (17 ses) | **Geen effect** zichtbaar; conversie blijft sterk (24) |
| (e) Assen scrolled users (90d) | >0 | **0** | **Geen effect** — Assen blijft het zwakste scherm |

## Observaties

1. **Cyclus 9 vertoont op 3 dagen géén meetbaar effect op de vier on-page meetdoelen.** Bounces op projecten (100%), cold contact (80%), prijsindicatie-entry (64,7%) en Assen-scroll (0) staan op of vlak bij de pre-deploy waarden. Dit is **verwacht** bij 3 dagen en lage volumes (6–17 sessies per landing) — het is nog ruis, geen falen. Hard oordeel pas bij de fetch over ~2 weken. De aanbeveling is niet "bijsturen" maar "doorlaten meten".
2. **Verkeer daalt week-over-week:** laatste volle week (11–17 mei) **48 sessies**, vorige week 75, piekweek 172. Sinds de piek eind april/begin mei zakt het volume drie weken op rij. De homepage trekt nog steeds het leeuwendeel (164/30d), maar het totale instroomvolume neemt af — relevant voor de PM: de kleine landing-volumes maken sprint-effecten traag meetbaar.
3. **Betaald: lichte verschuiving, maar Paid Search blijft op 0.** Cross-network `google / cpc` laat nu **5 conversies op 29 sessies** zien (was 0) — eerste teken dat de GA4↔Ads-koppeling deels werkt. Maar het label **Paid Search `google / cpc` blijft 13 sessies / 0 conversies**. Dat split-patroon (Cross-network converteert, Paid Search niet) wijst op een attributie-/labelingkwestie óf een landings-mismatch specifiek op de Search-campagnes. P0 voor Marketing Research.
4. **`prijsindicatie.html` is de sterkste inhoudspagina van de site:** 50 sessies, ~104 s gemiddelde duur, 30% pagina-bounce, en als entry 24 conversies op 17 sessies. De kosten-sectie-boven-wizard uit cyclus 9 schaadt de conversie in elk geval **niet**; de entry-bounce van 64,7% is het enige zwakke punt en moet over 2 weken opnieuw beoordeeld.
5. **`contact.html?modus=offerte` blijft de goudstandaard:** 9,1% bounce, 10 conversies op 11 sessies. Kale `/contact.html` als landing scoort onverminderd 80% bounce. De business case voor het overal hard doorlinken naar de offerte-deeplink is alleen maar sterker geworden.
6. **`over-ons.html` als instappunt is zwak:** 10 entry-sessies, 80% bounce, 0 conversies, en als pagina maar ~32 s gemiddelde duur (laagste van de inhoudspagina's). Wie hier binnenkomt haakt af. Kandidaat voor een duidelijke vervolg-CTA.
7. **Assen blijft het kritieke zwakke scherm:** ~0,7 s gemiddelde duur, 0 scrollers in 90d, 85,7%/100% bounce — ondanks de cyclus-9 lees-verder-link. Bij uitblijvend effect over 30d is een herontwerp van het eerste scherm onvermijdelijk.
8. **VS-verkeer (~30 sessies, korte duur) is ruis** en vertroebelt bounce-/conversie-aggregaten — onveranderd advies om een NL-only rapportagesegment of bot-filter te overwegen.

## Aanbevelingen voor Marketing Research Agent

- **Conversie-attributie Paid Search vs Cross-network (P0):** Cross-network `google / cpc` toont nu 5 conversies (29 ses), maar Paid Search `google / cpc` blijft op 0 (13 ses). Onderzoek dit split-patroon: is dit attributiemodel/auto-tagging, of landen Search-campagnes op een andere (slechtere) URL dan de converterende Cross-network/Demand-Gen-routes? Loop na tegen `.cursor/skills/google-ads-marketing/SKILL.md` (sectie GA4 ↔ Ads).
- **Final URL's:** zet betaalde offerte-/bel-campagnes op de bewezen deeplink `contact.html?modus=offerte#aanvraag` (9,1% bounce, 10 conv) — niet op kale `/contact.html` (80%) of generieke landings.
- **Search Terms review:** controleer of het Paid Search-verkeer op koop-/offerte-intentie zit; 13 sessies zonder enige conversie is verdacht voor informationele of brede match-termen.

## Voorstellen voor Product Manager

1. **Prioriteit: Hoog (Meten/Process)** — **Onderbouwing:** dit is de eerste post-deploy fetch (3 dagen na cyclus 9); volumes per landing zijn klein (6–17 ses) en geen meetdoel is bewogen. **Actie:** géén bijsturing op de cyclus-9-pagina's nu; plan expliciet een vervolg-fetch ~2 weken vooruit (rond 1 juni) en beoordeel meetdoelen a–e dan pas hard. **Verwacht effect:** beslissingen op signaal i.p.v. ruis.

2. **Prioriteit: Hoog (Conversie/Meting)** — **Onderbouwing:** Cross-network cpc converteert (5/29) maar Paid Search cpc blijft 0/13; 89 van ~95 conversies komen uit Direct. **Actie:** Marketing Research het Paid-Search-attributiegat en Final URL's laten verifiëren vóór nieuwe spend. **Verwacht effect:** betaalde Search-conversies zichtbaar of meetgat dichtgezet.

3. **Prioriteit: Hoog (CTA)** — **Onderbouwing:** kale `/contact.html` 80% bounce als landing tegenover `?modus=offerte` 9,1% / 10 conversies; patroon onverminderd. **Actie:** alle interne en externe verwijzingen met offerte-intentie hard naar `contact.html?modus=offerte#aanvraag` laten wijzen; cyclus-9 intent-strip-effect bij de juni-fetch beoordelen. **Verwacht effect:** lagere bounce op cold contact-instroom.

4. **Prioriteit: Midden (CRO)** — **Onderbouwing:** `over-ons.html` als entry 80% bounce, 0 conversies, ~32 s duur — zwakste inhoudspagina als instappunt, nog niet eerder geadresseerd. **Actie:** onderaan/over-ons een duidelijke vervolg-CTA toevoegen ("Bekijk prijsindicatie" / "Vraag offerte aan", deeplink). **Verwacht effect:** doorstroom van over-ons naar prijs/offerte i.p.v. afhaken.

5. **Prioriteit: Midden (SEO)** — **Onderbouwing:** Friesland 4 sessies vs Drenthe 164, ondanks doelregio; Hoogeveen nog niet geïndexeerd dus city-cluster heeft ruimte. **Actie:** na de Hoogeveen-evaluatie (juni-fetch) `vloerverwarming-leeuwarden.html` als volgende city-pagina activeren (backlog-item uit sprint.md). **Verwacht effect:** eerste organische Friesland-sessies binnen 4–8 weken.

6. **Prioriteit: Midden (CRO)** — **Onderbouwing:** Assen ~0,7 s duur, 0 scrollers 90d, 100% entry-bounce — lees-verder-link cyclus 9 toont na 3d (begrijpelijk) niets. **Actie:** bij de juni-fetch hard beoordelen; als nog steeds 0 scrollers, hero-concept Assen herontwerpen (kortere copy, eerste contentblok direct zichtbaar). **Verwacht effect:** >0 scrollers binnen 30d na bijsturing.

7. **Prioriteit: Laag (Datakwaliteit)** — **Onderbouwing:** ~30 VS-sessies + `disclaimer`/`privacy`/`logo-varianten` (alle 100%/85% bounce, 0 s) vervuilen aggregaten en verbergen echte trends in de kleine landing-volumes. **Actie:** NL-only rapportagesegment of internal/bot-filter in GA4; SEO-tech check op `logo-varianten.html` (redirect/`noindex`). **Verwacht effect:** schonere KPI's, betrouwbaardere sprint-evaluatie.

**Tone:** nuchter, direct, geen superlatieven — conform AGENTS.md.
