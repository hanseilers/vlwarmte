# Analytics Rapport — 6 juli 2026

**Periode:** 7 juni – 6 juli 2026 (30 dagen), plus 90d-engagement en 8-weeks trend
**Databron:** GA4 property 534641753, opgehaald 6 jul 06:01
**Vorige sprint effect:** Cyclus 20 (live 1 jul, 5 dagen geleden) leverde de Heerenveen-pagina + wizard-first CTA's op diensten/systemen/contact/werkwijze. **Te vers om te beoordelen** — die pagina's laten we deze cyclus met rust. Cyclus-19-wizard rijpt door tot ~27 jul.

---

## De alarmbel: 0 conversies over álle kanalen

Dit is de grootste bevinding van deze cyclus. Vorige keer kwamen er nog 2 conversies binnen, beide uit `google/cpc` (~10,5% ratio). **Nu staat de teller op 0 — Direct, cpc, organic én AI-assistant allemaal op nul.** De betaalde motor die vorige maand nog leads gaf, viel volledig stil.

Er zijn twee mogelijke verklaringen en die moet je uit elkaar houden, want ze vragen om totaal verschillende actie:

1. **Er komen écht geen leads binnen** — instroom is zo laag (34 sessies/30d) dat het bij een normale ratio statistisch goed 0 kan zijn. 34 sessies × ~5% ≈ 1,7 lead; dat kan een venster van 0 opleveren.
2. **De conversies wórden niet gemeten.** De site vuurt wél custom events af bij een lead: `wizard_lead_submit` en `lead_form_submit` (prijsindicatie.html, r.1688–1694) en `contact_submit` (main.js r.208). Maar de GA4-conversiekolom telt die pas mee als ze in GA4 als **key event** zijn aangemerkt. Als dat nooit is ingesteld, staat de kolom structureel op 0 — ongeacht hoeveel leads er binnenkomen via Formspree.

**Dit moet als eerste worden uitgezocht** (zie voorstel 1). Zolang we niet weten óf de meting klopt, weten we niet of we een instroom-probleem of een meet-probleem oplossen. De echte grondwaarheid zit in de Formspree-inbox: hoeveel aanvragen kwamen daar de afgelopen 30 dagen binnen? Dat cijfer beslecht de vraag.

---

## Kerncijfers (30 dagen)

| Metric              | Waarde              | Trend                          |
| ------------------- | ------------------- | ------------------------------ |
| Sessies (30d)       | ~34                 | ↓ ~11% (was 38)                |
| Actieve gebruikers  | ~30                 | ↓                              |
| Conversies (30d)    | **0**               | ↓ van 2 → 0 (alle kanalen)     |
| Gem. sessieduur     | sterk pagina-afhankelijk | prijsindicatie 312s, diensten 5s |
| Weektrend (laatste) | 9 sessies (29 jun–5 jul) | ↑ van 5, maar structureel laag |

**Instroom is en blijft het knelpunt.** In mei draaide de site nog 49–56 sessies/week; sinds eind mei zit hij op 1–16/week. De laatste week (9) is een lichte opleving, maar we zitten op een vijfde tot een zesde van het mei-niveau. Dit is geen ruis — dit is een structurele terugval in bereik.

---

## Top pagina's (30d)

| Pagina                        | Sessies | Gem. duur | Bounce | Signaal                                  |
| ----------------------------- | ------- | --------- | ------ | ---------------------------------------- |
| `/` (homepage, alle titels)   | ~27     | wisselend | ~55%   | instappunt nr. 1 (22 landings)           |
| `/prijsindicatie.html`        | 8       | **312s**  | 25%    | sterkste engagement, 0 conv — zie hieronder |
| `/contact.html`               | 4       | 139s      | **0%** | leest goed, converteert niet             |
| `/systemen-producten.html`    | 4       | 30s       | 50%    | bounce daalde (was 67%) — cyclus 20?     |
| `/diensten.html`              | 3       | **5s**    | 33%    | zeer korte duur, zwak                    |
| `/faq.html`                   | 2       | 64s       | 0%     | klein maar betrokken                     |
| `/vloerverwarming-drachten.html` | 2    | 107s      | 0%     | goede duur; title mixt nog Drachten+Heerenveen |

**`prijsindicatie.html` is het paradepaardje én het raadsel.** 312s gemiddelde sessieduur (90d: 69 sessies, 130s) met slechts 25% bounce — mensen dóórlopen de wizard, dat is uitzonderlijk sterk engagement voor een prijstool. En tóch 0 conversies over 90d. Dat wijst óf op een meet-gat (voorstel 1), óf op een drempel in de laatste stap: het lead-formulier komt pas ná de prijsberekening (`lead-after`, r.810–863) en vraagt naam + telefoon verplicht. Wie het richtbedrag heeft en verder niets wil, haakt daar af — precies wat je verwacht bij zulke lange sessies zonder conversie.

**`vloerverwarming-heerenveen.html`** (nieuw, live 1 jul) staat niet in de 30d-lijst — te vers, ~0 sessies. **Niet als mislukking beoordelen**; pas over ~4 weken meetbaar.

---

## Zwakste pagina's

| Pagina                     | Sessies | Duur | Bounce | Probleem                                    |
| -------------------------- | ------- | ---- | ------ | ------------------------------------------- |
| `/diensten.html`           | 3       | 5s   | 33%    | duur van 5s = mensen lezen niet, ze scannen en gaan |
| `/over-ons.html`           | 2       | 8s   | 0%     | korte duur                                  |
| `/werkwijze.html`          | 2       | 11s  | 0%     | korte duur, maar 90d wél 108s — n=2 vertekent |

`diensten.html` valt op: met 30 sessies over 90d en 63s gem. duur is het normaal geen slechte pagina, maar de 5s deze 30d bij 3 sessies is opvallend kort. De hero-CTA heet nog het brave **"Naar de prijsindicatie"** (r.73), terwijl de cta-band onderaan het sterkere **"Richtbedrag in 2 minuten →"** gebruikt. De hero is het eerste dat iemand ziet; dáár moet de scherpe belofte staan, niet onderaan. Dit is één van de weinige veilige, cyclus-20-onafhankelijke ingrepen: de cta-band zelf is vers (niet aankomen), maar de hero-knoptekst is dat niet.

---

## Traffic bronnen (30d)

| Bron                         | Sessies | Conversies |
| ---------------------------- | ------- | ---------- |
| Direct / (none)              | 15      | 0          |
| google / cpc (Cross-network) | 12      | **0** (was ~10,5%) |
| google / organic             | 6       | 0          |
| chatgpt.com / ai-assistant   | 1       | 0          |

**De cpc-terugval is de scherpste bocht.** Vorige cyclus was cpc de enige bron die converteerde; nu 12 sessies, 0 conv. Bij €2/dag en 12 sessies is 0 nog binnen de statistische marge, maar in combinatie met de site-brede 0 versterkt het het vermoeden van een meet-gat. **Aanbeveling voor Marketing Research Agent:** controleer of de Ads-conversie-import vanuit GA4 nog werkt en of het juiste key event gekoppeld is — een cpc-ratio die van 10,5% naar 0 klapt zonder inhoudelijke reden is verdacht.

Eén AI-assistant-sessie (chatgpt.com) — klein maar het teken dat de site in AI-antwoorden opduikt. Niets voor nu, wel om te blijven volgen.

---

## Geografie & device

**Geo:** In de regio 15 sessies (Drenthe 9, Friesland 3, Groningen 3). Buiten de regio 12 (Noord-Holland 5, Zuid-Holland 3, Duitsland 3, Canada 1). Dat is relatief véél buiten het werkgebied — bijna de helft. Bij zo'n laag totaal weegt elke buiten-regio-sessie zwaar; het is deels historische rest in het 30d-venster (Ads-geo staat al goed op DR/GR/FR volgens cyclus 20). Geen mutatie nodig, wél in de gaten houden.

**Device:** mobile 18, desktop 15, tablet 1. Mobiel is de meerderheid — de mobiele ATF van de wizard (r.400–458) is dus terecht al aangescherpt. Houd mobiel leidend bij elke CTA-wijziging.

---

## Observaties

1. **0 conversies is óf een lek in de emmer, óf een kapotte meter.** De site stuurt lead-events, maar GA4 telt 0. Eerst uitzoeken welke van de twee het is (Formspree-inbox = grondwaarheid), pas daarna optimaliseren.
2. **prijsindicatie.html bewijst dat de wizard werkt** (312s, 25% bounce) maar zet dat engagement niet om in leads. De verplichte naam+telefoon ná het richtbedrag is de meest waarschijnlijke inhoudelijke drempel.
3. **Instroom staat op ~20% van het mei-niveau.** Alle CTA-optimalisatie ten spijt: zonder bezoekers geen leads. Dit is een SEO/Ads-vraagstuk (escalatie), geen site-content-vraagstuk.
4. **GSC is nog steeds ~5+ weken oud** (`invalid_grant`). SEO-effect van cyclus 17–20 is niet meetbaar. Dit blokkeert het beantwoorden van observatie 3 — escalatie, geen dev-taak.
5. **Cyclus 20 raakte vijf pagina's aan (1 jul).** diensten/systemen/contact/werkwijze/Heerenveen zijn te vers voor een oordeel; niet opnieuw wijzigen deze cyclus.

---

## Voorstellen voor Product Manager

### 1. Verifieer de conversie-meting — is de meter kapot of de emmer leeg? `[HOOG]`
- **Prioriteit:** Hoog
- **Onderbouwing:** Site vuurt `wizard_lead_submit`, `lead_form_submit` (prijsindicatie.html r.1688–1694) en `contact_submit` (main.js r.208) af, maar GA4 conversiekolom = 0 over álle kanalen, 90d lang. cpc viel van 10,5% naar 0.
- **Actie:** (a) Tel de Formspree-aanvragen van de laatste 30d in beide inboxen (`xzdojzdk` = calculator, `xgodnvoq` = contact) — dat is de grondwaarheid. (b) Controleer in GA4 Admin of `wizard_lead_submit`/`lead_form_submit`/`contact_submit` als **key event (conversie)** zijn gemarkeerd. Zo niet: dat verklaart de 0 volledig. **Dit is geen autonome dev-taak — het is een GA4-config- en inbox-check voor de eigenaar/PM.**
- **Verwacht effect:** Duidelijkheid of we een instroom- of een meetprobleem oplossen. Zonder dit tasten alle andere conversie-voorstellen in het duister.

### 2. prijsindicatie.html — verlaag de drempel van de lead-stap `[HOOG]`
- **Prioriteit:** Hoog
- **Onderbouwing:** 312s duur, 25% bounce, 90d 69 sessies — sterkste engagement van de site, tóch 0 conv. Formulier ná het richtbedrag vraagt naam + telefoon verplicht; e-mail en woonplaats staan lager. Wie alleen het bedrag wilde, haakt af.
- **Actie:** Maak de eerste stap lichter: vraag alléén naam + één contactveld (telefoon óf e-mail, niet beide verplicht), of bied expliciet "stuur de indicatie naar mijn mail" als laagdrempelig alternatief. Geen tweede formulier, geen wizard-stappen aanraken — puur de `lead-after`-velden (r.832–853). Cyclus-19-wizard blijft ongemoeid (die zit vóór dit blok).
- **Verwacht effect:** Meetbaar over ~4 weken: eerste `wizard_lead_submit`-events > 0 (mits voorstel 1 de meting bevestigt).

### 3. diensten.html — scherp de hero-CTA aan naar de bewezen belofte `[MIDDEN]`
- **Prioriteit:** Midden
- **Onderbouwing:** 5s gem. duur deze 30d — mensen scannen en gaan. Hero-knop heet nog "Naar de prijsindicatie" (r.73); de cta-band onderaan gebruikt het sterkere "Richtbedrag in 2 minuten →". De hero is het eerste contactpunt.
- **Actie:** Wijzig alléén de hero-knoptekst naar "Richtbedrag in 2 minuten →" (r.73). De cta-band onderaan is cyclus-20-vers en blijft ongemoeid; dit is één regel, geen structuurwijziging.
- **Verwacht effect:** Hogere doorklik van hero naar wizard; iets langere sessieduur op diensten.

### 4. Herstel de cpc-conversiekoppeling — escalatie Marketing/Ads `[MIDDEN]`
- **Prioriteit:** Midden (escalatie, geen autonome dev-taak)
- **Onderbouwing:** cpc converteerde vorige cyclus als enige (10,5%), nu 12 sessies/0 conv. Als het key event ontbreekt (voorstel 1), importeert Ads geen conversies en stuurt het bidding blind.
- **Actie:** Marketing Research Agent: controleer GA4→Ads-conversie-import en of het juiste key event gekoppeld is. **Ads-scripts zijn in deze modus geblokkeerd — als escalatie naar eigenaar formuleren, niet autonoom draaien.**
- **Verwacht effect:** Ads stuurt weer op echte leads i.p.v. blind; cpc-ratio meetbaar terug.

### 5. Vernieuw GSC-toegang — SEO-effect is nu blind `[MIDDEN]` (escalatie)
- **Prioriteit:** Midden (escalatie eigenaar)
- **Onderbouwing:** GSC ~5+ weken oud (`invalid_grant`). Instroom staat op ~20% van mei; zonder verse GSC kunnen we niet zien of dat een indexatie-, ranking- of seizoensprobleem is.
- **Actie:** Eigenaar draait `scripts/gsc_get_refresh_token.py` met verified owner-account, daarna `gsc_fetch.py` in volgende cyclus. **Geen dev-taak.**
- **Verwacht effect:** Zicht op de oorzaak van de instroomval — de belangrijkste openstaande vraag.

### 6. contact.html — houd, meet, niet wijzigen `[LAAG]`
- **Prioriteit:** Laag (bewust géén actie)
- **Onderbouwing:** 4 sessies, 139s, 0% bounce, 0 conv. De wizard-teaser is cyclus-20-vers (1 jul). Leest goed, converteert nog niet — maar te vroeg voor een oordeel.
- **Actie:** Niet aanraken deze cyclus. Meenemen in de ~27 jul-evaluatie samen met de wizard-funnel.
- **Verwacht effect:** Zuivere meting van het cyclus-20-effect zonder ruis van nieuwe wijzigingen.

### 7. vloerverwarming-drachten.html — Drachten-only maken (na Heerenveen-indexatie) `[LAAG]`
- **Prioriteit:** Laag / afwachten
- **Onderbouwing:** Title/H1/meta mixen nog Drachten + Heerenveen; nu Heerenveen een eigen pagina heeft is dat kannibalisatie-risico. Maar Heerenveen is nog niet geïndexeerd (GSC blind).
- **Actie:** Uitstellen tot GSC bevestigt dat Heerenveen geïndexeerd is; dán Drachten-only refactoren. Nu niets doen.
- **Verwacht effect:** Schonere targeting per stad zodra veilig.

### 8. Instroom is het echte plafond — verwachtingsmanagement `[CONTEXT]`
- **Prioriteit:** Context, geen losse taak
- **Onderbouwing:** 34 sessies/30d. Zelfs een perfecte conversieratio levert op dit volume weinig absolute leads. CTA-optimalisatie (voorstel 2–3) is traffic-onafhankelijke winst en verstandig, maar de grote hefboom is méér gekwalificeerde bezoekers (Ads-budget + SEO/GSC).
- **Actie:** PM: weeg dat de grootste groei-hefboom (Ads-budget, escalatie uit cyclus 20) bij de eigenaar ligt, niet in de site-content.
- **Verwacht effect:** Realistische verwachtingen; focus op de juiste knop.

---

*Samengevat: eerst de meter checken (voorstel 1) — 0 conversies mét werkende lead-events schreeuwt om een key-event-verificatie. Daarna twee veilige, cyclus-20-onafhankelijke content-ingrepen: de lead-drempel op prijsindicatie verlagen en de hero-CTA op diensten aanscherpen. Alles rond cyclus-20-pagina's en de wizard-funnel: laten rijpen tot ~27 jul. GSC en Ads: escaleren, niet zelf draaien.*
