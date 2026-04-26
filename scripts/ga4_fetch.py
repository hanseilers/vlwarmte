#!/usr/bin/env python3
"""
Fetches GA4 data for vlwarmte.nl and writes a structured JSON report
to docs/website-manager/ga4_report.json for use by the website-manager skill.
"""

import json
import os
from datetime import datetime, timedelta
from pathlib import Path

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = (
    str(Path.home() / "Library/Mobile Documents/com~apple~CloudDocs/Downloads/vlwarmte-9996bc7cd475.json")
)

from google.analytics.data_v1beta import BetaAnalyticsDataClient
from google.analytics.data_v1beta.types import (
    RunReportRequest, DateRange, Metric, Dimension, OrderBy, FilterExpression, Filter
)

PROPERTY = "properties/534641753"
OUTPUT = Path(__file__).parent.parent / "docs/website-manager/ga4_report.json"

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


def main():
    report = {
        "generated_at": datetime.now().isoformat(),
        "period": "30daysAgo to today",
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
    print(f"Top pages: {len(report['top_pages'])} rows")
    print(f"Traffic sources: {len(report['traffic_sources'])} rows")


if __name__ == "__main__":
    main()
