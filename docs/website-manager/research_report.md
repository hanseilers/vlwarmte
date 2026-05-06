# Marketing Research Rapport — 6 mei 2026

**Methode-noot (eerlijk):** WebSearch en WebFetch waren tijdens deze ronde niet beschikbaar; deze iteratie is een **synthese-update** op basis van de bestaande inventaris (sitemap, FAQ, drie stadspagina's, prijsindicatie-wizard), `analytics_report.md` (2 mei) en eerdere research-iteraties (april + 1 mei Zuidlaren-verdieping). Externe SERP-checks van vandaag staan dus niet in deze update — die staan op de openstaande lijst voor de eerstvolgende ronde wanneer WebSearch weer aan kan.

## Samenvatting

De grote bouwblokken staan: stadspagina's (Groningen, Assen, Zuidlaren), volwaardige FAQ, prijsindicatie-wizard live met sterk conversiepad, schuimbeton-anker op `diensten.html`. De grootste open kansen zitten **niet** in nieuwe pagina's, maar in **drie zwakke plekken in het verkeer dat er al is**: `systemen-producten.html` (~4,5 s gemiddelde tijd), de stadspagina's als landing (bounce 1,0), en de dunne `projecten.html`. Daarnaast blijft één off-site hefboom doorslaggevend voor lokaal converteren: Google Bedrijfsprofiel + reviews. Maximaal 5 voorstellen, gesorteerd op verwachte impact-per-uur.

## Top zoekwoorden (huidige stand)

| Zoekwoord | Volume (indicatie) | Concurrentie | Pagina | Status |
|-----------|-------------------|--------------|--------|--------|
| vloerverwarming Groningen | hoog | hoog | `vloerverwarming-groningen.html` | live, monitoren CTR |
| vloerverwarming Assen | midden-hoog | midden-hoog | `vloerverwarming-assen.html` | live, monitoren CTR |
| vloerverwarming Zuidlaren | midden | hoog | `vloerverwarming-zuidlaren.html` | live |
| installateur Zuidlaren | midden | hoog (gidsen + CV-installateurs) | zelfde pagina, H2 inzetten | dekking ok — geen 2e URL |
| vloerverwarming infrezen + plaats | midden | midden | H2 binnen stadspagina + FAQ-item | aanwezig, kan verdiepen |
| schuimbeton vloerverwarming | laag-midden | laag | `diensten.html#schuimbeton` + FAQ | dekking ok, weinig diepgang |
| vloerverwarming op houten vloer | midden | laag | FAQ-item | dekking ok |
| wat kost vloerverwarming per m2 | hoog | hoog | `prijsindicatie.html` | dekking via wizard |
| vloerverwarming + warmtepomp | midden | midden | FAQ + systemen | dekking ok |

**Nieuw t.o.v. eerdere rondes:** geen nieuwe long-tails geïdentificeerd zonder verse SERP-data. **Volgende stap voor research:** Search Console-export over 2–4 weken (FAQ + stadspagina's) om titel/description op echte impressies bij te schaven — geen gokwerk meer.

## Concurrentie — top 3 lokaal (synthese eerdere rondes)

1. **ComfortFloors (Hoogeveen)** — brede `gemeente`-template, sterke merkbekendheid, dunne lokale inhoud. **VLWarmte tegenhanger:** vestiging Zuidlaren (echt adres) + traject-verhaal + prijsindicatie.
2. **Lemmers Vloerverwarming** — sterk op renovatie/frezen, `Tynaarlo` benoemd; telefoonnummer 0318 (Apeldoorn) ondergraaft "lokaal". **VLWarmte tegenhanger:** lokaal nummer en adres expliciet, niet alleen op contactpagina maar in hero/CTA-band waar de bezoeker landt.
3. **Drentse Vloerverwarming Specialist (Klazienaveen) / Kentech (Groningen-Assen)** — gemeentepagina's resp. installatiebedrijf met vloerverwarming als bijproduct. **VLWarmte tegenhanger:** specialist (alleen vloerverwarming) i.p.v. alleskunner.

## Content gaps — wat ontbreekt nog?

Geen nieuwe **paginagaten** met hoge prioriteit. De resterende gaten zitten **binnen bestaande pagina's**:

- `systemen-producten.html` mist een **vroege CTA** (eerste schermhoogte) — enige pagina in de top met gem. tijd ~4,5 s.
- `projecten.html` mist **echte cases met plaatsnaam + foto** — versterkt zowel SEO (lokaal signaal) als vertrouwen.
- Stadspagina's missen **één expliciete tweede stap** onder de hero (FAQ-link of belknop) — landing-bounce 1,0.
- Off-site: **Google Bedrijfsprofiel** + reviewstroom blijft het zwaarste lokale-SEO-signaal dat nog niet structureel geregeld is.

Bewust **niet** aanmaken (zoals eerder besloten): aparte `kosten.html`, aparte `vloerverwarming-infrezen.html`, dunne dorpspagina's (Roden/Leek/Veendam etc.), aparte aannemerspagina.

## Aanbevelingen voor Product Manager (max 5)

### 1. Vroege CTA op `systemen-producten.html` — Prioriteit: Hoog

- **Type:** Content/UX update bestaande pagina.
- **Onderbouwing:** GA4 toont 12 sessies met gem. ~4,5 s — typisch scan-en-weg. De pagina heeft inhoudelijk wel gewicht (garantie, schema), maar de bezoeker ziet geen volgende stap zonder te scrollen.
- **Actie:** Direct onder hero een compact CTA-blok met twee paden — `prijsindicatie.html` (richtbedrag) en `faq.html` (snelle antwoorden). Pak hetzelfde patroon als onderaan, gewoon naar boven kopiëren.
- **Effort:** ~30 min.
- **Verwacht effect:** halveren bounce/exit op deze pagina, meer `wizard_start`-events vanuit systemen.

### 2. Stadspagina's — tweede stap expliciet maken — Prioriteit: Hoog

- **Type:** Content update op `vloerverwarming-groningen.html`, `vloerverwarming-assen.html`, `vloerverwarming-zuidlaren.html`.
- **Onderbouwing:** Bounce 1,0 als landing op Groningen/Assen in entry-tabel. Hero-CTA lijkt onvoldoende zichtbaar of te zwaar (offerte vs. lichter informatieverzoek).
- **Actie:** Onder hero-CTA één regel met **twee lichtere paden**: link naar FAQ (infrezen, warmtepomp, kosten) en directe belknop met `tel:` — afgestemd op contact-deeplink (`?modus=informatie#aanvraag` of `?modus=bel#aanvraag`) zodat het formulier direct in de juiste modus opent.
- **Effort:** ~1 uur (3 pagina's, 1 patch).
- **Verwacht effect:** tweede-hit-rate omhoog op stadspagina's; betere data om titel/description in Search Console op te schaven.

### 3. `projecten.html` — twee echte cases met plaatsnaam + foto — Prioriteit: Hoog

- **Type:** Content update + 1 zin akkoord van klant.
- **Onderbouwing:** Pagina is dun, gem. tijd ~0,9 s als landing en bounce 0,86. Tegelijk is dit **het sterkste lokale-SEO-signaal** dat de site nog kan toevoegen zonder nieuwe URL's: project + plaats in body-copy + alt-text op foto's.
- **Actie:** Twee opgeleverde projecten omzetten naar case-blokken — m², ondergrond, gekozen systeem, plaats. Foto met beschrijvende `alt`. Klanttoestemming: 1 zin per mail volstaat (geen formulier nodig).
- **Effort:** 2–3 uur, exclusief klant-akkoord.
- **Verwacht effect:** vermindert "doorways"-gevoel van stadspagina's (echte content op `projecten.html`); maakt social posts inhoudelijk sterker (dezelfde foto + caption).

### 4. Prijsindicatie — tracking-event op afgeronde berekening — Prioriteit: Midden

- **Type:** JS-mini-uitbreiding op `prijsindicatie.html`.
- **Onderbouwing:** Wizard heeft sterk conversiepad (~292 s gem. tijd, bounce 0,33), maar zonder `gtag('event', 'calculator_complete', …)` op het moment van eindberekening is drop-off per stap niet zichtbaar in GA4. We kunnen wel zien dat het werkt, niet **waar het beter kan**.
- **Actie:** Eén regel `gtag(...)` bij de berekenfunctie + bestaande `wizard_start` blijft. Daarna 2–4 weken meten voor uitspraken.
- **Effort:** ~30 min dev, 0 contentwerk.
- **Verwacht effect:** verschuift de prijsindicatie-discussie van "goed gevoel" naar gemeten funnel — voorwaarde voor latere micro-optimalisaties (mini-proof, exit-redder, slider-UX).

### 5. Google Bedrijfsprofiel + reviewstroom inrichten — Prioriteit: Midden (off-site, eigenaar)

- **Type:** Off-site, geen code.
- **Onderbouwing:** Voor zoekopdrachten als "vloerverwarming installateur Groningen" zit Maps/local pack vrijwel altijd **boven** organische resultaten. Dit is voor de doelgroep (vergelijken, lokaal willen) een groter signaal dan een extra landingspagina. Blijft de enige aanbeveling die niet op de site zelf landt — bewust hier laten staan tot het écht gepakt is.
- **Actie:** GBP-profiel checken/aanvullen (categorieën, foto's, openingstijden, KVK-nummer, link naar `vloerverwarming-zuidlaren.html`). Standaardmail na oplevering: 1 zin met directe reviewlink. Doel: 10 reviews binnen 3 maanden.
- **Effort:** ~1 uur setup, daarna 5 min per oplevering.
- **Verwacht effect:** lokale rank-bump zonder dat er een regel code aan te pas komt; ondersteunt **alle** stadspagina's tegelijk.

---

## Bewust niet deze ronde

- Geen nieuwe stads- of dorpspagina's — `vloerverwarming-zuidlaren.html` is live (1 mei-iteratie), volgende uitbreiding pas als Search Console-data daar aanleiding toe geeft.
- Geen tweede "alleen-installateur"-URL voor Zuidlaren — risico op dunne dubbelcontent, beslist in 1 mei-rapport.
- Geen herbouw prijsindicatie-wizard — die werkt; alleen meten toevoegen.
- Geen extra hashtags-experiment in social-research — sociale richtlijn (FB 0–3, IG 5–10, LI 3–5) staat in de agent-omschrijving en is voor concept-posts leidend, niet voor research.

## Volgende ronde — research backlog (wanneer WebSearch weer kan)

1. SERP-check op "vloerverwarming Groningen", "infrezen Drenthe", "schuimbeton vloerverwarming Noord-Nederland" — actuele top 5 per query.
2. Search Console: queries op `/faq.html` en de drie stadspagina's na 2–4 weken (impressies + CTR).
3. ComfortFloors / Lemmers / DVS opnieuw bekijken — copy- of CTA-veranderingen sinds april?
4. Eventueel: vergelijkende prijspaginas in de markt (€/m²-bandbreedtes) — consistent houden met onze wizard-uitkomsten.
