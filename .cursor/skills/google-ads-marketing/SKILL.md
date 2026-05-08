---
name: google-ads-marketing
description: >-
  Google Ads campaigns, GA4 measurement and linking, landing-page strategy for paid
  traffic, and the analytics→ads feedback loop for vlwarmte.nl lead generation.
  Use for marketing-research, product-manager orchestration, and developer handoff.
---

# Google Ads + GA4 — marketing & PM workflow (VLWarmte)

## North star

- **Primary goal:** maximize **qualified leads** (contact/offerte/bel), not vanity clicks.
- **Product Manager** may orchestrate **Analytics → Marketing (incl. Ads) → Social → Developer**; Ads and landings must stay aligned with **GA4 behavior**, **search intent**, and **sprint capacity** (see `.claude/commands/product-manager.md`).
- **Business owner / product owner does not need Google Ads product knowledge:** agents (with repo + `secrets/google-ads.env` on **this machine**) run the Python workflow end-to-end. The owner is **not** expected to click around in `ads.google.com` for standard setup. **Agents do not delegate routine verification** (e.g. `google_ads_list_campaigns.py`, smoke tests, pasting campaign tables) to the PO — run those commands in the agent session and report conclusions. Irreducible human realities: **payment method and account ownership stay with the business**, occasional **Google policy / verification** prompts, and **approving spend risk** (e.g. confirming `--apply` / `--go-live` in chat when the agent asks once).

## When to use this skill

- Designing or launching **Search / Performance Max** (or other) campaigns and ad groups.
- **Linking Google Ads ↔ Google Analytics 4** and defining **conversions** used for bidding and reporting.
- Building **ad-specific landing paths** (URLs, UTMs, `contact.html` deep links) and iterating copy/layout from **GA4 + Ads** data.
- Using **local scripts** (`scripts/google_ads_*.py`) for read-only checks and for **`google_ads_create_search_campaign.py`** (full lead campaign mutate) after `--dry-run` validation, plus **`google_ads_add_rsa_variant.py`** when a Search ad group needs a **second RSA**.
- **Dutch Ads UI:** warnings about **“componentengroep” / “Itemgroep”** and **too little asset variety** usually refer to **Performance Max asset groups**, not to **Search + RSA** from the API script. Fix PMax in the Ads UI (more headlines, images, logos, video), or rely on the Search campaign if that is the intended channel.

## Ground rules

1. **Secrets:** never paste or commit tokens, refresh tokens, or service-account JSON. Use `secrets/google-ads.env` (gitignored); template `secrets/google-ads.env.example`. GA uses the same service-account JSON pattern as `scripts/ga4_fetch.py` unless overridden.
2. **Campaign creation default (VLWarmte):** use **`scripts/google_ads_create_search_campaign.py`** (`--dry-run` then `--apply`) so the **business owner does not need Ads UI skills**. The **UI checklist (§B.2)** is fallback only. **`--go-live`** (ENABLED = spend possible) only after explicit chat approval.
3. **Budgets & billing:** API script sets **daily budget** on create; agents must respect `--max-daily-budget-eur` and never raise spend without owner/PM consent. Account **payment method** remains with the business in Google’s billing UI.
4. **MCC / API Center:** developer token comes from a **manager account** API Center when required; client accounts still hold campaigns and conversions.
5. **No PO busywork:** when `secrets/google-ads.env` exists in the workspace, agents run read/write scripts themselves; only escalate to humans for missing credentials on that machine, billing, policy blocks, or **explicit spend approval** — not for “please run this command and paste output”.

---

## A. Google Analytics 4 ↔ Google Ads (do this before scaling spend)

| # | Action | Why |
|---|--------|-----|
| 1 | **GA4 Admin → Product links → Google Ads links** — link the Ads account to the GA4 property used for vlwarmte.nl. | Shared audiences, imported GA conversions (optional), cross-reporting. |
| 2 | **Google Ads → Tools & settings → Linked accounts → Google Analytics (GA4)** — confirm the property link. | Bidirectional trust; consistent identity where Google supports it. |
| 3 | **Google Ads → Admin → Account settings → Auto-tagging** — enable **auto-tagging** (`gclid`). | Attribution of sessions from Ads into GA4. |
| 4 | **GA4 — mark key events** as conversions: e.g. `contact_submit`, `lead_form_submit`, `wizard_lead_submit`, `wizard_calculate`, meaningful calculator steps (see `AGENTS.md` / site code). | Optimization signals; optional import into Ads as **primary/secondary** conversions per strategy. |
| 5 | **Google Ads → Goals → Conversions** — use **website** conversions that match the same fired tags / Google tag configuration as the site; align names with GA4 where helpful. | Bidding and “Maximize conversions” style goals need trustworthy conversion volume. |
| 6 | **Consent / EEA** — if applicable, keep consent mode and Ads remarketing policies aligned with site implementation. | Legal + data quality. |

**Data the PM/marketing agent should use:** `docs/website-manager/analytics_report.md`, gitignored `docs/website-manager/ga4_report.json` (from `scripts/ga4_fetch.py` when run locally), and **Google Ads** change history / search terms (UI or future read-only GAQL).

---

## B.1 Automated lead campaign (preferred when repo + secrets are available)

1. Tune copy/URLs/keywords in **`scripts/data/google_ads_lead_campaign_defaults.json`** (committed; PR-style edits).
2. Ensure `GOOGLE_ADS_CUSTOMER_ID` is set in `secrets/google-ads.env`.
3. Agent runs: `python scripts/google_ads_create_search_campaign.py --dry-run --daily-budget-eur <N> --campaign-name "<label>"`.
4. After validation, same command with **`--apply`**. Campaign stays **PAUSED** unless **`--go-live`** is used.
5. **GA4 ↔ Ads linking** (§A) should already be in progress or done so conversions feed optimization.
6. **Optional — second RSA:** after you know the numeric **`--campaign-id`** (from `google_ads_list_campaigns.py`), run `python scripts/google_ads_add_rsa_variant.py --dry-run --campaign-id <id>` then **`--apply`**. Copy lives under **`extra_rsa`** in the same defaults JSON; improves **ad strength** / headline–description variety in Search.

## B.2 Campaign setup (UI checklist — fallback)

Use this structure for **Search** campaigns unless strategy dictates otherwise.

1. **Campaign goal:** Leads / Phone calls / Contact form — match to conversion actions in §A.
2. **Campaign type:** Search (good control for local service intent); consider PMax only with clear asset groups and monitoring.
3. **Geo:** radius + cities aligned with **AGENTS / marketing playbook** (Noord-Nederland, ~50 km Zuid-Laren); exclude irrelevant regions.
4. **Languages:** Dutch; match ad copy to landing language.
5. **Networks:** Search partners optional; **disable Display inside Search** if you want pure search control (Display via separate campaigns if needed).
6. **Ad groups:** tight themes (e.g. “vloerverwarming + stad”, “schuimbeton + regio”, “renovatie / nieuwbouw”); **10–20 keywords** per group where possible; **negative keywords** list from research (jobs, DIY-only, wrong provinces).
7. **Ads:** RSAs with **up to 15 headlines and 4 descriptions** (30 / 90 character limits) where possible, stressing local vakmanschap, traject (ondervloer/schuimbeton), CTA; add a **second RSA** in the same ad group for more combinations. Use **sitelinks** to `prijsindicatie.html`, `werkwijze.html`, `contact.html` with correct deep links.
8. **Final URLs & tracking:** every ad group or ad variant should map to a **purpose-built URL** (see §C). Enable **upgraded URLs** / tracking templates only if the account uses them consistently.
9. **Budget & bidding:** start conservative daily budget; **Maximize clicks** only short warm-up, then **Maximize conversions** (or tCPA) once conversion volume is trustworthy.
10. **Review:** search terms report weekly; add negatives; pause low-intent queries.

---

## C. Landing pages & “specialized” experiences for Ads

**Principles**

- **Intent match:** high commercial intent → `contact.html?modus=offerte#aanvraag` or `prijsindicatie.html`; research intent → `diensten.html` / `werkwijze.html` with clear secondary CTA to contact.
- **Stable tracking:** use **UTM parameters** for non-Google channels; for Google Ads rely on **auto-tagging** for GA4, but you may still add **utm_campaign** for internal clarity in GA4 explorations (avoid duplicate parameter chaos—one convention per account).
- **Dedicated landings:** when Analytics shows a **cluster** (e.g. high engagement from “schuimbeton + Groningen” but low conversion), propose a **single focused HTML page** or a **section variant** in an existing page—route only those ad groups there. Hand off to **Developer Agent** in `sprint.md` with acceptance criteria and measurement (event + conversion).
- **Feedback loop:** monthly (or post-sprint): compare **GA4 landing engagement + Ads search terms + form submits** → adjust ad copy, negatives, and landing above-the-fold; document in `research_report.md` / sprint notes—not new standalone docs unless the user allows.

**Contact deep links (site):** `https://www.vlwarmte.nl/contact.html?modus=informatie|offerte|bel#aanvraag` (see `AGENTS.md`).

---

## D. Closed loop: “use all data to influence campaigns”

1. **Analytics Agent** — baseline funnels, landing performance, device/geo, events.
2. **Marketing Research Agent** — keywords, competitors, **Ads structure** + **UTM / URL map** + creative hypotheses tied to analytics gaps.
3. **Social Agent** — organic/paid social angles that echo proven messaging from Ads/GA4 (no channel silos).
4. **PM** — prioritizes **lead impact**; can explicitly instruct Marketing to **draft or launch** Ads changes and Developer to ship **landing experiments**.
5. **Developer** — implements HTML/JS/tracking changes; keeps events consistent with `AGENTS.md` naming where possible.

---

## E. Local scripts (repo root, `.venv`)

| Script | Role |
|--------|------|
| `python scripts/google_ads_smoke_test.py` | Auth sanity; lists accessible `customers/…`. |
| `python scripts/google_ads_print_customer_ids.py` | Prints **digits-only** customer ids (for `GOOGLE_ADS_CUSTOMER_ID`). **Not** `gcloud` — Ads ids come from the Ads API. |
| `python scripts/google_ads_campaign_next_steps.py` | **`negatives`** — add campaign negatives from `scripts/data/google_ads_campaign_negatives.json`. **`enable`** — set campaign **ENABLED** (spend can start). Use `--dry-run` / `--apply`; needs `--campaign-id` (from `list_campaigns`). |
| `python scripts/google_ads_list_campaigns.py` | Read-only campaign list: **id**, **advertising channel type** (e.g. `SEARCH`, `PERFORMANCE_MAX`), status, name. |
| `python scripts/google_ads_get_refresh_token.py` | OAuth path only if not using service-account JSON. |
| `python scripts/google_ads_create_search_campaign.py` | **Full lead Search setup in one mutate:** budget + **PAUSED** campaign + NL geo + **ad group** + **phrase keywords** + **RSA** (URLs/copy from `scripts/data/google_ads_lead_campaign_defaults.json`). Flow: **`--dry-run`** then **`--apply`**. Optional **`--go-live`** after apply sets campaign **ENABLED** (spend can start — use a low `--daily-budget-eur` at first). Hard cap `--max-daily-budget-eur` (default 100). Name prefix `VLW-API-`. **No Ads UI required** for this skeleton. |
| `python scripts/google_ads_add_rsa_variant.py` | Adds a **second responsive search ad** to the **first ad group** of an existing Search campaign (`--campaign-id`). Copy from **`extra_rsa`** in `google_ads_lead_campaign_defaults.json`. **`--dry-run`** / **`--apply`**. Not for Performance Max asset groups. |

For **new** read-only GAQL (search terms, impression share, conversion by campaign), add small scripts under `scripts/` following `google_ads_common.get_google_ads_client()` — prefer read-only until the user approves writes.

---

## F. API mutations (governed)

For **standard lead Search campaigns**, run **`google_ads_create_search_campaign.py --dry-run`**, report results, then **`--apply`** after PM/owner confirmation in chat. **`--go-live`** is an extra spend gate. For **non-standard** API edits, still document a change plan (resources, budgets, rollback) before mutating. Never hide spend side effects.

---

## References

- Google Ads API: https://developers.google.com/google-ads/api/docs/start  
- Link GA4 and Google Ads: https://support.google.com/google-ads/answer/7519530  
- GA4 conversions: https://support.google.com/analytics/answer/9267735  
- GAQL: https://developers.google.com/google-ads/api/docs/query/overview  
