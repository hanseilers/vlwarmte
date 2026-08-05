# Sprint — week van 5 augustus 2026 (cyclus 24)

**PM beslissing genomen op:** 5 augustus 2026, 11:15
**Doel deze sprint:** Meetklok cyclus 20/21 is verstreken — `prijsindicatie` en de rijpere stadspagina's (Heerenveen, Drachten) mogen weer als hefboom. Vijf autonoom-veilige ingrepen: Friese SEO-cadans (Leeuwarden FAQ), Heerenveen FAQ + breadcrumbs op beide Friese diepe pagina's, prijsindicatie ATF-versterking en homepage-doorstroom naar de wizard. De drie harde blokkades (conversie-meting, GSC, gesloten Ads-account) escaleren opnieuw — geen developer-taken.
**Meetdoel (over ~4 weken, mits GSC herstelt):** `prijsindicatie` krijgt meer `wizard_start`-events en lagere landing-bounce; Leeuwarden + Heerenveen krijgen FAQ-rich-result-eligibility; homepage-doorstroom naar `prijsindicatie` meetbaar in navigatie; geen daling in instroom door de wijzigingen.

---

## Belangrijkste databevindingen deze cyclus (verse GA4, per 5 aug)

1. **Instroom licht lager, laatste week herstel.** 17 sessies/30d (↓19% t.o.v. cyclus 23). Week 29 jul–4 aug: **6 sessies** na dieptepunt van 1 — te vroeg voor trend, maar geen verdere daling.
2. **Betaald kanaal: account GESLOTEN.** Campagne staat ENABLED maar Ads-account is `CLOSED`, geen billing, auto-tagging uit, RSA's in `REVIEW_IN_PROGRESS`. Dat verklaart 0 impressies — niet de landingspagina's. Eigenaar moet account heropenen + betaalmethode koppelen.
3. **0 conversies — 5e cyclus.** `prijsindicatie` toont 112 s/30d en 135 s/90d engagement — meetfout (key events niet gemarkeerd) blijft waarschijnlijker dan lege trechter. Hardste escalatie.
4. **Homepage lekt harder.** 85% bounce (was 75%), 71% van landings. Doelregio kromp in: **1 sessie** (alleen Groningen; Drenthe 0, Friesland 0). Cyclus 23 meta-targeting nog niet zichtbaar effectief.
5. **`prijsindicatie` groeit.** 2 → 4 sessies/30d — enige pagina met instroomstijging. Meetklok verstreken → mag weer aangepakt worden.
6. **GSC nog steeds blind.** OAuth `invalid_grant` (8+ weken); `REPLACE_WITH_TOKEN` op 19 pagina's.

---

## Goedgekeurde taken voor Developer Agent

### Taak 1: Lokale FAQ + `FAQPage`-schema op `vloerverwarming-leeuwarden.html` `[GOEDGEKEURD]`
**Bron:** Analytics Agent (voorstel 5) + Marketing Research Agent (taak 5)
**Prioriteit:** Hoog
**Type:** SEO / content-verrijking + conversie-routing
**Actie:**
- Voeg **na** het "Ook actief in"-blok en **vóór** de CTA-sectie een FAQ-sectie toe, exact volgens het Hoogeveen-sjabloon (`vloerverwarming-hoogeveen.html` regels 230–264): `<section class="section"><div class="container"><div class="section-head"><h2>Veelgestelde vragen — Leeuwarden</h2></div>` + drie `<div class="faq-item">`-blokken met `<button class="faq-question" data-faq-toggle>…</button>` en `<div class="faq-answer"><p>…</p></div>`.
- Gebruik **lokaal ingekleurde**, inhoudelijk unieke vragen:
  1. "Werken jullie ook in Stiens, Grou en de dorpen rond Leeuwarden?" (noem echte randkernen)
  2. "Wat kost vloerverwarming in Leeuwarden?" — **antwoord verwijst met link naar `prijsindicatie.html`**
  3. "Kunnen jullie infrezen in een bestaande dekvloer in Leeuwarden?"
- Voeg in de `<head>`, na het bestaande `BreadcrumbList`-script, een nieuw `<script type="application/ld+json">` toe met `{"@type":"FAQPage","mainEntity":[…]}`, waarin `name`/`acceptedAnswer.text` **woordelijk** overeenkomen met de zichtbare Q&A's.
**Succescriterium:** `grep '"FAQPage"' vloerverwarming-leeuwarden.html` → één treffer; zichtbare vraagteksten matchen JSON-LD 1-op-1; kosten-antwoord linkt naar `prijsindicatie.html`; accordeon werkt.

### Taak 2: `prijsindicatie.html` — kosten-verankeringsblok boven wizard `[GOEDGEKEURD]`
**Bron:** Analytics Agent (voorstel 4) + Marketing Research Agent (taak 4)
**Prioriteit:** Hoog
**Type:** CRO / conversie (ATF message-match)
**Actie:**
- Voeg een **additief** compact blok toe **direct boven** de wizard/calculator (niet de wizard-flow herschrijven): 2–3 zinnen die uitleggen wat de wizard doet (richtbedrag in 2 minuten, excl. btw, indicatief) + interne links naar `systemen-producten.html#laagopbouw` en minstens één relevante stadspagina.
- Gebruik bestaande CSS-patronen (bijv. `.section`, `.container`, of een bestaand info-blok uit de pagina). Geen nieuwe primaire CTA die concurreert met de wizard-knop.
- Optioneel: `FAQPage`- of `HowTo`-schema rond de kosten-uitleg als het past bij de zichtbare tekst.
**Succescriterium:** Zichtbaar kosten-uitlegblok staat boven de wizard; bevat link naar `#laagopbouw`; wizard-flow ongewijzigd; pagina rendert correct op mobiel.

### Taak 3: `BreadcrumbList`-schema op Heerenveen en Drachten `[GOEDGEKEURD]`
**Bron:** Analytics Agent (voorstel 6) + Marketing Research Agent (taak 7)
**Prioriteit:** Midden
**Type:** SEO / structured data
**Actie:** Voeg `BreadcrumbList`-JSON-LD toe in de `<head>` van `vloerverwarming-heerenveen.html` en `vloerverwarming-drachten.html`, conform het patroon op de andere stadspagina's (bijv. `vloerverwarming-groningen.html`). **Alleen schema; geen inhoudelijke wijzigingen.**
**Succescriterium:** `grep '"BreadcrumbList"'` geeft op beide bestanden elk ≥ 1 treffer; JSON-LD is valide (Home → Diensten → [Stad]).

### Taak 4: Lokale FAQ + `FAQPage`-schema op `vloerverwarming-heerenveen.html` `[GOEDGEKEURD]`
**Bron:** Marketing Research Agent (taak 6)
**Prioriteit:** Midden
**Type:** SEO / content-verrijking + Ads-keyword-afstemming
**Actie:** Idem taak 1, maar voor Heerenveen. Drie lokaal ingekleurde vragen, bijv.:
  1. "Werken jullie ook in Joure, Sneek en de dorpen rond Heerenveen?"
  2. "Wat kost vloerverwarming in Heerenveen?" — **link naar `prijsindicatie.html`**
  3. "Kunnen jullie vloerverwarming infrezen in een bestaande woning in Heerenveen?"
- Voeg `FAQPage`-JSON-LD toe in `<head>`, na breadcrumbs (taak 3).
**Succescriterium:** FAQ zichtbaar + `FAQPage`-schema; kosten-antwoord linkt naar wizard; unieke vragen t.o.v. Leeuwarden/Drachten.

### Taak 5: Homepage — compacte kosten-band onder hero `[GOEDGEKEURD]`
**Bron:** Analytics Agent (voorstel 7)
**Prioriteit:** Midden
**Type:** CRO / doorstroom (secundaire routing)
**Actie:** Voeg direct **onder** de hero-sectie op `index.html` een compacte trust/kosten-band toe: 1–2 zinnen + secundaire link "Richtbedrag in 2 minuten →" naar `prijsindicatie.html`. **Geen hero-herbouw, geen extra primaire CTA, H1 ongemoeid.** Gebruik bestaande band/section-styling.
**Succescriterium:** Band staat direct onder hero; bevat link naar `prijsindicatie.html`; hero/CTA/H1 ongewijzigd; geen tweede primaire CTA-knop.

---

## Uitgestelde voorstellen `[WACHT]`
- **FAQ Zuidlaren + Drenthe-hub** — volgende sprint(s), cadans één stad per cyclus.
- **Drachten FAQ** — na Heerenveen/Leeuwarden; Drachten heeft al 107s engagement zonder FAQ.
- **GSC-verificatietoken site-breed** — wacht op eigenaar-token; developer kan pas vervangen als token beschikbaar is.
- **Ads RSA #3 final URLs syncen** — wacht op account heropening + RSA-approval.

## Afgewezen voorstellen `[AFGEWEZEN]`
- **Homepage-hero herbouwen** — afgewezen: hoog risico op enige pagina met substantieel verkeer; bounce deels verkeerd-publiek.
- **Wizard-flow herschrijven** — afgewezen: net uit maturatie; eerst additief ATF-blok (taak 2).
- **`--go-live` op Ads** — afgewezen: account gesloten, geen billing; eerst eigenaar-actie.

---

## Harde escalaties (eigenaar, niet developer)

### Escalatie 1 — Conversie-meting (5e cyclus, 0 conversies)
Formspree-inboxen `xzdojzdk` + `xgodnvoq` controleren. GA4 → Admin → Events: `wizard_lead_submit`, `lead_form_submit`, `contact_submit` als **key event** markeren.

### Escalatie 2 — GSC OAuth vernieuwen
`python scripts/gsc_get_refresh_token.py` met verified owner-account. Echt site-verificatietoken leveren voor `REPLACE_WITH_TOKEN`.

### Escalatie 3 — Google Ads-account heropenen
Accountstatus `CLOSED`, geen billing, auto-tagging uit. Heropenen + betaalmethode op ads.google.com → Billing. Auto-tagging aanzetten. RSA-review afwachten.

---

## Social Media
**Status:** Weekplanning staat in `docs/website-manager/social/weekly_calendar.md`
**Actie vereist:** Handmatige publicatie door VLWarmte team

---

## Context voor volgende sprint
- Meet effect taak 2+5 op `wizard_start` en homepage→prijsindicatie navigatie in GA4.
- Meet FAQ-effect Leeuwarden/Heerenveen in GSC zodra OAuth hersteld is.
- Check of Ads-account heropend is → dan RSA-review en serveerstatus opvolgen.
- Drachten FAQ is logische volgende SEO-stap.

---

## Developer Rapport — 5 augustus 2026, 11:35
- Geïmplementeerde taken:
  1. FAQ + `FAQPage`-schema op `vloerverwarming-leeuwarden.html` (3 lokale vragen, kosten-antwoord linkt naar `prijsindicatie.html`)
  2. Kosten-verankeringsblok boven wizard op `prijsindicatie.html` (richtbedrag-uitleg + links naar `#laagopbouw` en Heerenveen)
  3. `BreadcrumbList`-schema op `vloerverwarming-heerenveen.html` en `vloerverwarming-drachten.html` (Home → stad, conform Leeuwarden/Groningen-patroon)
  4. FAQ + `FAQPage`-schema op `vloerverwarming-heerenveen.html` (3 unieke lokale vragen, kosten-antwoord linkt naar wizard)
  5. Compacte kosten-band onder hero op `index.html` (secundaire tekstlink naar `prijsindicatie.html`, hero/H1 ongewijzigd)
- Overgeslagen taken: geen — alle 5 goedgekeurde taken uitgevoerd
- Deployment: **Live** — commit `69e4e01`, GitHub Pages run `30993116057` (success, 5 aug 09:24 UTC)
- Live URL: https://www.vlwarmte.nl
- Smoke tests: `tests/smoke/navigation-links.sh` PASS · `tests/smoke/form-behavior.sh` PASS
- Aandachtspunten voor volgende sprint: BreadcrumbList op Friese stadspagina's is 2-niveau (geen Friesland-hub zoals Drenthe); optioneel `FAQPage` op Drachten blijft backlog. Prijsindicatie ATF op mobiel kan iets lager vallen door het nieuwe introblok — monitoren in GA4 `wizard_start`.
