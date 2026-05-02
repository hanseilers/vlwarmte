#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
cd "$ROOT"

pages=(
  "index.html"
  "diensten.html"
  "systemen-producten.html"
  "werkwijze.html"
  "over-ons.html"
  "faq.html"
  "projecten.html"
  "contact.html"
  "disclaimer.html"
  "privacy.html"
  "vloerverwarming-groningen.html"
  "vloerverwarming-assen.html"
  "vloerverwarming-zuidlaren.html"
)

for page in "${pages[@]}"; do
  test -f "$page"
done

test -f robots.txt
test -f sitemap.xml

contains() {
  local file="$1"
  local needle="$2"
  python3 -c "import pathlib,sys; t=pathlib.Path(sys.argv[1]).read_text(); sys.exit(0 if sys.argv[2] in t else 1)" "$file" "$needle"
}

contains index.html "<title>"
contains index.html "href=\"diensten.html\""
contains index.html "href=\"contact.html\""
contains diensten.html "<h1"
contains systemen-producten.html "<h1"
contains werkwijze.html "<h1"
contains over-ons.html "<h1"
contains projecten.html "<h1"
contains contact.html "<h1"
contains index.html "href=\"privacy.html\""
contains index.html "href=\"disclaimer.html\""
contains index.html "rel=\"canonical\""
contains index.html "application/ld+json"
contains sitemap.xml "https://www.vlwarmte.nl/"
contains sitemap.xml "vloerverwarming-zuidlaren.html"
contains sitemap.xml "faq.html"
contains faq.html "application/ld+json"

echo "navigation-links.sh: PASS"
