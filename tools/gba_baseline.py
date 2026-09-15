#!/usr/bin/env python3
"""Generate a reproducible first-pass binary map for a local GBA ROM.

ROM images remain outside the repository. This tool records only derived
metadata useful for decompilation: identity, header facts, block hashes,
ROM-pointer references, and lightweight executable signatures.
"""

from __future__ import annotations

import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
import struct

GBA_ROM_BASE = 0x08000000
GBA_ROM_END = 0x0A000000


def digest(data: bytes, name: str) -> str:
    h = hashlib.new(name)
    h.update(data)
    return h.hexdigest()


def ascii_field(raw: bytes) -> str:
    return raw.rstrip(b"\0").decode("ascii", errors="replace")


def gba_header(data: bytes) -> dict[str, object]:
    if len(data) < 0xC0:
        raise ValueError("file is too small to contain a complete GBA header")
    computed = (-(sum(data[0xA0:0xBD]) + 0x19)) & 0xFF
    stored = data[0xBD]
    return {
        "title": ascii_field(data[0xA0:0xAC]),
        "game_code": ascii_field(data[0xAC:0xB0]),
        "maker_code": ascii_field(data[0xB0:0xB2]),
        "fixed_value": data[0xB2],
        "main_unit_code": data[0xB3],
        "device_type": data[0xB4],
        "revision": data[0xBC],
        "header_checksum": stored,
        "computed_header_checksum": computed,
        "header_checksum_valid": stored == computed,
    }


def decode_entry_branch(data: bytes) -> dict[str, object] | None:
    if len(data) < 4:
        return None
    instr = struct.unpack_from("<I", data, 0)[0]
    if (instr & 0x0F000000) != 0x0A000000:
        return {"instruction": f"0x{instr:08X}", "kind": "not_arm_branch"}
    imm24 = instr & 0x00FFFFFF
    if imm24 & 0x00800000:
        imm24 -= 0x01000000
    target = 8 + (imm24 << 2)
    return {
        "instruction": f"0x{instr:08X}",
        "kind": "arm_branch",
        "target_offset": target,
        "target_address": f"0x{GBA_ROM_BASE + target:08X}",
    }


def block_hashes(data: bytes, block_size: int) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for offset in range(0, len(data), block_size):
        block = data[offset: offset + block_size]
        rows.append({"offset": offset, "size": len(block), "sha256": digest(block, "sha256")})
    return rows


def scan_rom_pointers(data: bytes, sample_limit: int) -> dict[str, object]:
    refs: list[dict[str, int | str]] = []
    targets_by_block: Counter[int] = Counter()
    total = 0
    for source in range(0, len(data) - 3, 4):
        value = struct.unpack_from("<I", data, source)[0]
        if not (GBA_ROM_BASE <= value < GBA_ROM_END):
            continue
        target = value - GBA_ROM_BASE
        if target >= len(data):
            continue
        total += 1
        targets_by_block[target >> 16] += 1
        if len(refs) < sample_limit:
            refs.append({"source_offset": source, "value": f"0x{value:08X}", "target_offset": target})
    return {
        "aligned_pointer_count": total,
        "sample_limit": sample_limit,
        "sample": refs,
        "target_64k_blocks": [
            {"block": block, "offset": block << 16, "references": count}
            for block, count in sorted(targets_by_block.items())
        ],
    }


def scan_thumb_returns(data: bytes, sample_limit: int) -> dict[str, object]:
    hits: list[int] = []
    total = 0
    for offset in range(0, len(data) - 1, 2):
        if data[offset] == 0x70 and data[offset + 1] == 0x47:
            total += 1
            if len(hits) < sample_limit:
                hits.append(offset)
    return {
        "bx_lr_halfword_count": total,
        "sample_limit": sample_limit,
        "sample_offsets": hits,
        "warning": "heuristic signature; data may contain false positives",
    }


def build_report(path: Path, block_size: int, sample_limit: int) -> dict[str, object]:
    data = path.read_bytes()
    return {
        "schema_version": 1,
        "source": {"filename": path.name, "size": len(data), "sha1": digest(data, "sha1"), "sha256": digest(data, "sha256")},
        "header": gba_header(data),
        "entrypoint": decode_entry_branch(data),
        "blocks": {"block_size": block_size, "hashes": block_hashes(data, block_size)},
        "rom_pointers": scan_rom_pointers(data, sample_limit),
        "thumb_signatures": scan_thumb_returns(data, sample_limit),
    }


def parse_int(value: str) -> int:
    return int(value, 0)


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate a first-pass GBA ROM decompilation baseline")
    parser.add_argument("rom", type=Path, help="local .gba image; never committed")
    parser.add_argument("--block-size", type=parse_int, default=0x10000, help="hash block size, default 0x10000")
    parser.add_argument("--sample-limit", type=int, default=4096, help="maximum pointer/signature samples")
    parser.add_argument("--out", type=Path, help="write JSON report to this path instead of stdout")
    args = parser.parse_args()

    if not args.rom.is_file():
        parser.error(f"ROM not found: {args.rom}")
    if args.block_size <= 0:
        parser.error("--block-size must be positive")
    if args.sample_limit < 0:
        parser.error("--sample-limit must be non-negative")

    try:
        report = build_report(args.rom, args.block_size, args.sample_limit)
    except ValueError as exc:
        parser.error(str(exc))

    rendered = json.dumps(report, indent=2, ensure_ascii=False) + "\n"
    if args.out:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_text(rendered, encoding="utf-8")
    else:
        print(rendered, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
