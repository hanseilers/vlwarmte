# Marketing Research Rapport — 26 mei 2026

**Cyclus 13** — eerste research na laagopbouw-cluster-deploy (23 mei, commit `7a45234`) en cyclus-11-deploy (20 mei). Eerste rapport dat **GSC-data** (vlwarmte.nl, 25 apr – 22 mei) meeneemt naast GA4.
**Scope:** leadgeneratie (organisch + betaald), landingskwaliteit, content-gaps die zichtbaar worden in GSC, Google Ads message-match. Geen premature bijsturing op cyclus 9–11-meetdoelen (juni-fetch ~1–15 juni blijft het ijkpunt).
**Bronnen:** `docs/website-manager/analytics_report.md` (22-05), `docs/website-manager/ga4_report.json` (23-05), `docs/website-manager/gsc_report.json` (23-05, 28 dagen), `docs/website-manager/sprint.md` cyclus 12 + addendum laagopbouw, `scripts/data/google_ads_lead_campaign_defaults.json`, `.cursor/skills/google-ads-marketing/SKILL.md`, root-HTML, WebSearch (mei 2026).

> **Ads-uitvoering deze sessie:** harness verbood Bash voor Python-scripts; `google_ads_list_campaigns.py` en `--dry-run`-runs **niet** opnieuw gedraaid. Read-only conclusies komen uit het vorige rapport (campagne `23834672782` ENABLED, €2/dag) plus de defaults-JSON. Bij volgende sessie zonder Bash-block: smoke-test + `list_campaigns` herhalen vóór elke mutatie-aanbeveling.

## Samenvatting

GSC bevestigt wat GA4 alleen suggereerde: **vlwarmte.nl is zichtbaar in heel Noord-Nederland**, maar de meeste vertoningen zitten **buiten pagina 1** (rang 30–80) en leveren dus 0 klikken. Drie patronen springen eruit als concrete leadkans:

1. **`vloerverwarming-hoogeveen.html`** rankt op rang 10,6 voor _vloerverwarming hoogeveen_ (8 vert.) en pakt veel small-town vertoningen (Hollandscheveld, Fluitenberg, Noordscheschut, Elim) — **close-to-page-1** is grijpbaar met title/meta + dorpen-cluster in body.
2. **`prijsindicatie.html`** krijgt 75 GSC-vertoningen en 56 GA4-sessies / ~94 s — maar 0 GSC-clicks (rang 52) **én** 65% entry-bounce op de 20 directe landings. De wizard converteert (24 conv. in GA4-pad), maar als landing voor "vloerverwarming drenthe / zuidlaren" is de eerste schermhelft te zwak.
3. **`vloerverwarming-drenthe`** is de grootste regio-term in GSC (82 vert., 0 clicks, gem. rang 65,7) — gespreid over `/`, `/diensten`, `/prijsindicatie`, `/faq` zonder duidelijke hub. **Geen toegewezen landings-URL** voor "Drenthe"; Google kiest zelf en niemand rankt.

Daarnaast: Paid Search blijft 13 / 0 conv vs Cross-network 64 / 9 conv; GA4↔Ads-attributiesessie staat nog open voor ~1 juni. `projecten.html` rankt al op gem. rang 3,3 op zijn 3 vertoningen — goed nieuws, maar 8 sessies / 0 conv blijft te dun om over bij te sturen.

**Geen `--apply`, geen `--go-live`, geen budgetverhoging deze cyclus.** Wel: kleine content-aanscherpingen die organische impressies omzetten in clicks, plus voorbereiding voor de juni-attributiesessie.

## GA4-kern (30d, fetch 23-05-2026)

| Metric | 23-05 | Trend t.o.v. 22-05 |
| ------ | ----- | ------------------ |
| Sessies (devices) | ~352 (186 desktop + 150 mobile + 16 tablet) | +~3% |
| Homepage `/` | 202 sessies, bounce 60,9% | +4 sessies, bounce stabiel |
| `/prijsindicatie.html` | 56 sessies, ~94 s, bounce 32,1% | stabiel |
| Betaald `google / cpc` | Cross-network 64 / 9; Paid Search 13 / 0 | +3 Cross, Paid ongewijzigd |
| Organic `google` | 8 sessies, 1 conv. | stabiel laag |
| Geo NL — Drenthe / Groningen / Friesland | 174 / 21 / 6 | +2 / +1 / 0 |

**Top entry-landings (selectie):**

| Landing | Sessies | Bounce | Conv. | Opmerking |
| ------- | ------- | ------ | ----- | --------- |
| `/contact.html?modus=offerte` | 11 | 9,1% | 10 | goudstandaard, ongewijzigd |
| `/prijsindicatie.html` | 20 | 65% | 24 | conv. hoog (paths), entry-bounce blijft P1 |
| `/diensten.html` | 15 | 73,3% | 3 | sprint-12 hero-link projecten live (commit `8fff9dd`) |
| `/contact.html` (koud) | 10 | 80% | 12 | intent-strip live; effect pas juni meetbaar |
| `/over-ons.html` | 10 | 80% | 0 | wacht juni-fetch |
| `/projecten.html` | 7 | 100% | 0 | cases live + Drachten-kruislink (cyclus 12) |
| `/vloerverwarming-assen.html` | 6 | 100% | 0 | 7 sessies in 90d engagement, **0 scrollers** |

> Weekvolume blijft laag; landing-cijfers blijven ruis tot juni-fetch.

## GSC-kern (28d, fetch 23-05-2026)

**Top vertoningen (queries, alle clicks 0 tenzij genoemd):**

| Query | Vert. | Gem. rang | Pagina (top) | Kans |
| ----- | ----- | --------- | ------------ | ---- |
| `vloerverwarming drenthe` | **82** | 65,7 | `/` + 4 andere URL's | **regiohub gap** |
| `vloerverwarming zuidlaren` | **33** | 9,3 | `/`, `/contact`, `/prijsindicatie`, `/diensten` | **close-to-page-1**, intern verspreid |
| `installatiebedrijf zuidlaren` | 20 | 6,5 | `/` | rang OK, copy-aanscherping op `/over-ons` of `/` ondertitel kan CTR helpen |
| `vloerverwarming schoonebeek` | 10 | 61,5 | `/` | mismatch — geen Emmen-omgeving binding |
| `vloerverwarming friesland` | 10 | 87,7 | `/vloerverwarming-leeuwarden.html` | rang slecht; Drachten-page beter? |
| `installateur zuidlaren` | 9 | 3,7 | `/` | top-3 organisch — vertaal naar CTR |
| `vloerverwarming hoogeveen` | 8 | 10,6 | `/vloerverwarming-hoogeveen.html` | **page-2-rand**, snelle winst |
| `vloerverwarming leeuwarden` | 7 | 27,3 | `/vloerverwarming-leeuwarden.html` | rang stabiel, body verdiepen |
| `vloerverwarming heerenveen` | 5 | 50,4 | `/vloerverwarming-drachten.html` | mapping klopt, rang slecht |
| `vloerverwarming hollandscheveld` | 6 | 20,3 | `/vloerverwarming-hoogeveen.html` | dorp-binnen-Hoogeveen, kruis-link werkt |
| `vloerverwarming fluitenberg` | 6 | 4,8 | `/vloerverwarming-hoogeveen.html` | **rang 4,8** — al sterk! |
| `warmtepomp zuidlaren` | 4 | 1,8 | `/` | **1 click / 25% CTR** — enige clickende query |

**Top vertoningen (pagina's):**

| Pagina | Vert. | Clicks | Rang |
| ------ | ----- | ------ | ---- |
| `/` (www + non-www) | 190 | 4 | mix 5,6–52,8 |
| `/prijsindicatie.html` | 75 | 0 | 52,0 |
| `/vloerverwarming-hoogeveen.html` | 30 | 0 | 18,3 |
| `/diensten.html` | 27 | 0 | 48,1 |
| `/contact.html` | 21 | 0 | 34 |
| `/vloerverwarming-leeuwarden.html` | 21 | 0 | 60,3 |
| `/vloerverwarming-drachten.html` | 8 | 0 | 37,6 |
| `/systemen-producten.html` | 5 | 0 | 29,4 |
| `/projecten.html` | 3 | 0 | **3,3** |
| `/faq.html` | 5 | 0 | 71 |

**Observaties:**

- `prijsindicatie.html` heeft de **op-één-na-grootste impression share** maar rangt slecht (52) — title/meta past niet bij brede stad/regio-queries die er nu op landen.
- `projecten.html` rangt op gem. rang 3,3 (3 vert.) — Drenthe-cases helpen al; meer crawl-tijd nodig.
- Stad-pagina Hoogeveen pakt 30 vertoningen op rang 18 — title/H1-tweak kan dit naar page-1 trekken.
- Domein non-www (`vlwarmte.nl/`) pakt 81 vert. naast www (109 vert.) — canonical/redirect-status check waard (geen drama; één huishouden naar www).
- `warmtepomp zuidlaren` rangt op 1,8 — niet hun core, maar laat zien dat lokale Zuidlaren-autoriteit gegrond is.

## Top zoekwoorden (indicatief — WebSearch + GSC + defaults)

| Zoekwoord | Volume (indic.) | Concurrentie | Pagina |
| --------- | --------------- | ------------ | ------ |
| vloerverwarming drenthe | hoog (GSC 82 vert.) | hoog (aggregators) | **gap — geen hub** |
| vloerverwarming kosten / per m² | hoog | hoog (aggregators) | `prijsindicatie.html#kosten-uitleg` |
| vloerverwarming hoogeveen | midden | midden | `vloerverwarming-hoogeveen.html` (rang 10,6) |
| vloerverwarming zuidlaren | midden-hoog (lokaal) | laag-midden | meerdere — versnipperd |
| droge vloerverwarming / laagopbouw | midden (groeiend) | midden | `systemen-producten.html#laagopbouw` (live 23-05) |
| schuimbeton vloerverwarming | midden | midden-hoog | `diensten.html#schuimbeton` |
| vloerverwarming leeuwarden / heerenveen / drachten | midden | midden-hoog | city-cluster, rangen 27–50 |
| vloerverwarming renovatie houten vloer | midden | midden | **gap** — alleen sectie op Drachten |
| installateur zuidlaren | laag (lokaal) | laag | `/` (rang 3,7) — vertaal naar CTR |

## Prijscalculator — haalbaarheidsonderzoek

### Conclusie

**Niet opnieuw bouwen.** Conclusie cyclus 12 staat: wizard + `#kosten-uitleg` dekken kosten-intent (56 sessies / 94s / 24 path-conv.). GSC bevestigt dat de pagina vertoningen ophaalt; het echte probleem is **landing-message-match**, niet de wizard-logica.

### Onderbouwing

Aggregators (Solvari, Slimster, Klussendirect) blijven domineren op brede `kosten` SERP's. VLWarmte wint met traject, lokaal bewijs, en heldere bandbreedte — niet met een vlakkere calculator. WebSearch mei 2026: geen nieuwe lokale concurrent met een interactieve calculator in Noord-NL die we onderschat hebben. Wel: meerdere installateurs gebruiken nu een **kort kostenblok in de hero** ("vanaf €X per m², afhankelijk van X factoren") — copy-tweak voor `prijsindicatie.html` ATF, geen nieuwe tool.

### Voorgestelde opbouw wizard

Geen wijziging deze cyclus.

### Leadgeneratie koppeling

`wizard_calculate`, `wizard_lead_submit`, `lead_form_submit` blijven key events. Import naar Ads na GA4↔Ads-fix (skill §A.4). **Risico:** als auto-tagging niet aanstaat, telt Paid Search GA4-conv. niet — verklaart wellicht een groot deel van de 0/13 op Paid Search.

### Risico's en aandachtspunten

- Entry-bounce `prijsindicatie.html` als landing 65% (20 sessies) — pas beoordelen na juni-fetch.
- GSC: 75 vert., rang 52, 0 clicks — title/description matcht waarschijnlijk niet bij `vloerverwarming drenthe` of `vloerverwarming zuidlaren` waar de pagina op verschijnt. Title-tweak overwegen (zie aanbeveling P1 hieronder).

### Aanbeveling aan Product Manager

- **Prioriteit:** Laag (onderhoud + title/meta-aanscherping P1)
- **Ontwikkeltijd:** 0,5–1 uur (alleen title/description) als PM groen licht geeft
- **Effect:** indirect via Ads-attributie + organische CTR

## Content gaps

**Afgevinkt (cyclus 9–12):**

- City-cluster incl. Drachten/Heerenveen; `projecten.html` met echte cases; footer Drachten site-breed; RSA-defaults projecten-copy + `final_urls` projecten; `diensten.html` hero-link projecten; OG-image Drachten; sitemap `lastmod`; laagopbouw-cluster live op `systemen-producten.html#laagopbouw` met FAQ-schema; trust-strip op 7 stad-pagina's; H2 laagopbouw op `vloerverwarming-groningen.html`; defaults aangevuld met laagopbouw-keywords + final URL.

**Open / nieuw zichtbaar in GSC:**

| Gap | GSC-signaal | Voorstel |
| --- | ----------- | -------- |
| **Geen "vloerverwarming Drenthe" hub** | 82 vert., 0 clicks, rang 65,7, verspreid over `/`, `/diensten`, `/prijsindicatie`, `/faq` | Provincie-pagina **óf** sterke Drenthe-section + canonical signaal op `index.html` (zie P1) |
| **`prijsindicatie.html` title/meta** | 75 vert., 0 clicks, rang 52, gepakt op stad/regio-queries | Title herschrijven met regio-anker; meta met richtbedrag-belofte (P1) |
| **`vloerverwarming-hoogeveen.html` close-to-page-1** | 30 vert., rang 18,3; pakt 4 dorpen rondom Hoogeveen | Title/H1-aanscherping + dorpen-lijst in body; **interne link** vanaf `index.html` (P1) |
| **`vloerverwarming-leeuwarden.html` zwakke rang** | 21 vert., rang 60; pakt _vloerverwarming bolsward_, _friesland_ | Body verdiepen met Friesland-context, Heerenveen-link bestaat al via Drachten | (P2) |
| **Renovatie houten vloer** | geen GSC-trekkers nog, sectie alleen op Drachten | Eigen pagina blijft P2-backlog (max. 1 pagina/sprint) |
| **Schoonebeek / Emmen-omgeving** | 10 vert. _schoonebeek_, 1 vert. _emmen_, rangen 60–80 | `vloerverwarming-emmen.html` bestaat — body uitbreiden met dorpenring (Schoonebeek, Klazienaveen, Nieuw-Amsterdam) — (P2) |
| **FAQ-pagina onzichtbaar** | 5 vert., rang 71 | Onderwerp-FAQs op service-pagina's blijven sterker dan losse `/faq.html`; geen actie nodig |

**Niet meer doen / afgewezen deze cyclus:**

- Standalone `vloerverwarming-drenthe.html` voordat GSC-clicks aantonen dat een hub-pagina effectiever is dan de huidige spread. Eerst aanscherpen op `/index.html` + `prijsindicatie.html` titles.
- Nieuwe pagina `vloerverwarming-renovatie-houten-vloer.html` — backlog blijft P2; sprint-12 vol; cyclus-13 vol met meetwacht.
- `vloerverwarming-meppel.html` — keyword pas terug zodra pagina bestaat (sprint-12 verwijderd uit defaults).

## Concurrentie observaties (WebSearch + GSC, mei 2026)

**Wie rankt op Drenthe-termen (top 20 GSC voor _vloerverwarming drenthe_):**

- Aggregators (Solvari, Slimster, Klussendirect, LeadAngels) bovenaan met "tot 6 offertes" en brede prijsranges.
- Lokale spelers: **ReWo & de Jong** (Groningen/Drenthe/Friesland, infrezen), **DRO Renovaties** ("tot 100 m² in 1 dag"), **EcoFloorNoord**, **WarmerHuis** (schuimbeton + warmtepomp-combo), **Faber** (alles-in-één), **vloerverwarminggroningen.com** (lead-aggregator, **niet** installateur — relevant voor laagopbouw-narrative).
- Generieke installateurs uit Randstad pakken regio-pagina's met thin content.

**Waar VLWarmte op kan winnen:**

- **Lokaal bewijs**: Zeegse + Zuidlaren cases op `projecten.html` zijn uniek; geen concurrent in top-20 toont vergelijkbaar werk op homepage of project-detail.
- **Eén traject** (ondervloer → schuimbeton → dekvloer → afwerking) blijft een sterk anker; concurrenten richten zich op één onderdeel.
- **Laagopbouw + droge vloerverwarming**: nieuwe cluster (sprint-12 addendum) onderscheidt VLWarmte van pure-schuimbeton en pure-infrezen-spelers. Concurrent _vloerverwarminggroningen.com_ heeft droogbouw maar is aggregator — vlwarmte wint op installatie-bewijs.
- **Bandbreedtes** in copy ("rondom Zuid-Laren", "binnen één werkdag") matchen Noord-Nederlandse tone of voice — concurrenten gebruiken vaak marketing-claims ("snelste van Nederland", "beste prijs").

**Waar VLWarmte achterloopt:**

- **Snelheids-claims**: ReWo & DRO leiden met dag-snelheid ("tot 100 m² in 1 dag"). VLWarmte heeft dit niet in primaire copy — kan toegevoegd worden in hero `diensten.html` of laagopbouw-sectie zonder superlatief.
- **Subsidie-hooks**: WarmerHuis en EcoFloorNoord noemen ISDE / warmtepomp-subsidie expliciet. VLWarmte noemt warmtepomp wel ("geschikt voor warmtepomp" — extra-RSA), maar geen subsidie-content. **Mogelijk gap** voor FAQ of body-paragraaf — laag prio.

## Google Ads — status en acties

**Secrets:** `secrets/google-ads.env` aanwezig op deze machine. **Geen** scripts gedraaid deze sessie (harness-block op Bash voor Python). Status hieronder is overgenomen uit `analytics_report.md` (22-05) en de defaults-JSON; **bij volgende sessie eerst `google_ads_list_campaigns.py` opnieuw draaien** voor live-bevestiging vóór mutaties.

**Campagne (laatst-bevestigd 22-05-2026):**

| id | channel_type | status | name | daily_budget |
|----|--------------|--------|------|--------------|
| 23834672782 | SEARCH | ENABLED | VLW-API-Leads NL auto | €2/dag |

**Defaults-JSON (na sprint-12 + laagopbouw-addendum):**

- `final_urls`: offerte-deeplink, prijsindicatie, **projecten**, **systemen#laagopbouw**, Groningen, Leeuwarden, Hoogeveen, Drachten — compleet voor huidige intent-spread.
- Geo: Drenthe, Groningen, Friesland.
- Keywords: 32 keywords incl. laagopbouw-cluster; `vloerverwarming meppel` verwijderd.
- `extra_rsa`: projecten-headline + "10 jaar garantie op buis", "Geschikt voor warmtepomp" — klaar voor `--apply`.
- `sitelinks`: 5 sitelinks incl. _Uitgevoerd werk_ → projecten.html.

| Onderwerp | Status | Actie |
| --------- | ------ | ----- |
| GA4 ↔ Ads + auto-tagging | **P0 open** | Sessie ~1 juni; check of `gclid` doorkomt op `?modus=offerte#aanvraag` (deeplink mag geen UTM-overschrijving doen) |
| Conversie-import GA4 → Ads | Open | Primair `wizard_lead_submit` + `contact_submit`; secundair `wizard_calculate` (zie skill §A.4) |
| RSA-variant live | Klaar in defaults, **niet** `--apply` zonder PO | `google_ads_add_rsa_variant.py --dry-run --campaign-id 23834672782` → `--apply` na PO |
| Sitelinks live | `google_ads_add_sitelinks.py` aanwezig in repo (zie sprint-22-mei commit `4fde7b9`) | `--dry-run` herhalen pre-mutatie; check welke sitelinks al live zijn |
| Negatieven | Onbekend (geen recente run) | Wekelijks zoektermen na attributiefix; `google_ads_campaign_next_steps.py negatives` |
| Spend | €2/dag cap | **Niet** verhogen vóór attributiefix + 2 weken Paid Search-conv. > 0 |
| `--go-live` | Reeds ENABLED | n.v.t. — campagne loopt al |

**Voorgestelde defaults-aanpassingen (geen API-run deze sessie):**

1. **Headline-experiment in `extra_rsa`:** vervang één van de "10 jaar garantie op buis" / "Geschikt voor warmtepomp" door **"Vloerverwarming binnen 1 dag"** of **"In één dag geïnstalleerd"** (max. 30 tekens — controleren op exacte char-count: `In één dag geïnstalleerd` = 25 tekens ✓). Reden: concurrent DRO leidt op snelheid; VLWarmte heeft dit niet in copy. Alleen toepassen op laagopbouw/infrezen-cases — niet voor schuimbeton-cases waar 1 dag onrealistisch is. Risico: ad-policy "exceptional claim" — voeg "vaak" of "tot 100 m²" toe om kwantificeerbaar te zijn.
2. **Sitelink-variant `Drenthe-projecten`:** als sitelink `Drachten & Heerenveen` te smal blijft (alleen Friesland), overweeg variant `Cases Drenthe` → `projecten.html`. Pas na `google_ads_add_sitelinks.py --dry-run` om huidige live-staat te zien.
3. **Negatieven-lijst aanvullen** (na zoekterm-rapport in juni-sessie): `meppel`, `huur`, `zelf aanleggen`, `cursus`, `vacature`, evt. `vlaanderen` / `belgie`.

## Aanbevelingen voor Product Manager (max. 8)

| # | P | Tag | Voorstel | Onderbouwing | Actie |
| - | - | --- | -------- | ------------ | ----- |
| 1 | **P0** | Ads / meet | **GA4 ↔ Ads + Paid Search-attributie** | 13 Paid Search-sessies / 0 conv vs 64 Cross / 9 conv; mogelijk auto-tagging mist op deeplink | Sessie ~1 juni: link, auto-tagging-check, conversie-import, geen budget↑ |
| 2 | **P0** | Analytics | **Cyclus 9–11 niet bijsturen vóór juni-fetch** | Projecten 100% entry-bounce / 7 sessies, over-ons 80% / 0 conv, Assen 0 scrollers — ~6 dagen post-cyclus-11 | Fetch 1–15 juni; harde beoordeling sprint-11 + sprint-12 meetdoelen |
| 3 | **P1** | SEO / CRO | **`prijsindicatie.html` title + meta herschrijven** | 75 GSC-vert., rang 52, 0 clicks; pakt regio-queries waar title niet bij past | Title: "Prijsindicatie vloerverwarming Drenthe & Noord-NL — richtbedrag in 2 minuten"; meta: richtbedrag + vrijblijvend + werkgebied. ~0,5 uur Developer; meet via GSC CTR over 4 weken |
| 4 | **P1** | SEO | **`vloerverwarming-hoogeveen.html` title + dorpen-lijst** | 30 GSC-vert., rang 18,3; pakt al Fluitenberg (rang 4,8), Hollandscheveld (20,3), Noordscheschut (33,8), Elim (14,5) zonder dat ze in body staan | Title: "Vloerverwarming Hoogeveen, Hollandscheveld & omgeving — installateur uit Zuidlaren"; alinea "Ook actief in" met 5–6 dorpen; interne link vanaf `index.html` services-blok. ~1 uur |
| 5 | **P1** | SEO | **Drenthe-hub: section-aanscherping op `index.html`** | 82 GSC-vert. `vloerverwarming drenthe` spread over 5 URL's, rang 65,7; geen kanonieke hub | Geen nieuwe pagina (max. 1/sprint, capaciteit op). In plaats daarvan: H2 of compacte hub-sectie op `index.html` ("Vloerverwarming in heel Drenthe") met links naar stad-pagina's + `projecten.html` + `prijsindicatie.html`. Internal-link signaal naar `/` als de-facto hub. ~1 uur |
| 6 | **P1** | Ads | **RSA-variant + sitelinks-status live zetten (na PO + bash-toegang)** | Defaults klaar; campagne ENABLED €2/dag | `google_ads_list_campaigns.py` → `google_ads_add_rsa_variant.py --dry-run --campaign-id 23834672782` → rapport → `--apply` na PO. Geen `--go-live` (al live). Geen budgetverhoging |
| 7 | **P2** | SEO / dev | **Renovatie houten vloer pagina** | Commerciële gap (cyclus 11+12 backlog); WebSearch toont geen sterke Noord-NL-pagina hierop | Eigen pagina `vloerverwarming-houten-vloer.html` met FAQ-kruislink + wizard-CTA. Plan voor cyclus 14 (na juni-fetch + Drenthe-hub) — niet deze sprint |
| 8 | **P2** | SEO | **`vloerverwarming-emmen.html` body uitbreiden met dorpenring** | 10 GSC-vert. _schoonebeek_ landt op `/` (rang 61,5), niet op Emmen-pagina | Body op Emmen-pagina met Schoonebeek, Klazienaveen, Nieuw-Amsterdam, Coevorden-grens; kruis-link naar Hoogeveen. Backlog cyclus 14 |

## Concrete developer-voorstellen (cyclus 13, alleen na PM-go)

1. **`prijsindicatie.html` title + meta** (P1 #3) — alleen `<title>` en `<meta name="description">`; geen HTML-body-wijziging. Acceptatie: GSC CTR voor pagina stijgt van 0% naar >0,5% binnen 4 weken (juni-eind-fetch).
2. **`vloerverwarming-hoogeveen.html` title + dorpen-blok** (P1 #4) — title + één paragraaf "Ook actief in: Hollandscheveld, Fluitenberg, Noordscheschut, Elim, Tiendeveen". Geen nieuwe sectie-H2; in bestaande "Ook actief in"-stijl van Drachten. Interne link vanaf `index.html` services-blok ("Vloerverwarming in Hoogeveen e.o."). Acceptatie: rang naar <10 binnen 4 weken op `vloerverwarming hoogeveen` of >1 GSC-click.
3. **`index.html` Drenthe-hub-sectie** (P1 #5) — H2 of een compacte "regio-grid" tussen bestaande secties met links naar Groningen / Assen / Hoogeveen / Emmen / Drachten / Leeuwarden / Zuidlaren-stad-pagina's + projecten + prijsindicatie. Geen extra hero-CTA. Acceptatie: `index.html` rangt op rang <30 voor `vloerverwarming drenthe` (nu 63,4 op `/`) binnen 6 weken.
4. **Geen wijziging** aan `projecten.html` / `over-ons.html` / `diensten.html` / Assen tot juni-fetch — meetvenster cyclus 9–12 nog open.
5. **Tracking** (alleen check, geen code): controleer dat `?modus=offerte#aanvraag` geen UTM-overschrijving doet die `gclid` van Ads kapot maakt. Test-URL: `?modus=offerte&gclid=test123#aanvraag` → verwacht `gclid` blijft in URL en `_ga`-cookie.
6. **Ads** (alleen na PO + bash-toegang): herhaal `google_ads_list_campaigns.py`, dan `--dry-run` op `add_rsa_variant` en `add_sitelinks` om delta te tonen vóór `--apply`.

## Uitgesteld / niet deze cyclus

- Budgetverhoging > €2/dag — pas na 2 weken Paid Search-conv. > 0 én GA4↔Ads gelinkt.
- `--go-live` — niet relevant (campagne al ENABLED).
- PMax/image-campagnes — geen capaciteit, geen meetbasis.
- Standalone `vloerverwarming-drenthe.html` — eerst section-aanscherping op `/` testen.
- `vloerverwarming-renovatie-houten-vloer.html` — cyclus 14.
- Assen hero-herontwerp — wacht juni-fetch.
- Friesland-cluster (Leeuwarden body verdiepen, Heerenveen sub-page) — wacht op Drachten >0 organische sessies in GA4.
- Snelheids-claim in RSA — alleen na compliance-check en sub-set keywords (laagopbouw/infrezen).
- Subsidie-content (ISDE / warmtepomp) — laag prio; backlog cyclus 15+.
- NL-only GA4-segment — US-bots in geo lijst (Oregon 13, Colorado 11, Iowa 5) zijn ruis maar geen lead-impact.

## Seizoenspatroon (indicatief)

Mei–juli: verbouw- en kostenintent — `prijsindicatie.html` + `#kosten-uitleg` blijven kern. **Renovatie-houten-vloer** piekt typisch september–november (planning voor stookseizoen) — pagina-launch idealiter voor 1 september. Schuimbeton/kruipruimte: stabiele intent jaarrond, piek februari–april (voor bouwseizoen) en augustus–september.

## Meetdoel deze cyclus (cyclus 13)

Geen nieuwe meetdoelen toevoegen; **bewaak** open meetdoelen cyclus 9–12 + addendum laagopbouw:

- (a) Harde beoordeling cyclus 9–11 meetdoelen (juni-fetch).
- (b) ≥1 organische sessie `vloerverwarming-drachten.html` (GA4).
- (c) `projecten.html` entry-bounce <90% bij ≥10 entry-sessies.
- (d) Paid Search-attributie vastgelegd in PM-notitie (juni-sessie).
- (e) `diensten.html` landing bounce/conv niet verslechterd.
- (f) **Nieuw**: ≥1 organische sessie `systemen-producten.html` met laagopbouw-query in GSC (addendum sprint 12).

**Bij PM-go op P1 #3-#5:** voeg toe:
- (g) `prijsindicatie.html` GSC CTR >0,5% in 4-weekse fetch.
- (h) `vloerverwarming-hoogeveen.html` gem. rang <10 of ≥1 GSC-click op `vloerverwarming hoogeveen`.
- (i) `index.html` zichtbaar op rang <30 voor `vloerverwarming drenthe`.

---

**Tone:** nuchter, direct — conform AGENTS.md. Geen secrets of tokens in dit document. Geen `--apply` / `--go-live` aanbevolen zonder expliciete PO-goedkeuring én herhaalde read-only Ads-check.
