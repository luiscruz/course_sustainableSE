#!/usr/bin/env bash
# run_forecast.sh
# ---------------
# Finds the best hour to run a GitHub Action in terms of CO₂ emissions
# by calling find_best_hour.py.
#
# Usage:
#   ./run_forecast.sh              # auto-detect Python / venv
#   ./run_forecast.sh --install    # also pip-install missing dependencies first

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PYTHON_SCRIPT="$SCRIPT_DIR/find_best_hour.py"
VENV_DIR="$SCRIPT_DIR/.venv"
INSTALL_DEPS=false

# ---------------------------------------------------------------------------
# Parse arguments
# ---------------------------------------------------------------------------
for arg in "$@"; do
  case "$arg" in
    --install) INSTALL_DEPS=true ;;
    *) echo "Unknown argument: $arg" >&2; exit 1 ;;
  esac
done

# ---------------------------------------------------------------------------
# Resolve Python interpreter
# Precedence: active venv → local .venv → system python3
# ---------------------------------------------------------------------------
if [[ -n "${VIRTUAL_ENV:-}" ]]; then
  PYTHON="$VIRTUAL_ENV/bin/python"
  echo "[run_forecast] Using active virtual environment: $VIRTUAL_ENV"
elif [[ -x "$VENV_DIR/bin/python" ]]; then
  PYTHON="$VENV_DIR/bin/python"
  echo "[run_forecast] Using local .venv: $VENV_DIR"
else
  PYTHON="$(command -v python3 || command -v python)"
  echo "[run_forecast] Using system Python: $PYTHON"
fi

# ---------------------------------------------------------------------------
# Optionally install / upgrade required packages
# ---------------------------------------------------------------------------
REQUIRED_PACKAGES=(requests python-dotenv)

if [[ "$INSTALL_DEPS" == true ]]; then
  echo "[run_forecast] Installing/upgrading dependencies …"
  "$PYTHON" -m pip install --quiet --upgrade "${REQUIRED_PACKAGES[@]}"
  echo "[run_forecast] Dependencies ready."
else
  # Check that required packages are importable; suggest --install if missing
  MISSING=()
  for pkg in requests dotenv; do
    if ! "$PYTHON" -c "import $pkg" 2>/dev/null; then
      MISSING+=("$pkg")
    fi
  done
  if [[ ${#MISSING[@]} -gt 0 ]]; then
    echo "ERROR: Missing Python package(s): ${MISSING[*]}" >&2
    echo "       Run:  $0 --install   to install them automatically." >&2
    exit 1
  fi
fi

# ---------------------------------------------------------------------------
# Run the forecast script
# ---------------------------------------------------------------------------
echo ""
echo "========================================"
echo "  Carbon-Aware GitHub Action Scheduler"
echo "========================================"
echo ""

"$PYTHON" "$PYTHON_SCRIPT"

EXIT_CODE=$?

if [[ $EXIT_CODE -eq 0 ]]; then
  echo ""
  echo "[run_forecast] Done. Check .env for GHA_BEST_HOUR and GHA_BEST_CRON."
else
  echo "[run_forecast] Script exited with code $EXIT_CODE." >&2
  exit $EXIT_CODE
fi
