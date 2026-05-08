#!/usr/bin/env python3
"""
Post-create Google Ads steps: enable a PAUSED campaign and/or add campaign negatives.

  # Add negatives (while paused or enabled)
  python scripts/google_ads_campaign_next_steps.py negatives --dry-run --campaign-id 123456789
  python scripts/google_ads_campaign_next_steps.py negatives --apply --campaign-id 123456789

  # Enable campaign (ads can serve — spend starts within daily budget)
  python scripts/google_ads_campaign_next_steps.py enable --dry-run --campaign-id 123456789
  python scripts/google_ads_campaign_next_steps.py enable --apply --campaign-id 123456789

Customer id: GOOGLE_ADS_CUSTOMER_ID or --customer-id.
Negatives list: scripts/data/google_ads_campaign_negatives.json
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

_NEGATIVES_FILE = _SCRIPTS_DIR / "data" / "google_ads_campaign_negatives.json"


def _cid(args) -> str | None:
    import os

    prepare_google_ads_env()
    raw = (args.customer_id or os.environ.get("GOOGLE_ADS_CUSTOMER_ID") or "").strip()
    cid = normalize_customer_id(raw)
    if len(cid) != 10:
        return None
    return cid


def _match_type(client, name: str):
    n = (name or "BROAD").upper()
    m = client.enums.KeywordMatchTypeEnum
    if n == "PHRASE":
        return m.PHRASE
    if n == "EXACT":
        return m.EXACT
    return m.BROAD


def cmd_enable(args) -> int:
    cid = _cid(args)
    if not cid:
        print("Need --customer-id or GOOGLE_ADS_CUSTOMER_ID.", file=sys.stderr)
        return 1
    if not str(args.campaign_id).strip().isdigit():
        print("--campaign-id must be numeric.", file=sys.stderr)
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
    campaign_rn = gas.campaign_path(cid, str(args.campaign_id).strip())

    mo = client.get_type("MutateOperation")
    mo.campaign_operation.update.resource_name = campaign_rn
    mo.campaign_operation.update.status = client.enums.CampaignStatusEnum.ENABLED
    mo.campaign_operation.update_mask.paths.append("status")

    req = client.get_type("MutateGoogleAdsRequest")
    req.customer_id = cid
    req.mutate_operations.append(mo)
    req.validate_only = bool(args.dry_run)

    print("enable", "DRY-RUN" if args.dry_run else "APPLY", "campaign", campaign_rn)
    try:
        gas.mutate(request=req)
    except GoogleAdsException as exc:
        print(str(exc).split("\n", 1)[0], file=sys.stderr)
        if getattr(exc, "failure", None) and exc.failure.errors:
            for e in exc.failure.errors:
                print(" ", e.message, file=sys.stderr)
        return 1

    print("OK — campaign ENABLED." if not args.dry_run else "OK — validation passed.")
    return 0


def cmd_negatives(args) -> int:
    cid = _cid(args)
    if not cid:
        print("Need --customer-id or GOOGLE_ADS_CUSTOMER_ID.", file=sys.stderr)
        print("See:", google_ads_env_path(), file=sys.stderr)
        return 1
    if not str(args.campaign_id).strip().isdigit():
        print("--campaign-id must be numeric.", file=sys.stderr)
        return 1

    path = Path(args.negatives_json) if args.negatives_json else _NEGATIVES_FILE
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print("Cannot read negatives JSON:", exc, file=sys.stderr)
        return 1

    rows = data.get("negatives") or []
    if not rows:
        print("No negatives in JSON.", file=sys.stderr)
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
    campaign_rn = gas.campaign_path(cid, str(args.campaign_id).strip())

    ops = []
    temp = -100
    for row in rows:
        text = (row.get("text") or "").strip()
        if not text:
            continue
        mo = client.get_type("MutateOperation")
        cr = mo.campaign_criterion_operation.create
        cr.resource_name = gas.campaign_criterion_path(cid, str(args.campaign_id).strip(), str(temp))
        temp -= 1
        cr.campaign = campaign_rn
        cr.negative = True
        cr.keyword.text = text
        cr.keyword.match_type = _match_type(client, row.get("match", "BROAD"))
        cr.status = client.enums.CampaignCriterionStatusEnum.ENABLED
        ops.append(mo)

    if not ops:
        print("Nothing to add.", file=sys.stderr)
        return 1

    req = client.get_type("MutateGoogleAdsRequest")
    req.customer_id = cid
    req.mutate_operations.extend(ops)
    req.validate_only = bool(args.dry_run)

    print("negatives", "DRY-RUN" if args.dry_run else "APPLY", len(ops), "criteria for", campaign_rn)
    try:
        client.get_service("GoogleAdsService").mutate(request=req)
    except GoogleAdsException as exc:
        print(str(exc).split("\n", 1)[0], file=sys.stderr)
        if getattr(exc, "failure", None) and exc.failure.errors:
            for e in exc.failure.errors:
                print(" ", e.message, file=sys.stderr)
        return 1

    print("OK — negatives added." if not args.dry_run else "OK — validation passed.")
    return 0


def main() -> int:
    p = argparse.ArgumentParser(description="Google Ads post-launch helpers.")
    sub = p.add_subparsers(dest="cmd", required=True)

    pe = sub.add_parser("enable", help="Set campaign status to ENABLED.")
    mode = pe.add_mutually_exclusive_group(required=True)
    mode.add_argument("--dry-run", action="store_true")
    mode.add_argument("--apply", action="store_true")
    pe.add_argument("--customer-id", default=None)
    pe.add_argument("--campaign-id", required=True, help="Numeric campaign id from list_campaigns.")
    pe.set_defaults(func=cmd_enable)

    pn = sub.add_parser("negatives", help="Add campaign-level negative keywords from JSON.")
    mod2 = pn.add_mutually_exclusive_group(required=True)
    mod2.add_argument("--dry-run", action="store_true")
    mod2.add_argument("--apply", action="store_true")
    pn.add_argument("--customer-id", default=None)
    pn.add_argument("--campaign-id", required=True)
    pn.add_argument("--negatives-json", type=Path, default=None)
    pn.set_defaults(func=cmd_negatives)

    args = p.parse_args()
    return int(args.func(args))


if __name__ == "__main__":
    raise SystemExit(main())
