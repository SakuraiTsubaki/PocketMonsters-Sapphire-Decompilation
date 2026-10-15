#include <stdint.h>

#define ISO_RANDOMIZE1(value) (1103515245u * (value) + 24691u)

uint32_t gRngValue;

uint16_t Random(void)
{
    gRngValue = ISO_RANDOMIZE1(gRngValue);
    return (uint16_t)(gRngValue >> 16);
}

void SeedRng(uint16_t seed)
{
    gRngValue = seed;
}
