#include <stdio.h>
#include <stdint.h>
#include <assert.h>
#include <stdbool.h>

uint32_t zero_bit(uint32_t n, uint32_t k)
{
    return n & ~(1<<k);
}

uint32_t set_bit(uint32_t n, uint32_t k)
{
    return n | (1<<k);
}

uint32_t negate_bit(uint32_t n, uint32_t k)
{
    return n ^ (1<<k);
}

uint32_t mult_pow2(uint32_t n, uint32_t k)
{
    return n<<k;
}

uint32_t div_pow2_floor(uint32_t n, uint32_t k)
{
    return n>>k;
}

uint32_t div_pow2_ceiling(uint32_t n, uint32_t k)
{
    return (n>>k) | (n & (1<<k)>>k);
}

uint32_t mod_pow2(uint32_t n, uint32_t k)
{
    return n & ~((~0)<<k);
}

bool is_pow2(uint32_t n)
{
    return (n != 0) && ((n & (n - 1)) == 0);
}
int main()
{
    assert(zero_bit(17,4) == 1);
    assert(zero_bit(1,4) == 1);
    assert(set_bit(3,2) == 7);
    assert(set_bit(7,2) == 7);
    assert(negate_bit(4,2) == 0);
    assert(negate_bit(0,2) == 4);
    assert(mult_pow2(4,0) == 4);
    assert(mult_pow2(31,2) == 31*4);
    assert(mult_pow2(4,0) == 4);
    assert(mult_pow2(31,2) == 31*4);
    assert(div_pow2_floor(1,2) == 0);
    assert(div_pow2_floor(17,2) == 4);
    assert(div_pow2_floor(16,2) == 4);
    assert(mod_pow2(0,4) == 0);
    assert(mod_pow2(31,3) == 7);
    assert(mod_pow2(31,6) == 31);
    assert(div_pow2_ceiling(1,1) == 1);
    assert(div_pow2_ceiling(5,1) == 3);
    assert(div_pow2_ceiling(0,1) == 0);
    assert(div_pow2_ceiling(4,1) == 2);
    assert(is_pow2(0)==false);
    assert(is_pow2(3)==false);
    assert(is_pow2(5)==false);
    assert(is_pow2(6)==false);
    assert(is_pow2(1)==true);
    assert(is_pow2(2)==true);
    assert(is_pow2(4)==true);
    assert(is_pow2(8)==true);
    assert(is_pow2(16)==true);
    return 0;
}