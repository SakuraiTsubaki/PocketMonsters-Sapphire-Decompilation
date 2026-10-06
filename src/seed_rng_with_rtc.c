#include <stdint.h>

extern uint32_t RtcGetMinuteCount(void);
extern void SeedRng(uint16_t seed);

/* AXPJ-rev0: 0x080003E8..0x08000400. */
void SeedRngWithRtc(void)
{
    uint32_t seed = RtcGetMinuteCount();
    seed = (seed >> 16) ^ (seed & 0xFFFF);
    SeedRng((uint16_t)seed);
}

