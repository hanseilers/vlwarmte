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
| **Status** | **Tekst-workshop afgerond** (8 mei 2026) — **vraag 1 = optie A** (koel alleen als mogelijk bij geschikte installatie + doorverwijzen). |
| **Duur** | **45 minuten** (harde stop op 45 om drift te voorkomen) |
| **Doel** | Eén set **afspraken** waar PM en marketing zich aan kunnen houden: *waar* mogen we koelen/combineren benoemen, *hoe* formuleren we het veilig, *wat* is de wekelijkse “accent”-workflow zonder de kernsite te verliezen. |
| **Deelnemers** | Solo: **Hans** (PM + marketing + technisch eindoordeel). |

**Korte research — koelen met watergedragen vloerverwarming**

*(Algemene branche-informatie; geen juridisch advies — copy altijd afstemmen op wat VLWarmte concreet ontwerpt/levert.)*

- **Het kan:** bij hydraulische vloerverwarming kan dezelfde vloerafgifte in veel ontwerpen **ook koelen** (kouder medium door de kring). Praktisch vaak gekoppeld aan een **omkeerbare warmtepomp** of andere bron die koud water kan leveren; een **traditionele gas-cv zonder koelbron** levert die optie niet.
- **Randvoorwaarden:** **dauwpunt en luchtvochtigheid** bepalen grenzen — **condens** op of in vloer/bouw is het risico; ontwerp gebruikt **regeling**, vaak **dauwpuntbewaking** en zorgvuldige **aanvoertemperaturen** (oppervlak boven dauwpunt houden).
- **Comfort / verwachting:** koelen via de vloer is meestal **zacht** (geen koude luchtstraal); koelvermogen hangt af van vocht, aanvoer, afwerking (o.a. **hout** vraagt extra zorg) en bron — niet te vergelijken met airco op max.
- **Marketing:** “Koelen kan” is **inhoudelijk verdedigbaar** als categorie, maar **niet** als universele belofte per woning zonder intake.

**Besluiten (tekst-workshop, 8 mei 2026)**

| Onderwerp | Besluit |
|-----------|---------|
| **Vraag 2 — Site in pilot** | **B:** één korte **teaser/regel** op de homepage (of één vaste plek), **handmatig** per week. |
| **Vraag 3 — Max. posts met weer-hook** | **1 per week** *(ingave “Vraag E” geïnterpreteerd als één; bij 0 of 2 bedoeld: document aanpassen)*. |
| **Vraag 4 — Pilotduur** | **4 weken** handmatig (geen automatisering vóór evaluatie). |
| **Vraag 5 — °C uit weerbericht** | **Ja**, mits de post niet impliceert dat elke woning exact zo wordt. |
| **Vraag 1 — Koel-story** | **A** — koelen in algemene marketing alleen als **mogelijkheid bij geschikte installatie** (typisch WP + regeling); doorverwijzen naar FAQ/diensten; geen “wij koelen je huis”-claim. |
| **Review** | **Hans** (solo). |

**Vraag 1 (herformuleerd, na research) — keuze**

**Gekozen: A.** Algemene marketing (site-teaser + social) benoemt koelen alleen als **mogelijkheid bij geschikte installatie** (typisch **omkeerbare warmtepomp** + regeling), met **doorverwijzing** naar FAQ/diensten — geen brede “wij koelen je huis”-claim.

**Checklist**

- [x] **Koel-story:** **A** (8 mei 2026).  
- [x] **Pilot:** 4 weken — **start: 8 mei 2026**, **eind (evaluatie): 4 juni 2026** (28 dagen; vastgelegd in `sprint.md`).  
- [x] **Site:** teaser **B**.  
- [x] **Social:** max. **1** weer-hook-post/week.  
- [x] **°C uit weerbericht:** toegestaan.  
- [x] **Review:** Hans.

**Na de workshop:** besluiten ook vastleggen in `sprint.md` (*Context*) of `research_report.md` wanneer vraag 1 gekozen is.


---

## Campagne-notitie (social + site)

Koppel social posts expliciet aan **prijsindicatie**, **vloerverwarming-groningen**, **vloerverwarming-assen** en **werkwijze** — past bij sprintdoel en helpt direct-verkeer om te zetten naar diepte en leads.
