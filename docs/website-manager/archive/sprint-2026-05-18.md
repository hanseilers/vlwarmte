# Sprint — week van 9 juni 2026 (cyclus 9)

**PM beslissing genomen op:** 15-05-2026 (verse GA4-fetch `2026-05-15T12:48:01`)  
**Doel deze sprint:** City-cluster verder uitbreiden (Hoogeveen), landings- en prijs-SEO versterken, projecten- en contact-cold-landings beter laten doorstromen naar offerte/prijs, Assen-scroll engagement verbeteren.  
**Meetdoel:** binnen 2–4 weken in GA4: (a) eerste organische sessies op `vloerverwarming-hoogeveen.html`, (b) `projecten.html` landingsbounce <90%, (c) lagere bounce op cold `/contact.html` landings, (d) `prijsindicatie.html` landingsbounce duidelijk lager dan 64%, (e) Assen: >0 scrolled users in 90d-venster.

---

## Goedgekeurde taken voor Developer Agent

### Taak 1: Nieuwe stadspagina `vloerverwarming-hoogeveen.html` `[GOEDGEKEURD]`
**Bron:** Analytics + Marketing Research (volgende city na Emmen).  
**Prioriteit:** Hoog (SEO — max. 1 nieuwe pagina)  
**Actie:** Nieuwe pagina gelijkwaardig aan `vloerverwarming-emmen.html`: unieke copy voor Hoogeveen/midden-Drenthe-corridor, JSON-LD `Service`, GA4-deferred, `main.js`. Voeg toe aan **`sitemap.xml`**, footer **Regio** op alle root-HTML, en **“Ook actief in”**-kruislinks op Groningen, Assen, Emmen en Zuidlaren waar die blokken al bestaan.  
**Succescriterium:** canonical naar `/vloerverwarming-hoogeveen.html`, bidirectionele interne links waar passend.

---

### Taak 2: `projecten.html` — snellere route naar offerte `[GOEDGEKEURD]`
**Bron:** Analytics — entry `projecten.html` **100%** bounce (6 sessies), weinig scroll.  
**Prioriteit:** Hoog (CTA)  
**Actie:** In de hero-CTA-rij een **derde knop** `Offerte aanvragen` (`contact.html?modus=offerte#aanvraag`) naast bestaande prijsindicatie en bel-route. H1 iets compacter (zelfde verhaal, minder woorden) zodat de CTA-rij op mobiel sneller zichtbaar is.  
**Succescriterium:** geen dubbele primaire styling (één primaire “prijsindicatie”); offerte secundair; geldige HTML.

---

### Taak 3: `prijsindicatie.html` — crawlbare kosten-sectie vóór wizard `[GOEDGEKEURD]`
**Bron:** Analytics — `prijsindicatie.html` als landing **64,7%** bounce; Marketing — crawlbare prijsdrivers voor SEO.  
**Prioriteit:** Hoog (SEO)  
**Actie:** Verplaats de bestaande statische sectie `#kosten-uitleg` **boven** de wizard (direct na de `cta-band` met “Start de wizard”). Verwijder de dubbele sectie onderaan. Behoud interne links en disclaimers; geen wizard-logica wijzigen.  
**Succescriterium:** in HTML-bron staat substantiële kosten-uitleg vóór `#wizard`; wizard werkt ongewijzigd.

---

### Taak 4: `contact.html` — intentie-keuze boven modus-tabs `[GOEDGEKEURD]`
**Bron:** Analytics — `/contact.html` zonder query als landing **80%** bounce.  
**Prioriteit:** Midden (CTA)  
**Actie:** Binnen `#aanvraag`, direct **boven** de `mode-switch`, een compact blok met drie korte regels + links: Informatie (`?modus=informatie#aanvraag`), Offerte (`?modus=offerte#aanvraag`), Bel mij (`?modus=bel#aanvraag`) — zelfde URL’s als de tabs gebruiken; geen extra formulieren.  
**Succescriterium:** tabs blijven werken; nieuwe blok is semantisch correct en leesbaar op mobiel.

---

### Taak 5: `vloerverwarming-assen.html` — scroll-prompt naar inhoud `[GOEDGEKEURD]`
**Bron:** Analytics — Assen **0 scrolled users (90d)** ondanks nieuwe hero.  
**Prioriteit:** Midden  
**Actie:** In de hero-copy een zichtbare tekstlink **“Lees verder”** naar het eerste inhoudelijke blok (anker op de sectie met “Waarom … Assen”). Geen extra zware afbeeldingen.  
**Succescriterium:** geldig anker; geen LCP-regressie.

---

## Uitgestelde voorstellen `[WACHT]`

- **Google Ads keyword/geo `--apply`:** zonder expliciete spend-goedkeuring geen mutaties; conversie-import eerst meten.  
- **`vloerverwarming-renovatie-houten-vloer.html`:** inhoudelijk waardevol; wacht op Hoogeveen-evaluatie.  
- **Leeuwarden / Meppel citypages:** backlog na Hoogeveen.

---

## Afgewezen voorstellen `[AFGEWEZEN]`

- **Root `index.html` hero wijzigen** — geen nieuwe data-ondersteuning; focus op landings met harde bounce-cijfers.

---

## Social Media

**Status:** weekplanning week **2 juni 2026** staat in `docs/website-manager/social/weekly_calendar.md`.  
**Actie vereist:** handmatige publicatie door VLWarmte team.

---

## Context voor volgende sprint

- Meet **Hoogeveen** indexering + stad-cluster CTR.  
- **Paid 0 conversies** — Marketing/PM: GA4 ↔ Ads conversies en Search Terms.  
- **Diensten** landingsbounce: keuzehulp staat kort live — volgende fetch beoordelen.

---

## Developer Rapport — 15-05-2026 cyclus 9

### Geïmplementeerde taken

- **Taak 1 — Hoogeveen:** nieuw `vloerverwarming-hoogeveen.html`, `sitemap.xml`, footers batch, kruislinks op Groningen/Assen/Emmen/Zuidlaren.  
- **Taak 2 — Projecten:** kortere H1/lead, derde CTA **Offerte aanvragen** (deeplink) in hero.  
- **Taak 3 — Prijsindicatie:** sectie `#kosten-uitleg` verplaatst naar **vóór** `#wizard`; disclaimercopy aangepast.  
- **Taak 4 — Contact:** `contact-intent-strip` boven mode-switch met drie deeplinks.  
- **Taak 5 — Assen:** anker `id="waarom-vlwarmte-assen"` + lees-verder-link in hero.

### Smoke tests

- **Handmatig:** `grep` op `vloerverwarming-hoogeveen` in `sitemap.xml` en footers; prijsindicatie: één `#kosten-uitleg`, wizard-blok gevolgd door `</main>` zonder dubbele sectie.

### Deployment

**Live** na `git push origin main` — GitHub Pages run **25914206844** (succes), E2E **25914207646** (IMAP E2E overgeslagen: geen `IMAP_USER` / `IMAP_PASSWORD` secrets op de repo). Commit **`d2bea47`**.
