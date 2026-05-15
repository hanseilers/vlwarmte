#!/usr/bin/env python3
"""
Vervang de placeholder in <meta name="google-site-verification" content="REPLACE_WITH_TOKEN" />
door het echte token uit omgeving of secrets/google-site-verification.env.

Zonder token: geen wijzigingen (exit 0). Geen secrets committen.
"""

from __future__ import annotations

import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PLACEHOLDER = "REPLACE_WITH_TOKEN"
META_NEEDLE = f'content="{PLACEHOLDER}"'


def _load_token() -> str:
    env_file = ROOT / "secrets" / "google-site-verification.env"
    if env_file.is_file():
        for raw in env_file.read_text(encoding="utf-8").splitlines():
            line = raw.strip()
            if not line or line.startswith("#"):
                continue
            if line.startswith("GOOGLE_SITE_VERIFICATION="):
                return line.split("=", 1)[1].strip().strip('"').strip("'")
    return os.environ.get("GOOGLE_SITE_VERIFICATION", "").strip()


def main() -> int:
    token = _load_token()
    if not token or token in ("paste_token_here", PLACEHOLDER):
        print(
            "inject_site_verification: geen token — sla over. "
            "Zet GOOGLE_SITE_VERIFICATION in secrets/google-site-verification.env "
            "of exporteer de variabele, en run opnieuw.",
            file=sys.stderr,
        )
        return 0

    updated = 0
    for path in sorted(ROOT.glob("*.html")):
        text = path.read_text(encoding="utf-8")
        if META_NEEDLE not in text:
            continue
        new = text.replace(META_NEEDLE, f'content="{token}"')
        if new != text:
            path.write_text(new, encoding="utf-8")
            updated += 1
    print(f"inject_site_verification: {updated} HTML-bestand(en) bijgewerkt.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
