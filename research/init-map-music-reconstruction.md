# Sapphire InitMapMusic reconstruction

The Japanese release `axp-j-rev0-retail` is the origin reference. All 12 cataloged releases (Japanese, English, German, French, Italian, Spanish) contain exactly one verified InitMapMusic routine. It clears the release-specific IWRAM gDisableMusic byte and calls ResetMapMusic. Per-release maps preserve ranges, hashes, call targets and raw-free control flow. No ROM instruction bytes are published. Naming is corroborated by `pret/pokeruby` at `5784633ce4ef7ade1a7f2d2d0c288e3d5e6cdd7f`, `src/sound.c`.
