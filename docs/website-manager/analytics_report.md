# Analytics Rapport — 8 mei 2026

**Periode:** laatste 30 dagen (GA4, `30daysAgo`–`today`)  
**Bron:** `docs/website-manager/ga4_report.json` (fetch **2026-05-08**; `.venv/bin/python scripts/ga4_fetch.py`)  
**Vorige sprint (effect in data):** sprint week 16 juni staat gepland; in deze export zie je vooral **huidige** landings/bounce-patronen (o.a. diensten/contact/systemen/projecten) die de sprint al target — meet **na livegang** opnieuw.

**Let op:** deze export bevat **geen exitpagina’s** en **geen eventnamen** (`contact_submit`, enz.). *Key events* hieronder = **GA4-conversies per kanaal/landing** + **wekelijkse sessietrend**. Voor event-trends: GA4 Explorations of script uitbreiden.

---

## Kerncijfers (samenvatting)

| Indicator | Waarde | Toelichting |
| --------- | ------ | ----------- |
| Sessies (som kanalen) | **247** | O.a. Direct dominant |
| Conversies (som kanalen) | **61** | Kanaalverdeling zie onder |
| Week–week sessies | **134** → **54** | Weken **2026-04-24–04-30** vs **2026-05-01–05-07** — **daling ~60%**; oude weken in 8-weeksreeks tonen **0** (weinig/geen historische dekking in die vensters) |
| Apparaten | **124** desktop / **113** mobile | Bijna fifty-fifty |

---

## Top landings (instap)

| Landing | Sessies | Bounce | Conversies |
| ------- | ------- | ------ | ----------- |
| `/` | **87** | 0,66 | **27** |
| `/prijsindicatie.html` | **15** | 0,67 | **21** |
| `/diensten.html` | **14** | **0,79** | 0 |
| *(lege string)* | **13** | **1,00** | 6 |
| `/index.html` | **9** | 0,44 | 0 |
| `/over-ons.html` | **9** | **0,78** | 0 |
| `/contact.html` | **8** | **0,88** | 3 |
| `/contact.html?modus=offerte` | **7** | 0,71 | 1 |
| `/disclaimer.html` | **7** | **1,00** | 0 |
| `/logo-varianten.html` | **7** | **0,86** | 0 |
| `/systemen-producten.html` | **7** | **1,00** | 0 |
| `/werkwijze.html` | **7** | **0,86** | 3 |
| `/privacy.html` | **6** | **1,00** | 0 |
| `/projecten.html` | **6** | **1,00** | 0 |
| `/vloerverwarming-assen.html` | **6** | **1,00** | 0 |

**Exit-proxy (geen exitdimensie in export):** landings met bounce **1,0** zijn **sterke exit-/single-page signalen** (o.a. legal/stads/project/systemen — weinig vervolgstap).

---

## Traffic-kanalen (belangrijkste)

| Kanaal | Bron/medium (voorbeeld) | Sessies | Conv. |
| ------ | ------------------------ | ------- | ----- |
| Direct | `(direct) / (none)` | **184** | **53** |
| Unassigned | `(not set)` | **16** | **7** |
| Organic Social | Facebook referral | **30** totaal | **0** |
| **Paid Search** | **`google / cpc`** | **12** | **0** |
| Organic Search | o.a. Bing | **4** | **0** |
| Organic Search | `google / organic` | **1** | **1** |

**Marketing Research (Ads):** Paid Search blijft **12 sessies, 0 conversies** — zelfde patroon als vorige cyclus: aparte regel in backlog voor **campagnes, landingsafstemming** en **conversiemeting** (zie `.cursor/skills/google-ads-marketing/SKILL.md`, GA4 ↔ Ads).

---

## Key events / conversies (proxy)

- **Direct** draagt het merendeel van de **61** conversies (**53** op **184** sessies).  
- **Paid + Organic Social** leveren **conversie 0** in deze export — bij social kan het ook aan **attribuutie** liggen (sessies zonder directe conversie).  
- Sterkste **landing → conversie**: homepage en **prijsindicatie** (wizard) — daar blijft de funnel warm.

---

## Geo (kort)

- **Drenthe: 143** sessies — past bij doelregio.  
- **Noord-Holland / Zuid-Holland** en **VS (Oregon, Colorado, …)** op de lijst: deels **niet-lokaal** publiek of **bots/tech**; alleen bijsturen als kwaliteit leads slecht blijkt.

---

## Opvallende punten

1. **Week-op-week -60% sessies** (134 → 54): prioriteit om te checken of dit **seizoen/campagne**, **meetfout**, of **echte daling** is; combineer met **Search Console** en **Ads-imp** dezelfde week.  
2. **Paid Search zonder conversies** terwijl Direct wél converteert → **landings- en boodschapmatch** + **enhanced conversions / key events** nalopen.  
3. **Landings met bounce 1,0** op **systemen**, **projecten**, **Assen-stadspagina**, **legal**: inhoud/SEO-sprint helpt, maar meet expliciet **scroll/CTA-klik** als secundaire signalen.  
4. **`/logo-varianten.html`** nog **sessies** (deels oude title-variant + 404-title) → **redirect/opschonen** om ruis te killen.  
5. **Lege `landingPagePlusQueryString`** (13 sessies, bounce 1,0): onderzoek in GA4 of dit **hostname/referrer**-artefact is; geen secrets in filters.

---

## Voorstellen voor Product Manager (weging)

1. **Prioriteit Hoog — Paid Search + conversie**  
   - *Onderbouwing:* **12** sessies, **0** conversies.  
   - *Actie:* Marketing Research: RSA/landings naar **prijsindicatie** of **contact?modus=offerte#aanvraag**; GA4 **Google Ads-koppeling** en conversieacties controleren.  
   - *Verwacht:* stijging **conversies/cpc-sessie** binnen 2–4 weken.

2. **Prioriteit Hoog — WoW-daling sessies**  
   - *Onderbouwing:* **134 → 54** sessies in opeenvolgende 7-dagenblokken.  
   - *Actie:* PM: korte **hypothesetabel** (Ads-budget, indexering, seizoen); developer alleen als technische oorzaak (404-spike, tag).  
   - *Verwacht:* heldere oorzaak + één **correctieve actie** op backlog.

3. **Prioriteit Midden — Contact als landing**  
   - *Onderbouwing:* `/contact.html` bounce **~0,88** (8 sessies); `?modus=offerte` **~0,71** (7).  
   - *Actie:* snippets/ads waar mogelijk naar **modus=offerte**; sprint **head SEO + formulier boven adres** afwachten en daarna opnieuw meten.  
   - *Verwacht:* lagere bounce op contact-landings.

4. **Prioriteit Midden — Systemen/projecten landings**  
   - *Onderbouwing:* bounce **1,0** op **7** sessies elk.  
   - *Actie:* sprint-CTA’s (**terugbel**, vroege band) live houden; eventueel **interne link** vanaf homepage/diensten naar deze pagina’s.  
   - *Verwacht:* meer **secundaire paginaviews** per sessie.

5. **Prioriteit Laag — Restverkeer logo-varianten**  
   - *Onderbouwing:* nog **sessies** op `/logo-varianten.html` (mengsel titles).  
   - *Actie:* **301 naar home** of FAQ; verwijder externe/oude links.  
   - *Verwacht:* schonere **contentrapportage** en minder 404-ruis.

---

*Geen credentials of paden naar secrets in dit rapport. Detaildata staat lokaal in `ga4_report.json` (veld `credentials_source` niet committen).*
