# Marketing Research Rapport — 2026-06-15

Bron: echte GSC-data 25 apr–22 mei 2026 (`gsc_report.json`) en GA4 30-daags
(`ga4_report.json`). Werkwijze in deze ronde: alleen analyse op bestaande
repo-bestanden — geen webonderzoek, geen scripts, geen Ads-mutaties (die zijn in
deze modus geblokkeerd). Ads-advies staat als escalatie/aanbeveling onderaan.

## Samenvatting
De leads komen nu vrijwel volledig uit betaald (google/cpc: 22 conv) en direct
(13 conv); organisch levert 0 conversies op 9 sessies. De grootste organische
kansen liggen niet in nieuwe pagina's maar in drie termen die net buiten pagina
1 hangen — "vloerverwarming zuidlaren" (9,3), "installatiebedrijf zuidlaren"
(6,5) en "vloerverwarming hoogeveen" (10,6) — plus één term met veel latente
vraag, "vloerverwarming drenthe" (82 impressies, positie 66). Daarnaast lekt de
betaalde campagne budget naar buiten het kerngebied (25 sessies North Holland,
11 South Holland), terwijl de geo-defaults wél Drenthe/Groningen/Friesland zijn.

## 1. Stand van zaken — organisch vs. betaald

| Kanaal | Sessies | Conversies | Opmerking |
|--------|---------|------------|-----------|
| google / cpc (Paid) | 85 + 1 | 22 | Draagt de leadmotor. |
| (direct) / (none) | 42 | 13 | Sterk — merk/herhaalverkeer, deels Ads-naijl. |
| google / organic | 9 | 0 | Veel impressies, nauwelijks clicks/conv. |
| facebook (social) | 7 | 0 | Klein, geen leads. |

Kernpunt: **organisch presteert ver onder potentie.** Er staan honderden
impressies op regio-termen, maar de rankings zitten grotendeels op pagina 3–9,
dus die impressies leveren geen clicks (CTR 0). De site verdient zijn leads nu
met advertentiegeld; elke positiewinst op een "bijna pagina 1"-term is gratis
volume dat structureel blijft staan.

## 2. SEO-kansen, geprioriteerd

### A. "Bijna pagina 1" — kleinste ingreep, snelste winst

**1. "vloerverwarming zuidlaren" — 33 impr, positie 9,3 (thuisbasis).**
Diagnose uit `query_page`: Google laat hier **de homepage** ranken (pos 6,6, 17
impr) náást de dedicated pagina `vloerverwarming-zuidlaren.html` (die voor déze
term nauwelijks in beeld komt). Ook `diensten.html` (16,6) en
`prijsindicatie.html` (19,4) pakken impressies. Dit is **keyword-cannibalisatie**:
relevantie en linkkracht zijn verspreid over 5+ URL's, geen enkele wint. De
dedicated pagina ís al sterk geschreven; ze mist alleen interne linkkracht met
exacte ankertekst.

**2. "installatiebedrijf zuidlaren" — 20 impr, positie 6,5.**
Rankt op de homepage. Verwante termen staan al hoog: "installateur zuidlaren"
3,7, "elektricien zuidlaren" 2,2. De homepage mist een expliciete
"installatiebedrijf in Zuidlaren"-formulering in een kop/contentblok. Kleinste
ingreep: één H2 + alinea + LocalBusiness-bevestiging.

**3. "vloerverwarming hoogeveen" — 8 impr, positie 10,6 (eigen pagina).**
Dedicated pagina rankt al, hangt op de pagina-1-grens. Subtermen lopen mee:
"vloerverwarming fluitenberg" 4,8, "vloerverwarming hollandscheveld" 20,3,
"vloerverwarming noordscheschut" 33,8. Kleinste ingreep: een paar interne links
mét ankertekst "vloerverwarming Hoogeveen" vanuit homepage/Drenthe-hub en
zusterpagina's, plus een korte FAQ-blok met schema voor extra relevantie.

### B. Grote latente vraag — "vloerverwarming drenthe" (82 impr, positie 66)

Dit is verreweg de grootste regioterm op impressies, maar rankt diep (pos 63–77)
verspreid over homepage (57 impr), prijsindicatie (49), diensten (13) en faq (4).
Er is **geen dedicated `vloerverwarming-drenthe.html`** — alleen een
`#drenthe-hub`-sectie op de homepage. Voor een provinciedekkende hoofdterm met
dit volume is een eigen, kanonieke landingspagina de logische zet: die bundelt de
nu versnipperde signalen, kan intern linken naar alle stadspagina's (Assen,
Hoogeveen, Emmen, Meppel, Beilen) en die linken terug. Dit is groter dan een
title-tweak (>1 sprintdag inclusief content), maar het is de enige term waar de
ranking-afstand zo groot is dat losse on-page-tweaks niet volstaan.

## 3. Concrete on-page taken voor de Developer Agent (deze sprint)

> Alle taken zijn <4u en raken bestaande bestanden. Succes meet je in GSC
> (positie/CTR per query) na 2–4 weken en in GA4 (`organic` sessies/landing).

**Taak 1 — Zuidlaren-cannibalisatie oplossen (interne links + ankertekst).**
Doel-URL's: `index.html`, `diensten.html`, `prijsindicatie.html`,
`vloerverwarming-zuidlaren.html`.
- In `index.html` staat in de hero de link `<a href="vloerverwarming-zuidlaren.html">Zuidlaren</a>`.
  Verrijk de ankertekst naar de exacte zoekterm, bv.:
  "Basis in <a href="vloerverwarming-zuidlaren.html">Zuidlaren — bekijk
  vloerverwarming Zuidlaren</a>."
- Voeg op `diensten.html` en `prijsindicatie.html` één regel toe met expliciete
  link + ankertekst "vloerverwarming Zuidlaren" naar de dedicated pagina, zodat
  Google die als kanoniek voor de term gaat zien (in plaats van die pagina's zelf).
- Op `vloerverwarming-zuidlaren.html`: H1 staat goed ("Vloerverwarming
  Zuidlaren"). Voeg in de eerste alinea de exacte combinatie
  "vloerverwarming in Zuidlaren" toe (nu opent de lead met "We zitten aan de
  Verlengde Stationsweg…").
- Succes: GSC ranking dedicated pagina voor "vloerverwarming zuidlaren" stijgt
  naar <5; homepage zakt voor die term. Doel: pagina 1.

**Taak 2 — "installatiebedrijf zuidlaren" op de homepage verankeren.**
Doel-URL: `index.html`.
- Voeg een kort contentblok toe (H2 + 1 alinea), bv.:
  H2: "Installatiebedrijf in Zuidlaren"
  Tekst: "VLWarmte is het installatiebedrijf in Zuidlaren voor complete
  vloerverwarming — van ondervloer en schuimbeton tot dekvloer en oplevering.
  Eén aanspreekpunt, eigen ploeg, reactie binnen één werkdag."
- Controleer dat de `LocalBusiness`-schema op `#localbusiness` een logisch
  `name`/`address` in Zuidlaren bevat (versterkt lokale relevantie).
- Succes: "installatiebedrijf zuidlaren" van 6,5 naar pagina 1 (top 5).

**Taak 3 — Hoogeveen over de pagina-1-grens duwen.**
Doel-URL: `vloerverwarming-hoogeveen.html` + interne links.
- Voeg minstens 2 interne links met exacte ankertekst "vloerverwarming
  Hoogeveen" toe vanuit `index.html` (`#drenthe-hub` heeft al een link — maak de
  ankertekst exact) en vanuit een zusterpagina (bv. Emmen/Assen "Ook actief in").
- Voeg onderaan een korte FAQ toe (2–3 vragen: "Werken jullie ook in
  Hollandscheveld/Fluitenberg?", "Wat kost vloerverwarming in Hoogeveen?") en
  markeer met `FAQPage`-schema. De subdorpen ranken al mee; dit consolideert.
- Succes: "vloerverwarming hoogeveen" van 10,6 naar <10; CTR > 0.

**Taak 4 — Title/meta-CTR op homepage voor "vloerverwarming drenthe".**
Doel-URL: `index.html` (interim, vóór taak 5).
- Homepage-title is nu "Vloerverwarming Zuidlaren & Noord-NL — installateur |
  VLWarmte". Overweeg "Drenthe" expliciet in title/description op te nemen zolang
  er nog geen dedicated pagina is, bv. description-opening:
  "Vloerverwarming in Drenthe, Groningen en Friesland — het hele traject van
  ondervloer tot oplevering…". Lage inspanning, houdt de term warm.
- Succes: positie "vloerverwarming drenthe" beweegt; meet vóór taak 5 live gaat.

**Taak 5 (groter, optioneel deze sprint) — dedicated `vloerverwarming-drenthe.html`.**
- Nieuwe pagina naar model van de bestaande stadspagina's (zelfde head/schema-
  patroon, `Service` + `areaServed` = "Drenthe", canonical naar nieuwe URL).
- H1 "Vloerverwarming Drenthe"; content over provinciedekking; **interne links
  naar én vanuit** alle stadspagina's (Assen, Hoogeveen, Emmen, plus Meppel/
  Beilen als die later komen). Zet de homepage-`#drenthe-hub` om naar een korte
  teaser die naar deze pagina linkt (voorkomt nieuwe cannibalisatie).
- Succes: nieuwe pagina pakt de 82 impr over en stijgt richting top 20, daarna
  verder. Dit is de enige structurele fix voor de grootste regioterm.

## 4. Google Ads-advies (escalatie — GEEN mutaties uitgevoerd)

Onderbouwing uit data: GA4-geo toont **25 sessies North Holland en 11 South
Holland** — samen 36 sessies (28% van het verkeer) buiten het kerngebied. De
live campagne heet "VLW-API-Leads NL auto" (id 23834672782, EUR 2/dag) en draait
dus **landelijk**, terwijl `google_ads_lead_campaign_defaults.json` juist
Drenthe/Groningen/Friesland als geo-constants heeft staan
(`geoTargetConstants/20759, 20763, 20761`). Het buiten-regio-verkeer is vrijwel
zeker (deels) betaald = budgetlek bij een dagbudget van EUR 2.

**Aanbeveling 1 — geo van de live campagne aanscherpen naar het kerngebied.**
De eigenaar kan dit later handmatig draaien (script bestaat in repo):
```
python scripts/google_ads_update_campaign_geo.py --campaign-id 23834672782 --dry-run
python scripts/google_ads_update_campaign_geo.py --campaign-id 23834672782 --apply
```
Dit vervangt de positieve LOCATION-criteria door de geo-lijst uit defaults
(Drenthe/Groningen/Friesland). Verwacht effect: minder verspilling, hogere
lead-relevantie bij gelijk budget.

**Aanbeveling 2 — landingsafstemming is al goed; bewaken.** De final URLs zijn
sinds 2026-06-01 beperkt tot offerte-deeplink + prijsindicatie (omdat brede URLs
op de homepage met 67% bounce landden). Prijsindicatie presteert sterk
(bounce 0,32, lange sessieduur) — laat staan. Geen wijziging nodig.

**Aanbeveling 3 — zoektermen oogsten na geo-fix.** Na 2–4 weken het
zoektermenrapport herlezen: de organische "bijna pagina 1"-termen
(installatiebedrijf/installateur zuidlaren) en subdorpen kunnen als negatieven
óf juist als nieuwe keywords dienen, afhankelijk van intentie. Keyword-toevoegen
kan later met:
```
python scripts/google_ads_add_keywords_from_defaults.py --campaign-id 23834672782 --dry-run
```
(voegt alleen ontbrekende keywords uit defaults toe; verwijdert niets.)

**Niet doen zonder expliciete spend-goedkeuring:** budget verhogen of `--go-live`
op nieuwe campagnes. Huidig dagbudget EUR 2 respecteren.

## 5. Top 5 aanbevolen acties (geprioriteerd op lead-impact × haalbaarheid <4u)

1. **(SEO, Dev — <2u)** Zuidlaren-cannibalisatie oplossen via interne links +
   exacte ankertekst naar `vloerverwarming-zuidlaren.html` (Taak 1). Hoogste
   ratio: term staat op 9,3, dichtbij pagina 1, thuisbasis.
2. **(Ads, Eigenaar — <30min)** Geo van live campagne 23834672782 beperken tot
   Drenthe/Groningen/Friesland (Aanbeveling 1). Stopt direct budgetlek (28%
   verkeer buiten regio).
3. **(SEO, Dev — <1u)** Contentblok "Installatiebedrijf in Zuidlaren" op de
   homepage (Taak 2). Term op 6,5; kleine ingreep, top-5 haalbaar.
4. **(SEO, Dev — <2u)** Hoogeveen-pagina versterken met interne links + FAQ-
   schema (Taak 3). Term op 10,6; subdorpen ranken al mee.
5. **(SEO, Dev — <30min interim)** "Drenthe" in homepage-title/description tot
   een dedicated pagina er is (Taak 4); plan Taak 5
   (`vloerverwarming-drenthe.html`) als grotere vervolgactie voor de term met de
   meeste latente vraag (82 impr).

---

### Samenvatting voor de Product Manager (max 5 regels)
- Leads draaien op betaald + direct; organisch (0 conv) is onbenut terwijl drie
  termen net buiten pagina 1 hangen (zuidlaren 9,3 / installatiebedrijf 6,5 /
  hoogeveen 10,6) — kleine on-page ingrepen, grote kans.
- Snelste winst: Zuidlaren-cannibalisatie oplossen via interne links/ankertekst
  (één dedicated pagina als winnaar aanwijzen).
- Grootste latente vraag: "vloerverwarming drenthe" (82 impr @ 66) heeft een
  eigen landingspagina nodig — groter werk, hoogste plafond.
- Ads-budgetlek: live campagne draait NL-breed (25 sessies North Holland) terwijl
  geo-defaults het kerngebied zijn — eigenaar kan geo aanscherpen met het
  `update_campaign_geo`-script (commando staat klaar). Geen mutaties uitgevoerd.
- 5 acties klaargezet, alle <4u; 4 voor de Developer-sprint, 1 handmatige Ads-fix
  voor de eigenaar.
