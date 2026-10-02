#include <stdint.h>
typedef uint8_t bool8;typedef void (*IntrCallback)(void);typedef void (*MainCallback)(void);
struct MainVBlankState{MainCallback callback1,callback2;uint8_t unknown_008[4];IntrCallback vblankCallback,hblankCallback,vcountCallback,serialCallback;uint16_t intrCheck;uint16_t unknown_01e;uint32_t vblankCounter1;uint32_t vblankCounter2;};
struct SoundInfoVBlank{uint8_t unknown_000[4];uint8_t pcmDmaCounter;};
extern struct MainVBlankState gMain;extern bool8 gLinkVSyncDisabled;extern uint8_t gPcmDmaCounter;extern struct SoundInfoVBlank gSoundInfo;
extern void LinkVSync(void);extern void m4aSoundVSync(void);extern void m4aSoundMain(void);extern void sub_800C35C(void);extern uint16_t Random(void);
#define REG_IME (*(volatile uint16_t *)0x04000208)
#define INTR_CHECK (*(volatile uint16_t *)0x03007FF8)
#define INTR_FLAG_VBLANK 1
/* AXPJ rev0: 0x08000574..0x080005d5. */
void VBlankIntr(void)
{
 uint16_t savedIme;
 if(!gLinkVSyncDisabled)LinkVSync();
 savedIme=REG_IME;REG_IME=0;m4aSoundVSync();REG_IME=savedIme;
 gMain.vblankCounter1++;
 if(gMain.vblankCallback)gMain.vblankCallback();
 gMain.vblankCounter2++;
 gPcmDmaCounter=gSoundInfo.pcmDmaCounter;
 m4aSoundMain();sub_800C35C();Random();
 INTR_CHECK|=INTR_FLAG_VBLANK;gMain.intrCheck|=INTR_FLAG_VBLANK;
}
