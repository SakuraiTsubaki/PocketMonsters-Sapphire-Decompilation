# SeedRngWithRtc reconstruction

Target: AXPJ-rev0 (6a5ff7656531ab41d1ea9cd8f2d045ab6228405b43f3ee09ea3ff5077c0f60c9)

The verified Japanese `AgbMain` map calls `SeedRngWithRtc` at 0x080003E8. A fresh Thumb trace closes at 0x08000400, observes a return, and is published without instruction halfwords. The exact code-range SHA-256 is `414b9289eaa06ccc648464e5cc564789a10d2a0e538acdcb822d55f487431cd7`; no ROM bytes are stored.

The routine reads the RTC minute count, XOR-folds its upper and lower 16-bit halves, and passes the resulting 16-bit value to `SeedRng`. Ruby and Sapphire have identical code bytes at this boundary.

Names were aligned with [pret/pokeruby](https://github.com/pret/pokeruby) at commit `5784633ce4ef7ade1a7f2d2d0c288e3d5e6cdd7f`, then checked against this ROM's boundary, direct-call targets, constants, and data flow.

