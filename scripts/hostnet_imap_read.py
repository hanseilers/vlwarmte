#!/usr/bin/env python3
"""Hostnet mail: IMAP (read, move, copy) + SMTP (send).

Loads secrets from secrets/hostnet-mail.env (same pattern as google-ads.env).
Stdlib only: imaplib, smtplib, ssl, email.

Examples:
  python scripts/hostnet_imap_read.py ping
  python scripts/hostnet_imap_read.py list-mailboxes
  python scripts/hostnet_imap_read.py recent --limit 15
  python scripts/hostnet_imap_read.py send --to you@example.com --subject Test --body "Hello"
  python scripts/hostnet_imap_read.py send-customer --to … --subject … --body-html-file scripts/data/email_fragment_offertebevestiging.nl.html
  python scripts/hostnet_imap_read.py move --uid 5 --to-folder Trash
  python scripts/hostnet_imap_read.py copy --uid 5 --to-folder Archive
  python scripts/hostnet_imap_read.py triage
  python scripts/hostnet_imap_read.py triage --dry-run
"""

from __future__ import annotations

import argparse
import html as html_module
import imaplib
import json
import os
import re
import smtplib
import ssl
import sys
from datetime import datetime, timedelta, timezone
from email import message_from_bytes
from email.header import decode_header, make_header
from email.message import EmailMessage, Message
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
_DEFAULT_ENV = REPO_ROOT / "secrets" / "hostnet-mail.env"
_DEFAULT_TRIAGE_RULES = REPO_ROOT / "scripts" / "data" / "hostnet_mail_triage.json"
_DEFAULT_CUSTOMER_TEMPLATE = REPO_ROOT / "scripts" / "data" / "email_vlwarmte_customer_template.html"


def load_env_file(path: Path) -> None:
    if not path.is_file():
        return
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        if "=" not in line:
            continue
        key, _, val = line.partition("=")
        key = key.strip()
        val = val.strip().strip('"').strip("'")
        if key and key not in os.environ:
            os.environ[key] = val


def _decode_mime_header(raw: str | None) -> str:
    if not raw:
        return ""
    try:
        return str(make_header(decode_header(raw)))
    except Exception:
        return raw


def connect_imap() -> imaplib.IMAP4_SSL:
    host = (os.environ.get("IMAP_HOST") or "imap.hostnet.nl").strip()
    port_s = (os.environ.get("IMAP_PORT") or "993").strip()
    user = (os.environ.get("IMAP_USER") or "").strip()
    password = (os.environ.get("IMAP_PASSWORD") or "").strip()
    try:
        port = int(port_s)
    except ValueError as e:
        raise SystemExit(f"IMAP_PORT must be an integer, got {port_s!r}") from e
    if not user or not password:
        raise SystemExit(
            "Missing IMAP_USER or IMAP_PASSWORD. "
            f"Set them in {_DEFAULT_ENV} (see secrets/hostnet-mail.env.example)."
        )
    ctx = ssl.create_default_context()
    conn = imaplib.IMAP4_SSL(host, port, ssl_context=ctx)
    conn.login(user, password)
    return conn


def _smtp_creds() -> tuple[str, int, str, str]:
    host = (os.environ.get("SMTP_HOST") or "smtp.hostnet.nl").strip()
    port_s = (os.environ.get("SMTP_PORT") or "587").strip()
    try:
        port = int(port_s)
    except ValueError as e:
        raise SystemExit(f"SMTP_PORT must be an integer, got {port_s!r}") from e
    user = (os.environ.get("SMTP_USER") or os.environ.get("IMAP_USER") or "").strip()
    password = (os.environ.get("SMTP_PASSWORD") or os.environ.get("IMAP_PASSWORD") or "").strip()
    if not user or not password:
        raise SystemExit(
            "Missing SMTP/IMAP credentials for send. "
            "Set IMAP_USER + IMAP_PASSWORD (or SMTP_USER + SMTP_PASSWORD) in hostnet-mail.env."
        )
    return host, port, user, password


def send_smtp(msg: EmailMessage) -> None:
    host, port, user, password = _smtp_creds()
    ctx = ssl.create_default_context()
    with smtplib.SMTP(host, port, timeout=60) as smtp:
        smtp.ehlo()
        smtp.starttls(context=ctx)
        smtp.ehlo()
        smtp.login(user, password)
        smtp.send_message(msg)


def cmd_ping(_: argparse.Namespace) -> int:
    conn = connect_imap()
    try:
        typ, data = conn.capability()
        print("OK imap", typ, (data[0][:120] + b"...") if data and len(data[0]) > 120 else data)
    finally:
        try:
            conn.logout()
        except imaplib.IMAP4.error:
            pass

    host, port, user, password = _smtp_creds()
    ctx = ssl.create_default_context()
    with smtplib.SMTP(host, port, timeout=30) as smtp:
        smtp.ehlo()
        smtp.starttls(context=ctx)
        smtp.ehlo()
        smtp.login(user, password)
    print("OK smtp login", host, port)
    return 0


def cmd_list_mailboxes(_: argparse.Namespace) -> int:
    conn = connect_imap()
    try:
        typ, data = conn.list()
        if typ != "OK":
            print("LIST failed:", typ, data, file=sys.stderr)
            return 1
        for line in data or []:
            if isinstance(line, bytes):
                print(line.decode("utf-8", errors="replace"))
            else:
                print(line)
    finally:
        try:
            conn.logout()
        except imaplib.IMAP4.error:
            pass
    return 0


def _select(conn: imaplib.IMAP4_SSL, mailbox: str, *, readonly: bool) -> None:
    typ, _ = conn.select(mailbox, readonly=readonly)
    if typ != "OK":
        raise SystemExit(f'SELECT {mailbox!r} failed: {typ}')


def _uid_search_all(conn: imaplib.IMAP4_SSL) -> list[int]:
    typ, data = conn.uid("SEARCH", None, "ALL")
    if typ != "OK" or not data or not data[0]:
        return []
    raw = data[0].decode("ascii", errors="ignore").strip()
    if not raw:
        return []
    uids: list[int] = []
    for part in raw.split():
        try:
            uids.append(int(part))
        except ValueError:
            continue
    return uids


def _uid_search_since(conn: imaplib.IMAP4_SSL, since: datetime) -> list[int]:
    imap_date = since.strftime("%d-%b-%Y")
    typ, data = conn.uid("SEARCH", None, "SINCE", imap_date)
    if typ != "OK" or not data or not data[0]:
        return []
    raw = data[0].decode("ascii", errors="ignore").strip()
    if not raw:
        return []
    uids: list[int] = []
    for part in raw.split():
        try:
            uids.append(int(part))
        except ValueError:
            continue
    return uids


def _fetch_headers(conn: imaplib.IMAP4_SSL, uid: int) -> dict[str, str]:
    typ, data = conn.uid("FETCH", str(uid), "(BODY.PEEK[HEADER])")
    if typ != "OK" or not data:
        return {"uid": str(uid), "error": "fetch failed"}
    header_bytes = b""
    for item in data:
        if isinstance(item, tuple) and len(item) >= 2 and isinstance(item[1], (bytes, bytearray)):
            header_bytes = bytes(item[1])
            break
    msg = message_from_bytes(header_bytes)
    return {
        "uid": str(uid),
        "subject": _decode_mime_header(msg.get("Subject")),
        "from": _decode_mime_header(msg.get("From")),
        "to": _decode_mime_header(msg.get("To")),
        "date": (msg.get("Date") or "").strip(),
    }


def cmd_recent(ns: argparse.Namespace) -> int:
    mailbox = (os.environ.get("IMAP_MAILBOX") or "INBOX").strip() or "INBOX"
    conn = connect_imap()
    try:
        _select(conn, mailbox, readonly=True)
        if ns.since_days is not None:
            since = datetime.now(timezone.utc) - timedelta(days=ns.since_days)
            uids = _uid_search_since(conn, since)
        else:
            uids = _uid_search_all(conn)
        tail = uids[-ns.limit :] if len(uids) > ns.limit else uids
        rows: list[dict[str, str]] = []
        for uid in tail:
            rows.append(_fetch_headers(conn, uid))
        if ns.json:
            print(json.dumps({"mailbox": mailbox, "messages": rows}, ensure_ascii=False, indent=2))
        else:
            for r in rows:
                print(f"{r.get('uid','')}\t{r.get('date','')}\t{r.get('from','')}\t{r.get('subject','')}")
    finally:
        try:
            conn.close()
        except Exception:
            pass
        try:
            conn.logout()
        except imaplib.IMAP4.error:
            pass
    return 0


def cmd_headers(ns: argparse.Namespace) -> int:
    mailbox = (os.environ.get("IMAP_MAILBOX") or "INBOX").strip() or "INBOX"
    conn = connect_imap()
    try:
        _select(conn, mailbox, readonly=True)
        r = _fetch_headers(conn, ns.uid)
        if ns.json:
            print(json.dumps(r, ensure_ascii=False, indent=2))
        else:
            for k, v in r.items():
                print(f"{k}: {v}")
    finally:
        try:
            conn.close()
        except Exception:
            pass
        try:
            conn.logout()
        except imaplib.IMAP4.error:
            pass
    return 0


def _imap_close_logout(conn: imaplib.IMAP4_SSL) -> None:
    try:
        conn.close()
    except Exception:
        pass
    try:
        conn.logout()
    except imaplib.IMAP4.error:
        pass


def _move_uid(conn: imaplib.IMAP4_SSL, uid: int, dest_mailbox: str) -> None:
    """Move message UID from the currently selected mailbox to dest_mailbox."""
    uid_s = str(uid)
    typ, dat = conn.uid("MOVE", uid_s, dest_mailbox)
    if typ == "OK":
        return
    typ_c, dat_c = conn.uid("COPY", uid_s, dest_mailbox)
    if typ_c != "OK":
        hint = (dat_c[-1] if dat_c else b"").decode(errors="replace")
        raise SystemExit(
            f"MOVE returned {typ!r}; COPY failed with {typ_c!r}. "
            f"Check --to-folder matches list-mailboxes exactly. Server said: {hint!r}"
        )
    typ_s, dat_s = conn.uid("STORE", uid_s, "+FLAGS", r"(\Deleted)")
    if typ_s != "OK":
        raise SystemExit(f"STORE \\Deleted failed after COPY: {typ_s!r} {dat_s!r}")
    conn.expunge()


def _copy_uid(conn: imaplib.IMAP4_SSL, uid: int, dest_mailbox: str) -> None:
    uid_s = str(uid)
    typ, dat = conn.uid("COPY", uid_s, dest_mailbox)
    if typ != "OK":
        hint = (dat[-1] if dat else b"").decode(errors="replace")
        raise SystemExit(f"COPY failed: {typ!r} {hint!r}")


def cmd_move(ns: argparse.Namespace) -> int:
    source = (ns.from_mailbox or os.environ.get("IMAP_MAILBOX") or "INBOX").strip() or "INBOX"
    dest = ns.to_folder.strip()
    if not dest:
        raise SystemExit("--to-folder is required (exact name from list-mailboxes)")
    conn = connect_imap()
    try:
        _select(conn, source, readonly=False)
        if ns.dry_run:
            print(f"dry-run: would move UID {ns.uid} from {source!r} to {dest!r}")
            return 0
        _move_uid(conn, ns.uid, dest)
        print("OK moved", ns.uid, source, "->", dest)
    finally:
        _imap_close_logout(conn)
    return 0


def cmd_copy(ns: argparse.Namespace) -> int:
    source = (ns.from_mailbox or os.environ.get("IMAP_MAILBOX") or "INBOX").strip() or "INBOX"
    dest = ns.to_folder.strip()
    if not dest:
        raise SystemExit("--to-folder is required (exact name from list-mailboxes)")
    conn = connect_imap()
    try:
        _select(conn, source, readonly=False)
        if ns.dry_run:
            print(f"dry-run: would copy UID {ns.uid} from {source!r} to {dest!r}")
            return 0
        _copy_uid(conn, ns.uid, dest)
        print("OK copied", ns.uid, source, "->", dest)
    finally:
        _imap_close_logout(conn)
    return 0


def cmd_send(ns: argparse.Namespace) -> int:
    mail_from = (os.environ.get("MAIL_FROM") or os.environ.get("IMAP_USER") or "").strip()
    if not mail_from:
        raise SystemExit("Set MAIL_FROM or IMAP_USER for the From header.")
    if (ns.body is None) == (ns.body_file is None):
        raise SystemExit("Provide exactly one of --body or --body-file.")

    if ns.body_file:
        body = Path(ns.body_file).read_text(encoding="utf-8")
    else:
        body = ns.body or ""

    msg = EmailMessage()
    msg["From"] = mail_from
    msg["To"] = ns.to.strip()
    msg["Subject"] = ns.subject
    if ns.reply_to:
        msg["Reply-To"] = ns.reply_to.strip()
    subtype = "html" if ns.html else "plain"
    msg.set_content(body, subtype=subtype, charset="utf-8")

    if ns.dry_run:
        print("dry-run: would send:")
        print(msg.as_string()[:4000])
        if len(msg.as_string()) > 4000:
            print("... [truncated]")
        return 0

    send_smtp(msg)
    print("OK sent to", ns.to)
    return 0


_DEFAULT_CUSTOMER_DISCLAIMER = (
    "U ontvangt deze e-mail omdat u contact met ons heeft gehad. Antwoord gerust op dit bericht."
)


def render_customer_email_html(
    *,
    body_html: str,
    title: str,
    preheader: str,
    template_path: Path | None = None,
    footer_disclaimer: str | None = None,
) -> str:
    path = template_path or _DEFAULT_CUSTOMER_TEMPLATE
    tpl = path.read_text(encoding="utf-8")
    disc = footer_disclaimer if footer_disclaimer is not None else _DEFAULT_CUSTOMER_DISCLAIMER
    return (
        tpl.replace("{{VLW_EMAIL_BODY}}", body_html)
        .replace("{{VLW_EMAIL_TITLE}}", html_module.escape(title))
        .replace("{{VLW_EMAIL_PREHEADER}}", html_module.escape(preheader))
        .replace("{{VLW_EMAIL_DISCLAIMER}}", html_module.escape(disc))
    )


def _plain_paragraphs_to_html(text: str) -> str:
    blocks = [p.strip() for p in re.split(r"\n\s*\n", text) if p.strip()]
    if not blocks:
        return '<p style="margin:0 0 16px 0;"></p>'
    parts: list[str] = []
    for i, b in enumerate(blocks):
        margin = "0" if i == len(blocks) - 1 else "0 0 16px 0"
        para = html_module.escape(b).replace("\n", "<br />\n")
        parts.append(f'<p style="margin:{margin};">{para}</p>')
    return "".join(parts)


def _html_to_plain_fallback(html: str) -> str:
    t = re.sub(r"(?is)<(script|style)\b[^>]*>.*?</\1>", " ", html)
    t = re.sub(r"(?is)<br\s*/?>", "\n", t)
    t = re.sub(r"(?is)</p\s*>", "\n\n", t)
    t = re.sub(r"(?is)<[^>]+>", " ", t)
    t = html_module.unescape(t)
    t = re.sub(r"[ \t]+", " ", t)
    t = re.sub(r"\n{3,}", "\n\n", t)
    return t.strip()[:8000]


def cmd_send_customer(ns: argparse.Namespace) -> int:
    src: list[str] = []
    if ns.body_html is not None:
        src.append("html")
    if ns.body_html_file is not None:
        src.append("file")
    if ns.body_text is not None:
        src.append("text")
    if len(src) != 1:
        raise SystemExit("Provide exactly one of: --body-html, --body-html-file, --body-text")

    if src[0] == "file":
        inner = Path(ns.body_html_file).expanduser().read_text(encoding="utf-8")
    elif src[0] == "text":
        inner = _plain_paragraphs_to_html(ns.body_text or "")
    else:
        inner = (ns.body_html or "").strip()
        if not inner:
            raise SystemExit("--body-html is empty")

    title = (ns.subject or "VLWarmte").strip()
    pre = (ns.preheader or "").strip()
    if not pre:
        pre = title if len(title) <= 140 else (title[:137] + "…")

    full_html = render_customer_email_html(
        body_html=inner,
        title=title,
        preheader=pre,
        template_path=ns.template,
        footer_disclaimer=ns.footer_disclaimer.strip() if ns.footer_disclaimer else None,
    )
    plain = _html_to_plain_fallback(inner) or _html_to_plain_fallback(full_html)

    mail_from = (os.environ.get("MAIL_FROM") or os.environ.get("IMAP_USER") or "").strip()
    if not mail_from:
        raise SystemExit("Set MAIL_FROM or IMAP_USER for the From header.")

    msg = EmailMessage()
    msg["From"] = mail_from
    msg["To"] = ns.to.strip()
    msg["Subject"] = ns.subject
    if ns.reply_to:
        msg["Reply-To"] = ns.reply_to.strip()
    msg.set_content(plain, subtype="plain", charset="utf-8")
    msg.add_alternative(full_html, subtype="html", charset="utf-8")

    if ns.dry_run:
        print("dry-run: would send HTML customer mail to", ns.to, file=sys.stderr)
        print(full_html[:6000])
        if len(full_html) > 6000:
            print("... [truncated]", file=sys.stderr)
        return 0

    send_smtp(msg)
    print("OK sent customer template to", ns.to)
    return 0


def _load_triage_config(path: Path) -> dict:
    if not path.is_file():
        raise SystemExit(f"Triage rules file missing: {path}")
    return json.loads(path.read_text(encoding="utf-8"))


def _collect_ensure_folders(cfg: dict) -> list[str]:
    out: list[str] = []
    for f in cfg.get("ensure_folders", []):
        f = (f or "").strip()
        if f and f.upper() != "INBOX" and f not in out:
            out.append(f)
    for rule in cfg.get("rules", []):
        f = (rule.get("folder") or "").strip()
        if f and f.upper() != "INBOX" and f not in out:
            out.append(f)
    return out


def _ensure_mailbox(conn: imaplib.IMAP4_SSL, name: str) -> None:
    typ, data = conn.create(name)
    if typ == "OK":
        print(f"Created mailbox {name}", file=sys.stderr)
        return
    tail = b""
    if data:
        last = data[-1]
        tail = last if isinstance(last, bytes) else str(last).encode()
    t = tail.decode(errors="replace").upper()
    if "EXISTS" in t or "ALREADY" in t:
        return
    raise SystemExit(f"CREATE {name!r} failed: {typ} {tail!r}")


def _header_present(msg: Message, header_name: str) -> bool:
    want = header_name.lower()
    for k in msg.keys():
        if k.lower() == want:
            if (msg.get(k) or "").strip():
                return True
    return False


def _rule_matches(msg: Message, rule: dict, subj: str, from_l: str) -> bool:
    if rule.get("match_always"):
        return True
    for s in rule.get("from_contains_any", []):
        if str(s).lower() in from_l:
            return True
    for s in rule.get("subject_contains_any", []):
        if str(s).lower() in subj:
            return True
    allp = rule.get("from_contains_all")
    if allp and isinstance(allp, list) and all(str(p).lower() in from_l for p in allp):
        return True
    h = rule.get("has_header")
    if h and _header_present(msg, str(h)):
        return True
    if rule.get("precedence_bulk"):
        pv = (msg.get("Precedence") or "").strip().lower()
        if pv and ("bulk" in pv or "list" in pv or "junk" in pv):
            return True
    return False


def _classify_message(msg: Message, rules: list[dict]) -> tuple[str, str]:
    subj = (_decode_mime_header(msg.get("Subject")) or "").lower()
    from_l = (_decode_mime_header(msg.get("From")) or "").lower()
    for rule in rules:
        rid = rule.get("id")
        if not rid:
            continue
        if _rule_matches(msg, rule, subj, from_l):
            return ((rule.get("folder") or "INBOX/Overig").strip(), str(rid))
    return ("INBOX/Overig", "fallback")


def _fetch_header_message(conn: imaplib.IMAP4_SSL, uid: int) -> Message:
    typ, data = conn.uid("FETCH", str(uid), "(BODY.PEEK[HEADER])")
    if typ != "OK" or not data:
        raise SystemExit(f"FETCH headers failed for uid {uid}: {typ}")
    header_bytes = b""
    for item in data:
        if isinstance(item, tuple) and len(item) >= 2 and isinstance(item[1], (bytes, bytearray)):
            header_bytes = bytes(item[1])
            break
    if not header_bytes:
        raise SystemExit(f"Empty header fetch for uid {uid}")
    return message_from_bytes(header_bytes)


def cmd_triage(ns: argparse.Namespace) -> int:
    cfg = _load_triage_config(ns.rules)
    rules = cfg.get("rules", [])
    if not rules:
        raise SystemExit("Triage config has no rules.")

    will_move = not ns.dry_run

    source = (ns.mailbox or "INBOX").strip() or "INBOX"
    conn = connect_imap()
    try:
        for folder in _collect_ensure_folders(cfg):
            _ensure_mailbox(conn, folder)

        _select(conn, source, readonly=False)
        uids = _uid_search_all(conn)
        plans: list[dict[str, str]] = []
        for uid in uids:
            msg = _fetch_header_message(conn, uid)
            dest, rule_id = _classify_message(msg, rules)
            plans.append(
                {
                    "uid": str(uid),
                    "folder": dest,
                    "rule": rule_id,
                    "subject": _decode_mime_header(msg.get("Subject"))[:500],
                    "from": _decode_mime_header(msg.get("From"))[:500],
                }
            )

        if ns.json:
            print(
                json.dumps(
                    {"mailbox": source, "applied": will_move, "moves": plans},
                    ensure_ascii=False,
                    indent=2,
                )
            )
        else:
            for row in plans:
                subj = row["subject"].replace("\n", " ").replace("\r", "")[:70]
                frm = row["from"].replace("\n", " ").replace("\r", "")[:50]
                print(f"{row['uid']}\t{row['rule']}\t{row['folder']}\t{subj}\t{frm}")

        if not plans:
            print("No messages in", source, file=sys.stderr)
            return 0

        if not will_move:
            print(
                "# Dry-run: no messages moved. Run without --dry-run to move everything out of",
                source,
                file=sys.stderr,
            )
            return 0

        for row in plans:
            uid = int(row["uid"])
            dest = row["folder"]
            if dest == source:
                print(f"skip uid {uid}: target equals source", file=sys.stderr)
                continue
            _move_uid(conn, uid, dest)
        print(f"OK triaged {len(plans)} message(s) from {source}", file=sys.stderr)
    finally:
        _imap_close_logout(conn)
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Hostnet IMAP + SMTP mail helper")
    parser.add_argument(
        "--env-file",
        type=Path,
        default=_DEFAULT_ENV,
        help=f"Path to env file (default: {_DEFAULT_ENV})",
    )
    sub = parser.add_subparsers(dest="command", required=True)

    p_ping = sub.add_parser("ping", help="IMAP + SMTP login check")
    p_ping.set_defaults(func=cmd_ping)

    p_lm = sub.add_parser("list-mailboxes", help="IMAP LIST (folder names)")
    p_lm.set_defaults(func=cmd_list_mailboxes)

    p_rec = sub.add_parser("recent", help="Show newest messages (headers only)")
    p_rec.add_argument("--limit", type=int, default=20, help="Max messages (default 20)")
    p_rec.add_argument(
        "--since-days",
        type=int,
        default=None,
        metavar="N",
        help="Only UIDs with internal SINCE N days ago (server SEARCH)",
    )
    p_rec.add_argument("--json", action="store_true", help="JSON output")
    p_rec.set_defaults(func=cmd_recent)

    p_hdr = sub.add_parser("headers", help="Fetch headers for one UID")
    p_hdr.add_argument("--uid", type=int, required=True)
    p_hdr.add_argument("--json", action="store_true", help="JSON output")
    p_hdr.set_defaults(func=cmd_headers)

    p_mv = sub.add_parser("move", help="Move message UID to another folder (MOVE or COPY+delete)")
    p_mv.add_argument("--uid", type=int, required=True)
    p_mv.add_argument(
        "--to-folder",
        required=True,
        help="Destination mailbox (exact IMAP name, see list-mailboxes)",
    )
    p_mv.add_argument(
        "--from-mailbox",
        default=None,
        help="Source folder (default: IMAP_MAILBOX or INBOX)",
    )
    p_mv.add_argument("--dry-run", action="store_true", help="Print action only")
    p_mv.set_defaults(func=cmd_move)

    p_cp = sub.add_parser("copy", help="Copy message UID to another folder (original stays)")
    p_cp.add_argument("--uid", type=int, required=True)
    p_cp.add_argument("--to-folder", required=True, help="Destination mailbox")
    p_cp.add_argument("--from-mailbox", default=None, help="Source folder (default IMAP_MAILBOX or INBOX)")
    p_cp.add_argument("--dry-run", action="store_true")
    p_cp.set_defaults(func=cmd_copy)

    p_sd = sub.add_parser("send", help="Send mail via SMTP (STARTTLS)")
    p_sd.add_argument("--to", required=True, help="Recipient address")
    p_sd.add_argument("--subject", required=True)
    p_sd.add_argument("--body", default=None, help="Plain or HTML body (use with --html for HTML)")
    p_sd.add_argument("--body-file", default=None, help="Read body from UTF-8 file")
    p_sd.add_argument("--html", action="store_true", help="Body is HTML")
    p_sd.add_argument("--reply-to", default=None, dest="reply_to")
    p_sd.add_argument("--dry-run", action="store_true")
    p_sd.set_defaults(func=cmd_send)

    p_sc = sub.add_parser(
        "send-customer",
        help="Send multipart e-mail using scripts/data/email_vlwarmte_customer_template.html",
    )
    p_sc.add_argument("--to", required=True)
    p_sc.add_argument("--subject", required=True)
    p_sc.add_argument(
        "--preheader",
        default="",
        help="Short hidden preview (default: subject)",
    )
    p_sc.add_argument("--body-html", default=None, help="Inner HTML only (no full document)")
    p_sc.add_argument("--body-html-file", type=Path, default=None, help="UTF-8 file with inner HTML")
    p_sc.add_argument(
        "--body-text",
        default=None,
        help="Plain text; paragraphs separated by a blank line become HTML <p>",
    )
    p_sc.add_argument(
        "--template",
        type=Path,
        default=_DEFAULT_CUSTOMER_TEMPLATE,
        help=f"Outer template (default: {_DEFAULT_CUSTOMER_TEMPLATE})",
    )
    p_sc.add_argument("--reply-to", default=None, dest="reply_to")
    p_sc.add_argument(
        "--footer-disclaimer",
        default=None,
        dest="footer_disclaimer",
        help="Kleine grijze voetregel onder de kaart (default: klanttekst). Voor interne mails eigen tekst zetten.",
    )
    p_sc.add_argument("--dry-run", action="store_true")
    p_sc.set_defaults(func=cmd_send_customer)

    p_tr = sub.add_parser(
        "triage",
        help="Create category folders, classify INBOX by rules, move all (default: moves; use --dry-run to preview)",
    )
    p_tr.add_argument(
        "--rules",
        type=Path,
        default=_DEFAULT_TRIAGE_RULES,
        help=f"JSON rules (default: {_DEFAULT_TRIAGE_RULES})",
    )
    p_tr.add_argument(
        "--mailbox",
        default="INBOX",
        help="Mailbox to empty (default INBOX)",
    )
    p_tr.add_argument(
        "--dry-run",
        action="store_true",
        help="Only print the plan; do not move messages",
    )
    p_tr.add_argument(
        "--apply",
        action="store_true",
        help=argparse.SUPPRESS,
    )
    p_tr.add_argument("--json", action="store_true", help="JSON plan output")
    p_tr.set_defaults(func=cmd_triage)

    ns = parser.parse_args()
    load_env_file(ns.env_file)
    return int(ns.func(ns))


if __name__ == "__main__":
    raise SystemExit(main())
