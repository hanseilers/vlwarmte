# Marketing Research Rapport — 1 juni 2026

**Cyclus 14** — eerste research na sprint-13-deploy (26 mei, commit `47a9583`: prijsindicatie title/meta, Drenthe-hub op `/`, Hoogeveen-dorpen, werkwijze-links op diensten/projecten).
**Scope:** leadgeneratie (organisch + betaald), landingskwaliteit, content-gaps, Google Ads message-match. GSC ontbreekt deze cyclus — SEO-evaluatie sprint 13 uitgesteld tot GSC-OAuth.
**Bronnen:** `docs/website-manager/analytics_report.md` (01-06), `docs/website-manager/ga4_report.json` (01-06T11:03), vorig rapport (26-05), `scripts/data/google_ads_lead_campaign_defaults.json`, `.cursor/skills/google-ads-marketing/SKILL.md`, root-HTML, WebSearch (juni 2026).

> **Ads-uitvoering deze sessie:** `google_ads_list_campaigns.py` bevestigt campagne `23834672782` SEARCH ENABLED (€2/dag). `create_search_campaign --dry-run` faalt verwacht (campagnenaam bestaat al). Defaults-JSON aangepast: RSA `final_urls` teruggebracht tot offerte-deeplink + prijsindicatie. **Geen `--apply`, geen `--go-live`.** Live RSA in Ads UI handmatig syncen — geen update-script in repo.

## Samenvatting

Verkeer normaliseert na de campagne-piek (206 sess/30d vs 352 vorige fetch); post-piek ~50 sess/week is realistischer. Het echte probleem blijft **Paid Search 13 sess / 0 conv.** terwijl `contact.html?modus=offerte` **10 conv. op 11 entry-sess** haalt. Waarschijnlijke oorzaak: RSA met **8 final URLs** liet Google op `/` (67% entry-bounce) of zwakke pagina's landen — defaults zijn nu teruggebracht tot 2 conversie-URL's.

Drie leadkansen voor juni:

1. **Attributie + landing fix betaald** — GA4↔Ads koppeling afronden én live RSA final URL op offerte-deeplink zetten (P0).
2. **`vloerverwarming-assen.html` layout-fix** — 90d 7 sess / 0,7 s / 0 scrollers; Developer-rapport cyclus 13 klaar (P0 content).
3. **GSC OAuth** — blocker voor sprint-13 SEO-check (prijsindicatie CTR, Hoogeveen-rang, Drenthe-hub); zonder GSC blijft organische optimalisatie giswerk.

Sprint-13-wijzigingen (Drenthe-hub, prijsindicatie-title) zijn **6 dagen live** — te vroeg voor harde meting; juni-fetch ~22 juni is ijkpunt.

## GA4-kern (30d, fetch 01-06-2026)

| Metric | 01-06 | Trend t.o.v. 23-05 |
| ------ | ----- | ------------------ |
| Sessies (devices) | **206** (119 desktop + 70 mobile + 17 tablet) | ↓ −41%* |
| Homepage `/` | 147 sess, bounce **66%**, gem. **35 s** | ↓ sessies; bounce ↑ |
| `/prijsindicatie.html` | 35 sess, **86 s**, bounce 34% | ↓ sessies; engagement stabiel |
| Betaald `google / cpc` | Cross-network **75 / 20**; Paid Search **13 / 0** | Cross +11 conv.; Paid ongewijzigd |
| Organic `google` | 8 sess, 1 conv. | stabiel mager |
| Facebook (3 bronnen) | 20 sess, 0 conv. | ↓ sess; conv nog nul |
| Geo NL — Drenthe / Groningen / Friesland | 62 / 23 / 8 | Friesland +2 |

\*Deels meetvenster-effect: piekweek 172 sess (27 apr–3 mei) rolt uit venster. Stabiel post-piek: ~49–56 sess/week.

**Top entry-landings (selectie):**

| Landing | Sessies | Bounce | Conv. | Opmerking |
| ------- | ------- | ------ | ----- | --------- |
| `/contact.html?modus=offerte` | 11 | **9,1%** | **10** | goudstandaard campagne-landing |
| `/prijsindicatie.html` | 12 | 58,3% | 8 | conv. hoog als pad; entry-bounce koud |
| `/` | 138 | **67,4%** | 37 | veel conv. via direct/retour; slechte Search-landing |
| `/werkwijze.html` | 2 | 0% | **4** | sterk signaal; volume laag |
| `/diensten.html` | 4 | 75% | 0 | werkwijze-link net live; te vroeg |
| `/projecten.html` | 2 | 50% | 0 | 90d zwak (14 s gem.) |

## Top zoekwoorden (indicatief — WebSearch + vorig GSC + defaults)

| Zoekwoord | Volume (indic.) | Concurrentie | Pagina |
| --------- | --------------- | ------------ | ------ |
| vloerverwarming drenthe | hoog | hoog (aggregators) | `/` Drenthe-hub (live 26-05) — effect juni-fetch |
| vloerverwarming kosten / per m² | hoog | hoog | `prijsindicatie.html` |
| vloerverwarming hoogeveen | midden | midden | `vloerverwarming-hoogeveen.html` (vorig GSC rang 10,6) |
| vloerverwarming zuidlaren | midden-hoog (lokaal) | laag-midden | versnipperd over meerdere URL's |
| droge vloerverwarming / laagopbouw | midden (groeiend) | midden | `systemen-producten.html#laagopbouw` |
| schuimbeton vloerverwarming | midden | midden-hoog | `diensten.html#schuimbeton` |
| vloerverwarming heerenveen | laag-midden | midden | **gap** — geen dedicated pagina; keyword in Ads |
| vloerverwarming groningen / leeuwarden / drachten | midden | midden-hoog | city-pagina's; dun GA4-volume |
| vloerverwarming renovatie houten vloer | midden | midden | sectie Drachten; geen eigen pagina |
| installateur zuidlaren | laag (lokaal) | laag | `/` (vorig GSC rang 3,7) |

**Seizoenspatroon (WebSearch, indicatief):** interesse piekt richting herfst/winter (okt–dec) en bij renovatie-planning in voorjaar (apr–mei). Installaties plannen buiten winterpiek geeft kortere wachttijden — copy-kans op `werkwijze.html` en contact-CTA's ("plan nu voor najaar").

## Prijscalculator — haalbaarheidsonderzoek

### Conclusie

**Niet opnieuw bouwen.** De wizard op `prijsindicatie.html` is live, meetbaar (35 sess / 86 s / 34% bounce) en levert conv. op in het pad. Concurrenten (Benelux, DIJKO, aggregators) gebruiken vaste m²-banden of offerte-formulieren — geen interactieve calculator die VLWarmte mist.

### Onderbouwing

- VLWarmte-wizard dekt productkeuze, schuimbeton-band, kruipruimte-diepte — dieper dan Vastlegg/Ikbenbint (technische buislengte-calculators, geen trajectprijs).
- WebSearch juni 2026: leadplatforms (Slimster, BeterEnergie) domineren op brede kosten-SERP's; lokale installateurs winnen op vertrouwen + regio, niet op calculator-features.
- GA4: entry-bounce prijsindicatie als landing 58% (12 sess) — message-match ATF, geen extra tool.

### Voorgestelde opbouw wizard

Geen wijziging. Bestaande flow (product → oppervlakte → ondergrond → band → lead-form) blijft.

### Leadgeneratie koppeling

Key events: `wizard_lead_submit`, `contact_submit`. Import naar Ads na GA4↔Ads-fix. Prijs-keywords in Search-campagne landen op `prijsindicatie.html` (nu enige secundaire RSA-URL in defaults).

### Risico's en aandachtspunten

- Prijsindicatie is **indicatie**, geen offerte — disclaimer blijft zichtbaar houden.
- Schuimbeton-band zonder contactgegevens kan tire-kickers aantrekken; lead-form na band is juiste filter.

### Aanbeveling aan Product Manager

- **Prioriteit:** Laag (onderhoud)
- **Ontwikkeltijd:** 0 uur nieuwe build
- **Effect:** bestaande wizard blijft kernconverter; focus op landing/attributie

## Content gaps

**Recent afgevinkt (sprint 12–13):**

Laagopbouw-cluster, Drenthe-hub op `/`, Hoogeveen-dorpen, prijsindicatie title/meta, werkwijze-links diensten/projecten, trust-strips stad-pagina's.

**Open / actueel:**

| Gap | Signaal | Voorstel |
| --- | ------- | -------- |
| **`vloerverwarming-assen.html` kapotte UX** | 90d 7 sess / 0,7 s / 0 scrollers | Layout-fix cyclus 14 (zie #2) |
| **`vloerverwarming heerenveen` zonder pagina** | Keyword in Ads; Friesland 8 sess | Pagina cyclus 15 **of** keyword pauzeren na GSC |
| **Drenthe-hub effect** | Hub 6 dagen live | Juni-fetch + GSC: rang _vloerverwarming drenthe_ op `/` |
| **Renovatie houten vloer** | Concurrenten (Bull, ThermoLamina) hebben droogbouw-pagina's | Sectie op Drachten/systemen; eigen pagina P2-backlog |
| **`vloerverwarming-meppel`** | Geen pagina; keyword verwijderd uit defaults | Pagina of blijven weg — discipline 1 city/sprint |
| **Emmen-dorpenring** | Schoonebeek-termen vorig GSC | `vloerverwarming-emmen.html` body uitbreiden (P2) |

**Afgewezen deze cyclus:**

- Standalone `vloerverwarming-drenthe.html` — hub op `/` net live; thin-content-risico.
- Budgetverhoging Ads >€2/dag — Paid Search nog 0 conv.
- Hero-CTA homepage wijzigen — Drenthe-hub effect eerst meten.

## Concurrentie observaties (WebSearch, juni 2026)

**Lokale spelers Noord-NL:**

- **ReWo & de Jong** (Siddeburen) — drie provincies, infrezen, geen voorrijkosten-claim.
- **Kentech** (Groningen-Assen) — breed werkgebied, blog/FAQ.
- **DIJKO** (Leeuwarden) — €55–75/m² in copy, warmtepomp-combo.
- **Groningen Vloerverwarming / groningenvloerverwarming.com** — Therminon-merk, lead-aggregator.

**Aggregators:** Solvari, BeterEnergie, Slimster — "vergelijk 4 offertes", domineren brede SERP's.

**Laagopbouw/droogbouw:** Bull Vloerverwarming, ThermoLamina, Variokomp/Technea, WARP Systems — product×uitleg-pagina's; VLWarmte onderscheidt met **installatie + schuimbeton-traject** op `systemen-producten.html#laagopbouw`.

**Waar VLWarmte wint:**

- Echt projectwerk (Zeegse, Zuidlaren) vs stockfoto's.
- Compleet traject (ondervloer → schuimbeton → dekvloer).
- Online richtbedrag-wizard — zeldzamer bij lokale installateurs.

**Waar VLWarmte achterloopt:**

- Snelheidsclaims ("100 m² per dag") bij ReWo/DRO — optioneel in copy zonder superlatief.
- Subsidie-hooks (ISDE/warmtepomp) — laag prio FAQ-toevoeging.
- Stad-pagina Assen UX vs Groningen-template.

## Google Ads — status en acties

**Verificatie deze sessie:**

```
id=23834672782 | SEARCH | ENABLED | VLW-API-Leads NL auto | €2/dag
```

**Defaults-JSON wijziging (01-06, committed in repo):**

| Veld | Was | Nu |
| ---- | --- | -- |
| `final_urls` | 8 URL's incl. projecten, city-pagina's, laagopbouw | **2 URL's:** offerte-deeplink + prijsindicatie |
| Reden | GA4 Paid Search 0/13; `/` entry 67% bounce | Google rotatie naar zwakke landings voorkomen |

Sitelinks ongewijzigd (projecten, werkwijze, Drachten blijven secundaire paden).

| Onderwerp | Status | Actie |
| --------- | ------ | ----- |
| GA4 ↔ Ads + auto-tagging | **P0 open** | Admin-koppeling + gclid-test op offerte-deeplink |
| Live RSA final URLs | **P0 — handmatig** | Ads UI: bestaande RSA → enkel `contact.html?modus=offerte#aanvraag` (prijs-keywords: prijsindicatie) |
| Conversie-import | Open | `contact_submit` + `wizard_lead_submit` primair |
| RSA-variant (`extra_rsa`) | Klaar in defaults | `--apply` pas na attributiefix + PO-akkoord |
| Negatieven | Onbekend | `google_ads_campaign_next_steps.py negatives` na 2–4 weken search terms |
| Heerenveen keyword | Actief, geen pagina | Pauzeren na GSC **of** pagina cyclus 15 |

**Geen `--go-live`** — campagne draait al ENABLED; geen budgetwijziging zonder PO.

## Aanbevelingen voor Product Manager

### 1. Paid Search landing + GA4↔Ads — deze week
- **Prioriteit:** Hoog (P0)
- **Type:** Google Ads / Analytics
- **Onderbouwing:** Paid Search **13 sess / 0 conv.** vs offerte-deeplink **10 conv. / 11 sess.** RSA had 8 final URLs; Google landde waarschijnlijk op `/` (67% bounce).
- **Actie:** (a) GA4 Admin → Product Links → Google Ads + auto-tagging; (b) Ads UI campagne `23834672782`: RSA final URL → `https://www.vlwarmte.nl/contact.html?modus=offerte#aanvraag`; prijs-keywords optioneel aparte ad/ad group → `prijsindicatie.html`. Defaults-JSON al aangepast.
- **Verwacht effect:** Paid Search conv. 0% → 5–15% (= 1–2 leads/30d bij huidig volume).

### 2. `vloerverwarming-assen.html` — layout-fix cyclus 14
- **Prioriteit:** Hoog
- **Type:** Content / Developer
- **Onderbouwing:** 90d **7 sess / 0,7 s / 0 scrollers / 86% bounce**. Diagnose cyclus 13: readnext-link + CTA-band tussen hero en content verwijderen (Groningen-template).
- **Actie:** Developer: ~10 regels HTML; optioneel hero-image lichter. Geen andere stad-pagina's.
- **Verwacht effect:** Bounce <70%, gem. duur >5 s binnen 4–6 weken.

### 3. GSC OAuth inrichten — blocker SEO-evaluatie
- **Prioriteit:** Hoog
- **Type:** Analytics / SEO
- **Onderbouwing:** Sprint-13 meetdoelen (prijsindicatie CTR, Hoogeveen-rang, Drenthe-hub) vereisen GSC. `secrets/gsc.env` ontbreekt.
- **Actie:** `cp secrets/gsc.env.example secrets/gsc.env`; `scripts/gsc_get_refresh_token.py`; `scripts/gsc_fetch.py` vóór juni-fetch ~22 juni.
- **Verwacht effect:** Harde SEO-check op cyclus-13-wijzigingen.

### 4. Facebook message-match — social kalender
- **Prioriteit:** Midden
- **Type:** Social / CTA
- **Onderbouwing:** **20 Facebook-sess / 0 conv.**; fbclid-landings op `/` en contact 100% bounce.
- **Actie:** Eén intentie + één link per post (`?modus=offerte#aanvraag`, `?modus=bel#aanvraag` of prijsindicatie). Geen developer-werk.
- **Verwacht effect:** 1–2 leads per 30 social-sess (2–5% conv-rate).

### 5. Heerenveen — pagina of keyword pauzeren
- **Prioriteit:** Midden
- **Type:** SEO / Google Ads
- **Onderbouwing:** Keyword `vloerverwarming heerenveen` in defaults; geen dedicated pagina. Friesland 8 sess (was 6). Vorig GSC: Drachten rankt op term, rang ~50.
- **Actie:** Na GSC-fetch: rang <20 op Drachten? Zo niet: pauzeer keyword in Ads **of** plan `vloerverwarming-heerenveen.html` cyclus 15 (max. 1 city/sprint na Assen).
- **Verwacht effect:** Geen budgetlek naar pagina-loze keyword.

### 6. Drenthe-hub + prijsindicatie-title — juni-fetch afwachten
- **Prioriteit:** Midden
- **Type:** SEO / monitor
- **Onderbouwing:** Deploy 26-05 (~6 dagen in venster). Eén sessie met nieuwe prijsindicatie-title zichtbaar.
- **Actie:** Geen wijziging. Juni-fetch: GSC rang _vloerverwarming drenthe_ op `/`; prijsindicatie CTR >0,5%?
- **Verwacht effect:** Data-gedreven beslissing hub vs standalone pagina.

### 7. `projecten.html` — monitor, geen hero-tweak nu
- **Prioriteit:** Laag (uitgesteld)
- **Type:** Content
- **Onderbouwing:** 90d 18 sess / 14 s gem. / 2 scrollers. Werkwijze-link net live; entry-sample 2 sess.
- **Actie:** Juni-fetch: entry-bounce >90% bij ≥10 entry-sess → hero compacter. Blijft sitelink, niet RSA-final-URL.
- **Verwacht effect:** Voorkomt voortijdige roer-omgooi.

### 8. Conversie-definitie audit — dubbeltelling
- **Prioriteit:** Laag
- **Type:** Analytics
- **Onderbouwing:** `/contact.html` landing 3 sess / 9 conv. — meerdere events per sess mogelijk.
- **Actie:** GA4 Admin: alleen `contact_submit` + `wizard_lead_submit` als key events (conform AGENTS.md).
- **Verwacht effect:** Schonere vergelijking kanalen; betere Ads-bieding.

---

## Iteratie na 2–4 weken (juni-fetch ~22 juni)

1. **GA4 ↔ Ads gekoppeld?** → herinterpreteer Direct (55% conv.) vs Paid/Cross-network.
2. **GSC beschikbaar?** → prijsindicatie CTR, Hoogeveen-rang, Drenthe-hub op `/`.
3. **Paid Search:** nog 0 conv. na RSA-fix? → search terms report + negatives.
4. **`vloerverwarming-assen.html`:** bounce <70% na layout-fix?
5. **Facebook:** conv. >0 na message-match kalender?
6. **RSA-variant + sitelinks `--apply`:** pas na PO-akkoord en schone attributie.

## Hashtags (social — referentie)

Facebook 0–3 of geen; Instagram 5–10; LinkedIn 3–5. Standaard: `#vloerverwarming`, `#Drenthe` / `#Groningen`, `#renovatie` / `#nieuwbouw` — max. 1–2 regio-tags per post. Zie playbook `marketing-research-agent.md`.
