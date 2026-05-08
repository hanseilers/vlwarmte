#!/usr/bin/env python3
"""
Stuur de bovenste release uit docs/website-manager/release-notes.md als HTML-mail
met hetzelfde outer template als klantmail (email_vlwarmte_customer_template.html).

Vereist: secrets/hostnet-mail.env (zelfde als hostnet_imap_read) met o.a. IMAP_USER
of MAIL_FROM voor de From-header, en SMTP_* of defaults.

  python3 scripts/send_pm_release_notes_email.py
  python3 scripts/send_pm_release_notes_email.py --dry-run
  python3 scripts/send_pm_release_notes_email.py --to ander@voorbeeld.nl
"""

from __future__ import annotations

import argparse
import html
import importlib.util
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
RELEASE_PATH = REPO / "docs" / "website-manager" / "release-notes.md"
ENV_PATH = REPO / "secrets" / "hostnet-mail.env"
DEFAULT_TO = "jceilers@icloud.com"
INTERNAL_DISCLAIMER = (
    "Interne notificatie na een website-releasecyclus (geen klantmail). "
    "Antwoord mag naar info@vlwarmte.nl."
)


def _load_hostnet():
    path = REPO / "scripts" / "hostnet_imap_read.py"
    spec = importlib.util.spec_from_file_location("hostnet_imap_read", path)
    if spec is None or spec.loader is None:
        raise RuntimeError("Cannot load hostnet_imap_read")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def extract_top_release_block(text: str) -> tuple[str, str]:
    """
    Returns (title_line_without_hashes, markdown_body_of_first_release_section).
    """
    lines = text.splitlines()
    start = None
    for i, line in enumerate(lines):
        if line.startswith("## Release"):
            start = i
            break
    if start is None:
        raise SystemExit(f"No '## Release' section found in {RELEASE_PATH}")

    title_raw = lines[start].strip()
    title_plain = title_raw.replace("## Release —", "").replace("## Release -", "").strip()
    if not title_plain:
        title_plain = title_raw.removeprefix("##").strip()

    end = len(lines)
    for j in range(start + 1, len(lines)):
        if lines[j].strip() != "---":
            continue
        k = j + 1
        while k < len(lines) and not lines[k].strip():
            k += 1
        if k < len(lines) and lines[k].lstrip().startswith("##"):
            end = j
            break

    body = "\n".join(lines[start:end]).strip()
    return title_plain, body


def _inline_md(s: str) -> str:
    """Very small subset: **bold** only; rest escaped."""
    out: list[str] = []
    pos = 0
    for m in re.finditer(r"\*\*(.+?)\*\*", s):
        out.append(html.escape(s[pos : m.start()]))
        out.append("<strong>" + html.escape(m.group(1)) + "</strong>")
        pos = m.end()
    out.append(html.escape(s[pos:]))
    return "".join(out)


def markdown_release_to_inner_html(md: str) -> str:
    """Convert first-release markdown chunk to simple HTML (headings, lists, paragraphs)."""
    lines = md.splitlines()
    parts: list[str] = []
    in_ul = False
    first = True
    for raw in lines:
        line = raw.rstrip()
        if first:
            first = False
            if line.startswith("## Release"):
                t = line.removeprefix("## Release").strip()
                if t.startswith("—"):
                    t = t.lstrip("—").strip()
                elif t.startswith("-"):
                    t = t.lstrip("-").strip()
                parts.append(
                    f'<h2 style="margin:0 0 14px;font-size:1.2rem;color:#0f1724;">'
                    f"Release — { _inline_md(t) }</h2>"
                )
                continue
        if not line.strip():
            if in_ul:
                parts.append("</ul>")
                in_ul = False
            continue
        if line.startswith("### "):
            if in_ul:
                parts.append("</ul>")
                in_ul = False
            parts.append(
                f'<h3 style="margin:1.1em 0 0.45em;font-size:1.05rem;color:#0f4c81;">'
                f"{_inline_md(line[4:].strip())}</h3>"
            )
            continue
        if line.startswith("- "):
            if not in_ul:
                parts.append('<ul style="margin:0.35em 0 1em;padding-left:1.15em;">')
                in_ul = True
            parts.append(f'<li style="margin:0.25em 0;">{_inline_md(line[2:].strip())}</li>')
            continue
        if in_ul:
            parts.append("</ul>")
            in_ul = False
        parts.append(f'<p style="margin:0.45em 0;line-height:1.55;">{_inline_md(line.strip())}</p>')
    if in_ul:
        parts.append("</ul>")
    intro = (
        '<p style="margin:0 0 16px 0;">Hieronder de <strong>nieuwste</strong> release uit '
        "<code>release-notes.md</code> (bovenaan het bestand).</p>"
    )
    return intro + "\n".join(parts)


def main() -> int:
    p = argparse.ArgumentParser(description="E-mail top release notes via klant-template.")
    p.add_argument("--to", default=DEFAULT_TO, help=f"Ontvanger (default: {DEFAULT_TO})")
    p.add_argument(
        "--release-notes",
        type=Path,
        default=RELEASE_PATH,
        help="Pad naar release-notes.md",
    )
    p.add_argument("--dry-run", action="store_true", help="Print HTML, verzend niet")
    p.add_argument("--env-file", type=Path, default=ENV_PATH, help="hostnet-mail.env")
    args = p.parse_args()

    mod = _load_hostnet()
    mod.load_env_file(args.env_file)

    text = args.release_notes.read_text(encoding="utf-8")
    title_plain, md_block = extract_top_release_block(text)
    inner = markdown_release_to_inner_html(md_block)

    subject = f"VLWarmte release — {title_plain}"
    preheader = f"Release: {title_plain}"[:140]

    full_html = mod.render_customer_email_html(
        body_html=inner,
        title=subject,
        preheader=preheader,
        footer_disclaimer=INTERNAL_DISCLAIMER,
    )
    plain = mod._html_to_plain_fallback(inner) or mod._html_to_plain_fallback(full_html)

    import os
    from email.message import EmailMessage

    mail_from = (os.environ.get("MAIL_FROM") or os.environ.get("IMAP_USER") or "").strip()
    if not mail_from:
        raise SystemExit("Set MAIL_FROM or IMAP_USER in secrets/hostnet-mail.env")

    msg = EmailMessage()
    msg["From"] = mail_from
    msg["To"] = args.to.strip()
    msg["Subject"] = subject
    msg.set_content(plain, subtype="plain", charset="utf-8")
    msg.add_alternative(full_html, subtype="html", charset="utf-8")

    if args.dry_run:
        print("dry-run: would send to", args.to, file=sys.stderr)
        print(full_html[:12000])
        if len(full_html) > 12000:
            print("... [truncated]", file=sys.stderr)
        return 0

    mod.send_smtp(msg)
    print("OK sent PM release notes to", args.to)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
