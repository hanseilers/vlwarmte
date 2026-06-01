# VLWarmte — Release Notes

Wekelijks bijgewerkt door de Product Manager Agent. Nieuwste release bovenaan.

---

## Release — week van 2 juni 2026 (cyclus 14)
**Deployment:** 01-06-2026 — PM push naar `main` (GitHub Pages).
**Versie:** *(na commit)*

### Wat is er veranderd
- **Assen-pagina:** de extra "lees verder"-regel en de knoppenband direct onder de hero zijn weg. De pagina volgt nu hetzelfde patroon als Groningen — eerst uitleg, daarna pas acties onderaan.
- **Prijsindicatie:** de introtekst boven de wizard belooft nu expliciet een richtbedrag in ongeveer twee minuten, in lijn met de Google-titel. Social previews (Facebook/LinkedIn) tonen dezelfde boodschap.
- **Homepage Drenthe-hub:** de link naar Assen heet nu "Vloerverwarming Assen en omgeving".
- **Google Ads defaults (repo):** de RSA mag alleen nog landen op het offerte-formulier of de prijsindicatie — niet meer op projecten of losse stadspagina's. Live campagne in Ads UI moet handmatig worden gelijkgetrokken.

### Waarom
- **Assen:** GA4 toonde 0,7 seconden en nul scrollers — bezoekers zagen alleen hero en knoppen. Diagnose cyclus 13 bevestigde layout, geen inhoudsprobleem.
- **Prijsindicatie ATF:** 58% bounce als landing; titel belooft "2 minuten" maar de hero verwees nog naar FAQ — message-match aangescherpt.
- **Ads final URLs:** Paid Search had 13 sessies en 0 conversies terwijl het offerte-tabblad 10 conversies op 11 sessies haalt. Te brede final URLs lieten Google op de homepage landen (67% bounce).

### Verwacht effect
Bij juni-fetch (~22 juni):
- Assen: bounce onder 70%, sessieduur boven 5 seconden.
- Prijsindicatie: entry-bounce richting onder 45% bij voldoende verkeer.
- Paid Search: eerste conversies zodra GA4↔Ads gekoppeld is én RSA in Ads UI op offerte-deeplink staat.

### Social media deze week
Weekplanning 2–9 juni 2026: Drenthe-hub, Hoogeveen-dorpen en werkwijze zichtbaar maken op social; Facebook message-match (één link per post). Zie `docs/website-manager/social/weekly_calendar.md`.

---

## Release — week van 26 mei 2026 (cyclus 13)
**Deployment:** 26-05-2026 17:20 — PM push naar `main` (GitHub Pages).
**Versie:** `47a9583`
**GitHub Actions:** pages-build run `26457537868` (success, 51s); E2E production `26457539329` (success, 2m35s).

### Wat is er veranderd
- **Prijsindicatie-pagina** krijgt een scherpere zichtbaarheids-tekst: titel en omschrijving in Google noemen nu expliciet Drenthe en Noord-NL met de belofte "richtbedrag in 2 minuten". De wizard zelf en de pagina-inhoud blijven ongewijzigd.
- **Hoogeveen-pagina** vermeldt nu Hollandscheveld, Fluitenberg, Noordscheschut, Elim en Tiendeveen in één zin in de bestaande "Ook actief in"-sectie. Titel en omschrijving in Google ook bijgewerkt richting omgeving Hoogeveen.
- **Homepage** krijgt een compacte regio-sectie "Vloerverwarming in heel Drenthe" met links naar de zes stadspagina's (Groningen, Assen, Hoogeveen e.o., Emmen, Drachten, Leeuwarden) plus links naar uitgevoerd werk en prijsindicatie. Eén klik vanaf de homepage naar elke regio.
- **Werkwijze-pagina** krijgt zachtjes meer interne traffic: één tekstlink in de diensten-uitleg en één zin met link in de projecten-intro verwijzen nu naar `werkwijze.html`. Geen extra knoppen.
- **Diagnose Assen-pagina:** vastgesteld dat een extra "lees verder"-regel en een dubbele knoppen-band tussen hero en eerste content-sectie ervoor zorgen dat mobiele bezoekers de eigenlijke uitleg niet zien. Fix staat klaar voor volgende sprint — geen wijziging deze release.

### Waarom
- **Prijsindicatie & Hoogeveen titels:** Search Console laat zien dat beide pagina's veel vertoningen krijgen (75 en 30 in 28 dagen) maar 0 clicks — de Google-snippet matcht niet met wat mensen zoeken. Title- en meta-aanscherping is de goedkoopste hefboom om die vertoningen om te zetten in clicks. Hoogeveen rangt al op 4,8 voor "vloerverwarming fluitenberg" zonder dat het dorp in de body stond — nu wel.
- **Drenthe-hub op homepage:** 82 vertoningen op "vloerverwarming drenthe" verspreid over 5 URL's, geen ervan rangt — Google weet niet welke pagina de "Drenthe-pagina" is. Eén duidelijk regio-blok op `/` met links naar de stadspagina's geeft dat signaal af, zónder een nieuwe thin-content pagina te bouwen.
- **Werkwijze interne links:** GA4 laat zien dat `werkwijze.html` ~78% conversie haalt als landing-pagina, maar krijgt amper instromers. Twee kleine tekstlinks vanaf de twee grootste pagina's (diensten, projecten) is een laagdrempelige test.
- **Assen-diagnose:** GA4 toonde 0,7 seconden gemiddelde sessieduur en 0 scrollers op 7 bezoeken — extreem. Statische broncode-vergelijking met Groningen (werkt wel) wees twee structurele blokken aan; bevestiging dat het géén content-probleem maar een layout-probleem is.

### Verwacht effect
Bij de meet-cyclus over ~4 weken (juni-fetch ~22 juni):
- `prijsindicatie.html` GSC CTR van 0% naar >0,5% (eerste echte clicks vanuit Google).
- `vloerverwarming-hoogeveen.html` gemiddelde rang onder de 10, óf ≥1 GSC-click op "vloerverwarming hoogeveen".
- `/` zichtbaar op rang <30 voor "vloerverwarming drenthe" (nu 65,7).
- `werkwijze.html` entry-sessies +20% (van 9 naar ≥11) zonder dat `diensten` of `projecten` verzwakt.
- Assen-diagnose afgerond — fix uitgevoerd in cyclus 14, daarna 4–6 weken meten.

### Social media deze week
Weekplanning 27 mei – 4 juni 2026 in `docs/website-manager/social/weekly_calendar.md`. 10 posts: 3× LinkedIn, 4× Instagram, 3× Facebook. Thema's: Zeegse- en Zuidlaren-projecten (cyclus 11), laagopbouw op LinkedIn, Friesland-zuidoost via Drachten. Facebook-blok herstelt nadrukkelijk message-match (analytics-bevinding: 32 sessies / 0 conversies via FB tot nu toe) — één intentie + één link per post, met deeplinks naar `?modus=offerte#aanvraag`, `?modus=bel#aanvraag` of `prijsindicatie.html`.

---

## Release — week van 22 mei 2026 (cyclus 12)
**Deployment:** 22-05-2026 — PM push naar `main` (GitHub Pages).
**Versie:** `8fff9dd`

### Wat is er veranderd
- **Drachten ↔ projecten:** onderlinge links — vanaf projecten naar Drachten/Heerenveen, vanaf Drachten naar uitgevoerd werk met foto’s.
- **Diensten:** in de hero een link “Bekijk uitgevoerd werk” (geen tweede primaire knop).
- **Drachten delen:** social preview gebruikt nu het echte projectbeeld (`og-projecten.jpg`).
- **Sitemap:** `lastmod` bijgewerkt voor projecten en Drachten.
- **Google Ads-voorbereiding:** `projecten.html` in defaults-`final_urls`; zoekwoord Meppel uit de defaults-keywords (nog geen landingspagina).

### Waarom
Cyclus 11 staat nog in het meetvenster — geen retweak van projecten/over-ons/diensten-hero. Wel: social-kalender en Ads message-match op echte cases; Drachten had 0 GA4-sessies ondanks live pagina; Meppel-keyword zonder URL kost relevantie.

### Verwacht effect
Juni-fetch (~15 juni): eerste organisch verkeer Drachten, betere interne doorstroom naar projecten, voorbereid RSA/sitelinks met projecten-URL. Cyclus 9–11 meetdoelen dan hard beoordelen. GA4↔Ads-attributie blijft gepland ~1 juni.

### Social media deze week
7 posts (handmatig): live cases Zeegse/Zuidlaren, projecten-route, diensten, Drachten-pagina — sluit aan op nieuwe links op diensten en Drachten.

---

## Release — week van 20 mei 2026 (cyclus 11)
**Deployment:** 20-05-2026 — push `dc3d2de` naar `main` (GitHub Pages).
**Versie:** `dc3d2de`

### Wat is er veranderd
- **Projecten:** twee echte cases live — Zeegse (100 m², souterrain + begane grond) en Zuidlaren (50 m² op draadstaalnetten, benedenverdieping), met werkbeelden en korte situatie/oplossing/resultaat.
- **Foto’s:** productie-afbeeldingen in `assets/img/projecten/`; bronmateriaal blijft in `beeldmateriaal/projecten/`.
- **Projecten in sitemap** en link “Bekijk uitgevoerd werk” op homepage en diensten.
- **Diensten:** compacte keuze direct onder de hero — prijsindicatie of offerte, zonder eerst te scrollen.
- **Footer:** Drachten-link op alle pagina’s (zelfde plek als op de Drachten-stadspagina).
- **Google Ads-voorbereiding:** RSA-tekst in defaults wijst naar uitgevoerd werk op `projecten.html` (alleen repo; geen live advertentiewijziging).

### Waarom
- Eerste echte projectinput van de eigenaar: placeholders ondermijnen vertrouwen; analytics toonde 100% entry-bounce op projecten en ~7,5 s gemiddelde tijd.
- `diensten.html` als landing: 78,6% bounce, 0 conversies — vroege keuze-CTA volgt het bewezen offerte-deeplink-patroon.
- Drachten-pagina was live maar nog niet overal vindbaar; Friesland blijft ondervertegenwoordigd in GA4.

### Verwacht effect
GA4 rond 15 juni: lagere entry-bounce op `projecten.html`, meer scrollers, eerste sessies op Drachten-pagina, betere doorstroom vanaf diensten. Cyclus 9–10 meetdoelen pas dan hard beoordelen. GA4↔Ads-attributie blijft gepland rond 1 juni (geen extra spend deze sprint).

### Social media deze week
7 posts (handmatig): Zeegse- en Zuidlaren-foto’s, Drachten-pagina, projecten-route met offerte-deeplink. Na deze release mogen posts met plaatsnamen live; LinkedIn 2 en Instagram 1–2 gebruiken de nieuwe cases.

---

## Release — week van 18 mei 2026 (cyclus 10)
**Deployment:** 18-05-2026 UTC — GitHub Pages run **26013287851** (`pages-build-deployment`); E2E-run **26013288326** gestart na push.
**Versie:** `de6596b`

### Wat is er veranderd
- **Nieuwe stadspagina:** `vloerverwarming-drachten.html` voor Drachten én Heerenveen (zelfde opzet als de Leeuwarden-pagina), opgenomen in de sitemap.
- **Offerte-knoppen site-breed aangescherpt:** elke "Informatie / Offerte aanvragen"-knop gaat nu direct naar het offerteformulier (`contact.html?modus=offerte#aanvraag`) in plaats van de kale contactpagina — op alle 19 pagina's.
- **Over ons:** onderaan een duidelijk vervolgblok met twee knoppen — prijsindicatie en offerte aanvragen.
- **Projecten:** het eerste scherm is compacter gemaakt zodat de twee actieknoppen meteen zichtbaar zijn, vóór de fotogalerij.
- **Homepage + diensten:** een paar natuurlijke tekstlinks toegevoegd naar de kosten-uitleg en de stadspagina's (waaronder Drachten).
- **Google Ads-instelling:** de zoekwoorden "vloerverwarming drachten" en "vloerverwarming heerenveen" wijzen nu naar de nieuwe Drachten-pagina (alleen het instellingenbestand in de repo; geen advertenties live gezet, geen uitgaven gewijzigd).

### Waarom
- **Drachten/Heerenveen-pagina:** in de Google Ads-instellingen stonden zoekwoorden voor Drachten en Heerenveen zonder bijpassende pagina — bezoekers van die zoekopdrachten kwamen op een algemene pagina terecht. Dat lekt aanvragen. Friesland is bovendien sterk ondervertegenwoordigd in het bezoek (4 sessies tegen 164 in Drenthe).
- **Offerte-deeplink:** cijfers zijn helder — wie direct op het offerteformulier landt bouncet 9% en levert veel aanvragen op; wie op de kale contactpagina landt bouncet 80%. Alle offerte-knoppen sturen nu naar de bewezen route.
- **Over ons / projecten:** beide pagina's zijn zwakke instappunten (rond 80–100% bounce, vrijwel geen doorstroom). Een duidelijke vervolgstap naar prijs/offerte moet bezoekers vasthouden.
- **Interne links:** de homepage trekt het meeste verkeer; vandaar contextuele links naar de kosten-uitleg en stadspagina's voor zowel doorstroom als vindbaarheid.

### Verwacht effect
Bij de volgende meting (GA4-fetch rond 15 juni): eerste organische sessies op de Drachten-pagina, lagere bounce op de kale contactpagina met meer doorstroom naar het offerteformulier, lagere entry-bounce op over-ons en projecten, en geen Ads-zoekwoord meer zonder bijpassende pagina. De cyclus-9-wijzigingen worden bij diezelfde meting pas hard beoordeeld (3 dagen is nog ruis). De grote openstaande kwestie blijft de GA4↔Ads-conversiekoppeling — die vraagt een sessie met scriptrechten, gepland rond 1 juni.

### Social media deze week
7 posts gepland (handmatig te publiceren): 3 op LinkedIn (di–do, B2B/aannemers, kosten-uitleg, projecten-offerteroute) en 4 op Instagram (wo/vr/za, Assen-werkbeeld, eerlijke prijsbandbreedte, contactkeuze, vakmanschap). Kosten-intent linkt naar de prijsindicatie, offerte-intent naar de offerte-deeplink. Drachten/Heerenveen bewust nog geen stadsclaim tot de pagina geïndexeerd is.

---

## Release — week van 9 juni 2026 (cyclus 9)
**Deployment:** 15-05-2026 UTC — GitHub Pages run **25914206844** (succes); E2E **25914207646** (workflow succes; IMAP-stap overgeslagen zonder repo-secrets).  
**Versie:** `d2bea47`

### Wat is er veranderd
- **Nieuwe stadspagina:** `vloerverwarming-hoogeveen.html` met eigen copy, JSON-LD Service, hero-beeld uit `beeldmateriaal/`.
- **Projecten:** compactere kop + **offerte**-CTA naast prijsindicatie en opname in de hero.
- **Prijsindicatie:** de bestaande **kosten-uitleg** (drivers m², ondergrond, schuimbeton) staat nu **boven** de wizard voor betere SEO en cold landers.
- **Contact:** boven het tabblad-formulier een korte **intentie-keuze** met deeplinks naar dezelfde modi.
- **Assen:** **Lees verder**-link naar het eerste inhoudsblok om scroll/trust te helpen.
- **Footers + sitemap:** Hoogeveen toegevoegd op alle relevante pagina’s.

### Waarom
- GA4 (15-05): weekvolume herstelt; zwakke punten blijven cold **contact**-landings, **projecten** entry-bounce, **prijsindicatie** als landing, en **Assen** zonder scrollers.
- City-cluster: Hoogeveen is de logische volgende stap na Emmen.

### Verwacht effect
- Eerste organische sessies op Hoogeveen-URL; lagere bounce op prijs- en contactlandings; meer zichtbare scroll op Assen.

### Social media deze week
Zie `weekly_calendar.md` (week 2 juni): Hoogeveen-lancering, projecten-offerte, prijs-uitleg, contact-intent, meetnoot betaald.

---

## Release — week van 2 juni 2026 (cyclus 8)
**Deployment:** 13-05-2026 ~09:17 UTC (PM: `git push origin main` — GitHub Pages run **25784369037**, succesvol; E2E **25784370229**)  
**Versie:** `2f911bb`

### Wat is er veranderd
- **Stadspagina’s:** `vloerverwarming-assen.html` en `vloerverwarming-groningen.html` hebben nu een **twee-koloms hero** met echt klantbeeld en korte trustregel (werkgebied, reactie binnen 1 werkdag, 10 jaar garantie op de buis).
- **Nieuwe pagina:** `vloerverwarming-emmen.html` voor Emmen en Zuidoost-Drenthe — zelfde technische basis als andere citypages, unieke copy, JSON-LD Service.
- **Footer + sitemap:** Regio-links en `sitemap.xml` uitgebreid met Emmen op alle relevante pagina’s.
- **Diensten (`diensten.html`):** direct onder de hero een **keuzehulp** met drie kaarten (compleet traject / schuimbeton-kruipruimte / systeem+aanleg) met duidelijke doorklikken.
- **Systemen (`systemen-producten.html`):** extra toelichting voor zoek-landers + **offerte**-deeplink in de hero.
- **PM-docs:** verse `analytics_report.md` (13-05), bijgewerkt `research_report.md` (Ads-campagne ENABLED), nieuwe social kalender week 26 mei, sprint cyclus 8.

### Waarom
- GA4 toont op Assen **0 seconden** gemiddelde sessieduur en **100% bounce** — dat is geen “lastige klant”, dat is een **te zwakke eerste indruk**.
- `diensten.html` verliest landers in het eerste scherm; keuzehulp verlaagt cognitieve last en stuurt sneller naar prijsindicatie of offerte.
- Emmen ontbrak als landing terwijl keywords en werkgebied die richting al logisch maken.
- Systemen-pagina ving verkeer met hoge landingsbounce; heldere **volgende stap** moet daar direct zichtbaar zijn.

### Verwacht effect
- Stadspagina’s: bounce en tijd op pagina meetbaar verbeteren; Emmen: eerste organische sessies en betere aansluiting op Ads-termen.
- Diensten: landingsbounce richting **<70%**.
- Systemen: meer sessies met tweede pagina (prijs/contact).

### Social media deze week
Zie `weekly_calendar.md`: focus op Emmen-lancering, diensten-keuzehulp, systemen-route en Groningen-in-beeld; CTAs met `?modus=offerte` waar passend.

---

## Release — week van 25 mei 2026 (cyclus 7)
**Deployment:** 11-05-2026 10:07 (PM: `git push origin main` — GitHub Pages, runs **25658133756** (pages) en **25658134654** (E2E))  
**Versie:** `ecadcb7`

### Wat is er veranderd
- **Home (`index.html`):** carry-over van cyclus 6 is nu live — strakker hero met eyebrow, één heldere kop, **trust-strip** ("10 jaar garantie op de buis · Groningen · Friesland · Drenthe · Reactie binnen 1 werkdag") en een **mobiele sticky-CTA** naar de offerte-flow. Geen wijzigingen aan GA4-tracking.
- **Prijsindicatie (`prijsindicatie.html`):** onder de wizard staat nu ~340 woorden **leesbare uitleg** — wat een prijs per m² beïnvloedt, een nuchtere richtbandbreedte (€45-95/m², afhankelijk van situatie), regio-uitgangspunten en de expliciete disclaimer "indicatie ≠ offerte, geen verkoopgesprek". Wizard zelf is ongewijzigd.
- **Contact (`contact.html`):** boven de tabs (informatie / offerte / bel) staat nu een compact **"Zo werkt het na insturen"-blok**: 3 stappen + reactietijd binnen 1 werkdag + wat de klant terugkrijgt. In de **offerte-modus** is de "Bel ..."-knop tot secundair gedegradeerd, zodat het formulier de duidelijke primaire actie is. Voor informatie- en bel-modi blijft de hiërarchie ongewijzigd.
- **Projecten (`projecten.html`):** eerste viewport herschreven naar één concreet renovatieproject (Drenthe, opname tot oplevering in 8 werkdagen), één echte klantfoto, en twee duidelijke CTA's: prijsindicatie + "Plan een opname". De projectenlijst eronder is ongewijzigd.
- **Meetruis dichten:** `disclaimer.html` en `privacy.html` krijgen `noindex,follow` (geen indexering meer). `logo-varianten.html` (cyclus 5 redirect-pagina) is geverifieerd — geen interne links meer.
- **PM-docs:** verse GA4-analyse (cyclus 7), marketing-research rapport (incl. Google Ads keyword-uitbreiding voor infrezen, kruipruimte, prijsindicatie + extra Friesland/Drenthe-steden) en social weekplanning week 18-23 mei. Cyclus 6 sprint gearchiveerd.

### Waarom
- GA4 toont week-op-week een scherpe daling (171 → 72 sessies, -57,9%) en **0 conversies op 12 Paid Search sessies**. Dat laatste wijst op message-match + tracking-mismatch, niet op intent — vandaar de focus op kosten-content op `prijsindicatie.html` en één primaire actie op `contact.html?modus=offerte`.
- `projecten.html` had 87,5% bounce en 0,83 sec gem. sessieduur — een lek dat bezoekers verloren laat gaan vóór ze scrollden. Een concreet voorbeeld + helder klikpad biedt direct vervolg.
- `disclaimer.html`, `privacy.html` en `logo-varianten.html` werden samen 21 keer als landing geserveerd met 100% bounce — meetruis die de cijfers vertroebelt.
- De carry-over hero refresh + sticky-CTA versterken de toegevoegde trust-strip: kerngebied, reactietijd en buisgarantie zonder te hoeven scrollen.

### Verwacht effect
- **Paid Search:** eerste meetbare conversies in `google / cpc` binnen 2-4 weken zodra de message-match staat (offerte- en kosten-landings beter afgestemd).
- **Prijsindicatie:** lagere bounce voor organisch verkeer met "kosten per m²"-intent — Search Console laat binnen 2-4 weken nieuwe queries op dat cluster zien.
- **Projecten:** bounce onder 70% (was 87,5%) en gem. sessieduur naar minimaal 20 sec.
- **Meetruis:** sessies op `disclaimer.html` + `privacy.html` + `logo-varianten.html` als landing naar nul; schonere kanaaltoewijzing in GA4.

### Social media deze week
Week 18-23 mei: 3× LinkedIn (di/wo/do, 08:30-09:30) en 4× Instagram (wo/vr/za, 18:30-19:30). Captions versterken trust-signalen (werkgebied, 1 werkdag reactie, 10 jaar buisgarantie, één aanspreekpunt) en sturen intentgericht naar `prijsindicatie.html`, `?modus=offerte`, `?modus=informatie` of `?modus=bel`. Hoofdbeeld: nieuwe klantfoto `vlwarmte-facebook-2026-05-buiswerk-op-net.jpeg`. Het tweede inputbeeld (oogt AI) is afgewezen — vragen om een echte vakman-aan-het-werk-foto.

---

## Release — week van 18 mei 2026 (cyclus 5)
**Deployment:** 08-05-2026 16:28 (PM: `git push origin main` — GitHub Pages, run **25566957636**, succesvol)  
**Versie:** `75977ba`

### Wat is er veranderd
- **`logo-varianten.html`:** vervangen door een minimale **doorverwijspagina** naar de homepage — `noindex,follow`, canonical naar `/`, meta-refresh, zichtbare link en `noscript`-fallback. GA4-meting blijft staan zodat we kunnen zien of het restverkeer daadwerkelijk daalt.
- **`over-ons.html`:** **head SEO refresh** (title, meta, Open Graph, Twitter): Zuidlaren, werkgebied Drenthe / Groningen / Friesland, compleet traject (ondervloer, schuimbeton, installatie, dekvloer) bij **één partij**. H1 en body ongemoeid.
- **`vloerverwarming-assen.html`:** vroege **CTA-band** met drie knoppen — **Prijsindicatie**, **FAQ**, **Terugbelverzoek** — direct na de hero. In de openingsalinea een nuchtere link naar `werkwijze.html`.
- **Stadspagina-cluster (Assen, Groningen, Zuidlaren):** onderaan een sectie **"Ook actief in:"** met kruislinks naar de twee zusterstadspagina's. Geen aparte H1, gewoon een korte tekstuele verbinding.
- **`index.html` en `diensten.html`:** secundaire tekstlinks **Bekijk onze systemen** en **Bekijk projecten** toegevoegd (geen wijziging aan hero of head); de bestaande prijsindicatie/contact-CTA's blijven dominant.
- **PM-docs:** verse GA4-fetch (cyclus 5, 8 mei), marketing research-rapport (incl. Google Ads dry-run check), sprint cyclus 5 + social kalender week 11 mei. Archief van cyclus 4 toegevoegd.

### Waarom
- GA4 toont nog steeds **single-page bounces (1,0)** op stadspagina Assen, systemen, projecten en restverkeer op `/logo-varianten.html` (7 sessies); homepage en prijsindicatie blijven de echte conversiemotor (Direct dominant). Deze sprint richt zich op **opschonen van ruis** en **secundaire klikpaden** — geen grote nieuwe pagina's, wel duidelijkere routes naar de wizard, FAQ en terugbel.
- Marketing-research bevestigt: **geen nieuwe calculator** nodig, en de Google Ads-defaults (RSA + keywords) blijven dry-run-only tot er expliciete spend-/mutatie-goedkeuring is.

### Verwacht effect
- Minder sessies op `/logo-varianten.html` richting 0; signaal of er nog externe links blijven aanvoeren.
- Lagere single-page bounce op `/vloerverwarming-assen.html` en `/over-ons.html`; meer secundaire pageviews vanaf homepage en `/diensten.html` naar systemen/projecten.
- Stadspagina-onderlinge links → meer kans op vervolgklik bij regio-mismatch.
- Effecten in GA4 + Search Console pas zichtbaar na 2–4 weken.

### Social media deze week
Zie `docs/website-manager/social/weekly_calendar.md` (week van 11 mei 2026): 3× LinkedIn (di–do, 8–10u), 4× Instagram (wo/do avond + vr/za), met thema's prijsindicatie, werkwijze, FAQ en terugbel — geen paniek-copy over sessievolume, wel duidelijke vervolgstap.

---

## Release — week van 16 juni 2026
**Deployment:** 08-05-2026 (PM: `git push origin main` — GitHub Pages, run **25555351102**, succesvol)  
**Versie:** `ff6c9b9`

### Wat is er veranderd
- **`diensten.html` en `contact.html`:** scherpere **title + meta + sociale previews** (Zuidlaren, Drenthe, traject; contact met offerte/informatie/**terugbel** en reactie binnen werkdag).
- **`systemen-producten.html`:** zelfde snippet-aanscherping + knop **Terugbelverzoek** naast prijsindicatie en FAQ in het vroege CTA-blok.
- **`projecten.html`:** **Terugbelverzoek** naast informatie in de hero-soft-row.
- **`faq.html`:** snippet richting **infrezen, warmtepomp, kosten** en routes naar prijs/contact/terugbel.
- **PM-docs:** analytics (cyclus 4, verse fetch), marketingkop, sprint + social kalender week 16 juni; archief sprint week 9 juni en vorige socialweek.

### Waarom
- GA4: hoge landingsbounce op diensten/contact/systemen/projecten; Paid Search 12 sessies zonder conversie — duidelijkere SERP en dezelfde terugbel-CTA als elders.

### Verwacht effect
- Betere alignment zoeksnippet ↔ pagina; meer tweede stappen vanaf systemen en projecten.

### Social media deze week
Zie `docs/website-manager/social/weekly_calendar.md` (week van 16 juni 2026).

---

## Release — week van 9 juni 2026
**Deployment:** 08-05-2026 (PM: `git push origin main` — GitHub Pages, run **25554936393**, succesvol)  
**Versie:** `1d6bc5e`

### Wat is er veranderd
- **Live zetten sprint week 2 juni:** `prijsindicatie.html` CTA-band boven de wizard, navigatie-exit op `disclaimer.html` en `privacy.html`, `hero-soft-row` op `projecten.html`.
- **`werkwijze.html` en `over-ons.html`:** betere **SEO-snippet** (title + description + sociale previews) met Zuidlaren, Drenthe en traject/prijsindicatie — helpt verwachting bij korte sessies.
- **`diensten.html` en `faq.html`:** derde knop **Terugbelverzoek** in het donkere CTA-blok — licht pad naast prijs en FAQ.
- **`index.html`:** meta/OG/Twitter-description noemt **online prijsindicatie** voor duidelijkere SERP.
- **PM-docs:** nieuwe sprint, analytics (cyclus 3), marketing-update, social kalender week 9 juni; archief van vorige sprint/kalender.

### Waarom
- Vorige developer-ronde stond nog lokaal; zonder push geen meting op productie.
- Analytics: hoge bounce op diensten-landing; werkwijze korte sessies — snippets + terugbel verlagen drempel.

### Verwacht effect
- Meer gestarte contactflows vanuit diensten/FAQ; betere CTR vanuit organisch op werkwijze/over-ons na herindexering.

### Social media deze week
Zie `docs/website-manager/social/weekly_calendar.md` (week van 9 juni 2026).

---

## Release — week van 2 juni 2026
**Deployment:** 08-05-2026 (PM: `git push origin main` — GitHub Pages)  
**Versie:** `bab08a8`

### Wat is er veranderd
- **`prijsindicatie.html`:** CTA-blok direct onder de hero met link naar de wizard (`#wizard`), directe offerte-route en informatieformulier — betere aansluiting op **Paid Search**-landings en snellere tweede stap.
- **`scripts/data/google_ads_lead_campaign_defaults.json`:** Drie RSA-headlines gericht op **online prijsindicatie** en **richtbedrag** (voor volgende campagne-updates of handmatige RSA-sync).
- **`disclaimer.html` + `privacy.html`:** Korte navigatie-exit onder de hero (homepage, prijsindicatie, contact) om landings-bounce 1,0 te verzachten.
- **`projecten.html`:** `hero-soft-row` met **Informatie aanvragen** — lichtere stap naast bestaande knoppen.
- **Playbooks + `AGENTS.md`:** Product Manager voert **commit en push** zelf uit na developer (geen eigenaar nodig behalve bij git-auth).

### Waarom
- Analytics (cyclus 2, 8 mei): **google/cpc** zonder conversies; prijsindicatie en contactroutes moeten in copy én op de pagina maximaal zichtbaar zijn.
- Disclaimer/privacy als instap met bounce 1,0 — minimale exit-hulp.

### Verwacht effect
- Meer `wizard_start` / conversies vanaf prijsindicatie-landing; eerste signalen voor Paid Search na RSA-sync in Ads.
- Minder directe exit op disclaimer/privacy.

### Social media deze week
Zie `docs/website-manager/social/weekly_calendar.md` (week van 2 juni 2026).

---

## Release — week van 18 mei 2026
**Deployment:** 08-05-2026 (GitHub Pages run `25543472674`, succesvol)
**Versie:** `3e97a18` (code) + `d396fa9` (documentatie deploymentregels) — Sprint 18 mei: vroege CTA’s, logo-URL redirect, GA4 weekly_trend backfill

### Wat is er veranderd
- **`logo-varianten.html`:** minimale doorverwijspagina met canonical naar de homepage, meta-refresh en een zichtbare link voor bezoekers zonder automatische doorstuur — vangt bookmarks en oude links op zonder 404.
- **`diensten.html`, `werkwijze.html`, `over-ons.html`:** direct onder de hero een **`cta-band`** met duidelijke paden naar de prijsindicatie en FAQ of contact (informatie-dieplink), zodat landers meteen een tweede stap zien.
- **`assets/css/styles.css`:** helper **`.cta-band-stack`** voor nette stapeling van meerdere knoppen in donkere CTA-blokken op smalle schermen.
- **`scripts/ga4_fetch.py`:** `weekly_trend` bevat altijd **8 weken**; weken zonder data in GA4 worden met nul-sessies ingevuld zodat trends in rapportages niet breken.

### Waarom
- Analytics (7 mei) toonde nog restverkeer naar de oude logo-URL en een hoge bounce op `diensten.html` als landing, korte sessies op `werkwijze.html` en weinig vroege vervolgstap op `over-ons.html`.
- De fetch-export had soms minder dan acht weken in `weekly_trend` doordat de GA4-API geen rij teruggeeft bij nul sessies — dat maakt weekvergelijking onmogelijk voor de PM-cyclus.

### Verwacht effect (meting rond 4 juni 2026)
- Minder “dood” verkeer op `/logo-varianten.html`; consolidatie richting homepage.
- Lagere bounce en vaker tweede hit vanaf `diensten.html` en `werkwijze.html`; vaker start vanuit `over-ons.html` richting prijsindicatie of licht contact.
- Betrouwbare 8-punts weekreeks in `ga4_report.json` na elke fetch.

### Social media deze week
Zie `docs/website-manager/social/weekly_calendar.md` (week van 18 mei 2026).

---

## Release — week van 11 mei 2026
**Deployment:** 06-05-2026 10:28 (commit `2f22120`, GitHub Pages run `25424644693`, in_progress bij rapportage)
**Versie:** `2f22120` — Sprint 11 mei: conversiepaden contact + stadspagina's + projecten, GA4 weekly_trend fix, calculator_complete

### Wat is er veranderd
- **`contact.html`:** boven het bestaande formulier staat nu een directe-keuze blok met drie paden — bel-knop, sms-knop ("stuur een berichtje") en een secundaire route naar de prijsindicatie. Op mobiel staan de drie keuzes onder elkaar full-width. Het formulier zelf is ongewijzigd.
- **Stadspagina's** (Groningen, Assen, Zuidlaren): onder de bestaande hero-CTA een korte regel "liever bellen of even iets vragen?" met een bel-knop en een knop "informatie aanvragen" die `contact.html?modus=informatie#aanvraag` opent.
- **`projecten.html`:** de hero-tekst is herschreven naar één eerlijke alinea (er zijn nog geen openbaar gepubliceerde cases; referenties op verzoek), met daaronder twee knoppen: prijsindicatie en FAQ. De rest van de pagina blijft staan.
- **`prijsindicatie.html`:** nieuw GA4-event `calculator_complete` op het moment dat de eindberekening getoond wordt — met de ingevoerde m², ondergrond en gekozen systeem (geen persoonsgegevens). Bestaande events blijven staan.
- **`scripts/ga4_fetch.py`:** loop voor `weekly_trend` is gefixt — schrijft nu acht niet-overlappende weken in plaats van één. Maakt week-over-week analyse mogelijk vanaf de volgende fetch.

### Waarom
- Analytics Agent (6 mei) liet zien dat `contact.html` als landing 8 sessies trekt met bounce 1,00 en 0 conversions, terwijl `prijsindicatie.html` ter vergelijking 13 conversions levert op 11 landingen — sterkste lead-generatie kans van de week.
- Stadspagina's bouncen 1,00 als landing op Groningen en Assen; FAQ-link uit sprint 19 mei was het lichte pad, een bel-knop en lichte "informatie"-route maken de tweede stap nog expliciter.
- `projecten.html` had bounce 0,86 en 0,9 s gemiddelde tijd — de pagina was een dood spoor. Klant-akkoord voor echte cases is nog niet binnen, dus voor nu een eerlijke alinea + doorstroom in plaats van leeg laten.
- `calculator_complete`-event is voorwaarde om drop-off in de wizard te kunnen meten; zonder kunnen we de wizard wel zien werken, maar niet zien wáár het beter kan.
- `weekly_trend`-bug blokkeerde alle trend-analyse — pure infrastructuur-fix.

### Verwacht effect (meting per 3 juni 2026)
- ≥1 conversion uit `/contact.html` als landing (was 0).
- Bounce `/contact.html`-landing onder 0,80 (was 1,00).
- Tweede-hit-rate stijgt op stadspagina's; iets minder strakke 1,00 landingsbounce.
- `calculator_complete` verschijnt in GA4 met genoeg events om over 2–4 weken drop-off-analyse te doen.
- Volgende `ga4_fetch.py`-run levert 8 unieke weken in `weekly_trend` zodat trends meetbaar worden.

### Social media deze week (week van 11 mei)
- **LinkedIn (3 posts):** di 12 mei renovatie-opbouw infrezen vs schuimbeton; wo 13 mei prijsindicatie als planningstool; do 14 mei nieuwe Zuidlaren-pagina + Drentse dorpen.
- **Instagram (4 posts):** wo 13 mei schuimbeton onder de vloer; vr 15 mei comfort + opwarmtijd per vloerafwerking; za 16 mei lokaal werken vanuit Zuidlaren; zo 17 mei renovatie Assen.
- **Facebook (1 optionele post):** do 14 mei Zuidlaren-pagina.
- **Drie posts hebben een [FOTO NODIG]-placeholder** — VLWarmte moet beeld aanleveren in `social/input/` voor publicatie.

### Bekende kanttekeningen
- Geen WhatsApp-nummer expliciet bekend, dus contact-keuze gebruikt `sms:+31618817459` met label "stuur een berichtje". Kan later naar `wa.me` zonder UI-aanpassing.
- Smoke tests en `python3 scripts/ga4_fetch.py` konden in de developer-sessie niet draaien (sandbox-restrictie). Hans/PM moet ze handmatig draaien om de GA4-fix te valideren — verwacht 8 unieke weken in `weekly_trend`.

---

## Release — week van 19 mei 2026
**Deployment:** (na push / GitHub Pages — lokaal gevalideerd 02-05-2026)  
**Versie:** zie `git log -1 --oneline` op main na deze release — PM-cyclus: doorstroom FAQ + systemen-CTA + GA4-rapport

### Wat is er veranderd
- **Analytics:** verse GA4-export (`ga4_fetch.py` via project-`.venv`) en bijgewerkt `analytics_report.md` (2 mei).
- **Research & social:** `research_report.md` uitgebreid met PM-cyclus-update 2 mei; nieuwe `social/weekly_calendar.md` voor week 19 mei (LinkedIn/Instagram/Facebook-richting + diepe contact-URL’s).
- **`systemen-producten.html`:** vroege **cta-band** onder de hero naar prijsindicatie + link naar FAQ (korte verblijftijd in GA4 aangepakt).
- **Interne links naar FAQ en wizard:** `diensten.html`, `projecten.html`, `contact.html`, `prijsindicatie.html` met natuurlijke verwijzingen naar `faq.html` (en projecten ook naar prijsindicatie).
- **Stadspagina’s Groningen, Assen, Zuidlaren:** korte FAQ-regel onder de hero-CTA’s.
- **`index.html`:** in stap 2 van “4 stappen” linkt het woord **schuimbeton** naar `diensten.html#schuimbeton`.

### Waarom
Data toonde sterkere home- en contactpatronen, maar **zeer korte tijd** op systemen en **hoge bounce als landing** op stadspagina’s/projecten. FAQ staat live maar had nog weinig meetpad — interne links en vroege CTA’s verlagen de kans op “één hit en weg”.

### Verwacht effect
Meer sessies op `/faq.html`; langere engagement op `/systemen-producten.html`; vaker een tweede pagina per sessie vanaf stadspagina’s.

### Social media deze week
Zie `docs/website-manager/social/weekly_calendar.md` (week van 19 mei 2026).

---

## Release — week van 5 mei 2026
**Deployment:** (na push / GitHub Pages — lokaal gevalideerd 01-05-2026)  
**Versie:** (volgt na commit — werkdirectory sprint Zuidlaren + canonical + CTA’s)

### Wat is er veranderd
- **Nieuwe landingspagina** `vloerverwarming-zuidlaren.html` voor hyperlokale zoekintentie (Zuidlaren + installateur + vloerverwarming), met infrezen-sectie en schema `areaServed` Zuidlaren. In sitemap en footer Regio op alle pagina’s.
- **Sterkere hero-CTA** op de stadspagina’s Groningen en Assen: prijsindicatie, bellen en offerte-dieplink in één regel boven de vouw (`hero-cta-row`).
- **Canonieke home-URL:** logo en menu “Home” linken naar `/` in plaats van `index.html`; README vermeldt het verschil met `file://` lokaal openen.
- **Interne links** vanaf home, over-ons en diensten naar de Zuidlaren-pagina.
- **Prijsindicatie-CTA** op `werkwijze.html` en `systemen-producten.html` via bestaand `cta-band`-patroon.

### Waarom
Analytics en marketing research wezen op Drenthe-volume en het trefwoordcluster rond Zuidlaren; zonder eigen URL bleef dat verkeer op Groningen/Assen-titels landen. Dubbele `/` vs `index.html`-meting en lage engagement op stadspagina’s vroegen om technische en CTA-verbeteringen.

### Verwacht effect
Meetbaar in GA4: sessies op `/vloerverwarming-zuidlaren.html`; in Search Console (na token): queries met “zuidlaren”. Schonere home-rapportage door minder `index.html`-splitsing.

### Social media deze week
Zie `social/weekly_calendar.md`. Suggestie: één post met link naar de nieuwe Zuidlaren-URL na live-gang.

---

## Release — week van 27 april 2026
**Deployment:** 27-04-2026, 09:31 (commit `9e275a4`, GitHub Pages run `24982250357`)
**Versie:** `9e275a4` — "Sprint 27 april: GA4 events, Search Console-tag, twee locatiepagina's, projecten uit nav"

### Wat is er veranderd
- **Conversie-meting werkt nu.** De prijsindicatie-wizard stuurt vijf events naar Google Analytics: starten van de wizard, doorklikken naar stap 2 en 3, klikken op de bereken-knop en het verzenden van een lead. Het contactformulier stuurt een event mee per soort aanvraag (informatie, offerte of terugbelverzoek). Vanaf nu is in GA4 te zien wáár bezoekers afhaken.
- **Twee nieuwe stadspagina's.** `vloerverwarming-groningen.html` en `vloerverwarming-assen.html` zijn live. Beide met lokale plaatsnamen, reistijd vanaf Zuidlaren, een uitleg over infrezen voor renovatie, en doorlinks naar de prijsindicatie. Bedoeld om gevonden te worden op zoekopdrachten als "vloerverwarming Groningen" en "vloerverwarming Assen". Toegevoegd aan footer en sitemap, niet aan de hoofdnavigatie (die werd anders te lang).
- **Search Console klaar voor koppeling.** Op alle 10 productie-pagina's staat nu een placeholder verificatie-tag in de `<head>`. Hans hoeft alleen de echte token uit Search Console te plakken en te pushen, dan is de site geverifieerd.
- **Projectenpagina uit de hoofdnavigatie gehaald.** Zolang er nog geen echte cases met foto en plaatsnaam staan, is een lege projectenpagina een verkeerd signaal. De pagina blijft bestaan voor directe links, maar staat niet meer in de menubalk en niet meer in de sitemap. Bovenaan staat een korte uitleg met verwijzingen naar werkwijze en systemen.

### Waarom
GA4-events: zonder funnel-data weten we niet of de wizard werkt of bezoekers halverwege wegklikken. Stadspagina's: marketing research wijst Groningen en Assen aan als hoogste-ROI combinatie van zoekvolume, koopkracht en concurrentiedruk. Search Console: de site is sinds 26 april live en moet zo snel mogelijk geïndexeerd worden. Projecten uit nav: een pagina die "Straks aan te vullen" zegt schaadt het vertrouwen meer dan dat hij oplevert.

### Verwacht effect
Per 25 mei 2026 willen we in GA4 zien: minimaal één bevestigde wizard-conversie via het lead-event, en in Search Console minstens één van de twee stadspagina's met vertoningen op lokale termen. Dat is het beslismoment voor sprint 4.

### Social media deze week
Zeven posts gepland in `social/weekly_calendar.md`: 3 op LinkedIn (di/wo/do, B2B-toon, focus op detail-vakmanschap, schuimbeton en garantie) en 4 op Instagram (wo/vr/za en wo+1 week, particulier, focus op opgeleverde vloeren, het-werk-onder-de-vloer, het team en de prijscalculator). Alle posts hebben `[FOTO NODIG: ...]`-placeholders — VLWarmte moet zelf nog beeldmateriaal aanleveren in `social/input/` en handmatig publiceren.

---
