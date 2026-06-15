# Analytics Rapport — 15 juni 2026

**Periode GA4:** 30 dagen (verkeer/conversies), momentopname 8 jun 2026
**Periode GSC:** 25 apr – 22 mei 2026 (28 dagen), opgehaald 23 mei 2026
**Focus:** leadgeneratie voor vloerverwarming in Noord-Nederland

---

## Datawaarschuwing (lees dit eerst)

De cijfers in dit rapport zijn **verouderd** en deze cyclus **niet ververst**:

- **GA4-data is van 8 juni** (ruim een week oud). De fetch kon niet draaien: de systeem-Python is 3.9, het script `scripts/ga4_fetch.py` vereist 3.10+, en de venv-runner mag niet worden gestart in deze autonome modus. De getoonde 30-daagse cijfers lopen dus feitelijk t/m begin juni.
- **GSC-data is van 23 mei** (bijna vier weken oud) en dekt 25 apr – 22 mei. Posities en impressies kunnen inmiddels verschoven zijn.
- De twee bronnen dekken **niet exact dezelfde periode**. Vergelijk kanalen en SEO niet één-op-één.

Behandel alle conclusies als richting, niet als harde actuele stand. Eerste prioriteit voor de volgende cyclus: GA4-fetch weer werkend krijgen (Python 3.10+ in een toegestane venv).

---

## Kerncijfers (30d, per 8 jun)

| Metric                     | Waarde            | Opmerking                                    |
| -------------------------- | ----------------- | -------------------------------------------- |
| Sessies (30d)              | ~149 (top-bronnen)| desktop 72 / mobile 59 / tablet 18           |
| Conversies (30d)           | 35 totaal         | google/cpc 22 + direct 13                    |
| Gem. sessieduur home       | 47,6 sec          | matig — bezoeker overtuigt nog te traag      |
| Bounce home                | 67%               | net onder de zorggrens van 70%               |
| Bounce prijsindicatie      | 32%               | sterk — dit is de werkpaardpagina            |

Conversie-aandeel: **google/cpc + direct samen ~100% van de leads**. Organic search en social leveren in deze periode **0 conversies**.

---

## Belangrijkste bevindingen (leadgeneratie)

- **Google Ads is de motor.** google/cpc = 85 sessies en **22 conversies** — verreweg de grootste leadbron. Stopt of zakt dit kanaal, dan zakt de leadstroom mee.
- **Direct verkeer converteert opvallend goed:** 42 sessies, **13 conversies** (~31% conversieratio). Dit is deels merkbekendheid, deels waarschijnlijk Ads-bezoekers die later direct terugkomen. Een betrouwbare tweede leadbron.
- **Organisch levert nul leads.** 9 organic sessies, 0 conversies. Veel SEO-impressies (zie GSC), maar posities te laag om klikken — laat staan leads — op te leveren. Onbenut potentieel.
- **Prijsindicatie is de sterkste conversiepagina.** Lange sessieduur (100 sec, op 90d zelfs 132 sec), lage bounce (32%), 4 conversies als entry page. Bezoekers die hier landen, doen iets.
- **Home draagt het leeuwendeel van de leads** (27 conversies als entry page) maar verliest met 67% bounce twee op de drie bezoekers direct. Grootste hefboom zit hier.
- **Sterke verkeersdaling eind mei/juni** (zie aparte sectie) — signaal dat de leadmotor terugloopt.

---

## Conversie-analyse: wat levert leads, wat lekt

**Levert leads:**

| Kanaal / pagina        | Sessies | Conversies | Ratio   | Oordeel                         |
| ---------------------- | ------- | ---------- | ------- | ------------------------------- |
| google / cpc           | 85      | 22         | ~26%    | Hoofdmotor                      |
| direct / (none)        | 42      | 13         | ~31%    | Sterke tweede bron              |
| Home als entry page    | 115     | 27         | ~23%    | Volume-leverancier              |
| Prijsindicatie (entry) | 9       | 4          | ~44%    | Hoogste kwaliteit, te weinig volume |
| Werkwijze (entry)      | 2       | 4          | zeer hoog| Klein maar overtuigt sterk     |

**Lekt:**

- **Home bounce 67%.** Veruit het grootste lek in absolute aantallen: van 115 entry-sessies vertrekken er ~78 zonder actie. Eén procentpunt minder bounce hier weegt zwaarder dan welke optimalisatie elders ook.
- **Organic search: 9 sessies, 0 conversies.** Het verkeer dat binnenkomt is of te koud, of landt op de verkeerde pagina.
- **Prijsindicatie krijgt te weinig instroom** (9 entry-sessies) terwijl het de beste ratio heeft. Meer bezoekers naar deze pagina sturen = meer leads bij gelijke moeite.
- **Werkwijze** converteert uitstekend maar trekt amper 2 entry-sessies — onzichtbaar in de funnel.

**Voor de Marketing Research Agent:** google/cpc draagt de leadgeneratie. Aanbevolen vervolgvragen: (1) welke campagnes/zoektermen leveren die 22 conversies, (2) landen Ads-klikken op home of op prijsindicatie — gezien de veel hogere ratio van prijsindicatie kan landingsafstemming richting prijsindicatie/werkwijze de cost-per-lead verlagen, (3) zie geo-sectie over mogelijke verspilling. Koppelstappen: `.cursor/skills/google-ads-marketing/SKILL.md`, sectie GA4 ↔ Ads.

---

## SEO-bevindingen uit GSC

CTR is **vrijwel overal 0**: veel impressies, posities te laag om geklikt te worden. De site is zichtbaar maar staat op de verkeerde plek. Concreet:

### Bijna-pagina-1 kansen (laaghangend fruit — kleine zet, groot effect)

| Zoekterm                     | Impressies | Positie | Kans                                            |
| ---------------------------- | ---------- | ------- | ----------------------------------------------- |
| installatiebedrijf zuidlaren | 20         | 6,5     | Al op pagina 1, net niet in de kliks-zone. Push naar top 3. |
| vloerverwarming zuidlaren    | 33         | 9,3     | Thuisbasis, randje pagina 1. Hoogste prioriteit — meeste impressies binnen bereik. |
| vloerverwarming hoogeveen    | 8          | 10,6    | Eigen pagina bestaat al, staat net op pagina 2. Klein duwtje = pagina 1. |
| installateur zuidlaren       | 9          | 3,7     | Bijna top 3, maar 0 clicks — title/meta CTR-probleem. |
| elektricien zuidlaren        | 5          | 2,2     | Top 3, 0 clicks. CTR-lek (title/meta).          |
| warmtepomp zuidlaren         | 4          | 1,8     | Positie 1-2, levert wél 1 click (25% CTR) — bewijs dat top-posities hier wél klikken opleveren. |

**Patroon:** zodra een term in de top 3 staat, blijven klikken alsnog uit op alle termen behalve warmtepomp zuidlaren. Dat wijst op een **CTR-/snippet-probleem** (title + meta description) bovenop het positieprobleem. Markeer als **CTA-/snippet-kans**: title en meta van home + zuidlaren-pagina herschrijven zodat ze in de SERP uitnodigen tot klikken.

### Grote zwakte (kerngebied-term presteert ondermaats)

- **"vloerverwarming drenthe": 82 impressies @ positie 65,7 — 0 clicks.** Dit is een **kernterm voor het hele werkgebied** met de meeste impressies van alle queries, maar de positie is dramatisch (pagina 6-7). Dieper in de data blijkt waarom: de term landt **versnipperd** over meerdere pagina's — home (57 impr @ 63,4), prijsindicatie (49 @ 71,1), diensten (13 @ 77,2), faq (4 @ 68,8). Er is **geen sterke kanonieke "vloerverwarming Drenthe"-pagina**; Google weet niet welke pagina te tonen. Markeer als **grootste SEO-kans van deze sprint**: één duidelijke Drenthe-landingspagina (of home stevig optimaliseren op deze term) en interne links erheen bundelen.
- **"vloerverwarming friesland": 10 impr @ 87,7** — zeer slecht, ondanks bestaande Leeuwarden-pagina. Friesland-dekking is zwak.
- **www vs non-www versnippering:** GSC toont losse rijen voor `vlwarmte.nl/` (positie 5,6) én `www.vlwarmte.nl/` (positie 52,8) voor dezelfde homepage. De www-variant rankt veel slechter. Mogelijk canonical-/redirect-probleem dat ranking-signalen verdunt — waard om te laten controleren.

---

## Mogelijke Ads-geo-verspilling (hypothese)

**North Holland: 25 sessies — de op-één-na-grootste regio, buiten het kerngebied.** Het bedrijf werkt vanuit Zuidlaren met focus op Drenthe, Groningen, Friesland (en deel Overijssel). North Holland (25), South Holland (11) en North Brabant (8) zijn samen **44 sessies buiten de doelregio** — bijna evenveel als Drenthe (33) zelf.

**Hypothese:** Google Ads serveert (deels) buiten het kerngebied, of de geo-targeting staat op heel NL. Dat zou betekenen dat budget wegloopt naar bezoekers die nooit klant worden (te ver weg voor uitvoering). Te verifiëren door de Marketing Research Agent: staat de campagne-geo strak op Noord-NL? Zo niet, dan is hier waarschijnlijk cost-per-lead te winnen. **Signaal, geen bewijs** — het kan ook organisch of via gedeelde links binnenkomen.

---

## Verkeersdaling (signaal)

Wekelijkse sessies lopen sterk terug:

| Week (start) | Sessies |
| ------------ | ------- |
| 27 apr       | 172     |
| 4 mei        | 75      |
| 11 mei       | 49      |
| 18 mei       | 56      |
| 25 mei       | 15      |
| 1 jun        | 16      |

Van 172 naar ~15-16 per week — een daling van ruim 90% sinds de piek. De piek van 27 apr was waarschijnlijk een campagne-uitschieter.

**Plausibele oorzaken (niet bevestigd):**

1. **Ads-budget verlaagd of campagne gepauzeerd** — meest waarschijnlijk, want google/cpc is de hoofdmotor en de daling is abrupt. Eerst checken.
2. **Seizoen** — vloerverwarming is een winterproduct; richting de zomer (juni) zakt de zoekvraag natuurlijk. Verklaart een geleidelijke daling, niet de scherpe knik.
3. **Combinatie:** lager Ads-budget bovenop dalende zomervraag.

Actie: laat de Marketing Research Agent het Ads-budget/-status van eind mei controleren. Als budget bewust verlaagd is, is de daling verklaard; zo niet, dan loopt er mogelijk iets mis.

---

## Aanbevelingen voor deze sprint (max 5)

**1. Kanonieke "vloerverwarming Drenthe"-pagina opzetten + interne links bundelen** — SEO-kans
- Data: 82 impressies @ positie 65,7, versnipperd over 4 pagina's, 0 clicks. Grootste kernterm zonder sterke pagina.
- Verwacht effect: van pagina 6-7 naar pagina 2-3 haalbaar bij gebundelde signalen; bij doorzetten richting pagina 1 een structurele organische leadbron in het hele werkgebied. Geschat: enkele extra organische leads/maand op termijn.

**2. Title + meta van home en zuidlaren-pagina's herschrijven voor CTR** — CTA-/snippet-kans
- Data: installateur zuidlaren (3,7), elektricien zuidlaren (2,2) staan in top 3 maar leveren 0 clicks; warmtepomp zuidlaren (1,8) levert mét goede snippet 25% CTR. Bewijs dat snippet het verschil maakt.
- Verwacht effect: bestaande top-3-posities omzetten in klikken. Bij ~50 impressies op deze termen en zelfs 10% CTR = enkele extra bezoekers/week uit gratis verkeer.

**3. Meer Ads-verkeer naar prijsindicatie sturen i.p.v. alleen home** — CTA-/conversiekans
- Data: prijsindicatie entry-conversie ~44% vs home ~23%; prijsindicatie krijgt maar 9 entry-sessies. Bounce 32% vs 67%.
- Verwacht effect: bij gelijk Ads-budget meer leads, want hogere conversieratio. Te coördineren met Marketing Research Agent (landingsafstemming).

**4. Home-bounce van 67% terugdringen** — CTA-kans
- Data: home is grootste entry page (115 sessies) met 67% bounce; ~78 bezoekers vertrekken zonder actie. Sessieduur slechts 47 sec.
- Verwacht effect: elk procentpunt bounce minder = ~1 extra bezoeker die doorklikt. Sterkere boven-de-vouw CTA / prijsindicatie-knop direct in beeld kan enkele extra leads/maand opleveren.

**5. Ads-geo strak op Noord-NL laten zetten** — efficiëntiekans
- Data: 44 sessies (North Holland 25 + South Holland 11 + Brabant 8) buiten kerngebied, vrijwel evenveel als Drenthe (33).
- Verwacht effect: geen directe leadgroei, maar lagere cost-per-lead — budget verschuift naar bezoekers die wél klant kunnen worden. Eerst verifiëren of dit Ads of organisch is (Marketing Research Agent).

---

## Samenvatting voor Product Manager (max 5 regels)

1. **Datawaarschuwing:** GA4 van 8 jun, GSC van 23 mei — niet ververst (Python 3.9 vs vereist 3.10+); behandel als richting, fix de fetch volgende cyclus.
2. **Leadmotor = Google Ads (22 conv) + direct (13 conv); organisch levert 0 leads** ondanks veel SEO-impressies op te lage posities.
3. **Grootste SEO-kans:** "vloerverwarming drenthe" (82 impr @ 65,7, versnipperd over 4 pagina's) → één kanonieke pagina; plus title/meta-CTR-fix voor zuidlaren-termen die wél top-3 staan.
4. **Verkeer daalt ruim 90% sinds piek 27 apr** — waarschijnlijk lager Ads-budget en/of zomerseizoen; laat Marketing Research Agent Ads-status checken.
5. **Mogelijke Ads-geo-verspilling** (44 sessies buiten Noord-NL) — signaal, te verifiëren; en stuur Ads liever naar prijsindicatie (44% conv) dan alleen home (23%).
