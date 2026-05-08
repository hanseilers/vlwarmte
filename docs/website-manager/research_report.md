# Marketing Research Rapport — 8 mei 2026

**Bronnen:** `docs/website-manager/analytics_report.md` (fetch 8 mei 2026), `.cursor/skills/google-ads-marketing/SKILL.md`, korte SERP-check (WebSearch), repo-scripts voor Google Ads (read-only + `--dry-run` mutaties). Geen credentials of accountnummers in dit document.

## Samenvatting

GA4 toont **sterke conversies via Direct** en vooral **homepage + prijsindicatie-wizard**; **Paid Search (`google/cpc`) blijft 12 sessies en 0 conversies** — dat wijst eerder op **meet- en landingsafstemming** dan op gebrek aan vraag. Week-op-week daalde het sessievolume sterk (**134 → 54**); dat vraagt een korte PM-hypothese (seizoen, campagne, meetruis). Lokaal blijft concurrentie op stadstermen hoog (ComfortFloors, Lemmers, InFloor, RM Vloeren, ReWo & De Jong, enz.); onderscheid blijft **traject, regio en transparant richtbedrag**.

## Top zoekwoorden (indicatief)

| Zoekwoord / cluster | Volume | Concurrentie | Pagina / actie |
| ------------------- | ------ | ------------- | -------------- |
| vloerverwarming + Groningen/Assen/Drenthe | hoog | hoog | bestaande stadspagina’s; snippets blijven bijschaven |
| schuimbeton / ondervloer + vloerverwarming | midden | midden | `diensten.html`, FAQ, Ads-termen |
| wat kost / € per m² / kosten | hoog | hoog | `prijsindicatie.html` + Ads-intentie (zie defaults JSON) |
| installateur + regio | hoog | hoog (gidsen + CV-breed) | lokaal adres + werkwijze + GBP |

## Google Ads — agentverificatie (deze omgeving)

- **Smoke test** en **campagneoverzicht (read-only):** API bereikbaar; er draait een **ENABLED Search-campagne** (naam begint met `VLW-API-`).
- **`google_ads_create_search_campaign.py --dry-run`:** gelukt na bijstelling RSA-headlines (max. 15); defaults-JSON is syntactisch geldig voor toekomstige API-aanmaak.
- **`google_ads_add_rsa_variant.py --dry-run`:** validatie **OK** voor tweede RSA op de bestaande Search-campagne — **`--apply` alleen na expliciete goedkeuring** in chat (geen spend-go-live nodig voor alleen creatie).
- **`scripts/data/google_ads_lead_campaign_defaults.json`:** uitgebreid met **phrase**-keywords *vloerverwarming kosten* en *prijs vloerverwarming* en headlines gericht op **richtbedrag online** en **werkgebied Zuid-Laren** (bestaande live campagne synchroniseert dit **niet automatisch**; Developer/Marketing: keywords en RSA’s in Ads alsnog alignen of nieuwe mutatie-ronde plannen).

## Prijscalculator — kort (site al voorzien)

De site heeft al een **prijsindicatie-wizard** met sterk conversiepad in GA4. **Conclusie:** geen aparte “nieuwe calculator” bouwen; wel **meting en copy** blijven verfijnen (zie voorstellen). Juridisch: blijft vrijblijvende indicatie communiceren zoals nu in wizard en disclaimer.

## Concurrentie (kort)

Regionale en landelijke spelers combineren **stadspagina’s**, **snelle montagebeloftes** en **gratis offerte**. VLWarmte blijft differentiëren met **compleet traject** (ondervloer, schuimbeton, installatie, dekvloer), **echt Noord-Nederlands werkgebied** en **online richtbedrag vóór offerte**.

---

## Aanbevelingen voor Product Manager (6)

1. **Prioriteit Hoog — GA4 ↔ Google Ads + conversies**  
   - **Type:** Analytics / Ads-config (geen site-code vereist, wel admin).  
   - **Onderbouwing:** Paid Search met **0 conversies** terwijl Direct wél converteert → typisch **koppeling, auto-tagging of primary/secondary conversions** niet op één lijn.  
   - **Actie:** Skill §A doorlopen (property link, auto-tagging `gclid`,zelfde events als site: o.a. formulier- en wizard-events). Daarna 2–4 weken opnieuw `analytics_report.md` genereren.

2. **Prioriteit Hoog — Paid landings = wizard of offerte-deeplink**  
   - **Type:** Ads + landings/copy.  
   - **Onderbouwing:** Beste conversielandings zijn **`/`** en **`/prijsindicatie.html`**; contact als landing heeft hoge bounce.  
   - **Actie:** RSA’s en sitelinks laten verwijzen naar **`prijsindicatie.html`** en **`contact.html?modus=offerte#aanvraag`** (niet generiek contact zonder modus). Defaults JSON in repo is hierop al afgestemd; live campagne-inhoud expliciet vergelijken.

3. **Prioriteit Hoog — Week-op-week sessiedaling onderzoeken**  
   - **Type:** PM / data (eventueel Search Console + Ads-impressieszelfde week).  
   - **Onderbouwing:** **134 → 54** sessies in opeenvolgende 7-dagenblokken.  
   - **Actie:** Eén hypothesetabel (seizoen, budget/pauze, indexering, meetgap); één correctieve actie op backlog.

4. **Prioriteit Midden — Tweede RSA (`add_rsa_variant`) toepassen**  
   - **Type:** Ads-creatie (API `--apply` na chat-goedkeuring).  
   - **Onderbouwing:** Dry-run succesvol; tweede RSA verbetert vaak **Ad strength** en headline-variatie voor dezelfde keywords.  
   - **Actie:** Na PM-go: `google_ads_add_rsa_variant.py --apply` met `extra_rsa` uit defaults JSON (geen `--go-live` nodig tenzij campagne gepauzeerd was).

5. **Prioriteit Midden — Hoge-bounce landings (`diensten`, `over-ons`, `systemen`, `projecten`)**  
   - **Type:** Content / CTA (Developer-sprint, reeds deels ingepland).  
   - **Onderbouwing:** Analytics toont bounce **0,79–1,0** op meerdere instappagina’s met laag volume.  
   - **Actie:** Vroege **terugbel / prijsindicatie**-CTA’s en interne links vanaf homepage; sprint SEO snippets + formulier boven adres op contact waar van toepassing.

6. **Prioriteit Laag — Restverkeer `logo-varianten.html` + GBP**  
   - **Type:** Redirect/opschonen + off-site.  
   - **Onderbouwing:** Nog sessies op verwijderde/verwarde route; **Google Bedrijfsprofiel** blijft zwaar lokaal signaal naast organische pagina’s.  
   - **Actie:** 301 naar home of FAQ; GBP foto’s, categorie en reviewstroom (eigenaar).

---

## Hashtags (social)

Zie playbook in `.claude/commands/marketing-research-agent.md`: Facebook 0–3 optioneel, Instagram 5–10 relevant, LinkedIn 3–5 vak/regio — spaarzaam, geen trend-spam.
