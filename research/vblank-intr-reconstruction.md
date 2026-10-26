# Sapphire VBlankIntr reconstruction

The Japanese release `axp-j-rev0-retail` is the origin reference. All 12 cataloged releases (Japanese, English, German, French, Italian, Spanish) have a VBlank handler immediately after the verified serial callback setter and match the `rs` control-flow profile. The sound VSync call is protected by REG_IME save/disable/restore.

Per-release maps preserve code hashes, call targets, validated state addresses and the dependency hash for interrupt initialization. CFG evidence omits raw halfwords and no ROM instruction bytes are published. Naming and behavior are corroborated by `pret/pokeruby` at `5784633ce4ef7ade1a7f2d2d0c288e3d5e6cdd7f`, `src/main.c`.
