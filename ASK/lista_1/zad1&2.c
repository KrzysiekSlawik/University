#include <stdio.h>
#include <stdint.h>
#include <assert.h>
#include <stdbool.h>
uint32_t zero_bit(uint32_t n, uint32_t k)
{
    return n & ~(1<<k);
}
uint32_t copy_bit_i_to_k(uint32_t x, uint32_t i, uint32_t k)
{
    return zero_bit(x, k) | (((x >> i) & 1) << k);
}
static uint32_t m2bits  = 0x55555555;
static uint32_t m4bits  = 0x33333333;
static uint32_t m8bits  = 0x0f0f0f0f;
static uint32_t m16bits = 0x00ff00ff;
static uint32_t m32bits = 0x0000ffff;
uint32_t count_bits(uint32_t x)
{
    x = (x & m2bits) + ((x >> 1) & m2bits);
    x = (x & m4bits) + ((x >> 2) & m4bits);
    x = (x & m8bits) + ((x >> 4) & m8bits);
    x = (x & m16bits) + ((x >> 8) & m16bits);
    x = (x & m32bits) + ((x >> 16) & m32bits);
    return x;
}
int main()
{
    printf("%d set bit count = %d\n", 5, count_bits(5));
    printf("%d set bit count = %d\n", 15, count_bits(15));
    printf("%d set bit count = %d\n", 32, count_bits(32));
    printf("%d set bit count = %d\n", 127, count_bits(127));
}