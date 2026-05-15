# Marketing Research Rapport — 15 mei 2026

**Cyclus 9** — volledige update.  
**Scope:** leadgeneratie (organisch + betaald), landingskwaliteit en contentgaps voor vlwarmte.nl in Noord-Nederland.  
**Bronnen:** `.claude/commands/marketing-research-agent.md`, `.cursor/skills/google-ads-marketing/SKILL.md`, `docs/website-manager/analytics_report.md` (export `2026-05-15T12:48:01`), site-HTML in de root, `scripts/data/google_ads_lead_campaign_defaults.json`, `scripts/data/google_ads_campaign_negatives.json`.  
**Zoekvolume/concurrentie in de tabel:** indicatief (hoog/midden/laag) — geen Keyword Planner-cijfers in deze cyclus.

**Google Ads — lokaal geverifieerd (15 mei 2026, repo-root, `.venv/bin/python`):** `google_ads_smoke_test.py` en `google_ads_list_campaigns.py` gedraaid. Resultaat: één zichtbare lead-campagne **`VLW-API-Leads NL auto`**, kanaal **SEARCH**, status **ENABLED** (numeriek id bekend bij beheer; niet nodig voor PM-prioriteit). Geen tokens of inhoud van `secrets/google-ads.env` in dit document.

> **Technische noot voor agents:** `python3` zonder geïnstalleerde `requirements-google-ads.txt` kan direct stoppen met “Install deps”; op deze machine slaagt dezelfde run wél met `.venv/bin/python`.

## Samenvatting

Het verkeer herstelt week-op-week (export: **100** sessies in de laatste volledige week vs **54** de week ervoor). Dat helpt met meten; de knel blijft **betaald**: **Paid Search** en **cross-network** (`google / cpc`) samen **33** sessies in 30 dagen met **0** conversies — dat wijst op **conversiekoppeling / import**, **auto-tagging** en/of **message-match** (welke landings krijgen de klik?) vóór opschalen van biedstrategie. Sterk blijft **`contact.html?modus=offerte`** (laag bounce, conversies in de export). Zwak blijven koude landings op **`contact.html` zonder query**, **`diensten.html`** en **`vloerverwarming-assen.html`** (weinig engagement); **`prijsindicatie.html`** is inhoudelijk sterk als pagina, maar als **landing** nog een **hogere bounce** — daar past **crawlbare kosten-uitleg** naast de wizard. **Friesland** blijft dun in sessies (**4** in 30 dagen); **Hoogeveen** en **Leeuwarden** ontbreken nog als indexeerbare city-URL. **`vloerverwarming-emmen.html`** staat live na cyclus 8; effect in 30d-aggregaten is nog beperkt zichtbaar.

## Top zoekwoorden

| Zoekwoord | Zoekvolume (indicatie) | Concurrentie | Pagina nodig |
|-----------|-------------------------|--------------|--------------|
| vloerverwarming kosten per m2 | hoog | hoog | bestaand (`prijsindicatie.html` + crawlbare prijs-/driver-sectie) |
| prijs vloerverwarming berekenen | hoog | hoog | bestaand (`prijsindicatie.html`) |
| vloerverwarming infrezen / infrezen kosten | midden | midden | bestaand (`faq.html`, `werkwijze.html`) — FAQ-structuur en interne links aanscherpen |
| schuimbeton vloerverwarming kosten | midden | midden-hoog | bestaand (`diensten.html#schuimbeton`, prijsindicatie) |
| kruipruimte isoleren schuimbeton | midden | midden | bestaand (`diensten.html#schuimbeton`) |
| vloerverwarming groningen | hoog | hoog | bestaand (`vloerverwarming-groningen.html`) |
| vloerverwarming assen | midden-hoog | hoog | bestaand (`vloerverwarming-assen.html`) — inhoud/ATF verder meten |
| vloerverwarming emmen | midden | midden-hoog | bestaand (`vloerverwarming-emmen.html`, nieuw live) |
| vloerverwarming hoogeveen / meppel | midden-laag (per stad) | midden | bestaand (`vloerverwarming-hoogeveen.html`, nieuw live) |
| vloerverwarming leeuwarden / drachten / heerenveen | midden (per stad) | midden-hoog | **gap** — Friesland structureel onderbediend |
| installateur vloerverwarming noord-nederland | midden | hoog | bestaand (`index.html`, `werkwijze.html`) |
| vloerverwarming nieuwbouw / renovatie | midden | midden-hoog | bestaand + FAQ; renovatie/hout als aparte URL nog zwak |
| vloerverwarming warmtepomp combinatie | midden | midden | bestaand (FAQ) — in city- en dienstcopy uitlichten |
| vloerverwarming renovatie houten vloer | midden | midden | **gap** — geen eigen landingspagina |

**Iteratie:** zoektermenrapport in Google Ads wekelijks tegen keywords en negatives in `google_ads_campaign_negatives.json` zetten; nieuwe varianten terug naar defaults-JSON via normale repo-flow.

## Prijscalculator — korte conclusie

**Doorontwikkelen, niet opnieuw bouwen.** De wizard op `prijsindicatie.html` blijft een duidelijke intentiepagina: in de 30d-export **46** sessies, gemiddelde sessieduur rond **84 s**, pagina-bounce **32,6%** — dat is vergeleken met veel andere landings gunstig. Wel: **als landingspagina** (entry) blijft bounce rond **64,7%** op **17** sessies — zoekers met “kosten”-intent missen waarschijnlijk **directe, indexeerbare uitleg** vóór of naast de wizard. Juridisch/commercieel: bandbreedte + expliciet “indicatie, geen offerte” vasthouden; meet **`wizard_calculate`**, **`wizard_lead_submit`** en **`lead_form_submit`** consequent in GA4 en spiegel naar Ads-conversies waar passend (zie skill §A).

## Content gaps (ontbrekende of zwakke pagina's/secties)

- **`prijsindicatie.html` — crawlbare prijs-sectie (ca. 200–400 woorden):** drivers (m², ondergrond, schuimbeton ja/nee), wat wél in een offerte zit, link naar FAQ/contact. Helpt SEO op “kosten”-termen én betaalde landings die hierop uitkomen.
- **`vloerverwarming-hoogeveen.html`:** logische volgende city na Emmen (corridor Drenthe, werkgebied-radius); sitemap, footer, kruislinks volgens patroon Emmen/Assen/Groningen.
- **`vloerverwarming-leeuwarden.html` (+ eventueel Drachten/Heerenveen later):** Friesland telt in GA4 nog weinig sessies; dedicated URL helpt Ads-keyword “Leeuwarden” en organische lokale intent.
- **`vloerverwarming-meppel.html`:** grens Drenthe/Overijssel; lagere prioriteit dan Hoogeveen/Leeuwarden tenzij zoektermenrapport anders zegt.
- **`vloerverwarming-renovatie-houten-vloer.html` (of zware FAQ-cluster met vaste URL):** commerciële twijfelvraag, nu vooral in wizard/FAQ verspreid.
- **`projecten.html`:** entry blijft zwak (hoge bounce, weinig scroll in eerdere exports); geen nieuwe “pagina”, wel **ATF**: compacter, één project + duidelijke duo-CTA (prijsindicatie + offerte-deeplink).
- **`diensten.html` als landing:** bounce blijft hoog in subset; keuzehulp staat kort live — **na 14–30 dagen** opnieuw beoordelen met nieuwe GA4-export.
- **`systemen-producten.html`:** mix snelle exit vs. diep vergelijken; boven de vouw **één duidelijke volgende stap** naar prijsindicatie of contact.
- **`contact.html` zonder `?modus=`:** koud landen blijft zwaar; intentie-keuze boven het modus-blok (zonder dubbel formulier).

Concurrentie in het algemeen (eerdere SERP-ervaring, deze cyclus geen diepe WebSearch): aggregators domineren brede “kosten”-termen; lokaal win je op **stad + traject uitleg + bewijs** (echte projectfoto’s uit `beeldmateriaal/` — geen AI-beelden voor campagnes).

## Google Ads — status en acties (samenvatting)

| Onderwerp | Actie |
|-----------|--------|
| Campagne | Lead-Search-campagne **ENABLED** — spend en optimalisatie alleen met expliciete budget-/strategie-afspraak (geen stille opschaling in dit rapport). |
| GA4 ↔ Ads | Link + **auto-tagging** nalopen (skill §A); anders blijft attribuutie van betaald naar conversies onbetrouwbaar. |
| Conversies | GA4-key events (`contact_submit`, `lead_form_submit`, `wizard_lead_submit`, `wizard_calculate`, …) afstemmen op wat Ads echt als conversie gebruikt; **0 conversies op betaald** is nu het kernprobleem naast landingskwaliteit. |
| Final URL’s | Offerte-intent: `https://www.vlwarmte.nl/contact.html?modus=offerte#aanvraag`; kosten/prijs: `prijsindicatie.html`; info/traject: `diensten.html` / `werkwijze.html` met secundaire CTA. |
| Keywords/negatives | Defaults en `google_ads_campaign_negatives.json` blijven leidraad; zoektermen → negatives en eventueel nieuwe phrase’s. |
| Geo | Provincies Drenthe/Groningen/Friesland in defaults blijven passen bij playbook; monitor “ruis” (bijv. buitenlandse sessies) in GA4. |
| Creatief | Search-RSA is tekst; bij toekomstig PMax: alleen beelden uit `beeldmateriaal/`. |

## Aanbevelingen voor Product Manager

1. **Prioriteit: Hoog — Google Ads + GA4**  
   **Type:** Meetplan + accountcontrole  
   **Onderbouwing:** 30d-export: **13** Paid Search + **20** cross-network sessies, **0** conversies.  
   **Actie:** GA4↔Ads-link, auto-tagging, conversie-import/-namen; landingsrapport “source/medium = google/cpc” per URL. Pas daarna biedstrategie verschuiven richting conversies.

2. **Prioriteit: Hoog — Crawlbare prijs-sectie op `prijsindicatie.html`**  
   **Type:** Content / SEO + paid landing  
   **Onderbouwing:** Sterke pagina, maar landingbounce op kosten-intent nog hoog; crawlbare tekst ontbreekt voor zoekmachines en snelle lezers.  
   **Actie:** 200–400 woorden + interne links; acceptatie: zichtbaar zonder wizard te starten, `wizard_calculate` blijft meetbaar.

3. **Prioriteit: Hoog — `vloerverwarming-hoogeveen.html`**  
   **Type:** Nieuwe pagina (max. één per sprint)  
   **Onderbouwing:** Emmen staat live; Hoogeveen is de volgende duidelijke city-gap in het werkgebied.  
   **Actie:** Zelfde patroon als bestaande city-pagina’s; sitemap/footer/links.

4. **Prioriteit: Hoog — `projecten.html` ATF**  
   **Type:** Content / CRO  
   **Onderbouwing:** Entry blijft zwak in analytics; weinig vervolgstap.  
   **Actie:** Eerste scherm compacter + primaire duo-CTA’s (prijsindicatie + offerte-deeplink) vóór zware galerij.

5. **Prioriteit: Midden — `contact.html` koude landing**  
   **Type:** UX / CRO  
   **Onderbouwing:** Hoog bounce zonder `?modus=`.  
   **Actie:** Korte intentie-keuze (info / offerte / bel) met links naar dezelfde tabs — geen dubbele formulieren.

6. **Prioriteit: Midden — `vloerverwarming-assen.html` engagement**  
   **Type:** UX  
   **Onderbouwing:** Nieuwe hero live; gemiddelde duur en scroll nog laag in export — eerst 14 dagen vol meten, daarna lichte ATF-aanpassing (anker/“lees verder”, compact trust) zonder zware LCP.

7. **Prioriteit: Midden — Friesland: start met `vloerverwarming-leeuwarden.html`**  
   **Type:** SEO / local landing + Ads message-match  
   **Onderbouwing:** Weinig Friesland-sessies; keyword Leeuwarden in defaults zonder passende URL.  
   **Actie:** Eén pagina, daarna kruislink naar contact/prijsindicatie.

8. **Prioriteit: Laag — `logo-varianten.html` / stub-verkeer**  
   **Type:** Technisch / SEO  
   **Onderbouwing:** Blijft verkeer trekken; monitor Search Console en redirect.  
   **Actie:** Geen nieuwe features tenzij indexatie aanhoudt.

## Seizoenspatroon (indicatief)

Mei–augustus: nadruk op lopende verbouwing, offerte-intent en kostenvragen. Later jaar: planning richting wintercomfort en renovatie/warmtepomp-combinaties — copy in RSA’s pas roteren na 6–8 weken betrouwbare post-fix **betaalde** data.

---

**Tone:** nuchter, direct, conform AGENTS.md — geen overdreven claims.
