"""Credentials for Search Console API (OAuth preferred; service account often blocked in GSC UI)."""

from __future__ import annotations

import json
import os
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
GSC_ENV = REPO_ROOT / "secrets" / "gsc.env"
_OAUTH_JSON_NAMES = ("gsc-oauth-desktop.json", "gsc-oauth-client.json")
SCOPES = ("https://www.googleapis.com/auth/webmasters.readonly",)


def load_gsc_env() -> None:
    if not GSC_ENV.is_file():
        return
    for raw in GSC_ENV.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, _, val = line.partition("=")
        key, val = key.strip(), val.strip().strip('"').strip("'")
        if key and key not in os.environ:
            os.environ[key] = val


def oauth_refresh_token() -> str:
    load_gsc_env()
    return (os.environ.get("GSC_REFRESH_TOKEN") or "").strip()


def _oauth_client_from_json() -> tuple[str, str]:
    for name in _OAUTH_JSON_NAMES:
        path = REPO_ROOT / "secrets" / name
        if not path.is_file():
            continue
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            continue
        block = data.get("installed") or data.get("web") or data
        if not isinstance(block, dict):
            continue
        cid = (block.get("client_id") or "").strip()
        secret = (block.get("client_secret") or "").strip()
        if cid and secret:
            return cid, secret
    return "", ""


def oauth_client() -> tuple[str, str]:
    load_gsc_env()
    cid = (os.environ.get("GSC_OAUTH_CLIENT_ID") or os.environ.get("GOOGLE_ADS_CLIENT_ID") or "").strip()
    secret = (
        os.environ.get("GSC_OAUTH_CLIENT_SECRET")
        or os.environ.get("GOOGLE_ADS_CLIENT_SECRET")
        or ""
    ).strip()
    if not cid or not secret:
        cid, secret = _oauth_client_from_json()
    return cid, secret


def build_credentials():
    """OAuth refresh token first; else service account JSON (usually no GSC access)."""
    from google.oauth2.credentials import Credentials as UserCredentials
    from google.oauth2 import service_account
    from google.auth.transport.requests import Request

    token = oauth_refresh_token()
    client_id, client_secret = oauth_client()
    if token and client_id and client_secret:
        creds = UserCredentials(
            token=None,
            refresh_token=token,
            token_uri="https://oauth2.googleapis.com/token",
            client_id=client_id,
            client_secret=client_secret,
            scopes=list(SCOPES),
        )
        creds.refresh(Request())
        return creds

    sys_path = REPO_ROOT / "scripts"
    import sys

    if str(sys_path) not in sys.path:
        sys.path.insert(0, str(sys_path))
    from ga4_fetch import resolve_credentials_path

    creds_path = resolve_credentials_path()
    if not creds_path:
        raise SystemExit(
            "No GSC credentials.\n"
            "Preferred: OAuth — cp secrets/gsc.env.example secrets/gsc.env, "
            "reuse Desktop OAuth client from GCP, run:\n"
            "  .venv/bin/python scripts/gsc_get_refresh_token.py\n"
            "GSC UI cannot add service accounts (email not found)."
        )
    return service_account.Credentials.from_service_account_file(
        str(creds_path),
        scopes=list(SCOPES),
    )


def service_account_email() -> str:
    from ga4_fetch import resolve_credentials_path

    creds_path = resolve_credentials_path()
    if not creds_path:
        return ""
    try:
        return json.loads(creds_path.read_text(encoding="utf-8")).get("client_email", "")
    except (OSError, json.JSONDecodeError):
        return ""
