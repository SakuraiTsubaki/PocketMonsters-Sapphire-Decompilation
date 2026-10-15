# Pokémon Sapphire RNG release-catalog reconstruction

The existing Japanese reconstruction is retained as the origin reference. Eleven additional SHA-256-gated identities were independently verified, covering three English revisions and two revisions each for German, French, Italian, and Spanish. Each report binds the adjacent `Random`/`SeedRng` pair to its shared IWRAM state and publication-safe CFGs.

All twelve identities implement `state = 1103515245 * state + 24691`, return bits 31..16, and share the same reconstructed `src/random.c`; addresses remain per release. Naming and semantics follow `pret/pokeruby@5784633ce4ef7ade1a7f2d2d0c288e3d5e6cdd7f`, `src/random.c`. ROM halfwords are omitted.
