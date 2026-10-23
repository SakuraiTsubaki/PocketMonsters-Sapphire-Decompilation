# Pokemon Sapphire WaitForVBlank global reconstruction

The existing Japanese reconstruction remains the origin reference. All 12 cataloged releases (Japanese, English, German, French, Italian, Spanish) clear bit zero of `gMain.intrCheck` at offset `0x1C` before waiting for VBlank. Observed wait modes: bios-call.

Per-release evidence records the function range and hash, RAM base, literal locations, call target where present, and a raw-free CFG. The catalog also recalculates the legacy origin map's PC-relative literal locations instead of carrying forward a hand-entered address. No ROM instructions or binaries are published.

Naming and behavior are corroborated by `pret/pokeruby` at `5784633ce4ef7ade1a7f2d2d0c288e3d5e6cdd7f`, `src/main.c`.
