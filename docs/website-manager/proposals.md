# VLWarmte Website Voorstellen

> Gegenereerd op: 28 april 2026  
> Gebaseerd op GA4: `docs/website-manager/ga4_report.json` (fetch 2026-04-28, periode laatste 30 dagen)  
> Volgende analyse aanbevolen: **2–4 weken** na GSC-indexering en eventuele stijging organische sessies

---

## Samenvatting

In de laatste 30 dagen is het verkeer **klein maar meetbaar** (~13 sessies in de meest recente week in de export). Bezoekers komen **vooral direct** binnen; **organisch** verschijnt nog niet in de kanaal-top — dat past bij een net uitgerolde site en nog open Search Console-koppeling. De homepage (`/` en `/index.html` samen) domineert; **prijsindicatie** en **diensten** halen al meerdere sessies met redelijke tijd op de pagina. Focus: **dubbele homepage oplossen**, **FAQ + interne links** voor SEO, **conversies en GSC** afronden, daarna opnieuw meten.

### Kerncijfers (afgelopen 30 dagen — paginaniveau)

- **Homepage gecombineerd:** `/` 10 sessies + `/index.html` 4 sessies (zelfde content — rapportage dubbel)
- **Sterk relatief engagement:** `/prijsindicatie.html` — 2 sessies, gem. ~65 s
- **Landings-bounce op `/`:** ~67% (9 landingsessies in export)
- **Hoofdkanaal:** Direct (12 sessies); Unassigned 1
- **Zwakste signalen (kleine n):** `/systemen-producten.html` en `/over-ons.html` met zeer korte sessieduur bij 1 sessie — pas opnieuw beoordelen bij meer volume

---

## Voorstellen

### 1. Canonieke homepage: `/` versus `/index.html`

- **Prioriteit:** Hoog
- **Type:** Technisch / SEO
- **Onderbouwing:** GA4 toont 10 vs 4 sessies op twee URL’s voor dezelfde pagina — verdeelt autoriteit en vertroebelt rapportage.
- **Actie:** Eén strategie: server-side redirect `index.html` → `/`, of uitsluitend `/` intern linken + canonical op één variant (developer + hosting).
- **Verwacht effect:** Schonere metrics en betere SEO-consolidatie.

### 2. FAQ-pagina + FAQ-schema

- **Prioriteit:** Hoog
- **Type:** Nieuwe pagina / SEO
- **Onderbouwing:** Geen organic in kanaalrapport; research (`research_report.md`) wijst FAQ aan als grootste long-tail-hefboom.
- **Actie:** `faq.html` met 12–15 vragen, structured data, link vanaf homepage en beide stadspagina’s.
- **Verwacht effect:** Eerste organische instappen op vraagtermen.

### 3. Interne links naar prijsindicatie-wizard

- **Prioriteit:** Hoog
- **Type:** CTA / conversie
- **Onderbouwing:** Direct-verkeer heeft geen “tweede kans” via Google; interne routing naar wizard verhoogt kans op `wizard_start`. Prijsindicatie heeft al betrokkenheid bij kleine n.
- **Actie:** Contextuele blokken op `diensten.html`, `werkwijze.html`, `systemen-producten.html`.
- **Verwacht effect:** Meer wizard-funnel in GA4-events.

### 4. Google Search Console + conversiemarkering

- **Prioriteit:** Hoog
- **Type:** Technisch / meetbaarheid
- **Onderbouwing:** `conversions` in export = 0; sprint had events + verificatie-placeholder.
- **Actie:** Token plaatsen, sitemap indienen, `wizard_*` en `contact_submit` als conversies in GA4.
- **Verwacht effect:** SEO-inzicht + conversiedashboard.

### 5. Homepage: bounce en scroll verbeteren

- **Prioriteit:** Midden
- **Type:** Content / CTA
- **Onderbouwing:** Landings-bounce op `/` ~67%; weinig scrollers op homepage in 90d-export.
- **Actie:** Duidelijker primair pad (offerte/wizard); FAQ-snippet uitbreiden met link naar volledige FAQ.
- **Verwacht effect:** Lagere bounce, meer diepte.

### 6. Stadspagina’s zichtbaar maken

- **Prioriteit:** Midden
- **Type:** SEO / distributie
- **Onderbouwing:** Nieuwe URL’s zitten nog niet in top-pagina’s (laag volume).
- **Actie:** Social + footer (al deels) + interne contextlinks vanaf diensten/blog-toekomst.
- **Verwacht effect:** Sessies op Groningen/Assen-pagina’s in volgende pulls.

### 7. Schuimbeton-anker (H2 + `#schuimbeton`)

- **Prioriteit:** Midden
- **Type:** Content update / SEO
- **Onderbouwing:** Marketing research — lage effort, long-tail “schuimbeton”.
- **Actie:** H2 met anker op bestaande pagina.
- **Verwacht effect:** Betere anchor-landingservaring.

### 8. Geo / segmentatie in GA4

- **Prioriteit:** Laag
- **Type:** Analytics config
- **Onderbouwing:** 5 van 13 sessies uit VS-regio’s in export — bij kleine n verstoort dat lokaal beeld.
- **Actie:** Alleen NL segment of ongewenste regio filteren voor rapportage.
- **Verwacht effect:** Schonere beslissingen voor Noord-Nederland.

### 9. Projectenpagina vullen zodra materiaal er is

- **Prioriteit:** Laag (tot materiaal)
- **Type:** Content
- **Onderbouwing:** `projecten.html` 1 sessie, korte tijd; pagina is bewust uit nav gehaald maar blijft relevant voor vertrouwen.
- **Actie:** Cases met foto + plaatsnaam (Hans).
- **Verwacht effect:** Hogere trust en langere sessies.

---

## Data snapshot

| Pagina                 | Sessies | Bounce (landing /)  |
| ---------------------- | ------- | ------------------- |
| `/`                    | 10      | ca. 67% als landing |
| `/index.html`          | 4       | —                   |
| `/prijsindicatie.html` | 2       | —                   |
| `/diensten.html`       | 2       | —                   |

---

### 10. Weer-gedreven **accent** (verwarming vs. koelen) — PM + Marketing (discussie)

- **Prioriteit:** Te bepalen na akkoord (inhoudelijk + technisch)
- **Type:** Campagne / content / (optioneel) lichte site-“spotlight” per week
- **Idee (eigenaar):** Elke week in de PM-cyclus **kort naar het weer kijken** (bijv. KNMI/ECMWF-consensus voor Noord-Nederland) en op basis van de **verwachte temperatuur** een **klein verschuifbaar accent** kiezen: bij warme weken iets meer nadruk op **comfort + koelen met laagtemperatuur-vloer** (waar het past), bij koudere weken op **warmte en opbouw** — **niet** één thema exclusief, maar een **extra haak** voor social, e-mail en eventueel een **licht zichtbaar blok** op de site (hero-teaser, FAQ-item van de week, korte bannerregel).
- **Onderbouwing:** Seizoensbeeld en hittegolven verhogen **zoek- en gespreksintentie** rond “te warm in huis”, warmtepomp + koelen, vloer als afgifte — kan helpen om **breder** te landen bij wie nu vooral aan “verwarmen” denkt. Past bij wekelijkse cadans: PM en Marketing Research kunnen dit **vast laten landen** in `weekly_calendar.md` + sprintcontext zonder zware herbouw.
- **Technische voorwaarde (must):** Koelen met vloerverwarming gaat **niet** overal hetzelfde en niet zonder voorwaarden (o.a. **dauwpunt** / ontvochtiging, bron-koeling, regeling, ontwerp). Marketing en PM moeten copy **laten alignen met wat VLWarmte écht levert en adviseert** — geen brede belofte “wij koelen je huis” als dat niet klopt voor het merendeel van de trajecten.
- **Actie (discussie → plan):**
  1. **Workshop** — zie kop **Workshop — weer & koelaccent** hieronder (agenda + besluiten).
  2. **Vaste rubriek** in de wekelijkse cyclus: 5 regels in `sprint.md` of `research_report.md`: *weer deze week → gekozen accent → bewijs/CTA*.
  3. **Site:** basiscontent die **koelen + voorwaarden** al uitlegt (FAQ of `diensten.html`/`systemen-producten.html`); het “wekelijkse” deel is dan vooral **zichtbaarheid** (teaser, social, optioneel klein data-attribuut in HTML voor handmatige wissel — automatische weer-API op GitHub Pages is beperkt tenzij client-side fetch + fallback).
  4. **Social/Marketing:** 1 post per week die het accent **expliciet** koppelt aan het weerbeeld (“komende week richting X °C → tip over …”) zonder sensatie.
- **Verwacht effect:** Meer **relevantie** in de feed, iets sterkere **intentie-match** in de copy, mogelijk extra sessies op FAQ/diensten — te meten in GA4 na 4–8 weken (kleine n: voorzichtig interpreteren).
- **Risico’s:** Overclaimen, juridisch/technisch incorrecte koelbelofte, onderhoudslast van automatisering. **Mitigatie:** accent = **marketinglaag**, kernsite = **eeuwig waar**; automatisering pas na handmatige pilotweken.

#### Workshop — weer & koelaccent

| Veld | Invulling |
|------|-----------|
| **Status** | Gepland — **datum/tijd hier invullen** na afstemming |
| **Duur** | **45 minuten** (harde stop op 45 om drift te voorkomen) |
| **Doel** | Eén set **afspraken** waar PM en marketing zich aan kunnen houden: *waar* mogen we koelen/combineren benoemen, *hoe* formuleren we het veilig, *wat* is de wekelijkse “accent”-workflow zonder de kernsite te verliezen. |
| **Deelnemers** | Product Manager (orkest), Marketing Research / Social-lijn, **Hans** (technische waarheid + wat jullie echt leveren). |

**Voorbereiding (iedereen, max. 10 min eigen tijd)**

- **Hans:** 2–3 bullets “koelen: wanneer wél / wanneer niet / typische beperkingen” + of er **foto’s of korte cases** zijn die we mogen tonen.
- **Marketing:** 1 voorbeeld **warme week** + 1 **koude week** — welk accent zou je *nu* kiezen (headline-niveau, geen lange copy).
- **PM:** Welke **CTA** blijft leidend (prijsindicatie vs. contact vs. FAQ) als we het accent verschuiven.

**Agenda (live)**

1. **5 min — Context:** waarom weer als haak; accent ≠ exclusieve boodschap.  
2. **15 min — Technische waarheid (Hans):** grenzen koelen met vloerverwarming; standaardtraject vs. uitzonderingen; woorden die we **vermijden**.  
3. **15 min — Marketing + PM:** 2–3 veilige **formules** (headline + 1 zin) voor “warm weer” en voor “koud weer”; welk kanaal eerst (site-teaser vs. alleen social).  
4. **10 min — Workflow:** bron weer (KNMI weekoverzicht / app); waar vastleggen (`sprint.md` / `weekly_calendar`); pilot: **handmatig 2 weken** vóór automatisering.  

**Besluiten om aan het eind expliciet ja/nee op te zeggen**

- [ ] **Koel-story:** mogen we in marketing “koelen” noemen als **X** (definitie invullen in workshop).  
- [ ] **Pilot:** startdatum + einddatum handmatige wekelijkse accenten.  
- [ ] **Site:** geen wijziging / één vaste FAQ / klein herbruikbaar teaser-blok (kies één).  
- [ ] **Social:** max. posts per week die naar weer verwijzen (richtlijn).  
- [ ] **Review:** wie checkt elke week de copy vóór publicatie (naam).

**Na de workshop:** PM zet de besluiten in **één** bestaand document (`sprint.md` *Context* of `research_report.md` kop *Workshop*) — geen losse drive zonder trace.

---

## Campagne-notitie (social + site)

Koppel social posts expliciet aan **prijsindicatie**, **vloerverwarming-groningen**, **vloerverwarming-assen** en **werkwijze** — past bij sprintdoel en helpt direct-verkeer om te zetten naar diepte en leads.
