#include <stdint.h>

typedef int32_t s32;
typedef uint8_t u8;
typedef uint32_t u32;

void write_word_to_mem(u32 var, u8 *dataPtr)
{
    dataPtr[0] = var;
    dataPtr[1] = var >> 8;
    dataPtr[2] = var >> 16;
    dataPtr[3] = var >> 24;
}

void copy_word_to_mem(u8 *copyTo, const u8 *copyFrom)
{
    s32 i;

    for (i = 0; i < 4; i++)
        copyTo[i] = copyFrom[i];
}
