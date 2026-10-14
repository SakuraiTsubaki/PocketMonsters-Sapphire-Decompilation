# AXPJ-rev0 trainer-ID helper reconstruction

The verified Japanese ROM contains the following four-byte trainer-ID helpers:

- `write_word_to_mem`: `0x0804FF74..0x0804FF84`, SHA-256 `b219139d5a72a06b84b59c718f14ddff68a10a2a3e7c77994251bbc8cd5ca40b`.
- `copy_word_to_mem`: `0x0804FF84..0x0804FFA0`, SHA-256 `e2ede032f2797356414ff7d8a4c5803c4350847c7d86acc47bf4ba92bb5e75e5`.

The setters serialize a 32-bit value in little-endian order. Copy helpers move exactly four bytes; the Emerald-specific getter reconstructs the same little-endian value. Every function has one observed return, and none calls another routine.

Names and behavior are corroborated by `pret/pokeruby` commit `5784633ce4ef7ade1a7f2d2d0c288e3d5e6cdd7f`, `src/new_game.c`. The ROM digests and publication-safe CFGs are authoritative here. No ROM instruction bytes are published.
