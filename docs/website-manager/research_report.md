# Marketing Research Rapport — 7 juni 2026

**Cyclus 15** — eerste research na sprint-14-deploy (1 juni, commit `0099874`: Assen layout-fix, prijsindicatie ATF message-match, OG/Twitter meta, Drenthe-hub Assen-ankertekst, Ads-defaults JSON).
**Scope:** leadgeneratie (organisch + betaald), landingskwaliteit, content-gaps, Google Ads message-match, prijscalculator-status.
**Bronnen:** `docs/website-manager/analytics_report.md` (07-06), `docs/website-manager/archive/sprint-2026-06-07.md`, root-HTML sitemap, `scripts/data/google_ads_lead_campaign_defaults.json`, `.cursor/skills/google-ads-marketing/SKILL.md`, WebSearch (juni 2026), lokale Ads-scripts.

> **Ads-uitvoering deze sessie:** `google_ads_smoke_test.py` OK (3 toegankelijke accounts). `google_ads_list_campaigns.py`: campagne `23834672782` SEARCH **ENABLED**, €2/dag. Defaults-JSON ongewijzigd t.o.v. sprint 14 (2 `final_urls`). **Geen `--apply`, geen `--go-live`, geen budgetwijziging.**
>
> **GSC:** `secrets/gsc.env` aanwezig; `gsc_fetch.py` faalt met `invalid_grant: Token has been expired or revoked` — refresh token opnieuw genereren via `scripts/gsc_get_refresh_token.py` (PO/browser).

## Samenvatting

Verkeer blijft stabiel-laag (**201 sess/30d**, laatste twee weken elk ~16 sess/week). Het kernprobleem is ongewijzigd: **Paid Search 11 sess / 0 conv.** terwijl `contact.html?modus=offerte` **10 conv. op 11 entry-sess** haalt. Sprint-14-wijzigingen (RSA-defaults, prijsindicatie ATF) zijn **6 dagen live** — prijsindicatie entry-bounce daalde licht (58,3% → **54,5%**), maar Paid Search meetdoel (≥1 conv.) is **niet gehaald**.

Drie leadkansen voor juni–juli:

1. **Attributie + live RSA sync** — GA4↔Ads koppeling, auto-tagging en handmatige RSA final URL op offerte-deeplink (P0, nog open).
2. **Prijsindicatie mobile ATF** — wizard stap 0 zichtbaar zonder scroll; entry-bounce richting <45%.
3. **GSC refresh token vernieuwen** — blocker voor organische query-data (Heerenveen, prijsindicatie CTR, Drenthe-hub).

## GA4-kern (30d, fetch 07-06-2026)

| Metric | 07-06 | Trend t.o.v. 01-06 |
| ------ | ----- | ------------------ |
| Sessies (devices) | **201** (113 desktop + 70 mobile + 18 tablet) | ↓ −2% |
| Homepage `/` | 145 sess, bounce **64,8%**, gem. **50 s** | bounce ↓; duur ↑ (35 s → 50 s) |
| `/prijsindicatie.html` | 33 sess, **~35%** pageview-bounce, **73 s** | engagement stabiel |
| Betaald `google / cpc` | Cross-network **85 / 22**; Paid Search **11 / 0** | Cross +2 conv.; Paid nog nul |
| Organic `google` | 9 sess, 0 conv. | mager |
| Facebook (3 bronnen) | 20 sess, 0 conv. | stabiel |
| Geo NL — Drenthe / Groningen / Friesland | 57 / 23 / 10 | doelregio ~45% van verkeer |

**Top entry-landings (selectie):**

| Landing | Sessies | Bounce | Conv. | Opmerking |
| ------- | ------- | ------ | ----- | --------- |
| `/contact.html?modus=offerte` | 11 | **9,1%** | **10** | goudstandaard campagne-landing |
| `/prijsindicatie.html` | 11 | **54,5%** | 8 | ATF-fix werkt deels; doel <45% niet gehaald |
| `/` | 136 | **66,2%** | 32 | veel conv. via retour/direct; slechte koude Search-landing |
| `/werkwijze.html` | 2 | 0% | **4** | sterk signaal; volume laag |

Geen `gclid` zichtbaar in landingPagePlusQueryString — attributielek naar Direct (55% conv-rate op 74 sess) blijft waarschijnlijk.

## Top zoekwoorden (indicatief — WebSearch + defaults + vorig GSC)

| Zoekwoord | Volume (indic.) | Concurrentie | Pagina |
| --------- | --------------- | ------------ | ------ |
| vloerverwarming kosten / per m² | hoog | hoog (aggregators) | `prijsindicatie.html` |
| vloerverwarming drenthe | hoog | hoog (Bobex, Solvari) | `/` Drenthe-hub (live 26-05) |
| vloerverwarming groningen installateur | midden-hoog | midden-hoog | `vloerverwarming-groningen.html` |
| schuimbeton vloerverwarming | midden | midden-hoog | `diensten.html#schuimbeton` |
| droge vloerverwarming / laagopbouw | midden (groeiend) | midden | `systemen-producten.html#laagopbouw` |
| vloerverwarming hoogeveen | midden | midden | `vloerverwarming-hoogeveen.html` |
| vloerverwarming heerenveen | laag-midden | midden (lokale installateurs) | **gap** — keyword in Ads; content op `vloerverwarming-drachten.html` |
| vloerverwarming assen | midden (lokaal) | midden | `vloerverwarming-assen.html` (UX fix live, data nog rood) |
| vloerverwarming offerte [provincie] | midden | midden | `contact.html?modus=offerte#aanvraag` |
| vloerverwarming warmtepomp combinatie | midden | midden | FAQ + diensten; geen dedicated pagina |

**Seizoenspatroon (WebSearch, indicatief):** zoek- en planningsintentie piekt richting **voorjaar (apr–mei)** en **najaar (okt–dec)** — renovatieplanning en verwarmingsseizoen. Nieuwbouw vraagt planning in ruwbouwfase (leidingen vóór dekvloer). Copy-kans: "plan nu voor najaar" op `werkwijze.html` en contact-CTA's — past bij nuchtere toon, geen superlatief.

## Prijscalculator — haalbaarheidsonderzoek

### Conclusie

**Niet opnieuw bouwen.** VLWarmte heeft al een interactieve prijsindicatie-wizard op `prijsindicatie.html` (productkeuze → oppervlakte → ondergrond → schuimbeton-band → lead-form). Die presteert goed als pagina (**33 sess / 73 s / ~35% bounce**) en levert conversies in het pad. Focus ligt op **landing-optimalisatie en attributie**, niet op een tweede calculator.

### Onderbouwing

- **Concurrentie:** Bull Schuimbeton, RM Vloeren en Schuimbetonplus hebben online rekentools — vooral voor schuimbeton m³/m², soms met vloerverwarming als optie. Lokale installateurs (ReWo, Kentech, Lemmers Heerenveen) gebruiken vooral **offerteformulieren**, geen diepere traject-calculator.
- **VLWarmte-voordeel:** wizard dekt **compleet traject** (alleen vloerverwarming vs. schuimbeton, kruipruimte-diepte, zandophoging) — dieper dan Bull's m²-calculator of aggregator-formulieren (Bobex, Solvari).
- **Conversie-benchmarks (WebSearch):** B2B/installatie — websitebezoeker → lead **1–3%** gemiddeld; gerichte landingspagina's met zachte conversie (calculator, checklist) kunnen **20–30%** halen op warm verkeer. VLWarmte's offerte-deeplink haalt **~91% conv-rate op entry** (10/11 sess) — uitzonderlijk hoog door hoge intentie + goede match.
- **GA4 na ATF-fix (sprint 14):** entry-bounce prijsindicatie daalde 58,3% → **54,5%** — richting goed, wizard houdt engagement (73 s gem.).

### Voorgestelde opbouw wizard

Geen structurele wijziging. Bestaande flow blijft:

1. Productkeuze (alleen vloerverwarming / met schuimbeton; hout → contact)
2. Oppervlakte woning (m²)
3. Ondergrond kruipruimte
4. Schuimbeton-band (excl. btw, zonder contactgegevens)
5. Lead-form → Formspree → `wizard_lead_submit`

**Optioneel onderhoud (geen nieuwe build):** mobile ATF — stap 0 zichtbaar zonder scroll (zie PM-aanbeveling #3).

### Leadgeneratie koppeling

- Wizard eindigt in lead-form op dezelfde pagina; GA4 key event: `wizard_lead_submit`.
- Prijs-keywords in Search-campagne (`vloerverwarming kosten`, `prijsindicatie vloerverwarming`, enz.) horen op `prijsindicatie.html` als secundaire RSA-URL (defaults JSON).
- Disclaimer "vrijblijvende indicatie, geen offerte" blijft zichtbaar — juridisch en commercieel juist.

### Risico's en aandachtspunten

- Band zonder contactgegevens trekt soms tire-kickers aan — lead-form na band is het filter.
- Schuimbeton-band moet "indicatie" blijven; geen bindende prijsbelofte in Ads-copy.
- Import `wizard_lead_submit` naar Ads pas na GA4↔Ads-koppeling.

### Aanbeveling aan Product Manager

- **Prioriteit:** Laag (onderhoud / optimalisatie)
- **Geschatte ontwikkeltijd:** 0 uur nieuwe build; 2–4 uur mobile ATF-tweak indien nodig
- **Verwacht effect:** bestaande wizard blijft kernconverter; entry-bounce <45% verhoogt Paid/organic kwaliteit op prijs-keywords

## Content gaps

**Root HTML-sitemap (lead-relevant):**

| Pagina | Rol |
| ------ | --- |
| `index.html` | Hub + Drenthe-hub |
| `diensten.html`, `werkwijze.html`, `systemen-producten.html#laagopbouw` | Dienst/uitleg |
| `prijsindicatie.html` | Prijs-wizard |
| `contact.html` (+ `?modus=offerte\|informatie\|bel#aanvraag`) | Lead-form |
| `vloerverwarming-{assen,groningen,leeuwarden,emmen,hoogeveen,drachten,zuidlaren}.html` | Stad-SEO |
| `projecten.html`, `faq.html`, `over-ons.html` | Trust |

**Recent afgevinkt (sprint 14, live 01-06):** Assen layout-fix, prijsindicatie ATF + OG/Twitter, Drenthe-hub Assen-ankertekst, RSA-defaults (2 final URLs).

**Open / actueel:**

| Gap | Signaal | Voorstel |
| --- | ------- | -------- |
| **`vloerverwarming heerenveen` Ads vs. pagina** | Keyword actief; geen `vloerverwarming-heerenveen.html`; Drachten-pagina dekt Heerenveen in title/H1 | Route keyword naar `vloerverwarming-drachten.html` in Ads **of** pauzeren tot GSC-data |
| **`vloerverwarming-assen.html` data** | 90d 7 sess / 0,7 s / 0 scrollers; layout-fix 6 dagen live | Afwachten juni-fetch ~22 juni; eventueel LCP/hero-image |
| **Prijsindicatie entry-bounce** | 54,5% (doel <45%) | Mobile ATF wizard zichtbaar |
| **`vloerverwarming-meppel`** | Geen pagina; keyword verwijderd uit defaults | Geen actie tot vraag uit GSC/Ads search terms |
| **Renovatie houten vloer** | Concurrenten (Bull, ThermoLamina) hebben productpagina's | Sectie op `systemen-producten.html#laagopbouw` versterken (P2) |
| **Organisch volume** | 9 organic sess / 0 conv. | GSC nodig voor query-prioritering |

**Afgewezen (PM cyclus 14, blijft gelden):** standalone `vloerverwarming-drenthe.html`, budgetverhoging >€2/dag, hero-CTA homepage wijzigen.

## Concurrentie observaties (WebSearch, juni 2026)

**Lokale spelers Noord-NL:**

- **ReWo & de Jong** (Siddeburen) — drie provincies, infrezen, geen voorrijkosten-claim, warmtepomp-narratief.
- **Kentech** (Groningen-Assen) — breed werkgebied, blog/FAQ, offerte-CTA.
- **Lemmers Vloerverwarming** — dedicated `vloerverwarming-heerenveen/` pagina, reviews (5.0), infrezen-focus.
- **Installatieservice van der Veen** (Heerenveen) — lokale stad-pagina, transparante offertes.

**Aggregators:** Solvari (231 installateurs Groningen), Slimster, Bobex — "vergelijk 4 offertes", domineren brede kosten-SERP's. VLWarmte onderscheidt zich met **eigen traject + wizard**, niet met "vergelijk offertes".

**Schuimbeton/prijs-tools:** Bull Schuimbeton (online calculator m² + diepte + vloerverwarming), RM Vloeren (rekentool), Systeemvloeren NL (blog €80–120/m² band). VLWarmte-wizard is vergelijkbaar diep maar gekoppeld aan **installatie-traject**, niet alleen materiaal.

**Laagopbouw/droogbouw:** Bull, ThermoLamina, Variokomp — product×uitleg; VLWarmte heeft `#laagopbouw` op `systemen-producten.html` maar minder SEO-volume dan dedicated concurrent-pagina's.

**Waar VLWarmte wint:** echt projectwerk, compleet traject (ondervloer → schuimbeton → dekvloer), online richtbedrag-wizard, offerte-deeplink met kruipruimte-maat.

**Waar VLWarmte achterloopt:** dedicated stad-pagina's per concurrent (Lemmers Heerenveen vs. VLWarmte via Drachten); aggregator-dominantie op brede kosten-termen; Assen-pagina UX/data vs. Groningen-template.

## Google Ads — status en acties

**Verificatie deze sessie (07-06):**

```
Smoke test: OK — 3 accessible customer accounts
Campagne: id=23834672782 | SEARCH | ENABLED | VLW-API-Leads NL auto | €2/dag
```

**Defaults-JSON (ongewijzigd sinds sprint 14):**

| Veld | Waarde |
| ---- | ------ |
| `final_urls` | `contact.html?modus=offerte#aanvraag` + `prijsindicatie.html` |
| `keywords` | 32 phrase-keywords incl. prijs-, stad-, laagopbouw-termen |
| `location_targeting` | Drenthe, Groningen, Friesland |
| `extra_rsa` | Klaar in JSON; nog niet `--apply` |
| `sitelinks` | Prijsindicatie, projecten, offerte, werkwijze, Drachten & Heerenveen |

| Onderwerp | Status | Actie |
| --------- | ------ | ----- |
| GA4 ↔ Ads + auto-tagging | **P0 open** | Admin-koppeling; `gclid`-test op offerte-deeplink |
| Live RSA final URLs | **P0 — handmatig** | Ads UI campagne `23834672782`: RSA syncen met repo-defaults (2 URL's) |
| Paid Search conv. | **11 sess / 0 conv.** | Sprint-14-meetdoel niet gehaald |
| Negatieven | JSON klaar (`google_ads_campaign_negatives.json`) | `google_ads_campaign_next_steps.py negatives --dry-run` → `--apply` na attributiefix |
| Heerenveen keyword | Actief, geen dedicated pagina | Land op Drachten-URL of pauzeren (zie #5) |
| Budget | €2/dag | Geen verhoging zonder Paid Search conv. >0 |

**Geen `--go-live`** — campagne draait al ENABLED. Geen `--apply` deze sessie.

## Aanbevelingen voor Product Manager

### 1. GA4 ↔ Google Ads koppeling + live RSA sync — deze week
- **Prioriteit:** Hoog (P0)
- **Type:** Google Ads / Analytics (Admin/PO)
- **Onderbouwing:** Paid Search **11 sess / 0 conv.**; geen `gclid` in entry-rapport; Direct **55% conv-rate** wijst op attributielek. Offerte-deeplink: **10 conv. / 11 entry-sess.**
- **Actie:** (a) GA4 Admin → Product Links → Google Ads + auto-tagging aan; (b) Ads UI campagne `23834672782`: RSA final URLs → enkel offerte-deeplink + prijsindicatie (match repo-defaults). Geen developer-werk.
- **Verwacht effect:** Eerlijke Paid Search-rapportage; basis voor ≥1 conv. in juni-fetch.

### 2. GSC refresh token vernieuwen
- **Prioriteit:** Hoog
- **Type:** Analytics / SEO (PO)
- **Onderbouwing:** `gsc_fetch.py` faalt met expired/revoked token. Organic **9 sess / 0 conv.**; sprint-13/14 SEO-meetdoelen (prijsindicatie CTR, Heerenveen-rang, Drenthe-hub) blijven blind.
- **Actie:** `scripts/gsc_get_refresh_token.py` met verified owner-account; daarna `scripts/gsc_fetch.py` vóór juni-fetch ~22 juni.
- **Verwacht effect:** Query-level data voor keyword- en contentbeslissingen.

### 3. Prijsindicatie mobile ATF — wizard stap 0 zichtbaar
- **Prioriteit:** Hoog
- **Type:** Developer / CRO
- **Onderbouwing:** Entry-bounce **54,5%** (11 sess) — verbeterd na ATF-fix, maar meetdoel **<45%** niet gehaald. Pageview-bounce ~35% — koude instappers haken af vóór wizard.
- **Actie:** Developer — op mobile (375×667) wizard-stap 0 zichtbaar zonder scroll (compactere hero of wizard omhoog); geen extra CTA's.
- **Verwacht effect:** Entry-bounce <45% bij ≥10 entry-sess in juni-fetch; betere Paid Search-kwaliteit op prijs-keywords.

### 4. Paid Search negatives toepassen (na attributiefix)
- **Prioriteit:** Midden
- **Type:** Google Ads
- **Onderbouwing:** Negatieven-JSON staat klaar (gratis, vacature, diy, goedkoopste, enz.). Voorkomt budgetlek op verkeerde intentie zodra attributie klopt.
- **Actie:** Agent/PO: `python scripts/google_ads_campaign_next_steps.py negatives --campaign-id 23834672782 --dry-run` → `--apply`. Geen spend-wijziging.
- **Verwacht effect:** Schonere search terms; minder klikken zonder koopintentie.

### 5. Heerenveen-keyword — land op Drachten of pauzeren
- **Prioriteit:** Midden
- **Type:** Google Ads / SEO
- **Onderbouwing:** Keyword `vloerverwarming heerenveen` actief; geen dedicated pagina. `vloerverwarming-drachten.html` dekt Heerenveen in title, H1 en body. Concurrent Lemmers heeft wel eigen Heerenveen-URL.
- **Actie:** Na GSC: rang op Drachten-URL voor Heerenveen-term? Zo ja: laat keyword staan (message-match OK). Zo nee: pauzeer keyword **of** plan dedicated pagina cyclus 16 (max. 1 city/sprint). Geen pagina-build deze sprint (Assen eerst meten).
- **Verwacht effect:** Geen budgetlek naar irrelevante landing; betere QS op Heerenveen-queries.

### 6. Facebook message-match — social kalender cyclus 15
- **Prioriteit:** Midden
- **Type:** Social / CTA
- **Onderbouwing:** **20 Facebook-sess / 0 conv.**; `fbclid` op contact `modus=informatie` bounce't **100%**.
- **Actie:** Eén intentie + één link per post (`?modus=offerte#aanvraag`, `?modus=bel#aanvraag` of `prijsindicatie.html`). Geen developer-werk.
- **Verwacht effect:** Social conv. >0 of lagere bounce op social-entries.

### 7. Assen follow-up meten — eventueel LCP/hero-image
- **Prioriteit:** Midden (monitoring)
- **Type:** Developer (pas na juni-fetch)
- **Onderbouwing:** Layout-fix live 6 dagen; 90d nog **0,7 s** gem. duur, **0 scrollers** op 7 sess. 30d slechts 1 sessie — te vroeg voor harde uitspraak.
- **Actie:** Wacht tot fetch ~22 juni. Als bounce >70% en duur <5 s blijft: hero-image optimaliseren uit `beeldmateriaal/` of LCP-check.
- **Verwacht effect:** Bounce <70%, gem. duur >5 s, ≥1 scroller in 90d.

### 8. Betaald verkeer niet op homepage laten landen
- **Prioriteit:** Midden
- **Type:** Google Ads / landing
- **Onderbouwing:** `/` als landing: **136 sess, 66,2% bounce** — grootste instapper met meeste verlies. RSA-defaults beperken final URLs al tot offerte + prijsindicatie; live RSA in Ads UI moet syncen.
- **Actie:** Bevestig in Ads UI dat geen RSA meer op `/` of `projecten.html` landt. Overweeg aparte ad group voor prijs-keywords → `prijsindicatie.html` na attributiefix. Geen homepage hero-CTA-wijziging (PM cyclus 14 afgewezen).
- **Verwacht effect:** Minder verspilde klikken; hogere conv-rate op betaald verkeer.

---

## Iteratie na 2–4 weken (juni-fetch ~22 juni)

1. **GA4 ↔ Ads gekoppeld + RSA gesync?** → herinterpreteer Direct vs Paid/Cross-network; Paid Search conv. >0?
2. **GSC beschikbaar?** → prijsindicatie CTR, Heerenveen-rang op Drachten-URL, Drenthe-hub op `/`.
3. **Prijsindicatie entry-bounce <45%?** → mobile ATF-effect.
4. **`vloerverwarming-assen.html`:** bounce/duur/scrollers na layout-fix?
5. **Search terms report** → negatives bijstellen; `extra_rsa --apply` pas na schone attributie + PO-akkoord.
6. **Facebook:** conv. >0 na message-match kalender?

## Hashtags (social — referentie)

Facebook 0–3 of geen; Instagram 5–10; LinkedIn 3–5. Standaard: `#vloerverwarming`, `#Drenthe` / `#Groningen`, `#renovatie` / `#nieuwbouw` — max. 1–2 regio-tags per post. Zie playbook `marketing-research-agent.md`.
