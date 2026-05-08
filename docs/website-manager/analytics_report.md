# Analytics Rapport — 8 mei 2026 (cyclus 4)

**Periode:** laatste 30 dagen (GA4)  
**Databron:** `docs/website-manager/ga4_report.json` (fetch **2026-05-08T14:21:14**, `.venv/bin/python scripts/ga4_fetch.py`)

---

## Kerncijfers

| Metric | Waarde |
| ------ | ------ |
| `weekly_trend` | laatste week in export: **2026-05-01** t/m **2026-05-07** — **54** sessies / **34** actieve gebruikers (week ervoor **134** / **122**) |
| Homepage `/` (top pages) | **105** sessies, bounce **~0,61** |

**Top pagina’s (30 dagen):** `/`, `/contact.html`, `/prijsindicatie.html` (bounce **~0,32**), `/diensten.html` (**~0,52**), `/over-ons.html`, `/werkwijze.html` (gem. **~15 s**), `/systemen-producten.html` (gem. **~7 s**).

---

## Landings (selectie)

| Landing | Sessies | Bounce | Conversions |
| ------- | ------- | ------ | ----------- |
| `/` | 84 | 0,64 | **27** |
| `/diensten.html` | 14 | **0,79** | 0 |
| `/prijsindicatie.html` | 12 | 0,67 | **20** |
| `/over-ons.html` | 9 | **0,78** | 0 |
| `/contact.html` | 7 | **0,86** | **3** |
| `/disclaimer.html` | 7 | **1,00** | 0 |
| `/werkwijze.html` | 7 | **0,86** | **3** |
| `/projecten.html` | 6 | **1,00** | 0 |
| `/systemen-producten.html` | 6 | **1,00** | 0 |
| Stadspagina’s | 6 | **1,00** | 0 |

**Paid Search (`google/cpc`):** **12** sessies, **0** conversies (+1 sessie t.o.v. vorige export) — blijft hoogste betaalde prioriteit na live snippet/CTA-iteraties.

---

## Observaties

1. **Diensten** en **over-ons** als landing houden bounce **~0,78–0,79** — snippets kunnen dichter tegen **lokale intentie + prijs/terugbel** aanzitten (recent terugbel op diensten/FAQ staat pas kort live in data).  
2. **Contact** als landing: bounce **0,86** ondanks drie directe routes — SERP-snippet mist waarschijnlijk **terugbel** en **Zuidlaren**.  
3. **Systemen-producten** als landing: bounce **1,0** bij kleine cohort — zelfde **terugbel**-patroon als diensten/FAQ helpt tweede stap.  
4. **Projecten** landing bounce **1,0** — `hero-soft-row` heeft alleen informatie; **terugbel** maakt het pallet compleet.  
5. **FAQ** is sterk intern; meta kan **infrezen / warmtepomp** explicieter voor organisch.

---

## Voorstellen PM

1. **`[Hoog]`** `diensten.html` — **head SEO** (title + description + OG/Twitter): Zuidlaren, Drenthe, traject, verwijzing naar prijsindicatie en licht contact.  
2. **`[Hoog]`** `contact.html` — **head SEO**: offerte, informatie, **terugbelverzoek**, Zuidlaren, reactie binnen werkdag.  
3. **`[Hoog]`** `systemen-producten.html` — **head SEO** + knop **Terugbelverzoek** in vroege `cta-band`.  
4. **`[Midden]`** `projecten.html` — **terugbel** naast informatie in `hero-soft-row`.  
5. **`[Midden]`** `faq.html` — **head SEO** (infrezen, warmtepomp, terugbel/prijsindicatie in description).

---

## Gedrag PM

Na developer: **`git commit` + `git push origin main`**.
