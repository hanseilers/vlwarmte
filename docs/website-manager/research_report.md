# Marketing Research Rapport — 17 augustus 2026 (cyclus 25)

**Type run:** on-site SEO- en content-audit van de repo + zoekwoordadvies op domeinkennis.
**Niet gedaan deze run (geblokkeerd):** geen WebSearch/WebFetch, geen verse GA4, geen GSC, geen
Google Ads-scripts of -mutaties. Het Ads-account staat op `CLOSED` — dat blijft een eigenaarstaak,
geen developer-taak.

**Waar de cijfers vandaan komen:** GA4-export van 5 augustus (12 dagen oud). 17 sessies/30d,
homepage 85% bounce en 71% van alle landings, `prijsindicatie.html` 4 sessies/30d met 112 s
gemiddelde engagement, doelregio 1 sessie (Drenthe 0, Friesland 0), 0 conversies voor de vijfde
cyclus op rij, organisch 4 sessies.

---

## Samenvatting

Bij 17 sessies per maand is geen enkele conclusie over bounce of gedrag statistisch hard. Wat wél
hard is: de site is technisch netjes gebouwd, maar de enige pagina die groeit —
`prijsindicatie.html` — is tegelijk de slechtst geoptimaliseerde pagina van de hele site. Geen
structured data, een `<title>` van 76 tekens die geen enkele zoekterm raakt die iemand intikt, en
een H1 ("Prijsindicatie vloerverwarming") waar niemand op zoekt. Terwijl er dieper op die pagina
concrete, bruikbare kosteninformatie staat (€45–€95 per m², voorrijkosten, drie prijsdrijvers) die
precies de vraag beantwoordt waar de meeste zoekvolume in deze markt zit.

Tweede bevinding: alle negen stadspagina's en de homepage hebben een `<title>` boven de 60 tekens.
Dat betekent dat in de zoekresultaten structureel het einde wegvalt. Zeven pagina's hebben ook een
meta-description boven de 160 tekens.

Derde: `faq.html` heeft vijftien zichtbare vragen maar veertien in het `FAQPage`-schema. De vraag
over laagopbouw/droge vloerverwarming ontbreekt in de JSON-LD — juist de vraag met de minste
concurrentie in deze regio.

Er komt deze sprint **geen nieuwe pagina** bij. Negen stadspagina's waarvan er zeven nul verkeer
halen is geen argument voor een tiende. De thuisbasis-pagina (`vloerverwarming-zuidlaren.html`) is
de dunste van allemaal — die versterken levert meer op.

---

## Dekkingsmatrix stadspagina's en kernpagina's

Legenda: ✅ aanwezig/in orde · ❌ ontbreekt/te lang · ⚠️ deels

| Pagina | FAQPage | Breadcrumb | LocalBusiness/Service | title <60 | desc <160 | H1 | link naar prijsindicatie | kruislinks |
|---|---|---|---|---|---|---|---|---|
| `vloerverwarming-assen.html` | ✅ | ✅ | ✅ Service | ❌ 61 | ✅ 157 | ✅ | ✅ | ✅ |
| `vloerverwarming-drachten.html` | ❌ | ✅ | ✅ Service | ❌ 64 | ❌ 172 | ✅ | ✅ | ✅ |
| `vloerverwarming-drenthe.html` | ❌ | ✅ | ✅ Service | ❌ 62 | ⚠️ 160 | ✅ | ✅ | ✅ |
| `vloerverwarming-emmen.html` | ✅ | ✅ | ✅ Service | ❌ 61 | ❌ 166 | ✅ | ✅ | ✅ |
| `vloerverwarming-groningen.html` | ✅ | ✅ | ✅ Service | ❌ 65 | ✅ 158 | ✅ | ✅ | ✅ |
| `vloerverwarming-heerenveen.html` | ✅ | ✅ | ✅ Service | ❌ 66 | ❌ 197 | ✅ | ✅ | ✅ |
| `vloerverwarming-hoogeveen.html` | ✅ | ✅ | ✅ Service | ❌ 65 | ❌ 166 | ✅ | ✅ | ✅ |
| `vloerverwarming-leeuwarden.html` | ✅ | ✅ | ✅ Service | ❌ 66 | ❌ 173 | ✅ | ✅ | ✅ |
| `vloerverwarming-zuidlaren.html` | ❌ | ✅ | ✅ Service | ❌ 64 | ⚠️ 160 | ✅ | ✅ | ✅ |
| `prijsindicatie.html` | ❌ | ❌ | ❌ | ❌ 76 | ✅ 152 | ✅ | n.v.t. | ✅ |
| `index.html` | ✅ | n.v.t. | ✅ LocalBusiness | ❌ 61 | ✅ 135 | ✅ | ✅ | ✅ |
| `faq.html` | ⚠️ 14 van 15 | ❌ | ❌ | ✅ 60 | ❌ 186 | ✅ | ✅ | ✅ |
| `diensten.html` | ❌ | ❌ | ❌ | ✅ 56 | ❌ 205 | ✅ | ✅ | ✅ |
| `systemen-producten.html` | ✅ | ❌ | ❌ | ✅ 56 | ✅ | ✅ | ✅ | ✅ |
| `werkwijze.html` | ❌ | ❌ | ❌ | ✅ 58 | ✅ | ✅ | ✅ | ✅ |
| `over-ons.html` | ❌ | ❌ | ❌ | ✅ 57 | ✅ | ✅ | ✅ | ✅ |
| `projecten.html` | ❌ | ❌ | ❌ | ✅ 49 | ✅ | ✅ | ✅ | ✅ |
| `contact.html` | ❌ | ❌ | ❌ | ✅ 48 | ✅ | ✅ | ✅ | ✅ |

**Wat opvalt:**

- De negen stadspagina's zijn qua schema in orde op drie gaten na: FAQ ontbreekt op Drachten,
  Drenthe en Zuidlaren. Die stonden al als `[WACHT]` in sprint 24 — terecht, cadans één per cyclus.
- `prijsindicatie.html` heeft **geen enkele** JSON-LD. Geen breadcrumb, geen FAQ, geen Service.
  Dat is de enige pagina met groei en de langste engagement (112 s / 30d, 135 s / 90d).
- `google-site-verification` staat op alle 20 pagina's op `REPLACE_WITH_TOKEN`. Dat schaadt
  niets, maar het is dode code tot de eigenaar een echt token levert (escalatie 2).

---

## Onvolkomenheden gevonden tijdens de audit

### 1. `faq.html` — één zichtbare vraag ontbreekt in het schema

Zichtbaar op de pagina staan 15 vragen. In de `FAQPage`-JSON-LD staan er 14. De ontbrekende:
**"Wat is droge vloerverwarming of laagopbouw?"** — positie 3 op de pagina, tussen schuimbeton en
houten vloer. Dat is precies de vraag met de dunste concurrentie in Noord-Nederland, en de vraag
die aansluit op `systemen-producten.html#laagopbouw`.

### 2. `index.html` — grammaticafout in een zichtbare FAQ-vraag én in het schema

"Welke garantie **horen** bij jullie systemen?" moet "hoort" zijn. De fout staat zowel in de
zichtbare knop als woordelijk in de JSON-LD, dus hij kan in een rich result terechtkomen.

### 3. `vloerverwarming-zuidlaren.html` — twee tekstfouten

- "We werken vooral voor particuliere **kopwoningen**" → moet "koopwoningen" zijn.
- "leggen de buis in en **stomen** of egaliseren we dicht" → moet "storten" zijn; "stomen" is hier
  geen bestaande handeling.

### 4. Zeven stadspagina's delen woordelijk dezelfde `alt`-tekst

`alt="Vloerverwarmingsbuis strak op wapeningsnet, klaar voor dekvloer"` staat identiek op Assen,
Drachten, Drenthe, Emmen, Heerenveen, Hoogeveen en Leeuwarden. Gemiste lokale afbeeldings-SEO en
onnodige herhaling.

### 5. `sitemap.xml` — `lastmod` loopt achter

`index.html`, `diensten.html`, `prijsindicatie.html`, `vloerverwarming-drachten.html`,
`vloerverwarming-heerenveen.html` en `vloerverwarming-leeuwarden.html` zijn op 11 augustus
gewijzigd, maar de sitemap noemt data tussen 29 juni en 13 juli. Assen, Emmen, Hoogeveen en
Zuidlaren zijn op 20 juli gewijzigd, sitemap zegt 13 juli.

Verder is de sitemap compleet: alle 20 indexeerbare pagina's staan erin, `404.html` en
`logo-varianten.html` terecht niet (beide hebben `noindex, follow`). `robots.txt` is in orde en
verwijst naar de juiste sitemap-URL.

### 6. `prijsindicatie.html` — negen `<h2>`'s zijn wizard-stappen, geen inhoud

De koppen "Waar wil je een prijs voor?", "Hoeveel vierkante meter vloerverwarming?" enzovoort zijn
UI-labels die als `<h2>` in de DOM staan. De enige inhoudelijke `<h2>` — "Kosten vloerverwarming —
wat is realistisch?" — is nummer negen. Dat verdunt het onderwerpsignaal. De wizard herbouwen is
niet nodig en niet verstandig; wel kan het kosten-blok beter vindbaar gemaakt worden vanaf boven.

### 7. Het ATF-blok op `prijsindicatie.html` linkt naar de verkeerde stad

Het introblok uit sprint 24 verwijst als regiovoorbeeld naar `vloerverwarming-heerenveen.html`.
Heerenveen is de verste stad in het werkgebied en haalt nul verkeer. Assen of Groningen past beter
bij waar de klanten vandaan komen.

---

## Interne linkstructuur

**Geen wezen.** Elke pagina in de root linkt via het footer-werkgebiedblok naar alle negen
stadspagina's. Ook `privacy.html` en `disclaimer.html` doen dat. Er is dus geen pagina die
onbereikbaar is vanaf een andere pagina.

**Maar de structuur is volledig vlak.** Omdat iedere pagina naar iedere stadspagina linkt, krijgt
geen enkele stadspagina meer intern gewicht dan een andere. Emmen en Assen — de twee grootste
markten na Groningen — staan op dezelfde voet als Leeuwarden, dat 55 minuten rijden is en nul
verkeer haalt.

**`prijsindicatie.html` is goed gelinkt**, niet ondergelinkt: hij staat in de hoofdnavigatie én de
footer van elke pagina, en krijgt daarnaast 2 tot 8 contextuele links per pagina (homepage 8,
faq.html 8, systemen-producten 6, werkwijze 5). Het probleem van die pagina is dus niet interne
linkkracht — het is dat hij extern onvindbaar is op de termen waar mensen op zoeken.

**Concrete aanbeveling voor linkstructuur:** niets slopen. De footer-lijst mag blijven. Waar winst
zit, is in contextuele links vanuit de tekst naar de kernregio (Assen, Groningen, Emmen,
Hoogeveen, Zuidlaren) in plaats van de Friese trio, en in het kosten-blok als bestemming
(`prijsindicatie.html#kosten-uitleg`) in plaats van alleen de wizard-top.

---

## Duplicate en thin content

Het risico is er, maar het is kleiner dan verwacht. Steekproeven op gedeelde zinnen:

| Zin | Komt voor op |
|---|---|
| "Onze klanten kiezen voor kwaliteit boven prijs, en daar leveren we op." | Assen, Emmen |
| "Geen onderaannemer met een ander telefoonnummer" | Assen, Drenthe |
| "In beide gevallen krijg je één plan, één aanspreekpunt en één planning" | Assen, Drenthe |
| "Het scheelt sloopwerk, scheelt afvalafvoer" | alleen Assen |

Twee pagina's die een zin delen is geen duplicate-content-probleem. De teksten zijn per stad echt
anders ingekleurd (Marsdijk/Kloosterveen/Pittelo bij Assen, De Drait/Smallingerland bij Drachten).
Dat is goed werk.

**Wat wél opvalt is dunheid, niet duplicatie.** Bestandsgrootte als ruwe proxy:

| Pagina | Grootte | Beoordeling |
|---|---|---|
| `vloerverwarming-groningen.html` | 21 kB | rijkst — 3 inhoudelijke H2's + FAQ |
| `vloerverwarming-emmen.html` | 21 kB | in orde |
| `vloerverwarming-assen.html` | 20 kB | referentiesjabloon |
| `vloerverwarming-hoogeveen.html` | 20 kB | in orde |
| `vloerverwarming-heerenveen.html` | 20 kB | in orde |
| `vloerverwarming-leeuwarden.html` | 19 kB | in orde |
| `vloerverwarming-drachten.html` | 17 kB | dun — 2 korte alinea's per sectie, geen FAQ |
| `vloerverwarming-drenthe.html` | 16 kB | dun voor een provinciehub |
| `vloerverwarming-zuidlaren.html` | 16 kB | **dunste — en dit is de thuisbasis** |

Zuidlaren heeft bovendien als enige stadspagina **geen enkele projectfoto** (alleen het logo) en
geen FAQ-sectie. Terwijl "vloerverwarming Zuidlaren" de term is waar dit bedrijf per definitie
nummer één op hoort te staan, en waar het zwaartepunt van het werkgebied ligt.

---

## Top zoekwoorden en intentiedekking

Volumes zijn indicatief — zonder GSC en zonder betaalde tools is dit een inschatting op
domeinkennis van de Noord-Nederlandse markt, geen meting.

| Zoekterm / intentie | Volume (indicatie) | Concurrentie | Huidige landing | Oordeel |
|---|---|---|---|---|
| wat kost vloerverwarming per m2 | hoog | midden | `prijsindicatie.html#kosten-uitleg` | **content aanwezig, metadata mist** |
| vloerverwarming kosten | hoog | hoog | geen gerichte titel | gat |
| vloerverwarming infrezen | midden | laag | 8 stadspagina's + faq | goed gedekt |
| vloerverwarming warmtepomp | hoog | midden | alleen FAQ-antwoord | **gat — geen H2, geen sectie** |
| droge vloerverwarming / laagopbouw | midden | **laag** | `systemen-producten.html` | goed, maar schema-gat in faq |
| vloerverwarming installateur Groningen | midden | midden | `vloerverwarming-groningen.html` | gedekt |
| vloerverwarming Assen / Emmen / Hoogeveen | laag–midden | laag | eigen pagina's | gedekt |
| vloerverwarming Haren / Eelde / Tynaarlo | laag | **zeer laag** | alleen genoemd in lopende tekst | gat, hoge koopkracht |
| vloerverwarming nieuwbouw | midden | hoog | H2 op 4 stadspagina's | voldoende |
| vloerverwarming bestaande vloer | midden | midden | infrees-secties | voldoende |
| schuimbeton kruipruimte | laag | **zeer laag** | `diensten.html#schuimbeton` | gedekt, sterk onderscheidend |

**De grootste onbediende commerciële intentie is de warmtepomp-combinatie.** `warmtepomp` komt 9×
voor op `faq.html`, 5× op `systemen-producten.html`, 3× op de homepage — en **0× op
`prijsindicatie.html`**. Er is nergens een `<h2>` die dit onderwerp claimt. Bij deze doelgroep
(koopwoning, bovenmodaal, 35–60, bezig met verduurzamen) is "past vloerverwarming bij mijn
warmtepomp" vaak de eerste vraag, niet de derde.

**De tweede is de corridor Haren – Glimmen – Eelde-Paterswolde – Vries – Tynaarlo – Yde – De
Punt.** Dat is een kwartier rijden vanaf de Verlengde Stationsweg, het is de meest koopkrachtige
strook van het hele werkgebied, en de concurrentie op die plaatsnamen is verwaarloosbaar. Nu
worden alleen "Tynaarlo, Paterswolde, Bunne, Zuidwolde en Gieten" in één zin op de
Zuidlaren-pagina genoemd. Haren, Glimmen, Eelde, Vries, Yde en De Punt komen nergens voor.

Geen aparte pagina bouwen: die namen horen in de Zuidlaren-pagina, want dat is geografisch waar.
"Zuidwolde" kan er trouwens uit — dat ligt bij Hoogeveen of boven Groningen, niet naast Zuidlaren.

---

## Seizoen

Vloerverwarming heeft twee pieken: **augustus tot november** (mensen willen het voor de winter
klaar hebben, en het bouwseizoen loopt) en **januari–februari** (koude woning, koude vloer,
verbouwplannen voor het voorjaar). We zitten nu aan het begin van de sterkste periode van het
jaar. Als er één moment is waarop de kosten- en warmtepompcontent op orde moet zijn, is het de
komende zes weken.

---

## Genummerde taken voor de Developer Agent

Alle zeven zijn puur HTML/CSS-edits in deze repo, geen build, geen nieuwe pagina's.

### 1. `prijsindicatie.html` — metadata op kosten richten en structured data toevoegen

**Bestand:** `prijsindicatie.html`

**Wat:**

a) Vervang `<title>`, `og:title` en `twitter:title` (nu 76 tekens, targetet niemand):

```
Wat kost vloerverwarming per m²? Prijsindicatie Drenthe
```

b) Voeg in de `<head>` twee `<script type="application/ld+json">`-blokken toe. Eerst breadcrumbs:

```json
{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Home","item":"https://www.vlwarmte.nl/"},{"@type":"ListItem","position":2,"name":"Prijsindicatie vloerverwarming","item":"https://www.vlwarmte.nl/prijsindicatie.html"}]}
```

c) Voeg **onderaan de bestaande sectie `#kosten-uitleg`**, vóór de `<p class="small">`-disclaimer,
een zichtbare FAQ-accordeon toe volgens het patroon van `vloerverwarming-assen.html` (regels
227–234: `<div class="faq-item"><button class="faq-question" data-faq-toggle>…</button><div
class="faq-answer"><p>…</p></div></div>`), met deze drie Q&A's — daarna woordelijk spiegelen in
een `FAQPage`-JSON-LD in de `<head>`:

> **Wat kost vloerverwarming per m²?**
> Voor alleen vloerverwarming op een bestaande betonvloer zit je meestal tussen €45 en €95 per m²,
> inclusief arbeid en materiaal, exclusief btw. Nieuwbouw met een schone ondergrond zit aan de
> onderkant van die band; renovatie waar we moeten infrezen zit aan de bovenkant. De wizard op deze
> pagina geeft je in twee minuten een bandbreedte voor jouw situatie.

> **Waarom is de prijs per m² lager bij een grotere vloer?**
> Opstartkosten zijn er altijd: verdeler, aanvoer, opname en inregelen. Bij meer dan ongeveer
> 40 m² verdelen die zich over meer vierkante meters, dus daalt het tarief per m². Zit je eronder,
> dan zie je ze duidelijk terug in de prijs.

> **Betaal ik voorrijkosten in Drenthe, Groningen of Friesland?**
> Voor een opname binnen 50 km van Zuidlaren — Assen, Groningen, Hoogeveen, Roden, Veendam, Meppel
> en Drachten — rekenen we geen voorrijkosten apart; die zitten in de offerte. Voor Leeuwarden en
> Heerenveen kijken we per project; bij grotere oppervlakken valt dat in de praktijk weg in het
> tarief per m².

d) Voeg in het bestaande ATF-introblok (regel ~589) een tekstlink toe naar `#kosten-uitleg`, en
vervang de link naar Heerenveen door Assen:

> Wil je eerst weten waar die bandbreedte vandaan komt? Lees
> <a href="#kosten-uitleg">wat vloerverwarming per m² kost</a>. Meer over opbouw en systemen lees
> je bij <a href="systemen-producten.html#laagopbouw">laagopbouw en droge vloerverwarming</a>;
> voorbeelden uit de regio staan op <a href="vloerverwarming-assen.html">vloerverwarming Assen</a>.

**Waarom:** dit is de enige pagina met instroomgroei (2 → 4 sessies) en de langste engagement
(112 s). De inhoud die mensen zoeken staat er al — de bandbreedte, de drie prijsdrijvers, de
voorrijkosten — maar de `<title>` bevat het woord "kosten" niet, de H1 evenmin, en er is geen
enkele JSON-LD waarmee Google de kosteninformatie als antwoord kan tonen. Dit is de goedkoopste
hefboom op de site.

**Succescriterium:**
`grep -c '"FAQPage"' prijsindicatie.html` → 1 · `grep -c '"BreadcrumbList"' prijsindicatie.html` → 1 ·
`grep -c 'Wat kost vloerverwarming per m²' prijsindicatie.html` → ≥ 3 (title, og, zichtbare vraag) ·
`grep -c 'href="#kosten-uitleg"' prijsindicatie.html` → ≥ 1 ·
`grep -c 'vloerverwarming-heerenveen.html' prijsindicatie.html` → 0 ·
wizard-flow ongewijzigd, accordeon opent.

---

### 2. Alle `<title>`-tags onder 60 tekens brengen

**Bestanden:** de negen `vloerverwarming-*.html` + `index.html`

**Wat:** vervang `<title>`, `og:title` en `twitter:title` (alle drie per pagina — ze zijn nu
identiek) door:

| Bestand | Nieuwe title | Tekens |
|---|---|---|
| `vloerverwarming-assen.html` | `Vloerverwarming Assen — installateur uit Zuidlaren` | 50 |
| `vloerverwarming-drachten.html` | `Vloerverwarming Drachten — installateur uit Zuidlaren` | 53 |
| `vloerverwarming-drenthe.html` | `Vloerverwarming Drenthe — eigen ploeg uit Zuidlaren` | 51 |
| `vloerverwarming-emmen.html` | `Vloerverwarming Emmen — installateur uit Zuidlaren` | 50 |
| `vloerverwarming-groningen.html` | `Vloerverwarming Groningen — installateur uit Zuidlaren` | 54 |
| `vloerverwarming-heerenveen.html` | `Vloerverwarming Heerenveen — vakman uit Zuidlaren` | 49 |
| `vloerverwarming-hoogeveen.html` | `Vloerverwarming Hoogeveen — vakman uit Zuidlaren` | 48 |
| `vloerverwarming-leeuwarden.html` | `Vloerverwarming Leeuwarden — vakman uit Zuidlaren` | 49 |
| `vloerverwarming-zuidlaren.html` | `Vloerverwarming Zuidlaren — installateur in het dorp` | 52 |
| `index.html` | `Vloerverwarming Drenthe, Groningen en Friesland \| VLWarmte` | 58 |

**Waarom:** alle tien titles zitten nu tussen 61 en 66 tekens. Google kapt af rond 60; wat wegvalt
is precies het achtervoegsel `| VLWarmte` — de merknaam. Op de stadspagina's is dat achtervoegsel
overbodig omdat "Zuidlaren" al in de titel staat en het merk in de meta-description en de
breadcrumb terugkomt. Op de homepage blijft het merk staan, daar is ruimte.

**Succescriterium:** geen `<title>` in de tien genoemde bestanden is nog langer dan 60 tekens ·
`grep -c 'installateur uit Zuidlaren | VLWarmte' *.html` → 0 ·
per bestand geldt: `<title>`, `og:title` en `twitter:title` zijn onderling gelijk.

---

### 3. Meta-descriptions onder 160 tekens brengen

**Bestanden:** `vloerverwarming-drachten.html`, `vloerverwarming-heerenveen.html`,
`vloerverwarming-leeuwarden.html`, `vloerverwarming-emmen.html`, `vloerverwarming-hoogeveen.html`,
`faq.html`, `diensten.html`

**Wat:** vervang `<meta name="description">` én `og:description` én `twitter:description` per
bestand door onderstaande tekst (alle drie gelijk houden):

- **Drachten** (nu 172):
  `Vloerverwarming in Drachten — compleet van ondervloer tot oplevering. Eigen ploeg uit Zuidlaren, reactie binnen één werkdag. Vraag een prijsindicatie aan.`
- **Heerenveen** (nu 197):
  `Vloerverwarming in Heerenveen — compleet van ondervloer tot oplevering in Friesland. Eigen ploeg uit Zuidlaren. Vraag een prijsindicatie aan.`
- **Leeuwarden** (nu 173):
  `Vloerverwarming in Leeuwarden — compleet van ondervloer tot oplevering. Eigen ploeg uit Zuidlaren, reactie binnen één werkdag. Prijsindicatie aanvragen.`
- **Emmen** (nu 166):
  `Vloerverwarming in Emmen — compleet van ondervloer tot oplevering. Eigen ploeg uit Zuidlaren, een half uur rijden. Vraag een prijsindicatie aan.`
- **Hoogeveen** (nu 166):
  `Vloerverwarming in Hoogeveen, Hollandscheveld en Fluitenberg — van ondervloer tot oplevering. Eigen ploeg uit Zuidlaren, antwoord binnen één werkdag.`
- **faq.html** (nu 186):
  `Antwoorden over vloerverwarming: infrezen bij renovatie, warmtepomp, laagopbouw, schuimbeton en kosten per m². VLWarmte uit Zuidlaren.`
- **diensten.html** (nu 205):
  `Complete trajecten: ondervloer, schuimbeton, vloerverwarming, dekvloer en afwerking. VLWarmte uit Zuidlaren voor Drenthe, Groningen en Friesland.`

**Waarom:** een description boven 160 tekens wordt afgekapt of door Google vervangen door een
eigen snippet uit de pagina. Bij `diensten.html` (205) en `faq.html` (186) is dat vrijwel zeker.
Je verliest dan de controle over wat er in het zoekresultaat staat — inclusief de CTA.

**Succescriterium:** geen van de zeven bestanden heeft nog een `description`-, `og:description`-
of `twitter:description`-`content` langer dan 160 tekens · `grep -c 'Vrijblijvende prijsindicatie;
ook informatie of terugbelverzoek' diensten.html` → 0.

---

### 4. `faq.html` — schema-gat dichten en grammaticafout op `index.html` herstellen

**Bestanden:** `faq.html`, `index.html`

**Wat:**

a) In `faq.html` staat de zichtbare vraag **"Wat is droge vloerverwarming of laagopbouw?"** wel op
de pagina (derde accordeon) maar niet in de `FAQPage`-JSON-LD. Voeg hem toe op positie 3 in
`mainEntity`, met `name` en `acceptedAnswer.text` **woordelijk gelijk** aan de zichtbare tekst in
het bijbehorende `<div class="faq-answer">`.

b) In `index.html` staat tweemaal "Welke garantie **horen** bij jullie systemen?" — één keer in de
zichtbare `<button class="faq-question">` en één keer in de JSON-LD. Wijzig beide naar:

```
Welke garantie hoort bij jullie systemen?
```

**Waarom:** (a) Google negeert een `FAQPage` die niet overeenkomt met de zichtbare inhoud, maar
omgekeerd loop je hier gewoon een kans mis: "droge vloerverwarming" en "laagopbouw" zijn de
zoektermen met de laagste concurrentie in dit vak, en de site heeft er goede content over.
(b) De grammaticafout staat in het schema, dus hij kan letterlijk in een zoekresultaat verschijnen.
Dat past niet bij een bedrijf dat het van vakwerk moet hebben.

**Succescriterium:** `grep -c '"name":"Wat is droge vloerverwarming of laagopbouw?"' faq.html` → 1 ·
het aantal `"@type":"Question"` in `faq.html` is 15 en gelijk aan het aantal
`class="faq-question"`-knoppen · `grep -c 'Welke garantie horen' index.html` → 0 ·
`grep -c 'Welke garantie hoort' index.html` → 2.

---

### 5. `vloerverwarming-zuidlaren.html` — FAQ, buurdorpen en twee tekstfouten

**Bestand:** `vloerverwarming-zuidlaren.html`

**Wat:**

a) Herstel twee fouten:
- `particuliere kopwoningen` → `particuliere koopwoningen`
- `leggen de buis in en stomen of egaliseren we dicht` → `leggen de buis in en storten of egaliseren we dicht`

b) Vervang in de `<p class="lead">` in de hero de opsomming
`Tynaarlo, Paterswolde, Bunne, Zuidwolde en Gieten` door:

> Haren, Glimmen, Eelde-Paterswolde, Vries, Tynaarlo, Yde en De Punt

(Zuidwolde eruit — dat ligt niet naast Zuidlaren.)

c) Voeg **na** het "Ook actief in"-blok en **vóór** de CTA-sectie een FAQ-sectie toe volgens het
Assen-sjabloon (`vloerverwarming-assen.html`, regels 222–234), plus een spiegelend
`FAQPage`-JSON-LD in de `<head>` na het bestaande `BreadcrumbList`-script:

> **Werken jullie ook in Haren, Eelde-Paterswolde, Glimmen en Vries?**
> Ja. Dat is onze directe achtertuin. Vanaf de Verlengde Stationsweg sta je binnen een kwartier in
> Haren, Glimmen, Eelde-Paterswolde, Vries, Tynaarlo, Yde of De Punt. Voor een opname rijden we
> daar zonder voorrijkosten heen.

> **Wat kost vloerverwarming in Zuidlaren en omgeving?**
> Dat hangt af van het oppervlak, de ondergrond en of we in een bestaande vloer frezen of in
> nieuwbouw leggen. Loop de <a href="prijsindicatie.html">prijsindicatie</a> door voor een
> richtbedrag; de vaste prijs volgt na een opname bij je thuis.

> **Kunnen jullie infrezen in een woning uit de jaren zestig of zeventig?**
> Meestal wel. We meten eerst vlakheid, draagkracht en hechting van de bestaande dekvloer. Kan het
> veilig, dan frezen we sleuven en leggen we de buis daarin — geen sloop, geen extra vloerhoogte.
> Voldoet de ondergrond niet, dan zeggen we dat vooraf en stellen we een andere opbouw voor.

**Waarom:** dit is de thuisbasis-pagina en tegelijk de dunste van de negen (16 kB, geen FAQ, geen
projectfoto). De corridor Haren – Glimmen – Eelde – Vries is de meest koopkrachtige strook in het
hele werkgebied, ligt op een kwartier rijden en heeft nauwelijks lokale concurrentie op deze term.
Die plaatsnamen komen nu nergens op de site voor. Dit is de goedkoopste manier om ze te dekken —
zonder een tiende stadspagina te bouwen die daarna weer onderhouden moet worden.

**Succescriterium:** `grep -c '"FAQPage"' vloerverwarming-zuidlaren.html` → 1 ·
`grep -c 'Haren' vloerverwarming-zuidlaren.html` → ≥ 2 ·
`grep -c 'kopwoningen\|stomen of egaliseren' vloerverwarming-zuidlaren.html` → 0 ·
zichtbare vraagteksten matchen de JSON-LD 1-op-1 · accordeon werkt.

---

### 6. Sectie "Vloerverwarming en een warmtepomp" op `prijsindicatie.html`

**Bestanden:** `prijsindicatie.html`, `diensten.html`

**Wat:** voeg op `prijsindicatie.html` **na** de sectie `#kosten-uitleg` een nieuwe sectie toe met
`id="warmtepomp"`, in hetzelfde patroon (`<section class="section" id="warmtepomp"><div
class="container" style="max-width: 760px;">`):

> ## Vloerverwarming en een warmtepomp
>
> Vloerverwarming draait op een lage aanvoertemperatuur — meestal 30 tot 40 graden. Dat is precies
> waar een warmtepomp zijn rendement haalt; met radiatoren op 70 graden lukt dat niet. Combineer je
> de twee, dan leggen we de buizen dichter op elkaar — hart op hart 10 of 15 centimeter in plaats
> van 20 — zodat je bij die lage temperatuur genoeg vermogen in de ruimte krijgt.
>
> Heb je nu nog een cv-ketel maar wil je later overstappen? Zeg dat bij de opname. Dan leggen we
> het systeem meteen warmtepomp-klaar aan. Dat kost op dit moment weinig extra en scheelt je later
> een tweede keer de vloer open.
>
> In de wizard hierboven zit die keuze niet apart verwerkt. Bel even of
> <a href="contact.html?modus=informatie#aanvraag">stel je vraag</a> — dan rekenen we het mee. Meer
> over de opbouw lees je bij
> <a href="systemen-producten.html#laagopbouw">laagopbouw en droge vloerverwarming</a>.

Voeg daarnaast in `diensten.html`, in de sectie "Vloerverwarming aanleg", één contextuele zin met
link toe:

> Werk je met een warmtepomp of overweeg je die later? Lees hoe we het leidingwerk daarop afstemmen
> bij <a href="prijsindicatie.html#warmtepomp">vloerverwarming en een warmtepomp</a>.

**Waarom:** "vloerverwarming warmtepomp" is een van de zoekintenties met het meeste volume in dit
vak, en de site heeft er geen enkele `<h2>` voor — alleen FAQ-antwoorden van drie regels. Op
`prijsindicatie.html` komt het woord "warmtepomp" nul keer voor, terwijl juist iemand die een
warmtepomp overweegt de kostenvraag stelt. De doelgroep (koopwoning, bovenmodaal, bezig met
verduurzamen) stelt deze vraag vroeg in het traject.

**Succescriterium:** `grep -c 'id="warmtepomp"' prijsindicatie.html` → 1 ·
`grep -c 'warmtepomp' prijsindicatie.html` → ≥ 5 ·
`grep -c 'prijsindicatie.html#warmtepomp' diensten.html` → 1 ·
wizard-flow en `#kosten-uitleg` ongewijzigd.

---

### 7. `sitemap.xml` bijwerken en `alt`-teksten uniek maken

**Bestanden:** `sitemap.xml` + de zeven stadspagina's met identieke `alt`

**Wat:**

a) Actualiseer `<lastmod>` naar de echte laatste wijzigingsdatum:

| URL | Nu | Wordt |
|---|---|---|
| `/` | 2026-06-29 | 2026-08-11 |
| `/diensten.html` | 2026-06-29 | 2026-07-06 |
| `/prijsindicatie.html` | 2026-06-29 | 2026-08-11 |
| `/vloerverwarming-drachten.html` | 2026-07-06 | 2026-08-11 |
| `/vloerverwarming-heerenveen.html` | 2026-07-01 | 2026-08-11 |
| `/vloerverwarming-leeuwarden.html` | 2026-07-13 | 2026-08-11 |
| `/vloerverwarming-assen.html` | 2026-07-13 | 2026-07-20 |
| `/vloerverwarming-emmen.html` | 2026-07-13 | 2026-07-20 |
| `/vloerverwarming-hoogeveen.html` | 2026-07-13 | 2026-07-20 |
| `/vloerverwarming-zuidlaren.html` | 2026-07-13 | 2026-07-20 |

Werk daarnaast de datums bij van elke pagina die in taken 1 t/m 6 wordt aangeraakt, naar de dag
van implementatie.

b) Vervang de zeven identieke `alt`-teksten
(`alt="Vloerverwarmingsbuis strak op wapeningsnet, klaar voor dekvloer"`) door:

| Bestand | Nieuwe alt |
|---|---|
| `vloerverwarming-assen.html` | `Vloerverwarmingsbuis gelegd in een woning in Assen, klaar voor de dekvloer` |
| `vloerverwarming-drachten.html` | `Vloerverwarmingsbuis op wapeningsnet in een woning in Drachten` |
| `vloerverwarming-drenthe.html` | `Vloerverwarmingsbuis strak gelegd in een Drentse woning, klaar voor de dekvloer` |
| `vloerverwarming-emmen.html` | `Vloerverwarmingsbuis op wapeningsnet in een woning in Emmen` |
| `vloerverwarming-heerenveen.html` | `Vloerverwarmingsbuis gelegd in een woning in Heerenveen, klaar voor de dekvloer` |
| `vloerverwarming-hoogeveen.html` | `Vloerverwarmingsbuis op wapeningsnet in een woning in Hoogeveen` |
| `vloerverwarming-leeuwarden.html` | `Vloerverwarmingsbuis gelegd in een woning in Leeuwarden, klaar voor de dekvloer` |

**Waarom:** een `lastmod` die maanden achterloopt op de echte wijziging is een signaal dat Google
kan gebruiken om minder vaak te crawlen. Bij een site van 20 pagina's met weinig autoriteit telt
dat. De identieke `alt`-tekst op zeven pagina's is een gemiste kans voor lokale
afbeeldingsresultaten en versterkt het beeld van gesjabloneerde pagina's.

**Succescriterium:** `grep -c '2026-06-29' sitemap.xml` → 0 ·
`grep -c 'Vloerverwarmingsbuis strak op wapeningsnet, klaar voor dekvloer' *.html` → 0 ·
elke stadspagina heeft een `alt` waarin de eigen plaatsnaam voorkomt.

---

## Bewust niet gedaan deze cyclus

- **Geen nieuwe pagina.** Zeven van de negen stadspagina's halen nul verkeer. Een tiende erbij lost
  niets op en kost onderhoud. De Haren/Eelde-corridor gaat mee in taak 5.
- **FAQ op Drachten en Drenthe.** Staan al als `[WACHT]` in sprint 24; de cadans van één stad per
  cyclus is verstandig. Zuidlaren gaat voor, omdat dat de thuisbasis is en de dunste pagina.
- **De wizard-`<h2>`'s omzetten naar niet-koppen.** Technisch een verbetering voor het
  onderwerpsignaal, maar het raakt de JS en de toegankelijkheid van de wizard. Niet doen in een
  onbewaakte run. Taak 1d lost het grootste deel op met een ankerlink.
- **Homepage-hero.** Blijft af, conform sprint 24. Bij 17 sessies is 85% bounce geen betrouwbaar
  signaal.
- **`REPLACE_WITH_TOKEN` vervangen.** Wacht op een echt token van de eigenaar.

---

## Escalaties (eigenaar — geen developer-taak)

1. **Conversiemeting, zesde cyclus met 0 conversies.** `wizard_lead_submit`, `lead_form_submit` en
   `contact_submit` zijn niet als key event gemarkeerd in GA4. Met 112 s engagement op
   `prijsindicatie.html` is een meetfout waarschijnlijker dan een lege trechter. Controleer ook de
   Formspree-inboxen `xzdojzdk` en `xgodnvoq`. Zonder dit is elke uitspraak over conversie giswerk.
2. **GSC OAuth, `invalid_grant`, inmiddels 10+ weken.** Draai
   `python scripts/gsc_get_refresh_token.py` met een geverifieerd owner-account. Zolang dit staat,
   is al het SEO-werk in dit rapport blind — we weten niet welke termen impressies opleveren.
3. **Google Ads-account staat `CLOSED`.** Heropenen en betaalmethode koppelen op ads.google.com →
   Billing, auto-tagging aanzetten. Zolang het account gesloten is, verklaart dat de nul impressies
   volledig; de landingspagina's zijn niet de oorzaak.
4. **Beeldmateriaal.** `vloerverwarming-zuidlaren.html` heeft geen enkele projectfoto en
   `projecten.html` toont twee projecten. Een handvol nieuwe foto's uit de regio — Haren, Eelde,
   Assen — helpt zowel de stadspagina's als social meer dan welke schema-ingreep ook.

---

## Aanbeveling aan de Product Manager

| # | Taak | Prioriteit | Type | Autonoom uitvoerbaar |
|---|---|---|---|---|
| 1 | `prijsindicatie.html`: kosten-title + FAQ + breadcrumbs | **Hoog** | SEO + structured data | ja |
| 2 | Titles onder 60 tekens (10 pagina's) | **Hoog** | Metadata | ja |
| 4 | `faq.html` schema-gat + `index.html` typo | **Hoog** | Structured data + kwaliteit | ja |
| 6 | Warmtepomp-sectie | Midden | Content gap | ja |
| 5 | Zuidlaren: FAQ + buurdorpen + typo's | Midden | SEO + content | ja |
| 3 | Descriptions onder 160 tekens (7 pagina's) | Midden | Metadata | ja |
| 7 | Sitemap `lastmod` + unieke alt-teksten | Laag | Hygiëne | ja |

Als er maar tijd is voor de helft: doe 1, 2 en 4. Dat zijn de drie waar iets kapot of ongebruikt
is, niet waar iets ontbreekt.

En één nuchtere kanttekening tot slot: geen van deze zeven taken gaat bij vier organische sessies
per maand meteen leads opleveren. Ze zorgen ervoor dat de site klopt op het moment dat er wél
instroom komt — via een heropend Ads-account, via herstelde GSC-meting, of via het bouwseizoen dat
nu begint. De echte blokkade zit in de drie escalaties hierboven, niet in de HTML.
