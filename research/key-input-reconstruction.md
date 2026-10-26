# Sapphire key input reconstruction

The Japanese release `axp-j-rev0-retail` is the origin reference. All 12 cataloged releases (Japanese, English, German, French, Italian, Spanish) contain exactly one InitKeys and ReadKeys pair matching the `direct` profile. Options are read through a direct SaveBlock2 object.

The pair establishes repeat delays 5 and 40, derives active-high keys from REG_KEYINPUT with mask 0x03FF, implements repeat behavior, applies L-equals-A mode, and records watched-key presses. Per-release maps retain ranges, hashes, validated literals and control-flow counts without ROM instruction bytes. Naming and behavior are corroborated by `pret/pokeruby` at `5784633ce4ef7ade1a7f2d2d0c288e3d5e6cdd7f`, `src/main.c`.
