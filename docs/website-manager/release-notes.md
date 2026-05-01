# VLWarmte — Release Notes

Wekelijks bijgewerkt door de Product Manager Agent. Nieuwste release bovenaan.

---

## Release — week van 5 mei 2026
**Deployment:** (na push / GitHub Pages — lokaal gevalideerd 01-05-2026)  
**Versie:** (volgt na commit — werkdirectory sprint Zuidlaren + canonical + CTA’s)

### Wat is er veranderd
- **Nieuwe landingspagina** `vloerverwarming-zuidlaren.html` voor hyperlokale zoekintentie (Zuidlaren + installateur + vloerverwarming), met infrezen-sectie en schema `areaServed` Zuidlaren. In sitemap en footer Regio op alle pagina’s.
- **Sterkere hero-CTA** op de stadspagina’s Groningen en Assen: prijsindicatie, bellen en offerte-dieplink in één regel boven de vouw (`hero-cta-row`).
- **Canonieke home-URL:** logo en menu “Home” linken naar `/` in plaats van `index.html`; README vermeldt het verschil met `file://` lokaal openen.
- **Interne links** vanaf home, over-ons en diensten naar de Zuidlaren-pagina.
- **Prijsindicatie-CTA** op `werkwijze.html` en `systemen-producten.html` via bestaand `cta-band`-patroon.

### Waarom
Analytics en marketing research wezen op Drenthe-volume en het trefwoordcluster rond Zuidlaren; zonder eigen URL bleef dat verkeer op Groningen/Assen-titels landen. Dubbele `/` vs `index.html`-meting en lage engagement op stadspagina’s vroegen om technische en CTA-verbeteringen.

### Verwacht effect
Meetbaar in GA4: sessies op `/vloerverwarming-zuidlaren.html`; in Search Console (na token): queries met “zuidlaren”. Schonere home-rapportage door minder `index.html`-splitsing.

### Social media deze week
Zie `social/weekly_calendar.md`. Suggestie: één post met link naar de nieuwe Zuidlaren-URL na live-gang.

---

## Release — week van 27 april 2026
**Deployment:** 27-04-2026, 09:31 (commit `9e275a4`, GitHub Pages run `24982250357`)
**Versie:** `9e275a4` — "Sprint 27 april: GA4 events, Search Console-tag, twee locatiepagina's, projecten uit nav"

### Wat is er veranderd
- **Conversie-meting werkt nu.** De prijsindicatie-wizard stuurt vijf events naar Google Analytics: starten van de wizard, doorklikken naar stap 2 en 3, klikken op de bereken-knop en het verzenden van een lead. Het contactformulier stuurt een event mee per soort aanvraag (informatie, offerte of terugbelverzoek). Vanaf nu is in GA4 te zien wáár bezoekers afhaken.
- **Twee nieuwe stadspagina's.** `vloerverwarming-groningen.html` en `vloerverwarming-assen.html` zijn live. Beide met lokale plaatsnamen, reistijd vanaf Zuidlaren, een uitleg over infrezen voor renovatie, en doorlinks naar de prijsindicatie. Bedoeld om gevonden te worden op zoekopdrachten als "vloerverwarming Groningen" en "vloerverwarming Assen". Toegevoegd aan footer en sitemap, niet aan de hoofdnavigatie (die werd anders te lang).
- **Search Console klaar voor koppeling.** Op alle 10 productie-pagina's staat nu een placeholder verificatie-tag in de `<head>`. Hans hoeft alleen de echte token uit Search Console te plakken en te pushen, dan is de site geverifieerd.
- **Projectenpagina uit de hoofdnavigatie gehaald.** Zolang er nog geen echte cases met foto en plaatsnaam staan, is een lege projectenpagina een verkeerd signaal. De pagina blijft bestaan voor directe links, maar staat niet meer in de menubalk en niet meer in de sitemap. Bovenaan staat een korte uitleg met verwijzingen naar werkwijze en systemen.

### Waarom
GA4-events: zonder funnel-data weten we niet of de wizard werkt of bezoekers halverwege wegklikken. Stadspagina's: marketing research wijst Groningen en Assen aan als hoogste-ROI combinatie van zoekvolume, koopkracht en concurrentiedruk. Search Console: de site is sinds 26 april live en moet zo snel mogelijk geïndexeerd worden. Projecten uit nav: een pagina die "Straks aan te vullen" zegt schaadt het vertrouwen meer dan dat hij oplevert.

### Verwacht effect
Per 25 mei 2026 willen we in GA4 zien: minimaal één bevestigde wizard-conversie via het lead-event, en in Search Console minstens één van de twee stadspagina's met vertoningen op lokale termen. Dat is het beslismoment voor sprint 4.

### Social media deze week
Zeven posts gepland in `social/weekly_calendar.md`: 3 op LinkedIn (di/wo/do, B2B-toon, focus op detail-vakmanschap, schuimbeton en garantie) en 4 op Instagram (wo/vr/za en wo+1 week, particulier, focus op opgeleverde vloeren, het-werk-onder-de-vloer, het team en de prijscalculator). Alle posts hebben `[FOTO NODIG: ...]`-placeholders — VLWarmte moet zelf nog beeldmateriaal aanleveren in `social/input/` en handmatig publiceren.

---
