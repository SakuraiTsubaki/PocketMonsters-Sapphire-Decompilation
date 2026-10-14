# AXPJ-rev0 play-time counter control reconstruction

The verified Japanese ROM contains four control routines surrounding the previously reconstructed update routine:

- `PlayTimeCounter_Reset`: `0x0804FE9C..0x0804FEB2`, 22 bytes, SHA-256 `e44a0ece72a9a69ff423028e141af0efb7d82d53044888da1ac471b1b5c53781`.
- `PlayTimeCounter_Start`: `0x0804FEBC..0x0804FED6`, 26 bytes, SHA-256 `202148e4d04e48f8ed95bffbdb66f2e77211e26651ece55fd2ff39db9ecb2ffe`.
- `PlayTimeCounter_Stop`: `0x0804FEE4..0x0804FEEC`, 8 bytes, SHA-256 `af63598031ab14af781d7cf7af24c648b7677228730b316da86ab311a3171699`.
- `PlayTimeCounter_SetToMax`: `0x0804FF50..0x0804FF66`, 22 bytes, SHA-256 `1ba2a1d5e4ca75ca422147c1d135dabd416a4defe35836cade303dd2d4248a33`.

The publication-safe CFGs prove one return for every routine. Only `PlayTimeCounter_Start` has a call: when the saved hour count exceeds 999, it calls the observed `PlayTimeCounter_SetToMax` entry. Reset clears the state and all four saved counters, Stop clears only the state, and SetToMax stores state 2 with 999:59:59 plus 59 VBlanks.

Save access is recorded as `direct-gSaveBlock2`. Names and behavior are corroborated by `pret/pokeruby` commit `5784633ce4ef7ade1a7f2d2d0c288e3d5e6cdd7f`, `src/play_time.c`.

No ROM instruction bytes are published.
