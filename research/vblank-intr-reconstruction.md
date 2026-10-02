# AXPJ revision 0 VBlank interrupt

The Japanese Sapphire handler at `0x08000574` conditionally synchronizes
the link, protects the sound VSync call with IME save/restore, advances both
VBlank counters around the optional callback, mirrors the PCM DMA counter,
runs sound and random processing, and acknowledges VBlank in both BIOS and
`gMain` interrupt-check fields.

The map records this version's exact sound-engine and callback-trampoline
addresses. Raw ROM instructions are not published.
