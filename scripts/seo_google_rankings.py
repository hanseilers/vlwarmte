#!/usr/bin/env python3
"""Check organic Google positions for vlwarmte.nl via ScrapingBee.

Uses ScrapingBee Google Search API (structured JSON). Optional ``--custom-google``
uses the HTML API with ``custom_google=true`` (same SERP, harder to parse).

API key: env ``SCRAPINGBEE_API_KEY`` or gitignored ``secrets/scrapingbee.env``.

Example:
  python scripts/seo_google_rankings.py
  python scripts/seo_google_rankings.py --max-pages 3 --output /tmp/vlw-ranks.json
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEFAULTS_JSON = ROOT / "scripts" / "data" / "google_ads_lead_campaign_defaults.json"
SECRETS_ENV = ROOT / "secrets" / "scrapingbee.env"
STORE_URL = "https://app.scrapingbee.com/api/v1/store/google"
HTML_URL = "https://app.scrapingbee.com/api/v1"

DOMAIN_MARKERS = ("vlwarmte.nl", "www.vlwarmte.nl")


def load_api_key() -> str:
    key = os.environ.get("SCRAPINGBEE_API_KEY", "").strip()
    if key:
        return key
    if SECRETS_ENV.is_file():
        for line in SECRETS_ENV.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            if line.startswith("export "):
                line = line[7:].strip()
            if "=" not in line:
                continue
            name, _, value = line.partition("=")
            if name.strip() == "SCRAPINGBEE_API_KEY":
                return value.strip().strip("'\"")
    sys.exit(
        "Missing SCRAPINGBEE_API_KEY. Set env or create secrets/scrapingbee.env "
        "(see secrets/scrapingbee.env.example)."
    )


def load_keywords(path: Path) -> list[str]:
    data = json.loads(path.read_text(encoding="utf-8"))
    return [item["text"] for item in data.get("keywords", []) if item.get("text")]


def fetch_store_google(
    api_key: str,
    search: str,
    *,
    page: int,
    country_code: str,
    language: str,
    light_request: bool,
) -> dict:
    params = {
        "api_key": api_key,
        "search": search,
        "country_code": country_code,
        "language": language,
        "page": str(page),
        "light_request": "true" if light_request else "false",
    }
    url = STORE_URL + "?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req, timeout=120) as resp:
        return json.loads(resp.read())


def fetch_custom_google_html(
    api_key: str,
    search: str,
    *,
    country_code: str,
    language: str,
) -> str:
    google_url = "https://www.google.nl/search?" + urllib.parse.urlencode(
        {"q": search, "hl": language, "gl": country_code, "num": 20}
    )
    params = {
        "api_key": api_key,
        "url": google_url,
        "custom_google": "true",
        "country_code": country_code,
        "render_js": "false",
        "premium_proxy": "true",
    }
    url = HTML_URL + "?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req, timeout=120) as resp:
        return resp.read().decode("utf-8", errors="replace")


def position_in_organic(organic: list[dict]) -> tuple[int | None, str | None]:
    for row in organic:
        url = (row.get("url") or "").lower()
        domain = (row.get("domain") or "").lower()
        if any(m in url or m in domain for m in DOMAIN_MARKERS):
            pos = row.get("position")
            if isinstance(pos, int):
                return pos, row.get("url")
            if pos is not None:
                try:
                    return int(pos), row.get("url")
                except (TypeError, ValueError):
                    pass
            return None, row.get("url")
    return None, None


def position_in_custom_google_html(html: str) -> tuple[int | None, str | None]:
    # Match result blocks that link to vlwarmte; order in HTML ≈ SERP order.
    pattern = re.compile(
        r'href="(https?://(?:www\.)?vlwarmte\.nl[^"]*)"',
        re.IGNORECASE,
    )
    matches = list(pattern.finditer(html))
    if not matches:
        return None, None
    first_url = matches[0].group(1)
    # Rough position: count preceding /url?q= or cite blocks (heuristic).
    before = html[: matches[0].start()]
    organic_hints = len(re.findall(r'class="[^"]*\bg\b[^"]*"', before))
    pos = max(1, min(organic_hints, 30)) if organic_hints else None
    return pos, first_url


def rank_keyword(
    api_key: str,
    keyword: str,
    *,
    max_pages: int,
    country_code: str,
    language: str,
    light_request: bool,
    use_custom_google: bool,
    sleep_s: float,
) -> dict:
    if use_custom_google:
        html = fetch_custom_google_html(
            api_key, keyword, country_code=country_code, language=language
        )
        pos, url = position_in_custom_google_html(html)
        time.sleep(sleep_s)
        return {
            "keyword": keyword,
            "position": pos,
            "landing_url": url,
            "pages_checked": 1,
            "method": "custom_google_html",
            "in_top": (pos if pos is not None else 99) <= 10,
        }

    landing_url = None
    for page in range(1, max_pages + 1):
        data = fetch_store_google(
            api_key,
            keyword,
            page=page,
            country_code=country_code,
            language=language,
            light_request=light_request,
        )
        organic = data.get("organic_results") or []
        pos, url = position_in_organic(organic)
        if pos is not None:
            per_page = len(organic) or 10
            absolute = int(pos) + (page - 1) * per_page
            return {
                "keyword": keyword,
                "position": absolute,
                "landing_url": url,
                "pages_checked": page,
                "method": "store_google",
                "in_top": absolute <= 10,
            }
        if landing_url is None and url:
            landing_url = url
        time.sleep(sleep_s)

    return {
        "keyword": keyword,
        "position": None,
        "landing_url": landing_url,
        "pages_checked": max_pages,
        "method": "store_google",
        "in_top": False,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--keywords-file",
        type=Path,
        default=DEFAULTS_JSON,
        help="JSON with keywords[] (default: google_ads_lead_campaign_defaults.json)",
    )
    parser.add_argument("--max-pages", type=int, default=3, help="SERP pages to scan")
    parser.add_argument("--country-code", default="nl")
    parser.add_argument("--language", default="nl")
    parser.add_argument(
        "--light-request",
        action="store_true",
        default=True,
        help="10 credits/request (default). Use --no-light-request for 15 credits.",
    )
    parser.add_argument("--no-light-request", dest="light_request", action="store_false")
    parser.add_argument(
        "--custom-google",
        action="store_true",
        help="HTML API + custom_google=true (heuristic parsing; 25 credits with premium)",
    )
    parser.add_argument("--sleep", type=float, default=0.35, help="Delay between requests")
    parser.add_argument("--output", type=Path, help="Write JSON results to file")
    parser.add_argument("--limit", type=int, default=0, help="Only first N keywords (0=all)")
    args = parser.parse_args()

    api_key = load_api_key()
    keywords = load_keywords(args.keywords_file)
    if args.limit:
        keywords = keywords[: args.limit]

    results: list[dict] = []
    for i, kw in enumerate(keywords, 1):
        print(f"[{i}/{len(keywords)}] {kw} …", flush=True)
        try:
            row = rank_keyword(
                api_key,
                kw,
                max_pages=args.max_pages,
                country_code=args.country_code,
                language=args.language,
                light_request=args.light_request,
                use_custom_google=args.custom_google,
                sleep_s=args.sleep,
            )
        except urllib.error.HTTPError as exc:
            body = exc.read().decode("utf-8", errors="replace")[:300]
            row = {"keyword": kw, "error": f"HTTP {exc.code}: {body}"}
        except Exception as exc:  # noqa: BLE001
            row = {"keyword": kw, "error": str(exc)}

        if row.get("position") is None and not row.get("error"):
            row["position_label"] = f">{args.max_pages * 10}"

        results.append(row)
        pos = row.get("position")
        label = pos if pos is not None else row.get("position_label", "?")
        url = row.get("landing_url") or ""
        print(f"    → {label} {url}")

    ranked = [r for r in results if isinstance(r.get("position"), int)]
    top10 = [r for r in ranked if r["position"] <= 10]
    print()
    print(f"Keywords checked: {len(results)}")
    print(f"In top 10: {len(top10)}")
    print(f"Ranked (top {args.max_pages * 10}): {len(ranked)}")
    print(f"Not in top {args.max_pages * 10}: {len(results) - len(ranked) - sum(1 for r in results if r.get('error'))}")

    if args.output:
        args.output.write_text(
            json.dumps(
                {
                    "domain": "vlwarmte.nl",
                    "country_code": args.country_code,
                    "language": args.language,
                    "max_pages": args.max_pages,
                    "checked_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
                    "results": results,
                },
                indent=2,
                ensure_ascii=False,
            ),
            encoding="utf-8",
        )
        print(f"Wrote {args.output}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
