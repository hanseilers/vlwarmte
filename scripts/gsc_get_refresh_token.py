#!/usr/bin/env python3
"""
One-time OAuth for Search Console API (use your verified owner Google account).

GSC → Add user does NOT accept @*.iam.gserviceaccount.com ("email not found").
Use this flow instead.

Prerequisites:
  - GCP project with "Google Search Console API" enabled.
  - OAuth Desktop client (same as Google Ads is fine).
  - secrets/gsc.env with GSC_OAUTH_CLIENT_ID / GSC_OAUTH_CLIENT_SECRET
    (or reuse GOOGLE_ADS_CLIENT_ID / GOOGLE_ADS_CLIENT_SECRET from google-ads.env)

  cp secrets/gsc.env.example secrets/gsc.env
  .venv/bin/pip install -r scripts/requirements-gsc.txt
  .venv/bin/python scripts/gsc_get_refresh_token.py

Log in as the Google account that owns GSC for www.vlwarmte.nl.
The refresh token is saved directly to gitignored secrets/gsc.env (mode 0600),
without printing credentials. A Testing OAuth app still expires after 7 days;
use the approved Production app for the recurring report.
"""

from __future__ import annotations

import sys
from pathlib import Path

_SCRIPTS = Path(__file__).resolve().parent
if str(_SCRIPTS) not in sys.path:
    sys.path.insert(0, str(_SCRIPTS))

from gsc_auth import SCOPES, oauth_client, load_gsc_env

REPO_ROOT = _SCRIPTS.parent
GSC_ENV = REPO_ROOT / "secrets" / "gsc.env"


def main() -> int:
    load_gsc_env()
    client_id, client_secret = oauth_client()
    if not client_id or not client_secret:
        print(
            "Missing OAuth client credentials.\n"
            "  A) GCP → APIs & Services → Credentials → OAuth client ID → Desktop app\n"
            "     Download JSON → save as secrets/gsc-oauth-desktop.json (gitignored)\n"
            "  B) Or set GSC_OAUTH_CLIENT_ID / GSC_OAUTH_CLIENT_SECRET in secrets/gsc.env\n"
            "     (or GOOGLE_ADS_CLIENT_ID / GOOGLE_ADS_CLIENT_SECRET in google-ads.env).",
            file=sys.stderr,
        )
        return 1

    try:
        from google_auth_oauthlib.flow import InstalledAppFlow
    except ImportError:
        print("pip install -r scripts/requirements-gsc.txt", file=sys.stderr)
        return 1

    flow = InstalledAppFlow.from_client_config(
        {
            "installed": {
                "client_id": client_id,
                "client_secret": client_secret,
                "auth_uri": "https://accounts.google.com/o/oauth2/auth",
                "token_uri": "https://oauth2.googleapis.com/token",
                "redirect_uris": ["http://127.0.0.1", "http://localhost"],
            }
        },
        SCOPES,
    )
    creds = flow.run_local_server(
        port=0, prompt="consent", open_browser=True,
        authorization_prompt_message="Complete GSC sign-in in the opened browser.",
    )
    token = getattr(creds, "refresh_token", None)
    if not token:
        print("No refresh_token — revoke app access and retry.", file=sys.stderr)
        return 1

    lines = GSC_ENV.read_text(encoding="utf-8").splitlines() if GSC_ENV.exists() else []
    lines = [line for line in lines if not line.strip().startswith("GSC_REFRESH_TOKEN=")]
    lines.append("GSC_REFRESH_TOKEN=" + token)
    GSC_ENV.parent.mkdir(parents=True, exist_ok=True)
    import tempfile
    import os

    # mkstemp creates the secret file with 0600 before any credentials are written.
    fd, temporary = tempfile.mkstemp(dir=GSC_ENV.parent, prefix=".gsc-", suffix=".env")
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as handle:
            handle.write("\n".join(lines) + "\n")
        os.replace(temporary, GSC_ENV)
    finally:
        if os.path.exists(temporary):
            os.unlink(temporary)
    print("Search Console login saved securely to secrets/gsc.env.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
