#!/usr/bin/env python3
"""
Read-only: list non-removed campaigns for a Google Ads customer (id, **channel type**
SEARCH / PERFORMANCE_MAX / …, status, name).

Customer id: 10 digits without dashes — pass --customer-id or set GOOGLE_ADS_CUSTOMER_ID
in secrets/google-ads.env. When using an MCC to access a client, set GOOGLE_ADS_LOGIN_CUSTOMER_ID.

  pip install -r scripts/requirements-google-ads.txt
  python scripts/google_ads_list_campaigns.py
  python scripts/google_ads_list_campaigns.py --customer-id 1234567890
"""

from __future__ import annotations

import argparse
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


def main() -> int:
    p = argparse.ArgumentParser(description="List Google Ads campaigns (read-only).")
    p.add_argument(
        "--customer-id",
        help="Ads customer id without dashes (default: GOOGLE_ADS_CUSTOMER_ID from env)",
    )
    args = p.parse_args()

    import os

    prepare_google_ads_env()
    raw = (args.customer_id or os.environ.get("GOOGLE_ADS_CUSTOMER_ID") or "").strip()
    cid = normalize_customer_id(raw)
    if len(cid) != 10:
        print(
            "Need a 10-digit customer id: --customer-id or GOOGLE_ADS_CUSTOMER_ID in",
            google_ads_env_path(),
            file=sys.stderr,
        )
        print(
            "Discover ids (no customer id needed): python scripts/google_ads_print_customer_ids.py",
            file=sys.stderr,
        )
        print("Then add one line: GOOGLE_ADS_CUSTOMER_ID=<10 digits>", file=sys.stderr)
        return 1

    try:
        client = get_google_ads_client()
    except RuntimeError as exc:
        print(exc, file=sys.stderr)
        return 1

    query = """
        SELECT
          campaign.id,
          campaign.name,
          campaign.status,
          campaign.advertising_channel_type
        FROM campaign
        WHERE campaign.status != 'REMOVED'
        ORDER BY campaign.name
    """
    ga = client.get_service("GoogleAdsService")
    print("id\tchannel_type\tstatus\tname")
    try:
        for row in ga.search(customer_id=cid, query=query):
            c = row.campaign
            ch = c.advertising_channel_type.name
            print(f"{c.id}\t{ch}\t{c.status.name}\t{c.name}")
    except Exception as exc:  # noqa: BLE001
        print("Search failed:", exc, file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
