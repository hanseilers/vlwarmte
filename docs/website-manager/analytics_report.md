# Analytics Rapport — 20 juli 2026 (cyclus 23)

**Periode:** 30 dagen tot 20 jul 2026 (GA4 property `properties/534641753`, opgehaald 20 jul 06:02)
**Vorige sprint effect:** Cyclus 22 (SEO-hygiënecyclus: sitemap-lastmod, Groningen-FAQ+schema, breadcrumbs, kruislinks, laatste CTA) staat pas 7 dagen live (13 jul). Onzichtbaar schema + interne links geven per definitie geen engagement-effect; het beoogde crawl-/indexatie-effect is bovendien pas zichtbaar zodra Google herindexeert én GSC weer draait. **Niet** te beoordelen in dit venster. Wat wél zichtbaar is: de instroom zakt verder door (laatste week 3), en er staan opnieuw 0 conversies over alle kanalen — nu de **vierde** cyclus op rij.

## Kerncijfers

| Metric               | Waarde (30d)     | Trend                                  |
| -------------------- | ---------------- | -------------------------------------- |
| Sessies              | ~21              | ↓ ~5% (was ~22 vorige cyclus)          |
| Actieve gebruikers   | ~20              | ↓                                      |
| Conversies           | 0                | = 0 (**4e cyclus op rij**)             |
| Bounce homepage `/`  | 75%              | ↑ (boven zorggrens 70%)                |
| Gem. duur `/`        | ~5 s             | zeer laag                              |
| Betaald (google/cpc) | **0 sessies**    | ↓ (was 1 → nu volledig verdwenen)      |

Grondwaarheid instroom (week-sessies): 15 (25 mei) → 16 → 15 → **1** (15–21 jun) → 5 → 9 → 4 → **3** (13–19 jul). De laatste twee weken (4, 3) bevestigen dat we op bodemniveau blijven hangen — ~7% van het mei-niveau. De scherpe cliff zit in de week van **15–21 jun** (15 → 1): dat is te abrupt voor pure seizoensinvloed en is het eerste signaal dat er mid-juni iets is gebeurd met de instroombron.

## Top pagina's (30d)

| Pagina                        | Sessies | Gem. duur | Bounce |
| ----------------------------- | ------- | --------- | ------ |
| `/` (alle titelvarianten)     | 20      | ~5 s      | ~70%   |
| `/diensten.html`              | 3       | 10 s      | 0%     |
| `/contact.html`               | 2       | 26 s      | 0%     |
| `/prijsindicatie.html`        | 2       | **233 s** | 0%     |
| `/vloerverwarming-zuidlaren`  | 2       | 14 s      | 0%     |
| `/systemen-producten.html`    | 1       | 67 s      | 0%     |

## Sterkste engagement (90d, richtinggevend)

| Pagina                    | Sessies | Gem. duur |
| ------------------------- | ------- | --------- |
| `/prijsindicatie.html`    | 70      | **133 s** |
| `/werkwijze.html`         | 24      | 108 s     |
| `/systemen-producten.html`| 22      | 95 s      |
| `/contact.html`           | 62      | 62 s      |
| `/`                       | 264     | 61 s      |

## Zwakste pagina's

- **Homepage `/`**: 16 van 21 landingssessies (76%), 75% bounce, ~5 s duur. Blijft het grootste én slechtst presterende instappunt. De sterkste pagina van de site (`prijsindicatie.html`, 233 s / 0 bounce) wordt daarachter nauwelijks bereikt (2 sessies/30d).
- **Stadspagina's**: 0–2 sessies elk over 30d. Dunne instroom; niet de bottleneck, maar leveren ook niets op — precies de reden dat cyclus 22 hun vindbaarheid probeerde te repareren.

## Traffic bronnen (30d)

| Bron                     | Sessies | Conversies |
| ------------------------ | ------- | ---------- |
| Direct / (none)          | 14      | 0          |
| Organic google / organic | 7       | 0          |

**`google/cpc` is nu volledig verdwenen** (0 sessies; was 12 → 1 → 0 over drie cycli). Het betaalde kanaal — historisch 100% van álle conversies — is feitelijk dood. Dit verklaart een deel van de instroomterugval én, cruciaal, het wegvallen van de enige bron die ooit conversies leverde.

## Geografie (30d)

North Holland 5, Duitsland (Schleswig-Holstein) 3, Drenthe 3, South Holland 3, (not set) 2, USA 2, Groningen 1, Gelderland 1, NL-onbekend 1. **Kernprobleem blijft:** de doelregio (Drenthe 3 + Groningen 1 + Friesland **0** = 4 van 21) is minderheid. North Holland + Duitsland + South Holland + USA (13 sessies) vallen buiten het werkgebied. Verkeerd publiek op de homepage → dat drukt bounce omhoog en conversie omlaag, los van de pagina-inhoud.

---

## Focusvraag 1 — Wat is de meest waarschijnlijke oorzaak van de instroom-instorting?

Zonder verse GSC (OAuth `invalid_grant`, 6+ weken) blijft dit deels giswerk, maar de vorm van de curve wijst op een **combinatie van drie oorzaken**, in volgorde van waarschijnlijke bijdrage:

1. **Seizoenstrog (structureel, grootste aandeel).** Vloerverwarming is een najaars-/wintervraag. De daling loopt van mei (voorjaarsverbouwingen, 15–56/week) de diepe zomer in (jun–jul). Een groot deel van de terugval is normale seizoensvraag — de zoekvraag naar "vloerverwarming" zakt elke zomer in.
2. **Betaald kanaal volledig weggevallen (bevestigd, meetbaar).** `google/cpc` ging 12 → 1 → **0** sessies. Dat is een harde, zichtbare bron die is verdwenen — geen seizoen, maar een gepauzeerde/afgekeurde campagne. Dit haalt een vaste basislaag verkeer (én de enige conversiebron) onderuit.
3. **Mogelijke organische ranking-/indexatiedip (onbevestigd, verdacht).** De cliff in de week van **15–21 jun** (15 → 1 sessies) is te abrupt en te diep voor seizoen alleen. Dat patroon past bij een indexatie- of ranking-event mid-juni. We kúnnen dit niet bevestigen: GSC is blind, dus impressies/posities/zoektermen zijn onzichtbaar.

**Bijkomend, nieuw geconstateerd bij content-inspectie deze cyclus:** álle 11 hoofdpagina's dragen nog steeds `<meta name="google-site-verification" content="REPLACE_WITH_TOKEN" />` — een **placeholder** in plaats van een echt token. Dit deïndexeert de site niet, maar het betekent dat verificatie via de meta-tag nooit is voltooid, wat de GSC-koppeling verder bemoeilijkt. Het staat los van de OAuth-`invalid_grant`, maar het is hetzelfde onderliggende probleem: **de site is voor Search Console feitelijk niet gekoppeld.** Dit is de kern waarom oorzaak 3 niet te bevestigen is.

**Conclusie:** meest waarschijnlijk seizoenstrog + dood betaald kanaal, met een reëel vermoeden van een organische dip mid-juni die we niet kunnen zien. Zolang GSC blind is, is elke instroom-actie deels een gok — het herstellen van GSC-zicht is daarom de hoogste-waarde-stap, niet nóg een on-page ingreep.

## Focusvraag 2 — Is de 0-conversies een meetfout of een lege trechter?

**Beide zijn mogelijk; het bewijs kantelt richting meetfout, maar is niet sluitend.**

Wat pleit voor **lege trechter:** bij ~21 sessies/30d, waarvan 16 homepage-bounces en slechts 2 op `prijsindicatie` en 2 op `contact`, is het statistisch heel goed mogelijk dat simpelweg niemand een lead heeft ingediend. Bij dit volume is 0 conversies niet vreemd.

Wat pleit voor **meetfout (sterker):**
- De event-code fúnctioneert en is aanwezig. Geverifieerd in de codebase deze cyclus: `prijsindicatie.html` vuurt `wizard_lead_submit` (r.1689) en `lead_form_submit` (r.1695); `assets/js/main.js` vuurt `contact_submit` (r.208). De GA-tag `G-0BB9M7HYSF` laadt via `ga-deferred.js`.
- Dit zijn **custom events**. In GA4 tellen custom events **niet** als conversie tenzij ze in Admin → Events expliciet als **key event** zijn gemarkeerd. Als dat nooit is gedaan, staat de conversiekolom **per definitie op 0**, ongeacht of er leads binnenkomen.
- Over 90 dagen heeft `prijsindicatie.html` 70 sessies met **133 s** gemiddelde duur (en in dit venster één sessie van **233 s**). Dat is intens engagement met een leadformulier. Dat 90+ dagen lang niemand ook maar één lead-event triggert terwijl mensen 2–4 minuten op de calculator zitten, is onwaarschijnlijk — dat past beter bij "de events vuren wél, maar worden niet als conversie geteld".

**Dit is nu de 4e cyclus met deze open vraag en die is nog steeds niet door de eigenaar geverifieerd.** Zolang dat zo is, sturen we blind: we weten niet of de lead-drempelverlaging van cyclus 21 überhaupt meetbaar is. De verificatie is een taak van ~10 minuten (Formspree-inboxen + GA4 key-event-vinkje) met grote impact op alle verdere sturing. Dit móét deze cyclus hard belegd worden bij de eigenaar — het is belangrijker dan welke on-page tweak dan ook.

## Focusvraag 3 — Autonoom-veilige on-page hefbomen deze sprint

De grote hefbomen (Ads herstellen, GSC koppelen, key-events markeren) zijn allemaal geblokkeerd in autonome modus → escalatie. Wat blijft er autonoom-veilig over zónder de rijpende cyclus-20/21-pagina's (`prijsindicatie`, `heerenveen`, `drachten`, wizard-flow) aan te raken tot ~27 jul?

1. **FAQ-sjabloon uitrollen naar de volgende stadspagina (Emmen).** Cyclus 22 zette Groningen; de afgesproken cadans is één pagina per sprint (kwaliteit boven bulk). Emmen is een oudere, dunne pagina buiten de rijp-periode. Zichtbare lokale FAQ + `FAQPage`-JSON-LD, exact het bewezen Hoogeveen/Groningen-patroon. Onzichtbaar engagement-risico, additieve SEO-instroom.
2. **Meta-description van de homepage aanscherpen op regio + intentie.** De twee title-varianten in de data ("...Drenthe, Groningen en Friesland" vs. "...richtbedrag in 2 min") presteren verschillend op bounce (0,67 vs. 0,80). De meta-description raakt CTR in de SERP, niet de on-page engagement → geen risico voor de werkende hero. Kan de doelregio scherper vooropzetten om verkeerd-publiek-verkeer te ontmoedigen.
3. **Breadcrumb-schema op de resterende oudere stadspagina's** die cyclus 22 nog niet had (controleer welke; Heerenveen/Drachten blijven uitgesloten tot ~27 jul). Onzichtbaar, versterkt de structuur uit cyclus 22.

**Bewust NIET deze cyclus:** homepage-hero herbouwen (hoog risico op de enige relatief werkende pagina; de hoge bounce is grotendeels een verkeerd-publiek-/seizoensprobleem, geen pagina-probleem), en álles aan de rijpende cyclus-20/21-pagina's. Meetklok niet resetten.

---

## Observaties

1. **Instroom blijft het dominante knelpunt, maar is deels seizoensgebonden.** ~21 sessies/30d, laatste weken 4 en 3. De diepe-zomertrog is grotendeels normaal voor vloerverwarming; de mid-juni-cliff (15→1) is dat níét en blijft de open, onmeetbare vraag zonder GSC.
2. **Het betaalde kanaal is nu volledig dood (0 sessies).** Dat verwijderde tegelijk de enige historische conversiebron. Herstel vereist eerst serveerstatus + juiste landing, dan pas budget — geblokkeerd, escalatie.
3. **De homepage lekt onverminderd.** 76% van de landingssessies, 75% bounce, ~5 s. De sterkste pagina (`prijsindicatie`, 233 s / 0 bounce) wordt er nauwelijks vanaf bereikt. Deels verkeerd publiek (geo buiten regio), deels entree.
4. **0 conversies, 4e cyclus op rij — bewijs kantelt naar meetfout.** Custom lead-events vuren in de code, maar tellen alleen als conversie na key-event-markering in GA4. 90 dagen intens engagement op `prijsindicatie` zonder één lead-event past beter bij een ongemarkeerde meter dan bij een echt lege trechter. Nog steeds niet geverifieerd.
5. **GSC feitelijk niet gekoppeld.** OAuth `invalid_grant` (6+ weken) én een placeholder `REPLACE_WITH_TOKEN` in de site-verificatie-meta op alle 11 pagina's. Zolang dit staat is de instroomdiagnose (observatie 1) en het SEO-effect van cyclus 17–22 onmeetbaar. Langst openstaande blokkade.
6. **Doelregio blijft minderheid.** Drenthe+Groningen+Friesland = 4 van 21 sessies (Friesland 0). North Holland + Duitsland + South Holland + USA samen groter. Organisch bereik trekt deels het verkeerde publiek — dat drukt bounce en conversie, los van de pagina-inhoud.

## Voorstellen voor Product Manager

Rode draad: de trechter is bijna leeg én we sturen blind (GSC uit, meter mogelijk kapot). De hoogste hefboom deze cyclus is niet nóg een on-page ingreep, maar het **hard beleggen van de meet- en koppelblokkades bij de eigenaar**. On-page: één veilige, additieve SEO-stap (Emmen-FAQ) in de bewezen cadans. Rijpende pagina's met rust.

### Voorstel 1 — Escaleer (4e keer, hardst) de conversie-meting bij de eigenaar
- **Prioriteit:** Hoog
- **Onderbouwing:** 4 cycli 0 conversies over álle kanalen, terwijl lead-events (`wizard_lead_submit`, `lead_form_submit`, `contact_submit`) aantoonbaar in de code vuren en `prijsindicatie` 90d lang 133 s gemiddelde duur toont. Custom events tellen niet als conversie zonder key-event-markering. Zolang dit open staat weten we niet of cyclus 21's lead-drempelverlaging meetbaar is.
- **Actie (eigenaar, niet autonoom):** (a) Formspree-inboxen `xzdojzdk` (calculator) + `xgodnvoq` (contact) controleren — komen er aanvragen binnen? (b) GA4 → Admin → Events: zijn `wizard_lead_submit` / `lead_form_submit` / `contact_submit` als **key event** gemarkeerd? Zo niet: markeren. ~10 minuten, bepaalt of we op conversie of op instroom sturen.
- **Verwacht effect:** duidelijkheid of "0 conversie" echt is of een meetartefact. Grootste hefboom op sturingskwaliteit.

### Voorstel 2 — Herstel GSC-koppeling: OAuth vernieuwen én de placeholder-verificatietoken vervangen
- **Prioriteit:** Hoog
- **Onderbouwing:** De instroom zakte van 15 naar 1 sessie in de week van 15 jun — te abrupt voor seizoen. Zonder GSC (impressies, posities, zoektermen) kunnen we niet zien of dit een ranking-/indexatiedip is of gewoon volume. Bovendien draagt élke pagina `<meta name="google-site-verification" content="REPLACE_WITH_TOKEN">` — een placeholder; de meta-verificatie is nooit voltooid.
- **Actie (eigenaar, niet autonoom):** (a) `python scripts/gsc_get_refresh_token.py` met verified owner-account → daarna `gsc_fetch.py` volgende cyclus. (b) Het echte site-verificatietoken uit Search Console leveren zodat `REPLACE_WITH_TOKEN` site-breed vervangen kan worden (autonoom uit te voeren zodra het token er is).
- **Verwacht effect:** verse GSC-data → onderbouwde instroomdiagnose in plaats van giswerk; voltooide site-verificatie.

### Voorstel 3 — Betaald kanaal: serveerstatus + landing herstellen (cpc nu 0 sessies)
- **Prioriteit:** Hoog
- **Onderbouwing:** `google/cpc` viel 12 → 1 → **0** sessies over drie cycli en was historisch 100% van alle conversies. Dit is geen normale werking; wijst op gepauzeerde/afgekeurde campagne. Zolang dit stilstaat, mist de site zijn enige bewezen conversiebron.
- **Actie (eigenaar, niet autonoom):** campagnestatus/afkeuringen checken; RSA final URL's op de juiste landing (koop-adgroep → `prijsindicatie.html`, offerte-adgroep → `contact.html?modus=offerte#aanvraag`); budget pas ná fixes + expliciete spend-goedkeuring. Ads-scripts geblokkeerd in autonome modus → eigenaar/interactieve sessie.
- **Verwacht effect:** herstel van de enige conversieleverende bron; meetbaar zodra voorstel 1 de meter valideert.

### Voorstel 4 — FAQ-sjabloon uitrollen naar `vloerverwarming-emmen.html`
- **Prioriteit:** Midden
- **Onderbouwing:** Cyclus 22 zette de bewezen lokale-FAQ + `FAQPage`-JSON-LD op Groningen; de afgesproken cadans is één stadspagina per sprint (kwaliteit boven bulk). Emmen is een oudere, dunne pagina (0–1 sessie/30d) buiten de rijp-periode, en de op één na grootste Drentse markt na Assen.
- **Actie:** Kopieer het Hoogeveen/Groningen-patroon naar Emmen: zichtbare sectie `<h2>Veelgestelde vragen — Emmen</h2>` met 3 lokaal ingekleurde Q&A's (kosten → verwijs naar prijsindicatie, infrezen bestaande dekvloer, werkgebied met echte plaatsnamen rond Emmen), plus bijbehorend `FAQPage`-JSON-LD in de `<head>`. Verzin geen feiten. Raak geen rijpende pagina aan.
- **Verwacht effect:** long-tail-eligibility voor lokale Emmen-zoekopdrachten; meetbaar in GSC (mits voorstel 2 slaagt) over ~4 weken. Geen engagement-risico (schema onzichtbaar).

### Voorstel 5 — Homepage meta-description aanscherpen op doelregio (CTR-hefboom, niet on-page)
- **Prioriteit:** Midden
- **Onderbouwing:** 76% van het verkeer landt op `/` en een groot deel valt buiten de doelregio (geo). De meta-description bepaalt de SERP-snippet en dus wie klikt — een scherpere regio-framing kan verkeerd-publiek-klikken ontmoedigen zonder de werkende hero of engagement te raken. De twee title-varianten tonen bovendien verschil in bounce (0,67 vs. 0,80).
- **Actie:** Alleen `<meta name="description">` (en eventueel `og:description`) van `index.html` aanscherpen: Drenthe/Groningen/Friesland expliciet vooraan + de bewezen "richtbedrag in 2 minuten"-belofte. Hero, structuur en CTA's ongemoeid.
- **Verwacht effect:** iets betere SERP-kwalificatie richting doelregio; meetbaar in GSC-CTR (mits voorstel 2). Verwaarloosbaar risico.

### Voorstel 6 — NIET doen deze cyclus: rijpende pagina's aanraken of homepage-hero herbouwen
- **Prioriteit:** (bewuste onthouding)
- **Onderbouwing:** Cyclus 20/21-pagina's (`prijsindicatie` lead-flow, Heerenveen, Drachten) rijpen tot ~27 jul; ingrijpen reset de meetklok. De homepage-hero draagt al de bewezen CTA én de regio; de hoge bounce is grotendeels een verkeerd-publiek-/seizoensprobleem dat een hero-tweak niet oplost. Niet de enige (relatief) werkende pagina riskeren zonder GSC-zicht.
- **Actie:** met rust laten tot ~27 jul; dan meetklok van cyclus 19/20/21 uitlezen.

---

## Samenvatting

De trechter is bijna leeg (~21 sessies/30d, laatste weken 4 en 3) en staat voor de **4e cyclus op rij** op 0 conversies. De instroomterugval is het meest waarschijnlijk **seizoenstrog + volledig weggevallen betaald kanaal (cpc nu 0)**, met een reëel maar onbevestigd vermoeden van een organische dip mid-juni (de cliff 15→1 in de week van 15 jun). Zonder GSC — dat via OAuth `invalid_grant` én een placeholder-verificatietoken feitelijk niet gekoppeld is — kunnen we dat niet zien. De 0 conversies kantelt richting **meetfout**: de lead-events vuren aantoonbaar in de code maar tellen alleen als conversie na key-event-markering in GA4, en 90 dagen intens engagement op `prijsindicatie` (133 s) zonder één lead-event past niet bij een echt lege trechter. Prioriteit deze cyclus: de meet- en koppelblokkades hard beleggen bij de eigenaar (conversie-key-events, GSC-OAuth + verificatietoken, Ads-serveerstatus). Autonoom-veilig on-page: de bewezen FAQ-sjabloon doorzetten naar Emmen (voorstel 4) en de homepage-meta-description aanscherpen op de doelregio (voorstel 5). Bewust niet: rijpende cyclus-20/21-pagina's of de homepage-hero aanraken — meetklok niet resetten tot ~27 jul.
