#include <stdint.h>

typedef uint8_t bool8;
typedef void (*MainCallback)(void);

struct MainLoopState {
    MainCallback callback1;
    MainCallback callback2;
    uint8_t unknown_008[0x20];
    uint16_t heldKeysRaw;
    uint16_t newKeysRaw;
    uint16_t heldKeys;
    uint16_t newKeys;
};

struct LinkQueueState { uint8_t count; };
struct LinkLoopState { struct LinkQueueState sendQueue; struct LinkQueueState recvQueue; };

extern struct MainLoopState gMain;
extern struct LinkLoopState gLink;
extern bool8 gSoftResetDisabled;
extern bool8 gLinkTransferringData;
extern bool8 gFlashMemoryPresent;

extern void RegisterRamReset(uint32_t flags);
extern void InitKeys(void);
extern void InitIntrHandlers(void);
extern void m4aSoundInit(void);
extern void RtcInit(void);
extern void CheckForFlashMemory(void);
extern void InitMainCallbacks(void);
extern void InitMapMusic(void);
extern void SeedRngWithRtc(void);
extern void SetMainCallback2(MainCallback callback);
extern void ReadKeys(void);
extern void DoSoftReset(void);
extern bool8 LinkSendQueueReady(void);
extern bool8 LinkRecvQueueReady(void);
extern void LinkRecvPostprocess(void);
extern void UpdateLinkAndCallCallbacks(void);
extern void PlayTimeCounter_Update(void);
extern void MapMusicMain(void);
extern void WaitForVBlank(void);

enum {
    RESET_ALL = 0xFF,
    A_BUTTON = 1,
    B_BUTTON = 2,
    SELECT_BUTTON = 4,
    START_BUTTON = 8,
    B_START_SELECT = B_BUTTON | SELECT_BUTTON | START_BUTTON
};

/* AXPJ rev0: 0x0800024c..0x08000343; the back edge makes this non-returning. */
void AgbMain(void)
{
    RegisterRamReset(RESET_ALL);
    *(volatile uint16_t *)0x04000204 = 0x4014;
    InitKeys();
    InitIntrHandlers();
    m4aSoundInit();
    RtcInit();
    CheckForFlashMemory();
    InitMainCallbacks();
    InitMapMusic();
    SeedRngWithRtc();
    gSoftResetDisabled = 0;

    if (gFlashMemoryPresent != 1)
        SetMainCallback2(0);
    gLinkTransferringData = 0;

    for (;;) {
        ReadKeys();
        if (gSoftResetDisabled == 0
         && (gMain.heldKeysRaw & A_BUTTON)
         && (gMain.heldKeysRaw & B_START_SELECT) == B_START_SELECT)
            DoSoftReset();

        if (gLink.sendQueue.count > 1 && LinkSendQueueReady() == 1) {
            gLinkTransferringData = 1;
            UpdateLinkAndCallCallbacks();
            gLinkTransferringData = 0;
        } else {
            gLinkTransferringData = 0;
            UpdateLinkAndCallCallbacks();
            if (gLink.recvQueue.count > 1 && LinkRecvQueueReady() == 1) {
                gMain.newKeys = 0;
                LinkRecvPostprocess();
                gLinkTransferringData = 1;
                UpdateLinkAndCallCallbacks();
                gLinkTransferringData = 0;
            }
        }

        PlayTimeCounter_Update();
        MapMusicMain();
        WaitForVBlank();
    }
}


