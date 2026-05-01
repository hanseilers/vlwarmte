#!/usr/bin/env python3
"""
Idempotent GA4 Admin baseline for vlwarmte.nl (property 534641753).

Creates (if missing):
  - Key events for site-measurable leads and calculator funnel
  - Event-scoped custom dimensions for parameters used in gtag() on the site

Credentials (same order as ga4_fetch.py):
  GOOGLE_APPLICATION_CREDENTIALS, GA4_CREDENTIALS_PATH,
  secrets/vlwarmte-ga-service-account.json

Requires service account with analytics.edit on the property (e.g. Administrator).

  python3 -m venv .venv && . .venv/bin/activate
  pip install google-analytics-admin google-auth
  python3 scripts/ga4_admin_setup.py
"""

from __future__ import annotations

import os
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
PROPERTY = "properties/534641753"
_LEGACY_ICLOUD = (
    Path.home()
    / "Library/Mobile Documents/com~apple~CloudDocs/Downloads/vlwarmte-9996bc7cd475.json"
)
_REPO_SECRET = REPO_ROOT / "secrets" / "vlwarmte-ga-service-account.json"

KEY_EVENTS = (
    "contact_submit",
    "wizard_lead_submit",
    "lead_form_submit",
    "wizard_calculate",
    "calculator_result",
    "wizard_start",
)

# Event parameter names as sent from contact.html / prijsindicatie.html / main.js
CUSTOM_DIMENSIONS: tuple[tuple[str, str, str], ...] = (
    ("soort_aanvraag", "Soort aanvraag", "Contact: informatie, offerte of terugbelverzoek"),
    ("projecttype", "Projecttype", "Prijscalculator / wizard"),
    ("m2", "m2 vloeroppervlak", "Prijscalculator / wizard (vierkante meters)"),
    ("zones", "Zones", "Prijscalculator / wizard"),
    ("stap", "Wizard stap", "Prijscalculator stap-label"),
    ("event_category", "Eventcategorie", "Bijv. prijsindicatie bij lead_form_submit"),
)


def _readable_file(path: Path) -> bool:
    try:
        return path.is_file() and os.access(path, os.R_OK)
    except OSError:
        return False


def resolve_credentials_path() -> Path | None:
    candidates: list[Path] = []
    if os.environ.get("GOOGLE_APPLICATION_CREDENTIALS"):
        candidates.append(Path(os.environ["GOOGLE_APPLICATION_CREDENTIALS"]).expanduser())
    if p := os.environ.get("GA4_CREDENTIALS_PATH"):
        q = Path(p).expanduser()
        candidates.append(q if q.is_absolute() else REPO_ROOT / q)
    candidates.append(_REPO_SECRET)
    candidates.append(_LEGACY_ICLOUD)
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
        if _readable_file(path):
            return path
    return None


def main() -> int:
    try:
        from google.analytics.admin_v1alpha import AnalyticsAdminServiceClient
        from google.analytics.admin_v1alpha.types import CustomDimension, KeyEvent
        from google.api_core import exceptions
        from google.oauth2 import service_account
    except ImportError:
        print(
            "Installeer: pip install google-analytics-admin google-auth",
            file=sys.stderr,
        )
        return 1

    cred_path = resolve_credentials_path()
    if not cred_path:
        print("Geen leesbaar service-account JSON gevonden.", file=sys.stderr)
        return 1

    creds = service_account.Credentials.from_service_account_file(
        str(cred_path),
        scopes=["https://www.googleapis.com/auth/analytics.edit"],
    )
    client = AnalyticsAdminServiceClient(credentials=creds)

    existing_events = {
        e.event_name for e in client.list_key_events(parent=PROPERTY)
    }
    for name in KEY_EVENTS:
        if name in existing_events:
            print(f"key_event skip (bestaat al): {name}")
            continue
        try:
            client.create_key_event(
                parent=PROPERTY,
                key_event=KeyEvent(event_name=name),
            )
            print(f"key_event aangemaakt: {name}")
        except exceptions.AlreadyExists:
            print(f"key_event skip (AlreadyExists): {name}")

    existing_params = {
        d.parameter_name for d in client.list_custom_dimensions(parent=PROPERTY)
    }
    for param, display, desc in CUSTOM_DIMENSIONS:
        if param in existing_params:
            print(f"custom_dimension skip (bestaat al): {param}")
            continue
        try:
            client.create_custom_dimension(
                parent=PROPERTY,
                custom_dimension=CustomDimension(
                    parameter_name=param,
                    display_name=display,
                    description=desc,
                    scope=CustomDimension.DimensionScope.EVENT,
                ),
            )
            print(f"custom_dimension aangemaakt: {param} ({display})")
        except exceptions.AlreadyExists:
            print(f"custom_dimension skip (AlreadyExists): {param}")

    print("\nKlaar. Key events kunnen enkele uren nodig hebben in rapporten.")
    print(
        "Search Console: koppel handmatig in GA4 (Beheer → Productkoppelingen) "
        "als dat nog niet is gedaan."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
