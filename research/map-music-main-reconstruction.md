# AXPJ rev0 MapMusicMain reconstruction

The verified Japanese ROM implements `MapMusicMain` across `0x08071BFC..0x08071CE3`. The contiguous 232-byte function range has SHA-256 `aae49f25a7ff56e264652c7944d6913586830fca9c93fb2f71785fb2a580f9c5`; only its hash and publication-safe CFG are retained.

The function uses an agbcc-style absolute-word jump table with eight entries. `SakuraiTsubaki/Decompilation` commit `4f687a912ecc40823a17a67fa885768cdca12e98` extends the shared Thumb tracer to resolve this exact compiler pattern without treating the literal pool and table as instructions. The resulting CFG reaches every case and records eight direct calls.

Behavior and names are corroborated by `pret/pokeruby` commit `5784633ce4ef7ade1a7f2d2d0c288e3d5e6cdd7f`, `src/sound.c`: state 1 starts the current BGM, state 5 waits for BGM completion, state 6 waits for both BGM and fanfare completion before starting the queued track, and state 7 performs the corresponding fade-in transition. Sapphire preserves the Ruby control-flow shape while every direct target is recorded from the Sapphire ROM.

`src/map_music_main.c` is a behavioral reconstruction bound to the ROM CFG, jump-table targets, call order, and code-range hash. No ROM instruction bytes or table words are published.

