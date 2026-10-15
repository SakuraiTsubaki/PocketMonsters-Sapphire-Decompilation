# AXPJ rev0 RNG reconstruction

The verified Japanese ROM reaches `Random` at `0x0803E130` from `VBlankIntr`; `SeedRng` begins at `0x0803E150`. Publication-safe CFGs close both straight-line Thumb functions at one return with no calls.

Literal and instruction-shape validation proves the 32-bit recurrence `state = 1103515245 * state + 24691`, returning bits 31..16. Both routines address `gRngValue` at `0x03004748`. Sapphire and Ruby have identical function-range hashes.

Names and semantics are corroborated by pinned primary source `pret/pokeruby@5784633ce4ef7ade1a7f2d2d0c288e3d5e6cdd7f`, `src/random.c`. No ROM instruction bytes are published.
