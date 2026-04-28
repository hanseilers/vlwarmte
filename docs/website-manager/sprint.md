# Sprint — week van 27 april 2026

**PM beslissing genomen op:** 27-04-2026 06:30
**Doel deze sprint:** Meetbaarheid op orde krijgen en de eerste twee organische instappen voor lokale zoekopdrachten bouwen — zodat over 4 weken zichtbaar is wat werkt.
**Meetdoel:** Per 25 mei 2026 in GA4: minimaal 1 bevestigde wizard-conversie geregistreerd als event, en in Search Console minstens 1 stedelijke landingspagina die vertoningen krijgt op "vloerverwarming Groningen" of "vloerverwarming Assen".

---

## Goedgekeurde taken voor Developer Agent

### Taak 1: GA4 conversie-events op wizard en contact `[GOEDGEKEURD]`
**Bron:** Analytics Agent (voorstel 1) + Marketing Research (sectie 5)
**Prioriteit:** Hoog
**Actie:**
- In `prijsindicatie.html`: voeg `gtag('event', ...)` calls toe op `wizard_start` (bij eerste keuze in stap 1), `wizard_step_2`, `wizard_step_3`, `wizard_calculate` (bij druk op bereken-knop) en `wizard_lead_submit` (bij verzending lead-formulier).
- In `contact.html`: voeg `gtag('event', 'contact_submit', { soort_aanvraag: '...' })` toe in de submit-handler, met `soort_aanvraag` ingesteld op `informatie` / `offerte` / `terugbelverzoek` afhankelijk van de gekozen modus.
- Eén regel comment per event-locatie, niet meer.
**Succescriterium:** Doorloop wizard en contactformulier handmatig; in de GA4 DebugView verschijnen alle events binnen 30 seconden.

### Taak 2: Google Search Console verificatie-tag plaatsen `[GOEDGEKEURD]`
**Bron:** Analytics Agent (voorstel 2)
**Prioriteit:** Hoog
**Actie:** Voeg in de `<head>` van alle 10 HTML-pagina's (`index.html`, `diensten.html`, `werkwijze.html`, `over-ons.html`, `projecten.html`, `contact.html`, `systemen-producten.html`, `prijsindicatie.html`, `disclaimer.html`, `privacy.html`) de meta-tag toe:
`<meta name="google-site-verification" content="REPLACE_WITH_TOKEN" />`
Plaats een TODO-comment ernaast: `<!-- TODO Hans: vervang door echte token uit Search Console -->`. De daadwerkelijke koppeling en sitemap-indiening doet Hans handmatig in Search Console — de developer levert de tag-plek.
**Succescriterium:** Tag staat op alle 10 pagina's, op identieke plek in `<head>`, exact dezelfde placeholder. Hans hoeft alleen de token te vervangen en te pushen.

### Taak 3: Locatiepagina `vloerverwarming-groningen.html` `[GOEDGEKEURD]`
**Bron:** Analytics Agent (voorstel 3) + Marketing Research (sectie 1, prio 1)
**Prioriteit:** Hoog
**Actie:** Nieuwe pagina, gebaseerd op structuur van `diensten.html`. Vereist:
- `<title>`: "Vloerverwarming Groningen — installateur uit Zuidlaren | VLWarmte"
- `<meta name="description">`: "Vloerverwarming in Groningen door VLWarmte — complete trajecten van ondervloer tot oplevering. 15 minuten reistijd vanaf Zuidlaren. Vraag een prijsindicatie aan."
- `<link rel="canonical" href="https://www.vlwarmte.nl/vloerverwarming-groningen.html">`
- H1: "Vloerverwarming Groningen"
- 300–500 woorden lokale inhoud: 15 min reistijd vanaf Zuidlaren, plaatsen die we bedienen (Helpman, Haren, Paterswolde, Hoogkerk, Beijum, omliggende dorpen), nieuwbouw vs renovatie kort, koppeling naar wizard.
- Eén H2-blok "Vloerverwarming infrezen in Groningen" (3 alinea's) — vangt long-tail af.
- Schema.org `Service` met `areaServed` = "Groningen" en `provider` referentie naar bestaande `LocalBusiness` (zelfde patroon als index.html).
- CTA-blok bovenaan en onderaan met telefoon + link naar `prijsindicatie.html`.
- **Niet** toevoegen aan hoofdnavigatie (wordt te lang). **Wel** toevoegen aan footer onder "Regio" als linkje "Vloerverwarming Groningen".
- Toevoegen aan `sitemap.xml` met `lastmod` van vandaag en `priority` 0.8.
- GA4 tracking-snippet meekopiëren.
**Succescriterium:** Pagina valideert HTML, opent zonder JS-fouten, schema.org-snippet in Rich Results Test correct, footer-link werkt op alle pagina's.

### Taak 4: Locatiepagina `vloerverwarming-assen.html` `[GOEDGEKEURD]`
**Bron:** Analytics Agent (voorstel 3) + Marketing Research (sectie 1, prio 2)
**Prioriteit:** Hoog
**Actie:** Identiek format als taak 3, met inhoudelijke aanpassingen voor Assen:
- `<title>`: "Vloerverwarming Assen — installateur uit Zuidlaren | VLWarmte"
- `<meta name="description">`: "Vloerverwarming in Assen door VLWarmte — complete trajecten van ondervloer tot oplevering. 20 minuten reistijd vanaf Zuidlaren. Vraag een prijsindicatie aan."
- `<link rel="canonical" href="https://www.vlwarmte.nl/vloerverwarming-assen.html">`
- H1: "Vloerverwarming Assen"
- Lokale inhoud: 20 min reistijd, plaatsen (Marsdijk, Assen-Oost, Loon, Anreep, omliggende dorpen tot Beilen/Rolde), nadruk op renovatie en infrezen (groot deel woningvoorraad).
- Eén H2 "Vloerverwarming infrezen in Assen en omgeving".
- Schema.org `Service` met `areaServed` = "Assen".
- Footer-link, sitemap-entry, GA4-snippet idem.
**Succescriterium:** Zelfde als taak 3.

### Taak 5: Projectenpagina tijdelijk uit hoofdnavigatie halen `[GOEDGEKEURD]`
**Bron:** Analytics Agent (voorstel 4)
**Prioriteit:** Hoog
**Actie:**
- Verwijder de `<a href="projecten.html">Projecten</a>` link uit de `<nav class="site-nav">` in alle pagina's waar hij staat (index, diensten, systemen-producten, werkwijze, over-ons, projecten zelf, contact, prijsindicatie, disclaimer, privacy).
- Laat `projecten.html` zelf staan (directe links blijven werken), verwijder de `projecten.html`-regel uit `sitemap.xml`.
- Voeg bovenaan `projecten.html` één korte alinea toe: "Deze projectenpagina vullen we in de komende weken aan met opgeleverde cases. Tot die tijd zijn we beter te beoordelen op onze [werkwijze](werkwijze.html) en [systemen](systemen-producten.html)."
**Succescriterium:** Geen "Projecten"-knop meer in de nav op alle pagina's, geen 404 op de URL, sitemap.xml mist de regel.

---

## Uitgestelde voorstellen `[WACHT]`

- **Dienstpagina `vloerverwarming-infrezen.html` (Analytics voorstel 5)** — Marketing research adviseert juist géén losse pagina maar een H2-sectie binnen de stedelijke landingspagina's. We volgen marketing: infrezen krijgt deze sprint twee H2-secties (in taak 3 en 4) en geen eigen pagina. Heroverwegen na 4 weken op basis van Search Console-data.
- **FAQ-pagina `faq.html` (Analytics voorstel 10, Marketing aanbeveling 3)** — Hoge waarde maar valt buiten de 5 taken deze sprint. Eerste kandidaat voor sprint 2 (week van 4 mei).
- **Reviews / sociaal bewijs op homepage (Analytics voorstel 6, Marketing aanbeveling 8)** — Vraagt eerst dat Hans Google Bedrijfsprofiel activeert en review-verzoeken stuurt; pas daarna ontwerpwerk. Wacht op input uit `social/input/` of bevestiging dat profiel actief is.
- **Mobiele check wizard + contact (Analytics voorstel 7)** — Niet door Developer Agent in te schatten zonder echt apparaat. Vraag aan Hans: doe een handmatige test op iPhone en gemiddelde Android. Bij issues: nieuwe sprint-taak.
- **Kostengids-pagina (Analytics voorstel 8)** — Marketing research adviseert dit binnen `prijsindicatie.html` op te vangen, niet als losse pagina. Heroverwegen na 4 weken.
- **Interne wizard-links systematisch (Analytics voorstel 9)** — Gedeeltelijk in taak 3 en 4 meegenomen via CTA-blok. Volledig uitrollen op `diensten.html`/`werkwijze.html`/`systemen-producten.html` in sprint 2.
- **Wizard tracking-event + referentie in resultaatkaart (Marketing aanbeveling 4)** — Tracking-event zit in taak 1. De referentie ("Vergelijkbaar met Haren, voorjaar 2025") wacht op concreet referentiemateriaal van Hans.
- **Projectenpagina vullen (Marketing aanbeveling 5)** — Wacht op klantmateriaal. Tot dan: verbergen (taak 5).
- **Schuimbeton ankersectie (Marketing aanbeveling 7)** — Klein klusje voor sprint 2 of 3.

---

## Afgewezen voorstellen `[AFGEWEZEN]`

- Geen — alle voorstellen zijn óf goedgekeurd, óf gemotiveerd uitgesteld.

---

## Social Media
**Status:** Weekplanning staat in `docs/website-manager/social/weekly_calendar.md`
**Actie vereist:** Handmatige publicatie door VLWarmte team. Foto's nog aanleveren voor 7 posts (zie `[FOTO NODIG: ...]` placeholders in de kalender).

---

## Context voor volgende sprint
- Verwacht eerste organische vertoningen op stedelijke termen vanaf week 3 na live-gang (rond 18 mei).
- GA4-data wordt op 24 mei opnieuw opgehaald — dat is het beslismoment voor het al dan niet doorzetten van wizard-conversie-experimenten en de eerste richtige A/B keuze.
- Belangrijkste open afhankelijkheid van Hans: (1) Google Search Console-token, (2) Google Bedrijfsprofiel review-actie, (3) materiaal voor projecten-cases en social posts.
- Sprint 2 kandidaten (in volgorde): FAQ-pagina, interne wizard-links volledig uitrollen, schuimbeton ankersectie, mobiele test follow-up.

---

## Developer Rapport — 27 april 2026

**Taak 1 — GA4 conversie-events op wizard en contact:** klaar (al uit vorige run; events `wizard_start`, `wizard_step_2`, `wizard_step_3`, `wizard_calculate`, `wizard_lead_submit` zitten in `prijsindicatie.html`; `contact_submit` met `soort_aanvraag` zit in `assets/js/main.js` submit-handler).
**Taak 2 — Search Console verificatie-tag:** klaar (placeholder `<meta name="google-site-verification" content="REPLACE_WITH_TOKEN" />` met TODO-comment toegevoegd aan alle 10 sprint-pagina's én aan beide nieuwe locatiepagina's).
**Taak 3 — `vloerverwarming-groningen.html`:** klaar (300+ woorden lokale inhoud, H2-blok over infrezen, schema.org Service met `areaServed` Groningen + provider-referentie naar LocalBusiness, dubbele CTA, GA4-snippet, footer-link op alle pagina's).
**Taak 4 — `vloerverwarming-assen.html`:** klaar (zelfde format, lokale plaatsen Marsdijk/Assen-Oost/Loon/Anreep/Rolde/Beilen, infrezen-H2, schema.org Service met `areaServed` Assen).
**Taak 5 — Projecten uit hoofdnav:** klaar (link weg uit nav op alle 9 pagina's waar hij stond + uit projecten.html zelf; intro-alinea met links naar werkwijze en systemen toegevoegd; sitemap-regel verwijderd).

**Sitemap:** `projecten.html` regel weg, beide nieuwe URL's met `lastmod=2026-04-27` en `priority=0.8` toegevoegd.
**Footer Regio-blok:** op alle 10 pagina's uitgebreid met linkjeslijst naar beide locatiepagina's. Op `prijsindicatie.html` is een nieuwe Regio-sectie tussen Bedrijf en Juridisch ingevoegd (had nog geen Regio-blok).

**Deployment:**
- Commit: `9e275a4` — "Sprint 27 april: GA4 events, Search Console-tag, twee locatiepagina's, projecten uit nav"
- GitHub Actions run: [`24982250357`](https://github.com/hanseilers/vlwarmte/actions/runs/24982250357) (pages build and deployment)
- Status: **completed / success** (gestart 27-04 09:31, klaar 09:32, duur 58s)
- Head SHA: `9e275a42b8140f2e12d169db2938f578e6539981`

**Live verificatie (27-04 09:33):**
- `https://www.vlwarmte.nl/` → HTTP 200, GA4-tag `G-0BB9M7HYSF` aanwezig
- `https://www.vlwarmte.nl/vloerverwarming-groningen.html` → HTTP 200, verificatie-tag aanwezig
- `https://www.vlwarmte.nl/vloerverwarming-assen.html` → HTTP 200

**Open punten voor Hans:**
1. Echte token uit Search Console plaatsen (12× zoeken-en-vervangen op `REPLACE_WITH_TOKEN` in alle HTML-pagina's).
2. Handmatige test: doorloop wizard en contactformulier in alle drie modi, controleer in GA4 DebugView dat alle events binnen 30s binnenkomen.
3. Sitemap.xml indienen in Search Console na verificatie (URL: `https://www.vlwarmte.nl/sitemap.xml`).
4. Markeer `wizard_lead_submit` en `contact_submit` als conversies in GA4 Beheer → Events.

**Aandachtspunten voor volgende sprint:**
- De twee nieuwe stadspagina's hebben nog geen lokaal referentieproject (foto + plaatsnaam) — zodra Hans materiaal aanlevert, vullen we dat aan.
- Mobiele check op wizard en contactformulier nog niet uitgevoerd (vraagt echt apparaat).
- Footer is op `prijsindicatie.html` qua structuur licht afwijkend (Regio-blok was er niet, nu wel toegevoegd) — in een toekomstige refactor kan de footer als één gedeelde include-component worden uitgewerkt.
