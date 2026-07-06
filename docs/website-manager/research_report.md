# Marketing Research Rapport — 6 juli 2026 (cyclus 21)

Bron: verse analytics-context (30d per 6 jul 2026), vorig rapport
(`archive`/cyclus 20), sitemap-scan van de root-HTML (incl. `prijsindicatie.html`,
`vloerverwarming-drachten.html`, `vloerverwarming-heerenveen.html`, `index.html`,
`diensten.html`) en vakkennis van de Noord-Nederlandse vloerverwarmingsmarkt.

> **Beperkingen deze cyclus (autonome run zonder live tools):**
> geen WebSearch, geen Bash/netwerk, geen Google Ads-scripts. **Alle zoekvolumes
> hieronder zijn indicatief/geschat** — gebaseerd op prior research en marktkennis,
> niet op een live keyword-tool. Ads-adviezen zijn **escalatie voor de eigenaar**,
> geen autonome actie. GSC is nog steeds ~5+ weken oud (`invalid_grant`) — escalatie.

## Samenvatting

Twee knelpunten tegelijk deze cyclus. **(1) Instroom is structureel weggezakt:**
van ~49–56 sessies/week in mei naar ~9/week nu (~34 sessies/30d), met veel
buiten-regio ruis (12 van 34 sessies uit Noord/Zuid-Holland, Duitsland, Canada).
**(2) De 0-conversie is nieuw en hard:** `google/cpc` viel terug van ~10,5% naar
**0 conversies over álle kanalen**. `prijsindicatie.html` bindt wél sterk (312s,
25% bounce) maar zet niks om — de wizard boeit maar converteert niet.

De grootste traffic-onafhankelijke kansen: **(a) de Drachten-pagina opschonen naar
Drachten-only** nu de Heerenveen-pagina bestaat — de twee pagina's kannibaliseren
elkaar nu op "vloerverwarming Heerenveen" (SEO-winst, geen nieuwe pagina, raakt de
cyclus-20-pagina's niet inhoudelijk); **(b) de wizard een vroegere/lichtere
lead-uitstap geven** — de conversiedrempel zit nu volledig ná de volledige flow;
**(c) GSC deblokkeren** zodat organische effecten weer meetbaar worden. De
Ads-escalatie draait om landing + budget: stuur betaald verkeer naar de wizard
i.p.v. de homepage, en beoordeel of €2/dag nog zin heeft bij 0 conversie.

## Top zoekwoorden

| Zoekwoord | Volume (indicatie) | Concurrentie | Pagina / actie |
|-----------|-------------------|--------------|----------------|
| vloerverwarming heerenveen | laag–midden | **hoog** (5+ dedicated concurrentpagina's) | **bestaand** `vloerverwarming-heerenveen.html` (live cyclus 20) — nu ondermijnd door dubbeling in Drachten-title/H1 |
| vloerverwarming drachten | laag–midden | midden | **bestaand** `vloerverwarming-drachten.html` — title/H1/meta nog "Drachten en Heerenveen"; **verwateren** |
| vloerverwarming drenthe | midden | midden–hoog (ECOtherm, portals) | **bestaand** `vloerverwarming-drenthe.html` — ranken via links + GSC |
| vloerverwarming groningen installateur | midden | midden (ReWo, Kentech, Nadergas) | **bestaand** `vloerverwarming-groningen.html` |
| vloerverwarming friesland / leeuwarden | laag–midden | midden | **bestaand** `vloerverwarming-leeuwarden.html` + Heerenveen/Drachten als Friese cluster |
| vloerverwarming kosten / per m² | hoog (generiek) | hoog | **bestaand** `prijsindicatie.html#kosten-uitleg` — sterk engagement, 0 conv |
| prijs vloerverwarming schuimbeton | laag–midden | laag–midden | **bestaand** wizard schuimbeton-tak — differentiator |
| vloerverwarming infrezen renovatie | midden | midden | **bestaand** FAQ + diensten + stadspagina's; geen aparte pagina nodig |
| installateur / warmtepomp zuidlaren | laag (GSC mei: enkele impr, hoge CTR warmtepomp) | laag | **bestaand** — hyperlokaal; GSC nodig om te meten |
| laagopbouw / droge vloerverwarming | laag–midden | midden | **bestaand** `systemen-producten.html#laagopbouw` — zwakke landing (hoge bounce) |

\* Volume = **indicatief/geschat** (marktkennis + prior GSC mei 2026). Geen live keyword-tool deze cyclus.

## Content gaps (ten opzichte van huidige sitemap)

De acht stadspagina's + Drenthe-hub + Heerenveen-pagina bestaan. Er is **geen nieuwe
pagina nodig**; de winst zit in **opschonen en ontdubbelen** van wat er al staat:

- **`vloerverwarming-drachten.html` — Drachten-only refactor (de duidelijkste gap):**
  Sinds cyclus 20 bestaat `vloerverwarming-heerenveen.html` met een eigen canonical.
  Toch draagt de Drachten-pagina nog steeds:
  - title/meta/OG/twitter: *"Vloerverwarming Drachten **en Heerenveen**…"*
  - `<h1>Vloerverwarming Drachten en Heerenveen</h1>` (regel 89)
  - een volledige `<h2>Vloerverwarming Heerenveen en Zuidwest-Friesland</h2>`-sectie
    (regel 131) plus ~8 verdere Heerenveen-vermeldingen in de body.

  Twee eigen pagina's die op dezelfde term ("vloerverwarming Heerenveen") mikken =
  **keyword-kannibalisatie**: Google moet kiezen welke pagina rankt, en de sterkere
  (nieuwe, dedicated) pagina verliest autoriteit aan de bredere Drachten-pagina.
  **Actie:** Drachten-pagina terugbrengen naar Drachten-only (title/H1/meta), de
  Heerenveen-H2 vervangen door één korte doorverwijs-alinea + interne link naar de
  Heerenveen-pagina (die link staat er al, regel 135 — de rest van de Heerenveen-copy
  kan weg). Geen nieuwe pagina, raakt de Heerenveen-pagina zelf niet.

- **Geen nieuwe dienst-splitsingspagina's** ("alleen schuimbeton", aannemers,
  projectontwikkelaars): nog steeds nul vraagsignaal bij klein volume. Niet doen.

- **`systemen-producten.html#laagopbouw`**: content bestaat; landingervaring blijft
  onderbenut (hoge bounce). Hero/CTA aanscherpen, geen nieuwe pagina — lagere
  prioriteit nu instroom+conversie voorgaan.

- **Reeds gedaan (cyclus 20, niet opnieuw aanpakken):** `diensten.html` cta-band
  wijst nu al primair naar `prijsindicatie.html` ("Richtbedrag in 2 minuten →",
  regel 175) — de oude cyclus-20-aanbeveling is doorgevoerd. Homepage hero + sticky
  mobiele CTA wijzen ook al wizard-first. **Niet terugdraaien.**

## Concurrentie-observaties

Geen live scan deze cyclus; observaties uit prior research blijven staan:

**Regionale installateurs** ranken met **stad × dienst**-pagina's en brede
werkgebied-claims (ECOtherm Drenthe, ReWo Groningen/Drenthe/Friesland, Kentech
Groningen–Assen, plus meerdere dedicated Heerenveen-pagina's — van der Veen, Giet
Mooi, KIBS, ET-F). Sterke patronen bij hen: plaatsnaam in H1/title, vrijblijvende
offerte + snelle reactie, warmtepomp als upsell, "vaste prijs / geen verrassingen".

De concurrentie op Heerenveen is juist **hoog en dedicated** — dat maakt de eigen
Drachten+Heerenveen-dubbeling extra schadelijk: VLWarmte verdunt zijn enige Friese
schot voor open doel over twee pagina's terwijl concurrenten er één sterke
pagina tegenover zetten.

**VLWarmte-onderscheid** dat in copy en Ads moet blijven: **compleet traject**
(ondervloer, schuimbeton, leidingwerk, dekvloer), eigen ploeg uit Zuidlaren,
10 jaar garantie buis, online richtbedrag. Niet concurreren op "goedkoopste".

## Prijscalculator — conversie-optimalisatie (bestaande wizard, niet herbouwen)

### Conclusie

**Niet opnieuw bouwen.** `prijsindicatie.html` ís de calculator: meerstaps-wizard
(twee trajecten: alleen vloerverwarming vs. + schuimbeton), Formspree-lead
(`xzdojzdk`) en volledige GA4-funnel (`wizard_start` → `wizard_product` →
`calculator_result`/`calculator_complete` → `wizard_lead_submit`). Het probleem is
**geen ontbrekende tool maar een funnel-lek**: 312s engagement, 0 conversie.

### Waarom de wizard niet converteert (analyse van de bestaande code)

De frictie zit structureel in de flow, niet in de rekensom:

1. **De lead-uitstap staat volledig ácht­er het eindresultaat.** Het formulier
   (`#calc-form`) zit in het `result-block` dat pas verschijnt ná de laatste stap
   (`calculate()` / `finishSchuim()`). Wie afhaakt bij stap 2–4 — of alleen het
   richtbedrag wil zien en dan weggaat — heeft **geen enkele** kans gehad om een
   spoor achter te laten. 312s gemiddelde duur betekent dat mensen de wizard echt
   doorlopen en het bedrag lezen; het gat zit in de **stap van "bedrag gezien" naar
   "gegevens invullen"**.

2. **De gevraagde velden zijn relatief zwaar voor een eerste contact.** `naam` +
   `telefoon` zijn beide `required`; daarnaast e-mail, woonplaats en startdatum.
   Telefoon-verplicht is een bekende conversiedrempel — bezoekers die "even willen
   kijken" geven niet meteen hun 06.

3. **De belofte onder het bedrag is defensief geformuleerd.** "geen verkoper aan de
   deur", "geen automatische terugbelpoging" is eerlijk en past bij de toon, maar
   het herhaalt vooral wat er **niet** gebeurt. De waarde van hét gesprek ("we
   checken pompafstand, bodem en detailplan gratis") staat er wel, maar mag
   sterker als reden-om-nu-te-handelen.

4. **De uitstap is enkelvoudig zwaar.** De primaire actie is "Offerte aanvragen"
   (formulier). De lichtere alternatieven (bellen / belmoment) staan als bijzin
   naast de knop. Er is geen laagdrempelige "stuur het richtbedrag naar mijn mail"-
   micro-conversie die een e-mailadres vangt zonder telefoon-commitment.

### Voorgestelde optimalisaties (voor de Developer-sprint, geen herbouw)

Prioriteer op basis van meetbaarheid; elk is een kleine ingreep:

- **A. Lichtere lead-variant naast de offerte-knop.** Bied in `.lead-after` een
  tweede, lichtere actie: "Mail mij dit richtbedrag" met alléén e-mail verplicht
  (telefoon optioneel). Dit vangt de "wil kijken, nog niet bellen"-groep. Succes-
  meting: nieuw event `wizard_lead_email` naast `wizard_lead_submit`.
- **B. Telefoon optioneel maken (of e-mail óf telefoon verplicht i.p.v. beide).**
  Verlaagt de invuldrempel op het bestaande formulier zonder de flow te wijzigen.
- **C. Sterkere waarde-zin onder het bedrag.** Vervang de nadruk-op-wat-niet-gebeurt
  door één concrete reden nu te reageren (bv. "binnen één werkdag een opname-afspraak
  in jouw regio; deze maand nog inpasbaar vóór het stookseizoen").
- **D. Meet éérst de funnel-drop.** Draai in de analytics-cyclus de query
  `wizard_start` → `calculator_result` → `wizard_lead_submit`. Als de grote drop
  tussen `calculator_result` en `wizard_lead_submit` zit (verwacht), bevestigt dat
  A–C; zit de drop eerder, dan is het een flow-lengte-probleem.

### Leadgeneratie-koppeling (bestaand)

Formulier na richtbedrag → Formspree → `wizard_lead_submit` (key event) +
`lead_form_submit`. Secundair: `tel:` + `contact.html?modus=bel#aanvraag`.

### Risico's en aandachtspunten

- Bindende prijsclaim blijven vermijden ("indicatie", "richtbedrag", excl. btw) — is nu goed geregeld.
- Hout-ondergrond-route naar contact (geen prijs) behouden — is nu goed geregeld.
- Bij een lichtere e-mail-only variant: privacytekst en verwerking ongewijzigd houden.

### Aanbeveling aan Product Manager

- **Prioriteit:** Hoog (0 conv is nieuw en de wizard is de sterkste pagina)
- **Geschatte ontwikkeltijd:** 3–6 uur (A–C zijn kleine front-end-ingrepen; D is meting)
- **Verwacht effect:** Eerste wizard-leads binnen 2–4 weken; A (e-mail-only) is de meest kansrijke hefboom

## Seizoenspatroon

- **Aanleg:** zomer is klassiek aanlegseizoen (dekvloer droogt ~6 weken vóór
  stookseizoen); juli is nog oriëntatie/offerte-tijd. Wie nu een opname vraagt kan
  vaak nog vóór de winter geregeld worden — bruikbaar als urgentie-argument in de
  wizard-uitstap (optimalisatie C).
- **Zoekintentie kosten:** piekt richting winter/verbouwing (indicatief).
- **Implicatie:** de lage sessies nu zijn vooral **marketingvolume** (Ads €2/dag +
  organisch nog niet ingebakken), niet marktafwezigheid.

## Google Ads — escalatie voor de eigenaar (geen autonome actie deze run)

> Ads-scripts zijn geblokkeerd in deze modus; onderstaande is **advies/escalatie**,
> geen uitgevoerde wijziging.

De harde nieuwe data: **`google/cpc` = 12 sessies, 0 conversies** (30d), terwijl de
ratio vorige cyclus nog ~10,5% was. Twee dingen om te doen, in deze volgorde:

1. **Landing verleggen naar de wizard (eerst — kost geen extra spend).** Beide eerdere
   conversies landden op `/` (homepage), niet op de wizard. Bij 0 conversie nu is de
   homepage-landing verdacht: bezoekers met koop-/prijsintentie horen direct op
   `prijsindicatie.html` te landen, niet op de merk-homepage. **Advies:** zet de
   final URL van de RSA('s) op `prijsindicatie.html` (of `contact.html?modus=offerte#aanvraag`
   voor de puur offerte-gerichte adgroep), houd de sitelink "Prijsindicatie" en de
   headline "Richtbedrag in 2 minuten" prominent. Combineer dit met wizard-optimalisatie
   A–C hierboven zodat de landing ook echt converteert.
2. **Budget pas beoordelen ná de landing-fix.** €2/dag verhogen terwijl de landing
   0% converteert = meer geld naar een lekkende funnel. **Advies aan eigenaar:**
   houd budget op €2/dag tot (a) de wizard-landing live is en (b) 2 weken data
   binnen is; overweeg dán een test naar €5–10/dag. Budgetverhoging **alleen na
   expliciete spend-goedkeuring in chat**.
3. **Negatieven / geo-ruis:** 12 van 34 sessies komen buiten de regio (NH/ZH/DE/CA).
   Geo-targeting stond in cyclus 20 correct op DR+GR+FR; de ruis is waarschijnlijk
   organisch/direct, niet betaald. **Advies:** bij de landing-fix ook in de Ads UI
   controleren of er geen "presence or interest"-targeting aanstaat die buiten-regio
   vertoningen toelaat.

## GSC-status

| Item | Status |
|------|--------|
| `secrets/gsc.env` | Aanwezig |
| `gsc_fetch.py` | **Mislukt** — `invalid_grant` (refresh token verlopen) |
| Laatste export | ~5+ weken oud |
| Actie | Eigenaar: `python scripts/gsc_get_refresh_token.py` met verified owner-account; daarna `gsc_fetch.py` per cyclus |

Zonder verse GSC blijven de Heerenveen-pagina (cyclus 20), de stadlinks en de
Drachten-refactor (deze cyclus) **niet toetsbaar** op organisch effect.

## Aanbevelingen voor Product Manager (max 8, op prioriteit)

### 1. Drachten-pagina → Drachten-only (ontdubbelen met Heerenveen)

- **Prioriteit:** Hoog
- **Type:** SEO / content update (traffic-onafhankelijk, raakt cyclus-20-pagina niet)
- **Onderbouwing:** `vloerverwarming-drachten.html` draagt nog title/H1/meta
  "Drachten **en Heerenveen**" + een volledige Heerenveen-H2, terwijl de dedicated
  `vloerverwarming-heerenveen.html` sinds cyclus 20 live is. Twee eigen pagina's op
  dezelfde term = keyword-kannibalisatie; de sterkere pagina verliest.
- **Actie:** Developer: title/H1/meta/OG naar Drachten-only; Heerenveen-H2 (regel 131)
  vervangen door één korte alinea + de bestaande interne link naar de Heerenveen-pagina;
  overige Heerenveen-body-vermeldingen terugbrengen tot hooguit een terloopse noemer.
- **Verwacht effect:** Heerenveen-pagina wint rankingsautoriteit; Drachten scherper.

### 2. Wizard-conversie — lichtere lead-uitstap (e-mail-only)

- **Prioriteit:** Hoog
- **Type:** CRO / content update
- **Onderbouwing:** 312s engagement, 0 conversie. Lead-formulier staat volledig ná
  het eindresultaat; naam+telefoon beide verplicht. Grote drempel voor "wil kijken".
- **Actie:** Developer: tweede, lichtere actie in `.lead-after` ("Mail mij dit
  richtbedrag", alléén e-mail verplicht) + telefoon optioneel op het hoofdformulier +
  sterkere waarde-zin onder het bedrag. Nieuw event `wizard_lead_email`.
- **Verwacht effect:** Eerste wizard-leads binnen 2–4 weken; meest kansrijke hefboom op de 0-conversie.

### 3. Ads-landing verleggen naar de wizard (escalatie eigenaar)

- **Prioriteit:** Hoog
- **Type:** Ads / CRO (escalatie — geen autonome actie deze run)
- **Onderbouwing:** 12 cpc-sessies, 0 conv; eerdere conversies landden op `/`. Merk-
  homepage is de verkeerde landing voor prijs-/koopintentie.
- **Actie:** Eigenaar/Marketing: RSA final URL → `prijsindicatie.html` (koop-adgroep)
  resp. `contact.html?modus=offerte#aanvraag` (offerte-adgroep); sitelink "Prijsindicatie"
  + headline "Richtbedrag in 2 minuten" prominent. Koppelen aan aanbeveling 2.
- **Verwacht effect:** Betaald verkeer landt op de converterende pagina i.p.v. de homepage.

### 4. GSC OAuth vernieuwen

- **Prioriteit:** Hoog
- **Type:** Infra / SEO (escalatie)
- **Onderbouwing:** Token verlopen; data 5+ weken oud. Zonder GSC zijn cyclus 20 +
  deze cyclus (Heerenveen, Drachten-refactor) niet toetsbaar.
- **Actie:** Eigenaar: `scripts/gsc_get_refresh_token.py` → `gsc_fetch.py` per cyclus.
- **Verwacht effect:** Organische effecten stadspagina's + Zuidlaren-termen weer meetbaar.

### 5. Wizard-funnel meten vóór verdere ingrepen

- **Prioriteit:** Midden
- **Type:** Meting / CRO
- **Onderbouwing:** Bevestig waar de drop zit vóór je meer bouwt.
- **Actie:** Analytics: query `wizard_start` → `calculator_result` → `wizard_lead_submit`.
  Drop tussen result en submit bevestigt aanbeveling 2; eerdere drop = flow-lengte.
- **Verwacht effect:** Gerichte fix i.p.v. gissen.

### 6. Ads-budget beoordelen — pas ná landing-fix (escalatie eigenaar)

- **Prioriteit:** Midden
- **Type:** Ads / spend (escalatie)
- **Onderbouwing:** €2/dag verhogen terwijl de landing 0% converteert is zonde.
  Eerst landing (aanbeveling 3) + wizard (2), dan 2 weken meten.
- **Actie:** Eigenaar: budget op €2/dag houden tot landing live + data binnen;
  daarna eventueel test €5–10/dag — **alleen na expliciete spend-goedkeuring in chat**.
- **Verwacht effect:** Geen geld naar een lekkende funnel; schaalbeslissing op data.

### 7. Stadspagina's — social traffic naar de juiste pagina

- **Prioriteit:** Midden
- **Type:** Social / SEO
- **Onderbouwing:** Instroom is het hoofdknelpunt; stadspagina's krijgen buiten
  Drachten/Zuidlaren nauwelijks sessies. Social is een traffic-onafhankelijke hefboom.
- **Actie:** `weekly_calendar.md`: 1–2 posts met directe link naar een stadspagina
  (incl. de nieuwe Heerenveen-pagina), niet alleen home/wizard. Hashtags: max 1–2
  regionaal (#Heerenveen, #Drachten, #ZuidLaren).
- **Verwacht effect:** Eerste sessies op Friese cluster + hub.

### 8. `systemen-producten.html` — landing-hero aanscherpen

- **Prioriteit:** Laag
- **Type:** Content / CTA
- **Onderbouwing:** Hoge bounce op laagopbouw-intent; lager dan 1–3 nu instroom
  + conversie voorgaan.
- **Actie:** Developer (later): hero met concrete belofte + regio + primaire CTA
  wizard; trust-regel (10 jaar garantie buis, reactie binnen één werkdag). Geen
  tweede formulier, geen nieuwe pagina.
- **Verwacht effect:** Lagere bounce op laagopbouw-intent.

---

## Escalaties (menselijke actie vereist)

1. **Ads-landing + budget** — RSA final URL naar de wizard (kost geen spend);
   budgetverhoging pas ná landing-fix en alleen met expliciete spend-goedkeuring.
2. **GSC OAuth** — `invalid_grant`; refresh token opnieuw genereren, anders blijft
   organisch (incl. deze cyclus) blind.
3. **Beeldmateriaal** — `projecten.html` en social blijven beperkt zonder nieuwe
   foto's in `beeldmateriaal/projecten/`.

---

### Samenvatting voor de Product Manager

- **SEO-quick-win (dev, traffic-onafhankelijk):** Drachten-pagina ontdubbelen naar
  Drachten-only — de nieuwe Heerenveen-pagina wordt nu gekannibaliseerd door
  "Drachten en Heerenveen" in title/H1 + een hele Heerenveen-sectie.
- **Conversie (dev):** de wizard bindt (312s) maar heeft geen lichte uitstap —
  voeg een e-mail-only "mail mij het richtbedrag" toe en maak telefoon optioneel.
- **Ads (escalatie):** stuur betaald verkeer naar de wizard i.p.v. de homepage;
  beoordeel budget pas ná die landing-fix. 0 conversie op alle kanalen is nieuw.
- **GSC:** nog steeds geblokkeerd — eerst OAuth, dan effect meten.
- **Volume-context:** zoekvolumes dit rapport zijn indicatief/geschat (geen live tools deze run).
