# Sapphire interrupt initialization reconstruction

The Japanese release `axp-j-rev0-retail` is the origin reference. All 12 cataloged releases (Japanese, English, German, French, Italian, Spanish) contain exactly one InitIntrHandlers structure and its callback setters matching the `rs` profile. VBlank is enabled with direct IE and DISPSTAT writes.

The implementation copies 14 table entries, DMA-copies the 0x800-byte interrupt dispatcher with DMA3 control 0x84000200, installs the IWRAM vector, clears callbacks and enables VBlank. Per-release maps retain code ranges, hashes, validated literals and call targets without ROM instruction bytes. Naming and behavior are corroborated by `pret/pokeruby` at `5784633ce4ef7ade1a7f2d2d0c288e3d5e6cdd7f`, `src/main.c`.
