#!/usr/bin/env bash
# Wrapper script pour gitleaks qui utilise le fichier de config du repo
set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
CONFIG_FILE="${SCRIPT_DIR}/.gitleaks.toml"

if [[ -f "$CONFIG_FILE" ]]; then
    exec gitleaks protect --verbose --redact --staged --config "$CONFIG_FILE" "$@"
else
    exec gitleaks protect --verbose --redact --staged "$@"
fi
