# Analytics Rapport — 1 mei 2026

**Periode:** laatste 30 dagen (GA4: `30daysAgo` → `today`)  
**Databron:** `docs/website-manager/ga4_report.json` (gegenereerd 2026-05-01T15:37:50)  
**Vorige sprint effect:** Events en stadspagina’s zijn zichtbaar in het verkeer: `prijsindicatie.html` en de twee stadspagina’s staan in de top 15; **conversies** tellen nu mee in kanalen (direct 19, unassigned 11 in dit exportvenster). Volume is fors omhoog t.o.v. eind april.

---

## Kerncijfers

| Metric | Waarde | Toelichting |
| ------ | ------ | ----------- |
| Sessies (laatste week in export) | 155 | `weekly_trend` met `week_start` 2026-04-24 — één week in deze export |
| Actieve gebruikers (zelfde week) | 136 | |
| Traffic-kanalen (30 dagen, top) | Direct 136; Unassigned 23; Organic (Bing) 4; Facebook-referrals 10 | Google **organic** ontbreekt nog in de top-7 bucket — volume zit vooral in direct + tagging-gaten (`Unassigned`) |
| Conversions (GA4-standaard in dit export) | o.a. 19 (direct), 11 (unassigned) | Custom events lijken **wel** mee te tellen als conversies in deze property — goed voor funnel-analyse |

**Homepage-split:** `/` 66 sessies vs `/index.html` 12 — dezelfde inhoud blijft dubbel meetbaar.

---

## Top pagina’s (30 dagen)

| Pagina | Sessies | Actieve gebruikers | Gem. sessieduur (s) | Bounce (fractie) |
| ------ | ------- | ------------------ | ------------------- | ---------------- |
| `/` | 66 | 56 | ~84 | **0,86** |
| `/prijsindicatie.html` | 20 | 13 | ~319 | 0,55 |
| `/over-ons.html` | 15 | 14 | ~15 | **0,87** |
| `/contact.html` | 14 | 11 | ~162 | 0,71 |
| `/diensten.html` | 12 | 10 | ~6 | **0,83** |
| `/index.html` | 12 | 9 | ~361 | 0,58 |
| `/systemen-producten.html` | 10 | 10 | ~23 | 0,80 |
| `/werkwijze.html` | 9 | 9 | ~4 | **0,89** |
| `/vloerverwarming-assen.html` | 6 | 6 | 0 | **1,0** |
| `/vloerverwarming-groningen.html` | 6 | 6 | 0 | **1,0** |

\*Bij **n=6** en **sessieduur 0** op de stadspagina’s: bounce 100% is een signaal om te monitoren (intentie “snel adres/telefoon pakken” vs. echte mismatch), niet meteen een harde conclusie.

---

## Landingspagina’s (instappunten)

| Landing | Sessies | Bounce | Conversions |
| ------- | ------- | ------ | ----------- |
| `/` | 48 | ~0,85 | 3 |
| *(leeg)* | 21 | **1,0** | 6 |
| `/prijsindicatie.html` | 13 | ~0,62 | 17 |
| Overige o.a. diensten, contact, stadspagina’s | 6–9 | veelal 1,0 | laag |

**Datakwaliteit:** lege `landingPagePlusQueryString` met 21 sessies — in GA4 **definitie/controleren** (universal links, app, iOS referrer, of meetfout). Sessies tellen wél conversies; voor contentbeslissingen liever uitsluiten of herleiden zodra oorzaak bekend is.

---

## Traffic bronnen

| Kanaal | Source/Medium | Sessies | Conversions |
| ------ | ------------- | ------- | ----------- |
| Direct | (direct) / (none) | 136 | 19 |
| Unassigned | (not set) | 23 | 11 |
| Organic Search | bing / organic | 4 | 0 |
| Organic Social | facebook / lm / m / l | 10 | 0 |

---

## Apparaten & geo

- **Apparaten:** mobile 95, desktop 61 — mobiel is dominant; UX op klein scherm blijft prioriteit.
- **Geo (sessies):** **Drenthe 106** — past bij thuisbasis en “Zuidlaren”-gerelateerde zoekintentie; Groningen 4; Noord-/Zuid-Holland en VS nog aanwezig (deels bots/irrelevant — segment “NL + Drenthe/Groningen” helpt bij lezen).

---

## Zoektermen vs. dit rapport

Het script `scripts/ga4_fetch.py` schrijft **geen** zoekwoorden weg (GA4 geeft voor Google-organisch vrijwel geen termen meer; detail zit in **Google Search Console**). Als jij in de GA4-UI “installateur Zuidlaren” ziet, komt dat waarschijnlijk uit een **GSC- of verkenner-rapport** of een **andere dimensie** (bijv. Bing, campagne). Voor landingspagina-prioriteit: **Search Console → pagina’s + query’s** naast deze GA4-export gebruiken.

---

## Observaties

1. **Volume en Drenthe** — duidelijke stijging; doelregio weegt zwaar. Goed moment om **hyperlokale** pagina’s te beoordelen (niet alleen Groningen/Assen).
2. **Wizard en conversies** — `prijsindicatie` als landing heeft relatief lage bounce en hoge conversies in dit export: het blijft de sterkste commerciële landingsroute.
3. **Stadspagina’s Assen/Groningen** — al zichtbaar (6+6 sessies), maar **0 s gemiddelde sessieduur** in deze slice: controleer in GA4 **of** het meetartefacten zijn (tab sluiten, enkel event) of dat er echt geen engagement is; zo nodig boven de fold strakkere CTA naar wizard/contact.
4. **`/` bounce hoog** — veel bezoekers vertrekken zonder tweede hit; hero/primary CTA blijft relevant.
5. **“Installateur Zuidlaren”** — bestaande titels op Groningen/Assen noemen al “installateur uit Zuidlaren”, maar de **H1 is de stad** (Groningen/Assen). Wie precies “Zuidlaren” in de query zet, krijgt **geen** pagina waar Zuidlaren in de titel/H1 centraal staat. Dat is een inhoudelijke kloof met de signaalterm.

---

## Voorstellen voor Product Manager

1. **Prioriteit: Hoog — Landingspagina Zuidlaren (hyperlokaal)**  
   - **Onderbouwing:** Signaal uit analytics (zoekterm) + **106 sessies Drenthe** + vestiging in Zuidlaren. Groningen/Assen-pagina’s dekken “grote stad + installateur uit Zuidlaren”, niet “Zuidlaren” als primaire plek.  
   - **Actie:** Nieuwe pagina bv. `vloerverwarming-zuidlaren.html` met H1/titel in de trant van **vloerverwarming + Zuidlaren + installateur** (zonder overdreven marketingtaal), korte reistijd naar Tynaarlo/Paterswolde/Haren/Groningen-zuid in één alinea,zelfde blokken als andere stadspagina’s (infrezen, CTA wizard/contact), `Service` + `areaServed` Zuidlaren, footer + sitemap.  
   - **Verwacht effect:** betere match met query’s rond Zuidlaren; meetbaar in GSC op “zuidlaren” + in GA4 landingspad.

2. **Prioriteit: Hoog — Canonieke homepage**  
   - **Onderbouwing:** 66 vs 12 sessies op `/` vs `/index.html`.  
   - **Actie:** Eén strategie (redirect of één interne linkstijl + canonical), zoals eerder voorstel.  
   - **Verwacht effect:** schonere rapportage en sterker signaal naar zoekmachines.

3. **Prioriteit: Midden — Search Console koppelen aan beslissing**  
   - **Onderbouwing:** Zoektermen staan niet in `ga4_report.json`.  
   - **Actie:** In GSC filteren op queries met “Zuidlaren”, “installateur”, “vloerverwarming”; op basis daarvan volgorde voor **volgende** stad/dorp-pagina’s (bijv. Hoogeveen, Emmen) bepalen.  
   - **Verwacht effect:** minder gissen, betere prioriteit dan alleen GA4-paginapaden.

4. **Prioriteit: Midden — Lege landing (21 sessies)**  
   - **Onderbouwing:** bounce 1,0; vreemd voor contentbeslissingen.  
   - **Actie:** In GA4-exploratie bron/medium en technologie; eventueel intern filter.  
   - **Verwacht effect:** betrouwbaardere landingspagina-toplijst.

5. **Prioriteit: Midden — Stadspagina’s: engagement**  
   - **Onderbouwing:** 100% bounce en 0 s gemiddeld op beide stadspagina’s in deze export.  
   - **Actie:** Plaats boven de vouw één duidelijke regel + knop naar prijsindicatie; eventueel scroll-event (als jullie dat willen meten) — alleen als na check geen meetfout.  
   - **Verwacht effect:** meer wizard_start vanaf SEO-landingspagina’s.

6. **Prioriteit: Laag — `logo-varianten.html` in data**  
   - **Onderbouwing:** 7 sessies in top_pages — als die URL offline is, zijn dit resthits of externe links; geen prioriteit tenzij het blijft groeien.  
   - **Actie:** 301 naar home of 410; anders negeren.  
   - **Verwacht effect:** schonere toplijst.

---

## Marketing Agent vs. Analytics Agent (afspraak)

- **Analytics Agent** (`.claude/commands/analytics-agent.md`): data ophalen met `ga4_fetch.py`, dit rapport, prioriteiten op basis van **gedrag en cijfers**.  
- **Marketing Research Agent**: zoekvolume, concurrenten, **zoekintentie** en copy-richting — aanvullend op Search Console/websearch.  

Voor **“installateur Zuidlaren” + landingspagina’s**: start met **Analytics** (wat landt waar, conversies, geo), vul **Marketing Research** in voor concurrentie en exacte titel/H2-woorden — of één sessie waarin eerst fetch+rapport, daarna marketing dezelfde sprint aanvult.

---

## Synthese

De site heeft **meer verkeer en conversies** dan in het april-rapport; **Drenthe domineert**, wat het idee voor een **eigen Zuidlaren-landingspagina** ondersteunt. Implementatie is een **developer/sprint**-taak; dit document blijft de input voor prioriteit.
