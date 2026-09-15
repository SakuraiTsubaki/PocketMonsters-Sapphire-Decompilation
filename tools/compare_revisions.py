#!/usr/bin/env python3
"""Compare two same-size GBA ROMs without redistributing either image.

The report records changed byte offsets, compact contiguous ranges, changed
64 KiB blocks, and recognizable Thumb conditional-branch condition changes.
ROM images remain local and are never written to the repository.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import struct
from pathlib import Path

COND = {
    0x0: "EQ", 0x1: "NE", 0x2: "CS", 0x3: "CC",
    0x4: "MI", 0x5: "PL", 0x6: "VS", 0x7: "VC",
    0x8: "HI", 0x9: "LS", 0xA: "GE", 0xB: "LT",
    0xC: "GT", 0xD: "LE",
}
BLOCK_SIZE = 0x10000


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def ranges(offsets: list[int]) -> list[list[int]]:
    if not offsets:
        return []
    result: list[list[int]] = []
    start = previous = offsets[0]
    for offset in offsets[1:]:
        if offset == previous + 1:
            previous = offset
            continue
        result.append([start, previous])
        start = previous = offset
    result.append([start, previous])
    return result


def decode_thumb_conditional(data: bytes, changed_offset: int) -> dict | None:
    halfword_offset = changed_offset & ~1
    if halfword_offset + 2 > len(data):
        return None
    halfword = struct.unpack_from("<H", data, halfword_offset)[0]
    if (halfword & 0xF000) != 0xD000:
        return None
    condition = (halfword >> 8) & 0xF
    if condition not in COND:
        return None
    imm8 = halfword & 0xFF
    displacement = (imm8 - 0x100 if imm8 & 0x80 else imm8) << 1
    target = halfword_offset + 4 + displacement
    return {
        "halfword_offset": halfword_offset,
        "halfword": f"0x{halfword:04X}",
        "mnemonic": f"B{COND[condition]}",
        "condition": COND[condition],
        "target_offset": target,
    }


def compare(before: Path, after: Path) -> dict:
    left = before.read_bytes()
    right = after.read_bytes()
    if len(left) != len(right):
        raise ValueError("inputs must have the same size")

    changed = [i for i, (a, b) in enumerate(zip(left, right)) if a != b]
    changed_blocks = sorted({offset // BLOCK_SIZE for offset in changed})
    details = []
    for offset in changed:
        item = {"offset": offset, "before": left[offset], "after": right[offset]}
        old_thumb = decode_thumb_conditional(left, offset)
        new_thumb = decode_thumb_conditional(right, offset)
        if old_thumb and new_thumb and old_thumb != new_thumb:
            item["thumb_before"] = old_thumb
            item["thumb_after"] = new_thumb
        details.append(item)

    return {
        "schema_version": 1,
        "before": {"filename": before.name, "size": len(left), "sha256": sha256(left)},
        "after": {"filename": after.name, "size": len(right), "sha256": sha256(right)},
        "changed_byte_count": len(changed),
        "changed_ranges": ranges(changed),
        "changed_64k_blocks": changed_blocks,
        "changes": details,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("before", type=Path)
    parser.add_argument("after", type=Path)
    parser.add_argument("--out", type=Path)
    args = parser.parse_args()

    try:
        report = compare(args.before, args.after)
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
