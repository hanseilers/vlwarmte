# Sprint — week van 19 mei 2026 (cyclus 6)

**PM beslissing genomen op:** 09-05-2026  
**Doel deze sprint:** verhoog conversiekwaliteit voor affluent huiseigenaren in Noord-Nederland door trust-hiërarchie, paid-landing message-match en frictieverlaging in contact- en prijsflow.  
**Meetdoel:** binnen 2-4 weken in GA4: hogere doorklik naar contact/prijsindicatie vanaf home, betere offerte-mode submit-rate, en beter presterende paid landings.

---

## Goedgekeurde taken voor Developer Agent

### Taak 1: Premium trust-strip boven de vouw op home `[GOEDGEKEURD]`
**Bron:** Adversarial UX review + paid intent mismatch.  
**Prioriteit:** Hoog  
**Actie:** Voeg op `index.html` direct onder hero-copy een compacte trust-strip toe met 3-4 harde signalen: werkgebied (Drenthe/Groningen/Friesland), reactietijd (binnen 1 werkdag), 10 jaar garantie op buis, een aanspreekpunt van opname t/m oplevering.  
**Succescriterium:** trust-signalen zichtbaar zonder scroll op gangbare desktop; mobiel direct na hero zichtbaar zonder de primaire CTA te verdringen.

---

### Taak 2: Consultative pre-form blok op contact `[GOEDGEKEURD]`
**Bron:** Adversarial UX review (form effort before confidence).  
**Prioriteit:** Hoog  
**Actie:** Voeg op `contact.html` boven de tab-switch (`informatie/offerte/bel`) een kort blok toe: "Zo werkt het na insturen" (3 stappen + reactietijd + wat klant terugkrijgt).  
**Succescriterium:** blok staat boven het formulier, compact en scanbaar; bestaande tab-functionaliteit en deep links (`?modus=...#aanvraag`) blijven intact.

---

### Taak 3: Premium visual variant voor prijswizard opties `[GOEDGEKEURD]`
**Bron:** Adversarial design review (calculator voelt deels te speels).  
**Prioriteit:** Hoog  
**Actie:** Pas in `prijsindicatie.html` de keuze-kaarten aan naar professionelere visuele stijl (minder emoji-dominant, neutralere iconografie/labels), zonder logica of volgorde van de wizard te veranderen.  
**Succescriterium:** wizardflow en eventtracking blijven gelijk; UI oogt rustiger en vakinhoudelijker, met behoud van duidelijke keuze-affordance.

---

### Taak 4: Message-match op paid landings aanscherpen `[GOEDGEKEURD]`
**Bron:** Google Ads/GA4 analyse + landing review.  
**Prioriteit:** Hoog  
**Actie:** Harmoniseer bovenste copy en primaire CTA op:
- `prijsindicatie.html`
- `contact.html?modus=offerte#aanvraag`

Focus op zoekintentie "kosten / offerte / schuimbeton", met eenduidige vervolgstap per pagina.  
**Succescriterium:** copy sluit aantoonbaar aan op Ads-thema's in `scripts/data/google_ads_lead_campaign_defaults.json`; geen conflicterende primaire CTA's in dezelfde eerste viewport.

---

### Taak 5: Trackinghygiëne voor attributie en CRO `[GOEDGEKEURD]`
**Bron:** GA4 toont relatief hoog `Unassigned` aandeel.  
**Prioriteit:** Midden  
**Actie:** Controleer en corrigeer waar nodig trackingflow rond landings en leadinteracties (met name paid-deeplinks en formulier/wizard events), zonder functionele regressie.  
**Succescriterium:** documenteer in sprint developer-rapport welke checks zijn gedaan; events blijven afgaan; kanaaltoewijzing wordt consistenter in opvolgende GA4-metingen.

---

## Uitgestelde voorstellen `[WACHT]`

- Nieuwe image-led campagne (PMax) met alleen `beeldmateriaal/` assets.
- Volledige herstructurering van city pages buiten interne linking en CTA-optimalisaties.
- Uitgebreide contentmigratie van FAQ naar intent-specifieke landings.

---

## Afgewezen voorstellen `[AFGEWEZEN]`

- Nieuwe losse website of aparte calculator-app buiten huidige `prijsindicatie.html`.

---

## Social Media

**Status:** weekplanning staat in `docs/website-manager/social/weekly_calendar.md`.  
**Actie vereist:** handmatige publicatie door VLWarmte team.

---

## Context voor volgende sprint

- Effectmeting op bovenstaande UX/CRO wijzigingen combineren met Ads-searchtermen en kanaalverdeling.
- Paid Search follow-up na ad review completion en eerste nieuwe impressie/klikdata.
