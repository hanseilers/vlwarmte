#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
cd "$ROOT"

test -f contact.html
test -f assets/js/main.js

contains() {
  local file="$1"
  local needle="$2"
  python3 -c "import pathlib,sys; t=pathlib.Path(sys.argv[1]).read_text(); sys.exit(0 if sys.argv[2] in t else 1)" "$file" "$needle"
}

lacks() {
  local file="$1"
  local needle="$2"
  python3 -c "import pathlib,sys; t=pathlib.Path(sys.argv[1]).read_text(); sys.exit(1 if sys.argv[2] in t else 0)" "$file" "$needle"
}

# Kort contactformulier: naam, telefoon of e-mail, vraag en een optionele foto.
contains contact.html 'id="lead-form"'
contains contact.html 'action="https://formspree.io/f/xgodnvoq"'
contains contact.html 'id="aanvraag"'
contains contact.html 'name="soort_aanvraag"'
contains contact.html 'name="name"'
contains contact.html 'name="contact"'
contains contact.html 'name="message"'
# Foto's gaan niet via Formspree maar via WhatsApp.
lacks contact.html 'type="file"'
lacks contact.html 'name="foto"'
contains contact.html 'id="lead-status"'

# De lange offertevelden en de drie tabbladen zijn vervallen.
lacks contact.html 'name="m2"'
lacks contact.html 'name="vloerdiepte"'
lacks contact.html 'data-lead-mode='
lacks contact.html 'data-only='

# Deeplinks ?modus=info|offerte|bel vallen terug op hetzelfde formulier.
contains assets/js/main.js "readLeadModeFromUrl"
contains assets/js/main.js "function applyLeadMode"
contains assets/js/main.js "function validateLeadForm"
contains assets/js/main.js 'for (const fieldName of ["name", "contact", "message"])'
contains assets/js/main.js 'soort: "Offerte"'
contains assets/js/main.js 'soort: "Terugbelverzoek"'
contains assets/js/main.js '"contact_submit"'

# Terugbelformulier in het contactblok (elke pagina behalve contact).
contains index.html 'js-callback-form'
contains index.html 'name="terugbel_moment"'
contains assets/js/main.js "function initCallbackForms"

# WhatsApp als primair contact: headerknop, zwevende knop en groot blok.
contains index.html 'class="btn btn-wa btn-sm"'
contains index.html 'class="wa-float"'
contains index.html 'class="wa-hero"'
contains contact.html 'https://wa.me/message/SOVOXF6IXF3FM1'

echo "form-behavior.sh: PASS"
