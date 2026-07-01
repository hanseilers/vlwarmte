#!/usr/bin/env python3
"""
Align GA4 key events (conversions) with real VLWarmte leads only.

Keeps:  contact_submit, wizard_lead_submit
Removes funnel/noise: wizard_start, calculator_result, wizard_calculate,
  calculator_complete, lead_form_submit (duplicate), qualify_lead,
  close_convert_lead, purchase (when the API allows)

Uses the same service-account resolution as scripts/ga4_fetch.py.

  .venv/bin/python scripts/ga4_configure_conversions.py --dry-run
  .venv/bin/python scripts/ga4_configure_conversions.py --apply
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "scripts"))

PROPERTY_ID = "534641753"
PROPERTY = f"properties/{PROPERTY_ID}"

LEAD_CONVERSIONS = ("contact_submit", "wizard_lead_submit")
REMOVE_CONVERSIONS = (
    "wizard_start",
    "calculator_result",
    "wizard_calculate",
    "calculator_complete",
    "lead_form_submit",
    "qualify_lead",
    "close_convert_lead",
    "purchase",
)


def _resolve_credentials() -> None:
    from ga4_fetch import resolve_credentials_path

    cred = resolve_credentials_path()
    if cred is None:
        print("Geen GA4 service-account JSON gevonden (zie scripts/ga4_fetch.py).", file=sys.stderr)
        sys.exit(1)
    import os

    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = str(cred)


def _client():
    from google.analytics.admin_v1beta import AnalyticsAdminServiceClient
    from google.analytics.admin_v1beta.types import ConversionEvent

    return AnalyticsAdminServiceClient(), ConversionEvent


def list_conversions() -> dict[str, str]:
    client, _ = _client()
    out: dict[str, str] = {}
    for ev in client.list_conversion_events(parent=PROPERTY):
        out[ev.event_name] = ev.name
    return out


def apply(*, dry_run: bool) -> int:
    _resolve_credentials()
    client, ConversionEvent = _client()
    current = list_conversions()

    print(f"Property: {PROPERTY}")
    print(f"Huidige key events ({len(current)}): {', '.join(sorted(current)) or '—'}")
    print()

    removed = 0
    skipped = 0
    for event_name in REMOVE_CONVERSIONS:
        resource = current.get(event_name)
        if not resource:
            continue
        print(f"  verwijder key event: {event_name}")
        if dry_run:
            removed += 1
            continue
        try:
            client.delete_conversion_event(name=resource)
            removed += 1
            del current[event_name]
        except Exception as exc:
            skipped += 1
            print(f"    → overgeslagen ({exc.__class__.__name__}: {exc})")

    added = 0
    for event_name in LEAD_CONVERSIONS:
        if event_name in current:
            print(f"  behouden: {event_name}")
            continue
        print(f"  toevoegen key event: {event_name}")
        if not dry_run:
            client.create_conversion_event(
                parent=PROPERTY,
                conversion_event=ConversionEvent(event_name=event_name),
            )
            current[event_name] = "(new)"
        added += 1

    print()
    if dry_run:
        print(f"Dry-run: zou {removed} key event(s) verwijderen, {added} toevoegen.")
        print("Draai opnieuw met --apply om door te voeren.")
    else:
        after = list_conversions()
        print(f"Klaar. Key events nu ({len(after)}): {', '.join(sorted(after))}")
        if skipped:
            print(
                f"{skipped} event(s) kon(de) de API niet verwijderen (vaak Google-defaults; "
                "harmless als ze niet op de site firen, bv. purchase)."
            )
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description="GA4: alleen echte lead-events als conversie")
    group = ap.add_mutually_exclusive_group(required=True)
    group.add_argument("--dry-run", action="store_true", help="Toon wijzigingen, pas niet toe")
    group.add_argument("--apply", action="store_true", help="Wijzigingen doorvoeren in GA4")
    ns = ap.parse_args()
    return apply(dry_run=ns.dry_run)


if __name__ == "__main__":
    raise SystemExit(main())
