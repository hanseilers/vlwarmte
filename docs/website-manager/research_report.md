# Marketing Research Rapport — 2026-06-29

Bron: eerstegraads repo-data — verse GA4 30-daags per **29 jun 2026**
(`docs/website-manager/ga4_report.json`), vorige research (`research_report.md`,
22 jun), Ads-defaults (`scripts/data/google_ads_lead_campaign_defaults.json`),
de google-ads-marketing skill en de live site-bestanden.

> **Modus-waarschuwing (lees eerst).** Deze cyclus draait autonoom **zonder Bash,
> netwerk, WebSearch of WebFetch**. Er zijn dus **geen scripts gedraaid**
> (geen `google_ads_*.py`, geen `ga4_fetch.py`, geen `--dry-run`/`--apply`) en
> **geen live webonderzoek** (geen actuele zoekvolumes, geen verse concurrent-SERP's,
> geen GSC-fetch deze ronde). Alle conclusies zijn gebaseerd op de **verse GA4-data**
> in de repo plus domeinkennis van de Noord-Nederlandse vloerverwarmingsmarkt.
> Alle Google Ads-mutaties zijn **geblokkeerd**; Ads-acties staan als **expliciete
> escalatie** met klaargezette commando's voor de eigenaar. Geen secrets in output.

## Samenvatting

De situatie is in één woord **instroom-crisis**, geen conversieprobleem. De verse
GA4 (30d t/m 29 jun) toont **~42 sessies totaal** — een instorting t.o.v. de
mei-piek (75 sessies/week begin mei → 1–5/week nu). **google/cpc is met 22 sessies
en 2 conversies de enige converterende bron**; organic levert 6 sessies / 0 conv en
direct 12 sessies / 0 conv. Het organische fundament is dus feitelijk afwezig: de
acht stadspagina's die in cyclus 17–18 zijn gebouwd (drenthe, assen, drachten,
emmen, groningen, hoogeveen, leeuwarden, zuidlaren) krijgen elk **0–2 sessies** en
moeten nog gaan ranken. De grootste hefbomen deze ronde zijn daarom: (1) de
**prijsindicatie-wizard** beter voeden — die pagina presteert uitzonderlijk sterk
(307s sessieduur, bounce 0,25) maar krijgt nauwelijks instroom; (2) **interne links
+ on-page** afmaken zodat de nieuwe stadspagina's überhaupt geïndexeerd/gevonden
worden; (3) de **Ads-geo aanscherpen** want er lekt nog steeds budget naar buiten
het kerngebied (North/South Holland, Duitsland, zelfs Bangladesh/Canada in de geo).

## Top zoekwoorden / contentkansen (organisch)

> Let op: **geen verse GSC-fetch deze ronde** (netwerk geblokkeerd). De
> impressie-/positiecijfers hieronder komen uit de vorige GSC-export (28d t/m 22
> mei, zie vorig rapport); ze blijven de beste beschikbare richtwaarde maar moeten
> bij de volgende fetch herijkt worden. De **contentkansen** zijn afgestemd op de
> sitemap zoals die nu live staat (stadspagina's bestaan inmiddels).

| Zoekwoord | Impr (laatste GSC) | Positie | Concurrentie* | Status / actie |
|-----------|--------------------|---------|---------------|----------------|
| vloerverwarming drenthe | 82 | 65,7 | midden | **pagina bestaat nu** (`vloerverwarming-drenthe.html`, cyclus 18) — interne links + indexatie verifiëren |
| vloerverwarming zuidlaren | 33 | 9,3 | laag | bestaand — cannibalisatie-fix verifiëren in GSC |
| installatiebedrijf zuidlaren | 20 | 6,5 | laag | `index.html`-blok — CTR/snippet aanscherpen |
| vloerverwarming friesland | 10 | 87,7 | midden | Leeuwarden-pagina versterken + interne links |
| vloerverwarming schoonebeek | 10 | 61,5 | laag | aanhaken op `vloerverwarming-emmen.html` |
| installateur zuidlaren | 9 | 3,7 | laag | **CTR-fix** (top-3, 0 clicks) |
| vloerverwarming hoogeveen | 8 | 10,6 | laag | pagina bestaat — interne links + FAQ |
| vloerverwarming leeuwarden | 7 | 27,3 | midden | Leeuwarden-pagina versterken |
| vloerverwarming heerenveen | 5 | 50,4 | midden | Drachten/Heerenveen-pagina |
| elektricien zuidlaren | 5 | 2,2 | laag | **CTR-fix** (top-3, 0 clicks) |

\* Concurrentie-inschatting is **indicatief** (lokale dienst + plaatsnaam =
doorgaans laag/midden); niet geverifieerd met een live keyword-tool deze ronde.
Validatie staat als escalatie.

**Patroon (ongewijzigd, blijft de belangrijkste organische les):** zodra een term
in de top 3 staat blijven clicks alsnog uit (installateur 3,7 / elektricien 2,2 /
laren 3,0 → alle 0 clicks), behalve warmtepomp zuidlaren (pos 1,8 → 25% CTR). Dat
ene klikkende geval bewijst dat de **snippet (title + meta)** het verschil maakt,
niet alleen de positie. Een CTR-/snippet-herschrijving is net zo waardevol als
positiewinst — en kost niets aan verkeer.

**Nieuw GA4-signaal (29 jun) — titel-versnippering op de homepage.** De
`top_pages` tonen voor pad `/` **zes verschillende paginatitels** in 30 dagen
(o.a. "VLWarmte | Vloerverwarming van ondervloer tot oplevering",
"Vloerverwarming Zuidlaren & Noord-NL — installateur", "Vloerverwarming Drenthe &
Noord-NL — richtbedrag in 2 min", "Vloerverwarming Drenthe, Groningen & Friesland",
plus een Engelse variant). Dat is óf bewuste title-iteratie die nog niet
geconvergeerd is, óf een ongewenste churn die Google's begrip van de homepage
verdunt. **Actie: één definitieve `<title>` + meta vaststellen** (de variant met de
hoogste sessieduur/laagste bounce als basis) en niet meer wisselen — consistent
titel-signaal helpt zowel ranking als CTR.

## Content gaps (ten opzichte van de huidige sitemap)

De sitemap is sinds 22 jun fors uitgebreid; de meeste eerder gesignaleerde gaps
zijn **gedicht**. Wat resteert is vooral **versterken en intern verbinden**, niet
nieuwbouw:

- **Geen nieuwe stadspagina's nodig.** Drenthe, Assen, Drachten, Emmen, Groningen,
  Hoogeveen, Leeuwarden en Zuidlaren bestaan nu allemaal. De prioriteit verschuift
  van "bouwen" naar "**laten ranken**": interne ankerlinks met exacte zoekterm-
  ankertekst (`vloerverwarming Drenthe`, `vloerverwarming Leeuwarden`, etc.) van
  home/diensten/zusterpagina's naar de juiste stadspagina, plus controle dat elke
  pagina een correcte `canonical`, `Service`-schema met `areaServed` en een interne
  link in de footer/nav heeft.
- **Friesland-dekking blijft zwak** (friesland 87,7 / heerenveen 50,4 / bolsward
  70,5). Geen nieuwe pagina; wél de Leeuwarden- en Drachten-pagina's onderling en
  vanuit de Drenthe-hub verbinden met exacte ankertekst, en een korte
  Friesland-sectie/anker toevoegen.
- **Zuidoost-Drenthe (Emmen-omgeving) onderbenut** (schoonebeek 61,5 / elim).
  Subdorpen als sectie/anker aanhaken op `vloerverwarming-emmen.html`.
- **Géén doelgroep-/dienst-splitsingspagina's** ("alleen schuimbeton",
  "aannemers/projectontwikkelaars"): nul vraagsignaal in de data; niet bouwen
  zonder bewijs van zoekvolume (escalatie: keyword-tool).
- **Prijscalculator bestaat al** (`prijsindicatie.html`, meerstaps-wizard) en is de
  best presterende pagina — niet opnieuw bouwen, wél voeden (zie hieronder).

## Prijsindicatie-wizard — de grootste hefboom deze ronde

De verse GA4 onderstreept dit pagina-voor-pagina:

- **`/prijsindicatie.html`: 8 sessies, gemiddelde sessieduur 307s, bounce 0,25.**
  Veruit de hoogste engagement van de hele site — bezoekers blijven ruim 5 minuten
  en haken nauwelijks af. Dit is een pagina waar mensen daadwerkelijk hun project
  invoeren.
- Ter vergelijking: de homepagina-varianten zitten op 7–146s met bounce tot 1,0;
  diensten/systemen op 15–18s. De prijsindicatie is de enige pagina die de
  bezoeker echt vasthoudt.
- 90-daags bevestigt het: prijsindicatie 68 sessies @ 130s gemiddeld — stabiel de
  sterkste verblijfsduur na de index.

**Conclusie:** de tool werkt; het probleem is **te weinig instroom**. Elke extra
bezoeker die hier landt is meer waard dan een bezoeker op de homepage. Twee
concrete on-page acties (zie sprinttaken): (1) prominente "richtbedrag in 2
minuten"-CTA boven de vouw op home én op elke stadspagina, die naar de wizard
linkt; (2) Ads-landing vaker naar prijsindicatie sturen (Ads-escalatie hieronder).

**Funnel-meting (vervolgvraag voor Analytics):** lees de stap-events
(`wizard_start` → `calculator_result` → `wizard_calculate` → `wizard_lead_submit`)
per stap uit om de zwakste stap in de wizard te vinden. Alleen `wizard_lead_submit`
en `contact_submit` zijn key events (leads); de tussenstappen meten engagement.

## Concurrentie-observaties

Geen verse SERP-scan deze ronde (netwerk geblokkeerd). Wat de eigen data indirect
laat zien:

- Op **hyperlokale** termen (zuidlaren, laren) staat VLWarmte al hoog → dunne lokale
  concurrentie; kleine on-page-ingrepen leveren hier het meeste op.
- Op de **brede provincieterm** (vloerverwarming drenthe, pos 66) staan landelijke
  portals/aggregators sterker. De nieuwe dedicated Drenthe-pagina is precies de
  juiste zet; de vraag is nu of die top-10 haalbaar is in een portal-SERP.
- **Te valideren (escalatie):** wie staat top-5 op "vloerverwarming drenthe" en
  "vloerverwarming friesland", en met wat voor pagina (provinciehub vs. portal)?
  Bepaalt de haalbaarheid en het benodigde linkprofiel.

## On-page sprinttaken (voor de PM → sprint.md)

Concreet en klein gehouden, met meetbaar succescriterium per taak:

1. **Homepage-titel consolideren.** Eén definitieve `<title>` + meta description
   op `index.html` vaststellen (basis: de variant met hoogste sessieduur / laagste
   bounce) en niet meer wisselen. *Succes: GA4 toont nog maar één paginatitel voor
   `/`; GSC-CTR op home stijgt bij volgende fetch.*
2. **Interne ankerlinks naar de nieuwe stadspagina's.** Vanuit home, diensten en
   zusterstadspagina's exacte-ankertekstlinks (`vloerverwarming Drenthe`,
   `vloerverwarming Leeuwarden`, `vloerverwarming Emmen`, etc.) naar de juiste
   pagina; Drenthe als hub die naar alle stadspagina's linkt en terug. *Succes:
   elke stadspagina heeft ≥2 interne inkomende links met exacte ankertekst; GSC
   toont indexatie + positiewinst bij volgende fetch.*
3. **CTR-/snippet-fix top-3-termen.** Title + meta van `index.html` en
   `vloerverwarming-zuidlaren.html` herschrijven zodat de snippet uitnodigt tot
   klikken (USP + plaats + CTA), naar het patroon van de wél-klikkende
   warmtepomp-snippet. *Succes: installateur/elektricien/laren-termen gaan van 0
   naar >0 clicks in GSC.*
4. **"Richtbedrag in 2 minuten"-CTA boven de vouw.** Op `index.html` en elke
   stadspagina een prominente CTA die naar `prijsindicatie.html` linkt. *Succes:
   GA4 toont meer entry-/doorklik-sessies naar prijsindicatie; meer
   `wizard_start`-events.*
5. **Friesland- en Emmen-subdorpen aanhaken.** Exacte-ankertekstlinks naar
   `vloerverwarming-leeuwarden.html` (Friesland/Heerenveen) en
   `vloerverwarming-emmen.html` (Schoonebeek/Elim) vanuit zuster- en hubpagina's.
   *Succes: die termen schuiven omhoog in GSC bij volgende fetch.*
6. **www-/non-www ranking-splitsing verifiëren.** (Stond vorig rapport al;
   herhalen tot bevestigd.) Controleer 301-redirect + canonical naar één
   hostvariant. *Succes: GSC toont nog maar één homepage-URL met één positie i.p.v.
   een gesplitst 5,6 vs. 52,8 signaal.*

## Google Ads — ESCALATIE (geen verificatie/mutatie deze ronde)

Alle Ads-scripts en -mutaties zijn **geblokkeerd** in deze cyclus. Onderstaande
commando's staan klaar voor een sessie mét Ads-permissies (of voor handmatige
uitvoering door de eigenaar). Onderbouwing uit de verse GA4-geo en
traffic-sources:

- **google/cpc is de enige converterende bron** (22 sessies / 2 conv in 30d).
  Bescherm dit kanaal: elke euro telt bij EUR 2/dag.
- **Geo-lek bestaat nog.** De GA4-geo toont sessies buiten het kerngebied:
  North Holland (4), South Holland (3), Duitsland/Lower Saxony (2), plus zelfs
  Bangladesh (1) en Canada (1). Kerngebied: Drenthe (9), Friesland (6),
  Groningen (5). Een flink deel van het schaarse verkeer landt buiten het
  werkgebied terwijl de geo-defaults in de JSON wél Drenthe/Groningen/Friesland
  zijn → de live campagne staat vermoedelijk nog op NL-breed.
- **Verkeersdaling ~90%** sinds de mei-piek (75 → 1–5 sessies/week). Plausibel
  budgetgedreven (EUR 2/dag) en/of seizoen (vloerverwarming is winterproduct).
  Verifiëren of dit bewust is.

**Stap 0 — read-only verifiëren** (welke status/geo staat live?):
```
python scripts/google_ads_list_campaigns.py
```
Bevestig id, status (ENABLED?), kanaaltype en of de geo al is aangescherpt.

**Escalatie 1 — geo aanscherpen naar kerngebied** (stopt het budgetlek):
```
python scripts/google_ads_update_campaign_geo.py --campaign-id 23834672782 --dry-run
python scripts/google_ads_update_campaign_geo.py --campaign-id 23834672782 --apply
```

**Escalatie 2 — landing richting prijsindicatie.** GA4 toont prijsindicatie als
veruit sterkste engagement-pagina (307s, bounce 0,25). De `final_urls` in de
defaults zijn al beperkt tot offerte-deeplink + prijsindicatie (goed). Overweeg in
de live RSA de **prijsindicatie als primaire landing** voor de research-intentie-
adgroep. RSA in de Ads UI handmatig syncen (geen update-script).

**Escalatie 3 — verkeersdaling + status bewust maken.** Bevestig met
`list_campaigns` of de daling budget- of seizoensgedreven is. Bij EUR 2/dag is
budget de meest waarschijnlijke verklaring. **Budget verhogen of `--go-live`
alleen na expliciete spend-goedkeuring in chat** — niet in deze mode, niet zonder
akkoord. Huidig dagbudget EUR 2 respecteren.

**Niet doen zonder expliciete goedkeuring:** budget verhogen, `--go-live`,
keyword-/copy-mutaties live zetten. Geen tokens of `secrets/`-inhoud in output.

## Aanbevelingen voor de Product Manager (geprioriteerd, max 8)

1. **(SEO/Dev — <1u, Hoog) Homepage-titel consolideren.** Type: SEO/technisch.
   Onderbouwing: GA4 toont 6 verschillende titels voor `/` in 30d → verdund
   signaal + CTR-ruis. Actie: één definitieve title+meta vaststellen en bevriezen.
2. **(SEO/Dev — <2u, Hoog) Interne ankerlinks naar de 8 nieuwe stadspagina's.**
   Type: Content/interne links. Onderbouwing: stadspagina's bestaan maar krijgen
   0–2 sessies; zonder interne links ranken ze niet. Actie: exacte-ankertekstlinks
   + Drenthe als hub.
3. **(SEO/Dev — <1u, Hoog) CTR-/snippet-fix top-3-termen.** Type: SEO (title/meta).
   Onderbouwing: top-3-termen halen 0 clicks; goede snippet = 25% CTR bewezen.
   Actie: home + zuidlaren-snippet herschrijven (USP + plaats + CTA).
4. **(CRO/Dev — 2–4u, Hoog) "Richtbedrag in 2 minuten"-CTA boven de vouw.** Type:
   CTA/conversie. Onderbouwing: prijsindicatie 307s/bounce 0,25 maar te weinig
   instroom. Actie: prominente CTA op home + stadspagina's naar de wizard.
5. **(SEO/Dev — <1u, Midden) Friesland- en Emmen-subdorpen aanhaken.** Type:
   Content/interne links. Onderbouwing: friesland 87,7 / heerenveen 50,4 /
   schoonebeek 61,5 hangen aan verkeerde URL's. Actie: exacte-ankertekstlinks naar
   Leeuwarden- en Emmen-pagina.
6. **(SEO/Dev — <1u, Midden) www-/non-www ranking-splitsing verifiëren.** Type:
   Technische SEO. Onderbouwing: home-signaal mogelijk gesplitst over twee hosts.
   Actie: 301 + canonical naar één hostvariant bevestigen.
7. **(Ads/Escalatie — <30min, Hoog zodra permissies) Geo aanscherpen + status
   checken.** Type: Ads. Onderbouwing: geo-lek (NH/ZH/DE + buitenland) bij EUR
   2/dag, en cpc is de enige converter. Actie: `list_campaigns` →
   `update_campaign_geo` (commando's hierboven). Vraagt sessie met Ads-permissies.
8. **(Proces — Hoog) Verse GSC-fetch + WebSearch/Ads-permissies herstellen.** Type:
   Infra. Onderbouwing: deze cyclus kon geen GSC-fetch, geen webonderzoek en geen
   live Ads-state ophalen (geen Bash/netwerk). Actie: een research-/Ads-sessie met
   netwerk- en script-permissies inplannen zodat zoekvolumes, concurrent-SERP's,
   verse GSC-posities en live campagnestatus geverifieerd worden vóór de volgende
   grote contentbeslissing.

---

### Samenvatting voor de Product Manager (max 5 regels)
- **Modus:** autonoom, geen Bash/netwerk/WebSearch → analyse op verse GA4
  (29 jun) + domeinkennis; GSC-posities en live Ads-state staan als escalatie met
  klaargezette commando's.
- **Kernprobleem is instroom, niet conversie:** ~42 sessies in 30d (instorting
  vanaf 75/week in mei); google/cpc is de **enige** converterende bron (22 sess /
  2 conv), organic 6/0, direct 12/0.
- **Grootste hefboom:** de prijsindicatie-wizard (307s, bounce 0,25) méér voeden
  via CTA's boven de vouw + Ads-landing — de tool werkt, er komt te weinig verkeer.
- **SEO-fundament afmaken:** de 8 nieuwe stadspagina's intern linken zodat ze
  ranken, homepage-titel consolideren (6 varianten in GA4) en de top-3-snippets
  fixen (0 clicks ondanks top-3).
- **Ads (escalatie):** geo-lek bestaat nog (NH/ZH/DE + buitenland bij EUR 2/dag) →
  geo aanscherpen en status checken zodra een Ads-sessie draait; budget niet
  verhogen zonder goedkeuring.
</content>
</invoke>
