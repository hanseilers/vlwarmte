# Marketing Research Rapport — 20 juli 2026 (cyclus 23)

Bron: verse analytics-context (30d per 20 jul 2026), vorig rapport (13 jul / cyclus 22),
sitemap-scan van de root-HTML, en een gerichte on-page / structured-data / internal-linking
grep-audit van alle `vloerverwarming-*.html` stadspagina's + hubs. Vakkennis Noord-Nederlandse
vloerverwarmingsmarkt.

> **Beperkingen deze cyclus (autonome run zonder live tools):**
> geen WebSearch, geen Bash-loops/netwerk, geen Google Ads-scripts, geen GSC-fetch.
> **Alle zoekvolumes hieronder zijn indicatief/geschat** — marktkennis + prior research,
> geen live keyword-tool. Ads-adviezen zijn **escalatie voor de eigenaar**, geen autonome
> actie. GSC blijft geblokkeerd (`invalid_grant`) — escalatie.

## Samenvatting

Instroom is nog verder gezakt: **~21 sessies/30d, laatste week 3 sessies**, en **0 conversies
voor de vierde cyclus op rij**. Betaald kanaal is volledig dood. Een deel van het verkeer valt
bovendien buiten het werkgebied (Drenthe/Groningen/Friesland-brede queries zonder koopintentie).
De enige beïnvloedbare hefboom deze run is traffic-onafhankelijke organische winst op de
bestaande pagina's — precies wat cyclus 22 begon.

De audit bevestigt dat cyclus 22 goed geland is (**sitemap-`lastmod` Drachten staat nu op
2026-07-06**, Groningen heeft nu lokale FAQ + `FAQPage`-schema, breadcrumbs staan op alle
zeven oudere stadspagina's, Assen/Groningen kruislinken nu contextueel naar de Friese diepe
pagina's). Er resteren **vier schone, meetklok-veilige hefbomen** die alleen **oudere** pagina's
raken en de rijpende cyclus-20/21-pagina's (Heerenveen, Drachten) niet aankomen:
**(1)** het **FAQPage-gat** — nog altijd hebben maar 2 van de 9 stadspagina's een lokale FAQ +
schema; **(2)** een **contextueel kruislink-gat** — Emmen, Hoogeveen en Zuidlaren linken alleen
via de footer (niet in-body) naar de diepe Friese pagina's; **(3)** een te lange **`<title>`**
op Hoogeveen; **(4)** de nog openstaande escalaties (GSC, Ads).

## Audit-resultaat per controlepunt (huidige staat, na cyclus 22)

| Controle | Staat | Detail |
|----------|-------|--------|
| Sitemap-`lastmod` | ✅ opgelost | Drachten nu `2026-07-06`; alle cyclus-22-deploys op `2026-07-13`. Geen achterlopende URL meer. |
| `BreadcrumbList`-schema | ✅ op oudere pagina's | Aanwezig op Assen, Drenthe, Emmen, Groningen, Hoogeveen, Leeuwarden, Zuidlaren (7). **Ontbreekt** alleen op Heerenveen (c20) + Drachten (c21) — bewust uitgesteld. |
| Lokale FAQ + `FAQPage`-schema | ⚠️ **gat** | Alleen **Hoogeveen** en **Groningen** hebben een zichtbare lokale FAQ (`<h2>Veelgestelde vragen — [Stad]</h2>`) + `FAQPage`-JSON-LD. De andere 7 stadspagina's linken alleen naar `faq.html`. |
| Contextuele "Ook actief in"-kruislinks | ⚠️ **deels** | Assen, Groningen, Drenthe-hub, Leeuwarden kruislinken **in-body** naar Heerenveen + Drachten. **Emmen** en **Hoogeveen** doen dat níét (alleen footer); **Zuidlaren** linkt Heerenveen in-body maar Drachten alleen via footer. |
| Meta-descriptions | ✅ compleet | Alle 18 gecontroleerde pagina's hebben `name="description"`. |
| Dubbele H1's | ✅ geen | Elke pagina heeft exact 1 `<h1>`. |
| `<title>`-lengtes | ⚠️ 1 uitschieter | Hoogeveen: *"Vloerverwarming Hoogeveen, Hollandscheveld & omgeving — installateur uit Zuidlaren"* ≈ 81 tekens (wordt afgekapt in SERP en mist `| VLWarmte`). Overige stadstitels ~55–60 tekens. |
| Alt-teksten | ✅ compleet | Project-/fotobeelden hebben beschrijvende `alt`; merk-logo gebruikt bewust lege `alt=""` + `aria-label` (correct voor decoratief). |
| `LocalBusiness`/`Service`/`City`-schema | ✅ aanwezig | Alle stadspagina's dragen `Service` + `City` + `LocalBusiness`-JSON-LD. |
| Interne links home → stadspagina's (crawl-diepte) | ✅ solide | `index.html`, `diensten.html` en `werkwijze.html` linken naar alle stadspagina's; elke stad op crawl-diepte 1. |
| `robots.txt` / sitemap-dekking | ✅ ok | `Allow: /` met sitemap-referentie; sitemap bevat alle URL's. |

## Top zoekwoorden

| Zoekwoord | Volume (indicatie) | Concurrentie | Pagina / actie |
|-----------|-------------------|--------------|----------------|
| wat kost vloerverwarming in assen | midden (long-tail) | laag–midden | **bestaand** `vloerverwarming-assen.html` — mist nog lokale FAQ + schema |
| vloerverwarming infrezen emmen / zuidoost-drenthe | midden | midden | **bestaand** `vloerverwarming-emmen.html` — rijke dorpencontent, mist FAQ-laag |
| vloerverwarming assen / drenthe | laag–midden | midden | **bestaand** stadspagina's — te vangen met lokale FAQ (nu alleen Hoogeveen + Groningen) |
| vloerverwarming heerenveen / drachten | laag–midden | **hoog** | **bestaand** (cyclus 20/21) — **niet aankomen**, wél via meer in-body kruislinks vanaf oudere pagina's versterken |
| vloerverwarming kosten / per m² | hoog (generiek) | hoog | **bestaand** `prijsindicatie.html` — sterk engagement, onderbenut als instroom-asset (wizard rijpt tot ~27 jul → deze cyclus ongemoeid) |

\* Volume = **indicatief/geschat**. Geen live keyword-tool deze cyclus.

## Content gaps (structured-data & internal-linking audit)

**Geen nieuwe pagina nodig.** De winst zit in het dichten van twee resterende, aantoonbare
gaten op de **oudere** pagina's:

- **FAQPage-schema staat pas op 2 van de 9 stadspagina's.** Cyclus 22 voegde Groningen toe naast
  Hoogeveen. De zeven overige stadspagina's linken alleen naar de generieke `faq.html` en missen
  een eigen, lokaal ingekleurde FAQ. Van die zeven zijn **Heerenveen (c20)** en **Drachten (c21)**
  uitgesloten wegens maturatie; de veilige kandidaten zijn **Assen, Emmen, Leeuwarden, Zuidlaren**
  en de **Drenthe-hub**. Het sjabloon (`<h2>Veelgestelde vragen — [Stad]</h2>` + `data-faq-toggle`-
  accordeon + `FAQPage`-JSON-LD, met de accordeon-JS al in de gedeelde `assets/js/main.js`) staat
  klaar en is bewezen. Long-tail ("wat kost vloerverwarming in [stad]", "infrezen [stad]",
  dorps-/wijknamen) + kans op FAQ-rich-result → hogere CTR = instroom.

- **Contextuele in-body kruislinks zijn nog ongelijk.** Assen, Groningen, Drenthe-hub en Leeuwarden
  linken in de "Ook actief in"-alinea al naar de diepe/competitieve Friese pagina's; **Emmen** en
  **Hoogeveen** doen dat níét (die noemen alleen Groningen/Assen/Hoogeveen/Leeuwarden/Zuidlaren in
  de eerste alinea, en linken Heerenveen/Drachten hoogstens via de footer), en **Zuidlaren** mist
  de in-body Drachten-link. In-body links met beschrijvend keyword-anker wegen zwaarder dan
  footer-links. Door de oudere pagina's te laten kruislinken naar de diepe stadspagina's stroomt
  link-equity naar de pagina's met nu ~0 organisch verkeer — je bewerkt daarbij **de oudere**
  pagina's, de verse cyclus-20/21-pagina's blijven ongemoeid (er wijzigt niets ín Heerenveen/Drachten).

- **Reeds goed geregeld (niet aankomen):** sitemap-`lastmod`, breadcrumbs op oudere pagina's,
  meta-descriptions, H1-uniek, alt-teksten, `LocalBusiness`/`Service`/`City`-schema, crawl-diepte,
  `robots.txt`.

## Concurrentie-observaties

Geen live scan deze cyclus; observaties uit prior research blijven staan. Regionale installateurs
(ECOtherm Drenthe, ReWo, Kentech, meerdere dedicated Heerenveen-pagina's) ranken met stad×dienst-
pagina's, plaatsnaam in H1/title en vaak een lokale FAQ. Dat laatste is precies het gat dat
VLWarmte op zeven van de negen stadspagina's nog open heeft — terwijl het sjabloon (Hoogeveen,
Groningen) al twee keer in eigen repo staat.

## Seizoenspatroon

Zomer is aanlegseizoen (dekvloer droogt ~6 weken vóór het stookseizoen); juli is nog
oriëntatie-/offertetijd. Wie nu een opname vraagt, kan vaak nog vóór de winter geregeld worden —
bruikbaar als urgentie-argument in city-FAQ-copy. De lage sessies nu zijn vooral marketingvolume
(Ads nul + organisch nog niet ingebakken), niet marktafwezigheid.

---

## Autonoom-implementeerbare taken voor de Developer Agent (deze sprint)

Vier concrete taken, alle op **oudere/veilige** pagina's, samen ruim **< 4 uur**, geen risico voor
de rijpende cyclus-20/21-pagina's. Uitvoerder + succescriterium per taak conform planningsregel.

### 1. Lokale FAQ-sectie + `FAQPage`-schema op `vloerverwarming-assen.html`

- **Prioriteit:** Hoog
- **Type:** SEO / content-verrijking (bestaande dunne pagina)
- **Uitvoerder:** Developer Agent — Skills: `/developer-agent`, `/website-manager`
- **Bestandspad:** `/Users/hanseilers/vlwarmte/vloerverwarming-assen.html`
- **Onderbouwing:** Assen (Drentse hoofdstad) heeft nu alleen een footerlink naar `faq.html`.
  Hoogeveen + Groningen bewijzen het sjabloon; Assen is de logische volgende oudere pagina.
- **Exacte wijziging:**
  1. Voeg **na** het "Ook actief in"-blok (sluit op regel 217 met `</section>`) en **vóór** de
     CTA-`<section class="section">` op regel 219 een nieuwe sectie toe, exact volgens het
     Hoogeveen-sjabloon (regels 230–264 in `vloerverwarming-hoogeveen.html`):
     `<section class="section"><div class="container"><div class="section-head">`
     `<h2>Veelgestelde vragen — Assen</h2></div>` + drie `<div class="faq-item">`-blokken met
     `<button class="faq-question" data-faq-toggle>…</button>` en `<div class="faq-answer"><p>…</p></div>`.
  2. Gebruik **lokaal ingekleurde** vragen (niet Hoogeveens tekst kopiëren — vermijd duplicate content):
     - "Werken jullie ook in Assen-Oost, Kloosterveen en de dorpen rond Assen?" (noem echte
       randkernen: Loon, Ubbena, Rhee, Vries-kant)
     - "Wat kost vloerverwarming in Assen?" (verwijs naar `prijsindicatie.html`)
     - "Kunnen jullie infrezen in een bestaande dekvloer in Assen?"
  3. Voeg **in de `<head>`, direct na de bestaande `BreadcrumbList`-`<script>` (regel 50)**, een
     nieuw `<script type="application/ld+json">`-blok toe met `{"@type":"FAQPage","mainEntity":[…]}`,
     waarin de `name`/`acceptedAnswer.text` **woordelijk** overeenkomen met de zichtbare vragen/antwoorden
     (Google-vereiste). De accordeon-JS zit al in `assets/js/main.js` (`[data-faq-toggle]`, regel 71) —
     géén JS-wijziging nodig.
- **Succescriterium:** `grep '"FAQPage"' vloerverwarming-assen.html` geeft één treffer; de zichtbare
  vraagteksten matchen de JSON-LD 1-op-1; de accordeon opent/sluit; Rich Results Test valideert FAQ
  zonder fouten. Meetbaar effect (impressies/CTR) zodra GSC weer draait.

### 2. Lokale FAQ-sectie + `FAQPage`-schema op `vloerverwarming-emmen.html`

- **Prioriteit:** Hoog
- **Type:** SEO / content-verrijking
- **Uitvoerder:** Developer Agent — Skills: `/developer-agent`, `/website-manager`
- **Bestandspad:** `/Users/hanseilers/vlwarmte/vloerverwarming-emmen.html`
- **Onderbouwing:** Emmen heeft rijke dorpencontent (Zuidoost-Drenthe) maar mist de FAQ-laag; sterke
  long-tail-kans op dorps-/plaatsnamen (Klazienaveen, Nieuw-Amsterdam, Emmer-Compascuum).
- **Exacte wijziging:** Idem taak 1, maar in Emmen: het "Ook actief in"-blok sluit op regel 226
  (`</section>`); voeg de FAQ-sectie in **tussen regel 226 en de CTA-sectie op regel 228**. Voeg het
  `FAQPage`-`<script>` toe in de `<head>` na het bestaande tweede `ld+json`-blok (regel 48–50).
  Lokale vragen bijv.: "Werken jullie ook in Klazienaveen en Nieuw-Amsterdam?", "Wat kost
  vloerverwarming in Emmen?", "Kunnen jullie vloerverwarming infrezen in een bestaande woning in Emmen?".
- **Succescriterium:** identiek aan taak 1, voor Emmen.
- **Let op cadans:** taak 1 heeft voorrang; taak 2 mag deze óf de volgende sprint. Maak de vragen
  **inhoudelijk verschillend** per stad om duplicate-content-signaal te voorkomen. Leeuwarden,
  Zuidlaren en de Drenthe-hub blijven bewust voor volgende sprints.

### 3. Contextuele "Ook actief in"-kruislinks completeren (Emmen, Hoogeveen, Zuidlaren)

- **Prioriteit:** Midden
- **Type:** SEO / internal linking (alleen oudere pagina's bewerkt)
- **Uitvoerder:** Developer Agent — Skills: `/developer-agent`, `/website-manager`
- **Bestandspaden:** `vloerverwarming-emmen.html` (blok rond regel 210–225),
  `vloerverwarming-hoogeveen.html` (blok rond regel 205–224),
  `vloerverwarming-zuidlaren.html` (blok rond regel 180).
- **Onderbouwing:** Emmen en Hoogeveen linken nu alleen via de footer naar Heerenveen/Drachten;
  Zuidlaren mist de in-body Drachten-link. Assen/Groningen/Leeuwarden/Drenthe hebben dit al —
  gelijktrekken laat link-equity naar de diepe/competitieve Friese pagina's stromen.
- **Exacte wijziging:** Voeg in de "Ook actief in"-alinea van elk van de drie pagina's een
  **in-body** zin toe met beschrijvend anker, in dezelfde stijl als Assen (regels 211–214), bv.:
  *"Aan de Friese kant, over de A28/A32, rijden we net zo makkelijk door voor
  `<a href="vloerverwarming-heerenveen.html">vloerverwarming in Heerenveen</a>` en
  `<a href="vloerverwarming-drachten.html">vloerverwarming in Drachten</a>."*
  Voor Zuidlaren alleen de ontbrekende Drachten-link aanvullen. **Alleen de oudere pagina's
  worden bewerkt — er wijzigt niets ín Heerenveen of Drachten.**
- **Succescriterium:** `grep -c 'vloerverwarming-heerenveen.html' vloerverwarming-emmen.html` en
  `…-drachten.html` geven elk ≥ 2 (in-body + footer); idem voor Hoogeveen; Zuidlaren ≥ 2 op Drachten.
  Zichtbaar in GSC-linkrapport zodra GSC draait.

### 4. `<title>` van `vloerverwarming-hoogeveen.html` inkorten

- **Prioriteit:** Laag
- **Type:** SEO / on-page (metadata)
- **Uitvoerder:** Developer Agent — Skills: `/developer-agent`, `/website-manager`
- **Bestandspad:** `/Users/hanseilers/vlwarmte/vloerverwarming-hoogeveen.html`
- **Onderbouwing:** Huidige titel ≈ 81 tekens (afgekapt in SERP) en mist de merknaam `| VLWarmte`
  die alle andere stadspagina's wél dragen.
- **Exacte wijziging:** Vervang
  `<title>Vloerverwarming Hoogeveen, Hollandscheveld & omgeving — installateur uit Zuidlaren</title>`
  door bv. `<title>Vloerverwarming Hoogeveen — installateur uit Zuidlaren | VLWarmte</title>`
  (≈ 63 tekens; dorpsnamen leven al in H1/FAQ/tekst). Alleen `<title>`; H1 en content ongemoeid.
- **Succescriterium:** `<title>` ≤ 60–63 tekens en eindigt op `| VLWarmte`; H1 onveranderd.

---

## Bewust uitgesteld (geen actie deze cyclus)

- **FAQ op Leeuwarden, Zuidlaren en Drenthe-hub** — volgende sprint(s), om over-optimalisatie/
  duplicate-signaal in één keer te vermijden en de FAQ's per stad echt lokaal te houden.
- **`BreadcrumbList` op Heerenveen (c20) en Drachten (c21)** — die twee missen breadcrumb nog, maar
  worden deze cyclus **niet aangeraakt** (maturatie). Inhalen zodra de meetklok van die pagina's
  rond is (indicatief na eind juli).
- **`prijsindicatie.html` als instroom-asset** (additief kosten-schemablok + kosten-verankerde
  interne links) — wizard-flow rijpt tot ~27 jul; pas daarna. Blijft een goede Midden-prioriteit
  voor cyclus 24.

## Google Ads — escalatie voor de eigenaar (geen autonome actie deze run)

> Ads-scripts zijn geblokkeerd in deze modus; onderstaande is **advies/escalatie**.

Betaald kanaal is deze cyclus **volledig dood** (0 sessies/lead uit cpc). Advies, in volgorde:

1. **Controleer of de campagne überhaupt nog serveert / niet is afgekeurd of gepauzeerd** — nul
   verkeer bij een lopend budget wijst op status- of biedprobleem, niet op normale werking.
   Eigenaar/Marketing: check in de Ads UI (of `google_ads_list_campaigns.py` in een interactieve sessie).
2. **Landing verleggen naar de converterende pagina** (kost geen extra spend): RSA final URL →
   `prijsindicatie.html` resp. `contact.html?modus=offerte#aanvraag`, niet de merk-homepage.
3. **Conversie-import controleren:** staan `wizard_lead_submit`/`contact_submit` als key event
   gemarkeerd en importeert Ads ze? Zonder dat stuurt bidding blind.
4. **Budget pas beoordelen ná serveer-check + landing-fix**; verhoging alleen na **expliciete**
   spend-goedkeuring in chat.

## GSC-status

| Item | Status |
|------|--------|
| `secrets/gsc.env` | Aanwezig |
| `gsc_fetch.py` | **Mislukt** — `invalid_grant` (refresh token verlopen) |
| Laatste export | 7+ weken oud |
| Actie | Eigenaar: `scripts/gsc_get_refresh_token.py` met verified owner-account; daarna `gsc_fetch.py` per cyclus |

Zonder verse GSC blijven cyclus-20/21-pagina's én alle schema-/link-ingrepen **niet toetsbaar** op
organisch effect. Langst openstaande blokkade — prioriteit bij de eigenaar.

---

## Aanbevelingen voor Product Manager (op prioriteit)

1. **FAQ + `FAQPage`-schema op Assen** (dev, **Hoog**) — bewezen sjabloon, oudere pagina, autonoom.
2. **FAQ + `FAQPage`-schema op Emmen** (dev, **Hoog**) — long-tail op Zuidoost-Drenthe dorpen.
3. **Kruislinks completeren op Emmen/Hoogeveen/Zuidlaren** (dev, **Midden**) — link-equity naar diepe pagina's.
4. **Hoogeveen `<title>` inkorten** (dev, **Laag**) — quick metadata-fix.
5. **GSC-toegang vernieuwen** (eigenaar, **Hoog** — escalatie) — anders blijft al het SEO-werk blind.
6. **Ads serveer-check + landing naar wizard** (eigenaar/marketing, **Midden** — escalatie) — cpc is dood.
7. **Social: 1–2 posts met directe link naar een stadspagina** (Social Media Agent, **Laag**) —
   omzeilt de organische ranking-lag; hashtags spaarzaam, max 1–2 regionaal.

---

## Escalaties (menselijke actie vereist)

1. **GSC OAuth** — `invalid_grant`, 7+ weken oud; langst openstaande blokkade. Zonder dit blijft al
   het SEO-werk (incl. deze cyclus) blind.
2. **Ads volledig dood** — 0 cpc-sessies/30d; status + landing + conversie-import controleren in
   interactieve sessie. Geen autonome Ads-mutatie deze run.
3. **Beeldmateriaal** — `projecten.html` en social blijven beperkt zonder nieuwe foto's in
   `beeldmateriaal/projecten/`.

---

### Samenvatting voor de Product Manager

- **Cyclus 22 landde goed:** sitemap-`lastmod` gefixt, Groningen-FAQ + schema live, breadcrumbs op
  alle oudere pagina's, Assen/Groningen kruislinken nu contextueel.
- **Resterend FAQ-gat (dev):** pas 2 van 9 stadspagina's hebben lokale FAQ + schema — verrijk
  **Assen** (Hoog) en **Emmen** (Hoog) met hetzelfde sjabloon, lokaal ingekleurd.
- **Kruislink-gat (dev):** Emmen/Hoogeveen/Zuidlaren linken alleen via footer naar de diepe Friese
  pagina's — in-body gelijktrekken (Midden). Alle wijzigingen op **oudere** pagina's; Heerenveen/
  Drachten blijven ongemoeid.
- **Metadata (dev):** Hoogeveen-`<title>` inkorten (Laag).
- **Escalaties:** GSC deblokkeren (langst openstaand) en Ads-serveerstatus checken — cpc is dood.
- **Volume-context:** zoekvolumes dit rapport zijn indicatief/geschat (geen live tools).
