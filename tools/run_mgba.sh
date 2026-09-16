#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
if [ -f "$ROOT/.local/env.sh" ]; then
    # shellcheck disable=SC1091
    source "$ROOT/.local/env.sh"
fi

if ! command -v mgba >/dev/null 2>&1; then
    echo "mGBA is not installed for this checkout. Run: tools/setup_gba_environment.sh install" >&2
    exit 1
fi

if [ "$#" -eq 0 ]; then
    exec mgba
fi

exec mgba "$@"
