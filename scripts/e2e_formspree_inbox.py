#!/usr/bin/env python3
"""E2E: POST offerte to production Formspree, wait for mail at info@, verify marker, delete.

Uses the same Formspree endpoint as contact.html. Loads IMAP from secrets/hostnet-mail.env
or from environment variables (GitHub Actions secrets).

Env (see secrets/hostnet-mail.env.example + workflow comments):
  IMAP_HOST, IMAP_PORT, IMAP_USER, IMAP_PASSWORD
  E2E_FORMSPREE_URL — optional; default matches contact.html
  E2E_BASE_URL — default https://www.vlwarmte.nl (Referer only)
  E2E_SKIP — if set to 1/true, exit 0 without running (optional CI opt-out)

Exit codes: 0 success or skipped, 1 failure.
"""

from __future__ import annotations

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
# Fallback if live contact.html cannot be read (prefer resolving from production)
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
    m = re.search(r'https://formspree\.io/f/[a-zA-Z0-9]+', html)
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
        body = e.read().decode(errors="replace")[:2000]
        raise SystemExit(f"Formspree HTTP error {e.code}: {body}") from e
    except urllib.error.URLError as e:
        raise SystemExit(f"Formspree request failed: {e}") from e


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
    load_env_file(Path(os.environ.get("HOSTNET_MAIL_ENV", str(_DEFAULT_ENV))))
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
    formspree = _resolve_formspree_url(base)

    print("Posting offerte to Formspree …", file=sys.stderr)
    _post_offerte(marker, formspree, base)

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
