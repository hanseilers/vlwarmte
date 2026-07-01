#!/usr/bin/env python3
"""
Add **positive keywords** from `google_ads_lead_campaign_defaults.json` to the first ad group
of a Search campaign, skipping any (text + match type) already present.

Does not remove existing keywords — pause or delete broader terms in Ads if you are tightening.

  .venv/bin/python scripts/google_ads_add_keywords_from_defaults.py --dry-run --campaign-id 23834672782
  .venv/bin/python scripts/google_ads_add_keywords_from_defaults.py --apply --campaign-id 23834672782
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

_SCRIPTS_DIR = Path(__file__).resolve().parent
if str(_SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(_SCRIPTS_DIR))

from google_ads_common import (  # noqa: E402
    get_google_ads_client,
    google_ads_env_path,
    normalize_customer_id,
    prepare_google_ads_env,
)

_DEFAULTS = _SCRIPTS_DIR / "data" / "google_ads_lead_campaign_defaults.json"
_KW_TEMP_START = -600


def _match_type_enum(client, name: str):
    n = (name or "PHRASE").upper().strip()
    m = client.enums.KeywordMatchTypeEnum
    if n == "BROAD":
        return m.BROAD
    if n == "EXACT":
        return m.EXACT
    return m.PHRASE


def _match_label(enum_val) -> str:
    return enum_val.name if enum_val is not None else "PHRASE"


def main() -> int:
    p = argparse.ArgumentParser(description="Add missing keywords from defaults JSON to first ad group.")
    mode = p.add_mutually_exclusive_group(required=True)
    mode.add_argument("--dry-run", action="store_true")
    mode.add_argument("--apply", action="store_true")
    p.add_argument("--customer-id", default=None)
    p.add_argument("--campaign-id", required=True)
    p.add_argument("--defaults-json", type=Path, default=_DEFAULTS)
    args = p.parse_args()

    import os

    prepare_google_ads_env()
    raw = (args.customer_id or os.environ.get("GOOGLE_ADS_CUSTOMER_ID") or "").strip()
    cid = normalize_customer_id(raw)
    if len(cid) != 10:
        print("Need --customer-id or GOOGLE_ADS_CUSTOMER_ID.", file=sys.stderr)
        print("See:", google_ads_env_path(), file=sys.stderr)
        return 1

    try:
        defaults = json.loads(Path(args.defaults_json).read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print("Bad defaults JSON:", exc, file=sys.stderr)
        return 1

    try:
        client = get_google_ads_client()
    except RuntimeError as exc:
        print(exc, file=sys.stderr)
        return 1

    try:
        from google.ads.googleads.errors import GoogleAdsException
    except ImportError:
        GoogleAdsException = Exception  # type: ignore[misc,assignment]

    gas = client.get_service("GoogleAdsService")
    camp_id = str(int(args.campaign_id))

    q_ag = f"""
        SELECT ad_group.resource_name, ad_group.id
        FROM ad_group
        WHERE campaign.id = {camp_id}
          AND ad_group.status != 'REMOVED'
        ORDER BY ad_group.id
        LIMIT 1
    """
    ag_rn = None
    ag_id: str | None = None
    for row in gas.search(customer_id=cid, query=q_ag):
        ag_rn = row.ad_group.resource_name
        ag_id = str(row.ad_group.id)
        break
    if not ag_rn or not ag_id:
        print("No ad group found for campaign.", file=sys.stderr)
        return 1

    existing: set[tuple[str, str]] = set()
    q_kw = f"""
        SELECT ad_group_criterion.keyword.text, ad_group_criterion.keyword.match_type
        FROM ad_group_criterion
        WHERE ad_group.id = {ag_id}
          AND ad_group_criterion.type = KEYWORD
          AND ad_group_criterion.negative = FALSE
          AND ad_group_criterion.status != 'REMOVED'
    """
    for row in gas.search(customer_id=cid, query=q_kw):
        t = (row.ad_group_criterion.keyword.text or "").strip().lower()
        m = _match_label(row.ad_group_criterion.keyword.match_type)
        if t:
            existing.add((t, m))

    to_add: list[tuple[str, object]] = []
    for row in defaults.get("keywords", []):
        text = (row.get("text") or "").strip()
        if not text:
            continue
        mt = _match_type_enum(client, row.get("match", "PHRASE"))
        key = (text.lower(), _match_label(mt))
        if key not in existing:
            to_add.append((text, mt))

    print("Ad group:", ag_rn)
    print("Existing positive keywords:", len(existing))
    print("To add:", len(to_add))
    for text, mt in to_add:
        print(" ", text, "(" + _match_label(mt) + ")")

    if not to_add:
        print("Nothing to do.")
        return 0

    ops: list = []
    temp = _KW_TEMP_START
    for text, mt in to_add:
        mo = client.get_type("MutateOperation")
        kc = mo.ad_group_criterion_operation.create
        kc.resource_name = gas.ad_group_criterion_path(cid, ag_id, str(temp))
        temp -= 1
        kc.ad_group = ag_rn
        kc.status = client.enums.AdGroupCriterionStatusEnum.ENABLED
        kc.negative = False
        kc.keyword.text = text
        kc.keyword.match_type = mt
        ops.append(mo)

    req = client.get_type("MutateGoogleAdsRequest")
    req.customer_id = cid
    req.mutate_operations.extend(ops)
    req.validate_only = bool(args.dry_run)

    try:
        gas.mutate(request=req)
    except GoogleAdsException as exc:
        print(str(exc).split("\n", 1)[0], file=sys.stderr)
        if getattr(exc, "failure", None) and exc.failure.errors:
            for e in exc.failure.errors:
                print(" ", e.message, file=sys.stderr)
        return 1

    if args.dry_run:
        print("OK — validation passed.")
    else:
        print("OK — keywords added.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
