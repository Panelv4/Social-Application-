#!/usr/bin/env bash
# Self-healing launcher: ensures Flask is installed, then serves the site.
set -e
cd "$(dirname "$0")"
python3 -c "import flask" 2>/dev/null || pip install --break-system-packages -q -r Requirements.txt
exec python3 App.py
