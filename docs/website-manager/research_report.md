# Marketing Research Rapport — 2026-06-22

Bron: eerstegraads repo-data — GSC 25 apr–22 mei 2026 (`gsc_report.json`), GA4
30-daags per 8 jun (`ga4_report.json` / `analytics_report.md`), Ads-defaults
(`scripts/data/google_ads_lead_campaign_defaults.json`) en de live site-bestanden.

> **Modus-waarschuwing (lees eerst).** Deze cyclus draait autonoom in don't-ask
> mode. **WebSearch/WebFetch én alle `scripts/google_ads_*.py` zijn geblokkeerd**
> (bevestigd: smoke-test, list-campaigns en `.venv/bin/python` werden geweigerd;
> zie memory `pm-scheduled-run-permissions`). Er is dus **geen vers webonderzoek**
> (live zoekvolumes, actuele concurrent-SERP's, calculator-benchmarkstudies) en
> **geen live Ads-state/mutatie** uitgevoerd deze ronde. Alle conclusies hieronder
> zijn gebaseerd op de echte first-party data in de repo; web- en Ads-afhankelijke
> punten staan expliciet als **escalatie** met klaargezette commando's.

## Samenvatting

De leadmotor is onverminderd **betaald + direct** (google/cpc 22 conv, direct 13
conv); **organisch levert 0 conversies** terwijl de site honderden impressies op
regiotermen verzamelt op posities die net buiten of ver buiten de kliks-zone
liggen. De drie grootste gratis kansen zijn ongewijzigd: drie termen net buiten
pagina 1 (**vloerverwarming zuidlaren** 9,3 · **installatiebedrijf zuidlaren** 6,5 ·
**vloerverwarming hoogeveen** 10,6) plus één term met massale latente vraag,
**vloerverwarming drenthe** (82 impr @ 66, versnipperd over 4 URL's, nog steeds
géén dedicated pagina). Daarbovenop twee structurele lekken die los staan van
content: een **www-/non-www ranking-splitsing** op de homepage en een **CTR-/
snippet-probleem** waarbij top-3-posities (installateur/elektricien zuidlaren) 0
clicks opleveren. De prijsindicatie-wizard bestaat al en is de sterkste
conversiepagina (44% entry-conversie, bounce 0,32) — de kans zit in **méér
verkeer ernaartoe sturen**, niet in nieuwbouw.

## Top zoekwoorden (uit echte GSC-data, geen geschat extern volume)

| Zoekwoord | Impressies (28d) | Positie | Concurrentie* | Pagina nodig |
|-----------|------------------|---------|---------------|--------------|
| vloerverwarming drenthe | 82 | 65,7 | midden | **nieuw** (`vloerverwarming-drenthe.html`) |
| vloerverwarming zuidlaren | 33 | 9,3 | laag | bestaand (cannibalisatie oplossen) |
| installatiebedrijf zuidlaren | 20 | 6,5 | laag | bestaand (`index.html` blok) |
| vloerverwarming friesland | 10 | 87,7 | midden | bestaand (Leeuwarden-pagina versterken) |
| vloerverwarming schoonebeek | 10 | 61,5 | laag | bestaand (Emmen-hub) |
| installateur zuidlaren | 9 | 3,7 | laag | bestaand — **CTR-fix** (top-3, 0 clicks) |
| vloerverwarming hoogeveen | 8 | 10,6 | laag | bestaand (interne links + FAQ) |
| vloerverwarming leeuwarden | 7 | 27,3 | midden | bestaand (Leeuwarden-pagina) |
| vloerverwarming heerenveen | 5 | 50,4 | midden | bestaand (Drachten/Heerenveen-pagina) |
| elektricien zuidlaren | 5 | 2,2 | laag | bestaand — **CTR-fix** (top-3, 0 clicks) |

\* Concurrentie-inschatting is **indicatief** op basis van termtype (lokale
dienst + plaatsnaam = doorgaans laag/midden); **niet** geverifieerd met een live
keyword-tool deze ronde (WebSearch geblokkeerd). Validatie staat als escalatie.

**Patroon dat de data toont:** zodra een term in de top 3 staat blijven clicks
alsnog uit (installateur 3,7 / elektricien 2,2 / vloerverwarming laren 3,0 → alle
0 clicks), behalve **warmtepomp zuidlaren** (pos 1,8 → 25% CTR, 1 click). Dat ene
klikkende geval bewijst dat de **snippet (title + meta)** het verschil maakt, niet
alleen de positie. Een CTR-/snippet-herschrijving op home + zuidlaren-cluster is
daarmee net zo waardevol als positiewinst.

## Content gaps (ontbrekende of zwakke pagina's)

- **`vloerverwarming-drenthe.html` (ontbreekt volledig).** Grootste regioterm op
  impressies (82) zonder kanonieke pagina; signaal lekt nu weg over home (57),
  prijsindicatie (49), diensten (13), faq (4). Dit is de enige content-gap die een
  écht nieuwe pagina rechtvaardigt. Doelgroep: heel werkgebied. Onderbouwing: de
  versnippering verklaart de diepe positie (Google weet niet welke URL te tonen).
- **Friesland-dekking is zwak.** "vloerverwarming friesland" 87,7, "heerenveen"
  50,4, "bolsward" 70,5 — ondanks bestaande Leeuwarden- en Drachten-pagina's. Geen
  nieuwe pagina nodig; wél interne links + een Friesland-sectie/anker op de
  bestaande pagina's met exacte ankertekst.
- **Emmen-omgeving (Zuidoost-Drenthe) onderbenut.** "vloerverwarming schoonebeek"
  (10 @ 61,5) en "vloerverwarming elim" (4) hangen bij home/Hoogeveen i.p.v. de
  Emmen-pagina. Subdorpen aanhaken op `vloerverwarming-emmen.html`.
- **Géén nieuwe doelgroep-/dienstpagina's nodig deze ronde.** Aparte pagina's voor
  "alleen schuimbeton" of "aannemers/projectontwikkelaars" tonen **geen** vraag in
  de huidige GSC-data; niet bouwen zonder bewijs van zoekvolume (escalatie:
  keyword-tool). De prijsindicatie-, FAQ-, systemen- en werkwijze-pagina's dekken
  de bestaande intentie al.

## Concurrentie-observaties

Geen verse SERP-scan deze ronde (WebSearch geblokkeerd). Wat de **eigen** GSC-data
indirect laat zien over het speelveld:

- Op hyperlokale termen (zuidlaren, fluitenberg, laren) staat VLWarmte al hoog —
  de lokale concurrentie op exacte dorps-/stadcombinaties is **dun**; dat is precies
  waarom kleine on-page-ingrepen hier zoveel opleveren.
- Op de bredere provincieterm (**vloerverwarming drenthe**) staat de site diep
  (pos 66) — daar staan landelijke spelers/portals/aggregators sterker, en wint de
  partij met één duidelijke, intern goed gelinkte provinciepagina. Dat is de te
  veroveren ruimte.
- **Te valideren (escalatie):** wie rankt nu top-5 op "vloerverwarming drenthe" en
  "vloerverwarming friesland", en met wat voor pagina (provinciehub vs. portal)?
  Dit bepaalt of een dedicated Drenthe-pagina top-10 haalbaar is of dat het een
  portal-gedomineerde SERP is.

## Prijscalculator — haalbaarheidsonderzoek (geactualiseerd: tool bestaat al)

### Conclusie
**Niet opnieuw bouwen — de calculator/wizard staat al live op
`prijsindicatie.html` en is de best converterende pagina van de site.** De
opdracht uit het commando ("onderzoek of een prijscalculator een goed idee is")
is door de praktijk ingehaald: er is een meerstaps-wizard (`#wizard`, stappen
product → … met `wizard_start` / `calculator_result` / `wizard_lead_submit`
events, zie GA4-conversieconfig). De juiste vraag is nu **optimalisatie en
instroom**, niet nieuwbouw.

### Onderbouwing (eigen data)
- Prijsindicatie als entry page: **~44% conversie** (9 sessies → 4 conv), bounce
  **0,32**, sessieduur 100–132s. Veruit de hoogste kwaliteit van alle pagina's.
- Maar: krijgt **te weinig instroom** (slechts 9 entry-sessies vs. home 115). De
  hefboom zit in méér verkeer hierheen leiden, niet in de tool zelf.
- GA4 key events zijn correct ingericht op `wizard_lead_submit` + `contact_submit`
  als leads; funnel-events meten engagement (skill §A, regel 4). De meetkant is op
  orde.

### Optimalisatie i.p.v. nieuwbouw
1. **Instroom verhogen:** Ads vaker naar prijsindicatie laten landen i.p.v. home
   (zie Ads-escalatie); interne CTA "richtbedrag in 2 minuten" boven de vouw op
   home + stadspagina's.
2. **Stap-drop-off meten:** als de funnel-events (`wizard_start` →
   `calculator_result` → `wizard_lead_submit`) per stap worden uitgelezen, wijst
   dat de zwakste stap aan. Vervolgvraag voor Analytics.
3. **E-mail/lead-koppeling:** de wizard vraagt al om contact bij submit
   (`wizard_lead_submit`); houd het richtbedrag expliciet **vrijblijvend en excl.
   btw** (staat al in sitelink-copy) om bindendheid te vermijden.

### Risico's en aandachtspunten
Bestaande implementatie dekt dit grotendeels af (vrijblijvendheid, btw-vermelding).
Aandachtspunt blijft: een richtbedrag mag niet als offerte ogen — bewaak de
disclaimer-tekst bij elke copy-wijziging.

### Aanbeveling aan Product Manager
- Prioriteit: **Midden** (tool bestaat; optimaliseren, niet bouwen).
- Ontwikkeltijd: 0 voor nieuwbouw; ~2–4u voor instroom-CTA's + funnel-drop-off-
  rapport (Analytics).
- Verwacht effect op leads: meer entry-sessies op de 44%-pagina = directe leadwinst
  bij gelijk budget.

## Google Ads — advies (ESCALATIE: geen verificatie/mutatie deze ronde)

Scripts geblokkeerd in deze mode. Onderstaande staat klaar voor een sessie met
Ads-permissies (of handmatig). Onderbouwing uit data ongewijzigd sinds 15 jun:
GA4-geo toont **44 sessies buiten kerngebied** (North Holland 25 + South Holland
11 + Brabant 8) — bijna evenveel als Drenthe (33). Live campagne "VLW-API-Leads NL
auto" (id 23834672782, EUR 2/dag) draait landelijk, terwijl de geo-defaults wél
Drenthe/Groningen/Friesland zijn → vermoedelijk budgetlek.

**Stap 0 — verifiëren (read-only):**
```
python scripts/google_ads_list_campaigns.py
```
Bevestig id, status (ENABLED?), kanaaltype en of de geo al is aangescherpt.

**Aanbeveling 1 — geo aanscherpen naar kerngebied** (stopt budgetlek):
```
python scripts/google_ads_update_campaign_geo.py --campaign-id 23834672782 --dry-run
python scripts/google_ads_update_campaign_geo.py --campaign-id 23834672782 --apply
```

**Aanbeveling 2 — landing richting prijsindicatie sturen.** GA4 toont prijsindicatie
44% conv vs. home 23%. De final_urls in defaults zijn al beperkt tot
offerte-deeplink + prijsindicatie (goed); overweeg in de live RSA de
prijsindicatie als **primaire** landing voor de research-intentie-adgroep. RSA in
Ads UI handmatig syncen (geen update-script).

**Aanbeveling 3 — verkeersdaling verifiëren.** Sessies vielen ~90% terug sinds de
piek (27 apr 172 → 1 jun 16). Check of dit bewust lager budget is of zomerseizoen
(vloerverwarming is winterproduct). Bij EUR 2/dag is dat plausibel budgetgedreven.

**Niet doen zonder expliciete spend-goedkeuring:** budget verhogen of `--go-live`.
Huidig dagbudget EUR 2 respecteren. Geen tokens/secrets in output.

## Aanbevelingen voor de Product Manager (geprioriteerd, max 8)

1. **(SEO/Dev — <2u, Hoog) Zuidlaren-cannibalisatie afmaken/verifiëren.** Type:
   Content update + interne links. Onderbouwing: 33 impr @ 9,3, thuisbasis,
   signaal versnipperd over 5+ URL's (home 6,6 / diensten 16,6 / prijsindicatie
   19,4). Actie: exacte ankertekst "vloerverwarming Zuidlaren" naar de dedicated
   pagina vanuit home/diensten/prijsindicatie; controleer of de vorige sprinttaak
   (cyclus 17) al live staat in GSC bij de volgende fetch.
2. **(SEO/Dev — 0,5–1 dag, Hoog) Dedicated `vloerverwarming-drenthe.html`.** Type:
   Nieuwe pagina. Onderbouwing: 82 impr @ 66, grootste regioterm, geen kanonieke
   pagina, signaal lekt over 4 URL's. Actie: nieuwe pagina naar model stadspagina's
   (`Service` + `areaServed="Drenthe"`, canonical), interne links van/naar alle
   stadspagina's; zet `#drenthe-hub` op home om naar een teaser die hierheen linkt
   (voorkomt nieuwe cannibalisatie). Hoogste plafond, structurele gratis leadbron.
3. **(SEO/Dev — <1u, Hoog) CTR-/snippet-fix top-3-termen.** Type: SEO (title/meta).
   Onderbouwing: installateur (3,7), elektricien (2,2), laren (3,0) staan top-3 met
   0 clicks; warmtepomp zuidlaren (1,8) haalt mét goede snippet 25% CTR. Actie:
   title + meta van home + `vloerverwarming-zuidlaren.html` herschrijven zodat de
   SERP-snippet uitnodigt tot klikken (USP + plaats + CTA). Gratis verkeer
   ontsluiten dat nu blijft liggen.
4. **(SEO/Dev — <1u, Hoog) www-/non-www ranking-splitsing laten controleren.**
   Type: Technische SEO. Onderbouwing: GSC toont `vlwarmte.nl/` op pos 5,6 én
   `www.vlwarmte.nl/` op pos 52,8 voor dezelfde homepage — ranking-signalen worden
   verdund. Actie: canonical/redirect naar één hostvariant verifiëren (301 non-www
   → www of andersom, consistent met canonical-tags). Mogelijk de grootste
   onzichtbare hefboom: één homepage die op 5,6 staat i.p.v. gesplitst.
5. **(CRO/Dev — 2–4u, Midden) Meer instroom naar prijsindicatie + home-bounce.**
   Type: CTA/conversie. Onderbouwing: prijsindicatie 44% conv maar 9 entry-sessies;
   home 67% bounce op 115 entry-sessies. Actie: prominente "richtbedrag in 2
   minuten"-CTA boven de vouw op home en stadspagina's die naar de wizard linkt.
6. **(SEO/Dev — <1u, Midden) Friesland- en Emmen-subdorpen aanhaken.** Type:
   Content update + interne links. Onderbouwing: friesland 87,7 / heerenveen 50,4 /
   schoonebeek 61,5 hangen bij verkeerde URL's. Actie: exacte ankertekst-links naar
   `vloerverwarming-leeuwarden.html` (Friesland) en `vloerverwarming-emmen.html`
   (Schoonebeek/Elim) vanuit zuster- en hubpagina's.
7. **(Ads/Escalatie — <30min, Hoog zodra permissies) Geo aanscherpen + status
   checken.** Type: Ads. Onderbouwing: 44 sessies buiten kerngebied bij EUR 2/dag.
   Actie: `list_campaigns` → `update_campaign_geo` (commando's hierboven). Vraagt
   een sessie met Ads-permissies; niet uit te voeren in deze mode.
8. **(Proces — Hoog) GA4-fetch + WebSearch/Ads-permissies herstellen.** Type:
   Infra. Onderbouwing: deze cyclus kon geen verse GA4, geen webonderzoek en geen
   live Ads-state ophalen (Python-versie + don't-ask-mode). Actie: venv-runner
   (3.10+) whitelisten voor `ga4_fetch.py`, en een Ads-/research-sessie met
   netwerk- en script-permissies inplannen zodat zoekvolumes, concurrent-SERP's en
   live campagnestatus geverifieerd worden.

---

### Samenvatting voor de Product Manager (max 5 regels)
- **Modus:** autonoom, WebSearch + Ads-scripts geblokkeerd → analyse op echte
  repo-data; verse zoekvolumes, concurrent-SERP's en live Ads-state staan als
  escalatie met klaargezette commando's.
- **Grootste gratis kansen (ongewijzigd):** drie termen net buiten pagina 1
  (zuidlaren 9,3 / installatiebedrijf 6,5 / hoogeveen 10,6) + de dedicated
  `vloerverwarming-drenthe.html` voor de term met de meeste latente vraag (82 impr).
- **Twee nieuwe technische hefbomen:** CTR-/snippet-fix (top-3-termen halen 0 clicks)
  en de **www-/non-www ranking-splitsing** op de homepage (5,6 vs 52,8) — beide
  klein werk, mogelijk groot effect, los van content.
- **Prijscalculator-vraag is achterhaald:** de wizard bestaat al en is de
  44%-conversiepagina; focus op méér instroom (Ads + CTA) i.p.v. nieuwbouw.
- **Ads:** vermoedelijk budgetlek (44 sessies buiten kerngebied bij EUR 2/dag) +
  ~90% verkeersdaling sinds de piek — geo aanscherpen en status checken zodra een
  sessie met Ads-permissies draait; budget niet verhogen zonder goedkeuring.
