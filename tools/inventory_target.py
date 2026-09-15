#!/usr/bin/env python3
"""Create a metadata-only inventory for a locally supplied target build.

This tool does not decrypt, unpack, upload, or modify target data. It records
relative filenames, sizes, and SHA-256 hashes so later reverse-engineering work
can be tied to an exact local build without committing retail content or keys.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable

SENSITIVE_FILENAMES = {"prod.keys", "title.keys"}
SENSITIVE_SUFFIXES = {".keys"}
CHUNK_SIZE = 1024 * 1024


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(CHUNK_SIZE), b""):
            digest.update(chunk)
    return digest.hexdigest()


def is_sensitive(path: Path) -> bool:
    name = path.name.lower()
    return name in SENSITIVE_FILENAMES or path.suffix.lower() in SENSITIVE_SUFFIXES


def iter_files(target: Path) -> Iterable[tuple[Path, Path]]:
    if target.is_file():
        yield target, Path(target.name)
        return
    for path in sorted(p for p in target.rglob("*") if p.is_file()):
        yield path, path.relative_to(target)


def build_inventory(args: argparse.Namespace) -> dict:
    target = args.target.resolve()
    if not target.exists():
        raise SystemExit(f"Target does not exist: {target}")
    files = []
    omitted_sensitive_files = 0
    total_bytes = 0
    for absolute, relative in iter_files(target):
        if is_sensitive(absolute):
            omitted_sensitive_files += 1
            continue
        size = absolute.stat().st_size
        total_bytes += size
        files.append({"path": relative.as_posix(), "size": size, "sha256": sha256_file(absolute), "suffix": absolute.suffix.lower()})
    return {
        "schema_version": 1,
        "target_id": args.target_id,
        "product": args.product,
        "region": args.region,
        "language": args.language,
        "version": args.version,
        "update": args.update,
        "verification": "Observed",
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "source_kind": "file" if target.is_file() else "directory",
        "source_name": target.name,
        "file_count": len(files),
        "total_bytes": total_bytes,
        "omitted_sensitive_files": omitted_sensitive_files,
        "files": files,
        "notes": ["Generated from a local target supplied by the researcher.", "No retail content or key material is embedded in this manifest.", "Local absolute paths are intentionally not recorded."],
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("target", type=Path, help="Local target file or extracted directory")
    parser.add_argument("--target-id", required=True, help="Stable research identifier")
    parser.add_argument("--product", required=True, help="Product name")
    parser.add_argument("--region", default="TBD")
    parser.add_argument("--language", default="TBD")
    parser.add_argument("--version", default="TBD")
    parser.add_argument("--update", default="base")
    parser.add_argument("--output", type=Path, required=True, help="JSON output path")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    inventory = build_inventory(args)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(inventory, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Wrote {args.output}: {inventory['file_count']} files, {inventory['total_bytes']} bytes")


if __name__ == "__main__":
    main()
