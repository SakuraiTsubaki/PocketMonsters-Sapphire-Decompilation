#include <stdint.h>
typedef void (*IntrCallback)(void);typedef void (*MainCallback)(void);
struct MainInterruptState{MainCallback callback1,callback2;uint8_t unknown_008[4];IntrCallback vblankCallback,hblankCallback,vcountCallback,serialCallback;uint16_t intrCheck;};
extern struct MainInterruptState gMain;
#define INTR_CHECK (*(volatile uint16_t *)0x03007FF8)
#define INTR_FLAG_HBLANK 0x0002
#define INTR_FLAG_VCOUNT 0x0004
#define INTR_FLAG_SERIAL 0x0080
/* AXPJ rev0: 0x08000604, 0x08000634 and 0x08000664. */
void HBlankIntr(void){if(gMain.hblankCallback)gMain.hblankCallback();INTR_CHECK|=INTR_FLAG_HBLANK;gMain.intrCheck|=INTR_FLAG_HBLANK;}
void VCountIntr(void){if(gMain.vcountCallback)gMain.vcountCallback();INTR_CHECK|=INTR_FLAG_VCOUNT;gMain.intrCheck|=INTR_FLAG_VCOUNT;}
void SerialIntr(void){if(gMain.serialCallback)gMain.serialCallback();INTR_CHECK|=INTR_FLAG_SERIAL;gMain.intrCheck|=INTR_FLAG_SERIAL;}

