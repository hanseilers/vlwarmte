# Sprint — week van 2 juni 2026 (cyclus 8)

**PM beslissing genomen op:** 13-05-2026 (verse GA4-fetch `2026-05-13T09:08:07`)  
**Doel deze sprint:** City- en landingskwaliteit omhoog (Assen/Groningen + nieuwe Emmen), diensten- en systemen-instappers beter naar prijs/offerte leiden, voorbereid blijven op betaald verkeer (Ads-campagne staat ENABLED; conversies nog 0).  
**Meetdoel:** binnen 2–4 weken in GA4: (a) `vloerverwarming-assen.html` gem. sessieduur >0 en bounce <90%, (b) `diensten.html` landingsbounce <70%, (c) eerste organische sessies op `vloerverwarming-emmen.html`, (d) doorklik vanaf `systemen-producten.html` naar prijs/contact meetbaar hoger.

---

## Goedgekeurde taken voor Developer Agent

### Taak 1: `vloerverwarming-assen.html` — hero met beeld + trust `[GOEDGEKEURD]`
**Bron:** Analytics Agent (13-05) — 6 sessies, 0 s gem. duur, 100% bounce, 0 scrollers op 90d.  
**Prioriteit:** Hoog  
**Actie:** Vervang de kale tekst-hero door hetzelfde **twee-koloms patroon** als `projecten.html` (`project-hero`): echte foto uit `beeldmateriaal/`, `fetchpriority="high"`, trustregel (werkgebied, 1 werkdag, 10 jaar buisgarantie). Behoud alle bestaande CTA’s en vervolgsecties.  
**Succescriterium:** geldige HTML, LCP-vriendelijk beeld, geen regressie in navigatie/footer.

---

### Taak 2: `diensten.html` — keuzehulp eerste scherm `[GOEDGEKEURD]`
**Bron:** Analytics (landingsbounce `diensten.html` ~78,6%) + Marketing Research (keuzehulp).  
**Prioriteit:** Hoog (SEO + conversie: minimaal één SEO- en één CTA-taak)  
**Actie:** Direct onder de page-hero een sectie met **drie kaarten**: compleet traject (`werkwijze.html` + prijsindicatie), schuimbeton/kruipruimte (`#schuimbeton` + prijsindicatie), alleen systeem (`systemen-producten.html` + offerte-deeplink). Toon: nuchter, geen superlatieven.  
**Succescriterium:** crawlbaar statisch HTML, géén wizard-wijziging, kaarten zichtbaar vóór de bestaande “Wil je snel zien…”-cta-band.

---

### Taak 3: `systemen-producten.html` — landers helpen `[GOEDGEKEURD]`
**Bron:** Analytics — hoge bounce als landing op klein volume.  
**Prioriteit:** Midden (CTA)  
**Actie:** In de hero een korte **zoek-landen**-paragraaf + derde knop **Offerte aanvragen** (`contact.html?modus=offerte#aanvraag`) naast prijsindicatie en FAQ.  
**Succescriterium:** hero blijft leesbaar op mobiel; geen dubbele primaire styling (één primaire “prijsindicatie”, offerte secundair btn-styling is oké).

---

### Taak 4: Nieuwe stadspagina `vloerverwarming-emmen.html` `[GOEDGEKEURD]`
**Bron:** Marketing Research (Emmen als eerste city-gap).  
**Prioriteit:** Hoog (SEO — max. 1 nieuwe pagina)  
**Actie:** Nieuwe pagina gelijkwaardig aan bestaande stadspagina’s: unieke copy voor Emmen/Zuidoost-Drenthe, JSON-LD `Service`, GA4-deferred, `main.js`. Voeg toe aan **`sitemap.xml`**, footer **Regio**-lijst op alle root-HTML, en **“Ook actief in”**-kruislinks op Groningen, Assen, Zuidlaren.  
**Succescriterium:** canonical naar `/vloerverwarming-emmen.html`, interne links bidirectioneel waar passend.

---

### Taak 5: `vloerverwarming-groningen.html` — hero met beeld `[GOEDGEKEURD]`
**Bron:** Analytics — 87,5% bounce op stadspagina.  
**Prioriteit:** Midden  
**Actie:** Zelfde `project-hero`-patroon als Taak 1; gebruik **ander** beeld dan Assen om visuele duplicatie te beperken. Voeg trustregel toe.  
**Succescriterium:** layout consistent met Assen/Emmen-patroon; bestaande body-secties ongewijzigd.

---

## Uitgestelde voorstellen `[WACHT]`

- **Google Ads keyword/geo `--apply`**: campagne draait al ENABLED; script-mutaties wachten op aparte spend/check-ronde met expliciete PO-goedkeuring.  
- **`vloerverwarming-renovatie-houten-vloer.html`**: inhoudelijk waardevol, maar onder 5-takenlimiet na Emmen.  
- **`projecten.html` entry 100% bounce** op klein volume: eerst effect van cyclus 7-hero meten met nieuwe fetch.  
- **Hoogeveen / Meppel / Leeuwarden citypages**: volgende sprint na Emmen-evaluatie.

---

## Afgewezen voorstellen `[AFGEWEZEN]`

- **Root `index.html` hero opnieuw zetten** — geen regressie op net live trust-strip/sticky CTA; geen data-ondersteuning voor wijziging deze week.

---

## Social Media

**Status:** weekplanning week **26 mei 2026** staat in `docs/website-manager/social/weekly_calendar.md`.  
**Actie vereist:** handmatige publicatie door VLWarmte team.

---

## Context voor volgende sprint

- Meet **Assen/Groningen/projecten**-heroes: scrolled users + bounce in nieuwe 30d-venster.  
- **Paid Search 0 conversies** blijft — Marketing Research: Search Terms + GA4 landings per `google/cpc`, conversie-import controleren.  
- **Traffic-niveau:** week 6–12 mei 92 sessies vs 170 piekweek — trend blijven volgen.

---

## Developer Rapport — 13-05-2026 cyclus 8

### Geïmplementeerde taken

- **Taak 1 — Assen hero:** `page-hero` gebruikt nu `project-hero` met foto `beeldmateriaal/WhatsApp Image 2026-04-30 at 12.52.16.jpeg`, eyebrow, trustregel; “Ook actief” uitgebreid met Emmen; footer Regio 4 steden.  
- **Taak 2 — Diensten keuzehulp:** nieuwe `section section-muted` met drie `card`-routes direct onder hero.  
- **Taak 3 — Systemen landers:** zoekparagraaf + knop offerte-deeplink in hero-CTA-rij.  
- **Taak 4 — Emmen:** nieuw `vloerverwarming-emmen.html` (eigen copy), `sitemap.xml`, footers batch, kruislinks op stadspagina’s.  
- **Taak 5 — Groningen hero:** `project-hero` met `WhatsApp Image 2026-04-30 at 13.34.00.jpeg`, trustregel; “Ook actief” + footer bijgewerkt.

### Smoke tests

- **grep:** `vloerverwarming-emmen.html` voorkomt in `sitemap.xml` en footers van alle hoofd-HTML.  
- **Handmatig:** structuur `<main>` / secties gecontroleerd op open/sluit-balans in gewijzigde bestanden.

### Deployment

**Live** na `git push origin main` — GitHub Pages run **25784369037** (succes), E2E **25784370229**. Commit **`2f911bb`**.
