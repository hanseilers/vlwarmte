# Sprint — week van 6 juli 2026 (cyclus 21)

**PM beslissing genomen op:** 6 juli 2026, 06:20
**Doel deze sprint:** De verse 0-conversie-bel serieus nemen zonder de cyclus-20-pagina's opnieuw om te gooien: lead-drempel op de wizard verlagen, keyword-kannibalisatie tussen Drachten en de nieuwe Heerenveen-pagina opheffen, en de bewezen sterke CTA-tekst site-breed gelijktrekken.
**Meetdoel (over ~4 weken in GA4/Formspree):** eerste lead(s) via `prijsindicatie.html` (of aantoonbaar in Formspree-inbox `xzdojzdk`); Heerenveen-pagina begint autoriteit te winnen nu Drachten niet meer op dezelfde term meedingt; geen daling in wizard-instroom door de CTA-labelwissel. Parallel: eigenaar verifieert of de 0-conversie echt is of een GA4-meetfout (key events).

---

## Belangrijkste databevinding deze cyclus (verse GA4, per 6 jul)

1. **0 conversies over álle kanalen** — nieuw. `google/cpc` viel terug van ~10,5% ratio (2 leads vorige cyclus) naar 0. Direct (15), cpc (12), organic (6), AI (1) = ~34 sessies, geen enkele conversie.
2. **Instroom blijft het knelpunt.** ~34 sessies/30d (↓ van 38); week 29 jun–5 jul = 9 sessies. Mei zat op 49–56/week — we draaien op ~20% daarvan.
3. **De wizard boeit, maar zet niet om.** `prijsindicatie.html`: 312 s gem. duur, 25% bounce (sterkste engagement van de site) — tóch 0 conversie. Het lead-formulier ná het richtbedrag vereist **naam én telefoon**; e-mail is optioneel. Wie het bedrag ziet maar niet wil bellen, kan geen spoor achterlaten.
4. **Keyword-kannibalisatie Drachten ↔ Heerenveen.** `vloerverwarming-drachten.html` draagt nog steeds title/H1/meta *"Vloerverwarming Drachten én Heerenveen"* plus een volledige `<h2>Vloerverwarming Heerenveen en Zuidwest-Friesland</h2>`-sectie — terwijl de dedicated `vloerverwarming-heerenveen.html` sinds cyclus 20 (1 jul) live is met eigen canonical. Twee eigen pagina's op dezelfde term → de nieuwe pagina verliest autoriteit.
5. **Cyclus-20-ingrepen te vers** (live 1 jul, 5 dagen). Heerenveen-pagina verschijnt nog niet in het 30d-venster — niet als mislukking lezen. Contact/systemen/werkwijze wizard-first ook onbeoordeelbaar tot ~27 jul.
6. **CTA-tekst inconsistent.** De geteste sterke knoptekst "Richtbedrag in 2 minuten →" staat op sommige plekken (o.a. diensten cta-band, cyclus-20-pagina's); het bravere "Naar de prijsindicatie" staat nog op ~24 knoppen/links verspreid over 15 pagina's, inclusief de diensten-hero.
7. **Meetonzekerheid.** De site vuurt lead-events af (`wizard_lead_submit`, `lead_form_submit`, `contact_submit`), maar GA4 telt 0 conversies. Óf de emmer lekt (te weinig verkeer), óf de meter is kapot (events niet als **key event** gemarkeerd in GA4). Grondwaarheid = de Formspree-inboxen. Dit bepaalt of alle conversie-optimalisatie zin heeft → escalatie eigenaar.
8. **GSC nog 5+ weken oud** (`invalid_grant`) — SEO-effect cyclus 17–21 niet meetbaar.

Conclusie: een **bewust lichte cyclus**. Cyclus 20 heeft vijf dagen geleden vijf pagina's aangeraakt — die moeten rijpen. Deze sprint doet drie schone, elkaar niet-tegensprekende ingrepen die de meetklok van cyclus 19/20 niet resetten (één bewuste uitzondering op de wizard-leadstap, met onderbouwing), plus een harde escalatie op de meetkwestie.

---

## Goedgekeurde taken voor Developer Agent

### Taak 1: `prijsindicatie.html` — lead-drempel verlagen `[GOEDGEKEURD]`

**Bron:** Analytics Agent (voorstel 2) + Marketing Research Agent (voorstel 2) — beide onafhankelijk als #1 geprioriteerd.
**Prioriteit:** Hoog (conversie — direct op de 0-conversie-bel)
**Context:** In `#calc-form` (Formspree `xzdojzdk`) zijn zowel `#c-name` als `#c-phone` `required`; `#c-email` is optioneel. De verplichte telefoon is de meest waarschijnlijke afhaakreden op de best-bindende pagina van de site.
**Actie:**
1. Maak telefoon **optioneel**: verwijder `required` van `#c-phone` (laat het veld staan).
2. Maak e-mail **verplicht**: voeg `required` toe aan `#c-email` (heeft al `type="email"`). Minimale inzending wordt daarmee **naam + e-mail**, bellen hoeft niet.
3. Pas de sub-copy (`#lead-after-sub` / `lead-sub`) en/of een klein hulpzinnetje onder de knop aan zodat de lichtere weg duidelijk is, bijv.: *"Liever alleen je richtbedrag per mail? Vul je e-mail in — bellen hoeft niet."* Toon blijft nuchter.
4. **Wizard-stappen zelf niet aanraken** — alleen het lead-blok ná het resultaat. Geen tweede formulier bouwen; één `#calc-form` houden.
**Succescriterium:** formulier submit met alleen naam + e-mail (zonder telefoon); telefoon nog steeds invulbaar; hulpcopy zichtbaar; pagina werkt zonder JavaScript-fouten. Meetbaar: eerste lead in Formspree-inbox `xzdojzdk` / eerste `wizard_lead_submit` binnen 4 weken.
**PM-notitie (bewuste uitzondering op de rijp-regel):** dit raakt de cyclus-19-leadstap die "tot ~27 jul zou rijpen". Reden om tóch nu te doen: er is géén positief signaal om te beschermen (0 conversies), friction-verlaging is onvoorwaardelijk gunstig, en beide specialistische agents prioriteerden het onafhankelijk als #1. De rijp-regel beschermt attributie van een meetbaar effect — dat effect is hier nul.

### Taak 2: `vloerverwarming-drachten.html` — terug naar Drachten-only `[GOEDGEKEURD]`

**Bron:** Marketing Research Agent (voorstel 1) + openstaande follow-up cyclus-20 Developer Rapport.
**Prioriteit:** Hoog (SEO — heft kannibalisatie op)
**Actie:**
1. Title, meta description, OG- en Twitter-title/description terug naar **Drachten-only** (verwijder "en Heerenveen"). Behoud de nuchtere toon en de reistijd-formulering waar die klopt.
2. H1 → "Vloerverwarming Drachten" (zonder Heerenveen).
3. Vervang de volledige `<h2>Vloerverwarming Heerenveen en Zuidwest-Friesland</h2>`-sectie (± regel 131) door **één korte alinea** die naar de dedicated pagina verwijst met de reeds aanwezige interne link `vloerverwarming Heerenveen` → `vloerverwarming-heerenveen.html`. Eén verwijzing is genoeg; verwijder de overige losse Heerenveen-vermeldingen in kop- en bodytekst waar ze de Drachten-focus verwateren (losse links naar de Heerenveen-pagina in een regio-rijtje mogen blijven).
4. Canonical blijft `https://www.vlwarmte.nl/vloerverwarming-drachten.html`.
**Succescriterium:** Drachten-pagina richt zich in title/H1/meta uitsluitend op Drachten; precies één duidelijke interne link naar de Heerenveen-pagina; geen dubbele Heerenveen-H2-sectie meer; pagina blijft volwaardig (geen kale/dunne pagina).

### Taak 3: Wizard-CTA-tekst site-breed gelijktrekken naar "Richtbedrag in 2 minuten →" `[GOEDGEKEURD]`

**Bron:** Analytics Agent (voorstel 3) + eigen scan (24 voorkomens over 15 pagina's).
**Prioriteit:** Midden (CTA/conversie — versterkt de geteste variant)
**Context:** Primaire knoppen met tekst "Naar de prijsindicatie" staan o.a. op de diensten-hero (r.73), faq, over-ons, werkwijze en de stadspagina's; de bewezen sterkere tekst "Richtbedrag in 2 minuten →" staat elders al.
**Actie:** Vervang op **primaire knoppen** (`class="btn btn-primary"`) de zichtbare tekst "Naar de prijsindicatie" door **"Richtbedrag in 2 minuten →"**, over alle root-`*.html` waar dat voorkomt. **Laat inline-tekstlinks** (lopende zin, bijv. "…vraag een `prijsindicatie` aan") **ongemoeid** — alleen knoplabels. Href, classes en omliggende structuur niet wijzigen.
**Succescriterium:** geen primaire wizard-knop draagt nog "Naar de prijsindicatie"; alle primaire wizard-knoppen tonen "Richtbedrag in 2 minuten →"; inline-tekstlinks onveranderd; geen dubbele/gebroken knoppen. (Label-only wissel — raakt geen funnel-meting van cyclus 20.)

---

## Uitgestelde voorstellen `[WACHT]`

- **Wizard-funnel opnieuw meten** (Analytics/Research): cyclus-19 leadstap → `wizard_lead_submit` + funnel-events uitlezen op week ~27 jul. Taak 1 verlaagt nu wel de drempel; funnel-analyse volgt na rijping.
- **Cyclus-20-pagina's beoordelen** (Heerenveen, contact, systemen, werkwijze): live 1 jul, te vers — niet aanraken tot GA4/GSC-data er is (~27 jul).
- **Google Ads landing + budget** (Research Ads-escalatie): eerst RSA final URL's richten (koop-adgroep → `prijsindicatie.html`, offerte-adgroep → `contact.html?modus=offerte#aanvraag`); budgetverhoging (€2 → €5–10/dag) pas ná landing-fix + 2 weken data en alleen met expliciete spend-goedkeuring eigenaar. Scripts geblokkeerd in autonome modus → zie escalatie.
- **GSC OAuth vernieuwen**: `invalid_grant` — eigenaar draait `scripts/gsc_get_refresh_token.py`.
- **`projecten.html` opwaarderen** (14 s duur, 18 sessies/90d): geblokkeerd op eindresultaat-beeldmateriaal.
- **over-ons.html trust/CTA aanscherpen** (27 s, laag scroll): kandidaat volgende cyclus als deze sprint gerijpt is.

## Afgewezen voorstellen `[AFGEWEZEN]`

- **Nieuwe stadspagina deze cyclus**: max 1 nieuwe pagina/sprint is vorige cyclus op Heerenveen ingezet; bij ~2 sessies per bestaande stadspagina voegt nóg een dunne pagina niets toe. Instroom fixen, geen pagina's stapelen.
- **Prijscalculator herbouwen**: `prijsindicatie.html` ís de calculator en bindt sterk (312 s). Niet herbouwen — alleen de lead-uitstap lichter maken (taak 1).
- **diensten.html hero als aparte taak**: valt onder taak 3 (de hero-knop is één van de "Naar de prijsindicatie"-voorkomens).

---

## Social Media

**Status:** Weekplanning in `docs/website-manager/social/weekly_calendar.md` (7 posts, week van 6 jul), door PM opgesteld (subagent-run mislukte — geen dubbel werk).
**Actie vereist:** Handmatige publicatie door VLWarmte-team.
**Focus:** wizard-instroom (`prijsindicatie.html`) + de nieuwe Heerenveen-pagina promoten, plus Drachten/Zuidlaren/Drenthe-hub.
**Materiaal:** dezelfde beperkte set echte bouwfoto's (Zuidlaren/Zeegse mei 2026 + input/); eindresultaat-vloer, verdeler-detail en teamfoto ontbreken nog steeds.

---

## ESCALATIE — vereist eigenaar (NIET autonoom)

1. **Conversie-meting verifiëren (eerst!)** — 0 conversies over álle kanalen is verdacht. Controleer: (a) Formspree-inboxen `xzdojzdk` (calculator) en `xgodnvoq` (contact) — komen daar wél aanvragen binnen? (b) GA4 → Admin → Events: zijn `wizard_lead_submit` / `lead_form_submit` / `contact_submit` als **key event** gemarkeerd? Zo niet, dan is "0 conversies" een meetfout, niet de werkelijkheid. Dit bepaalt of taak 1 en het budgetbesluit ergens op gebaseerd zijn.
2. **Google Ads landing + budget** — RSA final URL's op de juiste landing zetten (kost geen spend). Budget €2 → €5–10/dag pas ná landing-fix + goedkeuring. `scripts/google_ads_*` geblokkeerd in autonome PM-modus; eigenaar of interactieve sessie nodig.
3. **GSC OAuth** — `python scripts/gsc_get_refresh_token.py` met verified owner-account; daarna `gsc_fetch.py` in volgende cyclus.
4. **Beeldmateriaal** — eindresultaat-vloer, verdeler-detail en teamfoto in `beeldmateriaal/projecten/` of `docs/website-manager/social/input/`.
5. **Release-mail (stap 8b)** — `python3 scripts/send_pm_release_notes_email.py` met `secrets/hostnet-mail.env` (outbound SMTP geblokkeerd in autonome modus).

---

## Context voor volgende sprint

- **Week ~27 jul:** meetklok van cyclus 19/20 én de nieuwe taak 1 (lead-drempel) uitlezen — eerste lead in Formspree/GA4? Heerenveen-pagina impressies in GSC (mits OAuth vernieuwd)?
- **Meetkwestie:** als eigenaar bevestigt dat events geen key events zijn, dan is de hele "0-conversie"-lezing van cyclus 20–21 een artefact — herijk de conversie-strategie op Formspree-grondwaarheid.
- **Betaald kanaal:** was 100% van conversies, nu 0 — eerst landing-URL fixen, dan pas budget.
- **Drachten/Heerenveen:** na de refactor volgen welke van de twee gaat ranken; bij succes overweeg Drachten interne links verder aanscherpen.

---

## Developer Rapport — 6 juli 2026

**Geïmplementeerde taken:**

- **Taak 1 — `prijsindicatie.html` lead-drempel verlaagd.** In `#calc-form` (Formspree `xzdojzdk`): `required` verwijderd van `#c-phone` (label → "Telefoon (optioneel)", veld blijft staan); `required` toegevoegd aan `#c-email` (label → "E-mail *"). Minimale inzending is nu naam + e-mail. Hulpzinnetje toegevoegd als apart statisch element boven de submit-knop: *"Liever alleen je richtbedrag per mail? Vul je e-mail in — bellen hoeft niet."* (class `lead-mail-hint small`). Bewuste keuze: dit zinnetje staat NIET in `#lead-after-sub`, want die tekst wordt dynamisch overschreven door `setLeadCopy()` (r.1200/1224/1245/1416) — een statische regel botst daar niet mee. Wizard-stappen ongemoeid; één `#calc-form` behouden; pagina werkt zonder JS.
- **Taak 2 — `vloerverwarming-drachten.html` terug naar Drachten-only.** Title, meta description, og:title/description, twitter:title/description → "en Heerenveen" verwijderd. H1 → "Vloerverwarming Drachten". Hero-eyebrow, lead-alinea, "Waarom"-H2, body-alinea, infrees-H2 + body en slot-H2 ontdaan van Heerenveen-vermeldingen die de Drachten-focus verwaterden. De volledige `<h2>Vloerverwarming Heerenveen en Zuidwest-Friesland</h2>`-sectie vervangen door één korte alinea met de bestaande interne link `vloerverwarming Heerenveen` → `vloerverwarming-heerenveen.html`. De regio-rijtje-link naar Heerenveen (r.217) is behouden. Canonical ongewijzigd. JSON-LD stond al op Drachten-only (ongemoeid gelaten). Pagina blijft volwaardig.
- **Taak 3 — Wizard-CTA-tekst gelijkgetrokken.** "Naar de prijsindicatie" → "Richtbedrag in 2 minuten →" op alle **primaire** knoppen (`class="btn btn-primary"`) in 15 root-`*.html`: contact.html (0 primair), diensten.html (1), over-ons.html (2), systemen-producten.html (1), faq.html (2), vloerverwarming-emmen.html (2), vloerverwarming-drenthe.html (1), vloerverwarming-leeuwarden.html (2), vloerverwarming-hoogeveen.html (2), vloerverwarming-drachten.html (2), vloerverwarming-groningen.html (1), vloerverwarming-assen.html (1), vloerverwarming-heerenveen.html (2), werkwijze.html (2), vloerverwarming-zuidlaren.html (1) = **22 primaire knoppen**. Href, classes en structuur ongewijzigd; inline-tekstlinks ongemoeid.

**Afwijking van de instructie (let op PM):** de sprint noemde 24 voorkomens over 15 bestanden, met contact.html(1) en werkwijze.html(3). Bij inspectie bleken **2 van die voorkomens `btn-secondary`, geen `btn-primary`**: `contact.html:95` en `werkwijze.html:152`. Conform de expliciete regel ("alleen knoplabels op btn-primary") zijn die twee **bewust ongewijzigd gelaten** — er staat dus nog "Naar de prijsindicatie" op die twee secundaire knoppen. Netto 22 primaire knoppen aangepast i.p.v. 24. Als de PM ook die twee secundaire knoppen wil gelijktrekken, is dat een aparte beslissing (viel buiten "primaire knoppen").

**Overgeslagen taken:** geen — alle drie `[GOEDGEKEURD]`-taken uitgevoerd. Geen andere pagina's/secties aangeraakt (cyclus-20 hero's/cta-bands op contact/systemen/werkwijze alleen via de label-swap in taak 3). GA4-snippet ongemoeid.

**Gewijzigde bestanden (17):** `prijsindicatie.html`, `vloerverwarming-drachten.html`, `diensten.html`, `over-ons.html`, `systemen-producten.html`, `faq.html`, `vloerverwarming-emmen.html`, `vloerverwarming-drenthe.html`, `vloerverwarming-leeuwarden.html`, `vloerverwarming-hoogeveen.html`, `vloerverwarming-groningen.html`, `vloerverwarming-assen.html`, `vloerverwarming-heerenveen.html`, `werkwijze.html`, `vloerverwarming-zuidlaren.html`, plus dit `sprint.md`-rapport.

**Deployment:** **Live** — PM commit `450917f` (site) + `409bd39` (release notes) + push naar `main` op 06-07-2026 06:30. Eerste GitHub-Pages-run `28767499003` faalde op de deploy-stap met een transiënte fout ("Deployment failed, try again later" — build zelf ✓ in 20s, geen codeprobleem); de release-notes-push triggerde run `28767542535`: **success** (deploy ✓ in 11s). Live geverifieerd: Drachten-title nu Drachten-only, `prijsindicatie.html` mail-hint ("bellen hoeft niet") live, CTA-tekst "Richtbedrag in 2 minuten" live op diensten, GA4-tag `G-0BB9M7HYSF` in `assets/js/ga-deferred.js`.

**Live URL's:** https://www.vlwarmte.nl/prijsindicatie.html · https://www.vlwarmte.nl/vloerverwarming-drachten.html

**Aandachtspunt CTA-swap:** 2 van de 24 voorkomens van "Naar de prijsindicatie" bleken `btn-secondary` (`contact.html`, `werkwijze.html`) en zijn conform de btn-primary-only-regel bewust ongemoeid gelaten — netto 22 primaire knoppen gewijzigd. Volgende cyclus: besluiten of die twee secundaire knoppen ook meegaan.
