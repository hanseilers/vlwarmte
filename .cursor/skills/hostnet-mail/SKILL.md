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

## E2E na deploy (Formspree → `info@`)

**Script:** `scripts/e2e_formspree_inbox.py`  
POST een **offerte** naar het **productie**-Formspree-endpoint (zelfde als `contact.html`), zoekt een unieke marker in **INBOX / INBOX/Leads / INBOX/Overig / INBOX/Systeem**, verwijdert de testmail na succes.

```bash
python scripts/e2e_formspree_inbox.py
```

Env: zelfde **`IMAP_*`** als `secrets/hostnet-mail.env`. Optioneel: `E2E_FORMSPREE_URL`, `E2E_BASE_URL`, `E2E_INBOX_TIMEOUT_SEC` (default 240), `E2E_POLL_INTERVAL_SEC` (8), `E2E_SKIP=1` om over te slaan.

**GitHub Actions:** `.github/workflows/e2e-production-formspree.yml` — draait op **`push` naar `main`** (met 120 s wachttijd voor Pages) en **`workflow_dispatch`**. Zet repository secrets **`IMAP_USER`** + **`IMAP_PASSWORD`** (optioneel `IMAP_HOST`, `IMAP_PORT`, `E2E_FORMSPREE_URL`). Zonder wachtwoord: job slaat over met een **notice** (handig voor forks).

Let op: Formspree kan soms **throttlen** of verdachte IP’s beperken; bij falen eerst **handmatig** het script lokaal proberen en Formspree-dashboard checken.

---

## Inbox “agent”: bedankmail (geen LLM)

**Script:** `scripts/inbox_auto_thankyou.py` — zoekt **ongelezen** mail in `INBOX`, `INBOX/Leads`, `INBOX/Overig` die op een **Formspree-/offerte-aanvraag** lijkt, bouwt een **lopende NL-bedanktekst** (geen bulletlist met velden), stuurt die met het **zelfde HTML-sjabloon** als `send-customer`, zet **`In-Reply-To`** op de originele mail en markeert daarna **gelezen**.

- Slaat berichten over met **`VLW-E2E-`** in de inhoud (deploy-test).
- Start altijd met **`--dry-run`**.

```bash
python scripts/inbox_auto_thankyou.py --dry-run --max 3
python scripts/inbox_auto_thankyou.py --max 3
```

**GitHub Actions:** `.github/workflows/inbox-auto-thankyou.yml` — alleen **`workflow_dispatch`** (geen cron), secrets zoals E2E + optioneel **`MAIL_FROM`** (anders `IMAP_USER`). Pas heuristiek in het script aan voordat je dit op een schema zet.

---

## Read vs write

- **`recent` / `headers`:** readonly `SELECT` + `BODY.PEEK[HEADER]`.
- **`triage` (default) / `move` / `send`:** mutating.

## When to use triage

- Clear **INBOX** into review buckets after busy periods.
- Tune **`hostnet_mail_triage.json`** when real leads land in the wrong folder.
