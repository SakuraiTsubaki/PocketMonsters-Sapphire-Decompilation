# AXPJ revision 0 `AgbMain` reconstruction

The verified Sapphire entry CFG reaches the non-returning Thumb function at
`0x0800024C`. Its 21 direct call sites and 18 branch edges occur at the same
locations as Japanese Ruby, but seven external targets differ. The per-game
JSON map records the Sapphire addresses instead of reusing Ruby evidence.

Call order, reset and wait-state initialization, soft-reset condition, link
queue branches, three callback dispatches, and the frame tail match
`pret/pokeruby` `src/main.c` at commit
`5784633ce4ef7ade1a7f2d2d0c288e3d5e6cdd7f`.

The Japanese-only call at `0x08000328` remains conservatively named
`LinkRecvPostprocess`; its exact upstream symbol is not established. No ROM
instruction bytes are published in this reconstruction unit.
