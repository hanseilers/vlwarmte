#!/usr/bin/env python3
"""
Fetches GA4 data for vlwarmte.nl and writes a structured JSON report
to docs/website-manager/ga4_report.json for use by the website-manager skill.

Credentials (eerste match wint):
  1. Bestaande omgevingsvariabele GOOGLE_APPLICATION_CREDENTIALS (als leesbaar)
  2. GA4_CREDENTIALS_PATH — absoluut of t.o.v. repo-root
  3. secrets/vlwarmte-ga-service-account.json in de repo (niet committen; zie .gitignore)
  4. Legacy pad: iCloud Downloads (werkt vaak niet vanuit Terminal / sandbox)

Python: gebruik een venv in de repo (PEP 668 blokkeert pip op systeem-Python):
  python3 -m venv .venv && source .venv/bin/activate && pip install google-analytics-data
"""

import json
import os
import sys
from datetime import datetime, timedelta
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
OUTPUT = REPO_ROOT / "docs" / "website-manager" / "ga4_report.json"
PROPERTY = "properties/534641753"

_LEGACY_ICLOUD = (
    Path.home()
    / "Library/Mobile Documents/com~apple~CloudDocs/Downloads/vlwarmte-9996bc7cd475.json"
)
_REPO_SECRET = REPO_ROOT / "secrets" / "vlwarmte-ga-service-account.json"


def _readable_file(path: Path) -> bool:
    try:
        return path.is_file() and os.access(path, os.R_OK)
    except OSError:
        return False


def resolve_credentials_path() -> Path | None:
    """Pick first usable credentials file; does not set os.environ."""
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


def _credentials_help() -> str:
    return f"""Geen leesbaar Google service-account JSON gevonden.

iCloud-pad (Mobile Documents/.../Downloads/): Terminal krijgt daar vaak
"Operation not permitted" — ook niet met sudo. Dat is macOS-toegangsbeleid,
geen rechten op het bestand zelf.

Wat wél werkt:
  A) In Finder: iCloud Downloads openen, JSON selecteren, kopiëren naar een
     map buiten iCloud (bijv. je echte ~/Downloads als die lokaal is, of
     ~/Desktop), daarna in Terminal:
       mkdir -p secrets && cp ~/Downloads/vlwarmte-*.json {_REPO_SECRET}
     (pas de bronnaam aan)

  B) Nieuw keybestand downloaden van Google Cloud Console en direct opslaan
     in ~/Downloads (lokaal), niet in "iCloud Downloads".

  C) Zet daarna óf bestand op:
       {_REPO_SECRET}
     óf:
       export GA4_CREDENTIALS_PATH=\"/volledig/lokaal/pad/naar.json\"

  D) Optioneel: Systeeminstellingen → Privacy en beveiliging → Volledige schijftoegang:
     Terminal (of je terminal-app) aanzetten — helpt soms, maar iCloud blijft
     onbetrouwbaar voor scripts; liever een lokaal pad.

Python-packages (eenmalig in deze repo):
  python3 -m venv .venv
  source .venv/bin/activate   # Windows: .venv\\Scripts\\activate
  pip install google-analytics-data
  python3 scripts/ga4_fetch.py
"""


def main() -> None:
    cred_path = resolve_credentials_path()
    if cred_path is None:
        print(_credentials_help(), file=sys.stderr)
        sys.exit(1)

    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = str(cred_path)

    from google.analytics.data_v1beta import BetaAnalyticsDataClient
    from google.analytics.data_v1beta.types import (
        DateRange,
        Dimension,
        Metric,
        OrderBy,
        RunReportRequest,
    )

    client = BetaAnalyticsDataClient()

    def run(dimensions, metrics, start="30daysAgo", end="today", limit=20, order_metric=None):
        req = RunReportRequest(
            property=PROPERTY,
            dimensions=[Dimension(name=d) for d in dimensions],
            metrics=[Metric(name=m) for m in metrics],
            date_ranges=[DateRange(start_date=start, end_date=end)],
            limit=limit,
        )
        if order_metric:
            req.order_bys = [OrderBy(metric=OrderBy.MetricOrderBy(metric_name=order_metric), desc=True)]
        resp = client.run_report(req)
        rows = []
        for row in resp.rows:
            entry = {}
            for i, dim in enumerate(dimensions):
                entry[dim] = row.dimension_values[i].value
            for i, met in enumerate(metrics):
                entry[met] = row.metric_values[i].value
            rows.append(entry)
        return rows

    report = {
        "generated_at": datetime.now().isoformat(),
        "period": "30daysAgo to today",
        "credentials_source": str(cred_path),
    }

    print("Fetching top pages...")
    report["top_pages"] = run(
        dimensions=["pagePath", "pageTitle"],
        metrics=["sessions", "activeUsers", "averageSessionDuration", "bounceRate"],
        order_metric="sessions",
    )

    print("Fetching traffic sources...")
    report["traffic_sources"] = run(
        dimensions=["sessionDefaultChannelGrouping", "sessionSourceMedium"],
        metrics=["sessions", "activeUsers", "conversions"],
        order_metric="sessions",
    )

    print("Fetching entry pages...")
    report["entry_pages"] = run(
        dimensions=["landingPagePlusQueryString"],
        metrics=["sessions", "bounceRate", "conversions"],
        order_metric="sessions",
        limit=15,
    )

    print("Fetching device categories...")
    report["devices"] = run(
        dimensions=["deviceCategory"],
        metrics=["sessions", "activeUsers"],
        order_metric="sessions",
        limit=5,
    )

    print("Fetching geo data...")
    report["geo"] = run(
        dimensions=["country", "region"],
        metrics=["sessions", "activeUsers"],
        order_metric="sessions",
        limit=10,
    )

    print("Fetching page engagement (last 90 days)...")
    report["page_engagement_90d"] = run(
        dimensions=["pagePath"],
        metrics=["sessions", "averageSessionDuration", "scrolledUsers"],
        start="90daysAgo",
        order_metric="sessions",
        limit=15,
    )

    print("Fetching weekly trend...")
    weekly = []
    for i in range(8):
        end_date = datetime.today() - timedelta(weeks=i)
        start_date = end_date - timedelta(weeks=1)
        rows = run(
            dimensions=[],
            metrics=["sessions", "activeUsers"],
            start=start_date.strftime("%Y-%m-%d"),
            end=end_date.strftime("%Y-%m-%d"),
            limit=1,
        )
        if rows:
            rows[0]["week_start"] = start_date.strftime("%Y-%m-%d")
            weekly.append(rows[0])
    report["weekly_trend"] = list(reversed(weekly))

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(report, indent=2, ensure_ascii=False))
    print(f"\nReport saved to {OUTPUT}")
    print(f"Credentials: {cred_path}")
    print(f"Top pages: {len(report['top_pages'])} rows")
    print(f"Traffic sources: {len(report['traffic_sources'])} rows")


if __name__ == "__main__":
    main()
