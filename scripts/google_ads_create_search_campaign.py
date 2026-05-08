#!/usr/bin/env python3
"""
Create a **lead-ready Search campaign** in one or two API steps — no Google Ads UI required.

Creates (single GoogleAdsService.mutate, grouped by resource type):
  - Daily budget
  - Search campaign (PAUSED by default so nothing serves until you choose)
  - Netherlands geo
  - One ad group (SEARCH_STANDARD) with default CPC bid
  - Phrase keywords (from JSON)
  - One responsive search ad (RSA) with final URLs from JSON

Defaults live in: scripts/data/google_ads_lead_campaign_defaults.json (committed; edit there for copy/keywords).

Safety:
  - Exactly one of --dry-run or --apply.
  - --apply blocks if daily budget > --max-daily-budget-eur (default 100).
  - Campaign name prefix GOOGLE_ADS_CAMPAIGN_PREFIX (default VLW-API-).
  - Optional --go-live: after a successful --apply, sets campaign status ENABLED (spend can start — use with a low daily budget).

Typical agent flow (no Ads knowledge needed from business owner):
  1) python scripts/google_ads_create_search_campaign.py --dry-run --daily-budget-eur 20 --campaign-name "Noord NL leads"
  2) python scripts/google_ads_create_search_campaign.py --apply  --daily-budget-eur 20 --campaign-name "Noord NL leads"
  3) optionally: same with --go-live to start serving.

Prerequisites: secrets/google-ads.env + service account invited in Ads (see google-ads.env.example).
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

_SCRIPTS_DIR = Path(__file__).resolve().parent
if str(_SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(_SCRIPTS_DIR))

from google_ads_common import (  # noqa: E402
    get_google_ads_client,
    google_ads_env_path,
    normalize_customer_id,
    prepare_google_ads_env,
)

_DATA_FILE = _SCRIPTS_DIR / "data" / "google_ads_lead_campaign_defaults.json"
_GEO_TARGET_NETHERLANDS = "geoTargetConstants/2528"
# Temporary negative IDs (must be unique within one mutate request)
_BUDGET_TEMP = "-1"
_CAMPAIGN_TEMP = "-2"
_AD_GROUP_TEMP = "-3"
_AD_TEMP = "-20"


def _eur_to_micros(eur: float) -> int:
    return int(round(eur * 1_000_000))


def _campaign_display_name(raw: str, prefix: str) -> str:
    raw = raw.strip()
    if not raw:
        raise ValueError("campaign name empty")
    if not raw.startswith(prefix):
        return f"{prefix}{raw}"
    return raw


def _load_defaults() -> dict:
    if not _DATA_FILE.is_file():
        raise FileNotFoundError(f"Missing defaults file: {_DATA_FILE}")
    return json.loads(_DATA_FILE.read_text(encoding="utf-8"))


def _match_type_enum(client, name: str):
    n = (name or "PHRASE").upper().strip()
    m = client.enums.KeywordMatchTypeEnum
    if n == "BROAD":
        return m.BROAD
    if n == "EXACT":
        return m.EXACT
    return m.PHRASE


def _build_full_mutate_operations(
    client,
    customer_id: str,
    campaign_name: str,
    budget_micros: int,
    defaults: dict,
    ad_group_cpc_micros: int,
) -> list:
    gas = client.get_service("GoogleAdsService")

    mo_budget = client.get_type("MutateOperation")
    b_create = mo_budget.campaign_budget_operation.create
    b_create.resource_name = gas.campaign_budget_path(customer_id, _BUDGET_TEMP)
    b_create.name = f"{campaign_name} — budget"
    b_create.delivery_method = client.enums.BudgetDeliveryMethodEnum.STANDARD
    b_create.amount_micros = budget_micros

    mo_c = client.get_type("MutateOperation")
    c_create = mo_c.campaign_operation.create
    c_create.resource_name = gas.campaign_path(customer_id, _CAMPAIGN_TEMP)
    c_create.name = campaign_name
    c_create.advertising_channel_type = client.enums.AdvertisingChannelTypeEnum.SEARCH
    c_create.status = client.enums.CampaignStatusEnum.PAUSED
    c_create.manual_cpc = client.get_type("ManualCpc")
    c_create.campaign_budget = b_create.resource_name
    c_create.network_settings.target_google_search = True
    c_create.network_settings.target_search_network = True
    c_create.network_settings.target_partner_search_network = False
    c_create.network_settings.target_content_network = False
    c_create.contains_eu_political_advertising = (
        client.enums.EuPoliticalAdvertisingStatusEnum.DOES_NOT_CONTAIN_EU_POLITICAL_ADVERTISING
    )

    mo_geo = client.get_type("MutateOperation")
    geo_create = mo_geo.campaign_criterion_operation.create
    geo_create.campaign = c_create.resource_name
    geo_create.location.geo_target_constant = _GEO_TARGET_NETHERLANDS

    mo_ag = client.get_type("MutateOperation")
    ag_create = mo_ag.ad_group_operation.create
    ag_create.resource_name = gas.ad_group_path(customer_id, _AD_GROUP_TEMP)
    ag_create.name = f"{campaign_name} — {defaults.get('ad_group_suffix', 'Leads')}"
    ag_create.campaign = c_create.resource_name
    ag_create.type_ = client.enums.AdGroupTypeEnum.SEARCH_STANDARD
    ag_create.status = client.enums.AdGroupStatusEnum.ENABLED
    ag_create.cpc_bid_micros = ad_group_cpc_micros

    ops: list = [mo_budget, mo_c, mo_geo, mo_ag]

    kw_temp_id = -4
    for row in defaults.get("keywords", []):
        text = (row.get("text") or "").strip()
        if not text:
            continue
        mo_kw = client.get_type("MutateOperation")
        kc = mo_kw.ad_group_criterion_operation.create
        kc.resource_name = gas.ad_group_criterion_path(
            customer_id, _AD_GROUP_TEMP, str(kw_temp_id)
        )
        kw_temp_id -= 1
        kc.ad_group = ag_create.resource_name
        kc.status = client.enums.AdGroupCriterionStatusEnum.ENABLED
        kc.negative = False
        kc.keyword.text = text
        kc.keyword.match_type = _match_type_enum(client, row.get("match", "PHRASE"))
        ops.append(mo_kw)

    mo_ad = client.get_type("MutateOperation")
    adga = mo_ad.ad_group_ad_operation.create
    adga.resource_name = gas.ad_group_ad_path(customer_id, _AD_GROUP_TEMP, _AD_TEMP)
    adga.ad_group = ag_create.resource_name
    adga.status = client.enums.AdGroupAdStatusEnum.ENABLED
    ad = adga.ad
    for u in defaults.get("final_urls", []):
        u = (u or "").strip()
        if u:
            ad.final_urls.append(u)
    rsa = ad.responsive_search_ad
    for h in defaults.get("headlines", []):
        h = (h or "").strip()[:30]
        if not h:
            continue
        asset = client.get_type("AdTextAsset")
        asset.text = h
        rsa.headlines.append(asset)
    for d in defaults.get("descriptions", []):
        d = (d or "").strip()[:90]
        if not d:
            continue
        asset = client.get_type("AdTextAsset")
        asset.text = d
        rsa.descriptions.append(asset)
    p1 = (defaults.get("path1") or "").strip()[:15]
    p2 = (defaults.get("path2") or "").strip()[:15]
    if p1:
        rsa.path1 = p1
    if p2:
        rsa.path2 = p2

    ops.append(mo_ad)
    return ops


def _enable_campaign(client, customer_id: str, campaign_resource_name: str, validate_only: bool) -> None:
    camp_svc = client.get_service("CampaignService")
    op = client.get_type("CampaignOperation")
    op.update.resource_name = campaign_resource_name
    op.update.status = client.enums.CampaignStatusEnum.ENABLED
    op.update_mask.paths.append("status")
    req = client.get_type("MutateCampaignsRequest")
    req.customer_id = customer_id
    req.operations.append(op)
    req.validate_only = validate_only
    camp_svc.mutate_campaigns(request=req)


def main() -> int:
    p = argparse.ArgumentParser(
        description="Create a full paused Search lead campaign (budget, geo, ad group, keywords, RSA)."
    )
    mode = p.add_mutually_exclusive_group(required=True)
    mode.add_argument("--dry-run", action="store_true", help="Validate only (no changes).")
    mode.add_argument("--apply", action="store_true", help="Create resources in Google Ads.")
    p.add_argument("--customer-id", help="10-digit customer id (else GOOGLE_ADS_CUSTOMER_ID).")
    p.add_argument(
        "--daily-budget-eur",
        type=float,
        required=True,
        help="Daily budget in EUR (account currency assumed EUR).",
    )
    p.add_argument("--campaign-name", required=True, help="Campaign label (prefix applied).")
    p.add_argument("--max-daily-budget-eur", type=float, default=100.0)
    p.add_argument("--campaign-prefix", default=None)
    p.add_argument(
        "--defaults-json",
        type=Path,
        default=_DATA_FILE,
        help="Path to keyword/headline/url JSON (default: bundled scripts/data/…).",
    )
    p.add_argument(
        "--ad-group-cpc-eur",
        type=float,
        default=0.5,
        help="Default max CPC per click for the ad group (EUR, default 0.5).",
    )
    p.add_argument(
        "--go-live",
        action="store_true",
        help="After successful --apply, enable the campaign so ads can serve (spend starts). Ignored for --dry-run.",
    )
    args = p.parse_args()

    import os

    prepare_google_ads_env()
    raw_cid = (args.customer_id or os.environ.get("GOOGLE_ADS_CUSTOMER_ID") or "").strip()
    customer_id = normalize_customer_id(raw_cid)
    if len(customer_id) != 10:
        print("Need --customer-id or GOOGLE_ADS_CUSTOMER_ID (10 digits).", file=sys.stderr)
        print("See:", google_ads_env_path(), file=sys.stderr)
        return 1

    prefix = (args.campaign_prefix or os.environ.get("GOOGLE_ADS_CAMPAIGN_PREFIX") or "VLW-API-").strip()
    if prefix and not prefix.endswith("-"):
        prefix = f"{prefix}-"

    try:
        campaign_name = _campaign_display_name(args.campaign_name, prefix)
    except ValueError as exc:
        print(exc, file=sys.stderr)
        return 1

    if args.daily_budget_eur <= 0:
        print("--daily-budget-eur must be positive.", file=sys.stderr)
        return 1

    if args.apply and args.daily_budget_eur > args.max_daily_budget_eur:
        print(
            f"--apply blocked: daily budget {args.daily_budget_eur} EUR exceeds "
            f"--max-daily-budget-eur {args.max_daily_budget_eur}.",
            file=sys.stderr,
        )
        return 1

    try:
        defaults = json.loads(Path(args.defaults_json).read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print("Could not read defaults JSON:", exc, file=sys.stderr)
        return 1

    budget_micros = _eur_to_micros(args.daily_budget_eur)
    ad_group_cpc_micros = _eur_to_micros(args.ad_group_cpc_eur)

    try:
        client = get_google_ads_client()
    except RuntimeError as exc:
        print(exc, file=sys.stderr)
        return 1

    try:
        from google.ads.googleads.errors import GoogleAdsException
    except ImportError:
        GoogleAdsException = Exception  # type: ignore[misc,assignment]

    ops = _build_full_mutate_operations(
        client, customer_id, campaign_name, budget_micros, defaults, ad_group_cpc_micros
    )
    gas = client.get_service("GoogleAdsService")
    req = client.get_type("MutateGoogleAdsRequest")
    req.customer_id = customer_id
    req.mutate_operations.extend(ops)
    req.validate_only = bool(args.dry_run)

    print("Mode:", "DRY-RUN (validate_only)" if args.dry_run else "APPLY")
    print("Customer:", customer_id)
    print("Campaign name:", campaign_name)
    print("Daily budget (EUR):", args.daily_budget_eur)
    print("Ad group default CPC (EUR):", args.ad_group_cpc_eur)
    print("Defaults file:", args.defaults_json)
    if args.go_live and args.apply:
        print("--go-live: campaign will be set to ENABLED after create.")

    try:
        response = gas.mutate(request=req)
    except GoogleAdsException as exc:
        print("Mutate failed:", str(exc).split("\n", 1)[0], file=sys.stderr)
        if getattr(exc, "failure", None) and exc.failure.errors:
            for err in exc.failure.errors:
                print(" ", err.message, file=sys.stderr)
        return 1
    except Exception as exc:  # noqa: BLE001
        print("Mutate failed:", exc, file=sys.stderr)
        return 1

    if args.dry_run:
        print("OK — validation passed; nothing created.")
        if args.go_live:
            print("(Note: --go-live only runs after a real --apply.)")
        return 0

    campaign_rn = ""
    for res in response.mutate_operation_responses:
        which = res._pb.WhichOneof("response")
        if which == "campaign_budget_result" and res.campaign_budget_result.resource_name:
            print("Budget:", res.campaign_budget_result.resource_name)
        elif which == "campaign_result" and res.campaign_result.resource_name:
            campaign_rn = res.campaign_result.resource_name
            print("Campaign:", campaign_rn)
        elif which == "campaign_criterion_result" and res.campaign_criterion_result.resource_name:
            print("Geo criterion:", res.campaign_criterion_result.resource_name)
        elif which == "ad_group_result" and res.ad_group_result.resource_name:
            print("Ad group:", res.ad_group_result.resource_name)
        elif which == "ad_group_criterion_result" and res.ad_group_criterion_result.resource_name:
            print("Keyword:", res.ad_group_criterion_result.resource_name)
        elif which == "ad_group_ad_result" and res.ad_group_ad_result.resource_name:
            print("Ad:", res.ad_group_ad_result.resource_name)

    if args.go_live and campaign_rn:
        try:
            _enable_campaign(client, customer_id, campaign_rn, validate_only=False)
            print("Campaign status set to ENABLED (--go-live). Review spend in Google Ads.")
        except GoogleAdsException as exc:
            print("Enable campaign failed:", str(exc).split("\n", 1)[0], file=sys.stderr)
            if getattr(exc, "failure", None) and exc.failure.errors:
                for err in exc.failure.errors:
                    print(" ", err.message, file=sys.stderr)
            return 1
    elif not args.go_live:
        print("Campaign left PAUSED — no spend until you run with --go-live or enable in Ads.")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
