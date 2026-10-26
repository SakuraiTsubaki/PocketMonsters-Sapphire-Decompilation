# Pokemon Sapphire SeedRngWithRtc reconstruction

The Japanese release `axp-j-rev0-retail` is the origin reference. All 12 cataloged releases (Japanese, English, German, French, Italian, Spanish) contain exactly one matching 24-byte Thumb function followed by the required 0x0000FFFF mask literal. The function obtains an RTC minute count, XOR-folds its upper and lower 16-bit halves, and passes the result to `SeedRng`.

The reconstructed C source contains no ROM instructions. Per-release CFGs omit raw halfwords, while maps preserve ranges, hashes and the release-specific `RtcGetMinuteCount` and `SeedRng` targets. Naming and semantics are corroborated by `pret/pokeruby` at `5784633ce4ef7ade1a7f2d2d0c288e3d5e6cdd7f`, `src/main.c`.
