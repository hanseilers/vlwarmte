#!/usr/bin/env python3
"""
Add a **second responsive search ad** to the first ad group of a Search campaign.

Improves Google’s “ad strength” / variety when the UI warns about limited assets.
Does not apply to Performance Max “asset groups” — those are a different campaign type.

  python scripts/google_ads_add_rsa_variant.py --dry-run --campaign-id 123456789
  python scripts/google_ads_add_rsa_variant.py --apply --campaign-id 123456789

Copy for headlines/descriptions: scripts/data/google_ads_lead_campaign_defaults.json → key `extra_rsa`.
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

_DEFAULTS = _SCRIPTS_DIR / "data" / "google_ads_lead_campaign_defaults.json"
_AD_TEMP = "-30"


def main() -> int:
    p = argparse.ArgumentParser(description="Add second RSA to first ad group of a campaign.")
    mode = p.add_mutually_exclusive_group(required=True)
    mode.add_argument("--dry-run", action="store_true")
    mode.add_argument("--apply", action="store_true")
    p.add_argument("--customer-id", default=None)
    p.add_argument("--campaign-id", required=True, help="Numeric campaign id (from list_campaigns).")
    p.add_argument("--defaults-json", type=Path, default=_DEFAULTS)
    args = p.parse_args()

    import os

    prepare_google_ads_env()
    raw = (args.customer_id or os.environ.get("GOOGLE_ADS_CUSTOMER_ID") or "").strip()
    cid = normalize_customer_id(raw)
    if len(cid) != 10:
        print("Need --customer-id or GOOGLE_ADS_CUSTOMER_ID.", file=sys.stderr)
        print("See:", google_ads_env_path(), file=sys.stderr)
        return 1

    try:
        data = json.loads(Path(args.defaults_json).read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print("Bad defaults JSON:", exc, file=sys.stderr)
        return 1

    extra = data.get("extra_rsa") or {}
    headlines = [str(h).strip()[:30] for h in extra.get("headlines", []) if str(h).strip()]
    descs = [str(d).strip()[:90] for d in extra.get("descriptions", []) if str(d).strip()]
    if len(headlines) < 3 or len(descs) < 2:
        print("extra_rsa needs at least 3 headlines and 2 descriptions.", file=sys.stderr)
        return 1

    finals = [u.strip() for u in data.get("final_urls", []) if u and str(u).strip()]
    if not finals:
        print("defaults missing final_urls.", file=sys.stderr)
        return 1

    try:
        client = get_google_ads_client()
    except RuntimeError as exc:
        print(exc, file=sys.stderr)
        return 1

    try:
        from google.ads.googleads.errors import GoogleAdsException
    except ImportError:
        GoogleAdsException = Exception  # type: ignore[misc,assignment]

    gas = client.get_service("GoogleAdsService")
    q = f"""
        SELECT ad_group.resource_name, ad_group.id
        FROM ad_group
        WHERE campaign.id = {int(args.campaign_id)}
          AND ad_group.status != 'REMOVED'
        ORDER BY ad_group.id
        LIMIT 1
    """
    ag_rn = None
    ag_id: str | None = None
    for row in gas.search(customer_id=cid, query=q):
        ag_rn = row.ad_group.resource_name
        ag_id = str(row.ad_group.id)
        break
    if not ag_rn or not ag_id:
        print("No ad group found for campaign id.", file=sys.stderr)
        return 1

    mo = client.get_type("MutateOperation")
    adga = mo.ad_group_ad_operation.create
    adga.resource_name = gas.ad_group_ad_path(cid, ag_id, _AD_TEMP)
    adga.ad_group = ag_rn
    adga.status = client.enums.AdGroupAdStatusEnum.ENABLED
    ad = adga.ad
    for u in finals:
        ad.final_urls.append(u)
    rsa = ad.responsive_search_ad
    for h in headlines:
        a = client.get_type("AdTextAsset")
        a.text = h
        rsa.headlines.append(a)
    for d in descs:
        a = client.get_type("AdTextAsset")
        a.text = d
        rsa.descriptions.append(a)
    p1 = (data.get("path1") or "").strip()[:15]
    p2 = (data.get("path2") or "").strip()[:15]
    if p1:
        rsa.path1 = p1
    if p2:
        rsa.path2 = p2

    req = client.get_type("MutateGoogleAdsRequest")
    req.customer_id = cid
    req.mutate_operations.append(mo)
    req.validate_only = bool(args.dry_run)

    print("Ad group:", ag_rn)
    print("Mode:", "DRY-RUN" if args.dry_run else "APPLY", "| extra RSA headlines:", len(headlines))
    try:
        res = gas.mutate(request=req)
    except GoogleAdsException as exc:
        print(str(exc).split("\n", 1)[0], file=sys.stderr)
        if getattr(exc, "failure", None) and exc.failure.errors:
            for e in exc.failure.errors:
                print(" ", e.message, file=sys.stderr)
        return 1

    if not args.dry_run:
        for r in res.mutate_operation_responses:
            if r._pb.WhichOneof("response") == "ad_group_ad_result" and r.ad_group_ad_result.resource_name:
                print("Created:", r.ad_group_ad_result.resource_name)
    else:
        print("OK — validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
