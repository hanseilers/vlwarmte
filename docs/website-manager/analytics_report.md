# Analytics Rapport — 27 april 2026
**Periode:** 30 dagen voorafgaand aan 27-04-2026 (vlwarmte.nl)
**Bron:** GA4 property `properties/534641753`, opgehaald via `scripts/ga4_fetch.py` (laatste run: 26-04-2026 19:45)
**Vorige sprint effect:** geen meetbaar effect — dit is de eerste analyse na live-gang. Recente commits (prijsindicatiewizard, terugbel-formulier, navigatie-uitbreiding) zijn allemaal binnen het meetvenster doorgevoerd, dus eventueel effect is nog niet uit data af te leiden.

---

## Belangrijke disclaimer over de data

Het GA4-rapport is **leeg op alle rapportdimensies**:

```
top_pages: []
traffic_sources: []
entry_pages: []
devices: []
geo: []
page_engagement_90d: []
weekly_trend: []
```

Twee verklaringen, vermoedelijk allebei waar:

1. **De site is recent live gegaan** (CNAME-commit `aa39dda` en sitemap `lastmod 2026-04-26`). In de eerste 24–72 uur is verkeer per definitie laag of nul.
2. **Het script kon in de subagent-sessie niet opnieuw draaien.** De cijfers zijn van 26 april 19:45 — minder dan een dag na live-gang.

Dit rapport is voor 70% gebaseerd op **content-analyse van de live HTML-pagina's** en de bestaande `research_report.md` van marketing. Voorstellen krijgen pas een data-onderbouwing zodra GA4 minimaal 4 weken aan verkeer heeft verzameld. Volgende run: ga4_fetch.py opnieuw draaien op of na 24 mei 2026.

---

## Kerncijfers

| Metric | Waarde | Trend |
|--------|--------|-------|
| Sessies (30d) | 0 (data leeg) | n.v.t. |
| Actieve gebruikers | 0 (data leeg) | n.v.t. |
| Gem. sessieduur | n.v.t. | n.v.t. |
| Bouncepercentage | n.v.t. | n.v.t. |

**Wat we wel weten uit de configuratie:** GA4-tag `G-0BB9M7HYSF` is op alle 8 hoofdpagina's correct ingebouwd. Tracking is dus operationeel; er is geen meetfout.

## Top pagina's

Geen data beschikbaar. Bij eerstvolgende analyse: bekijken of `prijsindicatie.html` als verwacht in de top-3 binnenkomt — dat is op het moment de pagina met de meeste functionele waarde voor de bezoeker.

## Zwakste pagina's (hoge bounce / laag verkeer)

Geen data beschikbaar. Op basis van content-analyse zijn de inhoudelijke risicopagina's:

| Pagina | Risico | Reden |
|--------|--------|-------|
| `projecten.html` | Hoge bounce verwacht | 3 generieke projectkaarten zonder foto's, m², systeemkeuze of plaatsnaam — letterlijk "Straks aan te vullen" in de lead. |
| `over-ons.html` | Hoge bounce verwacht | 4 algemene kaartjes, geen gezichten, geen verhaal, geen jaartal van oprichting, geen ervaringsindicatie. |
| `systemen-producten.html` | Lage doorklik verwacht | Vier korte kaarten zonder beeld of dieptetekst. Garantieblok is sterk; de rest is dun. |
| `diensten.html` | Lage conversie verwacht | 4 kaarten met 1–2 zinnen elk. Geen interne links naar systemen of werkwijze. |

## Traffic bronnen

Geen data beschikbaar. Verwachting:
- **Direct** zal de eerste weken domineren (visitekaartjes, mond-op-mond, eigen testverkeer).
- **Organisch** komt traag op gang; pagina's moeten eerst geïndexeerd worden via Google Search Console.
- **Referral / social** is nul tenzij de Social Media Agent actief publiceert.

## Geografie

Geen data beschikbaar. Doelregio is Groningen, Drenthe, Friesland (en deel van Overijssel). Bij eerstvolgende analyse: aandeel buiten deze provincies vlaggen — dat duidt op verkeerd publiek of slechte lokale SEO-targeting.

---

## Observaties

1. **GA4 levert nul data** — eerste serieuze analyse pas mogelijk eind mei 2026. Vandaag draait alles op content-analyse en de marketing research van 26 april.
2. **De prijsindicatie-wizard staat live** (4 stappen, formspree-koppeling, prijzen €45–€96/m², minimum €2.500). Dat is precies de differentiator die het researchrapport identificeerde — first-mover voordeel ten opzichte van ComfortFloors, DVS en Kentech is daarmee gerealiseerd. Volgende vraag: gaan bezoekers de wizard ook afmaken? Daarvoor moeten event-trackingstappen worden ingericht (zie voorstel 1).
3. **Search Console ontbreekt zichtbaar** — er is geen `google-site-verification` meta-tag in de HTML-headers. Zonder Search Console weten we niet op welke zoekwoorden de site begint te ranken, en kunnen we sitemap-indexering niet bevestigen.
4. **De content-as-is mist de drie zaken die marketing research als hoogste prioriteit aanwees:** (a) geen locatiepagina's voor Groningen/Assen/Emmen/Meppel/Hoogeveen, (b) geen dienstpagina voor "infrezen" — terwijl dat de standaardmethode voor renovatie is en nul keer voorkomt op de site, (c) geen review-bewijs of klantverhalen.
5. **De projectenpagina is in huidige vorm contraproductief.** "Straks aan te vullen met foto's, m² en systeemkeuze" leest als een bouwplaats. Tot er echte cases staan kun je beter geen `projecten.html` in de hoofdnavigatie zetten dan een lege variant tonen. Korte ingreep met direct effect op vertrouwen.
6. **Mobiele beleving is niet getest.** Aandachtspunt: de wizard-progressbar moet op smartphone op één regel passen, en het contactformulier heeft veel velden in offerte-modus.

---

## Voorstellen voor Product Manager

### 1. Conversie-events instellen in GA4 — Prioriteit: Hoog
- **Onderbouwing:** Zonder events meten we alleen pageviews en weten we niet of de wizard wordt afgemaakt of het contactformulier wordt ingediend.
- **Actie:** GA4-events toevoegen in `prijsindicatie.html` (`wizard_start`, `wizard_step_2/3`, `wizard_calculate`, `wizard_lead_submit`) en in `contact.html` (`contact_submit` met dimensie `soort_aanvraag`). Markeer lead-events als conversies.
- **Verwacht effect:** Binnen 4 weken funnel-data, onderbouwd kunnen sturen.

### 2. Google Search Console koppelen en sitemap indienen — Prioriteit: Hoog
- **Onderbouwing:** Site is sinds 26 april live, sitemap is netjes opgesteld, maar zonder Search Console weten we niet welke pagina's geïndexeerd zijn of op welke termen we vertonen.
- **Actie:** `<meta name="google-site-verification" ...>` plaatsen in `<head>` van alle 8 pagina's. Sitemap indienen.
- **Verwacht effect:** Vanaf week 2 zoekwoord-data, indexering bevestigd.

### 3. Locatiepagina Groningen + Assen — Prioriteit: Hoog
- **Onderbouwing:** "Vloerverwarming Groningen" en "vloerverwarming Assen" zijn de hoogst-volume zoektermen in het werkgebied (zie `research_report.md`). ComfortFloors en DVS pakken deze termen volledig.
- **Actie:** Bouw `vloerverwarming-groningen.html` en `vloerverwarming-assen.html`. Per pagina: H1 met plaatsnaam, 300–500 woorden lokale content, CTA naar wizard, schema.org `Service` met `areaServed`.
- **Verwacht effect:** Eerste organische rankings binnen 6–10 weken voor lokale termen.

### 4. Projectenpagina afmaken of tijdelijk verbergen — Prioriteit: Hoog
- **Onderbouwing:** "Straks aan te vullen met foto's, m² en systeemkeuze" is voor een bezoeker die op vertrouwen zoekt het slechtst denkbare signaal.
- **Actie:** Twee paden: (A) afmaken met 3 echte cases (foto, locatie, m², systeem) of (B) tijdelijk uit de hoofdnavigatie halen. Voor nu: tijdelijk verbergen tot er materiaal is.
- **Verwacht effect:** Hogere doorklikratio en lager bouncepercentage op vertrouwens-pagina's.

### 5. Dienstpagina "Vloerverwarming infrezen" — Prioriteit: Hoog
- **Onderbouwing:** Infrezen is dé renovatiemethode en wordt door alle directe concurrenten als aparte pagina behandeld. Op vlwarmte.nl komt het woord nul keer voor.
- **Actie:** `vloerverwarming-infrezen.html` met uitleg, wanneer-past-het, proces, vergelijking met traditioneel/laagopbouw, kostenrange, CTA naar wizard. Verwijs vanaf `diensten.html` en `systemen-producten.html`.
- **Verwacht effect:** Nieuwe organische instap voor renovatie-zoekopdrachten.

### 6. Reviews / sociaal bewijs op de homepage — Prioriteit: Midden
- **Onderbouwing:** ComfortFloors zet 9.7/5 op 261 reviews zwaar in als verschilmaker. VLWarmte toont nul referenties. De doelgroep hecht aan vertrouwenssignalen.
- **Actie:** (a) Activeer Google Bedrijfsprofiel, vraag drie klanten om review. (b) Voeg op `index.html` een blok met 1–3 klantcitaten + plaatsnaam toe.
- **Verwacht effect:** Lager bouncepercentage homepage, meer doorklikken naar contact/wizard.

### 7. Mobiele check van wizard en contactformulier — Prioriteit: Midden
- **Onderbouwing:** Vloerverwarming wordt vaak op smartphone georiënteerd. De wizard heeft een 4-staps progress-bar, optiekaartjes en een slider. Het contactformulier in offerte-modus heeft 8+ velden.
- **Actie:** Test op iPhone SE (smal) en gemiddelde Android. Controleer leesbaarheid progress-bar, stapelen optiekaartjes, slider met duim, lange formulier.
- **Verwacht effect:** Voorkomt verlies van mobiele leads.

### 8. Kostengids-pagina — Prioriteit: Midden
- **Onderbouwing:** "Wat kost vloerverwarming per m²" is hoog-volume in de oriëntatiefase. Bezoekers die snel een bandbreedte willen zien zonder 4 wizard-stappen haken af.
- **Actie:** `kosten.html` met bandbreedtes (€45–€96/m² conform wizard), kostenfactoren, CTA naar wizard voor nauwkeuriger.
- **Verwacht effect:** Extra organische instap, betere doorgeleiding naar conversie.

### 9. Interne links systematisch versterken — Prioriteit: Midden
- **Onderbouwing:** Pagina's verwijzen nu vooral naar `contact.html`. De wizard is nieuwer, converteert vermoedelijk beter, maar krijgt minder interne links. `diensten.html`, `werkwijze.html` en `systemen-producten.html` linken er niet naar.
- **Actie:** Op elke contentpagina minstens één call-out naar de wizard ("Snel een eerste prijsindicatie? 4 stappen, geen verplichtingen"). Directe wizard-knop in hero homepage naast huidige werkwijze-knop.
- **Verwacht effect:** Hogere wizard-startratio, lagere uitval.

### 10. FAQ-pagina met long-tail vragen — Prioriteit: Laag
- **Onderbouwing:** Op `index.html` staan 3 FAQ-items, op `systemen-producten.html` 2. Schema.org FAQPage is correct ingebouwd op de homepage. Long-tail vragen ("vloerverwarming op warmtepomp", "koelen zomers", "houten verdiepingsvloer") worden niet afgevangen.
- **Actie:** `faq.html` met 12–18 vragen, hergebruik bestaande items, voeg long-tail toe. Schema.org FAQPage. Linken vanaf homepage en systemen-pagina.
- **Verwacht effect:** Meer rich snippets, extra entry-points.

---

## Volgende meetmoment

Draai `python3 scripts/ga4_fetch.py` opnieuw vanaf 24 mei 2026 (4 weken na live-gang). Pas dan zijn de eerste echte vergelijkingen mogelijk.
