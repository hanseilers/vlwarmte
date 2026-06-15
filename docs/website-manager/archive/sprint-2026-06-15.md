# Sprint — week van 9 juni 2026 (cyclus 16)

**PM beslissing genomen op:** 2026-06-08 06:20
**Doel deze sprint:** De vraag verzilveren die nu op het scherm blijft liggen — page-1-posities zonder clicks oogsten (titels/meta), het Drenthe-signaal bundelen, en koude bezoekers op `projecten.html` naar de bewezen offerte-deeplink leiden.
**Meetdoel (juni-fetch ~22 juni, vol sample):** (a) ≥1–2 organische clicks op de Zuid-Laren/Hoogeveen-termen die nu 0 clicks halen (GSC-CTR van 0% af); (b) `vloerverwarming drenthe` consolideert op één pagina en stijgt richting top-30; (c) `projecten.html` bounce van 60% richting <50% met een duidelijke offerte-CTA.

> **Macrobeeld deze cyclus (verse fetch 08-06, 06:05):** verkeer is laag — ~16 sess/week, 149 sess/30d (de april-piek valt uit het venster). De cyclus-15-deploy stond pas ~14 uur vóór de fetch, dus de meetdoelen van cyclus 15 zijn **nog niet eerlijk te toetsen** (juni-fetch is het ijkpunt). Lichtpunt: `prijsindicatie.html` pageview-bounce 35,5% → 31,8%, gem. duur 73 → 100 s — de pagina werkt; het knelpunt is de **koude entry**, niet de pagina.

> **P0 buiten deze developer-sprint (escalatie — zie onder):** Paid Search-volume is ingestort (11 → 1 sessie) en de gouden offerte-deeplink viel terug van 11 sess/10 conv. naar 1/0. Totale conversies −44% (63 → 35). Dit wijst op een **gepauzeerde of uitgeputte Ads-campagne** (`23834672782`) of een attributieverschuiving. Dit is geen HTML-werk; het vraagt Ads-verificatie + de GA4↔Ads-koppeling (P0 sinds cyclus 14).

---

## Goedgekeurde taken voor Developer Agent

### Taak 1: Title + meta-description CTR-fix op `index.html` en `vloerverwarming-hoogeveen.html` `[GOEDGEKEURD]`
**Bron:** Marketing Research Agent (GSC) + Analytics Agent
**Prioriteit:** Hoog
**Actie:** Herschrijf alleen `<title>` en `<meta name="description">` — géén layout- of contentwijziging.
- `index.html`: huidige title is `VLWarmte | Vloerverwarming van ondervloer tot oplevering`. GSC toont page-1-posities met **0 clicks**: `vloerverwarming zuidlaren` (pos 9,3 / 33 impr), `installatiebedrijf zuidlaren` (pos 6,5 / 20 impr), `installateur zuidlaren` (pos 3,7). Zet de lokale term + intentie vóóraan en voeg een concrete USP toe. Voorstel-richting (developer mag verfijnen, ≤60 tekens title / ≤155 tekens meta):
  - title: `Vloerverwarming Zuidlaren & Noord-NL — installateur | VLWarmte`
  - meta: nuchtere USP, bv. heel traject ondervloer→oplevering, eigen ploeg, reactie binnen 1 werkdag, 10 jaar garantie op de buis.
- `vloerverwarming-hoogeveen.html`: title is al redelijk (`Vloerverwarming Hoogeveen, Hollandscheveld & omgeving — installateur uit Zuidlaren`). GSC: `vloerverwarming hoogeveen` (pos 10,6), `vloerverwarming fluitenberg` (pos 4,8), 0 clicks. Houd Hoogeveen vooraan, scherp de **meta-description** aan zodat hij uitnodigt tot klikken (concrete USP + regio, geen superlatieven).
**Succescriterium:** Beide pagina's hebben een herschreven title én meta met lokale term vooraan en een concrete, nuchtere USP; geen andere wijzigingen in de body; pagina's renderen correct. (Effect: GSC-CTR >0% op deze termen bij juni-fetch.)

### Taak 2: Drenthe-signaal bundelen met interne links `[GOEDGEKEURD]`
**Bron:** Marketing Research Agent (GSC)
**Prioriteit:** Midden
**Actie:** `vloerverwarming drenthe` haalt 82 impressies / pos 65,7 / 0 clicks, verspreid over `/`, `prijsindicatie.html` en `diensten.html` — Google kiest geen duidelijke pagina. Voeg natuurlijke, contextuele interne tekstlinks toe vanaf de stad-/regiopagina's (`vloerverwarming-zuidlaren.html`, `-assen.html`, `-groningen.html`, `-emmen.html`, `-hoogeveen.html`, `-drachten.html`, `-leeuwarden.html`) naar de Drenthe-hub-sectie op de homepage (of de duidelijkste Drenthe-landing), zodat het regionale signaal op één pagina bundelt. Anchor-tekst beschrijvend ("vloerverwarming in heel Drenthe"), geen keyword-spam, max. 1 link per pagina. Als een pagina al zo'n link heeft, laat staan.
**Succescriterium:** Elke genoemde stad-pagina bevat één relevante interne link naar de Drenthe-hub; links werken; geen dubbele/over-geoptimaliseerde anchors. (Effect: consolidatie + positiestijging bij juni-fetch.)

### Taak 3: Offerte-deeplink-CTA op `projecten.html` `[GOEDGEKEURD]`
**Bron:** Analytics Agent (conversiedata)
**Prioriteit:** Hoog
**Actie:** `projecten.html` heeft 60% bounce en slechts ~20 s gem. duur — bezoekers kijken en haken af zonder vervolgstap. De offerte-deeplink `/contact.html?modus=offerte` is de bewezen topconverter (in de sterke weken 9,1% bounce / 10 conv. op 11 sess). Voeg na (of binnen) de projectgalerij een duidelijke, nuchtere CTA-band toe die naar `/contact.html?modus=offerte` leidt — bv. "Zelf zo'n vloer? Vraag een vrijblijvende offerte aan." Eén intentie, één link. Sluit visueel aan bij de bestaande CTA-stijl (zie homepage CTA-band). Als er al een offerte-CTA op de pagina staat, maak die prominenter/dichter bij de galerij i.p.v. een tweede toe te voegen.
**Succescriterium:** `projecten.html` heeft een zichtbare CTA naar `/contact.html?modus=offerte` onder/in de galerij; link werkt; stijl consistent met de site. (Effect: bounce richting <50%, ≥1 offerte-klik vanaf projecten bij juni-fetch.)

---

## Uitgestelde voorstellen `[WACHT]`

- **Prijsindicatie mobile-ATF verder verbouwen** — entry-bounce 66,7% (9 sess) is omhoog t.o.v. 54,5%, maar dat is een minisample van ~14 uur post-deploy. De cyclus-15 ATF-fix staat live; pageview-engagement verbeterde juist. **Niet opnieuw verbouwen** vóór de juni-fetch een vol sample geeft. Het echte knelpunt is de koude entry/message-match van de bron (Ads/social), niet de pagina.
- **`vloerverwarming-assen.html` hero/LCP** — 90d nog rood (0,7 s, 0 scrollers), maar layout-fix is recent; wacht juni-fetch vóór ingrijpen.
- **Paid Search negatieven `--apply`** — 15 negatieven staan klaar (geen spend-effect), maar de Ads-scripts konden in deze omgeving niet draaien (live-account, geblokkeerd). Pas toe zodra een sessie met Ads-rechten beschikbaar is, ná de campagne-state-check (zie escalatie).

---

## Afgewezen voorstellen `[AFGEWEZEN]`

- **Standalone `vloerverwarming-drenthe.html` / `vloerverwarming-heerenveen.html`** — Heerenveen heeft 5 impressies (pos 50,4) en wordt al door de Drachten-pagina gedekt; Drenthe lossen we op met consolidatie (Taak 2), niet met een extra pagina. Kwaliteit > kwantiteit.
- **Organisch concurreren op brede kosten-termen** (`vloerverwarming kosten / per m²`) — SERP gedomineerd door aggregators; deze intentie hoort in de Ads-funnel naar `prijsindicatie.html`, niet als SEO-doel.
- **Budgetverhoging >€2/dag** — eerst Paid Search-volume + attributie herstellen (zie escalatie); geen spend-besluit zonder PO.

---

## Escalatie — Google Ads (P0, geen developer-werk)

De Ads-verificatiescripts (`google_ads_smoke_test.py`, `google_ads_list_campaigns.py`) konden in deze geautomatiseerde omgeving **niet draaien** (live-account-mutaties zijn geblokkeerd in don't-ask-mode). De data vraagt om een check zodra een sessie met Ads-rechten + `secrets/google-ads.env` beschikbaar is:

1. **Waarom is Paid Search-volume ingestort (11 → 1 sessie)?** Check campagne `23834672782`:
   ```bash
   python3 scripts/google_ads_smoke_test.py
   python3 scripts/google_ads_list_campaigns.py
   ```
   Verwachting: is de campagne nog ENABLED, of staat hij op PAUSED / budget uitgeput / policy-disapproval?
2. **GA4 ↔ Google Ads koppeling + auto-tagging** (GA4 Admin → Product Links) — P0 sinds cyclus 14. Zonder dit blijft de attributie lekken (Direct conv-rate 31%, geen `gclid`).
3. **Live RSA final URLs** = offerte-deeplink + prijsindicatie (match `google_ads_lead_campaign_defaults.json`).
4. **Negatieven** toepassen na state-check: `python3 scripts/google_ads_campaign_next_steps.py negatives --campaign-id 23834672782 --dry-run` → `--apply` (geen spend-effect).

---

## Social Media
**Status:** Weekplanning staat in `docs/website-manager/social/weekly_calendar.md` (7 posts: 3 LinkedIn, 4 Instagram).
**Rode draad:** social haalt de clicks die de SERP nu laat liggen — Zuid-Laren, Hoogeveen, Drenthe expliciet in de copy; offerte-deeplink en prijsindicatie als CTA's, geen `modus=informatie`.
**Actie vereist:** Handmatige publicatie door VLWarmte-team.

---

## Context voor volgende sprint
- **Juni-fetch (~22 juni) is het echte ijkpunt** voor cyclus 15 én 16: vol post-deploy sample voor prijsindicatie-entry, projecten-bounce, en de title/CTR-fixes.
- **Verse GSC-fetch** rond ~22 juni nodig om Taak 1 (CTR) en Taak 2 (Drenthe-consolidatie) te toetsen; GSC-fetch was deze cyclus geblokkeerd (data nog van 23-05).
- **Paid Search-collaps** is de scherpste open vraag — eerst campagne-state, dan attributie. Als de campagne gepauzeerd/uitgeput blijkt, verklaart dat de −44% conversies grotendeels.
- Werkwijze blijft de sterkste conversiepagina per sessie (4 conv. op 2 landings, 0% bounce) — de cyclus-15 mid-CTA daar in de gaten houden.

---

## Developer Rapport — 2026-06-08

**Geïmplementeerde taken:** Taak 1, Taak 2, Taak 3 (alle `[GOEDGEKEURD]`).
**Overgeslagen:** alle `[WACHT]` en `[AFGEWEZEN]` voorstellen + de Google Ads-escalatie (P0, geen developer-werk).
**Vooraf gecheckt:** geen NL/EN-varianten van de homepage — `index.html` is de enige homepage. Alleen NL-bestanden in de root.

### Taak 1 — Title + meta-description CTR-fix
- **`index.html`** (regel 9–11): alleen `<title>` en `<meta name="description">` herschreven. Lokale term + intentie vooraan, nuchtere USP toegevoegd.
  - title: `Vloerverwarming Zuidlaren & Noord-NL — installateur | VLWarmte` (`&` als `&amp;` geëscaped).
  - meta: ondervloer→oplevering, eigen ploeg, antwoord binnen één werkdag, 10 jaar garantie op de buis.
- **`vloerverwarming-hoogeveen.html`** (regel 10–11): title ongewijzigd (Hoogeveen stond al vooraan); alleen `<meta name="description">` aangescherpt met concrete USP (heel traject + eigen ploeg vanaf Zuidlaren + antwoord binnen één werkdag).
- **Bewust niet aangeraakt:** `og:title`/`og:description` en `twitter:*` — de taak schreef expliciet "alleen `<title>` en `<meta name="description">`". *Opmerking voor PM:* die social-tags lopen nu inhoudelijk iets uit de pas met de nieuwe title/meta; bewust conservatief gelaten. Als gewenst kan een vervolgtaak ze gelijktrekken.

### Taak 2 — Drenthe-signaal bundelen met interne links
- Drenthe-hub doel = bestaande sectie `index.html#drenthe-hub` (h2 "Vloerverwarming in heel Drenthe").
- Eén contextuele tekstlink toegevoegd in de bestaande "Ook actief in"-sectie van elke stad-pagina, anchor steeds `vloerverwarming in heel Drenthe`:
  - `vloerverwarming-zuidlaren.html`, `-assen.html`, `-groningen.html`, `-emmen.html`, `-hoogeveen.html`, `-drachten.html`, `-leeuwarden.html`.
- Precies **1 link per pagina** (geverifieerd via grep: 1× per bestand), beschrijvend, geen keyword-spam; per pagina licht gevarieerde zin om dubbel-boilerplate te vermijden. Geen pagina had al zo'n link.

### Taak 3 — Offerte-deeplink-CTA op `projecten.html`
- Pagina had al een offerte-CTA-band (los `<section>` ná de galerij, met witruimte ertussen). Conform de taak **geen tweede band toegevoegd**, maar de bestaande **prominenter en dichter bij de galerij** gezet:
  - De losse trailing `<section class="section">` verwijderd; de `.cta-band` nu direct ónder de project-cases binnen dezelfde galerij-sectie (`section-muted`) geplaatst — geen visuele gap meer.
  - Copy verscherpt naar één duidelijke intentie: kop "Zelf zo'n vloer?", primaire CTA `Vraag offerte aan` → `/contact.html?modus=offerte#aanvraag`; prijsindicatie blijft als secundaire knop.
  - Markup volgt exact het bewezen homepage-patroon (`.container` > `.cta-band` > `<div>` + `.cta-band-stack`), dus stijl is consistent.

### Smoke-resultaat
- HTML-structuur van alle gewijzigde regio's handmatig nagelopen (Read): tags gebalanceerd, geen kapotte nesting; gewijzigde `projecten.html` galerij-/CTA-blok sluit netjes (`.cta-band` → `</div>` container → `</section>` → `</main>`).
- Interne links: `id="drenthe-hub"` bestaat 1× in `index.html`; elke stad-pagina linkt er 1× naartoe (`index.html#drenthe-hub`). Offerte-deeplink op `projecten.html` is de standaard `contact.html?modus=offerte#aanvraag` (conform AGENTS.md deep-link-spec).
- **Beperking:** de geautomatiseerde validatie via `python3`/shell (tag-balancer-script, `git status`) was in deze sessie geblokkeerd (don't-ask-mode). De smoke check is daarom met de Read-tool gedaan i.p.v. een runner. Aanrader: PM draait lokaal nog even een linkcheck/validator vóór commit.

### Aandachtspunten voor volgende sprint
- Eventueel `og:`/`twitter:`-tags op `index.html` (en `vloerverwarming-hoogeveen.html`) gelijktrekken met de nieuwe title/meta.
- Effect van Taak 1 (CTR) en Taak 2 (Drenthe-consolidatie) pas toetsbaar bij de juni-fetch (~22 juni).
- Geen secrets aangeraakt; alleen `.html` + dit rapport gewijzigd.

### Deployment (Product Manager — stap 7b)
- **Commit:** `0fee542` — "Sprint cyclus 16 (9 jun): title/meta CTR-fix, Drenthe interne links, offerte-CTA projecten"
- **Push:** `main` → GitHub Pages, 08-06-2026.
- **GitHub Actions:** `pages-build-deployment` run `27115772288` — **completed/success** (39s). E2E production `27115772682` (Formspree-to-inbox) draaide nog door bij afronding cyclus — niet-blokkerend voor de site-deploy.
- **Live-verificatie (curl):** homepage-title = "Vloerverwarming Zuidlaren & Noord-NL — installateur | VLWarmte" ✓; Drenthe-link op stad-pagina's live ✓; offerte-CTA "Zelf zo'n vloer?" op `projecten.html` live ✓; Google Tag Manager geladen ✓ (measurement-ID via GTM-container, niet inline — conform vorige releases).
- **PM-smoke i.p.v. developer-runner:** de PM had wél Bash en heeft de diffs gereviewd (markup gebalanceerd, alleen bedoelde wijzigingen), `git status` gecontroleerd (geen secrets gestaged) en de live-site geverifieerd — de door de developer gevraagde validatie is daarmee gedaan.
