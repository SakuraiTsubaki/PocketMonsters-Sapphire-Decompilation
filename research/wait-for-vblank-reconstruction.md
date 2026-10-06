# WaitForVBlank reconstruction

Target: AXPJ-rev0 (6a5ff7656531ab41d1ea9cd8f2d045ab6228405b43f3ee09ea3ff5077c0f60c9)

The already verified Japanese `AgbMain` map calls `WaitForVBlank` at 0x08000698. A fresh conservative Thumb trace terminates at 0x080006AE, observes a return, and is published without instruction halfwords. The code-only ROM range SHA-256 is `076c65a08d6e9fa750583ef083463513054660ce8142cb32c461e4009aa6d1f9`; no ROM bytes are stored.

The function clears bit 0 of `gMain.intrCheck` at the proven offset `0x1C` before waiting. This build then calls the BIOS-facing `VBlankIntrWait` target 0x081B125C. The corresponding `VBlankIntr` reconstruction independently shows that the handler sets the same flag, closing the producer/consumer relationship.

Names were aligned with [pret/pokeruby](https://github.com/pret/pokeruby) at commit `5784633ce4ef7ade1a7f2d2d0c288e3d5e6cdd7f`, then checked against this ROM's addresses, control flow, literals, and state accesses. The upstream project is a naming reference, not a substitute for the local ROM evidence.

