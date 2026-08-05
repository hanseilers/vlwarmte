# Analytics Rapport — 5 augustus 2026 (cyclus 24)

**Periode:** 30 dagen tot 5 aug 2026 (GA4 property `properties/534641753`, opgehaald 5 aug 11:06)
**Vorige sprint effect:** Cyclus 23 (FAQ Assen + Emmen, homepage-meta op doelregio, kruislinks, Hoogeveen-title) staat sinds 20 jul live — nu ~16 dagen meetbaar. **Te vroeg voor harde SEO-conclusies** (GSC blijft blind), maar eerste signalen: `prijsindicatie.html` verdubbelde van 2 naar 4 sessies/30d; de laatste week steeg van 1 naar **6** sessies (29 jul–4 aug). Tegelijkertijd verslechterde de homepage-bounce (75% → **85%**) en verdween Drenthe volledig uit de geo (was 3 sessies). De meta-targeting heeft de verkeerd-publiek-verdeling nog niet zichtbaar verbeterd — of het volume is te laag om het te zien.

## Kerncijfers

| Metric               | Waarde (30d)     | Trend t.o.v. cyclus 23 (20 jul)        |
| -------------------- | ---------------- | -------------------------------------- |
| Sessies              | **17**           | ↓ ~19% (was ~21)                       |
| Actieve gebruikers   | ~17              | ↓                                      |
| Conversies           | **0**            | = 0 (**5e cyclus op rij**)             |
| Bounce homepage `/`  | **85%**          | ↑ (was 75%; boven zorggrens 70%)       |
| Gem. duur `/`        | **~11 s**        | ↑ (was ~5 s; nog steeds laag)          |
| Betaald (google/cpc) | **0 sessies**    | = 0 (nog steeds volledig weg)          |
| Organisch            | **4 sessies**    | ↓ (was 7)                              |
| Direct               | **11 sessies**   | ↓ (was 14)                             |

Grondwaarheid instroom (week-sessies): 7 (10–16 jun) → 3 → 4 → 10 → 2 → 4 → **1** (22–28 jul) → **6** (29 jul–4 aug). De dip naar 1 in de week vóór de laatste meetweek lijkt op een dieptepunt; de herstel naar 6 is een positief teken, maar op dit volume is één week geen trend — pas over 2–3 cycli zeggen of cyclus 23 iets doet.

## Top pagina's (30d)

| Pagina                        | Sessies | Gem. duur | Bounce |
| ----------------------------- | ------- | --------- | ------ |
| `/`                           | 13      | ~11 s     | **85%**|
| `/prijsindicatie.html`        | 4       | **112 s** | 75%    |
| `/contact.html`               | 1       | 50 s      | 0%     |
| `/diensten.html`              | 1       | 15 s      | 0%     |
| `/vloerverwarming-zuidlaren`  | 1       | 3 s       | 0%     |

## Sterkste engagement (90d, richtinggevend)

| Pagina                    | Sessies | Gem. duur |
| ------------------------- | ------- | --------- |
| `/prijsindicatie.html`    | 45      | **135 s** |
| `/werkwijze.html`         | 10      | 239 s     |
| `/systemen-producten.html`| 9       | 223 s     |
| `/contact.html`           | 42      | 58 s      |
| `/`                       | 185     | 46 s      |

## Zwakste pagina's

- **Homepage `/`**: 12 van 17 landingssessies (71%), **85% bounce**, ~11 s duur. Blijft het dominante én slechtst presterende instappunt. De sterkste converter (`prijsindicatie`, 112 s gemiddeld) krijgt nog steeds weinig instroom (4 sessies/30d, 3 als landing met 100% bounce — klein volume).
- **Stadspagina's**: Assen en Emmen (nieuwe FAQ cyclus 23) staan niet in de 30d-top; Assen heeft 1 sessie in 90d (5 s). Te weinig verkeer om het FAQ-effect te meten.
- **Leeuwarden**: 2 sessies/90d, 2,6 s gemiddeld — snelle bounce, geen FAQ-schema.

## Traffic bronnen (30d)

| Bron                     | Sessies | Conversies |
| ------------------------ | ------- | ---------- |
| Direct / (none)          | 11      | 0          |
| Organic google / organic | 4       | 0          |
| Cross-network            | 1       | 0          |
| Unassigned               | 1       | 0          |

**`google/cpc` blijft op 0 sessies** — vijfde cyclus zonder betaald verkeer. Historisch was dit kanaal 100% van alle conversies. **Aanbeveling voor Marketing Research Agent:** campagnestatus, RSA final URL's en GA4↔Ads-koppeling controleren zodra er een interactieve sessie met Ads-rechten is (zie `.cursor/skills/google-ads-marketing/SKILL.md`).

## Landingspagina's

| Landing                          | Sessies | Bounce | Opmerking |
| -------------------------------- | ------- | ------ | --------- |
| `/`                              | 12      | 83%    | 71% van alle instroom |
| `/prijsindicatie.html`           | 3       | 100%   | Kleine steekproef; 90d engagement sterk |
| `/vloerverwarming-zuidlaren.html`| 1       | 0%     | Enige stadspagina als landing |
| `/?ved=…` (Google SERP-variant)  | 1       | 100%   | Organisch verkeer, direct weg |

## Geografie (30d)

| Regio / land              | Sessies |
| ------------------------- | ------- |
| North Holland             | 3       |
| South Holland             | 3       |
| Duitsland (diverse)       | 3       |
| Groningen                 | 1       |
| Afghanistan, Armenië, VAE, VS | elk 1 |
| NL (regio niet ingesteld) | 1       |

**Doelregio (Drenthe + Groningen + Friesland): 1 sessie** (alleen Groningen). Drenthe en Friesland: **0**. North Holland + South Holland + Duitsland samen: **9 van ~15** geo-attribueerbare sessies — nog steeds ruim de meerderheid buiten het werkgebied. Cyclus 23's meta-targeting heeft dit patroon in 16 dagen **niet** zichtbaar verbeterd (Drenthe ging zelfs van 3 naar 0). Dat kan timing zijn, maar het bevestigt dat meta alleen niet genoeg is.

## Devices (30d)

| Device  | Sessies |
| ------- | ------- |
| Desktop | 11 (65%)|
| Mobile  | 4 (24%) |
| Tablet  | 1 (6%)  |

---

## Observaties

1. **Instroom blijft op bodemniveau, maar de laatste week licht omhoog.** 17 sessies/30d (↓19% t.o.v. vorige cyclus). De week 29 jul–4 aug telt 6 sessies — na een dieptepunt van 1. Te vroeg om toe te schrijven aan cyclus 23, maar het is geen verdere daling.
2. **Betaald kanaal blijft dood (0 sessies, 5e cyclus).** Geen `google/cpc` in de bronnen. De enige historische conversiebron is nog steeds uit. Dit is geen developer-taak — escalatie naar eigenaar + Marketing Research Agent.
3. **Homepage lekt harder.** 85% bounce (was 75%), nog steeds ~71% van alle landings. Gemiddelde duur steeg licht (5 → 11 s), maar dat is nog ver onder de 30s-drempel. Verkeerd publiek (geo) blijft de waarschijnlijkste verklaring naast het lage volume.
4. **0 conversies, 5e cyclus — meetfout blijft waarschijnlijker dan lege trechter.** `prijsindicatie` toont 112 s gemiddelde duur/30d en 135 s/90d — mensen blijven hangen. Custom lead-events tellen alleen als conversie na key-event-markering in GA4 Admin. Nog steeds niet door de eigenaar geverifieerd.
5. **GSC feitelijk niet gekoppeld (8+ weken).** OAuth `invalid_grant` bij fetch van 5 aug; placeholder `REPLACE_WITH_TOKEN` op 19 pagina's. Zonder GSC kunnen we het SEO-effect van cyclus 17–23 niet meten en blijft de mid-juni-cliff (week 10–16 jun: 7 sessies, daarna 3) giswerk.
6. **`prijsindicatie` groeit relatief.** Van 2 naar 4 sessies/30d — de enige pagina met duidelijke instroomstijging. Past bij de 90d-data (45 sessies, 135 s). De meetklok van cyclus 20/21 (~27 jul) is verstreken; deze pagina mag weer als hefboom worden overwogen.
7. **Cyclus 23 SEO-ingrepen nog niet meetbaar in verkeer.** Assen/Emmen-FAQ, kruislinks en Hoogeveen-title leveren geen zichtbaar verkeer op in 30d. Dat is normaal bij dit volume — pas met GSC impressies/posities wordt het zichtbaar.

## Voorstellen voor Product Manager

Rode draad: de trechter is bijna leeg, we sturen nog steeds blind (GSC uit, meter mogelijk kapot, betaald dood). De hoogste hefboom blijft het **hard beleggen van meet- en koppelblokkades**. On-page: meetklok cyclus 20/21 is verstreken — `prijsindicatie` en de rijpere stadspagina's mogen weer als hefboom. SEO-cadans: volgende FAQ-kandidaat Leeuwarden.

### Voorstel 1 — Escaleer (5e keer) de conversie-meting bij de eigenaar
- **Prioriteit:** Hoog
- **Onderbouwing:** 5 cycli 0 conversies over álle kanalen. `prijsindicatie` toont 112 s/30d en 135 s/90d gemiddelde duur — intens engagement zonder één lead-event in GA4 past beter bij een ongemarkeerde meter dan bij een lege trechter. Lead-events (`wizard_lead_submit`, `lead_form_submit`, `contact_submit`) staan in de code maar tellen alleen als conversie na key-event-markering.
- **Actie (eigenaar, niet autonoom):** (a) Formspree-inboxen `xzdojzdk` + `xgodnvoq` controleren — komen er aanvragen binnen? (b) GA4 → Admin → Events: `wizard_lead_submit` / `lead_form_submit` / `contact_submit` als **key event** markeren. ~10 minuten.
- **Verwacht effect:** duidelijkheid of "0 conversie" echt is of een meetartefact. Bepaalt of we op conversie of instroom sturen.

### Voorstel 2 — Herstel GSC-koppeling: OAuth vernieuwen én placeholder-token vervangen
- **Prioriteit:** Hoog
- **Onderbouwing:** GSC-fetch faalt opnieuw met `invalid_grant` (8+ weken). Alle 19 hoofdpagina's dragen nog `REPLACE_WITH_TOKEN`. Zonder GSC kunnen we het effect van cyclus 17–23 (FAQ, breadcrumbs, meta, kruislinks) niet meten. De mid-juni-cliff (7→3 sessies/week) blijft onbevestigd.
- **Actie (eigenaar, niet autonoom):** (a) `python scripts/gsc_get_refresh_token.py` met verified owner-account. (b) Echt site-verificatietoken leveren zodat `REPLACE_WITH_TOKEN` site-breed vervangen kan worden.
- **Verwacht effect:** verse GSC-data → onderbouwde instroomdiagnose; FAQ/rich-result-effect meetbaar over ~4 weken.

### Voorstel 3 — Betaald kanaal: serveerstatus + landing herstellen (cpc = 0, 5e cyclus)
- **Prioriteit:** Hoog
- **Onderbouwing:** `google/cpc` blijft op 0 sessies — vijfde cyclus. Historisch 100% van alle conversies. Geen normale werking.
- **Actie (eigenaar + Marketing Research Agent):** campagnestatus/afkeuringen checken (`google_ads_list_campaigns.py`); RSA final URL's op converterende landings (koop → `prijsindicatie.html`, offerte → `contact.html?modus=offerte#aanvraag`); budget pas ná fixes + spend-goedkeuring. GA4↔Ads-koppeling controleren.
- **Verwacht effect:** herstel van de enige bewezen conversiebron; meetbaar zodra voorstel 1 de meter valideert.

### Voorstel 4 — `prijsindicatie.html` als instroom-asset versterken (meetklok verstreken)
- **Prioriteit:** Midden
- **Onderbouwing:** Enige pagina met instroomstijging (2→4 sessies/30d) en sterkste engagement (112 s/30d, 135 s/90d). Meetklok cyclus 20/21 (~27 jul) is verstreken. Als landing heeft `prijsindicatie` 100% bounce op 3 sessies — klein volume, maar het patroon (sterk engagement als mensen blijven, hoge bounce als landing) wijst op een ATF/message-match-probleem voor nieuwe bezoekers.
- **Actie:** Additief kosten-verankeringsblok boven de wizard (korte uitleg + interne links naar `systemen-producten.html#laagopbouw` en relevante stadspagina's); geen wizard-flow herschrijven. Optioneel: `FAQPage`- of `HowTo`-schema rond de kosten-uitleg.
- **Verwacht effect:** lagere landing-bounce op `prijsindicatie`; meer `wizard_start`-events. Meetbaar in GA4 over 4 weken.

### Voorstel 5 — FAQ-sjabloon uitrollen naar `vloerverwarming-leeuwarden.html`
- **Prioriteit:** Midden
- **Onderbouwing:** Volgende kandidaat in de afgesproken cadans (cyclus 23 deed Assen + Emmen; `[WACHT]` noemde Leeuwarden als volgende). Leeuwarden heeft 2 sessies/90d met 2,6 s gemiddeld — snelle bounce, geen FAQ-schema. Friesland staat op 0 sessies/30d in geo; dit is de enige Friese stadspagina.
- **Actie:** Hoogeveen/Groningen-patroon: 3 lokaal ingekleurde Q&A's (werkgebied met echte plaatsnamen rond Leeuwarden, kosten → link naar `prijsindicatie.html`, infrezen bestaande dekvloer) + bijbehorend `FAQPage`-JSON-LD. Verzin geen feiten.
- **Verwacht effect:** long-tail-eligibility voor Friese zoekopdrachten; meetbaar in GSC (mits voorstel 2 slaagt) over ~4 weken.

### Voorstel 6 — `BreadcrumbList`-schema op Heerenveen en Drachten
- **Prioriteit:** Midden
- **Onderbouwing:** Enige stadspagina's zonder breadcrumb-schema (grep bevestigt: geen `BreadcrumbList` op `vloerverwarming-heerenveen.html` en `vloerverwarming-drachten.html`). Meetklok cyclus 20/21 is verstreken. Drachten toont 2 sessies/90d met 107 s gemiddeld — engagement is er als mensen landen.
- **Actie:** Voeg `BreadcrumbList`-JSON-LD toe in de `<head>`, conform het patroon op de andere stadspagina's. Geen inhoudelijke wijzigingen.
- **Verwacht effect:** structureel SEO-signaal; onzichtbaar voor bezoeker, geen engagement-risico.

### Voorstel 7 — Homepage: routing naar `prijsindicatie` versterken (niet hero herbouwen)
- **Prioriteit:** Midden
- **Onderbouwing:** 71% van landings op `/`, 85% bounce. `prijsindicatie` is de sterkste pagina (112 s) maar krijgt slechts 24% van het pagina-verkeer. De hero heeft al een primaire CTA naar `prijsindicatie`, maar bezoekers die niet direct klikken hebben geen tweede, lichtere instap.
- **Actie:** Voeg een compact trust/kosten-band toe direct onder de hero (1–2 zinnen + link "Richtbedrag in 2 minuten →") — geen hero-herbouw, geen extra primaire CTA's. Past bij de CTA-dichtheidsregel (één primaire actie in hero, secundaire in de band eronder).
- **Verwacht effect:** meer doorstroom van homepage naar `prijsindicatie`; lagere homepage-bounce. Meetbaar in GA4 navigatie-events over 4 weken.

### Voorstel 8 — Dedicated landingspagina `vloerverwarming-heerenveen.html` evalueren (Marketing Research Agent)
- **Prioriteit:** Midden
- **Onderbouwing:** Ads-keyword `vloerverwarming heerenveen` heeft geen dedicated page (AGENTS.md SEO-gap). Heerenveen-pagina bestaat maar heeft 0 sessies/30d. Drachten (2 sessies/90d) presteert beter qua engagement.
- **Actie:** Marketing Research Agent: keyword-volume en concurrentie checken; indien positief, content-audit Heerenveen-pagina (FAQ, lokale plaatsnamen, interne links) als developer-taak voorbereiden.
- **Verwacht effect:** sluit Ads/SEO-gap; meetbaar zodra GSC en Ads weer draaien.

### Voorstel 9 — NIET doen: homepage-hero herbouwen of wizard-flow herschrijven
- **Prioriteit:** (bewuste onthouding)
- **Onderbouwing:** Homepage is de enige pagina met substantieel verkeer; hero-herbouw is hoog risico bij 85% bounce die deels verkeerd-publiek is. Wizard-flow is net uit de maturatieperiode — eerst additieve verbeteringen (voorstel 4), geen structurele herschrijving.
- **Actie:** met rust laten; eerst voorstel 1–3 en 4 meten.

---

## Samenvatting

De trechter blijft bijna leeg (**17 sessies/30d**, ↓19% t.o.v. vorige cyclus) en staat voor de **5e cyclus op rij** op 0 conversies. De laatste week telt 6 sessies — een licht herstel na een dieptepunt van 1, maar op dit volume is dat nog geen trend. Cyclus 23 (FAQ Assen/Emmen, meta-targeting, kruislinks) is te vroeg en te laag-volume om hard te beoordelen; de homepage-bounce verslechterde (85%) en de doelregio kromp in (1 sessie, Drenthe 0). `prijsindicatie` is de enige pagina met instroomstijging en sterk engagement — nu de meetklok verstreken is, mag die weer als hefboom. Prioriteit: meet- en koppelblokkades hard beleggen (conversie-key-events, GSC-OAuth + verificatietoken, Ads-serveerstatus). Autonoom-veilig on-page: `prijsindicatie` versterken (voorstel 4), FAQ Leeuwarden (voorstel 5), breadcrumbs Heerenveen/Drachten (voorstel 6).

**Fetch-status:** GA4 ✅ geslaagd (credentials: `secrets/vlwarmte-ga-service-account.json`). GSC ❌ mislukt (`invalid_grant` — OAuth refresh token verlopen; `python scripts/gsc_get_refresh_token.py` vereist).
