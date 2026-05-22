# Marketing Research Rapport — 22 mei 2026

**Cyclus 12** — eerste research na cyclus-11-deploy (20 mei): echte cases Zeegse/Zuidlaren op `projecten.html`, Drachten in footer + sitemap, RSA-defaults met projecten-copy, `diensten.html` hero-CTA aangepast (zie opmerking hieronder).
**Scope:** leadgeneratie (organisch + betaald), landingskwaliteit, contentgaps, Google Ads message-match, meetplan juni — **geen premature bijsturing** op cyclus 9–11-meetdoelen.
**Bronnen:** `.claude/commands/marketing-research-agent.md`, `.cursor/skills/google-ads-marketing/SKILL.md`, WebSearch (mei 2026), `docs/website-manager/ga4_report.json` (export **`2026-05-22T17:32:56`**), `docs/website-manager/analytics_report.md` (20-05, ter referentie), `docs/website-manager/archive/sprint-2026-05-22.md`, root-HTML + `sitemap.xml`, `scripts/data/google_ads_lead_campaign_defaults.json`, read-only `google_ads_list_campaigns.py`.

## Samenvatting

Cyclus 11 staat **~2 dagen live** op het moment van deze fetch (4 dagen na deploy) — te vroeg om projecten-bounce, over-ons-entry of Assen-scroll hard te beoordelen. Wel zichtbaar: **betaald blijft gesplitst** (Cross-network 61 sessies / 9 conversies vs Paid Search 13 / 0); **offerte-deeplink** blijft de sterkste route (9,1% entry-bounce, 10 conv op 11 sessies). Echte projectcases en RSA-copy in defaults zijn klaar voor **message-match**; live Ads-sync (`--apply`) blijft achter tot PO + attributiesessie. **Geen `--go-live`**, geen budgetverhoging.

## GA4-kern (30d, fetch 22-05-2026)

| Metric | 22-05 | Trend t.o.v. 20-05 |
| ------ | ----- | ------------------- |
| Sessies (devices) | **~343** (181+149+13) | +~6% |
| Homepage `/` | 198 sessies, bounce **60,1%** | +16 sessies |
| `/prijsindicatie.html` | 56 sessies, **~94 s**, bounce **32,1%** | stabiel sterk |
| Betaald `google / cpc` | Cross-network **61 / 9 conv**; Paid Search **13 / 0** | meer Cross-sessies, Paid Search ongewijzigd |
| Organic `google` | 8 sessies, 1 conv | stabiel laag |
| NL — Drenthe / Groningen / Friesland | 172 / 20 / **6** | Friesland +2 |

**Landings (instap, selectie):**

| Landing | Sessies | Bounce | Conv. | Opmerking cyclus 11 |
| ------- | ------- | ------ | ----- | ------------------- |
| `/contact.html?modus=offerte` | 11 | **9,1%** | 10 | ongewijzigd goudstandaard |
| `/contact.html` (koud) | 10 | **80%** | 12 | nog geen effect intent-strip |
| `/diensten.html` | 15 | **73,3%** | **3** | vroeg signaal conv., sample klein |
| `/projecten.html` | 7 | **100%** | 0 | cases live; nog geen verbetering |
| `/over-ons.html` | 10 | **80%** | 0 | vervolg-CTA onderaan raakt entry niet |
| `/vloerverwarming-assen.html` | 6 | **100%** | 0 | 0 scrollers (90d) |
| `vloerverwarming-drachten.html` | — | — | — | **niet** in top/entry (0 meetbaar) |

**Weekvolume:** 49 sessies (15–21 mei) — blijft laag; landing-cijfers blijven ruis tot juni-fetch (~1–15 juni).

## Top zoekwoorden (indicatief — WebSearch + site/defaults)

| Zoekwoord | Volume (indic.) | Concurrentie | Pagina |
| --------- | --------------- | ------------ | ------ |
| vloerverwarming kosten / per m² | hoog | hoog (aggregators) | `prijsindicatie.html#kosten-uitleg` |
| prijs vloerverwarming / prijsindicatie | hoog | hoog | `prijsindicatie.html` (wizard) |
| vloerverwarming groningen / assen | hoog | hoog lokaal + aggregators | city-pagina’s |
| vloerverwarming drachten / heerenveen / leeuwarden | midden | midden-hoog | `vloerverwarming-drachten.html` enz. |
| schuimbeton vloerverwarming | midden | midden-hoog (EcoFloorNoord, WarmerHuis) | `diensten.html#schuimbeton` |
| vloerverwarming installateur [stad] | midden-hoog | hoog (Solvari, lead-platforms) | city-cluster |
| vloerverwarming renovatie houten vloer | midden | midden | **gap** — geen eigen URL |
| vloerverwarming meppel | laag-midden | midden | keyword in defaults, **geen** pagina |
| kruipruimte isoleren schuimbeton | midden | midden | diensten + wizard |

## Prijscalculator — haalbaarheidsonderzoek

### Conclusie

**Niet opnieuw bouwen.** Wizard + `#kosten-uitleg` dekken kosten-intent; 56 sessies / ~94 s gem. duur bevestigen engagement.

### Onderbouwing

Aggregators (Vastlegg, Klussendirect, LeadAngels) en content-sites domineren brede kosten-SERP’s met generieke €/m²-tools. VLWarmte wint met **traject** (kruipruimte-diepte, schuimbeton-bandbreedte) en **lokaal bewijs** (`projecten.html`), niet met een vlakkere calculator.

### Voorgestelde opbouw wizard

Geen wijziging deze cyclus.

### Leadgeneratie koppeling

Blijf `wizard_calculate`, `wizard_lead_submit`, `lead_form_submit` als key events; import naar Ads na GA4↔Ads-fix (skill §A).

### Risico's en aandachtspunten

Entry-bounce `prijsindicatie.html` als landing **65%** (20 sessies) — pas beoordelen na juni-fetch.

### Aanbeveling aan Product Manager

- **Prioriteit:** Laag (onderhoud/meting)
- **Ontwikkeltijd:** 0
- **Effect:** indirect via Ads-attributie + projectcases

## Content gaps

**Afgevinkt (cyclus 9–11):**
- City-cluster incl. Drachten/Heerenveen; `projecten.html` in sitemap; echte cases Zeegse/Zuidlaren; footer Drachten site-breed; RSA-defaults projecten-copy; interne link “Bekijk uitgevoerd werk” op `index.html`.

**Open / zwak:**
- **`projecten.html`:** inhoud live, **entry 100% bounce** (7 sessies) — meet pas na 2–4 weken; optioneel OG-beeld + tweede Zeegse-foto (developer backlog).
- **`vloerverwarming-drachten.html`:** 0 GA4-sessies — indexering + tijd; footer/sitemap/defaults kloppen.
- **`diensten.html` ATF:** cyclus-11 duo-CTA onder hero is **later verwijderd** (commit `b040cea` — minder dubbele CTA’s). Landing toont nu één primaire knop naar prijsindicatie; onderaan nog `cta-band`. **Niet opnieuw tweaken vóór juni-fetch** tenzij PM bewust terug wil naar sprint-opzet.
- **`vloerverwarming-renovatie-houten-vloer.html`:** commerciële gap; max. 1 nieuwe pagina per sprint — volgende cyclus.
- **`vloerverwarming-meppel.html`:** keyword in defaults zonder URL — pauzeren in Ads of pagina later.
- **`vloerverwarming-assen.html`:** 0 scrollers 90d — hero-backlog na juni.
- **`contact.html` zonder query:** 80% entry-bounce — doorlaten.

**Sitemap (22-05):** 17 URL’s incl. `projecten.html` (`lastmod` 2026-05-20); geen `logo-varianten.html` (correct).

## Concurrentie observaties (WebSearch, mei 2026)

**Wie rankt / adverteert op kerntermen:**
- **Aggregators:** Solvari, Slimster, Klussendirect, LeadAngels — “tot X offertes”, brede prijsranges.
- **Lokaal Noord-NL:** ReWo & de Jong (Groningen/Drenthe/Friesland, infrezen), vloerverwarminggroningen.com, DRO Renovaties (“tot 100 m² in 1 dag”), Infloor/ComfortFloors-stijl spelers op infrezen-prijsclaims.
- **Schuimbeton-combo:** EcoFloorNoord, WarmerHuis, Faber — alles-in-één + kostencontent + subsidie-hooks.

**Waar VLWarmte kan winnen:** één traject particulier renovatie/nieuwbouw; **echte foto’s** uit `beeldmateriaal/` (geen AI); nuchtere bandbreedte; bewezen `?modus=offerte#aanvraag`; nu ook **uitgevoerd werk** op `projecten.html`.

## Google Ads — status en acties

**Secrets op onderzoeks-machine:** `secrets/google-ads.env` **aanwezig** — alleen **read-only** verificatie uitgevoerd; **geen** `--apply`, `--go-live`, geo/keyword-mutaties of spend (conform opdracht).

**Campagne (read-only 22-05-2026):**

| id | channel_type | status | name |
|----|--------------|--------|------|
| 23834672782 | SEARCH | ENABLED | VLW-API-Leads NL auto |

**Defaults (`google_ads_lead_campaign_defaults.json`):**
- `extra_rsa` bevat “Bekijk uitgevoerd werk” + description met `projecten.html` — **repo klaar**, live RSA mogelijk nog oud tot `--apply`.
- `final_urls`: offerte-deeplink, prijsindicatie, Leeuwarden, Hoogeveen, Drachten — **`projecten.html` ontbreekt** (voorstel hieronder).
- Geo: Drenthe, Groningen, Friesland.
- Keyword `vloerverwarming meppel` zonder landingspagina.

| Onderwerp | Actie |
| --------- | ----- |
| GA4 ↔ Ads | **P0** — Paid Search 0 conv vs Cross-network 9 conv; skill §A (~1 juni gepland) |
| RSA sync | Na PO: `google_ads_add_rsa_variant.py --dry-run --campaign-id 23834672782` → `--apply` |
| Spend | Campagne ENABLED — geen opschalen vóór attributiefix + expliciete PO-goedkeuring |
| Negatives | Wekelijks zoektermen; `google_ads_campaign_next_steps.py negatives` indien nodig |

### Voorstel defaults-JSON (geen API-run)

1. Voeg toe aan `final_urls`: `https://www.vlwarmte.nl/projecten.html` (sitelink / variant voor vertrouwen-intent).
2. Overweeg headline in primaire RSA: “Projecten in Drenthe — bekijk foto’s” (max. 30 tekens controleren).
3. **Pauzeer of negatief** `vloerverwarming meppel` tot `vloerverwarming-meppel.html` bestaat, of plan pagina in backlog.

## Aanbevelingen voor Product Manager (max. 5)

| P | Tag | Voorstel | Onderbouwing | Actie |
| - | --- | -------- | ------------ | ----- |
| **P0** | Ads / meet | **GA4 ↔ Ads + Paid Search-attributie** | 13 Paid Search-sessies / 0 conv vs 61 Cross-network / 9 conv | Sessie ~1 juni: link, auto-tagging, conversie-import, Final URL’s in UI; geen budget↑ |
| **P0** | Analytics | **Cyclus 9–11 niet bijsturen vóór juni-fetch** | Projecten entry 100%, over-ons 80%/0 conv, Assen 0 scrollers — ~4d post-cyclus-11 | Fetch 1–15 juni; harde beoordeling meetdoelen sprint 11 |
| **P1** | Ads | **RSA-variant met projecten-copy live zetten (na PO)** | Defaults klaar; live campagne kan nog “referenties op aanvraag” tonen | `--dry-run` → `--apply` op `google_ads_add_rsa_variant.py`; geen `--go-live` |
| **P1** | SEO | **Drachten indexering afwachten + Search Console** | 0 sessies op nieuwe pagina; footer/sitemap/defaults OK | URL inspecteren; geen extra city-pagina deze cyclus |
| **P2** | SEO / dev | **Backlog: renovatie houten vloer + Meppel-keuze** | Commerciële gap; meppel-keyword mismatch | Max. 1 nieuwe HTML/sprint; anders keyword pauzeren in defaults |

## Concrete developer-voorstellen (cyclus 12, alleen na PM-go)

1. **Geen wijziging** aan `projecten.html` / `over-ons.html` / Assen **tot juni-fetch** — tenzij meetdoelen expliciet falen na 4 weken data.
2. **`projecten.html` (optioneel P2 na juni):** OG-image uit Zeegse/Zuidlaren i.p.v. `og-default.png`; `zeegse-2.jpeg` in case-card.
3. **`diensten.html`:** alleen als juni-fetch landing nog >70% bounce **én** 0 conv: heroverweeg compacte duo-CTA onder hero (zoals cyclus 11, verwijderd in `b040cea`) — acceptatie: bounce <70% of ≥1 conv op ≥15 entry-sessies.
4. **`over-ons.html`:** bij aanhoudend 80% entry / 0 conv na juni: één ATF-knop prijsindicatie of offerte-deeplink in hero (niet alleen onderaan).
5. **`vloerverwarming-renovatie-houten-vloer.html`:** nieuwe pagina met FAQ-kruislink + wizard/contact-CTA; 1 sprint, geen tweede city-pagina tegelijk.
6. **Tracking:** geen nieuwe events; wel controleren dat Ads-auto-tagging `gclid` op offerte-deeplink landt.

## Uitgesteld

- Budgetverhoging, `--go-live`, PMax/image-campagnes.
- Assen hero-herontwerp, NL-only GA4-segment, `logo-varianten.html`-ruis.
- Friesland-cluster (Leeuwarden/Heerenveen apart) tot Drachten >0 organisch.
- Social: handmatige posts uit `weekly_calendar.md` — na live projecten mogen Zeegse/Zuidlaren in captions.

## Seizoenspatroon (indicatief)

Mei–augustus: verbouw- en kostenintent — `#kosten-uitleg` + wizard blijven kern. September–november: planning renovatie/warmtepomp in RSA pas na **betrouwbare** betaalde data post-attributiefix.

---

**Tone:** nuchter, direct — conform AGENTS.md. Geen secrets of tokens in dit document.
