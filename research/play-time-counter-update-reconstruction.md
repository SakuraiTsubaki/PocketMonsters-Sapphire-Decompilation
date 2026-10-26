# Sapphire play-time counter update reconstruction

The Japanese release `axp-j-rev0-retail` is the origin reference. All 12 cataloged releases (Japanese, English, German, French, Italian, Spanish) contain one verified Update routine in the same `direct` cluster. It advances 60 VBlanks per second, 60 seconds per minute and 60 minutes per hour, then calls the exact observed SetToMax entry above 999 hours.

Per-release maps retain code hashes, thresholds, state/save addresses and raw-free control-flow summaries. No ROM instruction bytes are published. Naming and behavior are corroborated by `pret/pokeruby` at `5784633ce4ef7ade1a7f2d2d0c288e3d5e6cdd7f`, `src/play_time.c`.
