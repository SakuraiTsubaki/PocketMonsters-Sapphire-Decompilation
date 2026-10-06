# DoSoftReset reconstruction

Target: AXPJ-rev0 (6a5ff7656531ab41d1ea9cd8f2d045ab6228405b43f3ee09ea3ff5077c0f60c9)

The verified Japanese `AgbMain` map calls `DoSoftReset` at 0x080006B8. A fresh Thumb trace closes at 0x08000714, observes a return, and is published without instruction halfwords. The code-only range SHA-256 is `d46172e96c054367d83ecffa85ecf5ac1c9adb9522f3a39c95692c30bab71270`; no ROM bytes are stored.

The straight-line routine disables the interrupt master switch, stops sound VSync and the scanline effect, then disables DMA channels 1, 2, and 3 through their control-high registers. This Ruby/Sapphire/Emerald-family build protects the RTC and passes the full `0xFF` reset mask to `SoftReset`.

Names were aligned with [pret/pokeruby](https://github.com/pret/pokeruby) at commit `5784633ce4ef7ade1a7f2d2d0c288e3d5e6cdd7f`, then independently checked against this ROM's function boundary, direct-call targets, hardware addresses, and constants.

