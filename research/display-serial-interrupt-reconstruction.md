# Sapphire display and serial interrupt reconstruction

The Japanese release `axp-j-rev0-retail` is the origin reference. All 12 cataloged releases (Japanese, English, German, French, Italian, Spanish) contain exactly one HBlank, VCount and Serial handler matching the `rs` structural profile. VCount invokes the optional vcount callback.

Each handler sets both the shared IWRAM interrupt check and gMain.intrCheck with HBlank 0x0002, VCount 0x0004 or Serial 0x0080. Per-release maps retain ranges, code hashes, validated literals and call targets without publishing ROM instruction bytes. Naming and behavior are corroborated by `pret/pokeruby` at `5784633ce4ef7ade1a7f2d2d0c288e3d5e6cdd7f`, `src/main.c`.
