#!/usr/bin/env python3
"""Block changes to protected paths (directories or files)."""
from __future__ import annotations

import argparse
import sys
from typing import Sequence

# Default protected paths (hardcoded)
DEFAULT_PROTECTED_PATHS = [
    '.github',
    '.devcontainer',
]


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description='Block changes to protected paths'
    )
    parser.add_argument('filenames', nargs='*', help='Files being committed')
    parser.add_argument(
        '--path',
        action='append',
        dest='protected_paths',
        default=[],
        help='Additional path to protect (can be specified multiple times)',
    )
    parser.add_argument(
        '--no-defaults',
        action='store_true',
        help='Disable default protected paths',
    )
    args = parser.parse_args(argv)

    # Combine default and custom paths
    if args.no_defaults:
        protected_paths = args.protected_paths
    else:
        protected_paths = DEFAULT_PROTECTED_PATHS + args.protected_paths

    if not protected_paths:
        print('Warning: No protected paths specified')
        return 0

    blocked_files = []
    for filename in args.filenames:
        for protected_path in protected_paths:
            # Check if file is within a protected path
            if filename.startswith(protected_path.rstrip('/') + '/') or filename == protected_path:
                blocked_files.append((filename, protected_path))
                break

    if blocked_files:
        print('❌ Commit blocked: changes to protected paths detected')
        print()
        for filename, protected_path in blocked_files:
            print(f'  - {filename} (protected: {protected_path})')
        print()
        print('These paths are protected and cannot be modified.')
        print('Contact an administrator if changes are necessary.')
        return 1

    return 0


if __name__ == '__main__':
    sys.exit(main())
