#include <stdint.h>

typedef uint8_t u8;
typedef uint16_t u16;

struct SaveBlock2 {
    u8 unknown_000[0x0E];
    u16 playTimeHours;
    u8 playTimeMinutes;
    u8 playTimeSeconds;
    u8 playTimeVBlanks;
};

extern struct SaveBlock2 gSaveBlock2;
extern u8 sPlayTimeCounterState;
extern void PlayTimeCounter_SetToMax(void);

enum {
    PLAY_TIME_STOPPED,
    PLAY_TIME_RUNNING,
    PLAY_TIME_MAXED_OUT
};

void PlayTimeCounter_Update(void)
{
    if (sPlayTimeCounterState == PLAY_TIME_RUNNING) {
        gSaveBlock2.playTimeVBlanks++;
        if (gSaveBlock2.playTimeVBlanks > 59) {
            gSaveBlock2.playTimeVBlanks = 0;
            gSaveBlock2.playTimeSeconds++;
            if (gSaveBlock2.playTimeSeconds > 59) {
                gSaveBlock2.playTimeSeconds = 0;
                gSaveBlock2.playTimeMinutes++;
                if (gSaveBlock2.playTimeMinutes > 59) {
                    gSaveBlock2.playTimeMinutes = 0;
                    gSaveBlock2.playTimeHours++;
                    if (gSaveBlock2.playTimeHours > 999)
                        PlayTimeCounter_SetToMax();
                }
            }
        }
    }
}

