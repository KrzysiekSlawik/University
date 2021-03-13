#include <stdio.h>
#include <stdint.h>
#include <limits.h>
uint32_t will_overflow(uint32_t x, uint32_t y)
{
    //overflow happens if sign(x) != sign(s) && sign(x) != sign(s) where s = x + y
    uint32_t s = x + y;
    return (((s ^ y) & (s ^ x)) >> 31) & 1;
}