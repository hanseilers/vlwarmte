# Marketing Research Rapport — 8 juni 2026

**Cyclus 16** — vervolg op cyclus 15 (07-06). Belangrijkste verschuiving deze cyclus: er is **wél GSC-data beschikbaar** (`docs/website-manager/gsc_report.json`, fetch 23-05-2026, venster 25 apr – 22 mei). In cyclus 15 was GSC nog geblokkeerd; nu kunnen we organische queries, posities en CTR-gaps voor het eerst hard onderbouwen.
**Scope:** leadgeneratie (organisch + betaald), landingskwaliteit, content-gaps, Google Ads message-match, prijscalculator-status.
**Bronnen:** `docs/website-manager/analytics_report.md` (07-06), `docs/website-manager/gsc_report.json` (23-05), root-HTML sitemap, `scripts/data/google_ads_lead_campaign_defaults.json`, `scripts/data/google_ads_campaign_negatives.json`, `.cursor/skills/google-ads-marketing/SKILL.md`.

> **Sessie-beperkingen (transparant):** in deze sessie waren **Bash en WebSearch geblokkeerd** (don't-ask-mode). Daardoor kon ik **zelf geen Ads-scripts draaien** (`google_ads_smoke_test.py`, `google_ads_list_campaigns.py`, `create_search_campaign.py --dry-run`) en **geen verse WebSearch** uitvoeren. Alle Ads-acties hieronder zijn daarom **verificatie- en mutatie-voorstellen** op basis van de bestaande repo-data, niet zelf-uitgevoerde runs. Zie *Escalatie* onderaan. Geen secrets gelezen of getoond.

## Samenvatting

Verkeer blijft stabiel-laag (**201 sess/30d**, laatste twee weken ~16 sess/week). De grootste **nieuwe** kans zit in de GSC-data: VLWarmte heeft **veel organische impressies maar bijna geen clicks** — er staat vraag op het scherm die niet wordt verzilverd. Twee patronen springen eruit:

1. **`vloerverwarming drenthe`: 82 impressies, positie 65,7, 0 clicks.** Hoge regiovraag, maar de pagina staat op pagina 6–7. De Drenthe-hub op `/` (live sinds 26-05) is ná deze GSC-fetch live gegaan — meet effect bij volgende fetch, maar de positie is nu nog ver van pagina 1.
2. **Pagina-1-posities zonder clicks:** `vloerverwarming zuidlaren` (pos 9,3 / 33 impr / 0 clicks), `installatiebedrijf zuidlaren` (pos 6,5 / 20 impr), `vloerverwarming hoogeveen` (pos 10,6), `vloerverwarming fluitenberg` (pos 4,8). Op deze termen staat VLWarmte zichtbaar maar wordt **niet aangeklikt** — een **title/meta-CTR-probleem**, niet een rankingprobleem. Dit is de goedkoopste leadwinst: titles aanscherpen, geen nieuwe content nodig.

Het betaalde kernprobleem is ongewijzigd: **Paid Search 11 sess / 0 conv.** terwijl de offerte-deeplink **10 conv. op 11 entry-sess** haalt. De GA4↔Ads-koppeling + live RSA-sync (P0 uit cyclus 14/15) blijft de eerste hefboom.

## GA4-kern (30d, fetch 07-06-2026 — ongewijzigd t.o.v. analytics_report)

| Metric | 07-06 |
| ------ | ----- |
| Sessies (devices) | **201** (113 desktop + 70 mobile + 18 tablet) |
| Homepage `/` | 145 sess, bounce 64,8%, gem. 50 s |
| `/prijsindicatie.html` | 33 sess, ~35% bounce, 73 s |
| Paid Search `google/cpc` | **11 / 0 conv.** |
| Cross-network `google/cpc` | 85 / 22 conv. |
| Organic `google` | 9 / 0 conv. |
| Geo Drenthe / Groningen / Friesland | 57 / 23 / 10 (~45% van verkeer) |

**Goudstandaard landing:** `/contact.html?modus=offerte` — 11 sess, 9,1% bounce, **10 conv.**

## NIEUW — GSC-analyse (fetch 23-05, venster 25 apr – 22 mei)

Site-breed beeld: **veel impressies, vrijwel geen clicks** (totaal ~6 clicks in de top-pagina's). Dit is het meest waardevolle nieuwe signaal van deze cyclus.

### A. Hoge vraag, slechte positie (content/SEO-werk nodig)

| Query | Impressies | Positie | Clicks | Diagnose |
| ----- | ---------- | ------- | ------ | -------- |
| `vloerverwarming drenthe` | **82** | 65,7 | 0 | Grootste regiovraag; staat pagina 6–7. Drenthe-hub (live 26-05) ná deze fetch — meet bij volgende fetch. |
| `vloerverwarming zuidlaren` | **33** | 9,3 | 0 | Page 1 maar 0 clicks → **CTR-probleem** (zie B) |
| `vloerverwarming friesland` | 10 | 87,7 | 0 | Diep; Leeuwarden-pagina rankt zwak |
| `vloerverwarming schoonebeek` | 10 | 61,5 | 0 | Emmen-omgeving; geen sterke landing |

`vloerverwarming drenthe` verdeelt zich over `/` (57 impr, pos 63,4), `prijsindicatie.html` (49 impr, pos 71,1) en `diensten.html` (13 impr) — **Google kiest geen duidelijke pagina**. De Drenthe-hub op `/` moet dit consolideren; volgende fetch is de toets.

### B. Page-1 zonder clicks — CTR/title-kans (goedkoopste winst)

| Query | Impressies | Positie | Clicks | Pagina | Actie |
| ----- | ---------- | ------- | ------ | ------ | ----- |
| `vloerverwarming zuidlaren` | 33 | **9,3** | 0 | `/` (pos 6,6) + diensten (16,6) + prijsindicatie (19,4) | Title/meta `/` met "Zuid-Laren" + USP |
| `installatiebedrijf zuidlaren` | 20 | **6,5** | 0 | `/` | Title/meta toevoegen lokale term |
| `vloerverwarming hoogeveen` | 8 | **10,6** | 0 | `vloerverwarming-hoogeveen.html` | Title/meta CTR-aanscherping |
| `vloerverwarming fluitenberg` | 6 | **4,8** | 0 | `vloerverwarming-hoogeveen.html` | Idem (Hoogeveen-omgeving) |
| `installateur zuidlaren` | 9 | 3,7 | 0 | `/` | Brede installateur-intentie, page-1 |
| `warmtepomp zuidlaren` | 4 | 1,8 | **1** | `/` | **Enige click in dataset** — CTR 25% op pos 1,8 bevestigt: page-1 + relevante title = click |

**Conclusie B:** VLWarmte rankt op pagina 1 voor meerdere Zuid-Laren/Hoogeveen-termen maar oogst geen clicks. De enige query met een click (`warmtepomp zuidlaren`, pos 1,8) bewijst dat de titles wél werken als de positie hoog genoeg is. De rest staat op pos 4–10 met titles die kennelijk niet uitnodigen. **Title/meta-description-optimalisatie** op `/` en `vloerverwarming-hoogeveen.html` is de laagst hangende SEO-leadwinst deze cyclus — geen nieuwe pagina's, alleen `<title>`/`<meta description>`.

### C. Heerenveen-keyword — nu onderbouwd

`vloerverwarming heerenveen`: **5 impressies, positie 50,4, 0 clicks**, en Google koppelt het al aan `vloerverwarming-drachten.html`. Dat bevestigt de cyclus-15-conclusie: de Drachten-pagina **dekt** Heerenveen (message-match OK), maar staat te diep (pos 50) om clicks te oogsten. Geen dedicated pagina rechtvaardigen op 5 impressies — laat het Ads-keyword op de Drachten-URL landen en verbeter de Drachten-pagina-relevantie i.p.v. een nieuwe stad-pagina te bouwen.

### D. prijsindicatie.html organisch onzichtbaar

`prijsindicatie.html`: **75 impressies, positie 52, 0 clicks** organisch. De pagina converteert prima op betaald/direct verkeer maar is organisch onvindbaar op prijs-/kosten-queries. Opvallend: in de GSC-querylijst staan **geen** `vloerverwarming kosten`/`per m2`-termen waarop VLWarmte vertoont — die SERP wordt gedomineerd door aggregators (Solvari, Bobex) en kostengidsen. Organisch concurreren op brede kosten-termen is duur; **prijs-keywords horen in de Ads-funnel** (al in defaults), niet als organisch SEO-doel deze cyclus.

## Top zoekwoorden (GSC-onderbouwd + defaults)

| Zoekwoord | Volume (GSC-impr indicatie) | Positie nu | Concurrentie | Pagina / actie |
| --------- | --------------------------- | ---------- | ------------ | -------------- |
| vloerverwarming drenthe | hoog (82 impr) | 65,7 | hoog (aggregators) | `/` Drenthe-hub — meet effect |
| vloerverwarming zuidlaren | midden (33 impr) | **9,3** | midden | `/` — title/CTR-fix |
| installatiebedrijf/installateur zuidlaren | midden (29 impr) | 3,7–6,5 | midden | `/` — title/CTR-fix |
| vloerverwarming hoogeveen (+ fluitenberg) | midden (14 impr) | 4,8–10,6 | midden | `vloerverwarming-hoogeveen.html` — title/CTR |
| vloerverwarming kosten / per m² | hoog (geen vertoning) | n.v.t. | hoog (aggregators) | Ads-funnel → `prijsindicatie.html` |
| vloerverwarming friesland/leeuwarden | laag-midden (17 impr) | 27–88 | midden | `vloerverwarming-leeuwarden.html` — diep |
| vloerverwarming heerenveen | laag (5 impr) | 50,4 | midden | `vloerverwarming-drachten.html` (Ads-keyword) |
| schuimbeton friesland/drenthe | laag (2 impr) | 70 | midden | `diensten.html#schuimbeton` |

**Seizoen (indicatief, geen verse WebSearch deze sessie):** renovatie-/verwarmingsintentie piekt richting **najaar (sep–dec)**; nieuwbouw vraagt planning in ruwbouwfase. Copy-kans "plan nu voor het stookseizoen" op `werkwijze.html`/contact-CTA's — past bij nuchtere toon. (Cyclus 15-aanname; verifieer met WebSearch zodra beschikbaar.)

## Prijscalculator — haalbaarheidsonderzoek

### Conclusie
**Niet opnieuw bouwen** (ongewijzigd t.o.v. cyclus 15). VLWarmte heeft al een werkende prijsindicatie-wizard op `prijsindicatie.html` die goed presteert op pagina-niveau (33 sess / 73 s / ~35% bounce) en conversies levert. De GSC-data voegt één nuance toe: de wizard-pagina is **organisch onvindbaar** (75 impr / pos 52 / 0 clicks), dus de calculator levert leads via **betaald + direct**, niet via SEO. Focus blijft landing-optimalisatie + attributie, niet een tweede calculator.

### Onderbouwing
- Concurrenten met rekentools (Bull Schuimbeton, RM Vloeren) richten zich op materiaal-m²/m³; VLWarmte's wizard dekt het **complete traject** — dieper en gekoppeld aan installatie.
- B2B/installatie websitebezoeker→lead is gemiddeld 1–3%; de offerte-deeplink haalt ~91% conv-rate op entry (10/11) door hoge intentie + goede match.
- ATF-fix (sprint 14) verlaagde entry-bounce 58,3% → 54,5%; doel <45% nog niet gehaald.

### Voorgestelde opbouw wizard
Geen structurele wijziging. Bestaande flow blijft: productkeuze → oppervlakte → ondergrond → schuimbeton-band → lead-form → `wizard_lead_submit`. Enige onderhoud: mobile ATF (stap 0 zichtbaar zonder scroll).

### Leadgeneratie koppeling
Wizard eindigt in lead-form (`wizard_lead_submit`). Prijs-keywords blijven in de Ads-funnel met `prijsindicatie.html` als secundaire RSA-URL. Disclaimer "vrijblijvende indicatie, geen offerte" blijft zichtbaar.

### Risico's en aandachtspunten
Band zonder contactgegevens trekt soms tire-kickers; lead-form is het filter. Geen bindende prijsbelofte in Ads-copy. Import `wizard_lead_submit` naar Ads pas na GA4↔Ads-koppeling.

### Aanbeveling aan Product Manager
- **Prioriteit:** Laag (onderhoud)
- **Geschatte ontwikkeltijd:** 0 uur nieuwe build; 2–4 uur mobile ATF-tweak
- **Verwacht effect:** bestaande wizard blijft kernconverter; entry-bounce <45% verhoogt funnel-kwaliteit op prijs-keywords

## Content gaps

**Sitemap (root HTML, lead-relevant):** `index.html` (+ Drenthe-hub), `diensten.html`, `werkwijze.html`, `systemen-producten.html#laagopbouw`, `prijsindicatie.html`, `contact.html` (+ modi), stad-pagina's (`assen`, `groningen`, `leeuwarden`, `emmen`, `hoogeveen`, `drachten`, `zuidlaren`), `projecten.html`, `faq.html`, `over-ons.html`.

| Gap | GSC-signaal | Voorstel |
| --- | ----------- | -------- |
| **Title/meta-CTR op `/` en Hoogeveen** | Page-1 posities (zuidlaren 9,3; installatiebedrijf 6,5; hoogeveen 10,6; fluitenberg 4,8) met **0 clicks** | Title/meta aanscherpen met lokale term + USP (P1 — goedkoopste winst) |
| **`vloerverwarming drenthe` consolidatie** | 82 impr verdeeld over `/`, prijsindicatie, diensten; pos 65,7 | Drenthe-hub `/` moet dé pagina worden; meet bij volgende fetch |
| **`vloerverwarming-assen.html` data** | GA4 90d 7 sess / 0,7 s / 0 scrollers; GSC pos 77 op `/` | Afwachten juni-fetch; eventueel hero-image/LCP |
| **Heerenveen** | 5 impr, pos 50,4 op Drachten-URL | Geen nieuwe pagina; Ads-keyword op Drachten-URL houden |
| **Prijsindicatie organisch** | 75 impr / pos 52 / 0 clicks | Geen organisch SEO-doel; blijft Ads-/direct-converter |
| **Renovatie houten vloer / laagopbouw** | Concurrenten hebben productpagina's | Sectie `systemen-producten.html#laagopbouw` versterken (P2) |

**Afgewezen (blijft gelden):** standalone `vloerverwarming-drenthe.html`, standalone `vloerverwarming-heerenveen.html` (op 5 impr niet te rechtvaardigen), budgetverhoging >€2/dag, hero-CTA homepage wijzigen.

## Concurrentie observaties

(Geen verse WebSearch deze sessie — onderstaande uit cyclus-15-onderzoek, nog geldig.)

- **Lokale spelers:** ReWo & de Jong (Siddeburen, infrezen, geen-voorrijkosten), Kentech (Groningen-Assen, blog/FAQ), Lemmers (dedicated Heerenveen-pagina, 5.0 reviews), Installatieservice van der Veen (Heerenveen).
- **Aggregators:** Solvari, Slimster, Bobex domineren brede kosten-SERP's met "vergelijk 4 offertes" — bevestigd door GSC: VLWarmte vertoont **niet** op brede kosten-termen.
- **Waar VLWarmte wint:** echt projectwerk, compleet traject (ondervloer → schuimbeton → dekvloer), online richtbedrag-wizard, offerte-deeplink met kruipruimte-maat.
- **Waar VLWarmte achterloopt:** dedicated stad-pagina's per concurrent; aggregator-dominantie op kosten-termen; **CTR op eigen page-1-posities** (nieuw inzicht uit GSC).

## Google Ads — status en acties

**Verificatie deze sessie:** **niet uitgevoerd** — Bash geblokkeerd. Onderstaande is de bekende staat uit cyclus 15 (07-06) plus voorstellen.

**Bekende staat (cyclus 15):** campagne `id=23834672782` | SEARCH | ENABLED | VLW-API-Leads NL auto | €2/dag. Defaults-JSON: 2 `final_urls` (offerte-deeplink + prijsindicatie), 32 phrase-keywords, geo Drenthe/Groningen/Friesland, `extra_rsa` klaar maar niet `--apply`, negatieven-JSON klaar (15 termen).

| Onderwerp | Status | Voorgestelde actie (agent draait scripts zodra Bash beschikbaar) |
| --------- | ------ | ----- |
| GA4 ↔ Ads + auto-tagging | **P0 open** | Admin-koppeling; `gclid`-test op offerte-deeplink. Blijft de #1 hefboom: Paid Search 11/0 vs Cross-network 85/22. |
| Live RSA final URLs | **P0 — handmatig** | Ads UI campagne `23834672782`: RSA final URLs = offerte-deeplink + prijsindicatie (match defaults) |
| Negatieven | JSON klaar | `python scripts/google_ads_campaign_next_steps.py negatives --campaign-id 23834672782 --dry-run` → `--apply` (geen spend-effect) |
| `extra_rsa` 2e RSA | JSON klaar | `python scripts/google_ads_add_rsa_variant.py --campaign-id 23834672782 --dry-run` → `--apply` na attributiefix |
| Budget | €2/dag | **Geen verhoging** zolang Paid Search 0 conv. (PM cyclus 14). Spend-advies: pas na ≥1 conv. + schone attributie heroverwegen. |

**Geen spend-mutaties voorgesteld voor uitvoering zonder akkoord.** Geen `--go-live`, geen `--apply` deze sessie (Bash geblokkeerd én geen spend-goedkeuring).

## Aanbevelingen voor Product Manager

### 1. GA4 ↔ Google Ads koppeling + live RSA sync — deze week
- **Prioriteit:** Hoog (P0)
- **Type:** Google Ads / Analytics (Admin/PO)
- **Onderbouwing:** Paid Search **11 sess / 0 conv.** vs Cross-network 85/22; geen `gclid` in entry-rapport; Direct 55% conv-rate wijst op attributielek. Offerte-deeplink: 10 conv. / 11 entry-sess.
- **Actie:** (a) GA4 Admin → Product Links → Google Ads + auto-tagging aan; (b) Ads UI campagne `23834672782`: RSA final URLs → offerte-deeplink + prijsindicatie. Geen developer-werk.
- **Verwacht effect:** Eerlijke Paid Search-rapportage; basis voor ≥1 conv. in juni-fetch.

### 2. Title/meta-CTR-fix op `/` en `vloerverwarming-hoogeveen.html` — NIEUW, goedkoopste leadwinst
- **Prioriteit:** Hoog
- **Type:** SEO / Developer (kleine HTML-wijziging)
- **Onderbouwing (GSC):** Page-1 posities met **0 clicks**: `vloerverwarming zuidlaren` (pos 9,3 / 33 impr), `installatiebedrijf zuidlaren` (pos 6,5 / 20 impr), `vloerverwarming hoogeveen` (pos 10,6), `vloerverwarming fluitenberg` (pos 4,8). De enige click in de hele dataset (`warmtepomp zuidlaren`, pos 1,8, CTR 25%) bewijst dat titles werken bij hoge positie. We oogsten zichtbaarheid niet.
- **Actie:** Developer — herschrijf `<title>` + `<meta description>` van `index.html` (lokale term "Zuid-Laren / installateur" + concrete USP: regio, traject, reactie binnen 1 werkdag) en `vloerverwarming-hoogeveen.html`. Geen layout-/content-wijziging.
- **Verwacht effect:** ≥1–2 organische clicks op deze termen in volgende GSC-fetch; meetbaar via CTR-stijging van 0%.

### 3. Prijsindicatie mobile ATF — wizard stap 0 zichtbaar
- **Prioriteit:** Hoog
- **Type:** Developer / CRO
- **Onderbouwing:** Entry-bounce 54,5% (11 sess) — verbeterd na ATF-fix maar doel <45% niet gehaald. Pageview-bounce ~35%.
- **Actie:** Developer — op mobile (375×667) wizard-stap 0 zichtbaar zonder scroll (compactere hero of wizard omhoog). Geen extra CTA's.
- **Verwacht effect:** Entry-bounce <45% bij ≥10 entry-sess in juni-fetch.

### 4. Drenthe-hub effect meten + interne links versterken
- **Prioriteit:** Midden
- **Type:** SEO / monitoring
- **Onderbouwing (GSC):** `vloerverwarming drenthe` 82 impr / pos 65,7 / 0 clicks, verdeeld over `/`, prijsindicatie en diensten — Google kiest geen pagina. Drenthe-hub op `/` ging ná deze GSC-fetch (26-05) live.
- **Actie:** Meet bij volgende fetch of `/` consolideert en stijgt. Versterk interne links vanaf stad-pagina's naar de Drenthe-hub om signaal te bundelen. Geen nieuwe standalone Drenthe-pagina (afgewezen).
- **Verwacht effect:** `/` wordt dé Drenthe-pagina; positie stijgt richting top-30, daarna CTR-werk.

### 5. Paid Search negatives toepassen (na attributiefix)
- **Prioriteit:** Midden
- **Type:** Google Ads
- **Onderbouwing:** 15 negatieven staan klaar (gratis, vacature, diy, goedkoopste, tweedehands, marktplaats, enz.). Voorkomt budgetlek zodra attributie klopt.
- **Actie:** `python scripts/google_ads_campaign_next_steps.py negatives --campaign-id 23834672782 --dry-run` → `--apply`. Geen spend-wijziging.
- **Verwacht effect:** Schonere search terms; minder klikken zonder koopintentie.

### 6. Betaald verkeer niet op homepage laten landen
- **Prioriteit:** Midden
- **Type:** Google Ads / landing
- **Onderbouwing:** `/` als landing: 136 sess, 66,2% bounce — grootste instapper met meeste verlies. Defaults beperken final URLs al tot offerte + prijsindicatie; live RSA in Ads UI moet syncen (zie #1).
- **Actie:** Bevestig in Ads UI dat geen RSA op `/` of `projecten.html` landt. Overweeg aparte ad group voor prijs-keywords → `prijsindicatie.html` na attributiefix. Geen homepage hero-CTA-wijziging.
- **Verwacht effect:** Minder verspilde klikken; hogere conv-rate op betaald.

### 7. Facebook message-match — één intentie per post
- **Prioriteit:** Midden
- **Type:** Social / CTA
- **Onderbouwing:** 20 Facebook-sess / 0 conv.; `fbclid` op contact `modus=informatie` bounce't 100%.
- **Actie:** Eén intentie + één link per post (`?modus=offerte#aanvraag`, `?modus=bel#aanvraag` of `prijsindicatie.html`). Geen developer-werk.
- **Verwacht effect:** Social conv. >0 of lagere bounce op social-entries.

### 8. Assen follow-up meten — eventueel LCP/hero-image
- **Prioriteit:** Midden (monitoring)
- **Type:** Developer (pas na juni-fetch)
- **Onderbouwing:** GA4 90d 0,7 s / 0 scrollers op 7 sess; GSC pos 77. Layout-fix recent live.
- **Actie:** Wacht tot fetch ~22 juni. Als bounce >70% en duur <5 s blijft: hero-image optimaliseren uit `beeldmateriaal/` of LCP-check.
- **Verwacht effect:** Bounce <70%, gem. duur >5 s, ≥1 scroller in 90d.

---

## Escalatie (acties die deze sessie niet konden draaien)

1. **Bash geblokkeerd** → Ads-verificatie (`google_ads_smoke_test.py`, `google_ads_list_campaigns.py`) en dry-runs (`create_search_campaign.py`, `add_rsa_variant.py`, `campaign_next_steps.py negatives`) niet uitgevoerd. Voorstellen staan klaar; draaien zodra een sessie met Bash-rechten beschikbaar is. **Geen spend-goedkeuring gevraagd of nodig** — alle voorstellen blijven `--dry-run` / paused tot expliciet akkoord.
2. **WebSearch geblokkeerd** → geen verse concurrentie-/seizoen-/zoekvolume-update juni 2026. Concurrentie- en seizoenssecties leunen op cyclus-15-onderzoek (nog geldig).
3. **GSC-data is van 23-05** (28-daags venster t/m 22-05) → vóór de Drenthe-hub-deploy (26-05). Effect van de hub is dus **nog niet** in deze GSC-data zichtbaar; volgende GSC-fetch is de toets. Verse GSC-fetch aanbevolen rond ~22 juni.

## Iteratie na 2–4 weken (juni-fetch ~22 juni)

1. **GA4 ↔ Ads gekoppeld + RSA gesync?** → Paid Search conv. >0? Direct-leak gedaald?
2. **Verse GSC-fetch** → CTR op `/` en Hoogeveen na title-fix (#2); `vloerverwarming drenthe`-positie na hub-consolidatie (#4).
3. **Prijsindicatie entry-bounce <45%?** → mobile ATF-effect (#3).
4. **`vloerverwarming-assen.html`** bounce/duur/scrollers na layout-fix.
5. **Search terms report** → negatives bijstellen; `extra_rsa --apply` pas na schone attributie + PO-akkoord.
6. **Facebook** conv. >0 na message-match kalender.

## Hashtags (social — referentie)

Facebook 0–3 of geen; Instagram 5–10; LinkedIn 3–5. Standaard: `#vloerverwarming`, `#Drenthe` / `#Groningen`, `#renovatie` / `#nieuwbouw` — max. 1–2 regio-tags per post. Zie playbook `marketing-research-agent.md`.
