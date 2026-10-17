#!/usr/bin/env bash
set -euo pipefail

task_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
task_project="$task_root/chapters/w02"
case "${1:-slides}" in
  slides) task_mode=run; task_file=week02_slides.py ;;
  lab) task_mode=edit; task_file=practice/regression_lab.py ;;
  *) echo "사용법: bash scripts/week02.sh [slides|lab] [marimo 옵션]" >&2; exit 2 ;;
esac
if (( $# )); then shift; fi

if command -v uv >/dev/null 2>&1; then
  task_uv="$(command -v uv)"
else
  task_uv="$task_root/.tools/uv/uv"
  if [[ ! -x "$task_uv" ]]; then
    task_installer="$(mktemp)"
    trap 'rm -f "$task_installer"' EXIT
    curl --fail --silent --show-error --location https://astral.sh/uv/0.11.3/install.sh --output "$task_installer"
    UV_UNMANAGED_INSTALL="$task_root/.tools/uv" sh "$task_installer"
    rm -f "$task_installer"
    trap - EXIT
  fi
fi

export UV_CACHE_DIR="${UV_CACHE_DIR:-$task_project/.cache/uv}"
export UV_PYTHON_INSTALL_DIR="${UV_PYTHON_INSTALL_DIR:-$task_project/.cache/python}"
export XDG_STATE_HOME="${XDG_STATE_HOME:-$task_project/.cache/state}"
export MPLCONFIGDIR="${MPLCONFIGDIR:-$task_project/.cache/matplotlib}"
cd "$task_project"
exec "$task_uv" run --frozen --project "$task_project" marimo "$task_mode" "$task_project/$task_file" "$@"
