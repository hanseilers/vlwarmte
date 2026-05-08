#!/usr/bin/env python3
"""E2E: vul productie-offerteformulier (Playwright), wacht op mail op info@, verwijder testmail.

Standaard: **Playwright** opent de echte contactpagina — dezelfde JavaScript en form-`action` als
een bezoeker. Daarmee vermijd je een mis-match tussen handmatige POST-URL en wat de site echt doet.

Optioneel: `--http-post` voor directe POST (alleen voor debug; kan 404 geven als Formspree-hash
niet meer geldig is).

Secrets: zie secrets/hostnet-mail.env.example (IMAP_*). CI: GitHub Actions secrets.
"""

from __future__ import annotations

import argparse
import imaplib
import os
import re
import ssl
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
import uuid
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
_DEFAULT_ENV = REPO_ROOT / "secrets" / "hostnet-mail.env"
_DEFAULT_FORMSPREE = "https://formspree.io/f/29885138860528105515"
_DEFAULT_BASE = "https://www.vlwarmte.nl"
_MAILBOXES = ("INBOX", "INBOX/Leads", "INBOX/Overig", "INBOX/Systeem")


def _truthy(v: str | None) -> bool:
    if not v:
        return False
    return v.strip().lower() in ("1", "true", "yes", "on")


def load_env_file(path: Path) -> None:
    if not path.is_file():
        return
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, _, val = line.partition("=")
        key = key.strip()
        val = val.strip().strip('"').strip("'")
        if key and key not in os.environ:
            os.environ[key] = val


def connect_imap() -> imaplib.IMAP4_SSL:
    host = (os.environ.get("IMAP_HOST") or "imap.hostnet.nl").strip()
    port = int((os.environ.get("IMAP_PORT") or "993").strip())
    user = (os.environ.get("IMAP_USER") or "").strip()
    password = (os.environ.get("IMAP_PASSWORD") or "").strip()
    if not user or not password:
        raise SystemExit("Missing IMAP_USER or IMAP_PASSWORD for E2E inbox check.")
    ctx = ssl.create_default_context()
    conn = imaplib.IMAP4_SSL(host, port, ssl_context=ctx)
    conn.login(user, password)
    return conn


def _select(conn: imaplib.IMAP4_SSL, mailbox: str, *, readonly: bool) -> bool:
    typ, _ = conn.select(mailbox, readonly=readonly)
    return typ == "OK"


def _uid_list_desc(conn: imaplib.IMAP4_SSL, limit: int) -> list[int]:
    typ, data = conn.uid("SEARCH", None, "ALL")
    if typ != "OK" or not data or not data[0]:
        return []
    raw = data[0].decode("ascii", errors="ignore").strip()
    if not raw:
        return []
    uids = [int(x) for x in raw.split() if x.isdigit()]
    uids.sort(reverse=True)
    return uids[:limit]


def _fetch_rfc822(conn: imaplib.IMAP4_SSL, uid: int) -> bytes:
    typ, data = conn.uid("FETCH", str(uid), "(RFC822)")
    if typ != "OK" or not data:
        return b""
    for item in data:
        if isinstance(item, tuple) and len(item) >= 2 and isinstance(item[1], (bytes, bytearray)):
            return bytes(item[1])
    return b""


def _delete_uid(conn: imaplib.IMAP4_SSL, uid: int) -> None:
    typ, _ = conn.uid("STORE", str(uid), "+FLAGS", r"(\Deleted)")
    if typ != "OK":
        raise RuntimeError(f"STORE Deleted failed for uid {uid}")
    conn.expunge()


def _resolve_formspree_url(base_url: str) -> str:
    if (os.environ.get("E2E_FORMSPREE_URL") or "").strip():
        return os.environ["E2E_FORMSPREE_URL"].strip()
    contact = f"{base_url.rstrip('/')}/contact.html"
    req = urllib.request.Request(
        contact,
        headers={"User-Agent": "VLWarmte-E2E/1.0 (+https://www.vlwarmte.nl)"},
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            html = resp.read().decode("utf-8", errors="replace")
    except (urllib.error.URLError, OSError) as e:
        print(f"Could not fetch {contact}: {e}; using default Formspree URL.", file=sys.stderr)
        return _DEFAULT_FORMSPREE
    m = re.search(r"https://formspree\.io/f/[a-zA-Z0-9]+", html)
    if m:
        return m.group(0)
    print("No formspree.io URL in live contact.html; using default.", file=sys.stderr)
    return _DEFAULT_FORMSPREE


def _post_offerte(marker: str, formspree_url: str, base_url: str) -> None:
    message = (
        f"Dit is een automatische deploy-test van VLWarmte. Referentie: {marker}\n\n"
        "U kunt dit bericht negeren."
    )
    fields = {
        "soort_aanvraag": "Offerte",
        "name": "VLWarmte E2E Bot",
        "phone": "+31618817459",
        "email": "e2e-deploy-test@example.com",
        "region": "Zuidlaren (test)",
        "m2": "95",
        "vloerdiepte": "520",
        "ondergrond": "Beton",
        "projecttype": "Nieuwbouw",
        "planning": "Test — geen echte planning",
        "message": message,
    }
    body = urllib.parse.urlencode(fields).encode("utf-8")
    req = urllib.request.Request(
        formspree_url,
        data=body,
        method="POST",
        headers={
            "Content-Type": "application/x-www-form-urlencoded; charset=utf-8",
            "User-Agent": "VLWarmte-E2E/1.0 (+https://www.vlwarmte.nl)",
            "Referer": f"{base_url}/contact.html?modus=offerte",
            "Origin": base_url.rstrip("/"),
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=45) as resp:
            code = resp.getcode()
            if code not in (200, 302):
                print(f"Formspree HTTP {code}", file=sys.stderr)
    except urllib.error.HTTPError as e:
        body_err = e.read().decode(errors="replace")[:2000]
        raise SystemExit(f"Formspree HTTP error {e.code}: {body_err}") from e
    except urllib.error.URLError as e:
        raise SystemExit(f"Formspree request failed: {e}") from e


def _submit_offerte_playwright(base: str, marker: str, *, headed: bool) -> None:
    try:
        from playwright.sync_api import TimeoutError as PlaywrightTimeout
        from playwright.sync_api import sync_playwright
    except ImportError as e:
        raise SystemExit(
            "Playwright ontbreekt. Installeer: pip install -r scripts/requirements-e2e.txt\n"
            "Daarna: python -m playwright install chromium"
        ) from e

    message = (
        f"Dit is een automatische deploy-test van VLWarmte. Referentie: {marker}\n\n"
        "U kunt dit bericht negeren."
    )
    url = f"{base.rstrip('/')}/contact.html?modus=offerte#aanvraag"

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=not headed)
        try:
            context = browser.new_context(
                locale="nl-NL",
                viewport={"width": 1280, "height": 900},
                user_agent="VLWarmte-E2E/1.0 (+https://www.vlwarmte.nl)",
            )
            page = context.new_page()
            page.goto(url, wait_until="domcontentloaded", timeout=90000)
            page.wait_for_selector("#lead-form", state="visible", timeout=30000)

            page.get_by_role("button", name="Ik wil een offerte").click()
            page.locator("#m2").wait_for(state="visible", timeout=20000)

            page.locator("#name").fill("VLWarmte E2E Bot")
            page.locator("#phone").fill("+31618817459")
            page.locator("#email").fill("e2e-deploy-test@example.com")
            page.locator("#region").fill("Zuidlaren (test)")
            page.locator("#m2").fill("95")
            page.locator("#vloerdiepte").fill("520")
            page.locator("#ondergrond").select_option(label="Beton")
            page.locator("#projecttype").select_option(label="Nieuwbouw")
            page.locator("#planning").fill("Test — geen echte planning")
            page.locator("#message").fill(message)

            try:
                with page.expect_navigation(timeout=60000):
                    page.locator("form#lead-form button[type='submit']").click()
            except PlaywrightTimeout:
                status = page.locator("#lead-status").inner_text(timeout=5000)
                raise SystemExit(
                    f"Geen navigatie na Versturen (validatie of netwerk?). lead-status: {status!r}"
                ) from None

            final = page.url
            print(f"Navigated after submit: {final[:120]}…", file=sys.stderr)
        finally:
            browser.close()


def _find_marker_in_mailboxes(conn: imaplib.IMAP4_SSL, marker: str, scan_last: int) -> tuple[str, int] | None:
    for mbox in _MAILBOXES:
        if not _select(conn, mbox, readonly=True):
            continue
        for uid in _uid_list_desc(conn, scan_last):
            raw = _fetch_rfc822(conn, uid)
            if marker.encode() in raw or marker in raw.decode(errors="replace"):
                return (mbox, uid)
    return None


def _delete_in_mailbox(conn: imaplib.IMAP4_SSL, mbox: str, uid: int) -> None:
    if not _select(conn, mbox, readonly=False):
        raise SystemExit(f"Cannot select {mbox} for delete")
    _delete_uid(conn, uid)


def main() -> int:
    ap = argparse.ArgumentParser(description="E2E: offerte via Playwright + IMAP cleanup")
    ap.add_argument(
        "--http-post",
        action="store_true",
        help="Debug: directe POST naar Formspree-URL i.p.v. browser (kan 404 geven)",
    )
    ap.add_argument(
        "--headed",
        action="store_true",
        help="Chromium met venster (lokaal debuggen)",
    )
    ap.add_argument(
        "--env-file",
        type=Path,
        default=Path(os.environ.get("HOSTNET_MAIL_ENV", str(_DEFAULT_ENV))),
    )
    ns = ap.parse_args()

    load_env_file(ns.env_file)
    if _truthy(os.environ.get("E2E_SKIP")):
        print("E2E_SKIP set — skipping.", file=sys.stderr)
        return 0

    in_ci = os.environ.get("GITHUB_ACTIONS") == "true"
    if not (os.environ.get("IMAP_PASSWORD") or "").strip():
        if in_ci:
            print(
                "::warning::E2E skipped: set repository secrets IMAP_USER and IMAP_PASSWORD (Hostnet).",
                file=sys.stderr,
            )
            return 0
        raise SystemExit("Missing IMAP credentials. Create secrets/hostnet-mail.env or export IMAP_*.")

    marker = f"VLW-E2E-{uuid.uuid4().hex[:16]}"
    base = (os.environ.get("E2E_BASE_URL") or _DEFAULT_BASE).strip().rstrip("/")

    if ns.http_post:
        formspree = _resolve_formspree_url(base)
        print("Posting offerte via HTTP POST …", file=sys.stderr)
        _post_offerte(marker, formspree, base)
    else:
        print("Vullen en verzenden via Playwright (productiebrowser) …", file=sys.stderr)
        _submit_offerte_playwright(base, marker, headed=ns.headed)

    timeout = int(os.environ.get("E2E_INBOX_TIMEOUT_SEC", "240"))
    interval = int(os.environ.get("E2E_POLL_INTERVAL_SEC", "8"))
    scan_last = int(os.environ.get("E2E_SCAN_LAST", "40"))
    deadline = time.monotonic() + timeout

    conn = connect_imap()
    try:
        while time.monotonic() < deadline:
            hit = _find_marker_in_mailboxes(conn, marker, scan_last)
            if hit:
                mbox, uid = hit
                print(f"Found marker in {mbox} UID {uid}", file=sys.stderr)
                _delete_in_mailbox(conn, mbox, uid)
                print(f"Deleted {mbox} UID {uid}", file=sys.stderr)
                print("OK e2e_formspree_inbox")
                return 0
            time.sleep(interval)
        raise SystemExit(f"Timeout after {timeout}s: no mail containing {marker!r}")
    finally:
        try:
            conn.logout()
        except imaplib.IMAP4.error:
            pass


if __name__ == "__main__":
    raise SystemExit(main())
