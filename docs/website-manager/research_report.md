# Marketing Research Rapport — 18 mei 2026

**Cyclus 10** — volledige update.
**Scope:** leadgeneratie (organisch + betaald), landingskwaliteit, contentgaps en Google Ads message-match voor vlwarmte.nl in Noord-Nederland.
**Bronnen:** `.claude/commands/marketing-research-agent.md`, `.cursor/skills/google-ads-marketing/SKILL.md`, `docs/website-manager/analytics_report.md` (export `2026-05-15T12:48:01`), `docs/website-manager/ga4_report.json` (zelfde timestamp), site-HTML in de root, `scripts/data/google_ads_lead_campaign_defaults.json`, `scripts/data/google_ads_campaign_negatives.json`, vorig rapport (cyclus 9, 15 mei 2026).

## Uitvoeringsbeperking deze cyclus (transparant)

Dit was een **automatische run zonder gebruiker** in "don't ask"-modus. Daardoor waren in deze sessie **niet** beschikbaar:

- **WebSearch** — geen verse zoekvolume-/SERP-/concurrentiedata deze cyclus. De zoekwoorden- en concurrentieparagrafen leunen op de bestaande indicatieve inschatting uit cyclus 9 en op de site-/defaults-data in de repo. Niet als nieuw extern onderzoek lezen.
- **Python Google Ads-scripts** (`google_ads_smoke_test.py`, `google_ads_list_campaigns.py`, `google_ads_create_search_campaign.py`, enz.) — script-uitvoering was geblokkeerd in deze run; er is **geen verse campagne-verificatie** gedaan. De Google Ads-status hieronder is de **laatst geverifieerde stand uit cyclus 9** (15 mei 2026), niet opnieuw bevestigd. `secrets/google-ads.env` is wél aanwezig op deze machine; een volgende run met script-rechten kan de verificatie alsnog draaien.
- Geen mutaties uitgevoerd, geen `--apply`, geen `--go-live`, geen spend. Conform opdracht.

Read-only repo-inspectie (HTML, sitemap, footer, defaults-JSON) is wél gedaan en is de basis voor de conclusies.

## Samenvatting

De drie zwaarste aanbevelingen uit cyclus 9 zijn **geïmplementeerd en geverifieerd in de repo**: (1) de **crawlbare kosten-sectie** (`#kosten-uitleg` op `prijsindicatie.html`) staat live met prijsbandbreedte (€45–€95/m²), prijs-drivers, schuimbeton-uitleg en interne links naar FAQ/contact; (2) **`vloerverwarming-hoogeveen.html`** en **`vloerverwarming-leeuwarden.html`** zijn live, beide in `sitemap.xml` en de footer; (3) **`vloerverwarming-emmen.html`** idem. Daarmee verschuift de focus van "bouwen" naar **meten en aanscherpen**.

Het kernprobleem blijft **betaald = 0 conversies**: Paid Search + cross-network samen **33** sessies in 30 dagen, **0** conversies (GA4-export 15 mei). Dat is een **meet-/koppelingsprobleem** (GA4↔Ads-link, auto-tagging, conversie-import) plus **message-match**, niet primair een biedstrategieprobleem — niet opschalen voordat conversies betrouwbaar binnenkomen. Nieuwe message-match-gap: de defaults-keywords bevatten **`vloerverwarming drachten`** en **`vloerverwarming heerenveen`** (en `meppel`) terwijl er **geen eigen landingspagina** voor die steden is — die klikken landen nu op een generieke of Leeuwarden-pagina, wat conversie drukt.

## Top zoekwoorden (indicatief — geen verse Keyword Planner/WebSearch deze cyclus)

| Zoekwoord | Zoekvolume (indicatie) | Concurrentie | Pagina nodig |
|-----------|-------------------------|--------------|--------------|
| vloerverwarming kosten per m2 | hoog | hoog | bestaand — `prijsindicatie.html#kosten-uitleg` (nu live) |
| prijs vloerverwarming berekenen | hoog | hoog | bestaand — `prijsindicatie.html` |
| vloerverwarming infrezen / infrezen kosten | midden | midden | bestaand — `faq.html`, `werkwijze.html`; interne links aanscherpen |
| schuimbeton vloerverwarming kosten | midden | midden-hoog | bestaand — `diensten.html#schuimbeton`, prijsindicatie |
| kruipruimte isoleren schuimbeton | midden | midden | bestaand — `diensten.html#schuimbeton` |
| vloerverwarming groningen | hoog | hoog | bestaand — `vloerverwarming-groningen.html` |
| vloerverwarming assen | midden-hoog | hoog | bestaand — `vloerverwarming-assen.html` (engagement nog zwak) |
| vloerverwarming emmen | midden | midden-hoog | bestaand — `vloerverwarming-emmen.html` |
| vloerverwarming hoogeveen | midden-laag | midden | bestaand — `vloerverwarming-hoogeveen.html` (nieuw live) |
| vloerverwarming leeuwarden | midden | midden-hoog | bestaand — `vloerverwarming-leeuwarden.html` (nieuw live) |
| vloerverwarming drachten | midden | midden-hoog | **gap** — keyword in defaults, geen URL |
| vloerverwarming heerenveen | midden | midden-hoog | **gap** — keyword in defaults, geen URL |
| vloerverwarming meppel | midden-laag | midden | **gap** — keyword in defaults, geen URL (lagere prioriteit) |
| installateur vloerverwarming noord-nederland | midden | hoog | bestaand — `index.html`, `werkwijze.html` |
| vloerverwarming nieuwbouw / renovatie | midden | midden-hoog | bestaand + FAQ; renovatie/hout als aparte URL nog zwak |
| vloerverwarming warmtepomp combinatie | midden | midden | bestaand (FAQ + city-copy) |
| vloerverwarming renovatie houten vloer | midden | midden | **gap** — geen eigen landingspagina (wizard stuurt nu naar contact) |

**Iteratie:** zoektermenrapport in Google Ads wekelijks tegen `keywords` en `google_ads_campaign_negatives.json` zetten; nieuwe varianten terug naar defaults-JSON via normale repo-flow. Volgende run met WebSearch + script-rechten kan deze tabel met verse cijfers en SERP-observaties verrijken.

## Prijscalculator — korte conclusie

**Geen herbouw nodig — de gevraagde verbetering is geïmplementeerd.** De wizard op `prijsindicatie.html` blijft sterk (30d-export: **46** sessies, gem. duur ~84 s, pagina-bounce **32,6%** — gunstig). De in cyclus 9 aanbevolen **crawlbare kosten-uitleg** staat nu live (sectie `#kosten-uitleg`, regel ~751 e.v.): expliciete bandbreedte €45–€95/m² excl. btw, ondergrens ~€2.500, drie prijs-drivers (m², ondergrond, schuimbeton ja/nee), schuimbeton-toelichting en links naar FAQ/contact. Juridisch correct: overal "indicatie, geen offerte" en bandbreedtes; houten ondergrond stuurt bewust naar contact i.p.v. een automatische rekensom. Vervolg is **meten**, niet bouwen: volg `wizard_calculate`, `wizard_lead_submit` en `lead_form_submit` in GA4 en spiegel naar Ads-conversies (skill §A). Beoordeel na ~14–30 dagen of de **landing-bounce** op kosten-intent (was 64,7% op 17 sessies in cyclus 9) daalt nu de crawlbare tekst er staat.

## Content gaps (ontbrekende of zwakke pagina's/secties)

**Geïmplementeerd sinds cyclus 9 (afgevinkt):**
- ✅ `prijsindicatie.html` — crawlbare kosten-sectie live.
- ✅ `vloerverwarming-hoogeveen.html` — live, in sitemap + footer.
- ✅ `vloerverwarming-leeuwarden.html` — live, in sitemap + footer.
- ✅ `vloerverwarming-emmen.html` — live, in sitemap + footer.

**Open gaps:**
- **Drachten / Heerenveen message-match (nieuw urgent):** beide staan als keyword in `google_ads_lead_campaign_defaults.json` maar er is geen `vloerverwarming-drachten.html` / `vloerverwarming-heerenveen.html`. Twee opties — kies één: (a) keywords tijdelijk uit defaults halen tot er pagina's zijn, óf (b) één nieuwe Friesland-pagina (Drachten/Heerenveen) maken. Mismatch tussen advertentie-keyword en landing is een directe conversie-lek voor betaald verkeer.
- **`vloerverwarming-renovatie-houten-vloer.html` (of FAQ-cluster met vaste URL):** commerciële twijfelvraag; nu verspreid in wizard/FAQ. Wizard stuurt houten ondergrond naar contact — een indexeerbare uitlegpagina kan organisch verkeer + message-match leveren.
- **`projecten.html` — ATF:** entry blijft zwak (cyclus 9: ~100% entry-bounce, ~7,5 s). Geen nieuwe pagina; compacter eerste scherm + duo-CTA (prijsindicatie + offerte-deeplink) vóór de zware galerij.
- **`contact.html` zonder `?modus=`:** koud landen **80%** bounce. Korte intentie-keuze (info/offerte/bel) boven het modus-blok, links naar dezelfde tabs — geen dubbel formulier.
- **`vloerverwarming-assen.html`:** nieuwe hero live maar **0 scrollers (90d)**, gem. duur ~0,7 s. Lichte ATF-ingreep (anker/"lees verder" of compacte trust-band onder hero) zonder zware LCP — meet na volle 14 dagen post-live.
- **`diensten.html` / `systemen-producten.html` als landing:** bounce blijft hoog; keuzehulp resp. hero-copy staan kort live — pas volgende GA4-export hard beoordelen.
- **`vloerverwarming-meppel.html`:** blijft backlog (grens Drenthe/Overijssel), lagere prioriteit dan Drachten/Heerenveen tenzij zoektermenrapport anders zegt.

Concurrentie (geen verse SERP deze cyclus; bevestigd patroon uit eerdere cycli): aggregators domineren brede "kosten"-termen; lokaal win je op **stad + traject-uitleg + echt bewijs** (projectfoto's uit `beeldmateriaal/` — geen AI-beelden voor campagnes, conform skill creative policy).

## Google Ads — status en acties

**Status (laatst geverifieerd cyclus 9, 15 mei 2026 — niet opnieuw bevestigd deze run):** één zichtbare lead-campagne `VLW-API-Leads NL auto`, kanaal SEARCH, status ENABLED. Geen tokens of secrets-inhoud in dit document.

| Onderwerp | Actie |
|-----------|--------|
| Verificatie | Volgende run met script-rechten: `google_ads_smoke_test.py` + `google_ads_list_campaigns.py` opnieuw draaien om de ENABLED-status en numeriek id te herbevestigen. |
| GA4 ↔ Ads | **P0** — link + auto-tagging + conversie-import nalopen (skill §A). Zolang dit niet sluit blijven betaalde conversies onmeetbaar (33 sessies, 0 conversies). |
| Conversies | GA4-key events (`contact_submit`, `lead_form_submit`, `wizard_lead_submit`, `wizard_calculate`) afstemmen op wat Ads als conversie gebruikt. |
| Final URL's | Defaults `final_urls` verwijzen alle vier naar live pagina's (contact-offerte-deeplink, prijsindicatie, leeuwarden, hoogeveen) — OK. |
| Keywords/negatives | **Actie:** Drachten/Heerenveen-keywords óf pagina maken óf uit defaults halen (message-match). Negatives-lijst (15 termen) dekt jobs/DIY/tweedehands — passend; wekelijks zoektermenrapport blijft leidend. |
| Geo | Defaults `location_targeting`: Drenthe/Groningen/Friesland — past bij playbook. Monitor buitenlandse ruis in GA4 (~28 VS-sessies). |
| Helper-scripts | `google_ads_add_keywords_from_defaults.py` en `google_ads_update_campaign_geo.py` aanwezig in `scripts/` — bruikbaar in een volgende run om defaults-wijzigingen (na Drachten/Heerenveen-besluit) zonder volledige herbouw door te zetten. |
| Spend | Geen opschaling, geen `--go-live`. Geen spend-goedkeuring in deze run. |

## Aanbevelingen voor Product Manager (max. 8)

1. **Prioriteit: Hoog — GA4 ↔ Ads conversiekoppeling (P0)**
   **Type:** Meetplan + accountcontrole.
   **Onderbouwing:** 33 betaalde sessies, 0 conversies in 30d — onveranderd kernprobleem; opschalen is zinloos zonder meting.
   **Actie:** GA4↔Ads-link + auto-tagging + conversie-import (skill §A) nalopen; landingsrapport op `google/cpc` per URL. Pas daarna biedstrategie richting conversies. Vereist een run waarin de Ads-scripts mogen draaien.

2. **Prioriteit: Hoog — Drachten/Heerenveen message-match oplossen**
   **Type:** SEO/landing + Ads keywords.
   **Onderbouwing:** keywords in defaults zonder eigen URL = direct conversie-lek op betaald verkeer.
   **Actie:** kies (a) één Friesland-stadspagina (Drachten/Heerenveen, patroon = Leeuwarden) óf (b) keywords tijdelijk uit `google_ads_lead_campaign_defaults.json` tot er een pagina is. Niet beide laten staan zonder pagina.

3. **Prioriteit: Hoog — `projecten.html` ATF**
   **Type:** CRO.
   **Onderbouwing:** entry ~100% bounce, ~7,5 s — al sinds cyclus 7/8 zwak ondanks hero.
   **Actie:** compacter eerste scherm + primaire duo-CTA (prijsindicatie + offerte-deeplink) vóór galerij. Acceptatie: entry-bounce <85%, >0 scrollers binnen 30d.

4. **Prioriteit: Midden — Post-deploy meting prijsindicatie kosten-sectie**
   **Type:** Analytics-verificatie.
   **Onderbouwing:** crawlbare sectie is net live; effect op landing-bounce (was 64,7% op kosten-intent) nog niet gemeten.
   **Actie:** na volgende GA4-export landing-bounce + `wizard_calculate` op `prijsindicatie.html` vergelijken; bij uitblijvend effect ATF herzien.

5. **Prioriteit: Midden — `contact.html` koude landing**
   **Type:** UX/CRO.
   **Onderbouwing:** 80% bounce zonder `?modus=`; offerte-deeplink blijft daarentegen goudstandaard (9,1% bounce, 10 conversies).
   **Actie:** korte intentie-keuze (info/offerte/bel) boven het modus-blok, links naar dezelfde tabs — geen dubbel formulier.

6. **Prioriteit: Midden — `vloerverwarming-assen.html` engagement**
   **Type:** UX.
   **Onderbouwing:** 0 scrollers (90d), gem. duur ~0,7 s ondanks nieuwe hero.
   **Actie:** anker/"lees verder" of compacte trust-band onder hero, zonder zware LCP. Acceptatie: >0 scrollers binnen 30d.

7. **Prioriteit: Midden — `vloerverwarming-renovatie-houten-vloer.html` (of FAQ-cluster met vaste URL)**
   **Type:** Nieuwe pagina/content (max. 1 nieuwe pagina per sprint).
   **Onderbouwing:** commerciële twijfelvraag nu alleen in wizard/FAQ; wizard stuurt houten ondergrond naar contact — indexeerbare uitleg ontbreekt.
   **Actie:** één pagina of vaste FAQ-URL; kruislink naar contact/prijsindicatie.

8. **Prioriteit: Laag — `logo-varianten.html` / stub-verkeer**
   **Type:** Technisch/SEO.
   **Onderbouwing:** blijft verkeer trekken (85,7% bounce).
   **Actie:** Search Console + server-redirect controleren; geen nieuwe features tenzij indexatie aanhoudt.

## Seizoenspatroon (indicatief)

Mei–augustus: nadruk op lopende verbouwing, offerte-intent en kostenvragen — sluit aan op de nu-live crawlbare kosten-sectie. Later in het jaar: planning richting wintercomfort en renovatie/warmtepomp-combinaties. RSA-copy pas roteren na 6–8 weken betrouwbare post-fix **betaalde** data (en die data komt er pas als aanbeveling 1 is uitgevoerd).

---

**Tone:** nuchter, direct, conform AGENTS.md — geen overdreven claims. Geen secrets in dit document.
