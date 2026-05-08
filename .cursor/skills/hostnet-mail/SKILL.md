---
name: hostnet-mail
description: >-
  Hostnet mailbox info@vlwarmte.nl: IMAP read/send/move/copy, rule-based triage into
  category folders (empty INBOX by default), plus SMTP. Uses secrets/hostnet-mail.env.
---

# Hostnet mailbox (IMAP + SMTP + triage)

## Provider

- **IMAP:** `imap.hostnet.nl` **993** SSL/TLS.
- **SMTP:** `smtp.hostnet.nl` **587** STARTTLS (same login unless `SMTP_*` set).
- **Script:** `scripts/hostnet_imap_read.py` (stdlib only).

## Secrets

`secrets/hostnet-mail.env` from `secrets/hostnet-mail.env.example` (gitignored).

---

## Category folders (VLWarmte)

Rules live in **`scripts/data/hostnet_mail_triage.json`** (committed, editable). The script **creates** missing folders under `INBOX/…` before moving mail.

| Folder | Purpose |
|--------|---------|
| **INBOX/Leads** | Form pipelines (Formspree, etc.) + Dutch subject cues (offerte, aanvraag, …). |
| **INBOX/Systeem** | Platforms and transactional senders (Google, Meta, ESPs, …). |
| **INBOX/Promoties** | `List-Unsubscribe` or bulk `Precedence`. |
| **INBOX/Spam** | Junk domains / spammy subjects. |
| **INBOX/Overig** | Catch-all so **INBOX can end empty** — skim regularly. |

Rules run **top to bottom**; **first match wins**.

---

## Auto-triage (default: **moves** mail)

**Agents and humans:** run triage as part of inbox hygiene — **no extra flag** is required to apply moves.

```bash
python scripts/hostnet_imap_read.py triage
python scripts/hostnet_imap_read.py triage --json
```

**Preview only** (no moves):

```bash
python scripts/hostnet_imap_read.py triage --dry-run
```

Options: `--rules path.json`, `--mailbox INBOX` (default).

JSON output uses **`"applied": true`** when messages were moved, **`false`** with `--dry-run`.

---

## Other commands

```bash
python scripts/hostnet_imap_read.py ping
python scripts/hostnet_imap_read.py list-mailboxes
python scripts/hostnet_imap_read.py recent --limit 25 --json
python scripts/hostnet_imap_read.py send --to … --subject … --body "…"
python scripts/hostnet_imap_read.py move --uid 5 --to-folder "INBOX/Spam"
```

### Klant-e-mail (branding + footer)

**Template (outer shell):** `scripts/data/email_vlwarmte_customer_template.html`  
Placeholders: `{{VLW_EMAIL_BODY}}`, `{{VLW_EMAIL_TITLE}}`, `{{VLW_EMAIL_PREHEADER}}` (filled by the script).  
Logo in mail is **`assets/img/vlwarmte-email-logo.png`** (PNG — veel clients tonen **geen SVG** in e-mail). Publieke URL: **https://www.vlwarmte.nl/assets/img/vlwarmte-email-logo.png**. Zonder “Afbeeldingen laden” zie je alsnog de **oranje VLWarmte-tekst** onder het blok.

**Voorbeeldfragment (alleen inhoud):** `scripts/data/email_fragment_offertebevestiging.nl.html` — bevestiging offerteaanvraag; kopieer/aanpas voor vergelijkbare replies.

**Versturen:**

```bash
python scripts/hostnet_imap_read.py send-customer \
  --to klant@voorbeeld.nl \
  --subject "Onderwerp" \
  --preheader "Korte previewregel voor de inbox" \
  --body-html-file scripts/data/email_fragment_offertebevestiging.nl.html
```

Body mag ook inline: `--body-html '<p>…</p>'` of plat met alinea’s: `--body-text $'Alinea 1\n\nAlinea 2'`.  
Optioneel: `--template pad/naar/ander_template.html`, `--reply-to`, `--dry-run`.

---

## Read vs write

- **`recent` / `headers`:** readonly `SELECT` + `BODY.PEEK[HEADER]`.
- **`triage` (default) / `move` / `send`:** mutating.

## When to use triage

- Clear **INBOX** into review buckets after busy periods.
- Tune **`hostnet_mail_triage.json`** when real leads land in the wrong folder.
