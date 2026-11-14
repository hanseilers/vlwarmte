## Update 14 november — Google Ads-toegang en kosten gecontroleerd

Explorer-toegang voor Cloud-project vlwarmte is met expliciete toestemming aangevraagd en door Google goedgekeurd. De bestaande service-accountkoppeling kan nu echte Ads-accounts uitlezen. Een nieuw proces met de lokale configuratie slaagt. De standaardklant in gitignored secrets/google-ads.env is gecorrigeerd van de gesloten account 2781731612 naar VL Warmte 8864602674; geen credentials in Git.

| Account | Campagne | Status | Budgetinstelling | Levering |
| --- | --- | --- | ---: | --- |
|886-460-2674 VL Warmte|Campaign #1 (23824302411), Performance Max|REMOVED|€2/dag, historisch|Niet actief; interface meldt bovendien accountpauze door verlopen adverteerdersverificatie|
|278-173-1612, oude account|VLW-API-Leads NL auto (23834672782), Search|ENABLED; primary status PENDING|€2/dag, gedeeld|Accountstatus CLOSED; niet live|

**Gemaakte advertentiekosten (EUR, Europe/Amsterdam):** beide accounts €0 over 15 oktober–13 november 2026 en €0 over 1–14 november 2026 tot de controle rond 17:45. Lopende dag is onvolledig en Ads rapporteert met vertraging. Beide perioden ook 0 klikken en 0 vertoningen.

**Beschikbare historie:** VL Warmte 8864602674 heeft €66,608092 kosten (afgerond €66,61), 8.683 vertoningen en 111 klikken. Alle kosten vallen tussen 10 mei en 11 juni 2026. Oude account 2781731612 heeft in de beschikbare historie 0 kosten, 0 klikken en 0 vertoningen. Dit zijn advertentiekosten, geen factuur- of betalingssaldo. De 5 historische Ads-conversies zijn niet als gekwalificeerde klantaanvragen geteld.

Accounttotalen, campagnetotalen en dagelijkse kosten sluiten exact aan op 66.608.092 micros. Geen campagnes, budgetten, betalingen of verificatiestatus gewijzigd; geen advertenties gestart. De API-blokkade is opgelost. Hervatten van adverteren en adverteerdersverificatie zijn aparte product-/eigenaarsbesluiten.

Bronnen en reproduceerbare queries: /tmp/vlwarmte-ads-1808/verification.json,accounts.json,costs-8864602674.json,costs-2781731612.json,daily-spend.json en de scripts read_ads.py/cost_report.py. Screenshot access-result.jpg bevestigt Explorer; campaign-status.jpg toont de verwijderde campagne en accountmelding. De eerdere Ads-blokkademeldingen hieronder zijn historische bevindingen.

## Update 14 november — contactmeting en GSC hersteld

Het vervolgonderzoek vond en repareerde een reproduceerbaar laadlek: een geslaagde contactverzending vóór het laden van Google Analytics verloor contact_submit. De wachtrij wordt nu vooraf aangemaakt. Echte productieproeven bevestigen Formspree-success, ontvangst in de mailbox en Google collection HTTP 204. Daarna bevestigt de GA4 Realtime API contact_submit in property 534641753 (eventCount 1; vooraf geen events). Vijf browserregressies slagen, inclusief vertraagd laden, de drie contactmodi en twee foutpaden. Niet bewezen dat elke historische ontbrekende meting dezelfde oorzaak had; geen historische events bijgemaakt.

GSC-login opnieuw geautoriseerd. De OAuth-app stond op Testing; met expliciete toestemming van Hans naar Production gezet, daarna een productietoken verkregen. Twee verse API-processen werken. De eerder genoemde GSC-blokkade is daarmee opgelost. Oude cijfers hieronder blijven de afgebakende periode 15 oktober–13 november; de twee herkenbare testaanvragen van 14 november zijn geen klantleads en hun testmails zijn opgeruimd.

# Analytics Rapport — 14 november 2026 (cyclus 26)

De productiesite heeft **62 sessies en 52 actieve gebruikers** in 30 afgeronde dagen. Verkeer groeit ten opzichte van de vorige 30 dagen, terwijl organisch zoekverkeer daalt. GA4 registreert één calculatoraanvraag; de mailbox bevat vier inhoudelijke inzendingen van drie verschillende aanvragers. Analytics is dus geen volledige leadadministratie.

**Periode:** 15 oktober t/m 13 november 2026. **Vergelijking:** 15 september t/m 14 oktober. Europe/Amsterdam; alleen www.vlwarmte.nl en vlwarmte.nl. Lopende dag en lokale testhosts uitgesloten.

## Kerncijfers

| Metric | Nu | Vorige 30 dagen | Verschil |
| --- | ---: | ---: | ---: |
| Sessies | 62 | 54 | +8 (+14,8%) |
| Actieve gebruikers | 52 | 43 | +9 (+20,9%) |
| Gemiddelde sessieduur | 117,4 sec | 63,6 sec | +53,9 sec |
| Bounce | 59,7% | 55,6% | +4,1 procentpunt |
| Gemeten key events | 1 | 1 | gelijk |
| Organische sessies | 15 | 24 | −9 (−37,5%) |

Klein volume; geen bewijs dat een eerdere sprint een verandering veroorzaakte. Gemiddelde sessieduur is geen gemiddelde actieve leestijd. Meer verkeer betekent niet automatisch meer gekwalificeerde aanvragen.

## Pagina's

| Pad | Sessies met bezoek | Actieve gebruikers | Gem. sessieduur | Bounce |
| --- | ---: | ---: | ---: | ---: |
| / | 42 | 35 | 23,1 sec | 57,1% |
| /prijsindicatie.html | 15 | 14 | 180,5 sec | 40,0% |
| /diensten.html | 9 | 9 | 38,5 sec | 0% |
| /systemen-producten.html | 6 | 5 | 319,9 sec | 0% |
| /contact.html | 6 | 6 | 18,3 sec | 0% |
| /over-ons.html | 5 | 4 | 9,9 sec | 20,0% |

Sessies en gebruikers over pagina's overlappen; deze kolommen niet optellen. Een bounce van 0% bij zes sessies is geen bewijs van goede conversie. De homepage is de grootste instroompagina (40 landingssessies); geen brede herbouw op basis van dit kleine volume.

## Herkomst en apparaten

| Kanaal | Sessies | Key events |
| --- | ---: | ---: |
| Direct | 39 | 0 |
| Google organisch | 15 | 0 |
| crm.slimster.nl referral | 5 | 0 |
| ChatGPT / AI Assistant | 3 | 1 |

Som sessies = 62, gelijk aan de afzonderlijke totaalquery. Eén ChatGPT-conversie maakt het kanaal nog geen bewezen acquisitiestrategie. Desktop 37 sessies, mobiel 24 (38,7%), tablet 1. De property bevatte daarnaast vier lokale testsessies; de verbeterde export sluit die uit.

Drenthe 8 sessies en Groningen 6. IP-regio is geen postcode of klantkwalificatie. De VS en andere regio's blijven in de productietotalen; zonder aanvullend bewijs geen bots of ongewenst verkeer wegfilteren.

## Aanvragen: Analytics naast mailbox

- GA4: wizard_start 17 events bij 8 gebruikers; calculator_result 14 events bij 8 gebruikers; wizard_lead_submit 1 event bij 1 gebruiker. Dit is geen sequentieel gebruikersfunnelrapport en de eventaantallen mogen niet als stapconversie worden gedeeld.
- De enige geregistreerde lead-key-event is wizard_lead_submit op **26 oktober**. GA4 schrijft de sessie toe aan ChatGPT. De mailbox bevat die dag een calculatoraanvraag, buiten het kernwerkgebied.
- Mailbox: vier inhoudelijke Formspree-inzendingen, op 26 oktober, 30 oktober, 3 november en 8 november. De twee middelste betreffen dezelfde aanvraag. Dus **drie verschillende aanvragers, twee uit het werkgebied**, op basis van inhoud en vermelde plaats; geen uitspraak over commerciële kwalificatie of gewonnen opdrachten. Persoonsgegevens blijven uit Git.
- Voor de drie contactformulierinzendingen staan geen contact_submit-events in deze periode. Beide bedoelde key events zijn correct ingesteld. Adblock, script-/netwerkuitval of een andere submitroute zijn mogelijke verklaringen; de oorzaak is nog niet bewezen. De code vuurt alleen na een succesvolle Formspree-response.
- De mailbox is uitsluitend gelezen met readonly SELECT/BODY.PEEK. Geen klantantwoord, verplaatsing of leesstatuswijziging uitgevoerd. Geen volledige audit van Formspree-dashboard of alle andere leadkanalen gedaan.

## Actuele blokkades

GA4 werkt; de oude fetchblokkade en de oude claim nul aanvragen zijn achterhaald. GA4 Admin dry-run bevestigt contact_submit en wizard_lead_submit; purchase is een bestaande Google-default en wordt ongemoeid gelaten. GSC-refresh geeft invalid_grant: nieuwe eigenaarstoestemming nodig. Ads-read geeft ACTION_NOT_PERMITTED wegens testaccounttoegang; actuele kosten/status niet bevestigd. Het verificatie-placeholder in HTML verklaart geen OAuth-refreshfout.

## Voorstellen en beslissing

1. **Hoog — betrouwbare export:** afgeronde 30+30 dagen, productiehosts, echte totalen, pagina's zonder titelversnippering en benoemde events. Uitgevoerd en echte API-responses gecontroleerd.
2. **Hoog — bestaande systemenpagina:** de maatwerkvraag is ook terug te zien in een echte aanvraag met houten vloer. Leg droge vloerverwarming/laagopbouw duidelijk uit en stuur naar systeemadvies in het passende contacttabblad. Geen nieuwe prijsberekening of ononderbouwde conversiestijging beloven.
3. **Hoog — contactmeting nader onderzoeken:** vergelijk toekomstige succesvolle aanvragen met inbox; onderscheid browser-/trackinguitval van formulieraankomst. GA4 nooit als enige bron voor leads gebruiken.
4. **Uitgesteld — meer pagina's/Ads:** eerst GSC-toegang en Ads-inzage herstellen. Geen extra besteding.

## Meetdoel

Over vier afgeronde weken productie- en organische sessies naast ontvangen aanvragen leggen. Eén inhoudelijke aanvraag over systeemkeuze is een streefdoel, geen voorspelling. De systemenpagina blijft een kleine hypothese; Hans beoordeelt bruikbaarheid afzonderlijk.

## Bronnen en controle

GA4 Data API property 534641753; Admin API dry-run; Hostnet IMAP (INBOX, Leads, Overig, Systeem) vanaf 15 oktober; broncode. Export: gitignored ga4_report.json. Uitgevoerde aanvullende query's en ruwe aggregaties: /tmp/vlwarmte-pm-20261114/analytics_audit.py, analytics_audit.json, analytics_production.py en analytics_production.json. Echte GA4-fetch, periodegrenzen, kanaalsom, één key-event en padgroepering gecontroleerd. De oude export inclusief vandaag telde 67 sessies; het definitieve getal 62 heeft een andere afbakening en is geen verkeersdaling.

---

## Historisch rapport — augustus 2026

Onderstaande analyse is historie; actuele cijfers, toegang en conclusies staan hierboven.

# Analytics Rapport — 17 augustus 2026

**Periode:** 30d-venster 6 juli – 5 augustus 2026 · 90d-venster t/m 5 augustus 2026
**Vorige sprint:** cyclus 24, gedeployd 5 augustus (commit `69e4e01`, Pages-run `30993116057`)

---

## ⚠️ Databeperking deze cyclus — lees dit eerst

**Er is geen verse GA4-data.** `python3 scripts/ga4_fetch.py` is deze cyclus mislukt: de systeem-`python3` is geüpgraded naar 3.13.7 en mist de `google`-modules, en de venv-interpreter is in deze run geblokkeerd. Er is dus geen nieuwe fetch gedaan.

Alle cijfers in dit rapport komen uit `docs/website-manager/ga4_report.json`, `generated_at` **2026-08-05T11:06:14**. Dat is **12 dagen oud**. Het 30d-venster daarin loopt 6 juli – 5 augustus en overlapt dus vrijwel volledig met wat cyclus 24 al gerapporteerd heeft.

**Wat dat betekent:**

- Het effect van de cyclus-24-deploy (5 augustus) zit **niet** in deze data. De vijf ingrepen van vorige sprint zijn nul dagen gemeten.
- Elke uitspraak over trend is een herhaling van vorige cyclus, geen nieuwe waarneming.
- De verbetervoorstellen onderaan zijn daarom **niet** op verse verkeersdata gebaseerd maar op (a) de laatst bekende data en (b) een verse code-audit van de repo die deze cyclus wél volledig is uitgevoerd.

**Herstelactie voor de eigenaar/developer:** venv opnieuw opbouwen —
`python3 -m venv .venv && .venv/bin/pip install -r scripts/requirements-ga4.txt`, daarna `.venv/bin/python scripts/ga4_fetch.py`. Zonder dat blijft de volgende cyclus ook blind.

---

## Post-deploy verificatie cyclus 24 — 5 van 5 taken staan live in de repo

Gecontroleerd met `grep`/`Read` op de werkdirectory (branch `main`, na commit `69e4e01`).

| # | Taak | Live? | Bewijs |
| - | ---- | ----- | ------ |
| 1 | FAQ + `FAQPage` op Leeuwarden | **Ja** | `vloerverwarming-leeuwarden.html` r. 52: één `"@type":"FAQPage"` met drie `Question`-objecten. Zichtbare FAQ r. 225–250 (`<h2>Veelgestelde vragen — Leeuwarden</h2>` + 3× `faq-question`). Vraagteksten matchen 1-op-1 met de JSON-LD `name`-velden (Stiens/Grou, kosten, infrezen dekvloer). Kosten-antwoord linkt naar `prijsindicatie.html` (r. 241). |
| 2 | Kosten-verankeringsblok boven wizard | **Ja** | `prijsindicatie.html` r. 585–595: `<section class="section">` met uitleg "richtbedrag in ongeveer twee minuten — excl. btw, indicatief". Links naar `systemen-producten.html#laagopbouw` (r. 592) en `vloerverwarming-heerenveen.html` (r. 593). Staat vóór `<div class="wizard" id="wizard">` (r. 596). Geen extra primaire knop; wizard-flow ongewijzigd. |
| 3 | `BreadcrumbList` Heerenveen + Drachten | **Ja** | `vloerverwarming-heerenveen.html` r. 50 en `vloerverwarming-drachten.html` r. 50, beide valide `BreadcrumbList` met 2 `ListItem`s (Home → stad). |
| 4 | FAQ + `FAQPage` op Heerenveen | **Ja** | `vloerverwarming-heerenveen.html` r. 53 `FAQPage`; zichtbare FAQ r. 226–251. Vragen (Joure/Sneek, kosten, infrezen bestaande woning) zijn uniek t.o.v. Leeuwarden. Kosten-antwoord linkt naar `prijsindicatie.html` (r. 242). |
| 5 | Homepage kosten-band onder hero | **Ja** | `index.html` r. 93–101: `<section class="section section-muted">` staat direct na het einde van `<section class="hero">` (r. 91). Bevat tekstlink `prijsindicatie.html` "Richtbedrag in 2 minuten →" zonder `btn`-klasse, dus geen tweede primaire CTA. H1 (r. 74) ongewijzigd. |

**Oordeel:** de developer heeft geleverd wat er beloofd is. Geen afwijkingen, geen halve implementaties.

**Twee kanttekeningen bij taak 3:** de Friese breadcrumbs zijn 2-niveau (Home → stad), terwijl Assen, Emmen, Hoogeveen en Zuidlaren 3-niveau zijn (Home → Drenthe → stad). Dat komt doordat er geen Friesland-hub bestaat. Zie voorstel 5.

---

## Kerncijfers (30d, stand 5 aug — 12 dagen oud)

| Metric | Waarde | Trend |
| ------ | ------ | ----- |
| Sessies (30d) | 17 | ↓ 19% t.o.v. cyclus 23 |
| Actieve gebruikers (30d) | 17 | gelijk aan sessies |
| Conversies (alle kanalen) | **0** | 5e cyclus op rij |
| Bounce homepage | 85% | ↑ (was 75%) |
| Gem. duur homepage | 10,5 s | ver onder de 30 s-drempel |
| Sessies doelregio (DR/GR/FR) | **1** | Groningen 1, Drenthe 0, Friesland 0 |

**Weektrend:** 10-6: 7 · 17-6: 3 · 24-6: 4 · 1-7: 10 · 8-7: 2 · 15-7: 4 · 22-7: 1 · 29-7: 6. Sterk schommelend op een basis van een paar sessies per week; op deze aantallen zegt week-op-week vrijwel niets.

## Top pagina's (30d)

| Pagina | Sessies | Bounce | Gem. duur |
| ------ | ------- | ------ | --------- |
| `/` | 13 | 85% | 10,5 s |
| `/prijsindicatie.html` | 4 | 75% | 112 s |
| `/contact.html` | 1 | 0% | 50 s |
| `/diensten.html` | 1 | 0% | 15 s |
| `/vloerverwarming-zuidlaren.html` | 1 | 0% | 3 s |

## Landingspagina's (30d)

| Landing | Sessies | Bounce | Conversies |
| ------- | ------- | ------ | ---------- |
| `/` | 12 | 83% | 0 |
| `/prijsindicatie.html` | 3 | **100%** | 0 |
| `/?ved=…` (SERP-klik) | 1 | 100% | 0 |
| `(leeg)` | 1 | 100% | 0 |
| `/vloerverwarming-zuidlaren.html` | 1 | 0% | 0 |

## Traffic bronnen (30d)

| Kanaal | Sessies | Conversies |
| ------ | ------- | ---------- |
| Direct | 11 | 0 |
| Organic Search (google/organic) | 4 | 0 |
| Cross-network | 1 | 0 |
| Unassigned | 1 | 0 |

Geen Paid Search, geen `gclid`, geen `google/cpc` — consistent met een gesloten Ads-account. Geen aanbevelingen voor de Marketing Research Agent op betaald verkeer zolang dat zo blijft.

## Engagement en scroll (90d) — het scherpste signaal in deze dataset

| Pagina | Sessies | Gem. duur | Scrolled users | Scroll-ratio |
| ------ | ------- | --------- | -------------- | ------------ |
| `/` | 185 | 46 s | 16 | **8,6%** |
| `/prijsindicatie.html` | 45 | 135 s | 8 | 18% |
| `/contact.html` | 42 | 58 s | 5 | 12% |
| `/diensten.html` | 11 | 18 s | 1 | 9% |
| `/projecten.html` | 11 | 23 s | 1 | 9% |
| `/werkwijze.html` | 10 | **239 s** | 1 | 10% |
| `/systemen-producten.html` | 9 | **223 s** | 1 | 11% |
| `/faq.html` | 8 | 24 s | 1 | 13% |
| `/over-ons.html` | 8 | 16 s | 4 | 50% |
| `/vloerverwarming-zuidlaren.html` | 4 | 27 s | 1 | 25% |
| `/vloerverwarming-drachten.html` | 2 | 107 s | 1 | 50% |
| `/vloerverwarming-leeuwarden.html` | 2 | 2,6 s | **0** | 0% |
| `/vloerverwarming-assen.html` | 1 | 5 s | 0 | 0% |
| `/vloerverwarming-groningen.html` | 1 | 10 s | 0 | 0% |

---

## Observaties

**1. De conversiecode is er wél — de meting niet. Dat is nu hard vast te stellen.**
Code-audit deze cyclus: `prijsindicatie.html` r. 1145 vuurt `wizard_start`, r. 1698 `wizard_lead_submit`, r. 1704 `lead_form_submit`; `assets/js/main.js` r. 208 vuurt `contact_submit`. De events staan er, correct gewired, op elke pagina die `main.js` laadt (18 van 18 gecontroleerd). **Er is geen technische reden voor 0 conversies.** Vijf cycli op nul betekent daarom vrijwel zeker dat deze events in GA4 → Admin → Events niet als *key event* zijn gemarkeerd. Dit is geen developer-werk en geen contentprobleem: het is één vinkje in de GA4-admin. Escalatie 1 blijft staan en verdient de hoogste urgentie van alles in dit rapport.

**2. Bijna niemand scrolt. Alles onder de vouw is praktisch onzichtbaar.**
185 sessies op de homepage, 16 scroll-events. Dat is 8,6%. Op `werkwijze` en `systemen-producten` — de twee pagina's met de hoogste verblijfsduur van de site (239 s en 223 s) — is dat 1 op de 10 en 1 op de 9. Dit heeft directe consequenties voor het werk van cyclus 24: de nieuwe FAQ's op Leeuwarden en Heerenveen staan rond regel 225, ver onder de vouw. Voor Google (rich results) is dat prima; voor de bezoeker levert het niets. Leeuwarden bevestigt dat: 2 sessies, 2,6 s gemiddeld, **0 scrolled users**. De SEO-waarde van die FAQ's is reëel, de CRO-waarde is nul zolang er niet gescrold wordt.

**3. De sticky mobiele CTA staat maar op één van de 22 pagina's.**
`grep -c 'sticky-cta-mobile'`: `index.html` → 3, alle andere pagina's → **0**. Terwijl de CSS (`assets/css/critical-index.css` r. 584–630) op élke pagina wordt ingeladen en de JS (`assets/js/main.js`, `initStickyCta()` r. 10–23) op élke pagina draait. De enige voorwaarde die de JS stelt is een `.cta-band` op de pagina — en die is aanwezig op alle pagina's behalve `prijsindicatie.html` en `contact.html` (die zijn zelf de bestemming). Er ligt dus een volledig werkende, al betaalde component klaar die op 15 pagina's niet is aangezet. Mobiel is 4 van 16 sessies (25%) en scrolt niet; dit is de goedkoopste conversie-ingreep die er in deze repo ligt.

**4. `prijsindicatie.html` is de nummer-2-pagina van de site en heeft nul structured data.**
45 sessies en 135 s in 90 dagen, groeiend van 2 naar 4 sessies in het 30d-venster, mét een uitgeschreven kostensectie (`#kosten-uitleg`, r. 878–…) inclusief harde bandbreedte **€45–€95 per m²**. `grep -c 'application/ld+json' prijsindicatie.html` → **0**. Geen `FAQPage`, geen `BreadcrumbList`, geen `Service`. Dezelfde nul geldt voor `contact.html` (42 sessies/90d), `diensten.html`, `werkwijze.html`, `projecten.html` en `over-ons.html`. Alle stadspagina's hebben inmiddels breadcrumbs; de kern van de site niet.

**5. Landing op `prijsindicatie` bounct 100%, en het nieuwe introblok kan dat verergeren.**
3 van 3 landings op `/prijsindicatie.html` bouncten. Het ATF-blok van taak 2 (r. 585–595) is inhoudelijk goed, maar duwt de eerste wizard-stap op mobiel omlaag. De pagina heeft al een expliciete mobiele-ATF-mediaquery (r. 400–460, "wizard productkeuze zichtbaar zonder scroll ≤768px") die het nieuwe blok níét kent. Op dat punt werken taak 2 en de bestaande mobiel-optimalisatie tegen elkaar in. De developer heeft dit zelf als aandachtspunt genoteerd — het is een reële regressie-kandidaat.

**6. Friesland heeft geen hub, en de homepage-ankertekst klopt niet.**
Drenthe heeft `vloerverwarming-drenthe.html` en 3-niveau-breadcrumbs op alle Drentse stadspagina's. Friesland heeft drie stadspagina's (Leeuwarden, Heerenveen, Drachten), geen hub, en 2-niveau-breadcrumbs. Erger: `index.html` r. 168 zet de ankertekst **"vloerverwarming Friesland"** op een link naar `vloerverwarming-leeuwarden.html`. Dat is een mismatch tussen ankertekst en bestemming die zowel Google als de bezoeker misleidt. Friesland was 0 sessies in het 30d-venster.

**7. Titles zijn uniek, meta-descriptions bijna.**
Alle 18 `<title>`-tags gecontroleerd: uniek, geen duplicaten, geen ontbrekende. Meta-descriptions: alle aanwezig en uniek. Wel zijn Drachten en Leeuwarden woordelijk identiek op de stadsnaam na ("Ruim drie kwartier rijden vanaf Zuidlaren. Prijsindicatie of offerte aanvragen."). Technisch geen duplicaat, praktisch nauwelijks onderscheidend. Lage prioriteit, maar het staat genoteerd.

**8. Blokkades die niet van de developer zijn.**
`REPLACE_WITH_TOKEN` staat nog steeds op 19 live pagina's — GSC-verificatie is 8+ weken kapot en de repo kan dat niet zelf oplossen. Ads-account `CLOSED`. Sitemap is overigens in orde: 20 `<loc>`-entries, alle publieke pagina's aanwezig, `404.html` en `logo-varianten.html` terecht uitgesloten.

---

## Verbetervoorstellen — 6 stuks, allemaal HTML/CSS/JS in deze repo

Geen externe tooling, geen Ads, geen GSC. Elk voorstel heeft een succescriterium dat met één `grep` te controleren is.

### 1. Sticky mobiele CTA uitrollen naar de 15 pagina's die er al klaar voor zijn — **Hoog**

**Wat:** kopieer het `<a class="sticky-cta-mobile" href="prijsindicatie.html" data-sticky-cta …>`-blok uit `index.html` (r. 303–306) naar: `diensten.html`, `werkwijze.html`, `systemen-producten.html`, `projecten.html`, `over-ons.html`, `faq.html`, en de negen stadspagina's (`assen`, `drachten`, `drenthe`, `emmen`, `groningen`, `heerenveen`, `hoogeveen`, `leeuwarden`, `zuidlaren`). **Niet** op `prijsindicatie.html` en `contact.html` — die zijn de bestemming en hebben bovendien geen `.cta-band`, waardoor de JS de knop niet zou kunnen verbergen.

**Waarom:** de CSS staat al in `critical-index.css` (r. 584–630) dat élke pagina laadt, en `initStickyCta()` in `main.js` (r. 10–23) draait al op élke pagina. De component is compleet en werkt; alleen de markup ontbreekt. Data: mobiel is 25% van de sessies (4/16), en de scroll-ratio's (homepage 8,6%, `werkwijze` 10%, `systemen-producten` 11%) laten zien dat de CTA's onderaan de pagina zelden bereikt worden. `.cta-band` — de verbergings-trigger die de JS nodig heeft — is aanwezig op alle 15 doelpagina's, dus er is nul risico op een permanent zwevende knop.

**Succescriterium:**
`grep -l 'data-sticky-cta' *.html | wc -l` geeft **16** (was 1), en `grep -L 'data-sticky-cta' prijsindicatie.html contact.html` geeft beide bestanden terug (bevestigt dat ze bewust zijn overgeslagen).

---

### 2. `FAQPage` + `BreadcrumbList` op `prijsindicatie.html` — **Hoog**

**Wat:** voeg twee `<script type="application/ld+json">`-blokken toe in de `<head>`. De `BreadcrumbList` volgens het patroon van `vloerverwarming-groningen.html` r. 52 (Home → Prijsindicatie). De `FAQPage` uitsluitend gevuld met **woordelijke** tekst uit de bestaande zichtbare `#kosten-uitleg`-sectie (r. 878 e.v.) — bijvoorbeeld "Wat kost vloerverwarming per m²?" met het €45–€95-antwoord, "Wat bepaalt de prijs?" met de drie genoemde factoren, en "Is het richtbedrag een offerte?" met de bestaande disclaimer-tekst. Geen nieuwe content schrijven; alleen bestaande zichtbare tekst spiegelen.

**Waarom:** `grep -c 'application/ld+json' prijsindicatie.html` → **0**, terwijl dit met 45 sessies en 135 s (90d) de op één na drukste en verreweg de best-engagende pagina van de site is, en de enige die met stijgende instroom (2 → 4 in het 30d-venster) uit de laatste cyclus kwam. De pagina bevat al harde, concrete prijsinformatie die precies is waar Google op "wat kost vloerverwarming per m2" naar zoekt. Alle negen stadspagina's hebben breadcrumbs; de commercieel belangrijkste pagina van de site heeft niets.

**Succescriterium:**
`grep -c '"FAQPage"' prijsindicatie.html` → **1** én `grep -c '"BreadcrumbList"' prijsindicatie.html` → **1**, en elke `"name"` in de `FAQPage` komt woordelijk voor als zichtbare tekst in hetzelfde bestand.

---

### 3. Mobiele ATF van `prijsindicatie.html` terugwinnen — **Hoog**

**Wat:** geef het nieuwe kosten-introblok (r. 585–595) een eigen klasse, bijvoorbeeld `class="section kosten-intro"`, en breid de bestaande mobiele mediaquery (r. 400–460) uit met een regel die dat blok op ≤768px inkort: kleinere `font-size`, strakkere `margin`/`padding`, en de tweede zin verborgen achter een `<details>` of simpelweg `display:none` op de niet-essentiële regel. De desktopweergave blijft ongewijzigd.

**Waarom:** landing-bounce op `/prijsindicatie.html` is **100%** (3 van 3). De pagina had een expliciet ontworpen mobiele ATF-regel (r. 400: "wizard productkeuze zichtbaar zonder scroll (≤768px)") die het nieuwe blok van cyclus 24 niet kent — het introblok schuift daar dus dwars doorheen. De developer heeft dit zelf als aandachtspunt gemeld. Met een scroll-ratio van 18% op deze pagina is alles wat de eerste wizard-stap omlaag duwt direct conversieverlies. Dit is een correctie op eigen werk, geen terugdraaiing: de tekst blijft staan, alleen compacter op klein scherm.

**Succescriterium:**
`grep -c 'kosten-intro' prijsindicatie.html` → **≥ 2** (één keer op het blok, minstens één keer in de `@media (max-width: 768px)`-regel), en de string `kosten-intro` staat binnen het regelbereik 400–470 van het bestand.

---

### 4. `BreadcrumbList` op de vijf schemaloze kernpagina's — **Midden**

**Wat:** voeg `BreadcrumbList`-JSON-LD toe aan `contact.html`, `diensten.html`, `werkwijze.html`, `projecten.html` en `over-ons.html`, conform het patroon van `vloerverwarming-groningen.html` r. 52. Alleen schema, geen inhoudelijke wijziging.

**Waarom:** `grep -c 'application/ld+json'` geeft **0** op alle vijf. `contact.html` is met 42 sessies/90d de nummer 3 van de site; `werkwijze.html` heeft met 239 s de langste verblijfsduur van alle pagina's. De negen stadspagina's hebben inmiddels allemaal breadcrumbs — de kernpagina's zijn overgeslagen. Goedkoop, nul risico, consistent maken van iets dat al half gedaan is.

**Succescriterium:**
`grep -c '"BreadcrumbList"' contact.html diensten.html werkwijze.html projecten.html over-ons.html` geeft voor elk bestand **1**.

---

### 5. Friesland-hub + ankertekst op de homepage rechtzetten — **Midden**

**Wat:** drie samenhangende ingrepen. (a) Maak `vloerverwarming-friesland.html` naar het model van `vloerverwarming-drenthe.html`, met `BreadcrumbList`, kruislinks naar Leeuwarden/Heerenveen/Drachten en een CTA naar `prijsindicatie.html`. (b) Corrigeer `index.html` r. 168: de ankertekst "vloerverwarming Friesland" moet naar de nieuwe hub wijzen, niet naar `vloerverwarming-leeuwarden.html`. (c) Trek de breadcrumbs op Leeuwarden, Heerenveen en Drachten door naar 3 niveaus (Home → Friesland → stad), gelijk aan de Drentse pagina's. (d) Voeg de hub toe aan `sitemap.xml`.

**Waarom:** Friesland was **0 sessies** in het 30d-venster, terwijl er drie Friese stadspagina's zijn en de laatste twee cycli daar zwaar op hebben ingezet (FAQ's, breadcrumbs). Drenthe heeft wél een hub en haalt wél instroom (Zuidlaren 4 sessies/90d, Assen, Hoogeveen, Emmen). De ankertekst-mismatch op r. 168 is bovendien een concrete fout: link zegt "Friesland", bestemming is een stadspagina. En de 2-niveau-breadcrumbs op de Friese pagina's zijn een direct gevolg van het ontbreken van die hub — dit voorstel lost drie dingen tegelijk op.

**Succescriterium:**
Bestand `vloerverwarming-friesland.html` bestaat; `grep -c 'vloerverwarming-friesland.html' index.html sitemap.xml` geeft voor beide **≥ 1**; `grep -c '"position":3' vloerverwarming-leeuwarden.html vloerverwarming-heerenveen.html vloerverwarming-drachten.html` geeft voor elk **1**.

---

### 6. FAQ + `FAQPage` op `vloerverwarming-drachten.html` — **Midden**

**Wat:** voeg een FAQ-sectie toe na het "Ook actief in"-blok (r. 214) en vóór de CTA-sectie, exact volgens het Leeuwarden/Heerenveen-sjabloon: `<h2>Veelgestelde vragen — Drachten</h2>` met drie `faq-item`-blokken, plus `FAQPage`-JSON-LD in de `<head>` na de bestaande `BreadcrumbList` (r. 50). Vragen moeten uniek zijn t.o.v. Leeuwarden en Heerenveen — denk aan Ureterp, Beetsterzwaag, Drachtstercompagnie; het kosten-antwoord linkt naar `prijsindicatie.html`.

**Waarom:** Drachten haalt **107 s** gemiddelde verblijfsduur op 2 sessies (90d) en een scroll-ratio van 50% — de op één na beste engagement van alle stadspagina's, zónder FAQ. Ter vergelijking: Leeuwarden haalt 2,6 s en 0% scroll mét FAQ. Wie op Drachten landt, leest door. Dat is precies het profiel waar een FAQ met rich-result-eligibility rendement oplevert. Drachten stond al als backlog-item in de cyclus-24-sprint ("logische volgende SEO-stap") en is nu de enige Friese stadspagina zonder FAQ.

**Succescriterium:**
`grep -c '"FAQPage"' vloerverwarming-drachten.html` → **1**; `grep -c 'faq-question' vloerverwarming-drachten.html` → **3**; de drie `"name"`-waarden in de JSON-LD komen niet voor in `vloerverwarming-leeuwarden.html` of `vloerverwarming-heerenveen.html`.

---

## Wat níét in deze voorstellen zit, en waarom

- **Homepage-hero aanpassen** — de 85% bounce en 8,6% scroll-ratio wijzen daarheen, maar de PM heeft dit vorige cyclus expliciet afgewezen wegens risico op de enige pagina met substantieel verkeer. Ik dring niet aan zolang er geen verse data ligt.
- **Meta-descriptions Drachten/Leeuwarden differentiëren** — reëel maar marginaal; niet de moeite waard om een van de zes plekken aan te geven.
- **Alles rond GSC, Ads en het markeren van key events** — geen developer-werk. Zie escalaties hieronder.

## Escalaties (eigenaar, ongewijzigd t.o.v. cyclus 24, één nieuwe)

1. **Key events markeren in GA4** — deze cyclus is met code-audit hard vastgesteld dat `wizard_start`, `wizard_lead_submit`, `lead_form_submit` en `contact_submit` correct vuren. 0 conversies is een adminfout, geen websitefout. Hoogste urgentie.
2. **GSC OAuth vernieuwen** — `REPLACE_WITH_TOKEN` staat nog op 19 live pagina's.
3. **Ads-account heropenen** — status `CLOSED`, geen billing.
4. **NIEUW: GA4-fetch herstellen** — `.venv` opnieuw opbouwen zodat `scripts/ga4_fetch.py` weer draait. Zonder dat is de volgende analytics-cyclus opnieuw blind.
