"""Shared helpers for Google Ads scripts (local secrets only)."""

from __future__ import annotations

import os
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
_GOOGLE_ADS_ENV = REPO_ROOT / "secrets" / "google-ads.env"


# Same default as scripts/ga4_fetch.py (service account JSON).
_GA_SERVICE_ACCOUNT_DEFAULT = REPO_ROOT / "secrets" / "vlwarmte-ga-service-account.json"


def load_google_ads_env_file() -> None:
    """Load KEY=value pairs from secrets/google-ads.env into os.environ (no override)."""
    if not _GOOGLE_ADS_ENV.is_file():
        return
    for raw in _GOOGLE_ADS_ENV.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        if "=" not in line:
            continue
        key, _, val = line.partition("=")
        key = key.strip()
        val = val.strip().strip('"').strip("'")
        if key and key not in os.environ:
            os.environ[key] = val


def google_ads_env_path() -> Path:
    return _GOOGLE_ADS_ENV


def apply_google_ads_client_defaults() -> None:
    """Defaults required by newer google-ads Python releases (before GoogleAdsClient.load_from_env)."""
    os.environ.setdefault("GOOGLE_ADS_USE_PROTO_PLUS", "True")


def _readable_json_path(path: Path) -> bool:
    try:
        return path.is_file() and os.access(path, os.R_OK)
    except OSError:
        return False


def apply_google_ads_default_service_account_json() -> None:
    """If no JSON path set, reuse the same key file as GA4 (GA env or default repo path).

    Skips when OAuth client id is set (OAuth-only flow). Does not override an explicit
    GOOGLE_ADS_JSON_KEY_FILE_PATH.
    """
    if (os.environ.get("GOOGLE_ADS_JSON_KEY_FILE_PATH") or "").strip():
        return
    if (os.environ.get("GOOGLE_ADS_CLIENT_ID") or "").strip():
        return

    candidates: list[Path] = []
    if gac := os.environ.get("GOOGLE_APPLICATION_CREDENTIALS"):
        candidates.append(Path(gac).expanduser())
    if p := os.environ.get("GA4_CREDENTIALS_PATH"):
        q = Path(p).expanduser()
        candidates.append(q if q.is_absolute() else REPO_ROOT / q)
    candidates.append(_GA_SERVICE_ACCOUNT_DEFAULT)

    seen: set[str] = set()
    for raw in candidates:
        try:
            path = raw.resolve()
        except OSError:
            path = raw
        key = str(path)
        if key in seen:
            continue
        seen.add(key)
        if _readable_json_path(path):
            os.environ["GOOGLE_ADS_JSON_KEY_FILE_PATH"] = str(path)
            return


def normalize_google_ads_json_key_path() -> None:
    """Resolve relative GOOGLE_ADS_JSON_KEY_FILE_PATH against repo root (Terminal cwd-safe)."""
    raw = (os.environ.get("GOOGLE_ADS_JSON_KEY_FILE_PATH") or "").strip()
    if not raw:
        return
    path = Path(raw).expanduser()
    if not path.is_absolute():
        path = REPO_ROOT / path
    try:
        resolved = str(path.resolve())
    except OSError:
        return
    if Path(resolved).is_file():
        os.environ["GOOGLE_ADS_JSON_KEY_FILE_PATH"] = resolved


def prepare_google_ads_env() -> None:
    """Load local env file, apply GA JSON default, normalize paths, set library defaults."""
    load_google_ads_env_file()
    apply_google_ads_default_service_account_json()
    normalize_google_ads_json_key_path()
    apply_google_ads_client_defaults()


def google_ads_credentials_error_message() -> str | None:
    """Return a human-readable error string, or None if credentials look usable."""
    dev = (os.environ.get("GOOGLE_ADS_DEVELOPER_TOKEN") or "").strip()
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
    if not dev:
        return f"Missing GOOGLE_ADS_DEVELOPER_TOKEN (see {google_ads_env_path()})"
    if json_key and not json_ok:
        return f"GOOGLE_ADS_JSON_KEY_FILE_PATH is not a readable file: {json_key}"
    if not json_ok and not oauth_ok:
        return (
            "Need either GOOGLE_ADS_JSON_KEY_FILE_PATH (service account invited in Ads) "
            "or GOOGLE_ADS_CLIENT_ID + GOOGLE_ADS_CLIENT_SECRET + GOOGLE_ADS_REFRESH_TOKEN."
        )
    return None


def get_google_ads_client():  # noqa: ANN201 — GoogleAdsClient from optional dependency
    """Return GoogleAdsClient from environment after prepare_google_ads_env()."""
    prepare_google_ads_env()
    err = google_ads_credentials_error_message()
    if err:
        raise RuntimeError(err)
    try:
        from google.ads.googleads.client import GoogleAdsClient
    except ImportError as exc:
        raise RuntimeError(
            "Install deps: pip install -r scripts/requirements-google-ads.txt"
        ) from exc
    try:
        return GoogleAdsClient.load_from_env()
    except Exception as exc:  # noqa: BLE001
        raise RuntimeError(f"GoogleAdsClient.load_from_env() failed: {exc}") from exc


def normalize_customer_id(raw: str) -> str:
    """Digits only, no dashes (Google Ads API customer id)."""
    return "".join(c for c in raw.strip() if c.isdigit())
