#!/usr/bin/env python3
"""
Verify Google Ads API credentials: lists accessible customer resource names.

See scripts/google_ads_common.py and secrets/google-ads.env.example.

pip install -r scripts/requirements-google-ads.txt
"""

from __future__ import annotations

import sys
from pathlib import Path

_SCRIPTS_DIR = Path(__file__).resolve().parent
if str(_SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(_SCRIPTS_DIR))

from google_ads_common import get_google_ads_client, google_ads_env_path, prepare_google_ads_env


def main() -> int:
    import os

    prepare_google_ads_env()
    json_key = (os.environ.get("GOOGLE_ADS_JSON_KEY_FILE_PATH") or "").strip()
    json_ok = bool(json_key) and Path(json_key).is_file()
    oauth_ok = all(
        (os.environ.get(k) or "").strip()
        for k in (
            "GOOGLE_ADS_CLIENT_ID",
            "GOOGLE_ADS_CLIENT_SECRET",
            "GOOGLE_ADS_REFRESH_TOKEN",
        )
    )
    if json_ok and oauth_ok:
        print(
            "Warning: both service-account JSON and OAuth vars are set; clear one group to avoid ambiguity.",
            file=sys.stderr,
        )

    try:
        client = get_google_ads_client()
    except RuntimeError as exc:
        print(exc, file=sys.stderr)
        print("See:", google_ads_env_path(), file=sys.stderr)
        return 1

    try:
        svc = client.get_service("CustomerService")
        response = svc.list_accessible_customers()
    except Exception as exc:  # noqa: BLE001
        print("list_accessible_customers failed:", exc, file=sys.stderr)
        return 1

    names = list(response.resource_names)
    if not names:
        print(
            "No accessible customers (check Ads user list includes the service account email, "
            "or OAuth user has access)."
        )
        return 0

    print("Accessible customers:")
    for n in names:
        print(" ", n)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
