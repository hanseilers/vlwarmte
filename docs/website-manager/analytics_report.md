# Analytics Rapport — 8 mei 2026 (cyclus 3)

**Periode:** laatste 30 dagen (GA4)  
**Databron:** `docs/website-manager/ga4_report.json` (laatste succesvolle export: **2026-05-08T13:40:51**; `python3 scripts/ga4_fetch.py` faalde op deze machine door ontbrekende Python-module `google.analytics` — installatie: `pip install google-analytics-data` in je venv)  
**Vorige sprint (week 2 juni, repo):** CTA-band `prijsindicatie.html`, exitlinks disclaimer/privacy, `hero-soft-row` projecten, RSA-defaults — **stond lokaal klaar maar nog niet gecommit** tot deze PM-ronde.

---

## Kerncijfers

| Metric | Waarde |
| ------ | ------ |
| `weekly_trend` weken | **8** |
| Week 1–7 mei | **54** sessies / **34** actieve gebruikers |
| Week 24–30 apr | **134** / **122** |

**Top pagina’s (30 dagen, `top_pages`):** `/` (104 sessies, bounce ~0,61), `/contact.html`, `/prijsindicatie.html` (bounce ~0,32), `/diensten.html` (~0,52), `/over-ons.html`, `/werkwijze.html` (gem. duur **~15 s**), `/systemen-producten.html` (gem. **~7 s**).

---

## Landings (selectie, `entry_pages`)

| Landing | Sessies | Bounce | Conversions |
| ------- | ------- | ------ | ----------- |
| `/` | 83 | 0,64 | **27** |
| `/diensten.html` | 14 | **0,79** | 0 |
| `/prijsindicatie.html` | 12 | 0,67 | **20** |
| `/contact.html` | 7 | **0,86** | **3** |
| `/disclaimer.html` | 7 | **1,00** | 0 |
| `/werkwijze.html` | 7 | 0,86 | **3** |
| `/projecten.html` | 6 | **1,00** | 0 |
| `/systemen-producten.html` | 6 | **1,00** | 0 |
| Stadspagina’s (Assen/Groningen) | 6 | **1,00** | 0 |

**Paid Search (`google/cpc`):** **11** sessies, **0** conversies — campagne + landingsafstemming blijven prioriteit na live zetten van prijs-CTA’s.

---

## Traffic bronnen (fragment)

| Kanaal | Sessies | Conversies |
| ------ | ------- | ---------- |
| Direct | 171 | 52 |
| Paid Search | 11 | **0** |
| Organic Search (google) | 1 | 1 |

---

## Observaties

1. **Prijsindicatie** blijft het sterkste conversiepad; landingsbounce 0,67 is ruim boven pagina-gemiddelde — CTA boven de vouw (sprint vorige week) moet na deploy meetbaar helpen.  
2. **`werkwijze.html`**: korte gemiddelde tijd (~15 s) en weinig scrollers in 90d-engagement — bezoeker vindt snel antwoord of stapt uit; **SEO-snippet en lokale context** kunnen verwachting beter laten aansluiten.  
3. **`diensten.html` als landing**: bounce **0,79** — er is al een `cta-band`; een **lichtere derde stap** (terugbel) kan intentie vangen zonder offerte-druk.  
4. **Disclaimer/privacy** blijven riskante landings (bounce 1,0) — exit-secties staan in repo klaar voor push.  
5. **Paid Search zonder conversies** — na live: RSA’s in Ads bijwerken t.o.v. `google_ads_lead_campaign_defaults.json` en conversies in GA4/Ads nalopen (skill).

---

## Voorstellen PM (ingekort)

1. **`[Hoog]`** Zet vorige sprint live (commit/push) zodat meting niet blijft hangen op oude HTML.  
2. **`[Hoog]`** **`werkwijze.html` + `over-ons.html`**: title + meta description (+ OG/Twitter) verrijken met **Zuidlaren / Drenthe / traject** — SEO, sluit aan op korte sessies.  
3. **`[Hoog]`** **`diensten.html` + `faq.html`**: in bestaande `cta-band` een knop **Terugbelverzoek** (`contact.html?modus=bel#aanvraag`) — CTA, vangt twijfel tussen prijs en formulier.  
4. **`[Midden]`** **`index.html`**: meta description iets uitbreiden met **online prijsindicatie** — SERP-clariteit voor homepage-landings.  
5. **`[WACHT]`** Google Ads RSA-mutatie live — pas na deploy + secrets op agent-machine.

---

## Gedrag PM

Na developer: **`git commit` + `git push origin main`** (stap 7b playbook).
