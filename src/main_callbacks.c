#include <stddef.h>
#include <stdint.h>
typedef uint8_t bool8; typedef void (*MainCallback)(void);
struct MainState { MainCallback callback1; MainCallback callback2; uint8_t unknown_008[0x24]; uint16_t heldKeys; uint8_t unknown_02e[0x40a]; uint8_t state; };
extern struct MainState gMain; extern uint32_t gLinkStatus; extern bool8 gShouldAdvanceLinkState; extern uint16_t gSendCmd[]; extern uint16_t gRecvCmds[];
extern uint32_t LinkMain1(bool8 *,uint16_t *,uint16_t *); extern void LinkMain2(uint16_t *); extern bool8 LinkReceivedNothingOverride(void); extern void CopyrightScreenInit(void);
void CallCallbacks(void); void SetMainCallback2(MainCallback);
/* AXPJ rev0: 0x08000348..0x0800037b */
void UpdateLinkAndCallCallbacks(void){gLinkStatus=LinkMain1(&gShouldAdvanceLinkState,gSendCmd,gRecvCmds);LinkMain2(&gMain.heldKeys);if(!(gLinkStatus&0x100)||LinkReceivedNothingOverride()!=1)CallCallbacks();}
/* AXPJ rev0: 0x08000390..0x080003a5 */
void InitMainCallbacks(void){*(uint32_t *)((uint8_t *)&gMain+0x20)=0;*(uint32_t *)((uint8_t *)&gMain+0x24)=0;gMain.callback1=NULL;SetMainCallback2(CopyrightScreenInit);}
/* AXPJ rev0: 0x080003b0..0x080003cd */
void CallCallbacks(void){if(gMain.callback1)gMain.callback1();if(gMain.callback2)gMain.callback2();}
/* AXPJ rev0: 0x080003d4..0x080003e3 */
void SetMainCallback2(MainCallback callback){gMain.callback2=callback;gMain.state=0;}
