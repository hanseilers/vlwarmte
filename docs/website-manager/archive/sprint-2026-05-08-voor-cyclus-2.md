# Sprint — week van 26 mei 2026

**PM beslissing genomen op:** 08-05-2026 — volledige agentcyclus (Analytics → Marketing-research-update → Social → Developer) op basis van verse `ga4_report.json` (8 mei) en `analytics_report.md`.  
**Doel deze sprint:** **Betaald verkeer laten converteren** (Paid Search zonder conversies) + **FAQ- en systemen-landings** een duidelijke tweede stap geven; homepage **consistente merknaam** voor Google sitenaam-signaal.  
**Meetdoel:** Per **5 juni 2026** in GA4: ≥1 conversie uit **Paid Search** óf duidelijk lagere bounce op `/faq.html` en `/systemen-producten.html` als landing; homepage blijft stabiel (geen bounce-stijging op `/`).

---

## Goedgekeurde taken voor Developer Agent

### Taak 1: `index.html` — merknaam zichtbaar + `WebSite` `alternateName` `[GOEDGEKEURD]`

**Bron:** Analytics 8 mei + gebruikersvraag organische sitenaam (Google Search Central — site names).  
**Prioriteit:** Hoog  
**Type:** SEO

**Actie:** In de hero-lead doorlopend **“VLWarmte”** als gewone tekst (bijv. `<strong>VLWarmte</strong>`) i.p.v. alleen de opgesplitste wordmark in de eerste zin. In JSON-LD `@graph` → `WebSite`: voeg **`alternateName`** toe (bijv. `vlwarmte.nl`) naast bestaande `name":"VLWarmte"`.

**Succescriterium:** Schema Markup Validator zonder fout op `WebSite`-node; visueel geen dubbele merkstack in de hero; `h1` ongewijzigd.

---

### Taak 2: `systemen-producten.html` — knoppenstack onder hero `[GOEDGEKEURD]`

**Bron:** Analytics — gem. sessieduur **~7 s**, landing bounce **1,0** op kleine cohort; pagina had wel tekst-CTA maar één primaire knop.  
**Prioriteit:** Hoog  
**Type:** conversie

**Actie:** Eerste `cta-band` direct onder de hero: zelfde patroon als `diensten.html` — **`.cta-band-stack`** met primaire knop `prijsindicatie.html` en secundaire `faq.html`, korte copy.

**Succescriterium:** Op 375px breedte zijn beide knoppen zonder scroll in de `cta-band` zichtbaar; geen tweede `h1`.

---

### Taak 3: `faq.html` — vroege `cta-band` onder hero `[GOEDGEKEURD]`

**Bron:** Analytics / research — FAQ is lang; landers zagen eerst alleen accordeon zonder duidelijke **prijs- of contactstap** boven de vouw.  
**Prioriteit:** Hoog  
**Type:** conversie

**Actie:** Direct onder `page-hero` een compacte **`cta-band`** met `prijsindicatie.html` + `contact.html?modus=informatie#aanvraag` (`.cta-band-stack`).

**Succescriterium:** Eerste scherm mobiel toont duidelijke vervolgstap vóór het eerste FAQ-item; heading-hiërarchie blijft logisch (`h1` in hero, daarna `h2` in CTA-blok).

---

## Uitgestelde voorstellen `[WACHT]`

- **Google Ads copy/final URL’s** — geen repo-code; Marketing voert skill + `google_ads_lead_campaign_defaults.json` / campagnebeheer lokaal uit (agents zelf, geen PO-terminal).
- **Stadspagina’s bounce 1,0** — cohort 6 sessies; eerst meten na eerdere hero-soft-row.
- **`projecten.html` met echte cases** — blijft afhankelijk van klantfoto/toestemming.

---

## Afgewezen voorstellen `[AFGEWEZEN]`

- **Nieuwe stadspagina of wizard-grote refactors** — niet nodig voor dit datapunt.

---

## Social Media

**Status:** Zie `docs/website-manager/social/weekly_calendar.md` — **week van 26 mei 2026**.  
**Actie vereist:** Handmatige publicatie door VLWarmte team.

---

## Context voor volgende sprint

- Paid Search vs. organic social: beide zonder conversies in huidige export — prioriteit **cpc** boven Facebook-referral voor leadtest.
- `calculator_complete` staat live; over 2–4 weken funnelanalyse.

---

## Developer Rapport — 8 mei 2026

### Geïmplementeerde taken

- **Taak 1 — `index.html`:** Hero-lead start met `<strong>VLWarmte</strong>`; `WebSite` in JSON-LD uitgebreid met `"alternateName":"vlwarmte.nl"`.
- **Taak 2 — `systemen-producten.html`:** Eerste `cta-band` gebruikt `.cta-band-stack` (prijsindicatie + FAQ).
- **Taak 3 — `faq.html`:** Nieuwe `cta-band` direct onder hero met prijsindicatie + informatie-dieplink naar contact.

### Kwaliteit

- `tests/smoke/navigation-links.sh` — **PASS**
- `tests/smoke/form-behavior.sh` — **PASS**

### Deployment

- **Status:** lokaal geïmplementeerd in repo; push door eigenaar/CI zoals gebruikelijk.
