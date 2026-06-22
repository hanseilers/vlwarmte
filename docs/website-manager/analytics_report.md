# Analytics Rapport — 22 juni 2026 (cyclus 18)

> **PM-CORRECTIE (22 jun, na schrijven van dit rapport): GA4-data is alsnog ververst.**
> De PM heeft de fetch-blokkade opgelost (`from __future__ import annotations` in `scripts/ga4_fetch.py` → nu Python 3.9-compatibel) en verse data opgehaald (`ga4_report.json`, generated 2026-06-22T06:09). **De cijfers in de tabellen hieronder (8 juni-momentopname) zijn dus achterhaald.** Verse kernbevindingen:
> - **Verkeer is bijna volledig ingestort:** weektrend 15–21 jun = **1 sessie** (vorige weken 15–16). De Google Ads-leadmotor lijkt gepauzeerd of zonder budget.
> - **Conversies 30d gedaald van 35 → 9** (google/cpc 6 + direct 3; organic 0).
> - **www/non-www is al correct:** `vlwarmte.nl` → `www.` (301), canonical wijst naar www — geen fix nodig, GSC-split is historisch en consolideert vanzelf.
> - Home: 36 sessies, 94 sec, 61% bounce. Prijsindicatie: 9 sessies, **362 sec** duur, 22% bounce (sterkste pagina, te weinig instroom).
> - Geo: Drenthe 13 / Groningen 8 / Friesland 7 = 28 kern; North+South Holland 12 buiten kern.
> **Urgentste actie deze cyclus: eigenaar moet Ads-campagnestatus/budget checken — de leadstroom is feitelijk stilgevallen.**

**Periode GA4:** 30 dagen, momentopname **8 juni 2026** (niet ververst — zie waarschuwing)
**Vorige sprint:** cyclus 17 (15 juni) — SEO-cannibalisatie Zuidlaren, installatiebedrijf-blok, Hoogeveen FAQ-schema, home title/meta + prijsindicatie-CTA
**Focus:** leadgeneratie voor vloerverwarming in Noord-Nederland

---

## Datawaarschuwing (lees dit eerst)

**De GA4-data is niet ververst en is nu twee weken oud (8 juni).** De fetch kon opnieuw niet draaien: in de autonome modus is het uitvoeren van Python (`.venv/bin/python scripts/ga4_fetch.py`) geblokkeerd — alleen lezen en read-only shell-commando's (zoals `grep`) zijn toegestaan. Dit is exact de escalatie die in cyclus 17 al als hoogste prioriteit stond en die nog steeds open is.

Gevolg: de cijfers hieronder zijn **identiek aan die van cyclus 17**. Ik kan dus **niet** meten of de cyclus-17-wijzigingen effect hebben gehad — daar is verse data voor nodig. Behandel alle conclusies als richting, niet als actuele stand.

**Wat ik wél kon doen:** controleren of de cyclus-17-wijzigingen live in de HTML staan (zie volgende sectie) en op basis daarvan de voorstellen aanscherpen.

> **Escalatie #1 (onverminderd hoogste prioriteit):** GA4-fetch werkend krijgen. Zonder dit blijft de hele cyclus elke week op dezelfde verouderde momentopname sturen en kan geen enkel sprinteffect gemeten worden. Oplossing: óf de venv-runner (`.venv/bin/python`) toestaan in de autonome-modus-permissies, óf het script door de eigenaar handmatig laten draaien vóór de PM-cyclus zodat `ga4_report.json` vers is.

---

## Vorige sprint: wat staat er live? (HTML-verificatie)

Zonder verse data is het beste signaal of de implementatie correct deployed is. Gecontroleerd in de live HTML:

| Cyclus-17-taak | Status in HTML | Bewijs |
| --- | --- | --- |
| Home title "Vloerverwarming Drenthe, Groningen & Friesland" | ✅ live | `index.html` regel 9 |
| Home description met "Drenthe" expliciet | ✅ live | `index.html` regel 10-11 |
| Hero-CTA naar prijsindicatie + offerte-deeplink boven de vouw | ✅ live | `index.html` regel 81-84 |
| Anker "vloerverwarming Zuidlaren" in hero-lead | ✅ live | `index.html` regel 79 |
| Contentblok "Installatiebedrijf in Zuidlaren" | ✅ live | `index.html` regel 196 (H2) |
| FAQPage-schema op Hoogeveen-pagina | ✅ live | `vloerverwarming-hoogeveen.html` (1× `FAQPage`) |

Conclusie: alle vijf cyclus-17-taken staan correct live. Het **meten** van het effect (GSC-posities zuidlaren/hoogeveen/installatiebedrijf, home-bounce, prijsindicatie-instroom) kan pas zodra GA4 + GSC ververst zijn. Dat is de eerste taak van de PM/eigenaar deze week.

---

## Kerncijfers (30d, per 8 jun — ongewijzigd t.o.v. cyclus 17)

| Metric | Waarde | Opmerking |
| --- | --- | --- |
| Sessies (30d, top-bronnen) | ~149 | desktop 72 / mobile 59 / tablet 18 |
| Conversies (30d) | 35 totaal | google/cpc 22 + direct 13 |
| Gem. sessieduur home | 47,6 sec | matig — overtuigt traag |
| Bounce home | 67% | net onder de zorggrens van 70% |
| Bounce prijsindicatie | 32% | sterk — de werkpaardpagina |

Conversie-aandeel: **google/cpc + direct samen ~100% van de leads**. Organic search en social: **0 conversies**.

## Top pagina's (sessies, 30d)

| Pagina | Sessies | Gem. duur | Bounce |
| --- | --- | --- | --- |
| / (home) | 121 | 48 sec | 67% |
| /prijsindicatie.html | 22 | 100 sec | 32% |
| /contact.html | 11 | 30 sec | 27% |
| /projecten.html | 10 | 20 sec | 60% |
| /diensten.html | 5 | 32 sec | 0% |
| /werkwijze.html | 5 | 266 sec | 0% |

## Zwakste pagina's (laag verkeer / hoge bounce / korte duur)

| Pagina | Signaal |
| --- | --- |
| /projecten.html | 20 sec sessieduur, 60% bounce — bezoekers haken snel af; weinig overtuigingskracht |
| Stadspagina's (assen, groningen, leeuwarden) | 1-2 sessies elk, deels <10 sec duur — nauwelijks instroom, dunne funnel |
| /faq.html | 13 sec duur — bezoekers vinden hun antwoord niet of scrollen niet |

## Traffic bronnen (30d)

| Kanaal | Sessies | Conversies | Ratio |
| --- | --- | --- | --- |
| google / cpc (Cross-network) | 85 | 22 | ~26% |
| direct / (none) | 42 | 13 | ~31% |
| google / organic | 9 | 0 | 0% |
| facebook (social, alle varianten) | 7 | 0 | 0% |
| overig (not set / unassigned) | ~6 | 0 | 0% |

---

## Observaties

1. **Google Ads + direct dragen vrijwel alle leads** (22 + 13 van 35). Zakt het Ads-kanaal, dan zakt de leadstroom mee. Direct converteert zelfs nog iets beter (~31%) — deels merkbekendheid, deels Ads-bezoekers die terugkomen.
2. **Organisch levert nog steeds 0 leads** (9 sessies, 0 conv). De cyclus-17-SEO-ingrepen (zuidlaren/hoogeveen, title/meta-CTR) moeten dit op termijn verbeteren, maar of dat lukt is **niet meetbaar zonder verse GSC/GA4-data**.
3. **Prijsindicatie is de sterkste conversiepagina** (entry-conversie ~44%, bounce 32%, 100-132 sec duur) maar krijgt te weinig instroom (9 entry-sessies). De cyclus-17-CTA naar prijsindicatie staat nu boven de vouw — effect hierop is de belangrijkste te meten KPI zodra data vers is.
4. **Home is het grootste lek én de grootste hefboom:** 115 entry-sessies, 67% bounce → ~78 bezoekers vertrekken zonder actie. Eén procentpunt bounce minder weegt hier zwaarder dan elke andere optimalisatie.
5. **Verkeer daalde ruim 90% sinds de piek van 27 apr** (172 → ~15-16/week). Plausibel: lager Ads-budget en/of zomerseizoen. Nog steeds onverklaard/onbevestigd — moet door Marketing Research Agent geverifieerd worden in het Ads-account.
6. **Mogelijke geo-verspilling in Ads:** North Holland (25) + South Holland (11) + Brabant (8) = 44 sessies buiten kerngebied, bijna evenveel als Drenthe (33). De geo-defaults staan al op Drenthe/Groningen/Friesland, maar de live campagne (id 23834672782) draait mogelijk nog NL-breed — escalatie uit cyclus 17, nog niet bevestigd doorgevoerd.

---

## Voorstellen voor Product Manager

> Max 10, gesorteerd op prioriteit. Door de databevriezing is voorstel 1 (fetch repareren) de randvoorwaarde voor alle metingen; de overige bouwen voort op de bevroren 8-juni-data en de openstaande cyclus-17-kansen.

**1. GA4-fetch repareren — randvoorwaarde voor de hele cyclus**
- Prioriteit: **Hoog**
- Onderbouwing: data is nu 2 weken oud en al twee cycli niet ververst; geen enkel sprinteffect (cyclus 17) is meetbaar zonder verse cijfers.
- Actie: venv-Python (`.venv/bin/python`) toestaan in de autonome-modus-permissies, óf de eigenaar laat `scripts/ga4_fetch.py` handmatig draaien vóór de PM-cyclus. Idem voor GSC (`scripts/gsc_fetch.py`).
- Verwacht effect: vanaf volgende cyclus stuurt het team op actuele data; cyclus-17-effect wordt eindelijk meetbaar.

**2. Dedicated `vloerverwarming-drenthe.html` aanmaken** — grootste latente SEO-kans
- Prioriteit: **Hoog**
- Onderbouwing: "vloerverwarming drenthe" = meeste impressies van alle queries (82 @ pos ~66), versnipperd over 4 pagina's (home, prijsindicatie, diensten, faq), 0 clicks. Geen kanonieke pagina. Stond als `[WACHT]` in cyclus 17, expliciet ingepland voor cyclus 18.
- Actie: één gefocuste landingspagina naar model van de bestaande stadspagina's: `Service` + `areaServed` = Drenthe, canonical, wederzijdse interne links naar alle stadspagina's, en de home-Drenthe-hub omzetten naar een teaser om nieuwe cannibalisatie te voorkomen.
- Verwacht effect: van pagina 6-7 richting pagina 2-3 haalbaar bij gebundelde signalen; structurele organische leadbron voor het hele werkgebied.

**3. www vs non-www canonical/redirect controleren** — SEO-signaalverlies
- Prioriteit: **Midden**
- Onderbouwing: GSC toont losse rijen voor `vlwarmte.nl/` (pos ~5,6) én `www.vlwarmte.nl/` (pos ~52,8) voor dezelfde homepage; de www-variant rankt veel slechter. De canonical wijst naar `https://www.vlwarmte.nl/` — als de feitelijke serving/redirect daarmee niet strookt, verdunnen de signalen. Stond als `[WACHT]` in cyclus 17.
- Actie: eerst diagnose (canonical-tags + redirect-gedrag GitHub Pages/DNS), dan pas ingrijpen.
- Verwacht effect: gebundelde ranking-signalen op één host = hogere positie homepage, betere CTR.

**4. Ads-status/budget + geo verifiëren** — leadmotor + budgetlek
- Prioriteit: **Hoog** (voor Marketing Research Agent / eigenaar)
- Onderbouwing: verkeer −90% sinds piek 27 apr; 44 sessies (28%) buiten kerngebied. Live campagne "VLW-API-Leads NL auto" (id 23834672782, €2/dag).
- Actie: Marketing Research Agent / eigenaar checkt in het Ads-account of de daling bewust is (budget/pauze/seizoen) en of de geo strak op Noord-NL staat:
  `python scripts/google_ads_update_campaign_geo.py --campaign-id 23834672782 --dry-run` (daarna `--apply`).
- Verwacht effect: daling verklaard; lagere cost-per-lead doordat budget naar bereikbare klanten gaat.

**5. Ads-landingsafstemming richting prijsindicatie** — conversiekans
- Prioriteit: **Midden**
- Onderbouwing: prijsindicatie converteert ~44% (entry) vs home ~23%, maar krijgt maar 9 entry-sessies. De home-CTA naar prijsindicatie staat sinds cyclus 17 boven de vouw; gerichte Ads-landing erbovenop versterkt dat.
- Actie: Marketing Research Agent toetst of een deel van de Ads-klikken direct op `prijsindicatie.html` kan landen i.p.v. alleen home.
- Verwacht effect: meer leads bij gelijk budget door hogere conversieratio.

**6. Projecten-pagina overtuigender maken** — engagementkans
- Prioriteit: **Midden**
- Onderbouwing: `/projecten.html` 20 sec sessieduur, 60% bounce, 10 sessies — bezoekers met intentie (ze klikken door naar "uitgevoerd werk") haken alsnog af. Zwakke schakel in de vertrouwensopbouw.
- Actie: meer/betere projectfoto's + korte concrete cases (regio, type vloer, doorlooptijd) en een duidelijke CTA naar prijsindicatie/offerte onderaan. NB: beeldmateriaal raakt op (sinds mei geen nieuwe foto's) — aanlevering door team is randvoorwaarde.
- Verwacht effect: langere sessieduur, lagere bounce, meer doorklik naar de funnel.

**7. Home-bounce structureel verlagen (vervolg op cyclus 17)** — grootste hefboom
- Prioriteit: **Midden** (afhankelijk van meting)
- Onderbouwing: home 115 entry-sessies @ 67% bounce, 48 sec duur. Cyclus 17 voegde de boven-de-vouw-CTA toe; of dat de bounce verlaagt is nog niet meetbaar.
- Actie: eerst meten (na fetch-fix). Als bounce nog hoog blijft: sociale bewijskracht/garantie hoger in de pagina, of een lichtere micro-conversie (bv. "richtbedrag in 2 min") direct in de hero benadrukken. Geen pop-ups.
- Verwacht effect: elk procentpunt bounce minder ≈ 1 extra doorklikker; cumulatief enkele extra leads/maand.

**8. Friesland-dekking versterken** — onderbenutte regio
- Prioriteit: **Laag**
- Onderbouwing: "vloerverwarming friesland" ~88e positie ondanks bestaande Leeuwarden-pagina; Friesland 11 sessies. Zwakste van de drie kernregio's.
- Actie: pas oppakken ná de Drenthe-pagina (voorstel 2) — zelfde aanpak, lagere prioriteit. Eerst de grootste regioterm structureel fixen.
- Verwacht effect: betere regiodekking op termijn; nu niet rendabel genoeg t.o.v. Drenthe.

---

## Samenvatting voor Product Manager (kort)

1. **Databevriezing — top blocker:** GA4 staat al twee cycli stil op 8 juni; fetch is geblokkeerd in autonome modus (Python-uitvoering niet toegestaan). Hierdoor is **geen enkel cyclus-17-effect meetbaar**. Eerst dit fixen (voorstel 1), anders blijft het team op verouderde data sturen.
2. **Cyclus-17-werk staat correct live** (home title/meta + CTA, Zuidlaren-blok + ankers, Hoogeveen FAQ-schema) — geverifieerd in de HTML. Klaar om te meten zodra data vers is.
3. **Leadmotor = Google Ads (22 conv) + direct (13 conv); organisch nog 0 leads.** Grootste structurele kans blijft de **dedicated Drenthe-pagina** (voorstel 2) — was [WACHT], nu ingepland voor cyclus 18.
4. **Verkeer −90% sinds piek 27 apr** en 44 sessies buiten Noord-NL: laat Marketing Research Agent het Ads-budget/-status en de geo (campagne 23834672782) verifiëren (voorstel 4).
5. **Beste conversiepagina = prijsindicatie (~44%) maar te weinig instroom;** stuur Ads gerichter daarheen (voorstel 5). Beeldmateriaal raakt op — nieuwe foto's aanleveren is randvoorwaarde voor de projecten-pagina (voorstel 6).
