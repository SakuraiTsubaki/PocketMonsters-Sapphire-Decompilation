# AXPJ rev0 PlayTimeCounter_Update reconstruction

The verified Japanese ROM implements `PlayTimeCounter_Update` across `0x0804FEF0..0x0804FF43`. Its 84-byte code range has SHA-256 `d2123c06ebdd4894ff626eb8002e6f0fcd8dfd1412d4460ea920acdc7e5ca4cf`; the repository retains only this digest and a publication-safe CFG.

The CFG has ten direct branch edges, one return, and one call to `PlayTimeCounter_SetToMax`. The routine runs only in state 1, rolls 60 VBlanks into one second, 60 seconds into one minute, and 60 minutes into one hour, then clamps values when hours exceed 999. Save fields are accessed at offsets `0x0E`, `0x10`, `0x11`, and `0x12` through the direct `gSaveBlock2` object.

Names and behavior are corroborated by `pret/pokeruby` commit `5784633ce4ef7ade1a7f2d2d0c288e3d5e6cdd7f`, `src/play_time.c`. `src/play_time_counter.c` preserves this title family's direct-versus-pointer save access rather than forcing all five games into one binary layout.

No ROM instruction bytes are published.

