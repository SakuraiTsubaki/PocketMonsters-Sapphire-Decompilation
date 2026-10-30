# Sapphire VBlankIntrWait reconstruction

`axp-j-rev0-retail` is the Japanese origin reference. All 12 cataloged releases (Japanese, English, German, French, Italian, Spanish) use the BIOS-call WaitForVBlank variant and resolve it to the same three-instruction SDK wrapper: clear r2, invoke SWI 5, then return through LR. Emerald and FireRed/LeafGreen use their verified volatile-poll implementation instead and are intentionally outside this wrapper catalog. No ROM bytes or instruction dumps are published.
