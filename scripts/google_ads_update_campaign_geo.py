#!/usr/bin/env python3
"""
Replace **positive LOCATION** campaign criteria with the list from
`scripts/data/google_ads_lead_campaign_defaults.json` → `location_targeting.geo_target_constants`.

Use after narrowing targeting (e.g. NL-wide → northern provinces) without recreating the campaign.

  python scripts/google_ads_update_campaign_geo.py --dry-run --campaign-id 23834672782
  python scripts/google_ads_update_campaign_geo.py --apply --campaign-id 23834672782

Requires: secrets/google-ads.env, GOOGLE_ADS_CUSTOMER_ID, service account access.
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


def _geo_targets(defaults: dict) -> list[str]:
    loc = defaults.get("location_targeting") or {}
    raw = loc.get("geo_target_constants") or []
    if not isinstance(raw, list):
        return []
    return [str(x).strip() for x in raw if str(x).strip()]


def main() -> int:
    p = argparse.ArgumentParser(description="Replace campaign location criteria from defaults JSON.")
    mode = p.add_mutually_exclusive_group(required=True)
    mode.add_argument("--dry-run", action="store_true")
    mode.add_argument("--apply", action="store_true")
    p.add_argument("--customer-id", default=None)
    p.add_argument("--campaign-id", required=True, help="Numeric campaign id.")
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
        defaults = json.loads(Path(args.defaults_json).read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print("Bad defaults JSON:", exc, file=sys.stderr)
        return 1

    new_geos = _geo_targets(defaults)
    if not new_geos:
        print("location_targeting.geo_target_constants is empty in defaults.", file=sys.stderr)
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
    camp_id = str(int(args.campaign_id))
    campaign_rn = gas.campaign_path(cid, camp_id)

    q = f"""
        SELECT campaign_criterion.resource_name, campaign_criterion.location.geo_target_constant
        FROM campaign_criterion
        WHERE campaign.id = {camp_id}
          AND campaign_criterion.type = LOCATION
          AND campaign_criterion.negative = FALSE
    """
    to_remove: list[str] = []
    for row in gas.search(customer_id=cid, query=q):
        to_remove.append(row.campaign_criterion.resource_name)

    print("Campaign:", campaign_rn)
    print("Remove", len(to_remove), "existing LOCATION criterion/criteria")
    for rn in to_remove:
        print(" ", rn)
    print("Add", len(new_geos), "location target(s):")
    for g in new_geos:
        print(" ", g)

    ops: list = []
    for rn in to_remove:
        mo = client.get_type("MutateOperation")
        mo.campaign_criterion_operation.remove = rn
        ops.append(mo)

    for geo in new_geos:
        mo = client.get_type("MutateOperation")
        cc = mo.campaign_criterion_operation.create
        cc.campaign = campaign_rn
        cc.location.geo_target_constant = geo
        ops.append(mo)

    req = client.get_type("MutateGoogleAdsRequest")
    req.customer_id = cid
    req.mutate_operations.extend(ops)
    req.validate_only = bool(args.dry_run)

    try:
        gas.mutate(request=req)
    except GoogleAdsException as exc:
        print(str(exc).split("\n", 1)[0], file=sys.stderr)
        if getattr(exc, "failure", None) and exc.failure.errors:
            for e in exc.failure.errors:
                print(" ", e.message, file=sys.stderr)
        return 1

    if args.dry_run:
        print("OK — validation passed.")
    else:
        print("OK — campaign location targeting updated.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
