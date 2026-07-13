# Analytics Rapport — 13 juli 2026 (cyclus 22)

**Periode:** 30 dagen tot 13 jul 2026 (GA4 property `properties/534641753`, opgehaald 13 jul 06:01)
**Vorige sprint effect:** Cyclus 21 staat pas 7 dagen live (6 jul). De drie ingrepen — lichtere lead-drempel op `prijsindicatie.html`, Drachten-only refactor, CTA-tekst gelijkgetrokken — rijpen tot ~27 jul. Ze zijn in dit venster **niet** te beoordelen. Wat wél zichtbaar is: de instroom zakt verder door, en er staan opnieuw 0 conversies over alle kanalen (derde cyclus op rij).

## Kerncijfers

| Metric              | Waarde (30d)        | Trend                          |
| ------------------- | ------------------- | ------------------------------ |
| Sessies             | ~22                 | ↓ ~35% (was ~34 vorige cyclus) |
| Actieve gebruikers  | ~21                 | ↓                              |
| Conversies          | 0                   | = 0 (3e cyclus op rij)         |
| Bounce homepage `/` | 73%                 | ↑ (boven zorggrens 70%)        |
| Gem. duur `/`       | ~5–7 s              | zeer laag                      |

Grondwaarheid instroom (week-sessies): 56 (18 mei) → 15 → 16 → 15 → 1 → 5 → 9 → **4** (6–12 jul). De laatste week is de laagste ooit gemeten. We draaien op ~7% van het mei-niveau.

## Top pagina's (30d)

| Pagina                        | Sessies | Gem. duur | Bounce |
| ----------------------------- | ------- | --------- | ------ |
| `/` (alle titelvarianten)     | 20      | ~5–7 s    | ~70%   |
| `/diensten.html`              | 3       | 10 s      | 0%     |
| `/prijsindicatie.html`        | 2       | **233 s** | 0%     |
| `/contact.html`               | 2       | 26 s      | 0%     |
| `/vloerverwarming-zuidlaren`  | 2       | 14 s      | 0%     |
| `/systemen-producten.html`    | 1       | 67 s      | 0%     |

## Sterkste engagement (90d, richtinggevend)

| Pagina                    | Sessies | Gem. duur |
| ------------------------- | ------- | --------- |
| `/prijsindicatie.html`    | 70      | **133 s** |
| `/werkwijze.html`         | 24      | 108 s     |
| `/systemen-producten.html`| 22      | 95 s      |
| `/contact.html`           | 62      | 62 s      |
| `/`                       | 261     | 62 s      |

## Zwakste pagina's

- **Homepage `/`**: 20 van 22 sessies, ~70% bounce, 5–7 s duur. Het instappunt van bijna al het verkeer overtuigt niet. Dit is het lek.
- **Stadspagina's**: 1–2 sessies elk over 30d. Dunne instroom; niet de bottleneck, maar leveren ook niets op.

## Traffic bronnen (30d)

| Bron                    | Sessies | Conversies |
| ----------------------- | ------- | ---------- |
| Direct / (none)         | 12      | 0          |
| Organic google / organic| 8       | 0          |
| google / cpc            | 1       | 0          |
| Unassigned / (not set)  | 1       | 0          |

`google/cpc` — historisch 100% van alle conversies — is teruggevallen naar 1 sessie. Het betaalde kanaal staat feitelijk stil.

## Geografie (30d)

North Holland 5, Drenthe 4, Duitsland (Schleswig-Holstein) 3, South Holland 3, Groningen 1, Gelderland 1. **Kernprobleem:** de doelregio (Drenthe/Groningen/Friesland) is minderheid. Het grootste segment (North Holland) en het Duitse verkeer vallen buiten het werkgebied — dat verklaart mede de hoge bounce en 0 conversie: verkeerd publiek op de homepage.

## Observaties

1. **Instroom is nu het dominante, verslechterende knelpunt.** ~22 sessies/30d, laatste week 4 — de laagste ooit. Alle conversie-optimalisatie werkt op een lege trechter. Zolang de instroom instort is dit belangrijker dan welke pagina-tweak dan ook.
2. **De homepage lekt.** 20/22 sessies landen op `/`, ~70% bounce, ~5 s duur. Wie via organic of direct binnenkomt, ziet de homepage en gaat weg. De sterke pagina's (prijsindicatie 233 s, systemen 67 s) worden nauwelijks bereikt vanaf die entree.
3. **0 conversies over álle kanalen, derde cyclus op rij — dit blijft de open meetvraag.** Bij ~22 sessies kán het simpelweg te weinig verkeer zijn (de emmer lekt), maar 3 cycli nul over élk kanaal terwijl `wizard_lead_submit` / `lead_form_submit` / `contact_submit` afvuren wijst óók op een kapotte meter (events niet als **key event** gemarkeerd in GA4). Dit is nog steeds niet door de eigenaar geverifieerd (escalatie cyclus 21, punt 1). Zonder die verificatie weten we niet of "0 conversie" echt is.
4. **Geografische mismatch.** Doelregio Noord-NL is minderheid; North Holland + Duitsland zijn samen groter dan Drenthe+Groningen+Friesland. Organic bereikt deels het verkeerde publiek — dat drukt bounce omhoog en conversie omlaag, los van de pagina-inhoud.
5. **Cyclus-20/21-pagina's rijpen nog.** Heerenveen-pagina, contact/systemen/werkwijze wizard-first (cyclus 20, 1 jul) en de cyclus-21-ingrepen (6 jul) zijn te vers. Meetklok niet resetten; niet als mislukking lezen tot ~27 jul.
6. **GSC nog steeds blind** (`invalid_grant`). SEO-effect van cyclus 17–21 is niet meetbaar; we kunnen niet zien of organic zoektermen/impressies bewegen. Dat maakt de instroomdiagnose deels giswerk.

## Voorstellen voor Product Manager

Rode draad: de trechter is bijna leeg. De hoogste hefboom zit niet in nóg een conversie-tweak op een pagina die nauwelijks bezoek krijgt, maar in **(a) de homepage die het meeste verkeer opvangt beter laten vasthouden** en **(b) de meet- en instroomvraag hard beleggen bij de eigenaar**. De verse cyclus-21-pagina's blijven met rust.

### Voorstel 1 — Homepage-entree aanpakken: eerste scherm richten op doelregio + directe route naar de wizard
- **Prioriteit:** Hoog
- **Onderbouwing:** 20/22 sessies (91%) landen op `/`, ~70% bounce, ~5 s duur. Dit is het grootste en slechtst presterende instappunt. De sterkste pagina van de site (`prijsindicatie.html`, 233 s / 0 bounce) wordt daarachter nauwelijks bereikt.
- **Actie:** Optimaliseer het eerste scherm van `index.html`: één heldere regio-belofte (Drenthe/Groningen/Friesland expliciet boven de vouw) en de bewezen CTA "Richtbedrag in 2 minuten →" prominent als eerste actie. Geen herbouw — alleen het bovenste blok scherper. Raak de wizard en de cyclus-21-pagina's niet aan.
- **Verwacht effect:** homepage-bounce onder 65%, gem. duur `/` omhoog, meer doorklik naar `prijsindicatie.html`. Meetbaar over ~4 weken.

### Voorstel 2 — Escaleer (opnieuw, harder) de conversie-meting bij de eigenaar
- **Prioriteit:** Hoog
- **Onderbouwing:** 3 cycli lang 0 conversies over álle kanalen, terwijl lead-events afvuren. Dit is nog niet geverifieerd. Zolang dit open staat, weten we niet of taak 1 van cyclus 21 (lichtere lead-drempel) überhaupt te meten is, of dat we blind sturen.
- **Actie (eigenaar, niet autonoom):** (a) Controleer Formspree-inboxen `xzdojzdk` (calculator) en `xgodnvoq` (contact) — komen daar aanvragen binnen? (b) Check GA4 → Admin → Events: zijn `wizard_lead_submit` / `lead_form_submit` / `contact_submit` als **key event** gemarkeerd? Zo niet: markeren. Dit is een 10-minuten-taak met grote impact op alle verdere sturing.
- **Verwacht effect:** duidelijkheid of "0 conversie" echt is of een meetartefact. Bepaalt of we op conversie of op instroom moeten sturen.

### Voorstel 3 — Instroomdiagnose: GSC-koppeling herstellen om organic-terugval te kunnen zien
- **Prioriteit:** Hoog
- **Onderbouwing:** De instroom is in 8 weken van 56 naar 4 sessies/week gezakt. We kunnen de oorzaak niet zien: GSC is 5+ weken oud (`invalid_grant`), dus zoektermen, impressies en posities zijn onzichtbaar. Zonder GSC is elke instroom-actie een gok.
- **Actie (eigenaar, niet autonoom):** `python scripts/gsc_get_refresh_token.py` met verified owner-account draaien; daarna `gsc_fetch.py` in de volgende cyclus. Pas dán kunnen we zien of de organic-daling een indexatie-/ranking-probleem is of gewoon seizoen/volume.
- **Verwacht effect:** verse GSC-data volgende cyclus → onderbouwde instroom-strategie in plaats van giswerk.

### Voorstel 4 — Kleine, veilige afronding: twee resterende `btn-secondary`-knoppen gelijktrekken
- **Prioriteit:** Midden
- **Onderbouwing:** Cyclus 21 zette de bewezen CTA "Richtbedrag in 2 minuten →" op 22 primaire knoppen, maar liet bewust 2 secundaire knoppen (`contact.html`, `werkwijze.html`) op "Naar de prijsindicatie" staan (btn-primary-only-regel). Dit is de afgesproken open follow-up.
- **Actie:** Werk die twee `btn-secondary`-labels bij naar "Richtbedrag in 2 minuten →". Puur label-swap, raakt geen funnel-meting. Kan mee in dezelfde cyclus als voorstel 1.
- **Verwacht effect:** volledig consistente CTA site-breed; verwaarloosbaar risico.

### Voorstel 5 — NIET doen deze cyclus: de cyclus-20/21-pagina's aanraken of nieuwe pagina's stapelen
- **Prioriteit:** (bewuste onthouding)
- **Onderbouwing:** Prijsindicatie-lead-drempel (6 jul), Drachten-refactor (6 jul) en de Heerenveen-pagina (1 jul) rijpen tot ~27 jul. Ingrijpen nu reset de meetklok en maakt het effect van cyclus 21 onmeetbaar. Bij ~1–2 sessies per stadspagina voegt een nieuwe dunne pagina niets toe.
- **Actie:** Laat deze pagina's met rust tot ~27 jul. Focus deze cyclus op de homepage-entree (voorstel 1) en de eigenaar-escalaties (2 en 3).

### Escalatie-only (geblokkeerd in autonome modus, GEEN taak)
- **Google Ads / betaald kanaal.** `google/cpc` was 100% van alle conversies, staat nu op 1 sessie. Herstel vereist eerst RSA final-URL's op de juiste landing (koop-adgroep → `prijsindicatie.html`, offerte-adgroep → `contact.html?modus=offerte#aanvraag`), daarna pas budget. Ads-scripts zijn geblokkeerd in autonome modus → alleen de eigenaar of een interactieve sessie kan dit. Noem als escalatie, niet als sprint-taak.

---

## Samenvatting

De trechter is bijna leeg (~22 sessies/30d, laatste week 4 — laagste ooit) en staat voor de derde cyclus op rij op 0 conversies. Instroom is nu het dominante, verslechterende knelpunt. Prioriteit deze cyclus: (1) de homepage-entree scherper maken — 91% van het verkeer landt daar met ~70% bounce; (2) de eigenaar de conversie-meting laten verifiëren (Formspree + GA4 key events); (3) de GSC-koppeling herstellen zodat we de organic-terugval kunnen zíen. Klein en veilig: de twee resterende secundaire CTA-knoppen gelijktrekken (voorstel 4). Bewust niet doen: de cyclus-20/21-pagina's aanraken — die rijpen tot ~27 jul, meetklok niet resetten.
