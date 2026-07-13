# Sprint — week van 13 juli 2026 (cyclus 22)

**PM beslissing genomen op:** 13 juli 2026, 06:10
**Doel deze sprint:** De instroom-instorting serieus nemen op de enige hefboom die in autonome modus veilig te bedienen is: **organische vindbaarheid van de bestaande, oudere stadspagina's**. Vier schone, meetklok-veilige SEO-ingrepen (sitemap-signaal, lokale FAQ-schema, breadcrumbs, contextuele interne links) die geen van de rijpende cyclus-20/21-pagina's aanraken, plus de afgesproken laatste CTA-consistentie. De grote betaalde/GSC-hefbomen blijven geblokkeerd → harde escalatie.
**Meetdoel (over ~4 weken, mits GSC weer draait):** Google herindexeert de Drachten-refactor (verse `lastmod`); eerste long-tail-impressies op de verrijkte Groningen-pagina; breadcrumb-/FAQ-rich-result-eligibility zichtbaar in GSC; geen daling in instroom door de wijzigingen (schema/links zijn onzichtbaar voor de bezoeker → geen engagement-risico).

---

## Belangrijkste databevinding deze cyclus (verse GA4, per 13 jul)

1. **Instroom stort verder in — dit is nu hét knelpunt.** ~22 sessies/30d (↓ ~35% van 34). Week 6–12 jul = **4 sessies — de laagste ooit gemeten**. Mei zat op 15–56/week; we draaien op ~7% daarvan.
2. **0 conversies over álle kanalen, derde cyclus op rij.** Bij ~22 sessies kán het te weinig verkeer zijn (lege trechter), maar 3× nul terwijl lead-events afvuren houdt de kans op een **meetfout** (events niet als key event gemarkeerd) open. Nog steeds niet door eigenaar geverifieerd → escalatie, opnieuw.
3. **Betaald kanaal staat feitelijk stil.** `google/cpc` — historisch 100% van alle conversies — is van 12 sessies naar **1 sessie/30d** gevallen. Dat is geen normale werking; wijst op gepauzeerde/afgekeurde campagne. Ads-scripts geblokkeerd in autonome modus → escalatie.
4. **De homepage vangt bijna al het verkeer op (20/22 sessies, ~70% bounce, ~5 s).** Maar: de geo-data laat zien dat een groot deel **buiten de doelregio** valt (North Holland 5, Duitsland 3 > Drenthe 4 + Groningen 1). De hoge bounce is dus deels een **verkeerd-publiek-probleem**, niet puur een pagina-probleem. De hero draagt al de bewezen CTA ("Richtbedrag in 2 minuten →") én de regio (trust-strip). Daarom deze cyclus **géén** homepage-herbouw — dat risico weegt niet op tegen de marginale winst (zie `[WACHT]`).
5. **Structured-data-audit legt vier schone SEO-gaten bloot** (Research Agent), allemaal op **oudere** pagina's / sitemap-metadata — niet op de rijpende cyclus-20/21-pagina's:
   - **Sitemap-signaalgat:** `vloerverwarming-drachten.html` is 6 jul herschreven maar `sitemap.xml` draagt nog `<lastmod>2026-05-22`. Google ziet de refactor niet.
   - **FAQPage-schema alleen op Hoogeveen** — de andere 8 stadspagina's missen de bewezen lokale-FAQ-sjabloon.
   - **Geen enkele `BreadcrumbList`-schema** op de site.
   - **Ongelijke in-body "Ook actief in"-kruislinks** (Assen linkt niet contextueel naar het Friese cluster; Emmen/Leeuwarden wél).
6. **Cyclus-20/21-pagina's rijpen nog** (Heerenveen 1 jul; Drachten-refactor + lead-drempel + CTA 6 jul). Live 7–12 dagen — niet te beoordelen, meetklok niet resetten tot ~27 jul.
7. **GSC blijft blind** (`invalid_grant`, 6+ weken). SEO-effect van cyclus 17–22 niet toetsbaar → langst openstaande blokkade.

Conclusie: een bewuste **SEO-hygiëne- en vindbaarheidscyclus**. Geen nieuwe pagina, geen conversie-tweak op een lege trechter, geen aanraking van rijpende pagina's. In plaats daarvan: de instroom-fundamenten van de bestaande oudere pagina's op orde brengen, zodat organisch verkeer een kans krijgt zodra Google herindexeert. Plus de laatste twee CTA-knoppen gelijktrekken. De echte instroom-hefbomen (Ads, GSC) zijn geblokkeerd → als harde escalatie belegd bij de eigenaar.

---

## Goedgekeurde taken voor Developer Agent

> **Rijp-regel (streng deze cyclus):** raak **niet** aan: `prijsindicatie.html` (wizard/lead-flow), `vloerverwarming-heerenveen.html`, `vloerverwarming-drachten.html` (paginabestand), `contact.html`/`systemen-producten.html`/`werkwijze.html` **behalve** de expliciet benoemde CTA-label-swap in taak 5. Alle schema is **onzichtbaar** voor de bezoeker → geen engagement-effect, dus veilig naast rijpende pagina's.

### Taak 1: `sitemap.xml` — `lastmod` gelijkzetten met de echte deploys `[GOEDGEKEURD]`

**Bron:** Marketing Research Agent (voorstel 1, Hoog).
**Prioriteit:** Hoog (SEO / signaalhygiëne — traffic-onafhankelijk, geen pagina-inhoud)
**Context:** De cyclus-21-refactor van Drachten (6 jul) is crawl-technisch onzichtbaar omdat de sitemap nog `2026-05-22` draagt.
**Actie:**
1. Zet `<lastmod>` van `vloerverwarming-drachten.html` op **`2026-07-06`** (de cyclus-21-deploydatum; het paginabestand zelf niet aanraken).
2. Zet `<lastmod>` op **`2026-07-13`** (vandaag) voor élke URL die **deze sprint** wordt gewijzigd: `vloerverwarming-groningen.html`, `vloerverwarming-assen.html`, `vloerverwarming-drenthe.html`, `vloerverwarming-emmen.html`, `vloerverwarming-hoogeveen.html`, `vloerverwarming-leeuwarden.html`, `vloerverwarming-zuidlaren.html`, `contact.html`, `werkwijze.html`.
3. Laat de overige `lastmod`-waarden ongemoeid (geen bulk-herdatering; alleen echte wijzigingen krijgen een verse datum).
**Succescriterium:** Drachten draagt `2026-07-06`; alle in stap 2 genoemde, deze sprint gewijzigde URL's dragen `2026-07-13`; geen enkele andere `lastmod` gewijzigd; sitemap blijft valide XML.

### Taak 2: `vloerverwarming-groningen.html` — lokale FAQ-sectie + `FAQPage`-schema `[GOEDGEKEURD]`

**Bron:** Marketing Research Agent (voorstel 2, Hoog) — de kern-instroomtaak.
**Prioriteit:** Hoog (SEO / content-verrijking op een bestaande dunne pagina; **geen** nieuwe pagina)
**Context:** Alléén `vloerverwarming-hoogeveen.html` heeft een zichtbare lokale FAQ + `FAQPage`-JSON-LD. Groningen = grootste markt + "installateur"-intentie, maar mist de sjabloon. Sjabloon-referenties in Hoogeveen: JSON-LD op r.49, zichtbare sectie `<h2>Veelgestelde vragen — Hoogeveen</h2>` op r.230.
**Actie:**
1. Kopieer het Hoogeveen-patroon naar Groningen: een zichtbare sectie `<h2>Veelgestelde vragen — Groningen</h2>` met **3** lokaal ingekleurde Q&A's, plus bijbehorend `FAQPage`-JSON-LD in de `<head>` (zelfde structuur als Hoogeveen r.49).
2. Kleur de vragen **lokaal**: (a) kosten ("Wat kost vloerverwarming in Groningen?"), (b) infrezen bestaande dekvloer, (c) werkgebied/randgemeenten met echte plaatsnamen rond Groningen (bijv. Haren, Ten Boer, Zuidhorn, Bedum — nuchter, niet volproppen). Toon = Noord-Nederlands, nuchter; verwijs bij de kosten-vraag naar de prijsindicatie zoals Hoogeveen dat doet.
3. Plaats de zichtbare sectie op een logische plek in de bodyflow (zoals Hoogeveen: vóór het slot/CTA-blok). Verzin geen feiten; blijf binnen wat elders op de site staat.
**Succescriterium:** Groningen toont een zichtbare lokale FAQ met 3 Q&A's; geldig `FAQPage`-JSON-LD in de head (verifieerbaar: `mainEntity` met 3 `Question`-objecten); lokale plaatsnamen kloppen met het werkgebied; pagina blijft valide HTML, geen JS-fouten.

### Taak 3: `BreadcrumbList`-schema op oudere stadspagina's + Drenthe-hub `[GOEDGEKEURD]`

**Bron:** Marketing Research Agent (voorstel 3, Midden).
**Prioriteit:** Midden (SEO / structured data — onzichtbaar voor de bezoeker, versterkt taak 2)
**Context:** Geen enkele pagina draagt breadcrumb-markup. Stadspagina's zijn diepe pagina's (home → regio → stad).
**Actie:** Voeg een `BreadcrumbList`-JSON-LD-blok toe in de `<head>` van de **zes oudere stadspagina's + de hub**: `vloerverwarming-assen.html`, `vloerverwarming-emmen.html`, `vloerverwarming-groningen.html`, `vloerverwarming-hoogeveen.html`, `vloerverwarming-leeuwarden.html`, `vloerverwarming-zuidlaren.html`, `vloerverwarming-drenthe.html`. Hiërarchie per stadspagina: **Home (`/`) → Drenthe-regio (`vloerverwarming-drenthe.html`) → [Stad]** (Friese steden: Home → [Stad], zonder Drenthe-tussenstap waar dat geografisch niet klopt — gebruik je oordeel per pagina). Voor de Drenthe-hub zelf: Home → Drenthe. Gebruik absolute URL's (`https://www.vlwarmte.nl/…`) en de bestaande paginanaam als laatste `name`.
**Bewuste uitsluiting:** `vloerverwarming-heerenveen.html` en `vloerverwarming-drachten.html` **deze cyclus overslaan** (cyclus 20/21, rijpen) — ze krijgen breadcrumb in een volgende sprint. Netto tijdelijke inconsistentie is acceptabel; schema is onzichtbaar.
**Succescriterium:** de 7 genoemde pagina's dragen geldig `BreadcrumbList`-JSON-LD met kloppende hiërarchie en absolute URL's; Heerenveen/Drachten ongemoeid; geen zichtbare wijziging op de pagina's; valide HTML.

### Taak 4: Contextuele "Ook actief in"-interne links op oudere pagina's gelijktrekken `[GOEDGEKEURD]`

**Bron:** Marketing Research Agent (voorstel 4, Midden).
**Prioriteit:** Midden (SEO / internal linking — alleen oudere pagina's, versterkt taak 2 & 3)
**Context:** In-body "Ook actief in"-alinea's kruislinken ongelijk. In `vloerverwarming-assen.html` (`<h2>Ook actief in</h2>` r.195) linkt de contextuele alinea naar Groningen en Emmen, maar **niet** contextueel naar het Friese cluster (Heerenveen/Drachten) — die staan alleen in de footer-lijst. Emmen/Leeuwarden doen dit al wél.
**Actie:** Werk de **in-body** "Ook actief in"-alinea's op de **oudere** pagina's `vloerverwarming-assen.html`, `vloerverwarming-groningen.html` en `vloerverwarming-drenthe.html` bij, zodat ze contextueel (met beschrijvend anker, bijv. "vloerverwarming Heerenveen") kruislinken naar de diepe/competitieve stadspagina's die nu ~0 organisch verkeer krijgen. Houd het natuurlijk: 1–2 extra contextuele links per pagina, geen linklijst-opsomming in de lopende tekst. Footer-regio-lijst ongemoeid. **Je bewerkt uitsluitend de oudere pagina's** — niet de Heerenveen-/Drachten-bestanden (alleen érnaar linken mag).
**Succescriterium:** Assen, Groningen en Drenthe-hub hebben in hun in-body "Ook actief in"-blok elk 1–2 contextuele links méér naar diepe stadspagina's, met beschrijvend anker; geen kunstmatige linkdump; Heerenveen-/Drachten-bestanden ongewijzigd; valide HTML.

### Taak 5: Laatste twee CTA-knoppen gelijktrekken naar "Richtbedrag in 2 minuten →" `[GOEDGEKEURD]`

**Bron:** Analytics Agent (voorstel 4) + Developer Rapport cyclus 21 (openstaande follow-up).
**Prioriteit:** Midden (CTA/conversie — sluit de site-brede CTA-consistentie af)
**Context:** Cyclus 21 zette de bewezen CTA op 22 primaire knoppen, maar liet bewust **2 secundaire** knoppen op "Naar de prijsindicatie" staan (btn-primary-only-regel): `contact.html:95` en `werkwijze.html:152` (beide `class="btn btn-secondary"`). Dit is de afgesproken open follow-up.
**Actie:** Vervang op die twee `btn-secondary`-knoppen de zichtbare tekst "Naar de prijsindicatie" door **"Richtbedrag in 2 minuten →"**. Href (`prijsindicatie.html`), classes en structuur ongewijzigd. Alleen deze twee knoplabels; verder niets op die pagina's aanraken (contact/werkwijze zijn cyclus-20 wizard-first — géén andere wijziging).
**Succescriterium:** geen enkele knop op de site draagt nog "Naar de prijsindicatie"; de twee knoppen tonen "Richtbedrag in 2 minuten →"; href/classes ongewijzigd; geen andere wijziging op contact.html/werkwijze.html.

---

## Uitgestelde voorstellen `[WACHT]`

- **Homepage-entree scherper** (Analytics voorstel 1): de hero draagt al de bewezen CTA én de regio (trust-strip); de hoge bounce is deels een **verkeerd-publiek-probleem** (geo buiten doelregio), dat een hero-tweak niet oplost. Niet de werkende hero riskeren zonder GSC-zicht op de instroombron. Heroverwegen zodra GSC verse zoekterm-/geo-data levert.
- **`prijsindicatie.html` als instroom-asset** (Research voorstel 5, additief kosten-schemablok): waardevol, maar de wizard-/lead-flow rijpt tot ~27 jul — ook een additief blok op díé pagina raakt beter na maturatie. Volgende cyclus.
- **FAQ-schema op de overige stadspagina's** (Emmen, Assen, Leeuwarden, Zuidlaren): één pagina per sprint (Groningen nu); de rest gefaseerd, kwaliteit boven bulk.
- **Wizard-conversie A–D** (Research): lichtere lead-variant/funnel-meting — pas ná ~27 jul (funnel rijpt); taak 1 van cyclus 21 verlaagde de drempel al.
- **Breadcrumb op Heerenveen/Drachten**: inhalen zodra die pagina's uit de rijp-periode zijn (~27 jul).
- **`projecten.html` opwaarderen**: geblokkeerd op eindresultaat-beeldmateriaal (escalatie).

## Afgewezen voorstellen `[AFGEWEZEN]`

- **Nieuwe stadspagina**: instroom fixen op bestaande pagina's, geen dunne pagina's stapelen (max 1/sprint al op Heerenveen ingezet).
- **Homepage-hero herbouwen**: hoog risico op de enige pagina die (relatief) werkt; marginale winst; instroomprobleem is grotendeels verkeer-kwaliteit, niet de pagina.
- **Google Ads-mutaties autonoom**: scripts geblokkeerd in autonome PM-modus → escalatie, geen sprint-taak.

---

## Social Media

**Status:** Weekplanning in `docs/website-manager/social/weekly_calendar.md` (7 posts, week van 13 jul), door PM opgesteld (social-subagent draait onbetrouwbaar in autonome modus — geen dubbel werk).
**Actie vereist:** Handmatige publicatie door VLWarmte-team.
**Focus:** instroom aanjagen — 3 van 7 posts linken direct naar `prijsindicatie.html`; zomer/verbouwing-haak; stadsplaatsen (Groningen, Assen, Emmen, Hoogeveen, Zuidlaren) in captions/hashtags ter ondersteuning van de SEO-instroomfocus.
**Materiaal:** dezelfde beperkte set echte bouwfoto's; eindresultaat-vloer, verdeler-detail en teamfoto ontbreken nog (4 van 7 posts hebben `[FOTO NODIG]`) → escalatie beeldmateriaal.

---

## ESCALATIE — vereist eigenaar (NIET autonoom)

1. **GSC-toegang vernieuwen (langst openstaande blokkade, hoogste prioriteit).** `invalid_grant`, 6+ weken oud. Zonder verse GSC is álle SEO-werk van cyclus 17–22 (incl. deze cyclus se schema/links) blind. Actie: `python scripts/gsc_get_refresh_token.py` met verified owner-account → daarna `gsc_fetch.py` per cyclus.
2. **Conversie-meting verifiëren (opnieuw, harder).** 3 cycli 0 conversies over álle kanalen terwijl lead-events afvuren. Controleer: (a) Formspree-inboxen `xzdojzdk` (calculator) + `xgodnvoq` (contact) — komen daar aanvragen binnen? (b) GA4 → Admin → Events: zijn `wizard_lead_submit` / `lead_form_submit` / `contact_submit` als **key event** gemarkeerd? Zo niet: markeren. 10-minuten-taak, bepaalt of we op conversie of instroom sturen.
3. **Google Ads — serveerstatus + landing (cpc effectief dood).** 1 sessie/30d wijst op gepauzeerde/afgekeurde campagne. Check campagnestatus/afkeuringen; RSA final URL naar `prijsindicatie.html` resp. `contact.html?modus=offerte#aanvraag`; budget pas ná fixes + expliciete spend-goedkeuring. Ads-scripts geblokkeerd in autonome modus → eigenaar/interactieve sessie.
4. **Beeldmateriaal** — eindresultaat-vloer, verdeler-detail, teamfoto in `beeldmateriaal/projecten/` of `docs/website-manager/social/input/`.
5. **Release-mail (stap 8b)** — `python3 scripts/send_pm_release_notes_email.py` met `secrets/hostnet-mail.env` (outbound SMTP geblokkeerd in autonome modus).

---

## Context voor volgende sprint

- **Week ~27 jul:** meetklok van cyclus 19/20/21 uitlezen — eerste lead in Formspree/GA4? Heerenveen-impressies in GSC (mits OAuth vernieuwd)? Effect van de lead-drempel-verlaging?
- **Deze cyclus (SEO-schema/links) is pas toetsbaar zodra GSC draait** — daarom is escalatie 1 kritiek.
- **Instroom-diagnose:** de daling van 56→4 sessies/week is zonder GSC niet te duiden (indexatie/ranking vs. seizoen/volume). Prioriteit voor de eigenaar.
- **Betaald kanaal:** cpc is van 100%-van-conversies naar ~dood — eerst serveerstatus + landing fixen, dan pas budget.
- **Vervolg SEO:** na Groningen de FAQ-sjabloon uitrollen naar Emmen/Assen/Leeuwarden/Zuidlaren; breadcrumb op Heerenveen/Drachten inhalen; homepage-entree heroverwegen met verse geo/zoekterm-data.

---

## Developer Rapport — 13 juli 2026

**Alle 5 goedgekeurde taken uitgevoerd.** Geen enkel rijpend/verboden bestand bewerkt (zie bevestiging onderaan).

### Taak 1 — `sitemap.xml` `lastmod` gelijkgezet
- `vloerverwarming-drachten.html`: `2026-05-22` → **`2026-07-06`** (cyclus-21-deploydatum; paginabestand zelf niet aangeraakt).
- `2026-07-13` gezet op de 9 deze-sprint-gewijzigde URL's: `werkwijze.html`, `vloerverwarming-drenthe.html`, `vloerverwarming-groningen.html`, `vloerverwarming-assen.html`, `vloerverwarming-emmen.html`, `vloerverwarming-hoogeveen.html`, `vloerverwarming-leeuwarden.html`, `vloerverwarming-zuidlaren.html`, `contact.html`.
- Alle overige `lastmod` (home, diensten, systemen-producten, over-ons, faq, projecten, heerenveen, prijsindicatie, disclaimer, privacy) ongemoeid. XML-structuur ongewijzigd → blijft valide.

### Taak 2 — `vloerverwarming-groningen.html`: lokale FAQ + `FAQPage`-schema
- **Head:** `FAQPage`-JSON-LD toegevoegd direct na het bestaande `Service`-blok (nieuw `<script type="application/ld+json">`), met `mainEntity` = 3 `Question`-objecten. Structuur/plaatsing exact gespiegeld op Hoogeveen (r.49).
- **Body:** zichtbare sectie `<h2>Veelgestelde vragen — Groningen</h2>` toegevoegd vóór het slot-CTA-blok, met dezelfde `faq-item`/`faq-question`/`faq-answer`-opmaak als Hoogeveen. 3 Q&A's, lokaal ingekleurd:
  1. "Wat kost vloerverwarming in Groningen?" — verwijst naar de `prijsindicatie` (zoals Hoogeveen).
  2. "Kunnen jullie infrezen in een bestaande dekvloer?" — Groningse jaren 70/80-woningvoorraad.
  3. "In welke plaatsen rond Groningen werken jullie?" — Haren, Ten Boer, Zuidhorn, Bedum (plaatsnamen die al elders op de pagina/site staan; geen nieuwe feiten).
- Zichtbare tekst en JSON-LD-tekst komen 1-op-1 overeen.

### Taak 3 — `BreadcrumbList`-JSON-LD op 7 pagina's (head)
Toegevoegd als los `<script type="application/ld+json">`-blok in de head, absolute URL's:
- **Drentse steden** (Home → Drenthe → Stad): `vloerverwarming-assen.html`, `vloerverwarming-emmen.html`, `vloerverwarming-hoogeveen.html`, `vloerverwarming-zuidlaren.html`.
- **Groningen** (Home → Groningen, **zonder** Drenthe-tussenstap): Groningen ligt geografisch niet in Drenthe → 2-niveau breadcrumb, analoog aan de Friese-uitzonderingsregel.
- **Leeuwarden** (Home → Leeuwarden, zonder Drenthe): Fries.
- **Drenthe-hub** (Home → Drenthe): 2-niveau.
- Heerenveen en Drachten **overgeslagen** (rijpen, cyclus 20/21) — conform bewuste uitsluiting.

### Taak 4 — In-body "Ook actief in"-kruislinks (alleen oudere pagina's)
- `vloerverwarming-assen.html`: extra alinea in het "Ook actief in"-blok met beschrijvende ankers "vloerverwarming in Heerenveen" en "vloerverwarming in Drachten" (Friese cluster; stond eerder alleen in de footer).
- `vloerverwarming-groningen.html`: extra alinea met "vloerverwarming in Drachten" en "vloerverwarming in Heerenveen" (Westerkwartier/Friese kant).
- `vloerverwarming-drenthe.html`: bestaande contextuele zin uitgebreid met "vloerverwarming Drachten" naast de al aanwezige Leeuwarden/Heerenveen-links.
- Natuurlijke lopende tekst (1 extra alinea / 1 extra anker per pagina), geen linkdump. Footer-regio-lijsten ongemoeid. Heerenveen-/Drachten-**bestanden** niet bewerkt — er wordt alleen naartoe gelinkt.

### Taak 5 — CTA-label-swap
- `contact.html` (de `btn btn-secondary` in het wizard-teaser-blok): "Naar de prijsindicatie" → **"Richtbedrag in 2 minuten →"**.
- `werkwijze.html` (de `btn btn-secondary` in de cta-band-stack): idem.
- Href (`prijsindicatie.html`), classes en structuur ongewijzigd; verder niets op die twee pagina's aangeraakt.

### Gewijzigde bestanden (volledige lijst)
1. `sitemap.xml`
2. `vloerverwarming-groningen.html` (taken 2, 3, 4)
3. `vloerverwarming-assen.html` (taken 3, 4)
4. `vloerverwarming-drenthe.html` (taken 3, 4)
5. `vloerverwarming-emmen.html` (taak 3)
6. `vloerverwarming-hoogeveen.html` (taak 3)
7. `vloerverwarming-leeuwarden.html` (taak 3)
8. `vloerverwarming-zuidlaren.html` (taak 3)
9. `contact.html` (taak 5)
10. `werkwijze.html` (taak 5)
11. `docs/website-manager/sprint.md` (dit rapport)

### Afwijkingen / oordeelsbeslissingen
- **Groningen-breadcrumb zonder Drenthe-tussenstap:** de sprint gaf mandaat om per pagina te oordelen ("gebruik je oordeel waar dat geografisch niet klopt"). Groningen valt bestuurlijk/geografisch niet onder Drenthe → 2-niveau breadcrumb, net als de Friese steden.
- Verder geen afwijkingen.

### Bevestiging rijp-regel
**GEEN** rijpende/verboden bestanden aangeraakt: `prijsindicatie.html`, `vloerverwarming-heerenveen.html` en `vloerverwarming-drachten.html` (paginabestanden) zijn **niet** bewerkt — er wordt alleen vanaf andere pagina's naartoe gelinkt, en Drachten's `lastmod` is in de sitemap gezet (raakt het paginabestand niet). `contact.html`/`werkwijze.html` uitsluitend de toegestane CTA-label-swap; `systemen-producten.html` niet aangeraakt.

### Overdracht
- Live URL: https://www.vlwarmte.nl
- Aandachtspunt volgende sprint: FAQ-sjabloon uitrollen naar Emmen/Assen/Leeuwarden/Zuidlaren; breadcrumb op Heerenveen/Drachten inhalen na maturatie (~27 jul).

### PM-verificatie + deployment (13 juli 2026)
- **Grep-verificatie PM (allemaal ✓):** sitemap-`lastmod` — Drachten `2026-07-06`, 9 deze-sprint-URL's `2026-07-13`, overige ongemoeid; geen "Naar de prijsindicatie" meer op de site; Groningen `FAQPage` met 3 `Question`-objecten + zichtbare `<h2>Veelgestelde vragen — Groningen</h2>`; `BreadcrumbList` op exact 7 pagina's (assen/emmen/groningen/hoogeveen/leeuwarden/zuidlaren + drenthe-hub), **niet** op heerenveen/drachten; contextuele kruislinks toegevoegd op assen/groningen/drenthe; geen verboden paginabestanden in de changeset (geen `prijsindicatie.html`/`heerenveen.html`/`drachten.html`/`systemen-producten.html`).
- **Deployment:** PM commit `06ca9a8` (site) + `eef05b7` (release notes) + push naar `main` op 13-07-2026 ~06:15. GitHub-Pages-runs **`29223661697` (success, 38s)** en **`29223721364` (success, 45s)** — geen transiënte deploy-fout deze cyclus.
- **Live geverifieerd:** `Veelgestelde vragen — Groningen` staat live op de Groningen-pagina; GA-tag `G-0BB9M7HYSF` aanwezig in `assets/js/ga-deferred.js`.
- **Nog handmatig (escalatie eigenaar):** release-mail stap 8b (SMTP geblokkeerd in autonome modus), GSC-OAuth vernieuwen, conversie-meting verifiëren, Ads-serveerstatus + landing.
