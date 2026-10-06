# AXPJ revision 0 display and serial interrupts

Japanese Sapphire conditionally dispatches the HBlank, VCount, and serial
callbacks stored in `gMain`, then acknowledges each interrupt in the BIOS
check word and `gMain.intrCheck`. Unlike Emerald, this VCount handler has no
sound VSync call. The game-specific map records all boundaries, callback
trampoline targets, offsets, flags, and a publication-safe ROM range hash.

