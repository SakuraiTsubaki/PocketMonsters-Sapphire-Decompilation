# Pokemon Sapphire ClearPokemonCrySongs reconstruction

The Japanese release `axp-j-rev0-retail` is the origin reference. All 12 cataloged releases (Japanese, English, German, French, Italian, Spanish) contain exactly one function with the same 26-byte Thumb structure: a zero halfword is placed on the stack, then `CpuSet` repeats it for 52 halfwords (104 bytes) into the release-specific `gPokemonCrySongs` address.

The reconstructed C source expresses that behavior without embedding ROM instructions. Per-release maps retain function ranges, hashes, call targets, destination addresses, and raw-free control-flow evidence. Naming and semantics are corroborated by `pret/pokeruby` at `5784633ce4ef7ade1a7f2d2d0c288e3d5e6cdd7f`, `src/main.c`.
