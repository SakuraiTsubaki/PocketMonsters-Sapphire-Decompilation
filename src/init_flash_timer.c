#include <stdint.h>

typedef void (*IntrFunc)(void);

extern IntrFunc gFlashTimerIntrFunc;
extern void SetFlashTimerIntr(uint8_t timer, IntrFunc handler);

void InitFlashTimer(void)
{
    SetFlashTimerIntr(2, gFlashTimerIntrFunc);
}
