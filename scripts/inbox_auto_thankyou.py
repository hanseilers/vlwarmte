#!/usr/bin/env python3
"""Process unread Formspree-style lead mail: send conversational thank-you, mark read.

Loads secrets/hostnet-mail.env (or env vars). Reuses send + HTML template from
hostnet_imap_read.py via importlib.

Skips messages whose body contains VLW-E2E- (deploy test). Does not use external LLM APIs.

Usage:
  python scripts/inbox_auto_thankyou.py --dry-run --max 5
  python scripts/inbox_auto_thankyou.py --max 3
"""

from __future__ import annotations

import argparse
import email.policy
import importlib.util
import os
import re
import sys
from email import message_from_bytes
from email.header import decode_header, make_header
from email.message import EmailMessage, Message
from email.utils import getaddresses, parseaddr
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
_DEFAULT_ENV = REPO_ROOT / "secrets" / "hostnet-mail.env"


def _load_hostnet():
    path = REPO_ROOT / "scripts" / "hostnet_imap_read.py"
    spec = importlib.util.spec_from_file_location("hostnet_imap_read", path)
    if not spec or not spec.loader:
        raise RuntimeError("Cannot load hostnet_imap_read")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def _decode(raw: str | None) -> str:
    if not raw:
        return ""
    try:
        return str(make_header(decode_header(raw)))
    except Exception:
        return raw or ""


def _htmlish_to_plain(html: str) -> str:
    t = re.sub(r"(?is)<(script|style)\b[^>]*>.*?</\1>", " ", html)
    t = re.sub(r"(?is)<br\s*/?>", "\n", t)
    t = re.sub(r"(?is)</p\s*>", "\n\n", t)
    t = re.sub(r"(?is)<[^>]+>", " ", t)
    t = re.sub(r"[ \t\r\f]+", " ", t)
    t = re.sub(r"\n{3,}", "\n\n", t)
    return t.strip()


def _extract_text_body(msg: Message) -> str:
    if msg.is_multipart():
        plain = ""
        html = ""
        for part in msg.walk():
            ctype = part.get_content_type()
            if ctype == "text/plain" and not plain:
                try:
                    plain = part.get_content()
                except Exception:
                    raw = part.get_payload(decode=True)
                    if isinstance(raw, bytes):
                        plain = raw.decode(errors="replace")
            elif ctype == "text/html" and not html:
                try:
                    html = part.get_content()
                except Exception:
                    raw = part.get_payload(decode=True)
                    if isinstance(raw, bytes):
                        html = raw.decode(errors="replace")
        if plain:
            return plain
        if html:
            return _htmlish_to_plain(html)
        return ""
    try:
        return str(msg.get_content())
    except Exception:
        raw = msg.get_payload(decode=True)
        if isinstance(raw, bytes):
            return raw.decode(errors="replace")
        return str(raw or "")


def _norm_key(key: str) -> str:
    return re.sub(r"[^a-z0-9]+", "_", key.strip().lower()).strip("_")


def _parse_loose_fields(text: str) -> dict[str, str]:
    """Best-effort key: value lines (Formspree / forwarded forms)."""
    out: dict[str, str] = {}
    for line in text.splitlines():
        line = line.strip()
        if ":" not in line or len(line) > 400:
            continue
        key, _, val = line.partition(":")
        k = _norm_key(key)
        v = val.strip()
        if not k or not v:
            continue
        if k in ("naam", "name"):
            out["name"] = v
        elif k in ("e_mail", "email", "e_mailadres"):
            out["email"] = v
        elif k in ("telefoon", "phone", "tel"):
            out["phone"] = v
        elif k in ("soort_aanvraag", "soort", "type"):
            out["soort_aanvraag"] = v
        elif k in ("m2", "oppervlakte"):
            out["m2"] = v
        elif k in ("vloerdiepte", "diepte_kruipruimte"):
            out["vloerdiepte"] = v
        elif k == "ondergrond":
            out["ondergrond"] = v
        elif k == "projecttype":
            out["projecttype"] = v
        elif k in ("plaats", "region", "regio", "plaats_regio"):
            out["region"] = v
        elif k in ("opmerkingen", "message", "bericht"):
            out["message"] = v
    return out


def _reply_to_address(msg: Message, body_text: str) -> str | None:
    """Prefer Reply-To, then From (customer), not our own mailbox."""
    ours = (os.environ.get("IMAP_USER") or "").lower()
    for header in ("Reply-To", "From"):
        raw = msg.get(header)
        if not raw:
            continue
        pairs = getaddresses([raw])
        for _name, addr in pairs:
            a = (addr or "").strip()
            if a and "@" in a and not a.lower().endswith("@formspree.io"):
                if ours and a.lower() == ours:
                    continue
                return a
    fields = _parse_loose_fields(body_text)
    em = fields.get("email", "").strip()
    if em and "@" in em and (not ours or em.lower() != ours):
        return em
    _n, addr = parseaddr(_decode(msg.get("From")))
    if addr and "@" in addr and not addr.lower().endswith("@formspree.io"):
        if not ours or addr.lower() != ours:
            return addr
    return None


def _looks_like_submission(msg: Message, body: str) -> bool:
    subj = _decode(msg.get("Subject")).lower()
    blob = (body + "\n" + subj).lower()
    if "vlw-e2e-" in blob:
        return False
    if "new submission" in subj or "formspree" in blob or "soort_aanvraag" in blob:
        return True
    if "offerte" in subj and ("@" in body or "telefoon" in blob or "phone" in blob):
        return True
    return False


def _build_conversational_body(fields: dict[str, str], body_text: str) -> str:
    name = (fields.get("name") or "").strip() or "daar"
    first = name.split()[0]
    soort = (fields.get("soort_aanvraag") or "").strip() or "Offerte"
    m2 = (fields.get("m2") or "").strip()
    diepte = (fields.get("vloerdiepte") or "").strip()
    onder = (fields.get("ondergrond") or "").strip().lower()
    proj = (fields.get("projecttype") or "").strip().lower()
    regio = (fields.get("region") or "").strip()

    parts: list[str] = []
    parts.append(
        f'<p style="margin:0 0 16px 0;font-size:16px;line-height:1.55;color:#1a2332;">Beste {first},</p>'
    )
    if "offerte" in soort.lower():
        parts.append(
            '<p style="margin:0 0 16px 0;font-size:16px;line-height:1.55;color:#1a2332;">'
            "Hartelijk dank voor uw bericht en uw offerteaanvraag. We hebben uw aanvraag goed ontvangen "
            "en lezen met aandacht wat u ons stuurt."
            "</p>"
        )
        mid: list[str] = []
        if m2:
            mid.append(f"u schat de vloer rond de <strong>{m2} m²</strong>")
        if diepte:
            if mid:
                mid.append(f"en noemt een kruipruimte van <strong>{diepte} mm</strong>")
            else:
                mid.append(f"u noemt een kruipruimte van <strong>{diepte} mm</strong>")
        if onder:
            if mid:
                mid.append(f"met <strong>{onder}</strong> als ondergrond")
            else:
                mid.append(f"u werkt met <strong>{onder}</strong> als ondergrond")
        if proj:
            mid.append(f"het gaat om <strong>{proj}</strong>")
        if regio:
            mid.append(f"rond <strong>{regio}</strong>")
        if mid:
            parts.append(
                "<p style=\"margin:0 0 16px 0;font-size:16px;line-height:1.55;color:#1a2332;\">"
                "Even in eigen woorden terug: " + ", ".join(mid) + "."
                "</p>"
            )
    else:
        parts.append(
            '<p style="margin:0 0 16px 0;font-size:16px;line-height:1.55;color:#1a2332;">'
            "Hartelijk dank voor uw bericht. We hebben uw aanvraag goed ontvangen."
            "</p>"
        )

    msg_hint = (fields.get("message") or "").strip()
    if len(msg_hint) > 400:
        msg_hint = msg_hint[:400].rsplit(" ", 1)[0] + "…"
    if msg_hint and "deploy-test" not in msg_hint.lower():
        safe = msg_hint.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
        safe = safe.replace("\n", "<br />")
        parts.append(
            "<p style=\"margin:0 0 16px 0;font-size:16px;line-height:1.55;color:#1a2332;\">"
            "U schreef onder meer het volgende — dat nemen we mee in ons antwoord:<br />"
            f'<span style="color:#3d4a5c;">{safe}</span></p>'
        )

    parts.append(
        '<p style="margin:0 0 16px 0;font-size:16px;line-height:1.55;color:#1a2332;">'
        "We proberen u <strong>zo spoedig mogelijk</strong> persoonlijk terug te mailen. "
        "Heeft u tussendoor nog iets toe te voegen, dan kunt u gerust op deze thread antwoorden."
        "</p>"
    )
    parts.append(
        '<p style="margin:0;font-size:16px;line-height:1.55;color:#1a2332;">Met vriendelijke groet,<br />'
        '<strong style="color:#0f1724;">Team VLWarmte</strong></p>'
    )
    return "".join(parts)


def _uid_search_unseen(conn) -> list[int]:
    typ, data = conn.uid("SEARCH", None, "UNSEEN")
    if typ != "OK" or not data or not data[0]:
        return []
    raw = data[0].decode("ascii", errors="ignore").strip()
    if not raw:
        return []
    uids = [int(x) for x in raw.split() if x.isdigit()]
    uids.sort()
    return uids


def _fetch_full(conn, uid: int) -> Message:
    typ, data = conn.uid("FETCH", str(uid), "(RFC822)")
    if typ != "OK" or not data:
        raise RuntimeError(f"FETCH RFC822 failed uid {uid}")
    for item in data:
        if isinstance(item, tuple) and len(item) >= 2 and isinstance(item[1], (bytes, bytearray)):
            return message_from_bytes(bytes(item[1]), policy=email.policy.default)
    raise RuntimeError("empty FETCH")


def _mark_seen(conn, uid: int) -> None:
    typ, _ = conn.uid("STORE", str(uid), "+FLAGS", r"(\Seen)")
    if typ != "OK":
        raise RuntimeError(f"STORE Seen failed uid {uid}")


def main() -> int:
    ap = argparse.ArgumentParser(description="Auto thank-you for unread Formspree-style leads")
    ap.add_argument("--env-file", type=Path, default=_DEFAULT_ENV)
    ap.add_argument("--max", type=int, default=5, help="Max messages to process this run")
    ap.add_argument(
        "--mailboxes",
        default="INBOX,INBOX/Leads,INBOX/Overig",
        help="Comma-separated IMAP folders to scan",
    )
    ap.add_argument("--dry-run", action="store_true")
    ns = ap.parse_args()

    him = _load_hostnet()
    him.load_env_file(ns.env_file)

    subj_out = "Bedankt voor uw bericht — VLWarmte"
    pre = "We hebben uw aanvraag ontvangen en reageren zo snel mogelijk."

    import imaplib

    conn = him.connect_imap()
    processed = 0
    mailboxes = [x.strip() for x in ns.mailboxes.split(",") if x.strip()]
    hits: list[tuple[str, int, Message, dict[str, str], str]] = []
    try:
        for mbox in mailboxes:
            typ, _ = conn.select(mbox, readonly=True)
            if typ != "OK":
                continue
            for uid in _uid_search_unseen(conn):
                msg = _fetch_full(conn, uid)
                body = _extract_text_body(msg)
                if not _looks_like_submission(msg, body):
                    continue
                fields = _parse_loose_fields(body)
                to_addr = _reply_to_address(msg, body)
                if not to_addr:
                    print(f"skip uid {uid} ({mbox}): no customer reply address", file=sys.stderr)
                    continue
                hits.append((mbox, uid, msg, fields, to_addr))

        mail_from = (os.environ.get("MAIL_FROM") or os.environ.get("IMAP_USER") or "").strip()
        if not mail_from:
            raise SystemExit("MAIL_FROM or IMAP_USER required")

        for mbox, uid, msg, fields, to_addr in hits[: ns.max]:
            inner = _build_conversational_body(fields, _extract_text_body(msg))
            full_html = him.render_customer_email_html(
                body_html=inner,
                title=subj_out,
                preheader=pre,
            )
            plain = him._html_to_plain_fallback(inner) or him._html_to_plain_fallback(full_html)

            out = EmailMessage()
            out["From"] = mail_from
            out["To"] = to_addr
            out["Subject"] = subj_out
            mid = msg.get("Message-ID")
            if mid:
                out["In-Reply-To"] = mid
                out["References"] = mid
            out.set_content(plain, subtype="plain", charset="utf-8")
            out.add_alternative(full_html, subtype="html", charset="utf-8")

            if ns.dry_run:
                print(f"dry-run: would thank {to_addr} for uid {uid} in {mbox}", file=sys.stderr)
            else:
                typ2, _ = conn.select(mbox, readonly=False)
                if typ2 != "OK":
                    print(f"skip send: cannot reopen {mbox}", file=sys.stderr)
                    continue
                him.send_smtp(out)
                _mark_seen(conn, uid)
                print(f"OK thanked {to_addr} (uid {uid} {mbox})", file=sys.stderr)
            processed += 1
    finally:
        try:
            conn.close()
        except Exception:
            pass
        try:
            conn.logout()
        except imaplib.IMAP4.error:
            pass

    if processed == 0:
        print("No matching unread messages.", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
