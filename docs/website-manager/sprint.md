# Sprint — week van 17 augustus 2026 (cyclus 25)

**PM beslissing genomen op:** 17 augustus 2026, 06:30
**Doel deze sprint:** repareren wat kapot of ongebruikt is, in plaats van nieuwe dingen bouwen. Vier van de vijf taken raken iets dat er al ligt: een component die op 15 pagina's niet is aangezet, een schema met een gat erin, tien titels die Google afkapt, en een regressie uit onze eigen vorige cyclus. Geen nieuwe pagina's.
**Meetdoel (over ~4 weken, mits GA4-meting hersteld is):** `prijsindicatie.html` wordt zichtbaar op "wat kost vloerverwarming per m2"-achtige zoekopdrachten en verliest de 100% landing-bounce; mobiele bezoekers op de dieptepagina's krijgen een bereikbare CTA zonder te scrollen; geen daling in instroom door de metadata-wijzigingen.

---

## Belangrijkste databevindingen deze cyclus

**Waarschuwing vooraf: er is deze cyclus géén verse GA4-data.** `python3 scripts/ga4_fetch.py` faalt — systeem-python3 is geüpgraded naar 3.13.7 en mist de `google`-modules; de venv-interpreter is in deze onbewaakte modus geblokkeerd. Alle cijfers hieronder komen uit de snapshot van **5 augustus** (12 dagen oud). Het effect van de deploy van cyclus 24 is dus **nul dagen gemeten**. Dat is een nieuwe escalatie.

1. **Cyclus 24 staat volledig live — 5 van 5 taken geverifieerd in de code.** FAQ + `FAQPage` op Leeuwarden en Heerenveen, breadcrumbs op Heerenveen en Drachten, kosten-blok boven de wizard, homepage kosten-band. Allemaal met bestandsbewijs.
2. **0 conversies is nu hard vastgesteld als een meetfout, geen websitefout.** Code-audit: `wizard_start` (prijsindicatie r. 1145), `wizard_lead_submit` (r. 1698), `lead_form_submit` (r. 1704) en `contact_submit` (`main.js` r. 208) vuren correct op alle 18 pagina's. Er is geen technische reden voor zes cycli op nul. Dit is één vinkje in GA4 → Admin → Events. Hoogste urgentie van alles in dit document.
3. **De sticky mobiele CTA staat op 1 van de 22 pagina's.** CSS (`critical-index.css` r. 584–630) én JS (`initStickyCta()`) laden op élke pagina; alleen de markup ontbreekt op 15 pagina's die er wél klaar voor zijn. Een component die al betaald en gebouwd is, staat uit.
4. **Bijna niemand scrolt.** Homepage 16 scroll-events op 185 sessies (8,6%); `werkwijze` 10%; `systemen-producten` 11%. Alles onder de vouw is praktisch onzichtbaar — inclusief de FAQ's die we vorige cyclus rond regel 225 hebben neergezet. Die hebben SEO-waarde, geen CRO-waarde.
5. **`prijsindicatie.html` is de nummer 2 van de site en heeft nul structured data.** 45 sessies en 135 s per 90 dagen, de enige pagina met instroomgroei (2 → 4), met harde kostencontent (€45–€95/m²) — en `grep -c 'application/ld+json'` geeft **0**. De `<title>` bevat het woord "kosten" niet.
6. **Tien titels worden door Google afgekapt.** Alle negen stadspagina's plus de homepage zitten op 61–66 tekens; wat wegvalt is precies het `| VLWarmte`-achtervoegsel.
7. **Echte bug in `faq.html`:** 15 zichtbare vragen, 14 in het `FAQPage`-schema. De ontbrekende is "Wat is droge vloerverwarming of laagopbouw?" — juist de term met de laagste concurrentie in dit vak.
8. **Grammaticafout in gestructureerde data:** `index.html` heeft tweemaal "Welke garantie **horen** bij jullie systemen?" — ook in de JSON-LD, dus het kan letterlijk in een zoekresultaat verschijnen.
9. **Ankertekst-mismatch op de homepage:** `index.html` r. 168 zet de ankertekst "vloerverwarming Friesland" op een link naar de Leeuwarden-stadspagina.
10. **Doelregio blijft mager:** 1 sessie in Drenthe/Groningen/Friesland in het 30d-venster; Friesland 0. Organisch 4 sessies. GSC is 10+ weken blind, Ads-account staat `CLOSED`.

---

## Goedgekeurde taken voor Developer Agent

### Taak 1: `prijsindicatie.html` — kosten-metadata, structured data en mobiele ATF terugwinnen `[GOEDGEKEURD]`

**Bron:** Marketing Research Agent (taak 1) + Analytics Agent (voorstellen 2 en 3)
**Prioriteit:** Hoog
**Type:** SEO / structured data + CRO
**Bestand:** `prijsindicatie.html`

**Actie:**

a) Vervang `<title>`, `og:title` en `twitter:title` (nu 76 tekens) door exact:
`Wat kost vloerverwarming per m²? Prijsindicatie Drenthe`

b) Voeg in de `<head>` een `BreadcrumbList`-JSON-LD toe volgens het patroon van `vloerverwarming-groningen.html` r. 52 (Home → Prijsindicatie vloerverwarming).

c) Voeg **onderaan de bestaande sectie `#kosten-uitleg`**, vóór de `<p class="small">`-disclaimer, een zichtbare FAQ-accordeon toe volgens het Assen-sjabloon (`vloerverwarming-assen.html` r. 227–234: `<div class="faq-item"><button class="faq-question" data-faq-toggle>…</button><div class="faq-answer"><p>…</p></div></div>`), met de drie Q&A's die **woordelijk uitgeschreven in `research_report.md` regels 259–274 staan** ("Wat kost vloerverwarming per m²?", "Waarom is de prijs per m² lager bij een grotere vloer?", "Betaal ik voorrijkosten in Drenthe, Groningen of Friesland?"). Spiegel die daarna **woordelijk** in een `FAQPage`-JSON-LD in de `<head>`. Schrijf geen eigen varianten — de teksten zijn al goedgekeurd.

d) Pas het ATF-introblok (r. ~585–595, uit cyclus 24) aan: voeg een tekstlink naar `#kosten-uitleg` toe en **vervang de link naar `vloerverwarming-heerenveen.html` door `vloerverwarming-assen.html`** (Heerenveen haalt nul verkeer, Assen is een echte doelstad). Gebruik de kant-en-klare zin uit `research_report.md` r. 279–282.

e) **Regressie uit cyclus 24 herstellen:** geef datzelfde introblok een eigen klasse `kosten-intro` en breid de bestaande mobiele mediaquery (r. ~400–460, de regel met commentaar "wizard productkeuze zichtbaar zonder scroll (≤768px)") uit zodat het blok op ≤768px compact wordt — kleinere `font-size`, strakkere `margin`/`padding`, en de niet-essentiële tweede zin `display:none`. Desktop blijft ongewijzigd. Het blok van vorige cyclus duwt de eerste wizard-stap nu onder de vouw op mobiel; dat werkt tegen een expliciet ontworpen ATF-regel in.

**Succescriterium:**
`grep -c '"FAQPage"' prijsindicatie.html` → 1 · `grep -c '"BreadcrumbList"' prijsindicatie.html` → 1 · `grep -c 'Wat kost vloerverwarming per m²' prijsindicatie.html` → ≥ 3 · `grep -c 'href="#kosten-uitleg"' prijsindicatie.html` → ≥ 1 · `grep -c 'vloerverwarming-heerenveen.html' prijsindicatie.html` → 0 · `grep -c 'kosten-intro' prijsindicatie.html` → ≥ 2 (blok + mediaquery) · elke `"name"` in de `FAQPage` komt woordelijk voor als zichtbare tekst · wizard-flow ongewijzigd.

---

### Taak 2: Sticky mobiele CTA uitrollen naar de 15 pagina's die er al klaar voor zijn `[GOEDGEKEURD]`

**Bron:** Analytics Agent (voorstel 1)
**Prioriteit:** Hoog
**Type:** CRO / conversie
**Bestanden:** `diensten.html`, `werkwijze.html`, `systemen-producten.html`, `projecten.html`, `over-ons.html`, `faq.html`, `vloerverwarming-assen.html`, `-drachten`, `-drenthe`, `-emmen`, `-groningen`, `-heerenveen`, `-hoogeveen`, `-leeuwarden`, `-zuidlaren`

**Actie:**

- Kopieer het `<a class="sticky-cta-mobile" href="prijsindicatie.html" data-sticky-cta …>`-blok uit `index.html` (r. 303–306) **woordelijk** naar alle 15 bovengenoemde bestanden, op dezelfde positie in de documentstructuur als in `index.html`.
- **Niet** toevoegen aan `prijsindicatie.html` en `contact.html` — dat zijn de bestemmingen, en ze missen de `.cta-band` die `initStickyCta()` nodig heeft om de knop weer te verbergen. Zonder die band blijft er een permanent zwevende knop staan.
- Voeg geen CSS en geen JS toe. Beide bestaan al en laden op elke pagina (`critical-index.css` r. 584–630, `main.js` `initStickyCta()` r. 10–23). Controleer dit vóór je begint met één `grep`.
- Controleer per bestand dat `.cta-band` daadwerkelijk aanwezig is. Ontbreekt die op een pagina: sla die pagina over en meld het in je rapport.

**Waarom (voor je eigen afweging bij twijfel):** mobiel is 25% van de sessies en de scroll-ratio's liggen tussen 8% en 11% — de CTA's onderaan de pagina worden zelden bereikt. Dit is de goedkoopste conversie-ingreep die er in deze repo ligt: de component is compleet, alleen de markup ontbreekt.

**Succescriterium:**
`grep -l 'data-sticky-cta' *.html | wc -l` → **16** (was 1) · `grep -c 'data-sticky-cta' prijsindicatie.html` → 0 · `grep -c 'data-sticky-cta' contact.html` → 0 · geen wijzigingen in `assets/css/` of `assets/js/`.

---

### Taak 3: `faq.html`-schemagat dichten + twee fouten op `index.html` `[GOEDGEKEURD]`

**Bron:** Marketing Research Agent (taak 4) + Analytics Agent (observatie 6)
**Prioriteit:** Hoog
**Type:** Structured data + kwaliteit
**Bestanden:** `faq.html`, `index.html`

**Actie:**

a) In `faq.html` staat de zichtbare vraag **"Wat is droge vloerverwarming of laagopbouw?"** (derde accordeon) wél op de pagina maar **niet** in de `FAQPage`-JSON-LD. Voeg hem toe op positie 3 in `mainEntity`, met `name` en `acceptedAnswer.text` **woordelijk gelijk** aan de zichtbare tekst in het bijbehorende `<div class="faq-answer">`.

b) In `index.html` staat tweemaal "Welke garantie **horen** bij jullie systemen?" — één keer in de zichtbare `<button class="faq-question">` en één keer in de JSON-LD. Wijzig **beide** naar: `Welke garantie hoort bij jullie systemen?`

c) In `index.html` r. ~168 staat de ankertekst "vloerverwarming Friesland" op een link naar `vloerverwarming-leeuwarden.html`. Er is geen Friesland-hub en die bouwen we deze sprint niet. Maak daarom de ankertekst kloppend met de bestemming: gebruik **"vloerverwarming Leeuwarden"** (of een formulering waarin de bestemming Leeuwarden is). Verander de `href` niet.

**Succescriterium:**
`grep -c '"name":"Wat is droge vloerverwarming of laagopbouw?"' faq.html` → 1 · aantal `"@type":"Question"` in `faq.html` is 15 en gelijk aan het aantal `class="faq-question"`-knoppen · `grep -c 'Welke garantie horen' index.html` → 0 · `grep -c 'Welke garantie hoort' index.html` → 2 · geen link in `index.html` heeft nog de ankertekst "vloerverwarming Friesland".

---

### Taak 4: Alle `<title>`-tags onder 60 tekens brengen `[GOEDGEKEURD]`

**Bron:** Marketing Research Agent (taak 2)
**Prioriteit:** Hoog
**Type:** Metadata / SEO
**Bestanden:** de negen `vloerverwarming-*.html` + `index.html`

**Actie:** vervang per bestand `<title>`, `og:title` én `twitter:title` (die zijn nu alle drie identiek — houd ze identiek) door de tabel uit `research_report.md` r. 306–317. Voor de duidelijkheid hier herhaald:

| Bestand | Nieuwe title |
|---|---|
| `vloerverwarming-assen.html` | `Vloerverwarming Assen — installateur uit Zuidlaren` |
| `vloerverwarming-drachten.html` | `Vloerverwarming Drachten — installateur uit Zuidlaren` |
| `vloerverwarming-drenthe.html` | `Vloerverwarming Drenthe — eigen ploeg uit Zuidlaren` |
| `vloerverwarming-emmen.html` | `Vloerverwarming Emmen — installateur uit Zuidlaren` |
| `vloerverwarming-groningen.html` | `Vloerverwarming Groningen — installateur uit Zuidlaren` |
| `vloerverwarming-heerenveen.html` | `Vloerverwarming Heerenveen — vakman uit Zuidlaren` |
| `vloerverwarming-hoogeveen.html` | `Vloerverwarming Hoogeveen — vakman uit Zuidlaren` |
| `vloerverwarming-leeuwarden.html` | `Vloerverwarming Leeuwarden — vakman uit Zuidlaren` |
| `vloerverwarming-zuidlaren.html` | `Vloerverwarming Zuidlaren — installateur in het dorp` |
| `index.html` | `Vloerverwarming Drenthe, Groningen en Friesland \| VLWarmte` |

Raak `prijsindicatie.html` hier niet aan — die krijgt zijn eigen title in taak 1.

**Succescriterium:**
geen `<title>` in deze tien bestanden is langer dan 60 tekens · `grep -c 'installateur uit Zuidlaren | VLWarmte' *.html` → 0 · per bestand zijn `<title>`, `og:title` en `twitter:title` onderling gelijk.

---

### Taak 5: `vloerverwarming-zuidlaren.html` — FAQ, buurdorpen en twee tekstfouten `[GOEDGEKEURD]`

**Bron:** Marketing Research Agent (taak 5)
**Prioriteit:** Midden
**Type:** SEO / content
**Bestand:** `vloerverwarming-zuidlaren.html`

**Actie:**

a) Herstel twee tekstfouten: `particuliere kopwoningen` → `particuliere koopwoningen`, en `leggen de buis in en stomen of egaliseren we dicht` → `leggen de buis in en storten of egaliseren we dicht`.

b) Vervang in de `<p class="lead">` in de hero de opsomming `Tynaarlo, Paterswolde, Bunne, Zuidwolde en Gieten` door: `Haren, Glimmen, Eelde-Paterswolde, Vries, Tynaarlo, Yde en De Punt`. (Zuidwolde eruit — dat ligt niet naast Zuidlaren.)

c) Voeg **na** het "Ook actief in"-blok en **vóór** de CTA-sectie een FAQ-sectie toe volgens het Assen-sjabloon (`vloerverwarming-assen.html` r. 222–234), met de drie Q&A's die **woordelijk uitgeschreven staan in `research_report.md` r. 416–429** (Haren/Eelde/Glimmen/Vries-vraag, kostenvraag met link naar `prijsindicatie.html`, infrezen-in-jaren-zestig-vraag). Spiegel ze **woordelijk** in een `FAQPage`-JSON-LD in de `<head>`, na het bestaande `BreadcrumbList`-script.

**Waarom:** dit is de thuisbasis-pagina en tegelijk de dunste van de negen (16 kB, geen FAQ). De corridor Haren–Glimmen–Eelde–Vries ligt op een kwartier rijden, is de meest koopkrachtige strook van het werkgebied en komt nu nergens op de site voor. Dit dekt die plaatsnamen zonder een tiende stadspagina te bouwen.

**Succescriterium:**
`grep -c '"FAQPage"' vloerverwarming-zuidlaren.html` → 1 · `grep -c 'Haren' vloerverwarming-zuidlaren.html` → ≥ 2 · `grep -c 'kopwoningen' vloerverwarming-zuidlaren.html` → 0 · `grep -c 'stomen of egaliseren' vloerverwarming-zuidlaren.html` → 0 · zichtbare vraagteksten matchen de JSON-LD 1-op-1.

---

## Bij élke taak, als afsluiting (geen aparte taak)

Werk in `sitemap.xml` de `<lastmod>` bij van **elke pagina die je deze sprint hebt aangeraakt**, naar de implementatiedatum (2026-08-17). Niet de hele sitemap herdateren — alleen de bestanden die daadwerkelijk gewijzigd zijn. Reden: tien URL's lopen 1–6 weken achter op de echte wijziging, en dat is een signaal waarmee Google minder vaak komt crawlen.

---

## Uitgestelde voorstellen `[WACHT]`

- **Meta-descriptions onder 160 tekens brengen** (7 pagina's, Research taak 3) — reëel, maar deze sprint zitten er al twee metadata-taken in. Volgende cyclus, dan zijn de titels ook gemeten.
- **Sectie "Vloerverwarming en een warmtepomp" op `prijsindicatie.html`** (Research taak 6) — de grootste onbediende zoekintentie, maar `prijsindicatie.html` wordt deze sprint al op vier punten aangepakt. Twee grote ingrepen in één bestand in één onbewaakte run is vragen om problemen. Staat vooraan voor cyclus 26.
- **`BreadcrumbList` op de vijf schemaloze kernpagina's** (`contact`, `diensten`, `werkwijze`, `projecten`, `over-ons` — Analytics voorstel 4) — goedkoop en risicoloos, maar de zesde plek was op.
- **FAQ + `FAQPage` op `vloerverwarming-drachten.html`** (Analytics voorstel 6) — Drachten heeft de beste engagement van de Friese pagina's (107 s, 50% scroll). Blijft de logische volgende stap in de FAQ-cadans, na Zuidlaren.
- **Unieke `alt`-teksten op zeven stadspagina's** (Research taak 7b) — hygiëne, geen hefboom.

## Afgewezen voorstellen `[AFGEWEZEN]`

- **Friesland-hub bouwen + 3-niveau-breadcrumbs** (Analytics voorstel 5) — afgewezen als nieuwe pagina. Zeven van de negen stadspagina's halen nul verkeer; een tiende erbij lost niets op en kost onderhoud. De ankertekst-mismatch die eronder zat, lossen we wél op (taak 3c). Herzien zodra Friesland überhaupt verkeer trekt.
- **Homepage-hero aanpassen** — derde cyclus op rij afgewezen. 85% bounce op 12 sessies is geen betrouwbaar signaal, en dit is de enige pagina met substantieel verkeer. Niet aanraken zonder verse data.
- **De negen wizard-`<h2>`'s omzetten naar niet-koppen** — technisch een verbetering voor het onderwerpsignaal, maar het raakt de wizard-JS en de toegankelijkheid. Niet doen in een onbewaakte run.
- **`REPLACE_WITH_TOKEN` invullen** — wacht op een echt token van de eigenaar.

---

## Escalaties — eigenaar-actie, geen developer-werk

1. **Key events markeren in GA4 — hoogste urgentie, zesde cyclus op nul.** Deze cyclus is met code-audit hard vastgesteld dat `wizard_start`, `wizard_lead_submit`, `lead_form_submit` en `contact_submit` correct vuren op alle 18 pagina's. Er is dus géén technische reden voor 0 conversies; het is één vinkje in **GA4 → Admin → Events → markeer als key event**. Controleer tegelijk de Formspree-inboxen `xzdojzdk` (wizard) en `xgodnvoq` (contact) op echte inzendingen. Zolang dit staat, is elke uitspraak over conversie giswerk.
2. **NIEUW: GA4-fetch is stuk.** Systeem-`python3` is 3.13.7 geworden en mist de `google`-modules; `scripts/ga4_fetch.py` faalt met `ModuleNotFoundError: No module named 'google'`. Herstel met: `.venv/bin/pip install -r scripts/requirements-ga4.txt` (of de venv opnieuw opbouwen). Zonder dit draait de volgende analytics-cyclus opnieuw blind — deze cyclus is al blind gedraaid op 12 dagen oude cijfers.
3. **GSC OAuth vernieuwen — 10+ weken `invalid_grant`.** Draai `python scripts/gsc_get_refresh_token.py` met het geverifieerde owner-account. Zolang dit staat weten we niet welke zoektermen impressies opleveren, en is al het SEO-werk in deze sprint blind gestuurd. `REPLACE_WITH_TOKEN` staat nog op 19 live pagina's.
4. **Google Ads-account heropenen.** Status `CLOSED`, geen betaalmethode. Dat verklaart de nul impressies volledig — de landingspagina's zijn niet de oorzaak. ads.google.com → Billing, en zet auto-tagging aan.
5. **Beeldmateriaal.** Sinds mei 2026 is er geen nieuw fotomateriaal aangeleverd. `vloerverwarming-zuidlaren.html` heeft geen enkele projectfoto, `projecten.html` toont twee projecten, en de social-kalender recyclet voor de derde week dezelfde beelden. Eén middag fotograferen op een afgerond project (eindresultaat-vloer, verdelerkast, ploeg aan het werk) levert maanden content op.

---

## Social Media

**Status:** Weekplanning staat in `docs/website-manager/social/weekly_calendar.md` (week van 17 augustus, 3 LinkedIn + 4 Instagram).
**Actie vereist:** handmatige publicatie door het VLWarmte-team.
**Thema:** Friese pagina's (Leeuwarden/Heerenveen, live sinds 5 aug), de prijs-wizard, en de seizoenshaak — dekvloer droogt ~6 weken, dus half augustus is het laatste eerlijke moment om "vóór de winter klaar" te beloven.

---

## Context voor volgende sprint (cyclus 26)

- **Meet eerst of de fetch weer draait.** Als escalatie 2 niet is opgelost, draait cyclus 26 opnieuw blind. Draai `python3 scripts/ga4_fetch.py` vroeg in de cyclus en meld het meteen als het faalt.
- **Meetklok:** `prijsindicatie.html` is deze cyclus zwaar aangepakt (title, schema, FAQ, mobiele ATF). Laat die pagina in cyclus 26 met rust, tenzij de data een regressie laat zien. De warmtepomp-sectie staat wel klaar als eerste kandidaat zodra er gemeten is.
- **Wat er als eerste ligt voor cyclus 26:** warmtepomp-sectie, meta-descriptions onder 160 tekens, breadcrumbs op de vijf kernpagina's, FAQ op Drachten.
- **Wat we willen zien:** of de sticky mobiele CTA iets doet met de doorstroom naar `prijsindicatie.html` — dat is de eerste conversie-ingreep in maanden die op 15 pagina's tegelijk landt. Als GA4-meting hersteld is, zou dit het eerste zichtbare effect moeten zijn.
- **Blijvende nuchterheid:** bij vier organische sessies per maand levert geen van deze taken direct leads op. Ze zorgen dat de site klopt op het moment dat er wél verkeer komt. De echte blokkade zit in escalaties 1, 3 en 4 — niet in de HTML.

---

## Developer Rapport — 17 augustus 2026

### Geïmplementeerde taken

**Taak 1 — `prijsindicatie.html`: kosten-metadata, structured data en mobiele ATF** — volledig, met één afwijking (zie hieronder).
- a) `<title>`, `og:title` en `twitter:title` alle drie vervangen door `Wat kost vloerverwarming per m²? Prijsindicatie Drenthe` (54 tekens).
- b) `BreadcrumbList`-JSON-LD toegevoegd in de `<head>` (Home → Prijsindicatie vloerverwarming), patroon van `vloerverwarming-groningen.html`.
- c) Zichtbare FAQ-accordeon (3 Q&A's, Assen-sjabloon) onderaan `#kosten-uitleg`, direct vóór de `<p class="small">`-disclaimer; woordelijk gespiegeld in een `FAQPage`-JSON-LD in de `<head>`. Teksten letterlijk uit `research_report.md` r. 259–274.
- d) ATF-introblok: tekstlink naar `#kosten-uitleg` toegevoegd, Heerenveen-link vervangen door `vloerverwarming-assen.html`; zin letterlijk uit `research_report.md` r. 279–282.
- e) Introblok heeft klasse `kosten-intro` gekregen en is gesplitst in `.kosten-intro__lead` (essentieel, bevat de kosten-link) en `.kosten-intro__detail` (niet-essentieel). In de bestaande mediaquery met commentaar "Mobile ATF: wizard productkeuze zichtbaar zonder scroll (≤768px)" zijn drie regels bijgezet: kleinere `font-size`/`line-height` en `margin: 0` op de lead, strakkere `margin-bottom` op het blok, en `display: none` op `.kosten-intro__detail`. Desktop ongewijzigd; wizard-markup en -JS niet aangeraakt.

**Taak 2 — Sticky mobiele CTA uitgerold naar 15 pagina's** — volledig.
- Voorcontrole: `.cta-band` is op alle 15 doelbestanden aanwezig (1× op assen/drenthe/groningen/zuidlaren, 2–5× op de rest). Geen pagina overgeslagen.
- Voorcontrole component: CSS aanwezig (`assets/css/critical-index.css` r. 584 e.v.), JS aanwezig (`assets/js/main.js` r. 10–12, `initStickyCta()` met `.cta-band`-lookup).
- Het blok is woordelijk uit `index.html` gekopieerd en op dezelfde plek geplaatst: tussen `</main>` en `<footer class="site-footer">`. Geen wijzigingen in `assets/css/` of `assets/js/`.

**Taak 3 — `faq.html`-schemagat + twee fouten op `index.html`** — volledig.
- a) `"Wat is droge vloerverwarming of laagopbouw?"` toegevoegd op positie 3 in `mainEntity`; `acceptedAnswer.text` is de zichtbare alinea, met de linktekst als platte tekst ("… staat bij systemen en laagopbouw.").
- b) "Welke garantie **horen**" → "Welke garantie **hoort**" op beide plekken (zichtbare knop + JSON-LD).
- c) Ankertekst "vloerverwarming Friesland" → "vloerverwarming Leeuwarden"; `href` ongewijzigd.

**Taak 4 — Alle `<title>`-tags onder 60 tekens** — volledig, 10 bestanden, alle drie de varianten per bestand.
- Bijzonderheid: `vloerverwarming-hoogeveen.html` had afwijkende `og:title`/`twitter:title` ("Hoogeveen, Hollandscheveld & omgeving"); die zijn nu gelijkgetrokken met de nieuwe `<title>`, conform de opdracht "houd ze identiek".

**Taak 5 — `vloerverwarming-zuidlaren.html`** — volledig.
- a) `kopwoningen` → `koopwoningen`; `stomen of egaliseren` → `storten of egaliseren`.
- b) Hero-`lead`: `Tynaarlo, Paterswolde, Bunne, Zuidwolde en Gieten` → `Haren, Glimmen, Eelde-Paterswolde, Vries, Tynaarlo, Yde en De Punt`.
- c) FAQ-sectie (3 Q&A's, Assen-sjabloon) tussen het "Ook actief in"-blok en de CTA-sectie; `FAQPage`-JSON-LD in de `<head>` direct na het bestaande `BreadcrumbList`-script. Teksten letterlijk uit `research_report.md` r. 416–429.

**Afsluiting — `sitemap.xml`:** `<lastmod>` op `2026-08-17` gezet voor de 17 aangeraakte URL's (homepage, diensten, systemen-producten, werkwijze, over-ons, faq, projecten, prijsindicatie en de negen stadspagina's). `contact.html`, `disclaimer.html` en `privacy.html` zijn níét geraakt en houden hun oude datum.

### Overgeslagen taken

- Alle `[WACHT]`- en `[AFGEWEZEN]`-voorstellen: niet aangeraakt, conform opdracht.
- Geen enkele pagina uit taak 2 is overgeslagen — `.cta-band` was overal aanwezig.

### Verificatie per succescriterium

**Taak 1**

| Criterium | Verwacht | Gemeten | Status |
|---|---|---|---|
| `grep -c '"FAQPage"' prijsindicatie.html` | 1 | 1 | gehaald |
| `grep -c '"BreadcrumbList"' prijsindicatie.html` | 1 | 1 | gehaald |
| `grep -c 'Wat kost vloerverwarming per m²' prijsindicatie.html` | ≥ 3 | 5 | gehaald |
| `grep -c 'href="#kosten-uitleg"' prijsindicatie.html` | ≥ 1 | 1 | gehaald |
| `grep -c 'vloerverwarming-heerenveen.html' prijsindicatie.html` | 0 | **1** | **niet gehaald — zie toelichting** |
| `grep -c 'kosten-intro' prijsindicatie.html` | ≥ 2 | 6 | gehaald |
| Elke `"name"` in de `FAQPage` komt woordelijk voor als zichtbare tekst | ja | 3/3 (elke vraagtekst 2× in het bestand: knop + JSON-LD) | gehaald |
| Wizard-flow ongewijzigd | ja | wizard-markup, `data-`attributen en `main.js` niet aangeraakt | gehaald |

**Toelichting bij het niet-gehaalde criterium:** de resterende `vloerverwarming-heerenveen.html` staat níét in het ATF-introblok (die is vervangen door Assen, zoals gevraagd), maar op r. 1058 in de **site-brede footer**, in de regio-lijst die identiek is op alle 22 pagina's. Die link daar weghalen zou de footer van één pagina laten afwijken van de rest — een regressie die de sprint niet vraagt. Conform de gedragsregel "bij twijfel de conservatieve variant" is de footer ongemoeid gelaten. De bedoeling van het criterium (geen Heerenveen-link meer in de redactionele intro) is wél gehaald. Als de PM alsnog 0 wil, is dat een aparte, site-brede beslissing over de footer-regiolijst.

**Taak 2**

| Criterium | Verwacht | Gemeten | Status |
|---|---|---|---|
| `grep -l 'data-sticky-cta' *.html \| wc -l` | 16 | 16 | gehaald |
| `grep -c 'data-sticky-cta' prijsindicatie.html` | 0 | 0 | gehaald |
| `grep -c 'data-sticky-cta' contact.html` | 0 | 0 | gehaald |
| Geen wijzigingen in `assets/css/` of `assets/js/` | ja | `git status --short` toont geen enkel bestand onder `assets/` | gehaald |

De 16 bestanden: `index`, `diensten`, `werkwijze`, `systemen-producten`, `projecten`, `over-ons`, `faq` en de negen `vloerverwarming-*`-pagina's.

**Taak 3**

| Criterium | Verwacht | Gemeten | Status |
|---|---|---|---|
| `grep -c '"name":"Wat is droge vloerverwarming of laagopbouw?"' faq.html` | 1 | 1 | gehaald |
| Aantal `"@type":"Question"` in `faq.html` | 15 | 15 | gehaald |
| Aantal `class="faq-question"` in `faq.html` | gelijk aan bovenstaande | 15 | gehaald |
| `grep -c 'Welke garantie horen' index.html` | 0 | 0 | gehaald |
| `grep -c 'Welke garantie hoort' index.html` | 2 | 2 | gehaald |
| `grep -c 'vloerverwarming Friesland' index.html` | 0 | 0 | gehaald |

**Taak 4**

| Criterium | Verwacht | Gemeten | Status |
|---|---|---|---|
| Geen `<title>` langer dan 60 tekens in de tien bestanden | ja | langste is `index.html` met 58 tekens; stadspagina's 48–53 | gehaald |
| `grep -c 'installateur uit Zuidlaren \| VLWarmte'` over de tien bestanden | 0 | 0 op alle tien | gehaald |
| Per bestand `<title>` = `og:title` = `twitter:title` | ja | 10/10 gecontroleerd, inclusief de gecorrigeerde Hoogeveen-varianten | gehaald |

**Taak 5**

| Criterium | Verwacht | Gemeten | Status |
|---|---|---|---|
| `grep -c '"FAQPage"' vloerverwarming-zuidlaren.html` | 1 | 1 | gehaald |
| `grep -c 'Haren' vloerverwarming-zuidlaren.html` | ≥ 2 | 4 | gehaald |
| `grep -c 'kopwoningen' vloerverwarming-zuidlaren.html` | 0 | 0 | gehaald |
| `grep -c 'stomen of egaliseren' vloerverwarming-zuidlaren.html` | 0 | 0 | gehaald |
| Zichtbare vraagteksten matchen de JSON-LD 1-op-1 | ja | alle drie vraagteksten komen exact 2× voor (knop + JSON-LD) | gehaald |

**Eindstand: 24 van de 25 gecontroleerde criteria gehaald.** Het enige openstaande punt is de footer-Heerenveen-link op `prijsindicatie.html`, bewust zo gelaten.

### Gewijzigde bestanden (`git status --short`)

Door deze sprint gewijzigd (18 bestanden):

```
 M diensten.html
 M faq.html
 M index.html
 M over-ons.html
 M prijsindicatie.html
 M projecten.html
 M sitemap.xml
 M systemen-producten.html
 M vloerverwarming-assen.html
 M vloerverwarming-drachten.html
 M vloerverwarming-drenthe.html
 M vloerverwarming-emmen.html
 M vloerverwarming-groningen.html
 M vloerverwarming-heerenveen.html
 M vloerverwarming-hoogeveen.html
 M vloerverwarming-leeuwarden.html
 M vloerverwarming-zuidlaren.html
 M werkwijze.html
```

Daarnaast staan in de werkboom wijzigingen van andere agenten in deze cyclus (`AGENTS.md`, `docs/website-manager/analytics_report.md`, `research_report.md`, `sprint.md`, `social/weekly_calendar.md`, `.cursor/hooks/state/*`) en vier untracked archiefbestanden onder `docs/website-manager/archive/` en `docs/website-manager/social/archive/`.

Gecontroleerd: **geen** `secrets/`, **geen** `*.env`, **geen** service-account-JSON, **geen** `node_modules` in de wijzigingen. Niets onder `assets/` aangeraakt.

### Deployment

**Nog niet live — PM voert commit + push uit** (`git push origin main`, daarna GitHub Actions / GitHub Pages). Live URL: https://www.vlwarmte.nl

### Aandachtspunten voor de volgende sprint

1. **Footer-regiolijst.** De Heerenveen-link in de footer staat op alle 22 pagina's. Als Heerenveen structureel geen verkeer trekt, is dat een site-brede beslissing (link laten staan of overal vervangen), niet iets voor één pagina. Nu bewust ongemoeid gelaten.
2. **Mobiele ATF is niet visueel getest.** De `kosten-intro`-mediaquery is puur op code geschreven; in deze onbewaakte run is geen browser of viewport-check gedaan. Eerste bezoek aan `prijsindicatie.html` op een echt toestel (≤768px) is de verificatie die nog ontbreekt — controleer of de eerste wizard-stap weer boven de vouw staat.
3. **Sticky CTA op 15 pagina's ineens.** `initStickyCta()` verbergt de knop zodra `.cta-band` in beeld komt. Op pagina's met méérdere `.cta-band`-elementen (werkwijze 5×, over-ons 4×, faq 3×) pakt `document.querySelector` alleen de eerste. Op die pagina's kan de knop dus eerder verdwijnen dan bedoeld. Geen bug, wel een gedragsverschil dat het waard is te bekijken zodra er meting is.
4. **`prijsindicatie.html` is nu zwaar belast.** Vier ingrepen in één cyclus, ongemeten. Conform de sprint-context: cyclus 26 die pagina met rust laten tot er data is; de warmtepomp-sectie staat klaar maar kan wachten.
5. **De meetblokkade staat nog volledig.** GA4-key-events (escalatie 1), kapotte GA4-fetch (escalatie 2) en GSC OAuth (escalatie 3) zijn eigenaar-acties. Zolang die openstaan is het effect van deze sprint — inclusief de sticky CTA op 15 pagina's — niet vast te stellen. `REPLACE_WITH_TOKEN` staat nog in de `<head>` van de aangeraakte pagina's.
