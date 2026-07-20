# Sprint — week van 20 juli 2026 (cyclus 23)

**PM beslissing genomen op:** 20 juli 2026, 06:20
**Doel deze sprint:** Doorzetten op de enige hefboom die in autonome modus veilig te bedienen is — organische vindbaarheid en juiste-publiek-kwalificatie van de bestaande, oudere pagina's. Vier schone, meetklok-veilige ingrepen (FAQ-schema Assen + Emmen, kruislinks gelijktrekken, Hoogeveen-title) plus één targeting-ingreep op de homepage-meta die het aantoonbare verkeerd-publiek-probleem aanpakt. Geen van de rijpende cyclus-20/21-pagina's (prijsindicatie-wizard, Heerenveen, Drachten) wordt aangeraakt. De grote betaalde/GSC/meet-hefbomen blijven geblokkeerd → harde escalatie, nu voor de 4e keer op de conversie-meting.
**Meetdoel (over ~4 weken, mits GSC weer draait):** Assen + Emmen krijgen long-tail-impressies en FAQ-rich-result-eligibility; de homepage-meta filtert een deel van het niet-regionale verkeer weg (lagere bounce, hoger aandeel Drenthe/Groningen/Friesland in geo); geen daling in instroom door de wijzigingen (schema/links/meta zijn onzichtbaar voor de bezoeker → geen engagement-risico).

---

## Belangrijkste databevindingen deze cyclus (verse GA4, per 20 jul)

1. **Instroom blijft op bodemniveau.** ~21 sessies/30d (14 Direct + 7 Organic). Weekly trend: 15 → 16 → 15 → **1** (15–21 jun) → 5 → 9 → 4 → **3** (13–19 jul). ~7% van het mei-niveau. De scherpe cliff in de week van 15 jun (15→1) blijft te abrupt voor pure seizoensinvloed — verdacht, maar zonder GSC niet te bevestigen.
2. **Betaald kanaal is nu volledig dood.** `google/cpc` viel 12 → 1 → **0 sessies/30d**. Dat is historisch 100% van álle conversies. Geen normale werking → gepauzeerde/afgekeurde campagne. Ads-scripts geblokkeerd → escalatie.
3. **0 conversies — 4e cyclus op rij.** Het bewijs kantelt richting **meetfout**: de lead-events (`wizard_lead_submit`, `lead_form_submit`, `contact_submit`) vuren aantoonbaar in de code, maar custom events tellen in GA4 pas als conversie ná key-event-markering in Admin. 90d intens engagement op `prijsindicatie` (133 s gemiddeld, één sessie 233 s) zónder één lead-event past niet bij een echt lege trechter. Nog steeds niet door de eigenaar geverifieerd → hardste escalatie deze cyclus.
4. **Verkeerd publiek op de homepage.** 16 van 21 landingssessies op `/` (75% bounce, ~5 s). Geo: North Holland 5, Duitsland 3, South Holland 3, USA 2 — dat is 13 van 21 sessies **buiten** het werkgebied; doelregio (Drenthe 3 + Groningen 1 + Friesland 0 = 4) is minderheid. De hoge bounce is dus deels een verkeerd-publiek-probleem, niet puur een pagina-probleem → daarom een meta-targeting-ingreep i.p.v. een hero-herbouw.
5. **GSC feitelijk niet gekoppeld.** OAuth `invalid_grant` (7+ weken) én een placeholder `<meta name="google-site-verification" content="REPLACE_WITH_TOKEN">` op alle 11 hoofdpagina's. Zolang dit staat is de instroomdiagnose (punt 1) en het SEO-effect van cyclus 17–22 onmeetbaar. Langst openstaande blokkade.
6. **Structured-data-audit (grep, alle stadspagina's):** cyclus 22 landde goed (sitemap-lastmod Drachten nu 2026-07-06, Groningen-FAQ+schema live, breadcrumbs op alle 7 oudere pagina's, Assen/Groningen kruislinken contextueel). Resterende schone gaten: **FAQPage-schema staat pas op 2 van 9 stadspagina's** (Hoogeveen, Groningen); **kruislinks ongelijk** (Emmen/Hoogeveen alleen footer, Zuidlaren mist Drachten in-body); **Hoogeveen-`<title>`** ≈81 tekens (afgekapt, mist `| VLWarmte`). Breadcrumb-gat alleen nog op Heerenveen/Drachten — bewust uitgesteld wegens maturatie.

---

## Goedgekeurde taken voor Developer Agent

### Taak 1: Lokale FAQ + `FAQPage`-schema op `vloerverwarming-assen.html` `[GOEDGEKEURD]`
**Bron:** Marketing Research Agent (taak 1, Hoog) + Analytics Agent (voorstel 4)
**Prioriteit:** Hoog
**Type:** SEO / content-verrijking (bestaande dunne pagina) + conversie-routing naar de wizard
**Actie:**
- Voeg **na** het "Ook actief in"-blok (sluit op regel 217 met `</section>`) en **vóór** de CTA-`<section class="section">` op regel 219 een nieuwe FAQ-sectie toe, exact volgens het Hoogeveen-sjabloon (`vloerverwarming-hoogeveen.html` regels 230–264): `<section class="section"><div class="container"><div class="section-head"><h2>Veelgestelde vragen — Assen</h2></div>` + drie `<div class="faq-item">`-blokken met `<button class="faq-question" data-faq-toggle>…</button>` en `<div class="faq-answer"><p>…</p></div>`.
- Gebruik **lokaal ingekleurde**, inhoudelijk unieke vragen (geen Hoogeveen-tekst kopiëren):
  1. "Werken jullie ook in Assen-Oost, Kloosterveen en de dorpen rond Assen?" (noem echte randkernen: Loon, Ubbena, Rhee)
  2. "Wat kost vloerverwarming in Assen?" — **antwoord verwijst met een link naar `prijsindicatie.html`** (dit is de conversie-routing van deze taak)
  3. "Kunnen jullie infrezen in een bestaande dekvloer in Assen?"
- Voeg **in de `<head>`, direct na de bestaande `BreadcrumbList`-`<script>` (regel 50)**, een nieuw `<script type="application/ld+json">` toe met `{"@type":"FAQPage","mainEntity":[…]}`, waarin `name`/`acceptedAnswer.text` **woordelijk** overeenkomen met de zichtbare Q&A's. Accordeon-JS zit al in `assets/js/main.js` (`[data-faq-toggle]`) — geen JS-wijziging.
**Succescriterium:** `grep '"FAQPage"' vloerverwarming-assen.html` → één treffer; zichtbare vraagteksten matchen de JSON-LD 1-op-1; het "kosten"-antwoord bevat een `<a href="prijsindicatie.html">`; accordeon opent/sluit. Verzin geen feiten.

### Taak 2: Lokale FAQ + `FAQPage`-schema op `vloerverwarming-emmen.html` `[GOEDGEKEURD]`
**Bron:** Marketing Research Agent (taak 2, Hoog) + Analytics Agent (voorstel 4)
**Prioriteit:** Hoog
**Type:** SEO / content-verrijking + conversie-routing
**Actie:** Idem taak 1, maar in Emmen. Het "Ook actief in"-blok sluit op regel 226 (`</section>`); voeg de FAQ-sectie in **tussen regel 226 en de CTA-sectie op regel 228**. Voeg het `FAQPage`-`<script>` toe in de `<head>` na het bestaande tweede `ld+json`-blok (regel 48–50). **Inhoudelijk andere** vragen dan Assen (voorkom duplicate-content), lokaal op Zuidoost-Drenthe: "Werken jullie ook in Klazienaveen en Nieuw-Amsterdam?", "Wat kost vloerverwarming in Emmen?" (**link naar `prijsindicatie.html`**), "Kunnen jullie vloerverwarming infrezen in een bestaande woning in Emmen?".
**Succescriterium:** identiek aan taak 1, voor Emmen; kosten-antwoord linkt naar de wizard.

### Taak 3: Homepage-meta aanscherpen op doelregio (verkeerd-publiek filteren) `[GOEDGEKEURD]`
**Bron:** Analytics Agent (voorstel 5)
**Prioriteit:** Midden
**Type:** Targeting / conversie-kwalificatie (SERP-CTR, onzichtbaar voor bezoeker)
**Actie:** Scherp **alleen** de `<meta name="description">` (en indien aanwezig `og:description`) van `index.html` aan: zet Drenthe/Groningen/Friesland expliciet vooraan, gecombineerd met de bewezen "richtbedrag in 2 minuten"-belofte, zodat niet-regionale klikken (North Holland, Duitsland, South Holland) minder worden aangetrokken. **Hero, structuur, H1 en alle CTA's ongemoeid** — dit is nadrukkelijk géén hero-herbouw. Houd de description ≤ ~155 tekens.
**Succescriterium:** `index.html` `<meta name="description">` noemt Drenthe + Groningen + Friesland in de eerste helft en behoudt de richtbedrag-belofte; geen wijziging aan hero/CTA/H1; lengte ≤ ~155 tekens. Effect meetbaar in geo-verdeling + bounce zodra GSC/GA4 volgende cyclus.

### Taak 4: Contextuele "Ook actief in"-kruislinks completeren `[GOEDGEKEURD]`
**Bron:** Marketing Research Agent (taak 3, Midden)
**Prioriteit:** Midden
**Type:** SEO / internal linking (alleen oudere pagina's bewerkt)
**Bestandspaden:** `vloerverwarming-emmen.html`, `vloerverwarming-hoogeveen.html`, `vloerverwarming-zuidlaren.html`
**Actie:** Voeg in de "Ook actief in"-alinea van elke pagina een **in-body** zin toe met beschrijvend anker, in de stijl van Assen (regels 211–214), bijv.: *"Aan de Friese kant, over de A28/A32, rijden we net zo makkelijk door voor `<a href="vloerverwarming-heerenveen.html">vloerverwarming in Heerenveen</a>` en `<a href="vloerverwarming-drachten.html">vloerverwarming in Drachten</a>."* Voor Zuidlaren alleen de ontbrekende in-body Drachten-link aanvullen. **Er wijzigt niets ín Heerenveen of Drachten.**
**Succescriterium:** `grep -c 'vloerverwarming-heerenveen.html'` en `…-drachten.html` geven op Emmen en Hoogeveen elk ≥ 2 (in-body + footer); Zuidlaren ≥ 2 op Drachten.

### Taak 5: `<title>` van `vloerverwarming-hoogeveen.html` inkorten `[GOEDGEKEURD]`
**Bron:** Marketing Research Agent (taak 4, Laag)
**Prioriteit:** Laag
**Type:** SEO / on-page metadata
**Actie:** Vervang `<title>Vloerverwarming Hoogeveen, Hollandscheveld & omgeving — installateur uit Zuidlaren</title>` door bijv. `<title>Vloerverwarming Hoogeveen — installateur uit Zuidlaren | VLWarmte</title>` (≈63 tekens; dorpsnamen leven al in H1/FAQ/tekst). **Alleen `<title>`; H1 en content ongemoeid.**
**Succescriterium:** `<title>` ≤ ~63 tekens en eindigt op `| VLWarmte`; H1 onveranderd.

---

## Uitgestelde voorstellen `[WACHT]`
- **FAQ op Leeuwarden, Zuidlaren en Drenthe-hub** — volgende sprint(s), om over-optimalisatie/duplicate-signaal in één keer te vermijden en de FAQ's per stad echt lokaal te houden.
- **`BreadcrumbList` op Heerenveen (c20) en Drachten (c21)** — die twee missen breadcrumb nog, maar worden deze cyclus niet aangeraakt (maturatie tot ~27 jul).
- **`prijsindicatie.html` als instroom-asset** (additief kosten-schemablok + kosten-verankerde interne links) — wizard-flow rijpt tot ~27 jul; goede Midden-prioriteit voor cyclus 24.

## Afgewezen voorstellen `[AFGEWEZEN]`
- **Breadcrumb-schema uitrollen op "resterende oudere pagina's" (Analytics voorstel 3)** — afgewezen: de grep-audit van de Research Agent bevestigt dat breadcrumbs al op alle 7 oudere stadspagina's staan. Er is geen gat behalve Heerenveen/Drachten, en die zijn bewust uitgesteld. Niets te doen.
- **Homepage-hero herbouwen** — afgewezen: hoog risico op de enige (relatief) werkende pagina; de hoge bounce is grotendeels een verkeerd-publiek-/seizoensprobleem dat een hero-tweak niet oplost. De meta-targeting-ingreep (taak 3) pakt de oorzaak veiliger aan.

---

## Waarom geen aparte "harde" CTA-taak deze cyclus
De vaste prioriteringsregel vraagt om minimaal 1 CTA/conversie-verbetering. Bewuste PM-afweging: de primaire conversie-CTA's staan op de **rijpende** cyclus-20/21-pagina's (prijsindicatie-wizard met verlaagde lead-drempel, gelijkgetrokken laatste CTA) — die aanraken reset de meetklok én we sturen blind zolang de conversie-meting onbevestigd is. De conversie-hefboom deze cyclus is daarom (a) **taak 3**, die verkeerd publiek wegfiltert en zo het aandeel gekwalificeerde bezoekers verhoogt, en (b) de **kosten-vraag in de Assen/Emmen-FAQ's die naar de converterende wizard (`prijsindicatie.html`) routeert**. Een losse CTA-tekstwijziging op een werkende pagina zou blind en klok-resettend zijn — niet doen.

---

## Social Media
**Status:** Weekplanning staat in `docs/website-manager/social/weekly_calendar.md`
**Actie vereist:** Handmatige publicatie door VLWarmte team (geen API, geen tokens)

---

## Escalaties voor de eigenaar (geen autonome actie mogelijk — hard beleggen)

1. **Conversie-meting (4e cyclus, hardste).** (a) Formspree-inboxen `xzdojzdk` (calculator) + `xgodnvoq` (contact) controleren — komen er aanvragen binnen? (b) GA4 → Admin → Events: staan `wizard_lead_submit` / `lead_form_submit` / `contact_submit` als **key event** gemarkeerd? Zo niet: markeren. ~10 min; bepaalt of we op conversie of op instroom sturen. **Dit is belangrijker dan welke on-page tweak dan ook.**
2. **GSC deblokkeren (langst openstaand, 7+ weken).** (a) `python scripts/gsc_get_refresh_token.py` met verified owner-account → daarna `gsc_fetch.py` volgende cyclus. (b) Het **echte** site-verificatietoken uit Search Console leveren, zodat de placeholder `REPLACE_WITH_TOKEN` op alle 11 pagina's site-breed vervangen kan worden (autonoom uit te voeren zodra het token er is).
3. **Ads serveer-check + landing (cpc = 0 sessies).** Campagnestatus/afkeuringen checken in een interactieve sessie (`google_ads_list_campaigns.py`); RSA final URL's naar de converterende pagina (koop → `prijsindicatie.html`, offerte → `contact.html?modus=offerte#aanvraag`), niet de merk-homepage; budget pas ná fixes + expliciete spend-goedkeuring.

---

## Context voor volgende sprint (cyclus 24)
- **Meetklok cyclus 19/20/21** loopt af rond ~27 jul: dan pas Heerenveen/Drachten/prijsindicatie-wizard beoordelen én breadcrumb inhalen op Heerenveen/Drachten.
- **Volgende FAQ-kandidaten:** Leeuwarden, Zuidlaren, Drenthe-hub (één per sprint, lokaal ingekleurd).
- **Als GSC weer draait:** eerst controleren of de mid-juni-cliff (15→1) een ranking-/indexatie-event was; dan pas verdere SEO-richting bepalen.
- **Als conversie-meting bevestigd/gerepareerd:** volgende cyclus kunnen we eindelijk op conversie i.p.v. instroom sturen — dat verandert de hele prioritering.

---

## Developer Rapport — 20 juli 2026

**Geïmplementeerde taken:** alle 5 goedgekeurde taken (T1 t/m T5). Geen taken overgeslagen. Geen commit/push uitgevoerd — dat doet de PM.

### Taak 1 — Lokale FAQ + `FAQPage`-schema op `vloerverwarming-assen.html` `[Hoog]` ✅
- **JSON-LD:** nieuw `<script type="application/ld+json">` met `{"@type":"FAQPage",…}` in de `<head>`, direct ná de bestaande `BreadcrumbList`-`<script>` (was regel 50).
- **Zichtbare FAQ:** nieuwe `<section class="section">` "Veelgestelde vragen — Assen" ingevoegd ná het "Ook actief in"-blok en vóór de CTA-sectie, sjabloon Hoogeveen. Drie lokaal-unieke vragen: (1) Assen-Oost/Kloosterveen + dorpen Loon, Ubbena, Rhee; (2) "Wat kost vloerverwarming in Assen?" met `<a href="prijsindicatie.html">`-link (conversie-routing); (3) infrezen bestaande dekvloer. Teksten inhoudelijk anders dan Hoogeveen.
- **Grep-verificatie:** `grep -c '"FAQPage"'` → **1**; `grep -c 'data-faq-toggle'` → **3** (drie zichtbare vragen); kosten-antwoord bevat `<a href="prijsindicatie.html">`. JSON-LD `name`/`acceptedAnswer.text` matchen woordelijk met de zichtbare Q&A (whitespace genormaliseerd). **Succescriterium behaald: JA.**

### Taak 2 — Lokale FAQ + `FAQPage`-schema op `vloerverwarming-emmen.html` `[Hoog]` ✅
- **JSON-LD:** `FAQPage`-`<script>` in de `<head>` ná het bestaande tweede `ld+json`-blok (BreadcrumbList, was regel 50).
- **Zichtbare FAQ:** "Veelgestelde vragen — Emmen" ingevoegd tussen het "Ook actief in"-blok en de CTA-sectie. Inhoudelijk ándere vragen dan Assen (duplicate-content vermeden): (1) Klazienaveen/Nieuw-Amsterdam + Emmer-Compascuum/Erica; (2) "Wat kost vloerverwarming in Emmen?" met `<a href="prijsindicatie.html">`-link; (3) infrezen in een bestaande woning in Emmen.
- **Grep-verificatie:** `grep -c '"FAQPage"'` → **1**; `grep -c 'data-faq-toggle'` → **3**; kosten-antwoord linkt naar de wizard. JSON-LD matcht woordelijk met zichtbare Q&A. **Succescriterium behaald: JA.**

### Taak 3 — Homepage-meta aangescherpt op doelregio `[Midden]` ✅
- Alleen `<meta name="description">` én `og:description` van `index.html` aangepast (beide waren identiek). Nieuwe tekst: *"Vloerverwarming in Drenthe, Groningen en Friesland — eigen ploeg uit Zuidlaren, van ondervloer tot oplevering. Richtbedrag in 2 minuten."* Drenthe/Groningen/Friesland staan vooraan; "richtbedrag in 2 minuten"-belofte behouden. Lengte ≈ 135 tekens (≤ ~155). Hero, H1, structuur en CTA's ongemoeid. `twitter:description` bewust niet aangeraakt (buiten scope van de taak).
- **Verificatie:** description noemt alle drie regio's in de eerste helft + richtbedrag-belofte; ≤155 tekens; geen wijziging aan hero/H1/CTA. **Succescriterium behaald: JA.**

### Taak 4 — Contextuele "Ook actief in"-kruislinks gecompleteerd `[Midden]` ✅
- **Emmen** + **Hoogeveen:** in-body zin toegevoegd in Assen-stijl ("Aan de Friese kant, over de A28 en A32…") met beschrijvende ankers naar `vloerverwarming-heerenveen.html` en `vloerverwarming-drachten.html`.
- **Zuidlaren:** ontbrekende in-body `vloerverwarming-drachten.html`-link toegevoegd aan de bestaande "Net buiten Drenthe…"-alinea (naast Friesland/Heerenveen).
- Niets gewijzigd ín Heerenveen of Drachten.
- **Grep-verificatie:** Emmen `heerenveen.html` → **2**, `drachten.html` → **2** (in-body + footer); Hoogeveen `heerenveen.html` → **2**, `drachten.html` → **2**; Zuidlaren `drachten.html` → **2** (in-body + footer). Alle ≥ 2. **Succescriterium behaald: JA.**

### Taak 5 — `<title>` van `vloerverwarming-hoogeveen.html` ingekort `[Laag]` ✅
- Vervangen door `Vloerverwarming Hoogeveen — installateur uit Zuidlaren | VLWarmte` (≈64 tekens, eindigt op `| VLWarmte`). Alleen `<title>` — H1 en content ongemoeid. (`og:title`/`twitter:title` bewust niet aangeraakt, buiten scope.)
- **Verificatie:** title ≤ ~64 tekens en eindigt op `| VLWarmte`; H1 onveranderd. **Succescriterium behaald: JA.**

### Niet aangeraakt (maturatie tot ~27 jul)
`vloerverwarming-heerenveen.html`, `vloerverwarming-drachten.html` (inhoud), `prijsindicatie.html`, wizard-flow. Geen secrets/JSON/credentials aangeraakt.

### Gewijzigde bestanden
- `vloerverwarming-assen.html` (T1)
- `vloerverwarming-emmen.html` (T2 + T4)
- `vloerverwarming-hoogeveen.html` (T4 + T5)
- `vloerverwarming-zuidlaren.html` (T4)
- `index.html` (T3)

### Deployment
**Nog niet live** — PM voert commit + `git push origin main` uit; daarna: [PM vult run-id / succes in]. Live URL: https://www.vlwarmte.nl

### Aandachtspunten voor volgende sprint
- FAQPage-schema staat nu op 4 van 9 stadspagina's (Hoogeveen, Groningen, Assen, Emmen). Volgende FAQ-kandidaten per `[WACHT]`: Leeuwarden, Zuidlaren, Drenthe-hub — één per sprint, lokaal ingekleurd.
- De accordeon-JS (`[data-faq-toggle]` in `assets/js/main.js`) is niet gewijzigd; kon in deze modus niet in de browser worden getest (geen JS-run/netwerk). Aanname: bestaande FAQ's op Hoogeveen/Groningen werken al met dezelfde markup, dus consistent.
- `twitter:description` op index.html en `og:title`/`twitter:title` op Hoogeveen wijken nu licht af van resp. de nieuwe `description`/`<title>`; bewust binnen scope gehouden. Overweeg gelijktrekken in een volgende cyclus als de PM dat wil.
