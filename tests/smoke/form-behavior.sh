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

contains contact.html 'data-lead-mode="info"'
contains contact.html 'data-lead-mode="offerte"'
contains contact.html 'name="m2"'
contains contact.html 'name="vloerdiepte"'
contains contact.html 'data-only="offerte"'
contains assets/js/main.js "function validateLeadForm"
contains assets/js/main.js "requiredFields.push(\"m2\", \"vloerdiepte\", \"ondergrond\", \"projecttype\")"

echo "form-behavior.sh: PASS"
