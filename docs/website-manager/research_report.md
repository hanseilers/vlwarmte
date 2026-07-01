# Marketing Research Rapport — 1 juli 2026 (cyclus 20)

Bron: verse GA4 (`docs/website-manager/analytics_report.md`, fetch 2026-07-01),
vorige sprint (`archive/sprint-2026-07-01.md`), live Google Ads-verificatie
(smoke test + `list_campaigns` + geo `--dry-run`), WebSearch (concurrentie,
prijscalculator, seizoen), sitemap-scan en `scripts/data/google_ads_lead_campaign_defaults.json`.

> **GSC:** `secrets/gsc.env` aanwezig, maar fetch faalt met `invalid_grant` —
> refresh token verlopen. Posities in dit rapport komen uit GSC-export van
> **23 mei 2026** (`gsc_report.json`).

## Samenvatting

Het knelpunt blijft **instroom**, niet conversiekwaliteit op betaald verkeer:
38 sessies / 30d, 2 conversies, beide uit `google/cpc` (~10,5% ratio bij
€2/dag). Cyclus-19-ingrepen (wizard-leadstap, home-titel, interne stadlinks)
zijn **te vers om te meten** (live 29 jun). De grootste kansen deze cyclus:
**(1) Ads-budget en spend-goedkeuring** — campagne draait ENABLED maar volume is
structureel laag; **(2) wizard-funnel afwachten en daarna meten** — 68 sessies /
90d op `prijsindicatie.html`, nog steeds 0 `wizard_lead_submit`; **(3) GSC
deblokkeren** — zonder verse Search Console-data blijft organisch blind;
**(4) Heerenveen-gap** — Ads-keyword actief zonder dedicated landingspagina.

## Top zoekwoorden

| Zoekwoord | Volume (indicatie) | Concurrentie | Pagina / actie |
|-----------|-------------------|--------------|----------------|
| vloerverwarming drenthe | midden | midden–hoog (ECOtherm, portals) | **bestaand** `vloerverwarming-drenthe.html` — laten ranken via links + GSC |
| vloerverwarming groningen installateur | midden | midden (ReWo, Kentech, Nadergas) | **bestaand** `vloerverwarming-groningen.html` |
| vloerverwarming friesland / leeuwarden | laag–midden | midden | **bestaand** `vloerverwarming-leeuwarden.html` |
| vloerverwarming heerenveen | laag–midden | **hoog** (5+ dedicated concurrentpagina's) | **gap** — geen eigen pagina; keyword in Ads actief |
| installateur zuidlaren | laag (GSC: 9 impr, pos 3,7) | laag | **bestaand** — CTR-fix cyclus 19 live; GSC nodig |
| schuimbeton vloerverwarming drenthe/groningen | laag | laag–midden | **bestaand** diensten + `#schuimbeton`; Ads-keyword actief |
| laagopbouw / droge vloerverwarming | laag–midden | midden | **bestaand** `systemen-producten.html#laagopbouw` — zwakke landing (67% bounce) |
| vloerverwarming kosten / per m2 | hoog (generiek) | hoog | **bestaand** `prijsindicatie.html` — sterke engagement, 0 conv |
| vloerverwarming infrezen renovatie | midden | midden | **bestaand** FAQ + diensten; geen aparte pagina nodig |
| warmtepomp zuidlaren | laag (GSC: 4 impr) | laag | **bestaand** — enige term met clicks (25% CTR) |

\* Volume = indicatief (WebSearch + GSC mei 2026); geen betaalde keyword-tool deze cyclus.

## Content gaps (ten opzichte van huidige sitemap)

De acht stadspagina's + Drenthe-hub bestaan; prioriteit is **ranken en converteren**,
niet nieuwbouw — behalve één duidelijke gap:

- **`vloerverwarming-heerenveen.html` (nieuw)**: Ads-keyword `vloerverwarming
  heerenveen` staat in `google_ads_lead_campaign_defaults.json`; site heeft alleen
  een interne link vanaf Zuidlaren naar Drachten. Concurrenten (van der Veen, Giet
  Mooi, KIBS, ET-F) hebben dedicated Heerenveen-URL's. **Alternatief:** keyword
  pauzeren tot pagina er is.
- **Geen nieuwe dienst-splitsingspagina's** ("alleen schuimbeton", aannemers):
  nog steeds nul vraagsignaal in GA4/GSC bij klein volume.
- **`systemen-producten.html#laagopbouw`**: content bestaat; landingervaring
  onderbenut (3 landings, 67% bounce, 18 s) — hero/CTA, geen nieuwe pagina.
- **`diensten.html` cta-band**: hero wijst naar wizard, onderste band primair
  naar `contact.html?modus=offerte` — inconsistent met wizard-first strategie.

## Concurrentie-observaties

**Regionale installateurs** ranken met **stad × dienst**-pagina's en brede
werkgebied-claims (ECOtherm Drenthe, ReWo Groningen/Drenthe/Friesland, Kentech
Groningen-Assen, Nadergas per Groningse subregio). Sterke patronen bij hen:

- Plaatsnaam in H1/title ("Vloerverwarming Heerenveen")
- Vrijblijvende offerte + snelle reactie
- Warmtepomp-combinatie als upsell
- Vaste prijs / geen verrassingen (ECOtherm)

**VLWarmte-onderscheid** dat in copy en Ads moet blijven: **compleet traject**
(ondervloer, schuimbeton, leidingwerk, dekvloer), eigen ploeg uit Zuidlaren,
10 jaar garantie buis, online richtbedrag. Niet concurreren op "goedkoopste" —
concurrenten en portals (Slimster, Bobex) spelen wél op prijsvergelijking.

**Hyperlokaal Zuidlaren:** VLWarmte staat GSC-mei top-3 op installateur/elektricien
(0 clicks) — snippet-fix cyclus 19 moet dat doorbreken zodra GSC ververst is.

## Prijscalculator — haalbaarheidsonderzoek

### Conclusie

**Niet opnieuw bouwen.** `prijsindicatie.html` ís al de prijscalculator: meerstaps-
wizard met schuimbeton-bandbreedte, Formspree-lead (`xzdojzdk`) en GA4-events.
Prioriteit = **meer instroom + funnel-lek dichten**, geen tweede tool.

### Onderbouwing

- Eigen data: 307 s gem. duur, 25% bounce op `prijsindicatie.html` — sterkste
  pagina van de site; 0 conversies over 90d/68 sessies wijst op funnel-frictie,
  niet op afwezigheid van een calculator.
- Branche: interactieve checks/calculators verhogen leadkwaliteit (HomeZero claimt
  ~30% hogere website→lead-conversie; Leadmodule positioneert calculators vs.
  gedeelde Werkspot-leads). VLWarmte heeft dit al ingebouwd.
- Concurrenten: generieke calculators (Vastlegg: NEN 12831, €45–85/m²) zijn
  technisch/te algemeen; lokale installateurs gebruiken vooral offerteformulieren.
  VLWarmte's schuimbeton-specifieke bandbreedte is **differentiator**.

### Voorgestelde opbouw wizard (bestaand — geen wijziging deze cyclus)

1. Productkeuze (alleen VL vs. VL + schuimbeton)
2. m², kruipruimte-diepte, ondergrond
3. Resultaat + `.lead-after` (offerte + bellen)

Cyclus 19 versterkte stap 3 visueel; **4 weken wachten** vóór nieuwe ingreep.

### Leadgeneratie koppeling

Formulier na richtbedrag → Formspree → `wizard_lead_submit` (key event).
Secundair: `tel:` + `contact.html?modus=bel#aanvraag`. Ads-sitelink en home-CTA
moeten hier naartoe sturen.

### Risico's en aandachtspunten

- Bindende prijsclaim vermijden ("indicatie", "richtbedrag", excl. btw).
- Hout-ondergrond-route naar contact (geen prijs) — behouden.
- Bij aanhoudend 0 conv: funnel-events uitlezen (`wizard_start` →
  `calculator_result` → `wizard_lead_submit`).

### Aanbeveling aan Product Manager

- **Prioriteit:** Midden (onderhoud/meting, geen nieuwbouw)
- **Geschatte ontwikkeltijd:** 0 uur nieuwbouw; eventueel 2–4u funnel-fix na meting
- **Verwacht effect:** Eerste wizard-lead binnen 4–8 weken na cyclus 19

## Seizoenspatroon

- **Aanleg:** zomer is het klassieke aanlegseizoen (dekvloer droogt ~6 weken vóór
  stookseizoen) — nu (juli) is oriëntatie/offerte-tijd nog relevant.
- **Zoekintentie kosten:** piekt richting winter/verbouwing (indicatief; geen harde
  volume-data zonder keyword-tool).
- **Conjunctuur:** EIB H1 2026 — installatiebedrijven positiever over omzet dan
  bouwbedrijven; vraag naar verbouwing/verwarming blijft gunstig.
- **Implicatie:** lage sessies nu zijn vooral **marketingvolume** (Ads €2/dag +
  organisch nog niet ingebakken), niet per se marktafwezigheid.

## Google Ads — verificatie (cyclus 20)

| Check | Resultaat |
|-------|-----------|
| `google_ads_smoke_test.py` | OK — 3 toegankelijke accounts |
| `google_ads_list_campaigns.py` | **23834672782** — `SEARCH`, **ENABLED**, `VLW-API-Leads NL auto` |
| Dagbudget (defaults JSON) | **€2/dag** |
| `update_campaign_geo.py --dry-run` | Geo staat al op **Drenthe + Groningen + Friesland** (20759/20761/20763); dry-run is replace met dezelfde set — **geen `--apply` nodig** |
| GA4 geo-lek (NH/ZH/DE/BD/CA) | Waarschijnlijk historisch / "interesse"-locatie / restant 30d-venster; geo-targeting lijkt correct |

**Conversie-alignment:** beide conv. landen op `/`, niet op `prijsindicatie.html`.
RSA `final_urls` zijn al beperkt tot offerte-deeplink + prijsindicatie; sitelink
"Prijsindicatie" staat in defaults. Overweeg in Ads UI te controleren of Google
de homepage als canonical landing kiest — headline "Richtbedrag in 2 minuten" +
sitelink prominent houden.

**Niet uitgevoerd (bewust):** `--apply` geo (geen wijziging), budgetverhoging,
`--go-live` (campagne al ENABLED), negatives-script (bestaande set in JSON;
geen nieuwe negatieven uit research deze cyclus).

## GSC-status

| Item | Status |
|------|--------|
| `secrets/gsc.env` | Aanwezig |
| `gsc_fetch.py` | **Mislukt** — `RefreshError: invalid_grant` |
| Laatste export | 2026-05-23 (28d t/m 22 mei) |
| Actie | Eigenaar: `python scripts/gsc_get_refresh_token.py` met verified owner-account; daarna `gsc_fetch.py` in elke cyclus |

Zonder verse GSC zijn cyclus 17–19-ingrepen (stadlinks, CTR-fix Zuidlaren,
home-titel) **niet toetsbaar**.

## Aanbevelingen voor Product Manager (max 8)

### 1. Google Ads — budget beoordelen (escalatie eigenaar)

- **Prioriteit:** Hoog
- **Type:** Ads / spend
- **Onderbouwing:** 19 cpc-sessies / 2 conv (~10,5%); campagne ENABLED @ €2/dag.
  Enige schaalbare leadhefboom op korte termijn.
- **Actie:** Eigenaar bevestigt gewenst dagbudget (bijv. €5–10/dag test). Agent
  kan daarna `google_ads_update_campaign_budget.py` of recreate-flow met
  `--daily-budget-eur` — **alleen na expliciete spend-goedkeuring in chat**.
- **Verwacht effect:** Lineair meer leads bij gelijke ratio (indicatief +1 lead /
  ~10 extra betaalde sessies).

### 2. Wizard-conversie — 4 weken meten, geen nieuwe ingreep

- **Prioriteit:** Hoog
- **Type:** CRO / meting
- **Onderbouwing:** Cyclus 19 live 29 jun; 90d nog 0 `wizard_lead_submit` op
  68 sessies. Te vroeg om te falen.
- **Actie:** Sprint week ~27 jul: GA4-check `wizard_lead_submit`. Bij nog 0:
  funnel-query `wizard_start` → `calculator_result` → `wizard_lead_submit`.
- **Verwacht effect:** Gerichte fix i.p.v. gissen.

### 3. GSC OAuth vernieuwen

- **Prioriteit:** Hoog
- **Type:** Infra / SEO
- **Onderbouwing:** Token expired; data 5+ weken oud.
- **Actie:** `scripts/gsc_get_refresh_token.py` → `gsc_fetch.py` in analytics-cyclus.
- **Verwacht effect:** Indexatie/CTR stadspagina's en Zuidlaren-termen meetbaar.

### 4. Heerenveen — pagina bouwen of Ads-keyword pauzeren

- **Prioriteit:** Hoog
- **Type:** SEO + Ads-alignment
- **Onderbouwing:** Keyword actief in campagne; geen `vloerverwarming-heerenveen.html`;
  concurrenten hebben dedicated pagina's. Intent-mismatch kost Quality Score en
  bounce.
- **Actie:** Developer: pagina op patroon Drachten/Leeuwarden (werkgebied, wizard-CTA,
  canonical) **of** Marketing: keyword uit campagne tot pagina live is.
- **Verwacht effect:** Betere Ads-kwaliteit + organische dekking Friese subregio.

### 5. `diensten.html` — cta-band primair naar wizard

- **Prioriteit:** Midden
- **Type:** CTA
- **Onderbouwing:** Analytics cyclus 20: hero → wizard, cta-band → contact offerte;
  3 sessies, 17 s, 50% bounce als landing.
- **Actie:** `cta-band`: primaire knop `prijsindicatie.html` ("Richtbedrag in 2
  minuten"), secundair contact.
- **Verwacht effect:** Consistente wizard-routing; meer `wizard_start`.

### 6. `systemen-producten.html` — landing hero aanscherpen

- **Prioriteit:** Midden
- **Type:** Content / CTA
- **Onderbouwing:** 3 landings, 67% bounce, 18 s; laagopbouw-keywords in Ads.
- **Actie:** Hero: concrete belofte + plaats/regio + primaire CTA wizard; trust-regel
  (10 jaar garantie buis, reactie één werkdag). Geen tweede formulier.
- **Verwacht effect:** Lagere bounce op laagopbouw-intent.

### 7. Stadspagina's — social traffic (handmatig)

- **Prioriteit:** Midden
- **Type:** Social / SEO
- **Onderbouwing:** Drachten + Zuidlaren elk 2 sessies, 0% bounce na interne links;
  overige steden 0 sessies in 30d.
- **Actie:** `weekly_calendar.md`: 1–2 posts met directe link naar stadspagina
  (niet alleen home/wizard). Hashtags: max 1–2 regionale (#Drachten, #ZuidLaren).
- **Verwacht effect:** Eerste sessies op hub + zusterpagina's.

### 8. Ads-landing — homepage vs. wizard monitoren

- **Prioriteit:** Midden
- **Type:** Ads / CRO
- **Onderbouwing:** 100% conv via `/`; prijsindicatie 307 s engagement maar 67%
  bounce als directe landing en 0 conv.
- **Actie:** In Ads UI: ad strength + landing-rapport; sitelink "Prijsindicatie"
  en headline "Richtbedrag in 2 minuten" prominent. Geen budgetwijziging zonder
  goedkeuring. Over 4 weken: vergelijk conv per landing in GA4.
- **Verwacht effect:** Meer wizard-instroom zonder homepage-bounce te verergeren.

---

## Escalaties (menselijke actie vereist)

1. **Spend-goedkeuring** — budget verhogen boven €2/dag (enige hefboom voor meer
   leads bij gezonde cpc-ratio).
2. **GSC OAuth** — `invalid_grant`; refresh token opnieuw genereren.
3. **Beeldmateriaal** — `projecten.html` en social blijven geblokkeerd zonder nieuwe
   foto's in `beeldmateriaal/projecten/`.

---

### Samenvatting voor de Product Manager

- **Ads:** campagne `23834672782` draait **SEARCH / ENABLED** @ **€2/dag**; geo al
  DR+GR+FR — geen geo-mutatie nodig. Volume is de bottleneck; budget alleen met
  eigenaar-akkoord.
- **Site:** cyclus-19 live; meet wizard + titel over 4 weken. Grootste dev-kansen:
  Heerenveen-gap, diensten-cta-band, systemen-hero.
- **GSC:** fetch geblokkeerd (verlopen token) — eerst OAuth, dan SEO-effect meten.
- **Calculator:** niet opnieuw bouwen; optimaliseer instroom en funnel.
