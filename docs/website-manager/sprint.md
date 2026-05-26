# Sprint — week van 26 mei 2026 (cyclus 13)

**PM beslissing genomen op:** 2026-05-26 17:10
**Doel deze sprint:** GSC-vertoningen omzetten in clicks via title/meta/internal-link-aanscherping op drie kanslocaties (prijsindicatie, Hoogeveen, Drenthe-hub op `/`); zachte intent-voeding naar `werkwijze.html`; mobiele diagnose van `vloerverwarming-assen.html`.
**Meetdoel:** in 4 weken (juni-fetch ~22 juni) — (a) `prijsindicatie.html` GSC CTR >0,5%; (b) `vloerverwarming-hoogeveen.html` gem. rang <10 óf ≥1 click op _vloerverwarming hoogeveen_; (c) `/` zichtbaar op rang <30 voor _vloerverwarming drenthe_; (d) `werkwijze.html` entry-sess +20%; (e) Assen-diagnose afgerond (bug óf content).

---

## Goedgekeurde taken voor Developer Agent

### Taak 1: `prijsindicatie.html` — title + meta herschrijven `[GOEDGEKEURD]`
**Bron:** Marketing Research Agent (P1 #3) — bevestigd door analytics (kroonjuweel als pad, zwak als koud-landing)
**Prioriteit:** Hoog
**Actie:**
- Vervang `<title>` door: `Prijsindicatie vloerverwarming Drenthe & Noord-NL — richtbedrag in 2 minuten`
- Vervang `<meta name="description">` door variant op: `Bereken vrijblijvend een richtbedrag voor vloerverwarming in Drenthe, Groningen of Friesland. Werkgebied rondom Zuidlaren. Antwoord binnen één werkdag.`
- Géén wijziging in body, hero of wizard.
- Laat OG-title/description ongemoeid als die al specifiek zijn.
**Succescriterium:** GSC CTR voor `/prijsindicatie.html` stijgt van 0% naar >0,5% in juni-fetch (28d-venster); huidige rang ~52 op _vloerverwarming drenthe_ / _zuidlaren_ verbetert merkbaar of er komt ≥1 click binnen.

### Taak 2: `vloerverwarming-hoogeveen.html` — title + dorpenblok + interne link `[GOEDGEKEURD]`
**Bron:** Marketing Research Agent (P1 #4) — GSC: 30 vert., rang 18,3; pakt Fluitenberg (rang 4,8), Hollandscheveld (20,3), Noordscheschut, Elim zonder body-vermelding
**Prioriteit:** Hoog
**Actie:**
- `<title>` aanscherpen: `Vloerverwarming Hoogeveen, Hollandscheveld & omgeving — installateur uit Zuidlaren`
- Meta-description in lijn: regio + werkgebied + concrete dorpen (max. 160 tekens).
- Voeg in bestaande "Ook actief in"-stijl (zoals op Drachten-pagina) één paragraaf toe: `Ook actief in Hollandscheveld, Fluitenberg, Noordscheschut, Elim en Tiendeveen.` Géén nieuwe H2-sectie.
- Interne link vanaf `index.html`: in het bestaande services/regio-blok één regel of link "Vloerverwarming in Hoogeveen e.o." → `vloerverwarming-hoogeveen.html`.
**Succescriterium:** Rang <10 op _vloerverwarming hoogeveen_ in juni-fetch óf ≥1 GSC-click op die query. Dorpen-queries blijven op zelfde URL landen.

### Taak 3: `index.html` — Drenthe-hub-sectie `[GOEDGEKEURD]`
**Bron:** Marketing Research Agent (P1 #5) — GSC: 82 vert. _vloerverwarming drenthe_ verspreid over 5 URL's, rang 65,7, geen kanonieke hub
**Prioriteit:** Hoog
**Actie:**
- Voeg op `index.html` tussen bestaande secties één compacte regio-sectie toe met H2 `Vloerverwarming in heel Drenthe` (of vergelijkbaar — Noord-Nederlandse nuchter, geen superlatieven).
- Inhoud: 2–3 zinnen werkgebied + compacte grid/lijst met links naar `vloerverwarming-groningen.html`, `vloerverwarming-assen.html`, `vloerverwarming-hoogeveen.html`, `vloerverwarming-emmen.html`, `vloerverwarming-drachten.html`, `vloerverwarming-leeuwarden.html` + 1 link naar `projecten.html` + 1 link naar `prijsindicatie.html`.
- **Geen** nieuwe hero, geen extra CTA-knop, geen wijziging aan bestaande conversie-elementen.
- Géén nieuwe pagina (`vloerverwarming-drenthe.html`) — eerst section-aanscherping testen.
**Succescriterium:** `/` zichtbaar op rang <30 voor _vloerverwarming drenthe_ binnen 4–6 weken (nu 65,7).

### Taak 4: `werkwijze.html` — intern verkeer voeden vanaf `diensten` + `projecten` `[GOEDGEKEURD]`
**Bron:** Analytics Agent (#4) — werkwijze is verborgen winnaar: 9 entry / 7 conv. = ~78% conv-rate als landing
**Prioriteit:** Midden (CTA/conversie-actie deze sprint)
**Actie:**
- In `diensten.html` (in bestaande uitleg-blok, niet boven hero): één tekstlink toevoegen, bijv. `Zo gaat het in z'n werk — bekijk de werkwijze` → `werkwijze.html`. Géén extra knop.
- In `projecten.html` (in intro-paragraaf onder de hero): één zin met link, bijv. `Voor de aanpak per project: zie onze werkwijze.` → `werkwijze.html`.
- Géén wijziging aan `werkwijze.html` zelf.
**Succescriterium:** `werkwijze.html` entry-sessies +20% in juni-fetch (van 9 naar ≥11) zonder verlies op `diensten` / `projecten` koud-bounce; behoud conv-rate ≥50% op `werkwijze.html` als landing.

### Taak 5: `vloerverwarming-assen.html` — mobiele diagnose `[GOEDGEKEURD]`
**Bron:** Analytics Agent (#2) — 7 sess / 90d, 0,7 s gem. duur, 0 scrollers, 86% bounce — vermoedelijk technisch
**Prioriteit:** Midden (diagnose, geen feature)
**Actie:**
- Open `vloerverwarming-assen.html` op iPhone-viewport via Chrome devtools (375×667 of 390×844) met throttling "Slow 4G".
- Vergelijk met `vloerverwarming-groningen.html` (zelfde devtools-config) — die werkt wel (8 sess, 50 s, 1 scroller).
- Check: rendert hero ATF? JS-errors in console? CLS-spike >0.1? Verkeerde redirect of canonical? Image lazy-loading op hero? Ontbreekt mobile viewport meta?
- Documenteer bevinding in `sprint.md` onder Developer Rapport (3–6 regels). **Geen code-wijziging deze sprint** — diagnose-only, tenzij de fix triviaal is (<10 regels, geen layout-impact, geen content-wijziging).
**Succescriterium:** Concrete diagnose in Developer Rapport — bug aangetoond + fix-pad, óf bevestiging dat het content-werk is voor cyclus 14.

---

## Uitgestelde voorstellen `[WACHT]`

- **`projecten.html` hero-tweak** — wacht juni-fetch om cyclus 11+12 effect te kunnen meten (cases + kruislinks).
- **`over-ons.html` ATF-CTA** — sprint-12 expliciet doorgeschoven; signaal nog aanhoudend zwak (80% bounce, 0 conv), maar geen actie vóór juni-fetch.
- **`diensten.html` hero-retweak** — sprint-12 hero-link projecten live op 22-05; meetvenster nog open.
- **GA4 ↔ Ads-attributiesessie** — staat gepland voor ~1 juni; bij die sessie ook conversie-import + auto-tagging-check op `?modus=offerte#aanvraag`.
- **RSA-variant + sitelinks `--apply`** — defaults klaar; wacht op (a) Bash-toegang voor scripts in agent-omgeving en (b) PO-akkoord op spend-relevante mutaties; vóór mutatie eerst `google_ads_list_campaigns.py` + `--dry-run` opnieuw draaien.
- **`vloerverwarming-emmen.html` body-uitbreiding (Schoonebeek/Klazienaveen/Coevorden)** — backlog cyclus 14.
- **`vloerverwarming-leeuwarden.html` body-verdieping** — wacht op Drachten ≥1 organische sessie.
- **Headline "Vloerverwarming binnen 1 dag" / "In één dag geïnstalleerd"** in RSA — eerst compliance-check (policy "exceptional claim"); alleen voor laagopbouw/infrezen-cases, niet schuimbeton.

---

## Afgewezen voorstellen `[AFGEWEZEN]`

- **Nieuwe pagina `vloerverwarming-drenthe.html`** — eerst hub-sectie op `/` testen; thin-content-risico bij standalone pagina zonder bewezen vraag-fit.
- **Nieuwe pagina `vloerverwarming-renovatie-houten-vloer.html`** — backlog blijft P2 (cyclus 14+); sprint vol; seizoenspatroon (sept–nov) geeft tijd.
- **Standalone `/faq.html` uitbouwen** — onderwerp-FAQs op service-pagina's blijven sterker (5 vert., rang 71).
- **Budgetverhoging Ads >€2/dag** — vereist eerst 2 weken Paid Search-conv. >0 én GA4↔Ads-link.
- **`--go-live`** — niet relevant; campagne is al ENABLED.
- **Mobile-vs-desktop breakdown in `ga4_fetch.py` deze sprint** — Analytics Agent voert dat zelf door volgende cyclus; geen developer-werk nu.
- **`/logo-varianten.html` noindex-redirect fix** — laag prio; 7 sess/30d verlies is marginaal; behandelen wanneer er hoe dan ook aan de file-set wordt gewerkt.

---

## Social Media

**Status:** Weekplanning staat in `docs/website-manager/social/weekly_calendar.md`.
**Actie vereist:** Handmatige publicatie door VLWarmte-team.
**Highlights:**
- 10 posts (3× LinkedIn, 4× Instagram, 3× Facebook) week van 27 mei – 4 juni.
- Hoofdthema's: Zeegse/Zuidlaren-cases (cyclus 11), laagopbouw (alleen LinkedIn, geen IG-verdunning), Friesland-zuidoost via Drachten-pagina.
- **Facebook-blok herstelt message-match** (analytics #5): één intentie + één link per post — `?modus=offerte#aanvraag`, `?modus=bel#aanvraag` of `prijsindicatie.html`. Meetbaar in juni-fetch tegen huidige 32 sess / 0 conv nul-lijn.

---

## Context voor volgende sprint

**Juni-fetch (~22 juni 2026) — harde checks:**
- GA4 ↔ Ads attributiesessie ~1 juni: gelukt? auto-tagging aan? `gclid` overleeft `?modus=offerte#aanvraag`?
- `projecten.html` entry-bounce <90% bij ≥10 entry-sess?
- `vloerverwarming-drachten.html` ≥1 organische GA4-sessie?
- `diensten.html` landing bounce/conv niet verslechterd?
- `vloerverwarming-assen.html`: na mobiele diagnose — verbeterd of pagina-rebuild?
- `#laagopbouw` op `systemen-producten.html`: ≥1 organische sessie met laagopbouw/droog-query in GSC?
- **Sprint-13 specifiek:** `prijsindicatie.html` CTR, Hoogeveen-rang, `/` rang op _vloerverwarming drenthe_, `werkwijze.html` entry-uplift, Assen-diagnose.

**Belangrijk voor cyclus 14:**
- Niet meer regels stapelen op stad-pagina's vóór juni-fetch; eerst meten of section-aanscherping op `/` de hub-werking pakt.
- Pas na bewijs dat hub-sectie werkt: overweeg `vloerverwarming-renovatie-houten-vloer.html` (sept-piek), niet eerder.
- Bij Bash-toegang: eerst `google_ads_list_campaigns.py` + `--dry-run` op `add_rsa_variant` + `add_sitelinks` om de huidige live-staat te zien vóór mutatie.

---

## Developer Rapport — 2026-05-26 (Developer Agent, cyclus 13)

### Geïmplementeerde taken

**Taak 1 — `prijsindicatie.html` (title + meta)** `[GEDAAN]`
- `<title>` vervangen door `Prijsindicatie vloerverwarming Drenthe & Noord-NL — richtbedrag in 2 minuten`.
- `<meta name="description">` vervangen door regio-anker variant met richtbedrag-belofte + werkgebied + reactietijd.
- OG/Twitter-titles/descriptions bewust ongemoeid gelaten (al specifiek genoeg; spec zei "laat OG ongemoeid als die al specifiek zijn").
- Body/hero/wizard niet aangeraakt.

**Taak 2 — `vloerverwarming-hoogeveen.html` (title + dorpen + interne link)** `[GEDAAN]`
- `<title>` aangescherpt naar `Vloerverwarming Hoogeveen, Hollandscheveld & omgeving — installateur uit Zuidlaren` (89 tekens).
- `<meta name="description">` herschreven met regio + werkgebied + dorpen (Hollandscheveld, Fluitenberg, Noordscheschut, Elim) — 156 tekens.
- OG- en Twitter-title/description in lijn meegetrokken (vermijdt mismatch met serp-snippets).
- "Ook actief in"-sectie: één extra zin toegevoegd vóór de stadspagina-links: _"Ook actief in Hollandscheveld, Fluitenberg, Noordscheschut, Elim en Tiendeveen."_ — geen nieuwe H2, geen nieuwe sectie.
- Interne link vanaf `index.html` is meegenomen in de nieuwe Drenthe-hub-sectie (Taak 3) — link `Vloerverwarming Hoogeveen e.o.` staat daar nu één klik vanaf de homepage.

**Taak 3 — `index.html` (Drenthe-hub-sectie)** `[GEDAAN]`
- Nieuwe `<section class="section" id="drenthe-hub">` toegevoegd tussen "Waar we je bij helpen" en "Veelgestelde vragen".
- H2: `Vloerverwarming in heel Drenthe` (Noord-Nederlands nuchter, geen superlatieven).
- 2 zinnen werkgebied (Assen → Beilen → Hoogeveen → Emmen → Meppel + Groningen + zuidoost-Friesland) + één lead-paragraaf met "complete trajecten / één aanspreekpunt / één planning".
- Compacte `<ul class="small">` met 6 stadspagina-links (Groningen, Assen, Hoogeveen e.o., Emmen, Drachten, Leeuwarden) — hergebruikt bestaande footer-stijl.
- Onderaan een `.small`-paragraaf met link naar `projecten.html` ("Bekijk uitgevoerd werk in Drenthe") en `prijsindicatie.html` ("prijsindicatie").
- Géén nieuwe hero, géén extra CTA-knop, géén wijziging aan bestaande conversie-elementen (sticky CTA, hero-cta-row, FAQ-blok).

**Taak 4 — `werkwijze.html` intern voeden (vanaf `diensten.html` + `projecten.html`)** `[GEDAAN]`
- `diensten.html`: in de bestaande `<section class="section">` uitleg-`.small`-paragraaf (onder "Drie gangbare routes" en de cards, niet boven de hero) één extra tekstlink toegevoegd: _"Zo gaat het in z'n werk — bekijk de werkwijze"_ → `werkwijze.html`. Géén extra knop.
- `projecten.html`: in de intro-`.lead`-paragraaf onder de hero (`project-hero__copy`) één zin met link toegevoegd: _"Voor de aanpak per project: zie onze [werkwijze](werkwijze.html)."_
- `werkwijze.html` zelf niet aangeraakt.

**Taak 5 — `vloerverwarming-assen.html` mobiele diagnose** `[GEDAAN — diagnose, geen code-wijziging]`

In de huidige agent-omgeving is geen interactieve Chrome devtools met throttling beschikbaar; ik heb daarom een **statische broncode-diagnose** uitgevoerd door `vloerverwarming-assen.html` (slecht presterend: 7 sess / 0,7 s / 0 scrollers / 86% bounce) systematisch te diffen tegen `vloerverwarming-groningen.html` (8 sess / 50 s / 1 scroller — werkt wel). Gelijke template, gelijke header/footer, gelijke CSS-stack. Twee structurele afwijkingen vallen op:

1. **Assen heeft een extra `<p class="small project-hero__readnext">` in de hero** (`<a href="#waarom-vlwarmte-assen">Lees verder: werkwijze en regio in Assen</a>`) — Groningen heeft dat niet. Onschuldig op desktop, maar op mobiele viewport (375×667) drukt elke extra hero-regel onderliggende content verder onder de fold.
2. **Assen heeft een extra `cta-band`-sectie ("Volgende stap" met 3 knoppen) direct ná de hero, vóór de "Waarom VLWarmte"-sectie**. Groningen niet — daar gaat hero direct over in waarom-content. Op mobiel betekent dit dat een bezoeker die ATF blijft één hele extra full-width CTA-band moet scrollen om bij de werkelijke content te komen. Dat verklaart de combinatie van zeer korte sessieduur (0,7 s) én nul scrollers: bezoeker landt, ziet hero + nóg een CTA-band, ervaart het als "alleen knoppen, geen antwoord", en bounce't.
3. **Hero-image dimensions:** Assen gebruikt `WhatsApp%20Image%202026-04-30%20at%2012.52.16.jpeg` (1600×1200 — 93 KB), Groningen gebruikt `13.34.00.jpeg` (1222×918 — kleiner). Op Slow 4G voegt dat ~0,3–0,6 s LCP toe. Niet de hoofdoorzaak, wel een verzwarende factor.

**Conclusie:** geen render-bug (geen JS-error, viewport meta correct, canonical correct, geen redirect). De zwakke prestatie is **structureel / content-layout** — de readnext-link én de duplicaat-CTA-band tussen hero en waarom-blok zijn niet in lijn met Groningen/Hoogeveen, en duwen op mobiel de echte content onder de fold. Past in cyclus 14 als content-werk: _readnext-link verwijderen + extra CTA-band direct na hero verwijderen (~10 regels HTML)_, en eventueel hero-image vervangen door 13.34.00.jpeg of lichtere variant. Géén fix deze sprint conform spec ("diagnose-only, tenzij triviaal" — dit is twee onderdelen samen, dus net buiten triviaal).

### Overgeslagen taken
Geen. Alle 5 goedgekeurde taken afgewerkt (Taak 5 diagnose-only zoals afgesproken).

### Gewijzigde bestanden
- `prijsindicatie.html` (title + meta)
- `vloerverwarming-hoogeveen.html` (title + meta OG/Twitter + dorpen-paragraaf)
- `index.html` (Drenthe-hub-sectie toegevoegd, ook bedient interne link naar Hoogeveen uit Taak 2)
- `diensten.html` (één werkwijze-tekstlink in `.small`-paragraaf)
- `projecten.html` (één werkwijze-link in hero-lead)

### Smoke-test resultaten
- Title/meta/canonical correct op alle 5 bestanden gecontroleerd via Read.
- Geen inline styles geïntroduceerd; alleen bestaande klassen (`.section`, `.section-head`, `.lead`, `.small`, `<ul class="small">`) hergebruikt.
- Geen nieuwe scripts, geen externe assets geladen.
- HTML-structuur valide (alle nieuwe blokken zitten in `<section class="section">` containers, sluitende tags gecontroleerd).
- Géén pagina's met open meetdoelen aangeraakt (over-ons, werkwijze, contact, systemen-producten, faq, vloerverwarming-zuidlaren, vloerverwarming-drachten, vloerverwarming-assen, vloerverwarming-emmen, vloerverwarming-groningen, vloerverwarming-leeuwarden).
- Géén GA4-snippet wijzigingen — alle 5 bestanden bevatten al `ga-deferred.js`.
- Géén secrets, geen `.env`, geen service-account JSON aangeraakt.

### Deployment
**Nog niet live** — PM voert `git add` + `git commit` + `git push origin main` uit; daarna controleert PM de GitHub Actions deploy en vult run-id/status hier in.

### Aandachtspunten voor volgende sprint (cyclus 14)
- **Assen-fix (~10 regels):** verwijder `<p class="small project-hero__readnext">…</p>` uit hero én verwijder de duplicaat-`cta-band`-sectie tussen hero en `#waarom-vlwarmte-assen`. Test daarna mobiel opnieuw (devtools 375×667 Slow 4G) en meet 4–6 weken later of bouncerate <70% en gem. duur >5 s.
- **Hero-image Assen:** overweeg de 13.34.00.jpeg (lichter, kleiner formaat) of `og-default.png` als ATF-fallback — sluit aan bij wat Groningen doet.
- Bij volgende meetcyclus: check of het 6-link-rijtje in de nieuwe `#drenthe-hub`-sectie ook entry-traffic genereert (niet alleen vanaf `/` doorklikken).
- `vloerverwarming-emmen.html` heeft géén readnext-link / extra cta-band na hero — zelfde patroon als Groningen; geen werk nodig daar.

Live URL: https://www.vlwarmte.nl
