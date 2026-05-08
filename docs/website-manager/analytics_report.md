# Analytics Rapport — 7 mei 2026

**Periode:** laatste 30 dagen (GA4: `30daysAgo` → `today`)
**Databron:** `docs/website-manager/ga4_report.json` (gegenereerd 2026-05-07T17:53:19)
**Fetch-status:** `python3 scripts/ga4_fetch.py` succesvol uitgevoerd (verse export).
**Vorige sprint effect (week 11 mei, deployment ~6 mei):** Eerste signalen na uitrol. **`/contact.html` als landing:** bounce **0,86** (was 1,00 in mei-export), **3 conversions** op 7 sessies (was **0**). Dat is precies het gedrag waar de sprint op mikte — nog niet “klaar” t.o.v. meetdoel <0,80 bounce, maar wel een meetbare verschuiving. **`/prijsindicatie.html` als landing:** bounce **0,64**, **20 conversions** op 11 sessies — blijft de sterkste motor.

---

## Kerncijfers

| Metric | Waarde | Toelichting |
| ------ | ------ | ----------- |
| Sessies homepage `/` (30d) | 87 | Instappunt |
| Bounce homepage | 0,53 | Ruim onder 70%-norm |
| Mobile vs. desktop | 102 vs. 87 | Mobiel blijft dominant |
| Direct-kanaal | 163 sessies, **52 conversions** | Kern van het verkeer |
| `weekly_trend` rijen | **8** | Script aangepast 7 mei: lege weekresponses worden met `sessions`/`activeUsers` **0** backfilled |

**Week-over-week (8 disjuncte weken in `ga4_report.json`):**

| week_start | week_end | Sessies | Actieve gebruikers |
| ---------- | -------- | ------- | ------------------ |
| 2026-03-12 | 2026-03-18 | 0 | 0 |
| 2026-03-19 | 2026-03-25 | 0 | 0 |
| 2026-03-26 | 2026-04-01 | 0 | 0 |
| 2026-04-02 | 2026-04-08 | 0 | 0 |
| 2026-04-09 | 2026-04-15 | 0 | 0 |
| 2026-04-16 | 2026-04-22 | 0 | 0 |
| 2026-04-23 | 2026-04-29 | 99 | 94 |
| 2026-04-30 | 2026-05-06 | 88 | 61 |

---

## Top pagina’s (30 dagen)

| Pagina | Sessies | Gebruikers | Gem. duur (s) | Bounce |
| ------ | ------- | ---------- | ------------- | ------ |
| `/` | 87 | 70 | 88 | 0,53 |
| `/prijsindicatie.html` | 28 | 18 | **118** | **0,25** |
| `/contact.html` | 20 | 16 | 70 | **0,40** |
| `/diensten.html` | 20 | 14 | 86 | **0,50** |
| `/over-ons.html` | 18 | 16 | 32 | 0,39 |
| `/index.html` | 17 | 12 | 314* | 0,35 |
| `/werkwijze.html` | 14 | 13 | **15** | 0,43 |
| `/systemen-producten.html` | 13 | 13 | **7,2** | 0,46 |
| `/logo-varianten.html` | 9† | 7 | 141* | 0,75 |
| `/projecten.html` | 7 | 7 | **0,9** | **0,86** |
| `/vloerverwarming-groningen.html` | 7 | 7 | 56 | **0,86** |

\*Zelfde caveat als eerdere rapporten: enkele zeer lange sessies trekken gemiddelde omhoog.
†`logo-varianten.html` bestaat niet meer als inhoudspagina; deels 404-titel in export — restverkeer en bookmarks.

---

## Landingspagina’s (top uit export)

| Landing | Sessies | Bounce | Conversions |
| ------- | ------- | ------ | ----------- |
| `/` | 68 | 0,56 | **27** |
| `/diensten.html` | 13 | **0,77** | 0 |
| `/prijsindicatie.html` | 11 | 0,64 | **20** |
| `/contact.html` | 7 | **0,86** | **3** |
| `/vloerverwarming-groningen.html` | 6 | **1,00** | 0 |
| `/vloerverwarming-assen.html` | 6 | **1,00** | 0 |
| `/projecten.html` | 6 | **1,00** | 0 |
| `/systemen-producten.html` | 6 | **1,00** | 0 |

**Interpretatie:** Prijsindicatie blijft extreem sterk. Contact-landing toont **herstel** t.o.v. eerdere “alles stuitert”-meting, maar stadspagina’s en `projecten`/`systemen` als **instap** blijven 1,00 bounce — daar is nog geen tweede klik zichtbaar in GA4.

---

## Traffic bronnen

| Kanaal | Sessies | Conversions |
| ------ | ------- | ----------- |
| Direct | 163 | 52 |
| Organic Social (Facebook) | 17 | 0 |
| Organic Search (o.a. Bing) | 4 | 0 |
| Organic Search Google | 1 | 1 |
| Paid Search Google | 2 | 0 |

Google-organisch blijft **minimaal** in deze property-export — GSC-koppeling blijft de belangrijkste blind spot voor SEO-iteratie.

---

## Geo (top)

- **Drenthe:** 123 sessies — kernregio.
- **Groningen (NL):** 4 sessies — laag t.o.v. Drenthe; stadspagina blijft strategisch relevant maar volume is dun.
- **VS-staten** (Colorado, Oregon, Iowa, NC, Virginia): bot/ruis — uit PM-segment halen bij interpretatie.

---

## Voorstellen voor Product Manager

### 1. `[Hoog]` Restverkeer `logo-varianten.html` — SEO-hygiëne

Oude URL blijft sessies trekken. Minimale **redirect-landingspagina** (canonical + meta refresh naar `/` of `over-ons.html`) voorkomt 404-ervaring en consolideert signaal.

### 2. `[Hoog]` `diensten.html` — landing bounce 0,77, 0 conv

Bezoeker landt op dienstenoverzicht maar start geen tweede stap. **Compact CTA-blok direct onder hero** (prijsindicatie + FAQ), zelfde patroon als `systemen-producten.html`.

### 3. `[Hoog]` `werkwijze.html` — korte verblijfsduur (~15 s)

De eerste `cta-band` staat pas na het zes-stappenblok. **Verplaats of kopieer** een compacte CTA direct onder de hero zodat mobile scanners een pad zien zonder te scrollen.

### 4. ~~`ga4_fetch.py` — `weekly_trend` altijd 8 weken~~ **Gedaan 7 mei** (backfill bij lege API-response).

### 5. `[WACHT / monitor]` Stadspagina’s als landing

Nieuwe hero-soft-row uit vorige sprint staat live; **eerste echte cohort** pas na 2–3 weken extra data. Geen extra code deze sprint tenzij bounce na meting nog 1,00 blijft.

---

## Gedrag PM

Max. 5 developer-taken; minstens één SEO-gericht (logo-URL) en één CTA (`diensten` + `werkwijze` dekt conversie).
