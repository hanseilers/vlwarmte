#!/usr/bin/env bash
# Static preview: always serves the repo root (avoids “directory listing” from wrong CWD).
set -euo pipefail
cd "$(dirname "$0")/.."
PORT="${PORT:-8890}"
echo "VLWarmte: http://127.0.0.1:${PORT}/  (cwd: $(pwd))"
exec python3 -m http.server "$PORT" --bind 127.0.0.1
