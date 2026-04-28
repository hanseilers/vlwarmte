# Marketing Research Rapport — 27 april 2026

> Vorige iteratie (26 april 2026) bevatte een brede contentinventarisatie inclusief het haalbaarheidsonderzoek prijscalculator. Die calculator staat inmiddels live op `prijsindicatie.html` (4 stappen, slider, lead-gate, Formspree). Deze update verdiept de vier focusvragen van deze week: stedelijke landingspagina's, long-tail kansen, content gaps en concurrentie. Conclusies en aanbevelingen uit de vorige ronde die nog open staan, blijven geldig en zijn hieronder samengevat.

---

## GA4-koppeling — 28 april 2026

_(Bron: `docs/website-manager/ga4_report.json`, laatste fetch.)_

- **Volume:** klein (~13 sessies in de meest recente week in de export). Marketingconclusies blijven dus **strategisch** (SEO, FAQ, distributie), niet “pagina X heeft bewezen…”
- **Kanaal:** vrijwel alleen **Direct** — er is nog **geen zichtbaar organisch** kanaal in de data. Dat onderstreept: **FAQ + Search Console + interne links + social/LinkedIn** zijn de hefbomen om niet alleen op merkherkenning te leunen.
- **Homepage:** verkeer splitst tussen **`/`** en **`index.html`** — marketing én SEO profiteren van **één duidelijke canonieke URL** in communicatie (visitekaartje, e-mailhandtekening, social bio) en van de technische fix die de analytics-agent voorstelt.
- **Prijsindicatie:** meerdere sessies met **langere tijd op pagina** — de calculator verdient **prominente CTAs** op site en in social (niet alleen “link in bio” generiek).
- **Regio in data:** Drenthe en Groningen komen voor; ook **VS-sessies** — bij campagnes en uitleg richting “lokaal Noord-Nederland” segment in GA4 of filter gebruiken zodat contentbeslissingen niet op bots buiten de markt gebaseerd worden.

De **ranglijst steden, long-tail-tabel en aanbevelingen 1–8** hieronder blijven leidend; bovenstaande data **versterkt** vooral de urgentie van FAQ, canonical/redirect en meetbare conversie-instelling.

---

## Samenvatting

De grootste resterende kans voor vlwarmte.nl is een dunne maar gerichte stedelijke laag: niet alle steden tegelijk, maar twee landingspagina's waar de combinatie van zoekvolume, koopkracht en relatief lage concurrentie het hoogst is — Groningen stad en Assen. Daarnaast liggen er drie long-tail clusters waar VLWarmte met weinig moeite snel kan ranken (infrezen + plaatsnaam, schuimbeton, "vloerverwarming bij houten vloer"). De huidige prijscalculator is sterk maar mist twee dingen die meetbaarheid en conversie helpen: een tracking-event op berekening voltooid en een mini-proof in het resultaatblok. Aanbevelingen zijn beperkt tot 8, gesorteerd op verwacht effect per uur werk.

---

## 1. Stedelijke landingspagina's — waar zit de hoogste ROI?

### Beoordelingscriteria

Per stad gewogen op zoekvolume, koopkracht doelgroep, concurrentiedruk en reistijd vanuit Zuidlaren.

### Ranglijst werkgebied

| Stad                  | Zoekvolume  | Koopkracht                         | Concurrentie | Reistijd  | Score  | Aanbeveling                        |
| --------------------- | ----------- | ---------------------------------- | ------------ | --------- | ------ | ---------------------------------- |
| Groningen stad        | hoog        | hoog (Helpman, Haren, Paterswolde) | hoog         | 15 min    | 8.5/10 | Bouwen — prio 1                    |
| Assen                 | midden-hoog | hoog (Marsdijk, Assen-Oost)        | midden-hoog  | 20 min    | 7.5/10 | Bouwen — prio 2                    |
| Haren / Paterswolde   | laag-midden | zeer hoog                          | laag         | 10 min    | 6.5/10 | Sub-sectie binnen Groningen-pagina |
| Roden / Leek          | laag        | hoog                               | laag         | 25 min    | 5.5/10 | Wachten                            |
| Emmen                 | midden      | midden                             | midden-hoog  | 50 min    | 5.0/10 | Buiten kerngebied                  |
| Hoogeveen / Meppel    | laag        | midden                             | laag         | 45-60 min | 4.5/10 | Buiten 50 km feitelijk             |
| Veendam / Stadskanaal | laag        | midden                             | laag         | 35 min    | 4.5/10 | Wachten                            |

### Conclusie focus deze week

**Maak twee stedelijke pagina's: Groningen en Assen.** Niet meer.

Reden: kwaliteit boven kwantiteit. Tien dunne locatiepagina's (de ComfortFloors-aanpak) leveren weinig op zonder lokale signalen — Google straft "doorways" af. Twee pagina's met écht lokale inhoud (referentieproject in die stad, reistijd, lokale plaatsnamen) wegen zwaarder. Voor de overige plaatsen is het beter om binnen die twee pagina's de omliggende dorpen te benoemen.

**Wat een goede landingspagina nodig heeft:**

- H1: "Vloerverwarming Groningen — installateur uit Zuidlaren" (variant voor Assen)
- 1 alinea waarom een installateur uit Zuidlaren snel in Groningen is (15 min reistijd expliciet)
- 1 lokaal referentieproject met foto en plaatsnaam
- Lijstje omliggende plaatsen
- Korte uitleg systeemkeuze nieuwbouw vs renovatie (geen duplicaat)
- Drie stadsspecifieke FAQ's
- CTA-blok met telefoon, formulier en link naar prijscalculator
- Schema.org `LocalBusiness` met correcte `areaServed`

---

## 2. Long-tail zoekwoorden waar VLWarmte snel kan ranken

| Zoekterm                                 | Volume      | Concurrentie | Pagina-strategie             | Effort   |
| ---------------------------------------- | ----------- | ------------ | ---------------------------- | -------- |
| vloerverwarming infrezen Groningen       | midden      | midden       | H2 binnen Groningen-pagina   | klein    |
| vloerverwarming infrezen Drenthe         | midden      | midden       | H2 binnen Assen-pagina       | klein    |
| vloerverwarming op houten vloer          | midden      | laag         | FAQ-item + sectie renovatie  | klein    |
| schuimbeton vloerverwarming Groningen    | laag-midden | zeer laag    | H2 binnen schuimbeton-sectie | klein    |
| vloerverwarming Drenthe kosten           | laag-midden | laag         | Anker binnen prijsindicatie  | minimaal |
| vloerverwarming bij verbouwing           | midden      | midden       | Renovatie-sectie             | midden   |
| vloerverwarming aansluiten op cv-ketel   | midden      | laag         | FAQ-item                     | minimaal |
| vloerverwarming en warmtepomp combineren | midden      | midden       | FAQ-item + 1 alinea systemen | minimaal |
| ondervloer dekvloer vloerverwarming      | laag        | zeer laag    | H2 op diensten-pagina        | minimaal |

**Patroon:** de meest haalbare long-tail termen zijn vraag-gericht en kunnen voor een groot deel worden afgevangen met één **FAQ-pagina van 12–15 vragen** plus FAQ-schema voor rich snippets.

---

## 3. Content gaps

### Status bestaande pagina's

| Pagina                  | Status | Opmerking                                     |
| ----------------------- | ------ | --------------------------------------------- |
| index.html              | sterk  | Hero, USP's, FAQ-snippets, schema             |
| diensten.html           | sterk  | Per dienst een blok                           |
| werkwijze.html          | sterk  | 6 stappen helder                              |
| systemen-producten.html | sterk  | Garantie staat hier al                        |
| projecten.html          | dun    | Mist concrete projecten met foto + plaatsnaam |
| over-ons.html           | sterk  | Persoonlijk, lokaal verankerd                 |
| contact.html            | sterk  | Inclusief terugbelverzoek                     |
| prijsindicatie.html     | sterk  | Wizard live, lead-gate werkt                  |

### Resterende gaps (gesorteerd op urgentie)

1. **Volwaardige FAQ-pagina** — index.html heeft 3 FAQ-items als snippet, maar geen aparte pagina met 12–15 vragen. Grootste gemiste kans voor long-tail SEO.
2. **Renovatie vs nieuwbouw — beslisuitleg** — de wizard vraagt het, maar er is geen uitlegpagina.
3. **Stedelijke landingspagina's** — Groningen + Assen.
4. **Schuimbeton — eigen ankersectie** — wordt genoemd maar krijgt geen eigen anker. Een H2 met `#schuimbeton` is voldoende.
5. **Projecten met locatie + foto** — projecten.html is dun.

### Niet (nog) nodig — bewust schrappen uit vorige research

- Aparte `kosten.html` — calculator dekt dit; binnen prijsindicatie.html kan een korte "Wat bepaalt de prijs?"-sectie het zoekwoord "wat kost vloerverwarming per m2" afvangen.
- Doelgroeppagina aannemers — blijft lage prioriteit.
- Aparte `vloerverwarming-infrezen.html` — beter geïntegreerd in Groningen/Assen-pagina's en FAQ.

---

## 4. Concurrentie-observaties (update)

### ComfortFloors (Hoogeveen)

Strategie: brede dekking via dunne locatiepagina's. Werkt voor merkbekendheid maar weinig diepgang per stad. **VLWarmte beter:** twee stadspagina's mét echte lokale inhoud, prijscalculator als onderscheider in elke CTA noemen.

### Drentse Vloerverwarming Specialist (Klazienaveen)

Strategie: gemeentepagina's per Drentse gemeente + blog. Beperkt review-volume. **VLWarmte beter:** binnen Drenthe (Assen) sneller op kwaliteit zitten + calculator-voorsprong.

### Kentech BV (Groningen-Assen)

Strategie: breed installatiebedrijf, vloerverwarming als bijproduct. **VLWarmte beter:** specialisatie expliciet maken op de Groningen-pagina ("alleen vloerverwarming, geen elektra of cv erbij").

### Lokale aannemers en vloerenleggers

Tientallen kleine spelers ranken zelden maar krijgen wel mond-tot-mond aanvragen. **VLWarmte concurreert hier op vertrouwen** — Google Reviews en projectfoto's wegen zwaarder dan extra pagina's.

---

## 5. Prijscalculator — evaluatie

Wizard staat live. 4 stappen, slider, opties, lead-gate via Formspree. Werkt goed.

**Kansen zonder structurele wijziging:**

- Tracking-event op `calculate()`: `gtag('event', 'calculator_complete', {...})` — anders mis je drop-off-data.
- Mini-proof in resultaatkaart: "Vergelijkbaar met onze opdracht in Haren, voorjaar 2025".
- Mobiele slider controleren — ±/− knoppen overwegen.
- Optionele "stuur me deze indicatie per mail" als exit-redder midden in de flow.

**Geen actie nodig:** disclaimer-tekst, prijsranges (€45–96/m² conform markt), stappenstructuur.

---

## Aanbevelingen voor Product Manager

### 1. Landingspagina Groningen — Prioriteit: Hoog

- Type: Nieuwe pagina (`vloerverwarming-groningen.html`)
- Onderbouwing: Hoogste zoekvolume in werkgebied, korte reistijd, sterke koopkracht. Concurrenten zijn dun.
- Effort: 4–6 uur

### 2. Landingspagina Assen — Prioriteit: Hoog

- Type: Nieuwe pagina (`vloerverwarming-assen.html`)
- Onderbouwing: Tweede stad met sterke koopkracht; DVS pakt dit oppervlakkig. Tweede pagina sneller dankzij templating.
- Effort: 3–4 uur

### 3. Volwaardige FAQ-pagina — Prioriteit: Hoog

- Type: Nieuwe pagina (`faq.html`)
- Onderbouwing: Vangt 5–8 long-tail termen tegelijk af. Eén pagina, 12–15 vragen, FAQ-schema.
- Effort: 4–5 uur

### 4. Prijscalculator — twee verbeteringen — Prioriteit: Midden

- Type: Bestaand uitbreiden
- Acties: tracking-event toevoegen + referentieproject in resultaatkaart
- Effort: 1–2 uur

### 5. Projectenpagina vullen — Prioriteit: Midden

- Type: Bestaand uitbreiden
- Onderbouwing: Versterkt SEO en vertrouwen. Vraag bij elke oplevering 1 foto + 1 zin akkoord.
- Effort: 2–3 uur

### 6. FAQ-snippet uitbreiden op homepage — Prioriteit: Midden

- Type: Content update (`index.html`)
- Onderbouwing: Uitbreiden naar 5–6 items, link naar volledige FAQ-pagina.
- Effort: 1 uur

### 7. Schuimbeton — eigen ankersectie — Prioriteit: Laag-Midden

- Type: Content update binnen bestaande pagina
- Onderbouwing: USP, lage concurrentie. Geen aparte pagina; een H2 met anker volstaat.
- Effort: 1–2 uur

### 8. Google Bedrijfsprofiel + reviews-strategie — Prioriteit: Laag (maar belangrijk)

- Type: Off-site
- Onderbouwing: Doorslaggevend voor de vergelijkende doelgroep.
- Acties: profiel checken, na elke oplevering review vragen, embed na 10+ reviews.
- Effort: 1 uur setup, daarna structureel

---

## Wat we deze ronde bewust niet doen

- Geen aparte `kosten.html` — calculator dekt dit.
- Geen aparte `vloerverwarming-infrezen.html` — eerst stedelijke pagina's.
- Geen Emmen/Hoogeveen/Meppel/Roden/Leek-pagina's — buiten 30-min radius te dun.
- Geen aparte aannemerspagina — uitbreiden van over-ons.html volstaat wanneer dit relevant wordt.

Houdt de site klein, snel en onderhoudbaar — past bij de tone-of-voice: doen wat moet, niet meer.
