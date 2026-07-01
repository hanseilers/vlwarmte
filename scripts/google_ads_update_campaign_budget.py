#!/usr/bin/env python3
"""
Update the **daily budget** (EUR) on the campaign budget linked to a Search campaign.

  .venv/bin/python scripts/google_ads_update_campaign_budget.py --dry-run --campaign-id 23834672782 --daily-budget-eur 2
  .venv/bin/python scripts/google_ads_update_campaign_budget.py --apply --campaign-id 23834672782 --daily-budget-eur 2

If --daily-budget-eur is omitted, uses `daily_budget_eur` from
`scripts/data/google_ads_lead_campaign_defaults.json` when present.

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


def _eur_to_micros(eur: float) -> int:
    return int(round(eur * 1_000_000))


def _fetch_budget_row(client, customer_id: str, campaign_id: str):
    gas = client.get_service("GoogleAdsService")
    q = f"""
        SELECT campaign.id, campaign.name, campaign.status,
               campaign_budget.resource_name, campaign_budget.amount_micros,
               campaign_budget.name
        FROM campaign
        WHERE campaign.id = {int(campaign_id)}
    """
    rows = list(gas.search(customer_id=customer_id, query=q))
    if not rows:
        return None
    return rows[0]


def main() -> int:
    p = argparse.ArgumentParser(description="Update daily campaign budget (EUR).")
    mode = p.add_mutually_exclusive_group(required=True)
    mode.add_argument("--dry-run", action="store_true")
    mode.add_argument("--apply", action="store_true")
    p.add_argument("--customer-id", default=None)
    p.add_argument("--campaign-id", required=True, help="Numeric campaign id.")
    p.add_argument("--daily-budget-eur", type=float, default=None)
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

    if not str(args.campaign_id).strip().isdigit():
        print("--campaign-id must be numeric.", file=sys.stderr)
        return 1

    daily_eur = args.daily_budget_eur
    if daily_eur is None:
        try:
            defaults = json.loads(Path(args.defaults_json).read_text(encoding="utf-8"))
            daily_eur = defaults.get("daily_budget_eur")
        except (OSError, json.JSONDecodeError):
            daily_eur = None
    if daily_eur is None:
        print("Pass --daily-budget-eur or set daily_budget_eur in defaults JSON.", file=sys.stderr)
        return 1
    if daily_eur <= 0:
        print("--daily-budget-eur must be positive.", file=sys.stderr)
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

    row = _fetch_budget_row(client, cid, str(args.campaign_id).strip())
    if row is None:
        print("Campaign not found:", args.campaign_id, file=sys.stderr)
        return 1

    budget_rn = row.campaign_budget.resource_name
    before_micros = row.campaign_budget.amount_micros
    before_eur = before_micros / 1_000_000
    after_micros = _eur_to_micros(daily_eur)

    print("Campaign:", row.campaign.name, f"(id {row.campaign.id}, {row.campaign.status.name})")
    print("Budget resource:", budget_rn)
    print("Budget name:", row.campaign_budget.name)
    print(f"Current daily budget: EUR {before_eur:.2f}")
    print(f"Target daily budget: EUR {daily_eur:.2f}")

    if before_micros == after_micros:
        print("No change needed — already at target.")
        return 0

    mo = client.get_type("MutateOperation")
    mo.campaign_budget_operation.update.resource_name = budget_rn
    mo.campaign_budget_operation.update.amount_micros = after_micros
    mo.campaign_budget_operation.update_mask.paths.append("amount_micros")

    req = client.get_type("MutateGoogleAdsRequest")
    req.customer_id = cid
    req.mutate_operations.append(mo)
    req.validate_only = bool(args.dry_run)

    label = "DRY-RUN" if args.dry_run else "APPLY"
    print("budget", label, f"EUR {before_eur:.2f} -> EUR {daily_eur:.2f}")
    try:
        client.get_service("GoogleAdsService").mutate(request=req)
    except GoogleAdsException as exc:
        print(str(exc).split("\n", 1)[0], file=sys.stderr)
        if getattr(exc, "failure", None) and exc.failure.errors:
            for e in exc.failure.errors:
                print(" ", e.message, file=sys.stderr)
        return 1

    print("OK — validation passed." if args.dry_run else "OK — budget updated.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
