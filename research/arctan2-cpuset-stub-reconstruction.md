# Sapphire ArcTan2 and CpuSet BIOS stub reconstruction

axp-j-rev0-retail is the Japanese origin reference. All 12 builds (Japanese, English, German, French, Italian, Spanish) verify ArcTan2 SWI 0x0A and CpuSet SWI 0x0B at SDK-layout offsets from the LZ77 VRAM wrapper, including Ruby debug. CpuSet has duplicate signatures in 0 build(s), so only the candidate at the verified -4/-8 position is selected. Pinned libagbsyscall sources corroborate symbols and calling conventions. No ROM bytes are published.
