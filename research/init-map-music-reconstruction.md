# InitMapMusic reconstruction

The selected Japanese retail target places `InitMapMusic` at `0x08071BE8` through `0x08071BF8`. The 16-byte Thumb routine clears `gDisableMusic`, calls `ResetMapMusic`, and returns.

Its publication-safe CFG records one direct call at `0x08071BF0` to `0x08071CF4` and omits raw halfwords. The exact ROM range SHA-256 is `208cc1ca4b9d4d1ab7ff55f003e775a720b1f0e2f8ac1be80107ce41c8a250be`.

Ruby, Sapphire, Emerald, FireRed, and LeafGreen use byte-identical code for this routine even though their ROM addresses differ. The C naming and semantics are corroborated by `pret/pokeruby` commit `5784633ce4ef7ade1a7f2d2d0c288e3d5e6cdd7f`, `src/sound.c`; the local retail ROM and its own SHA-256 remain the authoritative evidence for this repository.

