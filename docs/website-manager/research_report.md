# Marketing Research Rapport — 13 juli 2026 (cyclus 22)

Bron: verse analytics-context (30d per 13 jul 2026), vorig rapport (6 jul / cyclus 21),
sitemap-scan van de root-HTML, en een gerichte structured-data- en internal-linking-audit
van alle stadspagina's + hubs. Vakkennis Noord-Nederlandse vloerverwarmingsmarkt.

> **Beperkingen deze cyclus (autonome run zonder live tools):**
> geen WebSearch, geen Bash-loops/netwerk, geen Google Ads-scripts, geen GSC-fetch.
> **Alle zoekvolumes hieronder zijn indicatief/geschat** — marktkennis + prior research,
> geen live keyword-tool. Ads-adviezen zijn **escalatie voor de eigenaar**, geen autonome
> actie. GSC blijft geblokkeerd (`invalid_grant`, 6+ weken oud) — escalatie.

## Samenvatting

Instroom is en blijft het dominante knelpunt en verslechtert: ~22 sessies/30d (was 34),
de week 6–12 jul telde **4 sessies — de laagste ooit**, en 0 conversies over alle kanalen
voor de derde cyclus op rij. Ads levert vrijwel niets meer (cpc = 1 sessie). Organisch
google draagt nog 8 sessies; dat is het enige kanaal met enig fundament, en dus de plek
waar traffic-onafhankelijke winst te halen is.

De audit legt vier **schone, meetklok-veilige** organische hefbomen bloot die instroom
kunnen verhogen zonder de rijpende cyclus-20/21-pagina's aan te raken:
**(1)** een **sitemap-signaalgat** — de op 6 jul refactorde Drachten-pagina draagt nog
`<lastmod>2026-05-22`, dus Google krijgt geen crawl-signaal dat de cyclus-21-wijziging
bestaat; **(2)** een **FAQPage-schema-gat** — van de negen stadspagina's heeft alléén
Hoogeveen een lokale FAQ-sectie met `FAQPage`-schema; de andere acht missen die volledig,
terwijl het een bewezen sjabloon in eigen huis is; **(3)** **geen enkele** pagina heeft
`BreadcrumbList`-schema; **(4)** de contextuele "Ook actief in"-blokken kruislinken de
diepe stadspagina's onvolledig. Alle vier raken **oudere** pagina's of sitemap-metadata,
niet Heerenveen (cyclus 20) of Drachten (cyclus 21).

## Top zoekwoorden

| Zoekwoord | Volume (indicatie) | Concurrentie | Pagina / actie |
|-----------|-------------------|--------------|----------------|
| vloerverwarming groningen installateur | midden | midden (ReWo, Kentech, Nadergas) | **bestaand** `vloerverwarming-groningen.html` — mist lokale FAQ + schema |
| wat kost vloerverwarming in [stad] | midden–hoog (long-tail per stad) | laag–midden | **bestaand** stadspagina's — te vangen met lokale FAQ-sectie (nu alleen Hoogeveen) |
| vloerverwarming infrezen [stad] | midden | midden | **bestaand** stadspagina's + FAQ; long-tail via lokale FAQ-vraag |
| vloerverwarming kosten / per m² | hoog (generiek) | hoog | **bestaand** `prijsindicatie.html` — sterk engagement (232s), 2 sessies/30d; onderbenut als instroom-asset |
| vloerverwarming emmen / klazienaveen e.o. | laag–midden | midden | **bestaand** `vloerverwarming-emmen.html` — rijke dorpencontent, mist alleen FAQ-laag |
| vloerverwarming assen | laag–midden | midden | **bestaand** `vloerverwarming-assen.html` — contextlink naar Friese cluster ontbreekt |
| vloerverwarming drenthe | midden | midden–hoog (ECOtherm, portals) | **bestaand** `vloerverwarming-drenthe.html` (hub) — geschikt voor breadcrumb + hub-links |
| vloerverwarming heerenveen | laag–midden | **hoog** (5+ dedicated pagina's) | **bestaand** `vloerverwarming-heerenveen.html` (cyclus 20) — **niet aankomen**, wél via contextlinks versterken |

\* Volume = **indicatief/geschat**. Geen live keyword-tool deze cyclus.

## Content gaps (structured-data & internal-linking audit)

Er is **geen nieuwe pagina nodig** (max 1/sprint is al op Heerenveen ingezet). De winst
zit in het dichten van vier concrete, aantoonbare gaten in wat er al staat:

- **Sitemap-`lastmod` loopt achter op de deploys.** `vloerverwarming-drachten.html` is op
  6 jul (cyclus 21) inhoudelijk herschreven naar Drachten-only, maar `sitemap.xml` draagt
  voor die URL nog `<lastmod>2026-05-22`. Google ziet in de sitemap dus **geen** wijziging
  en heeft geen reden tot herindexatie. De cyclus-21-refactor is daarmee crawl-technisch
  onzichtbaar. Pure metadata-fix, raakt de pagina-inhoud niet.

- **FAQPage-schema alleen op Hoogeveen.** Van de negen stadspagina's heeft **alléén**
  `vloerverwarming-hoogeveen.html` een zichtbare lokale FAQ-sectie
  (`<h2>Veelgestelde vragen — Hoogeveen</h2>`) én bijbehorend `FAQPage`-JSON-LD met lokale
  plaatsnamen (Hollandscheveld, Fluitenberg, Noordscheschut). De andere acht
  (Assen, Drenthe, Emmen, Groningen, Leeuwarden, Zuidlaren + de twee cyclus-pagina's)
  hebben dit niet. Dit is een bewezen sjabloon in eigen repo dat long-tail
  ("wat kost vloerverwarming in [stad]", "infrezen [stad]", dorpsnamen) vangt en
  FAQ-rich-results in de SERP kan opleveren — hogere CTR = instroom.

- **Geen `BreadcrumbList`-schema op de site.** Geen enkele pagina draagt breadcrumb-
  structured-data. Stadspagina's zijn diepe pagina's (home → regio → stad); breadcrumb-
  markup verduidelijkt hiërarchie voor crawlers en kan breadcrumb-rich-results geven.
  Onzichtbaar voor de bezoeker, dus geen engagement-/meetklok-effect.

- **Contextuele "Ook actief in"-kruislinks zijn ongelijk.** De footer linkt uniform naar
  alle steden, maar de sterkere **in-body** "Ook actief in"-alinea's variëren:
  Emmen en Leeuwarden linken contextueel al naar Heerenveen/Drachten; **Assen niet**
  (alleen footer). In-body links met keyword-anker dragen meer gewicht dan footer-links.
  Door de oudere pagina's (Assen, Groningen, Drenthe-hub) contextueel te laten kruislinken
  naar de diepe/competitieve stadspagina's stroomt link-equity naar de pagina's die nu
  ~0 organisch verkeer krijgen — je bewerkt daarbij **de oude pagina's**, niet de verse.

- **Reeds goed geregeld (niet aankomen):** sitemap bevat alle 20 URL's incl. Heerenveen;
  `robots.txt` staat op `Allow: /` met sitemap-referentie; stadspagina's dragen al
  `LocalBusiness`/`Service`/`City`-schema; footer-regio-lijst is compleet en uniform.

## Concurrentie-observaties

Geen live scan deze cyclus; observaties uit prior research blijven staan. Regionale
installateurs (ECOtherm Drenthe, ReWo, Kentech, plus meerdere dedicated Heerenveen-
pagina's) ranken met stad×dienst-pagina's, plaatsnaam in H1/title en vaak een lokale
FAQ. Dat laatste is precies het gat dat VLWarmte op acht van de negen stadspagina's nog
open heeft staan — terwijl het sjabloon (Hoogeveen) al bestaat.

## prijsindicatie.html — conversie-optimalisatie (bestaande wizard, niet herbouwen)

De conversie-analyse uit cyclus 21 staat nog. `prijsindicatie.html` bindt sterk (232s,
lage bounce) maar krijgt weinig verkeer (2 sessies/30d) en zet niet om. De aanbevelingen
blijven geldig maar zijn **conversie**, niet **instroom** — en de wizard-flow rijpt door
tot ~27 jul, dus die flow blijft deze cyclus ongemoeid:

- **A. Lichtere lead-variant** ("Mail mij dit richtbedrag", alleen e-mail) naast de
  offerte-knop — nieuw event `wizard_lead_email`.
- **B. Telefoon optioneel** (e-mail óf telefoon i.p.v. beide verplicht).
- **C. Sterkere waarde-zin** onder het bedrag (concrete reden nu te reageren).
- **D. Funnel-drop meten** (`wizard_start` → `calculator_result` → `wizard_lead_submit`)
  vóór verdere ingrepen.

**Instroom-hoek (nieuw, additief, deze cyclus):** de wizard-flow zelf niet aanraken, maar
onder/naast de wizard een **indexeerbaar tekstblok** "wat kost vloerverwarming per m²" met
`FAQPage`- of `Article`-schema toevoegen, plus kosten-verankerde interne links vanuit de
stadspagina's en `faq.html` naar deze pagina. Zo wordt de sterkste engagement-pagina óók
een instroom-asset op de generieke "kosten"-long-tail. Additief, raakt de rijpende
funnel niet. Lagere prioriteit gezien de maturatie-constraint.

### Aanbeveling aan Product Manager (wizard)

- **Prioriteit:** conversie A–D = Hoog maar **pas ná ~27 jul** (funnel rijpt); instroom-
  schemablok = Midden, additief en nu al veilig.
- **Geschatte ontwikkeltijd:** A–C 3–6 uur; schemablok 2–3 uur.
- **Verwacht effect:** eerste wizard-leads na maturatie; schemablok = long-tail instroom.

## Seizoenspatroon

Zomer is aanlegseizoen (dekvloer droogt ~6 weken vóór het stookseizoen); juli is nog
oriëntatie-/offertetijd. Wie nu een opname vraagt kan vaak nog vóór de winter geregeld
worden — bruikbaar als urgentie-argument in wizard- en city-FAQ-copy. De lage sessies nu
zijn vooral marketingvolume (Ads bijna nul + organisch nog niet ingebakken), niet
marktafwezigheid. Zoekintentie "kosten" piekt richting winter/verbouwing (indicatief).

## Google Ads — escalatie voor de eigenaar (geen autonome actie deze run)

> Ads-scripts zijn geblokkeerd in deze modus; onderstaande is **advies/escalatie**.

cpc is nu vrijwel dood: **1 sessie/30d, 0 conversies** (was 12 sessies vorige cyclus,
daarvoor ~10,5% ratio). De betaalde motor draait feitelijk niet meer. Advies, in volgorde:

1. **Eerst controleren of de campagne überhaupt nog serveert.** 1 sessie in 30 dagen bij
   €2/dag wijst op een gepauzeerde/afgekeurde campagne, uitgeputte relevantie, of een
   biedprobleem — niet op normale werking. Eigenaar/Marketing: check campagnestatus en
   afkeuringen in de Ads UI (of `google_ads_list_campaigns.py` in een interactieve sessie).
2. **Landing verleggen naar de wizard** (kost geen extra spend): RSA final URL →
   `prijsindicatie.html` resp. `contact.html?modus=offerte#aanvraag`, niet de merk-homepage.
3. **Conversie-import controleren:** staan `wizard_lead_submit`/`contact_submit` als key
   event gemarkeerd en importeert Ads ze? Zonder dat stuurt bidding blind.
4. **Budget pas beoordelen ná landing-fix + serveer-check**; verhoging alleen na
   expliciete spend-goedkeuring in chat.

## GSC-status

| Item | Status |
|------|--------|
| `secrets/gsc.env` | Aanwezig |
| `gsc_fetch.py` | **Mislukt** — `invalid_grant` (refresh token verlopen) |
| Laatste export | 6+ weken oud |
| Actie | Eigenaar: `scripts/gsc_get_refresh_token.py` met verified owner-account; daarna `gsc_fetch.py` per cyclus |

Zonder verse GSC blijven Heerenveen (cyclus 20), de Drachten-refactor (cyclus 21) en de
hieronder voorgestelde schema-ingrepen **niet toetsbaar** op organisch effect. Dit is
inmiddels de langst openstaande blokkade en verdient prioriteit bij de eigenaar.

## Aanbevelingen voor Product Manager (max 8, op prioriteit)

Uitvoerder-notatie per aanbeveling volgt de planningsregel: welke agent + welke check.

### 1. Sitemap-`lastmod` bijwerken voor cyclus-20/21-deploys

- **Prioriteit:** Hoog
- **Type:** SEO / signaalhygiëne (traffic-onafhankelijk, geen inhoud-wijziging)
- **Uitvoerder:** Developer Agent — Skills: `/website-manager`
- **Onderbouwing:** `vloerverwarming-drachten.html` is 6 jul herschreven maar draagt in
  `sitemap.xml` nog `<lastmod>2026-05-22`. Google krijgt geen crawl-signaal; de
  cyclus-21-refactor is onzichtbaar in de sitemap.
- **Actie:** Zet `lastmod` van Drachten (en elke andere op 6 jul gewijzigde URL) op de
  deploy-datum. Alleen sitemap-metadata, geen pagina-inhoud → geen meetklok-reset.
- **Succes / verwacht effect:** Google herindexeert de refactor sneller; meetbaar zodra
  GSC weer draait.

### 2. Lokale FAQ-sectie + `FAQPage`-schema op één oudere stadspagina (Groningen)

- **Prioriteit:** Hoog
- **Type:** SEO / content-verrijking (bestaande dunne pagina, geen nieuwe pagina)
- **Uitvoerder:** Developer Agent — Skills: `/website-manager`
- **Onderbouwing:** Alleen Hoogeveen heeft een lokale FAQ + `FAQPage`-schema; de andere
  acht stadspagina's missen het. Groningen = grootste markt + "installateur"-intentie.
  Long-tail ("wat kost vloerverwarming in Groningen", "infrezen Groningen", wijk-/
  randgemeentenamen) + kans op FAQ-rich-result → hogere CTR = instroom.
- **Actie:** Kopieer Hoogeveens sjabloon (zichtbare `<h2>Veelgestelde vragen — Groningen</h2>`
  + `FAQPage`-JSON-LD) met 3 lokaal ingekleurde vragen (kosten, infrezen, werkgebied/
  randgemeenten). Eén oudere pagina deze sprint; Emmen/Assen in volgende sprints.
  **Heerenveen en Drachten expliciet uitgesloten** (cyclus 20/21, rijpen).
- **Succes / verwacht effect:** FAQ-rich-result-eligibility op Groningen; eerste long-tail-
  impressies zodra GSC draait.

### 3. `BreadcrumbList`-schema op oudere stadspagina's + hubs

- **Prioriteit:** Midden
- **Type:** SEO / structured data (onzichtbaar voor bezoeker)
- **Uitvoerder:** Developer Agent — Skills: `/website-manager`
- **Onderbouwing:** Geen enkele pagina draagt breadcrumb-markup. Stadspagina's zijn diepe
  pagina's; `BreadcrumbList` (home → regio → stad) helpt hiërarchie-begrip en kan
  breadcrumb-rich-results geven.
- **Actie:** Voeg `BreadcrumbList`-JSON-LD toe aan de zes oudere stadspagina's + Drenthe-hub.
  **Heerenveen/Drachten deze cyclus overslaan** om de meetklok niet te raken (later inhalen).
- **Succes / verwacht effect:** Breadcrumb-eligibility in SERP; geen engagement-effect
  (invisibel), dus veilig naast de rijpende pagina's.

### 4. Contextuele internal-linking-pass op oudere "Ook actief in"-blokken

- **Prioriteit:** Midden
- **Type:** SEO / internal linking (alleen oudere pagina's bewerkt)
- **Uitvoerder:** Developer Agent — Skills: `/website-manager`
- **Onderbouwing:** In-body kruislinks zijn ongelijk: Assen's "Ook actief in" linkt níét
  contextueel naar Heerenveen/Drachten (alleen footer), Emmen/Leeuwarden wél. In-body
  links met keyword-anker wegen zwaarder dan footer-links.
- **Actie:** Werk de "Ook actief in"-alinea's op de **oudere** pagina's (Assen, Groningen,
  Drenthe-hub) bij zodat ze contextueel kruislinken naar de diepe/competitieve
  stadspagina's, met beschrijvend anker ("vloerverwarming Heerenveen"). Je bewerkt de oude
  pagina's, niet de verse.
- **Succes / verwacht effect:** Sterkere link-equity naar diepe stadspagina's die nu ~0
  organisch krijgen; zichtbaar in GSC-linkrapport zodra actief.

### 5. `prijsindicatie.html` als instroom-asset — additief kosten-schemablok

- **Prioriteit:** Midden–Laag
- **Type:** SEO / content-verrijking (additief, wizard-flow ongemoeid)
- **Uitvoerder:** Developer Agent — Skills: `/website-manager`
- **Onderbouwing:** Sterkste engagement-pagina (232s) maar 2 sessies/30d — puur als
  conversietool gebruikt. "vloerverwarming kosten per m²" is hoog-volume generiek.
- **Actie:** Onder/naast de wizard een indexeerbaar "wat kost vloerverwarming per m²"-
  tekstblok + `FAQPage`/`Article`-schema; kosten-verankerde interne links vanuit
  stadspagina's en `faq.html` hierheen. **Wizard-stappen en lead-flow niet aanraken**
  (rijpt tot ~27 jul). Additief, geen funnel-reset.
- **Succes / verwacht effect:** Generieke kosten-long-tail gaat naar een pagina die al
  bindt; instroom + latere conversiekans.

### 6. GSC-toegang vernieuwen (escalatie eigenaar)

- **Prioriteit:** Hoog (escalatie, geen dev-taak)
- **Type:** Infra / SEO
- **Uitvoerder:** Eigenaar (interactieve sessie)
- **Onderbouwing:** Token verlopen, data 6+ weken oud. Aanbevelingen 1–5 én de cyclus-20/21-
  pagina's zijn zonder verse GSC niet toetsbaar.
- **Actie:** `scripts/gsc_get_refresh_token.py` met verified owner-account → `gsc_fetch.py`
  per cyclus.
- **Succes / verwacht effect:** Organisch effect (schema, links, refactor) weer meetbaar.

### 7. Ads — serveer-check + landing naar wizard (escalatie eigenaar)

- **Prioriteit:** Midden (escalatie, Ads-scripts geblokkeerd in deze run)
- **Type:** Ads / CRO
- **Uitvoerder:** Eigenaar / Marketing (interactieve sessie)
- **Onderbouwing:** cpc = 1 sessie/30d, 0 conv. Dat is geen normale werking; check
  campagnestatus/afkeuringen. Landing hoort op de wizard, niet de homepage.
- **Actie:** Campagnestatus + conversie-import controleren; RSA final URL naar
  `prijsindicatie.html` / `contact.html?modus=offerte#aanvraag`; budget pas ná fixes,
  alleen met expliciete spend-goedkeuring.
- **Succes / verwacht effect:** Betaald verkeer serveert weer en landt op de converterende
  pagina.

### 8. Social — 1–2 posts met directe link naar een stadspagina

- **Prioriteit:** Laag
- **Type:** Social / SEO (traffic-onafhankelijke instroomhefboom)
- **Uitvoerder:** Social Media Agent — Skills: `/social-media-agent`
- **Onderbouwing:** Instroom is het plafond; stadspagina's krijgen buiten Drachten/Zuidlaren
  nauwelijks sessies. Social omzeilt de organische ranking-lag.
- **Actie:** In `weekly_calendar.md` 1–2 posts met directe link naar een stadspagina
  (bv. de nieuwe Heerenveen-pagina of de verrijkte Groningen-pagina). Hashtags spaarzaam,
  max 1–2 regionaal.
- **Succes / verwacht effect:** Eerste sessies op de diepe stadspagina's.

---

## Escalaties (menselijke actie vereist)

1. **GSC OAuth** — `invalid_grant`, 6+ weken oud; langst openstaande blokkade. Zonder dit
   blijft al het SEO-werk (incl. deze cyclus) blind.
2. **Ads serveert vrijwel niet** — 1 sessie/30d wijst op gepauzeerde/afgekeurde campagne;
   status + landing + conversie-import controleren in interactieve sessie. Geen autonome
   Ads-mutatie deze run.
3. **Beeldmateriaal** — `projecten.html` en social blijven beperkt zonder nieuwe foto's in
   `beeldmateriaal/projecten/`.

---

### Samenvatting voor de Product Manager

- **Sitemap-signaalgat (dev, quick win):** Drachten is 6 jul herschreven maar draagt nog
  `lastmod 22 mei` — Google ziet de cyclus-21-refactor niet. Metadata-fix, geen inhoud.
- **FAQPage-schema-gat (dev):** alleen Hoogeveen heeft een lokale FAQ + schema; verrijk
  één oudere pagina (Groningen) met hetzelfde bewezen sjabloon voor long-tail + rich results.
- **Breadcrumb + contextuele kruislinks (dev):** geen breadcrumb-schema op de site, en
  in-body "Ook actief in"-links zijn ongelijk — beide dichten op de **oudere** pagina's,
  niet de verse.
- **prijsindicatie als instroom-asset (dev, additief):** kosten-schemablok + interne links
  zonder de rijpende wizard-flow te raken.
- **Escalaties:** GSC deblokkeren (langst openstaand) en Ads-serveerstatus checken —
  cpc is effectief dood.
- **Volume-context:** zoekvolumes dit rapport zijn indicatief/geschat (geen live tools).
