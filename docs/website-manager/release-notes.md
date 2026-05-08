# VLWarmte — Release Notes

Wekelijks bijgewerkt door de Product Manager Agent. Nieuwste release bovenaan.

---

## Release — week van 2 juni 2026
**Deployment:** 08-05-2026 (PM: `git push origin main` — GitHub Pages)  
**Versie:** `c43d609`

### Wat is er veranderd
- **`prijsindicatie.html`:** CTA-blok direct onder de hero met link naar de wizard (`#wizard`), directe offerte-route en informatieformulier — betere aansluiting op **Paid Search**-landings en snellere tweede stap.
- **`scripts/data/google_ads_lead_campaign_defaults.json`:** Drie RSA-headlines gericht op **online prijsindicatie** en **richtbedrag** (voor volgende campagne-updates of handmatige RSA-sync).
- **`disclaimer.html` + `privacy.html`:** Korte navigatie-exit onder de hero (homepage, prijsindicatie, contact) om landings-bounce 1,0 te verzachten.
- **`projecten.html`:** `hero-soft-row` met **Informatie aanvragen** — lichtere stap naast bestaande knoppen.
- **Playbooks + `AGENTS.md`:** Product Manager voert **commit en push** zelf uit na developer (geen eigenaar nodig behalve bij git-auth).

### Waarom
- Analytics (cyclus 2, 8 mei): **google/cpc** zonder conversies; prijsindicatie en contactroutes moeten in copy én op de pagina maximaal zichtbaar zijn.
- Disclaimer/privacy als instap met bounce 1,0 — minimale exit-hulp.

### Verwacht effect
- Meer `wizard_start` / conversies vanaf prijsindicatie-landing; eerste signalen voor Paid Search na RSA-sync in Ads.
- Minder directe exit op disclaimer/privacy.

### Social media deze week
Zie `docs/website-manager/social/weekly_calendar.md` (week van 2 juni 2026).

---

## Release — week van 18 mei 2026
**Deployment:** 08-05-2026 (GitHub Pages run `25543472674`, succesvol)
**Versie:** `3e97a18` (code) + `d396fa9` (documentatie deploymentregels) — Sprint 18 mei: vroege CTA’s, logo-URL redirect, GA4 weekly_trend backfill

### Wat is er veranderd
- **`logo-varianten.html`:** minimale doorverwijspagina met canonical naar de homepage, meta-refresh en een zichtbare link voor bezoekers zonder automatische doorstuur — vangt bookmarks en oude links op zonder 404.
- **`diensten.html`, `werkwijze.html`, `over-ons.html`:** direct onder de hero een **`cta-band`** met duidelijke paden naar de prijsindicatie en FAQ of contact (informatie-dieplink), zodat landers meteen een tweede stap zien.
- **`assets/css/styles.css`:** helper **`.cta-band-stack`** voor nette stapeling van meerdere knoppen in donkere CTA-blokken op smalle schermen.
- **`scripts/ga4_fetch.py`:** `weekly_trend` bevat altijd **8 weken**; weken zonder data in GA4 worden met nul-sessies ingevuld zodat trends in rapportages niet breken.

### Waarom
- Analytics (7 mei) toonde nog restverkeer naar de oude logo-URL en een hoge bounce op `diensten.html` als landing, korte sessies op `werkwijze.html` en weinig vroege vervolgstap op `over-ons.html`.
- De fetch-export had soms minder dan acht weken in `weekly_trend` doordat de GA4-API geen rij teruggeeft bij nul sessies — dat maakt weekvergelijking onmogelijk voor de PM-cyclus.

### Verwacht effect (meting rond 4 juni 2026)
- Minder “dood” verkeer op `/logo-varianten.html`; consolidatie richting homepage.
- Lagere bounce en vaker tweede hit vanaf `diensten.html` en `werkwijze.html`; vaker start vanuit `over-ons.html` richting prijsindicatie of licht contact.
- Betrouwbare 8-punts weekreeks in `ga4_report.json` na elke fetch.

### Social media deze week
Zie `docs/website-manager/social/weekly_calendar.md` (week van 18 mei 2026).

---

## Release — week van 11 mei 2026
**Deployment:** 06-05-2026 10:28 (commit `2f22120`, GitHub Pages run `25424644693`, in_progress bij rapportage)
**Versie:** `2f22120` — Sprint 11 mei: conversiepaden contact + stadspagina's + projecten, GA4 weekly_trend fix, calculator_complete

### Wat is er veranderd
- **`contact.html`:** boven het bestaande formulier staat nu een directe-keuze blok met drie paden — bel-knop, sms-knop ("stuur een berichtje") en een secundaire route naar de prijsindicatie. Op mobiel staan de drie keuzes onder elkaar full-width. Het formulier zelf is ongewijzigd.
- **Stadspagina's** (Groningen, Assen, Zuidlaren): onder de bestaande hero-CTA een korte regel "liever bellen of even iets vragen?" met een bel-knop en een knop "informatie aanvragen" die `contact.html?modus=informatie#aanvraag` opent.
- **`projecten.html`:** de hero-tekst is herschreven naar één eerlijke alinea (er zijn nog geen openbaar gepubliceerde cases; referenties op verzoek), met daaronder twee knoppen: prijsindicatie en FAQ. De rest van de pagina blijft staan.
- **`prijsindicatie.html`:** nieuw GA4-event `calculator_complete` op het moment dat de eindberekening getoond wordt — met de ingevoerde m², ondergrond en gekozen systeem (geen persoonsgegevens). Bestaande events blijven staan.
- **`scripts/ga4_fetch.py`:** loop voor `weekly_trend` is gefixt — schrijft nu acht niet-overlappende weken in plaats van één. Maakt week-over-week analyse mogelijk vanaf de volgende fetch.

### Waarom
- Analytics Agent (6 mei) liet zien dat `contact.html` als landing 8 sessies trekt met bounce 1,00 en 0 conversions, terwijl `prijsindicatie.html` ter vergelijking 13 conversions levert op 11 landingen — sterkste lead-generatie kans van de week.
- Stadspagina's bouncen 1,00 als landing op Groningen en Assen; FAQ-link uit sprint 19 mei was het lichte pad, een bel-knop en lichte "informatie"-route maken de tweede stap nog expliciter.
- `projecten.html` had bounce 0,86 en 0,9 s gemiddelde tijd — de pagina was een dood spoor. Klant-akkoord voor echte cases is nog niet binnen, dus voor nu een eerlijke alinea + doorstroom in plaats van leeg laten.
- `calculator_complete`-event is voorwaarde om drop-off in de wizard te kunnen meten; zonder kunnen we de wizard wel zien werken, maar niet zien wáár het beter kan.
- `weekly_trend`-bug blokkeerde alle trend-analyse — pure infrastructuur-fix.

### Verwacht effect (meting per 3 juni 2026)
- ≥1 conversion uit `/contact.html` als landing (was 0).
- Bounce `/contact.html`-landing onder 0,80 (was 1,00).
- Tweede-hit-rate stijgt op stadspagina's; iets minder strakke 1,00 landingsbounce.
- `calculator_complete` verschijnt in GA4 met genoeg events om over 2–4 weken drop-off-analyse te doen.
- Volgende `ga4_fetch.py`-run levert 8 unieke weken in `weekly_trend` zodat trends meetbaar worden.

### Social media deze week (week van 11 mei)
- **LinkedIn (3 posts):** di 12 mei renovatie-opbouw infrezen vs schuimbeton; wo 13 mei prijsindicatie als planningstool; do 14 mei nieuwe Zuidlaren-pagina + Drentse dorpen.
- **Instagram (4 posts):** wo 13 mei schuimbeton onder de vloer; vr 15 mei comfort + opwarmtijd per vloerafwerking; za 16 mei lokaal werken vanuit Zuidlaren; zo 17 mei renovatie Assen.
- **Facebook (1 optionele post):** do 14 mei Zuidlaren-pagina.
- **Drie posts hebben een [FOTO NODIG]-placeholder** — VLWarmte moet beeld aanleveren in `social/input/` voor publicatie.

### Bekende kanttekeningen
- Geen WhatsApp-nummer expliciet bekend, dus contact-keuze gebruikt `sms:+31618817459` met label "stuur een berichtje". Kan later naar `wa.me` zonder UI-aanpassing.
- Smoke tests en `python3 scripts/ga4_fetch.py` konden in de developer-sessie niet draaien (sandbox-restrictie). Hans/PM moet ze handmatig draaien om de GA4-fix te valideren — verwacht 8 unieke weken in `weekly_trend`.

---

## Release — week van 19 mei 2026
**Deployment:** (na push / GitHub Pages — lokaal gevalideerd 02-05-2026)  
**Versie:** zie `git log -1 --oneline` op main na deze release — PM-cyclus: doorstroom FAQ + systemen-CTA + GA4-rapport

### Wat is er veranderd
- **Analytics:** verse GA4-export (`ga4_fetch.py` via project-`.venv`) en bijgewerkt `analytics_report.md` (2 mei).
- **Research & social:** `research_report.md` uitgebreid met PM-cyclus-update 2 mei; nieuwe `social/weekly_calendar.md` voor week 19 mei (LinkedIn/Instagram/Facebook-richting + diepe contact-URL’s).
- **`systemen-producten.html`:** vroege **cta-band** onder de hero naar prijsindicatie + link naar FAQ (korte verblijftijd in GA4 aangepakt).
- **Interne links naar FAQ en wizard:** `diensten.html`, `projecten.html`, `contact.html`, `prijsindicatie.html` met natuurlijke verwijzingen naar `faq.html` (en projecten ook naar prijsindicatie).
- **Stadspagina’s Groningen, Assen, Zuidlaren:** korte FAQ-regel onder de hero-CTA’s.
- **`index.html`:** in stap 2 van “4 stappen” linkt het woord **schuimbeton** naar `diensten.html#schuimbeton`.

### Waarom
Data toonde sterkere home- en contactpatronen, maar **zeer korte tijd** op systemen en **hoge bounce als landing** op stadspagina’s/projecten. FAQ staat live maar had nog weinig meetpad — interne links en vroege CTA’s verlagen de kans op “één hit en weg”.

### Verwacht effect
Meer sessies op `/faq.html`; langere engagement op `/systemen-producten.html`; vaker een tweede pagina per sessie vanaf stadspagina’s.

### Social media deze week
Zie `docs/website-manager/social/weekly_calendar.md` (week van 19 mei 2026).

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
