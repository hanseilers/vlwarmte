# Sprint — 14 november 2026 (cyclus 26)

**Doel:** bezoekers met een renovatievloer naar passend systeemadvies leiden en beslissen op betrouwbare GA4-data.
**Besluit:** kleine aanpassing van de bestaande systemenpagina; geen nieuwe pagina, calculatorprijs of advertentiebudget. De volledige productmanagercyclus omvat publicatie via GitHub Pages. Ontwikkeling geïsoleerd vanaf lokale main; één eigenaar voor integratie en publicatie: codex · vlwarmte (Werkbank 1805).
**Vorige sprint:** met toestemming bewaard in archive/sprint-2026-11-14.md. Oude foutmeldingen worden opnieuw gecontroleerd.

## Goedgekeurde taken voor Developer Agent

### 1. Zoekintentie en advies op systemenpagina [GOEDGEKEURD]

**Prioriteit:** hoog. **Type:** SEO/content.
**Actie:** H1 benoemt droge vloerverwarming en laagopbouw. Beschrijving en intro maken helder dat de pagina meerdere systemen behandelt. Houd bestaande componenten en logo aan. Geef geen vaste opbouwhoogte, droogtijd of prijs voor onbekende constructies. Stem FAQ-schema af op zichtbare antwoorden zonder rich-resultsbelofte.
**Succes:** één H1; consistente metadescriptions; bezoekers begrijpen waarvoor opname nodig is. Alleen gewijzigde publieks-URL's krijgen een nieuwe sitemapdatum.

### 2. Passende aanvraagroute voor laagopbouw [GOEDGEKEURD]

**Prioriteit:** hoog. **Type:** CTA.
**Actie:** vervang de prijsbelofte bij droge/houten vloeren door systeemadvies via contact.html?modus=informatie#aanvraag. Kies één primaire adviesactie bovenaan, een offerte als tweede actie; vervang de generieke eerste CTA-band en mobiele sticky-actie door passend advies. Verminder herhaalde gelijkwaardige knoppen. Leg in #laagopbouw en kosten-FAQ uit dat de calculator geen aparte droge-opbouwprijs geeft. Geen nieuw formulier en geen prijsrekenwijziging. Browsercontrole toonde dat #aanvraag boven lange uitleg stond en het formulier buiten beeld liet. Verplaats dit bestaande anker naar de moduskeuze vlak boven het formulier; dit hoort bij de werkende adviesroute. Contact.html krijgt daarom ook een nieuwe sitemapdatum.
**Succes:** mobiele/desktop browserjourney opent Informatie en het aanvraagblok; offerte blijft bereikbaar; FAQ werkt met aria-expanded. Geen testbericht naar klanten.

### 3. Betrouwbare terugkerende Analytics-export [GOEDGEKEURD]

**Prioriteit:** hoog. **Type:** meetkwaliteit.
**Actie:** rapporteer exact 30 afgeronde dagen en voorafgaande 30 dagen; filter op publieke productiehost(s), groepeer pagina's zonder titelsplitsing, lever echte totalen en benoemde funnel-/lead-events. Gebruik keyEvents. Rapporteer dat het geen unieke klanten of volledige leadadministratie zijn. Lokale hostmetingen zijn daadwerkelijk gevonden in de huidige property.
**Succes:** echte GA4-export slaagt, 30+30 dagen overlappen niet, productiekanalen sluiten aan op totalen; export blijft gitignored. Geen wijziging aan GA4 key-eventconfiguratie, omdat beide bedoelde events al bestaan.

## Uitgesteld [WACHT]

- GSC-herauthenticatie: invalid_grant; eigenaarlogin nodig, geen nieuwe credentials verzinnen.
- Ads: API staat alleen testaccounts toe; accountstatus niet vast te stellen. Geen campagne- of budgetmutatie.
- Contact-submitregistratie: mail bevat aanvragen die niet allemaal als contact_submit in GA4 staan. Eerst oorzaak onderzoeken; adblock/andere clients blijven mogelijke verklaringen. Geen volledige conversiedekking beloven.
- Nieuwe pagina's en brede metadata-ronde: weinig verkeer, geen gemeten zoektermen; liever bestaande intentie verbeteren.

## Afgewezen [AFGEWEZEN]

- FAQ rich results als groeibelofte; geen aantoonbare groeiverwachting.
- Nogmaals de calculator uitbreiden of bestaande prijzen wijzigen zonder productbesluit.
- Sociale posts automatisch publiceren of klanten automatisch benaderen.

## Social media

Zeven conceptposts voor 16–22 november staan in social/weekly_calendar.md. Echte bronfoto's, handmatige publicatie door VLWarmte.

## Meetdoel en volgende cyclus

Na vier weken: productie-sessies en organische sessies vergelijken met gelijke afgeronde periode; adviesaanvragen naar inhoud beoordelen naast GA4 contact_submit/wizard_lead_submit. Streef naar ten minste één inhoudelijke aanvraag over systeemkeuze; dit is een doel, geen voorspelling. Klein volume laat geen causaal sprintresultaat toe.

## Developer Rapport

Taken 1–3 uitgevoerd. Systeemadvies primair; offerte beschikbaar; geen fictieve droge-opbouwprijs. Bestaand contactanker naar de formulierkeuze verplaatst na een aantoonbaar browserprobleem. Vijf FAQ-antwoorden komen overeen met hun schema. Alleen systemen- en contactpagina hebben nieuwe sitemapdatum.

- Echte GA4-fetch geslaagd; 30+30 dagen aaneensluitend zonder overlap, 62 huidige/54 vorige sessies; kanaalsom gecontroleerd. Key-events blijven ongewijzigd.
- Statische controles: metadata, links en fragmenten, vijf FAQ-antwoorden, sitemap, git diff --check groen. Geen secrets of persoonsgegevens toegevoegd.
- Playwright via geïnstalleerde Chrome op 390×844 en 1440×1000: primaire actie boven de vouw, informatie- en offertemodus, aanvraagformulier in beeld, FAQ aria-expanded, mobiele sticky-actie, geen JS-fouten of horizontale overflow. Screenshots visueel bekeken. Rapport en video's: /tmp/vlwarmte-pm-20261114/local-evidence/.
- Browserbasis 5107258 met dirty wijzigingen contact.html, systemen-producten.html, sitemap.xml en ga4_fetch.py. Publieke anonieme rol; geen login nodig. Geen formulier verzonden; GA-verzoeken tijdens browsercontrole geblokkeerd om testvervuiling te vermijden. Dit bewijst de route, niet Formspree-bezorging of productie-eventontvangst.
- Hergebruik: bestaande CTA-, FAQ- en contactcomponenten; geen CSS/nieuwe user action. Canonieke checkout en .claude/launch.json behouden; geïsoleerde tijdelijke worktree voorkomt overlap met rapportagenten.
- Publicatie: commit 83c0d1ab6bf9da7199f63ff0c9b2f3da7006dd5a geïntegreerd in lokale main, gepusht en succesvol gedeployed: https://github.com/hanseilers/vlwarmte/actions/runs/43611254081. Pages build 1369394438 meldt built op exact deze bron.
- Productie: beide gewijzigde HTML-bestanden byte-voor-byte gelijk aan commit. Dezelfde mobiele/desktop Playwright-journeys opnieuw groen op https://www.vlwarmte.nl, screenshots en video's in /tmp/vlwarmte-pm-20261114/production-evidence/. Rapport noemt broncommit en documentatie-dirty-status; productcode schoon. Geen formulierverzending of GA-hit tijdens deze browsercontrole.
- Lighthouse op live homepage: performance 100, accessibility 100, best practices 100, SEO 100; geen runwaarschuwingen. Eenmalige meting, geen garantie op alle apparaten/pagina's. Rapport: /tmp/vlwarmte-pm-20261114/lighthouse/home.report.html.
- Automatische Formspree-inbox workflow 43611254120 meldt success, maar de test is aantoonbaar overgeslagen wegens ontbrekende GitHub-secrets IMAP_USER/IMAP_PASSWORD. Dit is geen bewijs van bezorging. De echte ontvangen aanvragen zijn hierboven apart gecontroleerd; deze sprint verstuurt geen nieuwe testaanvraag.
- Interne release-notificatie volgens .claude/commands/product-manager.md stap 8b: dry-run gecontroleerd en SMTP-verzending naar jceilers@icloud.com bevestigd. Geen sociale posts gepubliceerd.
- Afsluitende documentatiecommit gebruikt [skip ci] om dezelfde reeds overgeslagen inboxjob niet opnieuw te starten; productcode blijft identiek.
- Volgende meetdiagnose geregistreerd als Werkbank 1806. Geen tracking-backfill of klantcontact uitgevoerd.

## Open voor volgende cyclus

Prioriteit: oorzaak van ontbrekende contact_submit-events vaststellen; klantaanvragen uit mail blijven leidend. Geen automatische klantmail. GSC herauth en Ads API-access apart oplossen. Productacceptatie door Hans blijft open.
