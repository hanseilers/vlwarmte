# VLWarmte Website Voorstellen

> Gegenereerd op: 28 april 2026  
> Gebaseerd op GA4 data van: **niet beschikbaar** — `ga4_report.json` is leeg; live fetch deze run niet gelukt (Python-deps / credentials-pad).  
> Volgende analyse aanbevolen: **na succesvolle `ga4_fetch.py` + minimaal 7 dagen data na live-gang sprint 27 april** (richting 12–19 mei 2026)

---

## Samenvatting

De site heeft net een sterke technische en lokale SEO-sprint gehad (events, Search Console-tagplek, twee stedelijke pagina’s, nav opgeschoond). Zonder verse GA4-cijfers zijn voorstellen nu **inhoudelijk en marketing-gedreven**, afgestemd op `docs/website-manager/research_report.md` en de open punten uit de huidige `sprint.md`. De grootste hefboom voor de komende periode is een **volwaardige FAQ** plus **interne verwijzingen naar de prijsindicatie-wizard** — dat versterkt organische dekking én het meetbare conversiepad zodra de data binnenkomt.

### Kerncijfers (afgelopen 30 dagen)

- Sessies: _onbekend (geen data in JSON)_
- Actieve gebruikers: _onbekend_
- Beste pagina: _n.v.t._
- Zwakste pagina: _n.v.t._
- Hoofdkanaal: _n.v.t._

---

## Voorstellen

### 1. FAQ-pagina met schema en interne links

- **Prioriteit:** Hoog
- **Type:** Nieuwe pagina / SEO
- **Onderbouwing:** `research_report.md` — grootste content gap; geen GA4 nodig om prioriteit te verdedigen.
- **Actie:** `faq.html` met 12–15 vragen (long-tail uit research), `FAQPage`-schema, links vanaf `index.html`, `vloerverwarming-groningen.html`, `vloerverwarming-assen.html`.
- **Verwacht effect:** meer organische instap op vraagtermen; rich snippet-kans.

### 2. Wizard-CTA’s op diensten, werkwijze en systemen

- **Prioriteit:** Hoog
- **Type:** CTA / conversie
- **Onderbouwing:** Sprint-context `[WACHT]` — uitrol interne links; straks zichtbaar in events `wizard_*`.
- **Actie:** Korte blokken met link naar `prijsindicatie.html` op logische plekken per pagina.
- **Verwacht effect:** hoger aandeel bezoekers in de wizard-funnel.

### 3. Schuimbeton — eigen H2 met anker

- **Prioriteit:** Midden
- **Type:** Content update / SEO
- **Onderbouwing:** Marketing — laag volume maar zwakke concurrentie; kleine aanpassing.
- **Actie:** H2 `#schuimbeton` + korte uitleg op bestaande pagina (diensten of systemen, consistent met site).
- **Verwacht effect:** betere landingsdiepte voor schuimbeton-zoektermen.

### 4. Homepage FAQ-snippet uitbreiden

- **Prioriteit:** Midden
- **Type:** Content update / SEO
- **Onderbouwing:** Marketing aanbeveling 6; ondersteunt voorstel 1.
- **Actie:** 5–6 items + link naar volledige FAQ.
- **Verwacht effect:** meer doorklik naar FAQ en contact/wizard.

### 5. Geplande data-review (geen implementatie)

- **Prioriteit:** Midden
- **Type:** Technisch / proces
- **Onderbouwing:** Meetdoel sprint (25 mei); events staan volgens sprint klaar.
- **Actie:** Op eigen machine `ga4_fetch.py` draaien; in GA4 conversies markeren; notitie in volgende sprint.
- **Verwacht effect:** onderbouwde optimalisaties i.p.v. giswerk.

### 6. Wizard-resultaat: mini-proof wanneer materiaal er is

- **Prioriteit:** Laag
- **Type:** Content / CTA
- **Onderbouwing:** Marketing sectie 5 + sprint `[WACHT]` — afhankelijk van case van Hans.
- **Actie:** Eén regel referentie in resultaatkaart zodra project/foto akkoord.
- **Verwacht effect:** lichte trustwinst op het moment van beslissen.

### 7. Google Bedrijfsprofiel + reviews (off-site)

- **Prioriteit:** Laag (impact op termijn hoog)
- **Type:** Marketing (off-site)
- **Onderbouwing:** Research concurrentie/trust; geen sitewijziging vereist.
- **Actie:** Profiel compleet; na oplevering review vragen; later embed.
- **Verwacht effect:** betere click-through en geloofwaardigheid in de regio.

---

## Data snapshot

| Pagina      | Sessies | BounceRate |
| ----------- | ------- | ---------- |
| _Geen data_ | —       | —          |

---

## Aanbeveling voor Product Manager (concept-sprint 2)

Samenvattend voor `sprint.md` (max. 5 taken — PM vult definitief in):

1. **FAQ-pagina** — `[GOEDGEKEURD]`-kandidaat (SEO + long-tail).
2. **Interne wizard-links** op diensten/werkwijze/systemen — `[GOEDGEKEURD]` (CTA/conversie).
3. **Schuimbeton H2 + anker** — `[GOEDGEKEURD]` of `[WACHT]` als tijd krap is.
4. **Homepage FAQ-uitbreiding** — `[GOEDGEKEURD]` of samenvoegen met taak 1 als één “FAQ-programma”.
5. **Mobiele doorloop-test** (Hans) — blijft proces; desnoods `[WACHT]` tot bewijs binnen is.

_Zie ook:_ `docs/website-manager/analytics_report.md` voor dezelfde lijn en databeperking.
