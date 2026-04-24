# VLWarmte website redesign - design specification

## Doel en context

Deze specificatie beschrijft de nieuwe website voor VLWarmte: een modern, vriendelijk en professioneel platform dat duidelijk maakt dat VLWarmte het volledige traject uitvoert, van ondervloer en schuimbeton tot en met oplevering en afwerking.

Uitgangspunten:

- De huidige site is inhoudelijk te beperkt en stuurt te vroeg op offerte.
- De nieuwe site moet eerst informeren en vertrouwen opbouwen, daarna converteren.
- Look & feel moet eigentijds zijn, met herkenning van bestaand merkgevoel (logo en kleurenfamilie).
- Eerste versie wordt gebouwd als statische multi-page website (HTML/CSS/JS).

## Scope (v1)

Gekozen scope: **multi-page core**.

Pagina's:

1. Home
2. Diensten
3. Systemen & Producten
4. Werkwijze
5. Over Ons
6. Projecten
7. Contact / Informatie & Offerte
8. Disclaimer
9. Privacy

Niet in scope voor v1:

- CMS
- Meertaligheid
- Geavanceerde uploadfunctionaliteit in formulieren
- Volledig uitgewerkte casebibliotheek met veel beeldmateriaal

## Positionering en boodschap

Kernboodschap:
**"Van ondervloer en schuimbeton tot een perfect afgewerkte, comfortabele vloer - één partner voor het hele traject."**

Merktone:

- Nuchter
- Vakbekwaam
- Toegankelijk
- Oplossingsgericht

Primaire bedrijfsbelofte:

- Heldere communicatie
- Betrouwbare uitvoering
- Realistische planning
- Kwalitatieve materialen en afwerking

## Informatie-architectuur en navigatie

Hoofdnavigatie:

- Home
- Diensten
- Systemen & Producten
- Werkwijze
- Over Ons
- Projecten
- Contact

Navigatieprincipes:

- Alle menu-items zijn klikbaar (geen dode elementen).
- Sticky header met vaste primaire CTA: `Informatie / Offerte aanvragen`.
- Footer met contactgegevens, regio's, snelle links en juridische pagina's.
- Interne doorverwijzingen tussen relevante pagina's voor betere gebruikersflow en SEO.

## Contentmodel per pagina

### 1) Home

- Hero met duidelijke propositie en regiofocus.
- Korte introductie van VLWarmte.
- Visuele 4-stappen samenvatting van ondervloer tot oplevering.
- USP-blok met concrete voordelen.
- Korte previews naar Diensten, Werkwijze en Systemen.
- CTA-blok met keuze: informatie of offerte.

### 2) Diensten

- Overzicht van het complete vloerpakket.
- Dienstblokken:
  - Ondervloer voorbereiding
  - Schuimbeton isolatie
  - Vloerverwarming aanleg
  - Dekvloer/afwerking/oplevering
- Per dienst:
  - Wanneer toepassen
  - Voordelen
  - Verwachte uitvoering
  - Korte FAQ

### 3) Systemen & Producten

- Uitleg van methodes en toepassingsgebieden.
- Vergelijkingssectie "welk systeem past bij welke situatie".
- Materiaalinformatie (isolatie, leidingen, verdelers, afwerklaag).
- Transparante keuzeprincipes en verwachting dat definitieve keuze volgt na inspectie.

### 4) Werkwijze

- 6 stappen van intake tot nazorg:
  1. Intake
  2. Opname/inspectie
  3. Voorstel en planning
  4. Ondervloer/isolatie
  5. Installatie en afwerking
  6. Oplevering en instructie
- Blok "Wat we vooraf van u nodig hebben" met o.a. m2 en ondergrondtype.
- Blok "Wat u van ons mag verwachten" met reactietijd en communicatie.

### 5) Over Ons

- Persoonlijk bedrijfsverhaal.
- Ervaring, vakmanschap en regionale focus.
- Uitleg over samenwerking met betrouwbare partners/leveranciers.

### 6) Projecten

- Structuur voor projectkaarten met:
  - Situatie
  - Oplossing
  - Resultaat
- Start met beperkte inhoud en voorbereid op latere uitbreiding met echte foto's en reviews.

### 7) Contact / Informatie & Offerte

- Keuze bovenaan:
  - "Ik wil eerst informatie"
  - "Ik wil een offerte"
- Formuliervelden:
  - Naam
  - Telefoon
  - E-mail
  - Plaats/regio
  - Oppervlakte (m2)
  - Type ondergrond
  - Nieuwbouw/renovatie
  - Gewenste planning
  - Opmerkingen
- Duidelijke opvolgverwachting (reactietermijn en vervolgstap).

### 8) Disclaimer

- Aansprakelijkheid en informatie-actualiteit.
- Duidelijke beperking van aansprakelijkheid binnen redelijke kaders.

### 9) Privacy

- Basale privacy-uitleg over gegevensgebruik vanuit contactformulier.
- Contactpunt voor privacyvragen.

## Visuele richting (goedgekeurd: C - hybride)

Stijl: **technisch sterk + warm en toegankelijk**.

Designprincipes:

- Schone, moderne basis met duidelijke hiërarchie.
- Vriendelijke details: subtiele rondingen en zachte schaduwen.
- Merkherkenning door behoud van bestaande logo-invloed en kleurenfamilie.
- Vermijden van generieke "AI-look" door eigen compositie, teksttoon en ritme.

Kleurgedrag:

- Primair accent: warme rood/oranje tinten voor CTA en highlights.
- Ondersteunend: donkere neutrale tekstkleur + lichte vlakken voor sectie-onderscheid.

Typografie:

- Moderne sans-serif.
- Krachtige koppen, praktische bodytekst.
- Heldere taal zonder overbodig marketingjargon.

Beeldstrategie:

- Focus op echte procescontext (ondervloer, schuimbeton, leidingen, afwerking).
- Consistente uitlijning, kadergebruik en beeldverhoudingen.

## Functioneel ontwerp

Conversieprincipes:

- Eerst informeren, dan converteren.
- Primaire CTA op alle kernpagina's.
- Secundaire optie: terugbelverzoek/telefonisch contact.

Formuliergedrag:

- Inline validatie.
- Duidelijke foutmeldingen per veld.
- Succesmelding met concreet vervolg.
- Altijd alternatieve contactmogelijkheid zichtbaar.

Toegankelijkheid:

- Voldoende kleurcontrast.
- Logische heading-structuur.
- Toetsenbordvriendelijke basisinteractie voor menu en formulieren.

Technische aanpak:

- Statische site in HTML/CSS/JS.
- Lichte JavaScript voor menu, accordion en formulierinteractie.
- Geoptimaliseerde afbeeldingen en lazy-loading.
- Structuur voorbereid op latere uitbreiding.

## SEO en vindbaarheid

SEO-principes v1:

- Unieke title en meta description per pagina.
- Unieke H1 per pagina met relevante zoekintentie.
- Sterke interne linkstructuur tussen diensten, systemen en werkwijze.
- Semantische HTML-opbouw.
- FAQ-secties voorbereid op structured data uitbreiding.

## Kwaliteits- en testkader

Minimale validatie voor oplevering v1:

- Responsief gedrag op mobiel/tablet/desktop.
- Alle navigatie- en CTA-links werken.
- Formuliervalidatie en succes/foutstatus gecontroleerd.
- Basis Lighthouse-check op performance, toegankelijkheid en SEO.
- Inhoudelijke review op consistentie en begrijpelijkheid.

## Risico's en vervolgstappen

Belangrijkste risico's:

- Beperkte initiële bewijslast (nog weinig reviews/cases).
- Mogelijke contentgaten per systeemtype zonder technische input.

Mitigatie:

- Starten met sterke, duidelijke basiscontent en heldere werkwijze.
- Structuur direct voorbereiden op het later toevoegen van reviews, cases en detailpagina's.

Fase na v1:

- Echte projectfoto's toevoegen.
- Testimonials/reviews integreren.
- Verdere SEO-verbreding met aanvullende pagina's per systeem en regio.
