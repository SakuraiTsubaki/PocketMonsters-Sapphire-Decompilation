#include <stdint.h>

struct MainVBlankState
{
    uint8_t unknown_000[0x1C];
    volatile uint16_t intrCheck;
};

extern struct MainVBlankState gMain;
extern void VBlankIntrWait(void);

enum { INTR_FLAG_VBLANK = 1 };

/* AXPJ-rev0: 0x08000698..0x080006ae. */
void WaitForVBlank(void)
{
    gMain.intrCheck &= (uint16_t)~INTR_FLAG_VBLANK;
    VBlankIntrWait();
}

