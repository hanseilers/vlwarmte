#!/usr/bin/env python3
"""
Fetch Search Console performance (queries + pages) for vlwarmte.nl.

Auth (in order):
  1. OAuth refresh token in secrets/gsc.env (recommended — GSC UI rejects service accounts)
  2. Service-account JSON (same as GA4) — only works if Google ever grants GSC access

  cp secrets/gsc.env.example secrets/gsc.env
  .venv/bin/python scripts/gsc_get_refresh_token.py
  .venv/bin/python scripts/gsc_fetch.py

Writes docs/website-manager/gsc_report.json (gitignored).
"""

from __future__ import annotations

import json
import sys
from datetime import date, timedelta
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
OUTPUT = REPO_ROOT / "docs" / "website-manager" / "gsc_report.json"

sys.path.insert(0, str(REPO_ROOT / "scripts"))
from gsc_auth import build_credentials  # noqa: E402

SITE_CANDIDATES = [
    "https://www.vlwarmte.nl/",
    "https://vlwarmte.nl/",
    "sc-domain:vlwarmte.nl",
]

DAYS = 28


def _service():
    from googleapiclient.discovery import build

    creds = build_credentials()
    return build("searchconsole", "v1", credentials=creds, cache_discovery=False)


def _pick_site(service) -> str:
    sites = service.sites().list().execute().get("siteEntry", [])
    permitted = {s["siteUrl"] for s in sites if s.get("permissionLevel") != "siteUnverifiedUser"}
    for candidate in SITE_CANDIDATES:
        if candidate in permitted:
            return candidate
    if permitted:
        # Prefer www property if multiple
        for url in sorted(permitted):
            if "www.vlwarmte" in url:
                return url
        return sorted(permitted)[0]
    raise SystemExit(
        "No Search Console properties for these credentials.\n"
        "Use OAuth: scripts/gsc_get_refresh_token.py with the Google account that "
        "owns GSC (service accounts cannot be added in GSC UI — 'email not found')."
    )


def _search_analytics(service, site_url: str, dimensions: list[str], row_limit: int = 25):
    end = date.today() - timedelta(days=1)
    start = end - timedelta(days=DAYS - 1)
    body = {
        "startDate": start.isoformat(),
        "endDate": end.isoformat(),
        "dimensions": dimensions,
        "rowLimit": row_limit,
        "dataState": "final",
    }
    return service.searchanalytics().query(siteUrl=site_url, body=body).execute()


def main() -> int:
    service = _service()
    site_url = _pick_site(service)
    queries = _search_analytics(service, site_url, ["query"], row_limit=50)
    pages = _search_analytics(service, site_url, ["page"], row_limit=30)
    query_page = _search_analytics(
        service, site_url, ["query", "page"], row_limit=100
    )

    end = date.today() - timedelta(days=1)
    start = end - timedelta(days=DAYS - 1)

    report = {
        "fetched_at": date.today().isoformat(),
        "site_url": site_url,
        "period": {"start": start.isoformat(), "end": end.isoformat(), "days": DAYS},
        "top_queries": _rows(queries),
        "top_pages": _rows(pages),
        "query_page": _rows(query_page),
    }
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"Wrote {OUTPUT} ({site_url}, {len(report['top_queries'])} queries)")
    return 0


def _rows(payload: dict) -> list[dict]:
    out = []
    for row in payload.get("rows", []):
        keys = row.get("keys", [])
        out.append(
            {
                "keys": keys,
                "clicks": row.get("clicks", 0),
                "impressions": row.get("impressions", 0),
                "ctr": round(row.get("ctr", 0) * 100, 2),
                "position": round(row.get("position", 0), 1),
            }
        )
    return out


if __name__ == "__main__":
    raise SystemExit(main())
