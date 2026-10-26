# Sapphire play-time counter controls reconstruction

The Japanese release `axp-j-rev0-retail` is the origin reference. All 12 cataloged releases (Japanese, English, German, French, Italian, Spanish) contain one verified Reset/Start/Stop/SetToMax control family using the `direct` save-storage profile. Start calls the observed SetToMax entry when hours exceed 999.

Per-release maps preserve ranges, hashes, state/save addresses and raw-free control-flow summaries. No ROM instruction bytes are published. Naming and behavior are corroborated by `pret/pokeruby` at `5784633ce4ef7ade1a7f2d2d0c288e3d5e6cdd7f`, `src/play_time.c`.
