#!/usr/bin/env python3
"""
Print Google Ads customer IDs accessible to the current credentials (digits only).

Same auth as other Ads scripts (secrets/google-ads.env + service account invited in Ads).
Not gcloud — Google Cloud CLI does not expose Ads customer IDs.

  pip install -r scripts/requirements-google-ads.txt
  python scripts/google_ads_print_customer_ids.py

Copy a line into secrets/google-ads.env as GOOGLE_ADS_CUSTOMER_ID=...
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

_SCRIPTS_DIR = Path(__file__).resolve().parent
if str(_SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(_SCRIPTS_DIR))

from google_ads_common import get_google_ads_client  # noqa: E402


def main() -> int:
    try:
        client = get_google_ads_client()
    except RuntimeError as exc:
        print(exc, file=sys.stderr)
        return 1

    svc = client.get_service("CustomerService")
    try:
        response = svc.list_accessible_customers()
    except Exception as exc:  # noqa: BLE001
        print("list_accessible_customers failed:", exc, file=sys.stderr)
        return 1

    names = list(response.resource_names)
    if not names:
        print("No accessible customers.")
        return 0

    print("# Paste one into secrets/google-ads.env:")
    for n in names:
        m = re.search(r"customers/(\d+)", n)
        if m:
            print(m.group(1))
        else:
            print(n)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
