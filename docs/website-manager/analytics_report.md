# Analytics Rapport — 13 mei 2026

**Periode:** `30daysAgo` t/m `today` (GA4 property `properties/534641753`)  
**Vorige sprint effect:** Sprint cyclus 7 (live 11-05-2026) bracht o.a. kosten-sectie op `prijsindicatie.html`, pre-form op `contact.html`, hero op `projecten.html`, `noindex` op disclaimer/privacy en home trust-strip + sticky CTA. In deze **30-daags** export zijn disclaimer/privacy als landings nog zichtbaar (historische sessies + vertraging indexering). `prijsindicatie.html` als pagina presteert sterk (bounce ~30%); als **landing** is de bounce hoger (~60%) — waarschijnlijk mix van instappen halverwege de wizard.

**Data-fetch:** `.venv/bin/python scripts/ga4_fetch.py` — `docs/website-manager/ga4_report.json`, timestamp **`2026-05-13T09:08:07`**.

## Kerncijfers

| Metric | Waarde | Trend / context |
| ------ | ------ | ---------------- |
| Sessies (laatste volledige week in export) | 92 (week 6–12 mei) | week ervoor 29 apr–5 mei: **170** → **-45,9%** week-op-week; wel **herstel** t.o.v. de extreem lage week in het vorige rapport (~72) |
| Homepage `/` (30d pad) | 141 sessies, bounce **56,7%** | hoofdingang; engagement scroll 90d: 24 scrolled users op 141 sessies |
| Paid Search (`google / cpc`) | **13** sessies, **0** conversies | zelfde patroon: kanaal levert verkeer, conversies ontbreken |
| Cross-network (`google / cpc`) | **12** sessies, **0** conversies | naast Paid Search — in rapportage apart geclusterd |
| Unassigned `(not set)` | **2** sessies, **2** conversies | sterk verbeterd t.o.v. eerdere cyclus (21/15) — attributie iets schoner |

> GA4 telt sessies per dimensie; sommen over tabellen zijn indicatief. Trendrichting gaat voor.

## Top pagina's (30d, pagePath)

| Pagina | Sessies | Gem. sessieduur | Bounce |
| ------ | ------- | ---------------- | ------ |
| `/` | 141 | ~68 s | 56,7% |
| `/prijsindicatie.html` | 43 | ~95 s | **30,2%** |
| `/contact.html` (beide titels samen) | 50 | ~60 s | mix — zie landings |
| `/diensten.html` | 23 | ~75 s | 52,4% |
| `/werkwijze.html` | 20 | ~63 s | 40% |
| `/over-ons.html` | 19 | ~30 s | 38,9% |
| `/systemen-producten.html` | 17 | ~124 s | 46,2% |
| `/projecten.html` | 8 | **~7,5 s** | **75%** |
| `/vloerverwarming-groningen.html` | 8 | ~51 s | **87,5%** |
| `/vloerverwarming-assen.html` | 6 | **0 s** | **100%** |

## Zwakste signalen (landings + engagement)

| Landing / pad | Sessies | Bounce | Opmerking |
| --------------- | ------- | ------ | --------- |
| `/contact.html?modus=offerte` | 11 | **9,1%** | **10 conversies** — deeplink blijft de goudstandaard |
| `/contact.html` (zonder query) | 9 | 77,8% | 12 conversies (deels terugkerende gebruikers) |
| `/diensten.html` | 14 | **78,6%** | als landing: te weinig directe keuze boven de vouw |
| `/systemen-producten.html` | 9 | 77,8% | landers zoeken houvast; lange sessies op andere titelvariant, korte op vergelijk-pagina |
| `/projecten.html` | 6 | **100%** (entry) | hero-cyclus 7 staat kort in data; 90d scrolled users nog **1** op 8 sessies — nog monitoren |
| `/disclaimer.html` / `/privacy.html` | 7 + 6 | 100%, 0 s | `noindex` live — verwacht teruglopend |
| `/vloerverwarming-assen.html` | 6 | 100%, **0 s** | **0 scrolled users (90d)** — eerste viewport moet sterker (bewijs, beeld, vertrouwen) |

## Traffic bronnen (selectie)

| Kanaal | Source / medium | Sessies | Conversies |
| ------ | ----------------- | ------- | ---------- |
| Direct | `(direct) / (none)` | 211 | 82 |
| Paid Search | `google / cpc` | 13 | 0 |
| Cross-network | `google / cpc` | 12 | 0 |
| Organic Social | Facebook-varianten | ~30 | 0 |
| Organic Search | `google / organic` | 4 | 1 |
| Unassigned | `(not set)` | 2 | 2 |

## Geografie (top)

| Regio | Sessies | Doelregio? |
| ----- | ------- | ---------- |
| NL — Drenthe | 159 | Ja, kern |
| NL — Groningen | 11 | Ja — relatief laag volume |
| NL — Friesland | 4 | Ja — ondervertegenwoordigd |
| NL — North Holland | 19 | Buiten kern |
| VS (diverse staten) | ~28 totaal | waarschijnlijk ruis |

## Observaties

1. **Weekvolume blijft onder piek (170) maar herstelt licht** (92 vs eerder gemelde 72) — oorzaak van de dip nog steeds monitoren (Ads, index, tracking).
2. **Paid + cross-network samen ~25 sessies, 0 conversies** — conversiekoppeling en message-match blijven prioriteit (Marketing Research + Ads-scripts).
3. **`contact.html?modus=offerte` blijft extreem sterk** als landing (lage bounce, hoge conversies) — alle campagnes en social moeten deze URL blijven gebruiken waar offerte-intentie klopt.
4. **`vloerverwarming-assen.html` is een rode vlag** (0 s, 100% bounce, geen scroll) — technisch en inhoudelijk de eerste viewport scherper maken (zelfde principes als `projecten.html`-hero).
5. **`diensten.html` als landing verliest** (78,6% bounce) — keuzehulp met drie duidelijke paden helpt intentie-match.
6. **`systemen-producten.html` als landing** — korte verbinding naar prijsindicatie/offerte in de hero verlaagt doodlopende lezing.

## Aanbevelingen voor Marketing Research Agent

- **Google Ads:** campagne **`VLW-API-Leads NL auto`** staat **ENABLED** (check 13-05-2026). Bevestig budget, zoektermen, final URL’s per ad group en conversie-import — 0 conversies op betaald verkeer blijft het kernprobleem.
- **GA4 ↔ Ads:** auto-tagging, conversie-acties (`wizard_lead_submit`, `lead_form_submit`, `contact_submit`) en landings-URL’s nalopen tegen `.cursor/skills/google-ads-marketing/SKILL.md`.

## Voorstellen voor Product Manager

1. **Prioriteit: Hoog** — **Onderbouwing:** Assen-stadspagina 6 sessies, 0 s, 100% bounce, 0 scrollers (90d). **Actie:** Hero herschrijven met visueel bewijs + zelfde vertrouwen als projecten/home (werkgebied, 1 werkdag, buisgarantie), zonder city-template te breken. **Verwacht:** bounce <75%, sessieduur >20 s.

2. **Prioriteit: Hoog** — **Onderbouwing:** `diensten.html` landing bounce 78,6%. **Actie:** Eerste scherm **keuzehulp**: drie kaarten (compleet traject / schuimbeton-kern / aanleg systeem) met duidelijke doorklik naar `werkwijze`, `#schuimbeton`, `systemen-producten` + gedeelde CTA prijsindicatie. **Verwacht:** landingsbounce <65%.

3. **Prioriteit: Hoog (SEO + bereik)** — **Onderbouwing:** research backlog — Emmen binnen radius, geen stadspagina. **Actie:** Nieuwe pagina `vloerverwarming-emmen.html` (max. 1 nieuwe pagina deze sprint), zelfde kwaliteit als Assen/Groningen, footer + sitemap. **Verwacht:** eerste organische sessies + betere Ads-landing voor Emmen-termen.

4. **Prioriteit: Midden** — **Onderbouwing:** `systemen-producten.html` landing 77,8% bounce. **Actie:** Korte “als je via zoeken hier landt”-regel + **offerte**-CTA in hero naast prijsindicatie/FAQ. **Verwacht:** meer doorklik naar prijsindicatie en contact.

5. **Prioriteit: Midden** — **Onderbouwing:** Groningen-stadspagina 87,5% bounce. **Actie:** Eén **echte** projectfoto in eerste viewport (zelfde patroon als Assen/projecten), plus behouden CTA’s. **Verwacht:** bounce richting <75%.

6. **Prioriteit: Laag** — **Onderbouwing:** `projecten.html` entry nog 100% bounce op klein volume na hero-update. **Actie:** Na cyclus 8 opnieuw meten; eventueel tweede trust-element of FAQ-link in hero.

7. **Prioriteit: Laag** — **Onderbouwing:** disclaimer/privacy nog als landings in 30d-venster. **Actie:** Search Console URL-inspectie na `noindex`; geen extra dev tenzij Google blijft indexeren.

**Tone:** nuchter, direct, geen superlatieven — conform AGENTS.md.
