# Pokemon Sapphire SetMainCallback2 global reconstruction

The existing Japanese reconstruction remains the origin reference. All 12 cataloged releases (Japanese, English, German, French, Italian, Spanish) independently prove the same leaf behavior: the argument is stored at `gMain + 0x4`, a release-specific state byte at `gMain + 0x438, 0x43C` is cleared, and the function returns without a call. Observed compiler forms: inline-state-offset, literal-state-offset.

Per-release maps retain addresses, code-range hashes, RAM addresses, and raw-free control-flow evidence. No ROM instruction bytes are published. Names and behavior are corroborated by `pret/pokeruby` at `5784633ce4ef7ade1a7f2d2d0c288e3d5e6cdd7f`, `src/main.c`.
