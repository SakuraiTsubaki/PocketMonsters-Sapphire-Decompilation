#!/usr/bin/env python3
"""Check the local GBA decompilation toolchain without touching ROM data."""
from __future__ import annotations

import os
from pathlib import Path
import shutil
import subprocess
import sys

REQUIRED = (
    "git", "make", "python3",
    "arm-none-eabi-as", "arm-none-eabi-objdump", "arm-none-eabi-ld",
)
OPTIONAL = ("arm-none-eabi-gcc", "arm-none-eabi-gdb", "gbafix", "grit", "mgba")


def first_line(command: str, *args: str) -> str:
    path = shutil.which(command)
    if not path:
        return "missing"
    try:
        proc = subprocess.run([path, *args], stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                              text=True, timeout=10, check=False)
        line = next((x.strip() for x in proc.stdout.splitlines() if x.strip()), "available")
        return line[:180]
    except Exception as exc:  # diagnostic only
        return f"available ({exc.__class__.__name__})"


def main() -> int:
    failures: list[str] = []
    print("GBA decompilation environment")
    print(f"DEVKITPRO={os.environ.get('DEVKITPRO', '<unset>')}")
    print(f"DEVKITARM={os.environ.get('DEVKITARM', '<unset>')}")
    print(f"AGBCC_ROOT={os.environ.get('AGBCC_ROOT', '<unset>')}")

    for command in REQUIRED:
        path = shutil.which(command)
        print(f"required {command:24} {path or 'MISSING'}")
        if not path:
            failures.append(command)

    for command in OPTIONAL:
        print(f"optional {command:24} {shutil.which(command) or 'not found'}")

    agbcc = os.environ.get("AGBCC_ROOT")
    if agbcc:
        compiler = Path(agbcc) / "bin" / "agbcc"
        print(f"required {'agbcc':24} {compiler if compiler.is_file() else 'MISSING'}")
        if not compiler.is_file():
            failures.append("agbcc")
    else:
        print(f"required {'agbcc':24} MISSING (AGBCC_ROOT unset)")
        failures.append("agbcc")

    print("\nversions")
    print("git:", first_line("git", "--version"))
    print("make:", first_line("make", "--version"))
    print("arm-none-eabi-as:", first_line("arm-none-eabi-as", "--version"))
    print("mGBA:", first_line("mgba", "--version"))

    if failures:
        print("\nmissing required components:", ", ".join(failures), file=sys.stderr)
        return 1
    print("\ncore toolchain: OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
