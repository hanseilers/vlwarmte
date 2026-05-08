#!/usr/bin/env python3
"""E2E: vul productie-offerteformulier (Playwright), wacht op mail op info@, verwijder testmail.

Standaard: **Playwright** opent de echte contactpagina — dezelfde JavaScript en form-`action` als
een bezoeker. Daarmee vermijd je een mis-match tussen handmatige POST-URL en wat de site echt doet.

Optioneel: `--http-post` voor directe POST (alleen voor debug; kan 404 geven als Formspree-hash
niet meer geldig is).

Secrets: zie secrets/hostnet-mail.env.example (IMAP_*). CI: GitHub Actions secrets.
Marker-matching decodeert multipart mail (Formspree-HTML/base64), niet alleen ruwe RFC822.
Klant-e-mail in testsubmissions: E2E_CUSTOMER_EMAIL of default jceilers@icloud.com.
`--no-inbox` / `E2E_NO_INBOX=1`: Playwright op productie (default `E2E_BASE_URL`) zonder IMAP-wacht.

Optioneel **volledige keten**: ``--with-thankyou`` of ``E2E_WITH_THANKYOU=1`` — na het
vinden van de Formspree-mail met marker wordt ``inbox_auto_thankyou.py --include-e2e``
gedraaid (bedankmail naar het testadres), daarna wordt de testmail verwijderd.
"""

from __future__ import annotations

import argparse
import imaplib
import os
import re
import ssl
import subprocess
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
import uuid
from email import message_from_bytes
from email.header import decode_header, make_header
from pathlib import Path

import email.policy

REPO_ROOT = Path(__file__).resolve().parent.parent
_DEFAULT_ENV = REPO_ROOT / "secrets" / "hostnet-mail.env"
_DEFAULT_FORMSPREE = "https://formspree.io/f/xaqvdrvq"
_DEFAULT_BASE = "https://www.vlwarmte.nl"
_DEFAULT_E2E_CUSTOMER_EMAIL = "jceilers@icloud.com"
_MAILBOXES = (
    "INBOX",
    "INBOX/Leads",
    "INBOX/Overig",
    "INBOX/Systeem",
    "INBOX/Promoties",
    "INBOX/Spam",
)


def _e2e_customer_email() -> str:
    """Reply-to / klant-e-mail in testsubmissions. Overschrijf met E2E_CUSTOMER_EMAIL."""
    v = (os.environ.get("E2E_CUSTOMER_EMAIL") or "").strip()
    return v or _DEFAULT_E2E_CUSTOMER_EMAIL


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


def _decode_mime_header(raw: str | None) -> str:
    if not raw:
        return ""
    try:
        return str(make_header(decode_header(raw)))
    except Exception:
        return raw or ""


def _rfc822_contains_marker(raw: bytes, marker: str) -> bool:
    """Zoek marker in mail; Formspree stuurt vaak multipart HTML (base64) — dan staat de tekst niet raw in RFC822."""
    if not raw or not marker:
        return False
    ml = marker.lower()
    if marker.encode("utf-8") in raw:
        return True
    try:
        wire = raw.decode("utf-8", errors="ignore")
    except Exception:
        wire = ""
    if marker in wire or ml in wire.lower():
        return True
    try:
        msg = message_from_bytes(raw, policy=email.policy.default)
    except Exception:
        return False
    chunks: list[str] = []
    subj = _decode_mime_header(msg.get("Subject"))
    if subj:
        chunks.append(subj)
    if msg.is_multipart():
        for part in msg.walk():
            ctype = (part.get_content_type() or "").lower()
            if ctype not in ("text/plain", "text/html"):
                continue
            try:
                pl = part.get_payload(decode=True)
            except Exception:
                pl = None
            if isinstance(pl, bytes):
                cs = part.get_content_charset() or "utf-8"
                try:
                    chunks.append(pl.decode(cs, errors="replace"))
                except LookupError:
                    chunks.append(pl.decode("utf-8", errors="replace"))
            elif isinstance(pl, str):
                chunks.append(pl)
    else:
        try:
            pl = msg.get_payload(decode=True)
            if isinstance(pl, bytes):
                cs = msg.get_content_charset() or "utf-8"
                try:
                    chunks.append(pl.decode(cs, errors="replace"))
                except LookupError:
                    chunks.append(pl.decode("utf-8", errors="replace"))
        except Exception:
            pass
    blob = "\n".join(chunks).lower()
    return ml in blob


def _debug_imap_recent(conn: imaplib.IMAP4_SSL, scan_last: int) -> None:
    """Laatste berichten per map (onderwerp) — zet E2E_DEBUG_IMAP=1 bij timeout-debug."""
    print("E2E_DEBUG_IMAP: recente onderwerpen (max 5 per map):", file=sys.stderr)
    for mbox in _MAILBOXES:
        if not _select(conn, mbox, readonly=True):
            print(f"  {mbox}: (niet te openen)", file=sys.stderr)
            continue
        uids = _uid_list_desc(conn, scan_last)[:5]
        if not uids:
            print(f"  {mbox}: (leeg)", file=sys.stderr)
            continue
        for uid in uids:
            raw = _fetch_rfc822(conn, uid)
            try:
                msg = message_from_bytes(raw, policy=email.policy.default)
                subj = _decode_mime_header(msg.get("Subject"))
            except Exception as exc:
                subj = f"<parse {exc}>"
            print(f"  {mbox} uid={uid} {subj[:120]!r}", file=sys.stderr)


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
        "email": _e2e_customer_email(),
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
            page.locator("#email").fill(_e2e_customer_email())
            page.locator("#region").fill("Zuidlaren (test)")
            page.locator("#m2").fill("95")
            page.locator("#vloerdiepte").fill("520")
            page.locator("#ondergrond").select_option(label="Beton")
            page.locator("#projecttype").select_option(label="Nieuwbouw")
            page.locator("#planning").fill("Test — geen echte planning")
            page.locator("#message").fill(message)

            # Contact gebruikt fetch() naar Formspree: blijf op contact.html, succes in #lead-status
            url_before = page.url
            page.locator("form#lead-form button[type='submit']").click()

            try:
                page.locator("#lead-status.success").wait_for(state="visible", timeout=60000)
            except PlaywrightTimeout:
                status_text = ""
                try:
                    status_text = page.locator("#lead-status").inner_text(timeout=2000)
                except Exception:
                    pass
                raise SystemExit(
                    f"Geen success-status na Versturen (validatie of netwerk?). "
                    f"lead-status: {status_text!r}, url: {page.url!r}"
                ) from None

            if page.url != url_before:
                raise SystemExit(
                    f"Onverwachte navigatie na Versturen: {url_before!r} -> {page.url!r}. "
                    "Verwacht: blijven op contact.html (fetch i.p.v. redirect)."
                )

            status_text = page.locator("#lead-status").inner_text(timeout=2000)
            print(f"Inline success on {page.url[:120]}: {status_text!r}", file=sys.stderr)
        finally:
            browser.close()


def _submit_calc_playwright(base: str, marker: str, *, headed: bool) -> None:
    """Prijsindicatie calc-form: JS fetch() naar Formspree — geen volledige navigatie."""
    try:
        from playwright.sync_api import TimeoutError as PlaywrightTimeout
        from playwright.sync_api import sync_playwright
    except ImportError as e:
        raise SystemExit(
            "Playwright ontbreekt. Installeer: pip install -r scripts/requirements-e2e.txt\n"
            "Daarna: python -m playwright install chromium"
        ) from e

    url = f"{base.rstrip('/')}/prijsindicatie.html"
    uit = f"E2E prijscalculator (automatische test).\nReferentie: {marker}\n"

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
            # Form staat in #result; die is pas zichtbaar na wizard — voor E2E alleen tonen.
            page.evaluate(
                """() => {
                  const r = document.getElementById('result');
                  if (r) r.classList.add('is-visible');
                }"""
            )
            page.wait_for_selector("#calc-form", state="visible", timeout=30000)
            page.locator("#calc-form").scroll_into_view_if_needed()

            # type="hidden": geen fill() in Playwright — waarden via DOM zetten
            hidden_fields = {
                "f-product": "E2E test",
                "f-traject": "e2e_traject",
                "f-m2": "80",
                "f-type": "Nieuwbouw",
                "f-ondergrond": "beton",
                "f-zones": "1",
                "f-vloerdiepte": "500",
                "f-schuim-m2": "",
                "f-kruip-ondergrond": "",
                "f-prijs": "indicatie E2E",
                "f-uitgangspunten": uit,
            }
            page.evaluate(
                """(fields) => {
                  for (const [id, val] of Object.entries(fields)) {
                    const el = document.getElementById(id);
                    if (el) el.value = val;
                  }
                }""",
                hidden_fields,
            )

            page.locator("#c-name").fill("VLWarmte E2E Calc")
            page.locator("#c-phone").fill("+31618817459")
            page.locator("#c-email").fill(_e2e_customer_email())
            page.locator("#c-place").fill("Zuidlaren (test)")
            page.locator("#c-planning").fill("Test")

            page.locator("#calc-form button[type='submit']").click()
            try:
                page.locator("#calc-status .status-msg.ok").wait_for(state="visible", timeout=60000)
            except PlaywrightTimeout:
                status = page.locator("#calc-status").inner_text(timeout=5000)
                raise SystemExit(f"calc-form geen succes-status: {status!r}") from None
            print("calc-form: Formspree fetch OK (status-msg ok)", file=sys.stderr)
        finally:
            browser.close()


def _run_inbox_thankyou(env_file: Path, max_msgs: int) -> None:
    """Zelfde repo, apart proces: SMTP + IMAP-mark-read in inbox_auto_thankyou."""
    script = REPO_ROOT / "scripts" / "inbox_auto_thankyou.py"
    cmd = [
        sys.executable,
        str(script),
        "--include-e2e",
        "--max",
        str(max_msgs),
        "--env-file",
        str(env_file),
    ]
    print("Bedankmail-keten: " + " ".join(cmd), file=sys.stderr)
    r = subprocess.run(cmd, cwd=str(REPO_ROOT))
    if r.returncode != 0:
        raise SystemExit(f"inbox_auto_thankyou exited {r.returncode}")


def _wait_delete_marker(
    conn: imaplib.IMAP4_SSL,
    marker: str,
    scan_last: int,
    timeout: int,
    interval: int,
    *,
    env_file: Path | None = None,
    with_thankyou: bool = False,
    thankyou_max: int = 5,
) -> None:
    deadline = time.monotonic() + timeout
    while time.monotonic() < deadline:
        hit = _find_marker_in_mailboxes(conn, marker, scan_last)
        if hit:
            mbox, uid = hit
            print(f"Found marker in {mbox} UID {uid}", file=sys.stderr)
            if with_thankyou and env_file is not None:
                _run_inbox_thankyou(env_file, thankyou_max)
            _delete_in_mailbox(conn, mbox, uid)
            print(f"Deleted {mbox} UID {uid}", file=sys.stderr)
            return
        time.sleep(interval)
    if _truthy(os.environ.get("E2E_DEBUG_IMAP")):
        try:
            _debug_imap_recent(conn, scan_last)
        except Exception as exc:
            print(f"E2E_DEBUG_IMAP failed: {exc}", file=sys.stderr)
    raise SystemExit(
        f"Timeout after {timeout}s: no mail containing {marker!r}. "
        "Formspree levert wél — controleer IMAP_USER (zelfde inbox), triage-map, "
        "E2E_SCAN_LAST (te weinig recente berichten?), of zet E2E_DEBUG_IMAP=1. "
        "Alleen site-UI: --no-inbox / E2E_NO_INBOX=1."
    )


def _find_marker_in_mailboxes(conn: imaplib.IMAP4_SSL, marker: str, scan_last: int) -> tuple[str, int] | None:
    for mbox in _MAILBOXES:
        if not _select(conn, mbox, readonly=True):
            continue
        for uid in _uid_list_desc(conn, scan_last):
            raw = _fetch_rfc822(conn, uid)
            if _rfc822_contains_marker(raw, marker):
                return (mbox, uid)
    return None


def _delete_in_mailbox(conn: imaplib.IMAP4_SSL, mbox: str, uid: int) -> None:
    if not _select(conn, mbox, readonly=False):
        raise SystemExit(f"Cannot select {mbox} for delete")
    _delete_uid(conn, uid)


def main() -> int:
    ap = argparse.ArgumentParser(description="E2E: Formspree via Playwright + IMAP cleanup")
    ap.add_argument(
        "--form",
        choices=("lead", "calc", "both"),
        default="lead",
        help="lead=contact offerte; calc=prijsindicatie wizard-formulier; both=beide",
    )
    ap.add_argument(
        "--http-post",
        action="store_true",
        help="Alleen bij --form lead: debug POST i.p.v. Playwright",
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
    ap.add_argument(
        "--no-inbox",
        action="store_true",
        help="Alleen Playwright-flow op de site (succes-UI); geen IMAP-wacht of verwijderen. "
        "Ook: omgeving E2E_NO_INBOX=1.",
    )
    ap.add_argument(
        "--with-thankyou",
        action="store_true",
        help="Na vinden van testmail: inbox_auto_thankyou --include-e2e, daarna verwijderen",
    )
    ap.add_argument(
        "--thankyou-max",
        type=int,
        default=5,
        metavar="N",
        help="Max berichten door te geven aan inbox_auto_thankyou (default 5)",
    )
    ns = ap.parse_args()

    load_env_file(ns.env_file)
    if _truthy(os.environ.get("E2E_SKIP")):
        print("E2E_SKIP set — skipping.", file=sys.stderr)
        return 0

    base = (os.environ.get("E2E_BASE_URL") or _DEFAULT_BASE).strip().rstrip("/")
    no_inbox = bool(ns.no_inbox) or _truthy(os.environ.get("E2E_NO_INBOX"))

    in_ci = os.environ.get("GITHUB_ACTIONS") == "true"
    if not no_inbox and not (os.environ.get("IMAP_PASSWORD") or "").strip():
        if in_ci:
            print(
                "::warning::E2E skipped: set repository secrets IMAP_USER and IMAP_PASSWORD (Hostnet).",
                file=sys.stderr,
            )
            return 0
        raise SystemExit("Missing IMAP credentials. Create secrets/hostnet-mail.env or export IMAP_*.")

    if no_inbox:
        markers: list[str] = []
        if ns.form in ("lead", "both"):
            markers.append(f"VLW-E2E-{uuid.uuid4().hex[:16]}")
        if ns.form in ("calc", "both"):
            markers.append(f"VLW-E2E-{uuid.uuid4().hex[:16]}")
        print("E2E_NO_INBOX: alleen UI, geen mailbox.", file=sys.stderr)
        if ns.form in ("lead", "both"):
            m = markers[0]
            if ns.http_post:
                formspree = _resolve_formspree_url(base)
                print("Posting offerte via HTTP POST …", file=sys.stderr)
                _post_offerte(m, formspree, base)
            else:
                print("Lead: Playwright contact offerte …", file=sys.stderr)
                _submit_offerte_playwright(base, m, headed=ns.headed)
            print("OK e2e lead (no-inbox)", file=sys.stderr)
        if ns.form in ("calc", "both"):
            m = markers[-1] if ns.form == "both" else markers[0]
            if ns.http_post:
                raise SystemExit("--http-post werkt alleen met --form lead")
            print("Calc: Playwright prijsindicatie formulier …", file=sys.stderr)
            _submit_calc_playwright(base, m, headed=ns.headed)
            print("OK e2e calc (no-inbox)", file=sys.stderr)
        print("OK e2e_formspree_inbox (no-inbox)")
        return 0

    timeout = int(os.environ.get("E2E_INBOX_TIMEOUT_SEC", "240"))
    interval = int(os.environ.get("E2E_POLL_INTERVAL_SEC", "8"))
    scan_last = int(os.environ.get("E2E_SCAN_LAST", "80"))
    with_ty = bool(ns.with_thankyou) or _truthy(os.environ.get("E2E_WITH_THANKYOU"))
    ty_max = max(1, int(ns.thankyou_max))

    def run_lead(marker: str) -> None:
        if ns.http_post:
            formspree = _resolve_formspree_url(base)
            print("Posting offerte via HTTP POST …", file=sys.stderr)
            _post_offerte(marker, formspree, base)
        else:
            print("Lead: Playwright contact offerte …", file=sys.stderr)
            _submit_offerte_playwright(base, marker, headed=ns.headed)

    def run_calc(marker: str) -> None:
        if ns.http_post:
            raise SystemExit("--http-post werkt alleen met --form lead")
        print("Calc: Playwright prijsindicatie formulier …", file=sys.stderr)
        _submit_calc_playwright(base, marker, headed=ns.headed)

    markers: list[str] = []
    if ns.form in ("lead", "both"):
        markers.append(f"VLW-E2E-{uuid.uuid4().hex[:16]}")
    if ns.form in ("calc", "both"):
        markers.append(f"VLW-E2E-{uuid.uuid4().hex[:16]}")

    conn = connect_imap()
    try:
        if ns.form in ("lead", "both"):
            m = markers[0]
            run_lead(m)
            _wait_delete_marker(
                conn,
                m,
                scan_last,
                timeout,
                interval,
                env_file=ns.env_file,
                with_thankyou=with_ty,
                thankyou_max=ty_max,
            )
            print("OK e2e lead", file=sys.stderr)
        if ns.form in ("calc", "both"):
            m = markers[-1] if ns.form == "both" else markers[0]
            run_calc(m)
            _wait_delete_marker(
                conn,
                m,
                scan_last,
                timeout,
                interval,
                env_file=ns.env_file,
                with_thankyou=with_ty,
                thankyou_max=ty_max,
            )
            print("OK e2e calc", file=sys.stderr)
        print("OK e2e_formspree_inbox")
        return 0
    finally:
        try:
            conn.logout()
        except imaplib.IMAP4.error:
            pass


if __name__ == "__main__":
    raise SystemExit(main())
