#!/usr/bin/env python3
"""
Add **sitelink assets** to a Search campaign from defaults JSON.

  python scripts/google_ads_add_sitelinks.py --dry-run --campaign-id 23834672782
  python scripts/google_ads_add_sitelinks.py --apply --campaign-id 23834672782

Copy: scripts/data/google_ads_lead_campaign_defaults.json → key `sitelinks`.
Skips apply when the campaign already has ≥2 enabled sitelinks (use --force to add anyway).
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
_ASSET_TEMP_START = -100


def _truncate(s: str, n: int) -> str:
    return (s or "").strip()[:n]


def _load_sitelinks(defaults: dict) -> list[dict]:
    raw = defaults.get("sitelinks") or []
    out: list[dict] = []
    for row in raw:
        if not isinstance(row, dict):
            continue
        link = _truncate(str(row.get("link_text", "")), 25)
        url = str(row.get("final_url", "")).strip()
        if not link or not url:
            continue
        out.append(
            {
                "link_text": link,
                "description1": _truncate(str(row.get("description1", "")), 35),
                "description2": _truncate(str(row.get("description2", "")), 35),
                "final_url": url,
            }
        )
    return out


def _count_existing_sitelinks(gas, cid: str, campaign_id: str) -> int:
    q = f"""
        SELECT campaign.id
        FROM campaign_asset
        WHERE campaign.id = {int(campaign_id)}
          AND campaign_asset.field_type = SITELINK
          AND campaign_asset.status != 'REMOVED'
    """
    n = 0
    for _ in gas.search(customer_id=cid, query=q):
        n += 1
    return n


def _build_operations(client, cid: str, campaign_id: str, sitelinks: list[dict]) -> list:
    gas = client.get_service("GoogleAdsService")
    campaign_rn = gas.campaign_path(cid, campaign_id)
    ops: list = []
    for i, sl in enumerate(sitelinks):
        temp = str(_ASSET_TEMP_START - i)
        mo_a = client.get_type("MutateOperation")
        asset = mo_a.asset_operation.create
        asset.resource_name = gas.asset_path(cid, temp)
        asset.sitelink_asset.link_text = sl["link_text"]
        if sl["description1"]:
            asset.sitelink_asset.description1 = sl["description1"]
        if sl["description2"]:
            asset.sitelink_asset.description2 = sl["description2"]
        asset.final_urls.append(sl["final_url"])
        ops.append(mo_a)

        mo_ca = client.get_type("MutateOperation")
        ca = mo_ca.campaign_asset_operation.create
        ca.campaign = campaign_rn
        ca.asset = asset.resource_name
        ca.field_type = client.enums.AssetFieldTypeEnum.SITELINK
        ops.append(mo_ca)
    return ops


def main() -> int:
    p = argparse.ArgumentParser(description="Add sitelink assets to a Search campaign.")
    mode = p.add_mutually_exclusive_group(required=True)
    mode.add_argument("--dry-run", action="store_true")
    mode.add_argument("--apply", action="store_true")
    p.add_argument("--customer-id", default=None)
    p.add_argument("--campaign-id", required=True, help="Numeric campaign id (from list_campaigns).")
    p.add_argument("--defaults-json", type=Path, default=_DEFAULTS)
    p.add_argument(
        "--force",
        action="store_true",
        help="Add sitelinks even when campaign already has ≥2 sitelinks.",
    )
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

    sitelinks = _load_sitelinks(data)
    if len(sitelinks) < 2:
        print("defaults `sitelinks` needs at least 2 entries with link_text + final_url.", file=sys.stderr)
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
    existing = _count_existing_sitelinks(gas, cid, args.campaign_id)
    if existing >= 2 and not args.force:
        print(
            f"Campaign already has {existing} sitelink(s). Use --force to add more, or manage in Ads UI.",
            file=sys.stderr,
        )
        return 1

    ops = _build_operations(client, cid, args.campaign_id, sitelinks)
    req = client.get_type("MutateGoogleAdsRequest")
    req.customer_id = cid
    for op in ops:
        req.mutate_operations.append(op)
    req.validate_only = bool(args.dry_run)

    print("Campaign id:", args.campaign_id)
    print("Mode:", "DRY-RUN" if args.dry_run else "APPLY", "| sitelinks:", len(sitelinks))
    for sl in sitelinks:
        print(f"  - {sl['link_text']} → {sl['final_url']}")

    try:
        res = gas.mutate(request=req)
    except GoogleAdsException as exc:
        print(str(exc).split("\n", 1)[0], file=sys.stderr)
        if getattr(exc, "failure", None) and exc.failure.errors:
            for e in exc.failure.errors:
                print(" ", e.message, file=sys.stderr)
        return 1

    if not args.dry_run:
        created = 0
        for r in res.mutate_operation_responses:
            if r._pb.WhichOneof("response") == "asset_result" and r.asset_result.resource_name:
                print("Asset:", r.asset_result.resource_name)
                created += 1
        print(f"OK — linked {len(sitelinks)} sitelink(s) to campaign.")
    else:
        print("OK — validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
