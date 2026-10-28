# Sapphire flash-memory detection reconstruction

The Japanese release `axp-j-rev0-retail` is the origin reference. All 12 cataloged releases (Japanese, English, German, French, Italian, Spanish) preserve the same 38-byte control-flow shape: `IdentifyFlash` returns zero on success, the presence flag is set, and `InitFlashTimer` is called only on that success path. Per-release maps retain addresses, calls and code hashes without ROM bytes or instruction halfwords. `pret/pokeruby` commit `5784633ce4ef7ade1a7f2d2d0c288e3d5e6cdd7f`, `src/load_save.c`, is the naming basis.
