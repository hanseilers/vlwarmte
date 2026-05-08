#!/usr/bin/env python3
"""
One-time OAuth to obtain GOOGLE_ADS_REFRESH_TOKEN for the Google Ads API.

Use this only if you do **not** use a service account for the Ads API. Prefer
`GOOGLE_ADS_JSON_KEY_FILE_PATH` when the same service account is already invited
under Google Ads → Admin → Access and security → Users (see Google’s
“Authenticate with service accounts” guide).

Prerequisites (Google Cloud + Google Ads UI):
  - GCP project with "Google Ads API" enabled.
  - OAuth consent screen published or your Google user added as test user.
  - OAuth client type "Desktop app" → copy Client ID and Client Secret.
  - Google Ads: API Center → developer token (Test is OK to start; production
    access is a separate approval).

Setup in this repo:
  1. cp secrets/google-ads.env.example secrets/google-ads.env
  2. Leave GOOGLE_ADS_JSON_KEY_FILE_PATH unset; fill GOOGLE_ADS_DEVELOPER_TOKEN,
     GOOGLE_ADS_CLIENT_ID, GOOGLE_ADS_CLIENT_SECRET (refresh token empty for this step).
  3. python3 -m venv .venv && source .venv/bin/activate
     pip install -r scripts/requirements-google-ads.txt
  4. python scripts/google_ads_get_refresh_token.py
  5. Paste the printed refresh token into secrets/google-ads.env as GOOGLE_ADS_REFRESH_TOKEN=

Uses a local browser redirect (run_local_server). Complete the Google login in the browser.
"""

from __future__ import annotations

import sys
from pathlib import Path

_SCRIPTS_DIR = Path(__file__).resolve().parent
if str(_SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(_SCRIPTS_DIR))

from google_ads_common import google_ads_env_path, load_google_ads_env_file

SCOPES = ("https://www.googleapis.com/auth/adwords",)


def main() -> int:
    load_google_ads_env_file()

    import os

    client_id = (os.environ.get("GOOGLE_ADS_CLIENT_ID") or "").strip()
    client_secret = (os.environ.get("GOOGLE_ADS_CLIENT_SECRET") or "").strip()
    if not client_id or not client_secret:
        print(
            "Set GOOGLE_ADS_CLIENT_ID and GOOGLE_ADS_CLIENT_SECRET in",
            google_ads_env_path(),
            file=sys.stderr,
        )
        return 1

    try:
        from google_auth_oauthlib.flow import InstalledAppFlow
    except ImportError:
        print("Install deps: pip install -r scripts/requirements-google-ads.txt", file=sys.stderr)
        return 1

    flow = InstalledAppFlow.from_client_config(
        {
            "installed": {
                "client_id": client_id,
                "client_secret": client_secret,
                "auth_uri": "https://accounts.google.com/o/oauth2/auth",
                "token_uri": "https://oauth2.googleapis.com/token",
                "client_auth_method": "client_secret_post",
                "redirect_uris": ["http://127.0.0.1", "http://localhost"],
            }
        },
        SCOPES,
    )
    creds = flow.run_local_server(port=0, prompt="consent", open_browser=True)
    token = getattr(creds, "refresh_token", None)
    if not token:
        print("No refresh_token returned. Revoke app access and retry with prompt=consent.", file=sys.stderr)
        return 1

    print("\nAdd this line to secrets/google-ads.env (keep it private):\n")
    print(f'GOOGLE_ADS_REFRESH_TOKEN="{token}"\n')
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
