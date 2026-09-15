#include <stdbool.h>
#include <stdint.h>

/*
 * Reconstructed from directly observed Sapphire targets.
 *
 * SAPPHIRE_DATE_YEAR_LOOP_FIXED = 0:
 *   AXPJ rev0, AXPE rev0, AXPE rev1, AXPF rev0, AXPI rev0
 *
 * SAPPHIRE_DATE_YEAR_LOOP_FIXED = 1:
 *   AXPE rev2, AXPD rev1, AXPF rev1, AXPI rev1
 *
 * Semantic symbol names are provisional until callers are reconstructed.
 */
#ifndef SAPPHIRE_DATE_YEAR_LOOP_FIXED
#error "Define SAPPHIRE_DATE_YEAR_LOOP_FIXED to 0 or 1 for the selected target"
#endif

#if SAPPHIRE_DATE_YEAR_LOOP_FIXED != 0 && SAPPHIRE_DATE_YEAR_LOOP_FIXED != 1
#error "SAPPHIRE_DATE_YEAR_LOOP_FIXED must be 0 or 1"
#endif

static const uint32_t sDaysInMonth[12] = {
    31, 28, 31, 30, 31, 30,
    31, 31, 30, 31, 30, 31,
};

uint8_t BcdToBinary(uint8_t value)
{
    uint8_t low;
    uint8_t high;

    if (value > 0x9F)
        return 0xFF;

    low = value & 0x0F;
    if (low > 9)
        return 0xFF;

    high = (value >> 4) & 0x0F;
    return (uint8_t)(high * 10 + low);
}

bool IsLeapYear(uint8_t year)
{
    if ((year & 3) != 0)
        return false;
    if (year % 100 != 0)
        return true;
    return year % 400 == 0;
}

uint16_t CalcDateOrdinal(uint8_t year, uint8_t month, uint8_t day)
{
    uint16_t total = 0;
    int yearIndex;
    int monthCount;
    const uint32_t *monthDays;

    yearIndex = (int)year - 1;
#if SAPPHIRE_DATE_YEAR_LOOP_FIXED
    while (yearIndex >= 0)
#else
    while (yearIndex > 0)
#endif
    {
        total = (uint16_t)(total + 365);
        if (IsLeapYear((uint8_t)yearIndex))
            total = (uint16_t)(total + 1);
        --yearIndex;
    }

    monthCount = (int)month - 1;
    if (monthCount > 0) {
        monthDays = sDaysInMonth;
        do {
            total = (uint16_t)(total + *monthDays++);
            --monthCount;
        } while (monthCount != 0);
    }

    if (month > 2 && IsLeapYear(year))
        total = (uint16_t)(total + 1);

    total = (uint16_t)(total + day);
    return total;
}

uint16_t BcdDateToOrdinal(const uint8_t date[3])
{
    uint8_t year = BcdToBinary(date[0]);
    uint8_t month = BcdToBinary(date[1]);
    uint8_t day = BcdToBinary(date[2]);

    return CalcDateOrdinal(year, month, day);
}
