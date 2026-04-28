# Analytics Rapport — 28 april 2026

**Periode:** laatste 30 dagen (GA4: `30daysAgo` → `today`)  
**Databron:** `docs/website-manager/ga4_report.json` (gegenereerd 2026-04-28T15:46:49)  
**Vorige sprint effect:** Sprint week 27 apr is uitgerold (events, stadspagina’s, nav); dit rapport vangt nog **weinig post-deploy volume** — meet opnieuw over 2–4 weken voor Search Console + nieuwe URL’s.

---

## Kerncijfers

| Metric                                    | Waarde                  | Toelichting                                                                                             |
| ----------------------------------------- | ----------------------- | ------------------------------------------------------------------------------------------------------- |
| Sessies (laatste week in export)\*        | 13                      | Alleen `weekly_trend` met `week_start` 2026-04-21; korte trendreeks in huidige export                   |
| Traffic-kanalen                           | Direct 12; Unassigned 1 | **Geen Organic / Paid / Referral** in de top — merk/direct-first; SEO nog niet zichtbaar in dit venster |
| Conversions (GA4 standaard in dit export) | 0                       | Zet custom events (`wizard_*`, `contact_submit`) als **conversies** in GA4 als dat nog niet is gedaan   |

**Sessies op pagina’s (top_paths):** let op dubbele homepage: `/` (10 sessies) en `/index.html` (4) — dezelfde inhoud, dubbele meting.

---

## Top pagina’s (30 dagen)

| Pagina                 | Sessies                                            | Actieve gebruikers | Gem. sessieduur (s)                        | BounceRate\*   |
| ---------------------- | -------------------------------------------------- | ------------------ | ------------------------------------------ | -------------- |
| `/`                    | 10                                                 | 8                  | ~160                                       | 0,70 → **70%** |
| `/index.html`          | 4                                                  | 3                  | ~171                                       | 0              |
| `/diensten.html`       | 2                                                  | 2                  | ~13                                        | 0              |
| `/prijsindicatie.html` | 2                                                  | 2                  | ~65                                        | 0              |
| `/contact.html`        | 1                                                  | 1                  | ~135                                       | 0              |
| Overige (1 sessie elk) | over-ons, projecten, systemen-producten, werkwijze | …                  | kort op systemen (~2,7s) en over-ons (~3s) | 0              |

\*GA4 `bounceRate` in de API is een fractie 0–1; **>0,7 = zorgwekkend** bij voldoende volume. Bij **n=1** per pagina is bounce weinig zinvol.

---

## Landingspagina’s

| Landing       | Sessies | BounceRate                                     |
| ------------- | ------- | ---------------------------------------------- |
| `/`           | 9       | ~0,67 → **~67%**                               |
| `/index.html` | 3       | 0                                              |
| _(leeg)_      | 1       | 100% — datakwaliteit: filter of herleid in GA4 |

---

## Traffic bronnen

| Kanaal     | Source/Medium     | Sessies | Gebruikers | Conversions |
| ---------- | ----------------- | ------- | ---------- | ----------- |
| Direct     | (direct) / (none) | 12      | 9          | 0           |
| Unassigned | (not set)         | 1       | 1          | 0           |

**Implicatie:** acquisitie is nu vooral **direct/merk**. Marketing + technische SEO (GSC, sitemap, FAQ, stadspagina’s) moeten **Organic** gaan vullen — pas daarna heeft dit dashboard meer zin voor content-optimalisatie per pagina.

---

## Apparaten & regio

- **Apparaten:** in dit exportvenster **alleen desktop** (13 sessies / 10 gebruikers) — mobiel mist of is nul; handmatige mobiele test blijft nodig (zie sprint `[WACHT]`).
- **Geo (sessies):** Nederland Drenthe 7; Groningen 1; VS (Colorado, Iowa, Virginia) 5 — **deel VS** kan tooling/bots zijn; in GA4 segmentatie controleren voordat je conclusies trekt over “internationaal bereik”.

---

## 90 dagen scroll (indicator)

Op `/`: `scrolledUsers` 2 bij 10 sessies — **lage scroll-diepte** op homepage; overweeg boven-de-fold duidelijker pad naar wizard of contact (interne links + CTA).

---

## Observaties

1. **Laag volume** — conclusies zijn indicatief; herbereken na groei en na GSC-indexering stadspagina’s.
2. **`/` vs `/index.html`** — splitsing verwaterd rapportage; technisch **één canonieke homepage** (redirect of één interne linkstijl) helpt interpretatie.
3. **Prijsindicatie** — 2 sessies, ~65 s gemiddeld: positief signaal voor betrokkenheid bij kleine n.
4. **Systemen + over-ons** — zeer korte sessies bij 1 sessie elk: geen harde uitspraak mogelijk; wél reden om na groei **scroll/exit** te monitoren.
5. **Geen organische bucket** — past bij vroege fase; meetdoel sprint (Search Console + stadstermen) blijft leidend.

---

## Voorstellen voor Product Manager

1. **Prioriteit: Hoog — Canonieke homepage**
   - **Onderbouwing:** 10 vs 4 sessies op `/` en `/index.html`.
   - **Actie:** 301 van `index.html` → `/` of consistente interne links + canonical (één strategie met developer).
   - **Verwacht effect:** schonere pagina-rapportage en betere SEO-signalen.

2. **Prioriteit: Hoog — FAQ + interne links (sprint-2)**
   - **Onderbouwing:** geen organic in data; research zegt FAQ = grootste long-tail-hefboom.
   - **Actie:** `faq.html` + wizard-CTA’s op diensten/werkwijze/systemen.
   - **Verwacht effect:** eerste organische sessies meetbaar in volgende fetch.

3. **Prioriteit: Midden — Homepage: bounce / scroll**
   - **Onderbouwing:** landings-bounce `/` ~67%; weinig scrollers in 90d-export.
   - **Actie:** Sterker primair pad (prijsindicatie/contact); eventueel hero-copy A/B na baseline-events.
   - **Verwacht effect:** lagere bounce, meer wizard_start.

4. **Prioriteit: Midden — GSC + conversiemarkering**
   - **Onderbouwing:** 0 conversions in export; sprint had events + placeholder-tag.
   - **Actie:** Token invullen, sitemap indienen, events als conversies markeren.
   - **Verwacht effect:** Search data + conversie-dashboard.

5. **Prioriteit: Midden — Stadspagina’s promoten**
   - **Onderbouwing:** nieuwe URL’s staan nog niet in top 9 pagina’s (volume te klein).
   - **Actie:** Social + interne links + (later) betaalde/test campagnes optioneel.
   - **Verwacht effect:** sessies op `/vloerverwarming-groningen.html` en `-assen.html` in volgende rapporten.

6. **Prioriteit: Laag — Geo-filter / uitsluiting**
   - **Onderbouwing:** VS-sessies bij kleine dataset.
   - **Actie:** GA4: intern verkeer / ongewenste regio’s uitsluiten of segment “alleen NL”.
   - **Verwacht effect:** schonere besluitvorming voor lokale doelgroep.

---

## Synthese voor volgende sprint

Data bevestigt: **weinig verkeer, vooral direct, homepage dominant, calculator en contact al interessant**. Prioriteit blijft: **meetbaarheid afronden (GSC + conversies)** en **organische laag (FAQ + links + stadspagina’s laten indexeren)**. Herbereken eind mei zoals in `sprint.md` afgesproken.
