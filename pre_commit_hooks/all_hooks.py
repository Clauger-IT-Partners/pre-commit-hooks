#!/usr/bin/env python3
"""Run all Clauger pre-commit hooks."""
from __future__ import annotations

import shutil
import subprocess
import sys
from pathlib import Path
from typing import Sequence

from pre_commit_hooks.detect_private_key import main as detect_private_key
from pre_commit_hooks.protect_paths import main as protect_paths


def run_gitleaks() -> int:
    """Run gitleaks if available."""
    if not shutil.which('gitleaks'):
        print('⚠️  gitleaks not found, skipping secrets detection')
        return 0

    # Find config file in the hooks package directory
    hooks_dir = Path(__file__).parent.parent
    config_file = hooks_dir / '.gitleaks.toml'

    cmd = ['gitleaks', 'protect', '--verbose', '--redact', '--staged']
    if config_file.exists():
        cmd.extend(['--config', str(config_file)])

    result = subprocess.run(cmd)
    return result.returncode


def main(argv: Sequence[str] | None = None) -> int:
    if argv is None:
        argv = sys.argv[1:]

    retval = 0

    # Run detect-private-key
    retval |= detect_private_key(list(argv))

    # Run protect-paths
    retval |= protect_paths(list(argv))

    # Run gitleaks
    retval |= run_gitleaks()

    return retval


if __name__ == '__main__':
    sys.exit(main())
