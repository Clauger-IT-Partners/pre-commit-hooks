#!/usr/bin/env python3
"""Detect private keys in files.

Source: https://github.com/pre-commit/pre-commit-hooks
License: MIT
"""
from __future__ import annotations

import argparse
import re
import sys
from typing import Sequence

PRIVATE_KEY_PATTERNS = [
    re.compile(rb'-----BEGIN RSA PRIVATE KEY-----'),
    re.compile(rb'-----BEGIN DSA PRIVATE KEY-----'),
    re.compile(rb'-----BEGIN EC PRIVATE KEY-----'),
    re.compile(rb'-----BEGIN OPENSSH PRIVATE KEY-----'),
    re.compile(rb'-----BEGIN PRIVATE KEY-----'),
    re.compile(rb'-----BEGIN ENCRYPTED PRIVATE KEY-----'),
    re.compile(rb'-----BEGIN PGP PRIVATE KEY BLOCK-----'),
]


def detect_private_key(filename: str) -> int:
    retval = 0
    try:
        with open(filename, 'rb') as f:
            content = f.read()
            for pattern in PRIVATE_KEY_PATTERNS:
                if pattern.search(content):
                    print(f'{filename}: Private key detected')
                    retval = 1
                    break
    except OSError:
        print(f'{filename}: Unable to read file')
        retval = 1
    return retval


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description='Detect private keys')
    parser.add_argument('filenames', nargs='*', help='Files to check')
    args = parser.parse_args(argv)

    retval = 0
    for filename in args.filenames:
        retval |= detect_private_key(filename)
    return retval


if __name__ == '__main__':
    sys.exit(main())
