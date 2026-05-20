# Marketing Research Rapport — 20 mei 2026

**Cyclus 11** — volledige update na cyclus-10-deploy (18 mei) en eerste projectinput in `beeldmateriaal/projecten/`.
**Scope:** leadgeneratie (organisch + betaald), landingskwaliteit, contentgaps, Google Ads message-match en besluitvorming rond echte projectcases.
**Bronnen:** `.claude/commands/marketing-research-agent.md`, `.cursor/skills/google-ads-marketing/SKILL.md`, WebSearch (mei 2026), `docs/website-manager/analytics_report.md` + `ga4_report.json` (export `2026-05-18T06:05:10`), site-HTML, `sitemap.xml`, `scripts/data/google_ads_lead_campaign_defaults.json`, `google_ads_list_campaigns.py` (verse run 20-05-2026).

## Samenvatting

Cyclus 10 heeft het **betaalde Friesland-lek** grotendeels gedicht: `vloerverwarming-drachten.html` is live (Drachten + Heerenveen in copy), staat in `sitemap.xml`, en `final_urls` in de Ads-defaults wijzen ernaar. De site gebruikt nu **site-breed** de bewezen offerte-deeplink (`contact.html?modus=offerte#aanvraag`). Het grootste resterende meetprobleem is **Paid Search zonder conversies** (13 sessies / 0 conv) terwijl Cross-network `google / cpc` wél 5 conversies op 29 sessies toont — dat vraagt GA4↔Ads-attributie en Final-URL-controle vóór opschalen, niet meer pagina’s.

De grootste **contentkans** is geen nieuwe stadspagina maar **echt bewijs**: twee verse cases (Zeegse 100 m² souterrain, Zuidlaren 50 m² draadstaalnetten) kunnen `projecten.html` van generieke placeholders naar vertrouwen voor de doelgroep tillen. **Aanbeveling:** publiceer beide cases zodra de product owner **expliciet akkoord** geeft op plaatsnamen en foto’s — **niet wachten** op een grotere case-bibliotheek; wel geen publicatie zonder dat akkoord.

## Top zoekwoorden (indicatief — WebSearch + site/defaults)

| Zoekwoord | Zoekvolume (indicatie) | Concurrentie | Pagina nodig |
|-----------|-------------------------|--------------|--------------|
| vloerverwarming kosten per m2 | hoog | hoog (aggregators) | bestaand — `prijsindicatie.html#kosten-uitleg` |
| prijs vloerverwarming / prijsindicatie | hoog | hoog | bestaand — `prijsindicatie.html` (wizard) |
| vloerverwarming groningen | hoog | hoog | bestaand — `vloerverwarming-groningen.html` |
| vloerverwarming assen | midden-hoog | hoog (aggregators + lokaal) | bestaand — `vloerverwarming-assen.html` (engagement zwak) |
| vloerverwarming drachten / heerenveen | midden | midden-hoog | bestaand — `vloerverwarming-drachten.html` (beide in copy) |
| vloerverwarming leeuwarden | midden | midden-hoog | bestaand — `vloerverwarming-leeuwarden.html` |
| vloerverwarming emmen / hoogeveen | midden | midden | bestaand — eigen pagina’s |
| schuimbeton vloerverwarming | midden | midden-hoog | bestaand — `diensten.html#schuimbeton`; concurrenten EcoFloorNoord, Bull Schuimbeton |
| vloerverwarming infrezen kosten | midden | midden | bestaand — FAQ/werkwijze; lokale infrezen-spelers (ComfortFloors, Nadergas) |
| vloerverwarming installateur [stad] | midden-hoog | hoog (Solvari, vloerverwarmingsinstallatie.nl) | city-cluster dekt kern; **meppel** nog gap |
| kruipruimte isoleren schuimbeton | midden | midden | bestaand — diensten |
| vloerverwarming renovatie houten vloer | midden | midden | **gap** — geen eigen landingspagina |
| vloerverwarming souterrain / kelder | laag-midden | laag-midden | **gap** — Zeegse-case dekt inhoudelijk; geen URL |
| vloerverwarming zuidlaren | laag-midden | laag | bestaand — `vloerverwarming-zuidlaren.html` + case-kans |

**Iteratie:** zoektermenrapport in Google Ads wekelijks; nieuwe varianten via `google_ads_campaign_negatives.json` en defaults-JSON. Juni-fetch (rond 1 juni) voor organische Drachten/Hoogeveen-sessies.

## Prijscalculator — haalbaarheidsonderzoek

### Conclusie

**Niet opnieuw bouwen.** De wizard op `prijsindicatie.html` is live, meet sterk (30d: ~50 sessies, ~104 s gem. duur, 30% bounce), en de crawlbare `#kosten-uitleg` (€45–€95/m²) dekt kosten-intent voor SEO. Vervolg = **meten en Ads-koppeling**, geen tweede calculator.

### Onderbouwing

- Concurrentie en aggregators (OfferteAdviseur, Vastlegg, 123Vloerverwarming, Verwarminginfo) bieden online rekenhulpen — dat bevestigt vraag, niet dat VLWarmte een generieke m²-calculator moet kopiëren.
- VLWarmte differentieert op **traject** (ondervloer, schuimbeton, kruipruimte-diepte) — dat past bij de bestaande wizard, niet bij een vlakke €/m²-tool.
- Juridisch: bestaande copy houdt vast aan “indicatie, geen offerte”; houten ondergrond stuurt bewust naar contact.

### Voorgestelde opbouw wizard

Geen wijziging voorgesteld deze cyclus. Bestaande flow: productkeuze → ondergrond → m²/diepte → bandbreedte → optioneel lead.

### Leadgeneratie koppeling

Blijf `wizard_calculate`, `wizard_lead_submit` en `lead_form_submit` als GA4-key events; import naar Ads na §A skill.

### Risico's en aandachtspunten

- Aggregators domineren brede “kosten”-SERP — win met **lokale stad + traject + echt projectbeeld**, niet met lagere claim-prijzen.
- Entry-bounce op `prijsindicatie.html` als landing blijft ~64,7% (17 sessies) — herbeoordelen na juni-fetch.

### Aanbeveling aan Product Manager

- **Prioriteit:** Laag (onderhoud)
- **Geschatte ontwikkeltijd:** 0 (alleen meting)
- **Verwacht effect op leads:** indirect via betere Ads-attributie en projectcases

## Content gaps (ontbrekende of zwakke pagina's/secties)

**Afgevinkt sinds cyclus 9–10:**
- ✅ Crawlbare kosten-sectie op `prijsindicatie.html`
- ✅ City-pagina’s Emmen, Hoogeveen, Leeuwarden, **Drachten/Heerenveen**
- ✅ Site-breed offerte-deeplink, `over-ons` vervolg-CTA, `projecten` ATF duo-CTA, interne links index/diensten

**Open gaps:**
- **`projecten.html` — inhoud, niet structuur:** ATF duo-CTA is live (cyclus 10), maar de pagina toont nog **drie generieke kaarten** (Groningen/Friesland/Drenthe) zonder echte plaats, foto uit de nieuwe projectmappen of technische details. Analytics: 8 sessies / 30d, **75% bounce**, entry **100%** bounce, ~7,5 s — inhoudelijke upgrade is de hefboom.
- **`vloerverwarming-meppel.html`:** keyword in defaults, geen URL — lagere prioriteit dan meet/Ads; pas na zoektermenrapport of organische vraag.
- **`vloerverwarming-renovatie-houten-vloer.html`:** commerciële twijfelvraag; wizard stuurt al naar contact — max. één nieuwe pagina per sprint.
- **`vloerverwarming-assen.html`:** 0 scrollers (90d), ~0,7 s gem. duur — hero-herontwerp backlog (juni-fetch).
- **`contact.html` zonder `?modus=`:** 80% bounce als landing; intent-strip nog geen effect na 3 dagen post-deploy — doorlaten tot juni-fetch.
- **Zeegse / souterrain:** geen city-pagina; case op `projecten.html` volstaat; eventueel één zin op `diensten.html` of FAQ over souterrain/kruipruimte.

## Concurrentie observaties (WebSearch, mei 2026)

**Wie rankt op kerntermen:**
- **Aggregators / lead-platforms:** Solvari, Slimster, vloerverwarmingsinstallatie.nl — domineren “installateur [stad]” en offertevergelijking; sterke op reviews en “tot 4 offertes”.
- **Lokale installateurs (Noord-NL):** Infloor (Groningen, frees in één dag), ComfortFloors (Groningen, infrezen €25–50/m² claim), Stef over de Vloer (Friesland/Groningen), Eric Haikens / Nadergas (Assen), D. Huberts (G/F/D).
- **Schuimbeton-combinatie:** Bull Schuimbeton, EcoFloorNoord — benadrukken “alles-in-één” en snelle oplevering; overlap met VLWarmte-traject maar vaak minder nadruk op **complete** particuliere woningrenovatie uit één regio.

**Wat zij beter doen:** brede prijsranges en calculators op content-sites; sterke lokale SEO-titels per stad; soms agressieve “binnen één dag”-beloftes.

**Waar VLWarmte kan winnen:** één aanspreekpunt ondervloer → schuimbeton → leidingwerk → dekvloer; **echte projectfoto’s** uit `beeldmateriaal/` (geen AI, conform skill); nuchtere bandbreedte i.p.v. schreeuwerige laagste prijs; offerte-deeplink met bewezen conversie.

## Google Ads — status en acties

**Verificatie 20-05-2026 (verse run, geen secrets in output):**

| id | channel_type | status | name |
|----|--------------|--------|------|
| 23834672782 | SEARCH | ENABLED | VLW-API-Leads NL auto |

**Defaults (`google_ads_lead_campaign_defaults.json`):**
- `final_urls` bevat o.a. offerte-deeplink, `prijsindicatie.html`, Leeuwarden, Hoogeveen, **Drachten** — keywords Drachten/Heerenveen hebben weer message-match.
- Geo: Drenthe, Groningen, Friesland — past bij playbook.
- RSA bevat “Referenties op aanvraag” in `extra_rsa` — na live projectcases copy aanpassen naar “Bekijk uitgevoerd werk” + link `projecten.html`.

| Onderwerp | Actie |
|-----------|--------|
| GA4 ↔ Ads | **P0** — Cross-network 5 conv / Paid Search 0 conv (GA4 18-05) wijst op attributie of URL-split; skill §A nalopen (link, auto-tagging, conversie-import). |
| Final URL's in live campagne | Bevestig in Ads UI of RSA’s de defaults-URL’s gebruiken; prioriteit offerte-deeplink voor koop-intent. |
| Negatives / zoektermen | Wekelijks zoektermenrapport; `google_ads_campaign_next_steps.py negatives` indien nodig. |
| Geo/keywords sync | `google_ads_update_campaign_geo.py` / `google_ads_add_keywords_from_defaults.py` na defaults-wijzigingen — alleen `--dry-run` dan `--apply` na PM-goedkeuring. |
| Spend | Campagne ENABLED — geen `--go-live` of budgetverhoging zonder expliciete spend-goedkeuring; geen opschalen vóór betrouwbare Search-conversies. |

## Echte projectcases — expliciete aanbeveling (publish vs wachten)

**Besluit voor PM:** **Publiceer, maar niet zonder akkoord.**

| Optie | Voor | Tegen |
|-------|------|-------|
| **Nu publiceren (na PO-akkoord)** | Sluit gat tussen “referenties op aanvraag” en site; versterkt Ads/organisch vertrouwen; past bij doelgroep (lokaal bewijs); slechts 2 cases is genoeg om **drie placeholder-kaarten te vervangen**; Zuidlaren-case versterkt thuisbasis + `vloerverwarming-zuidlaren.html`. | Privacy/AVG: plaatsnamen en werkbeelden op site/social vereisen expliciete toestemming. |
| **Wachten op meer cases** | Rijkere galerij later. | `projecten.html` blijft generiek; bounce/7,5 s blijft waarschijnlijk; RSA “referenties op aanvraag” blijft zwakker dan concurrenten met foto’s. |

**Aanbevolen uitvoering (developer-sprint na PO-akkoord):**
1. Vervang de drie generieke kaarten door **twee case-cards** (Zeegse, Zuidlaren) met README-metadata (m², ondergrond, oplossing in 3 regels).
2. Kopieer geoptimaliseerde WebP/JPEG naar `assets/img/projecten/` (niet zware WhatsApp-paden in HTML); bron blijft in `beeldmateriaal/projecten/`.
3. Hero: sterkste foto (bijv. Zuidlaren leidingwerk) i.p.v. oud root-beeld.
4. Cross-link Zuidlaren-case → `vloerverwarming-zuidlaren.html`; Zeegse → algemene Drenthe/Friesland-tekst (geen city-pagina nodig).
5. **Navigatie:** `projecten` terug in footer-regio of “Werk”-link op `over-ons`/`index` — **niet** per se hoofdnav tot er ≥3 cases zijn; **wel** `sitemap.xml` + `lastmod` bij publicatie voor SEO.
6. **Social/Ads:** één post met echt beeld (skill: `beeldmateriaal/`, geen AI); optioneel sitelink naar `projecten.html` na livegang.

**Tot akkoord:** item op `[WACHT]`; geen plaatsnamen op de live site.

## Aanbevelingen voor Product Manager (max. 8)

1. **Prioriteit: Hoog — GA4 ↔ Ads + Paid Search-attributie**
   **Type:** Meetplan + accountcontrole.
   **Onderbouwing:** 42 betaalde sessies / 30d; Paid Search 0 conv vs Cross-network 5 conv — opschalen zonder fix is blind varen.
   **Actie:** Skill §A (link, auto-tagging, conversies); in Ads UI controleren welke final URL’s de ENABLED Search-campagne (id 23834672782) daadwerkelijk serveert; rapporteer split Paid Search vs Cross-network.

2. **Prioriteit: Hoog — Projectcases publiceren na PO-akkoord**
   **Type:** Content/CRO + trust.
   **Onderbouwing:** Eerste echte input 20-05; placeholders ondermijnen “vakmanschap tonen”; analytics projecten blijft zwak.
   **Actie:** PO bevestigt publicatie Zeegse + Zuidlaren; developer vervangt placeholder-cards + hero; meet entry-bounce & scrollers in juni-fetch.

3. **Prioriteit: Hoog — Juni-meetronde cyclus 9–10 (geen premature bijsturing)**
   **Type:** Analytics-proces.
   **Onderbouwing:** 3 dagen post-deploy was ruis; nu ~5 dagen — nog steeds kleine volumes per landing.
   **Actie:** GA4-fetch rond 1 juni; hard beoordelen meetdoelen a–e (Drachten organisch, projecten bounce, cold contact, prijsindicatie entry, Assen scroll).

4. **Prioriteit: Midden — RSA/copy na projectcases**
   **Type:** Ads copy.
   **Onderbouwing:** `extra_rsa` headline “Referenties op aanvraag” is zwakker dan bewezen werk op de site.
   **Actie:** Na live `projecten.html` tweede RSA of headlines bijwerken (“Bekijk project in Zuidlaren”); geen `--apply` zonder dry-run + goedkeuring.

5. **Prioriteit: Midden — `vloerverwarming-assen.html` engagement**
   **Type:** UX/CRO.
   **Onderbouwing:** 0 scrollers 90d; aggregerende concurrentie op Assen-zoektermen.
   **Actie:** Bij uitblijvend effect juni-fetch: hero herontwerp (eerste contentblok + trust direct zichtbaar).

6. **Prioriteit: Midden — `over-ons.html` entry (cyclus 10 CTA live)**
   **Type:** Meting → eventueel bijsturing.
   **Onderbouwing:** 80% entry-bounce, 0 conv; vervolg-CTA net toegevoegd.
   **Actie:** Juni-fetch; pas bij geen verbetering extra trust-regel (werkwijze-link of één projectfoto).

7. **Prioriteit: Midden — `vloerverwarming-renovatie-houten-vloer.html`**
   **Type:** Nieuwe pagina (max. 1/sprint).
   **Onderbouwing:** commerciële intent; geen SERP-eigen URL.
   **Actie:** Volgende cyclus na projectcases + juni-data; kruislink wizard/contact.

8. **Prioriteit: Laag — `vloerverwarming-meppel.html`**
   **Type:** SEO/landing.
   **Onderbouwing:** keyword in defaults zonder URL; grens Drenthe/Overijssel.
   **Actie:** Alleen als zoektermenrapport of Search Console vraag toont; anders keyword tijdelijk pauzeren in Ads.

## Seizoenspatroon (indicatief)

Mei–augustus: verbouw- en offerte-intent, kostenvragen — sluit aan op live `#kosten-uitleg` en prijsindicatie. September–november: planning renovatie/warmtepomp; RSA pas roteren na 6–8 weken **betrouwbare** betaalde data post-attributiefix. Winter: comfort- en binnenklimaat-hooks bruikbaar in social, niet primair voor nieuwe Search-keywords.

---

**Tone:** nuchter, direct, conform AGENTS.md — geen overdreven claims. Geen secrets in dit document.
