#include <stdio.h>
#include <stdint.h>
#include <limits.h>
int main()
{
    int32_t x;
    int32_t y;
    printf("(x > 0) || (x - 1 < 0)\n");
    x = INT32_MIN;
    printf("x=%d\n", x);
    printf("x-1=%d\n\n", x-1);

    printf("(x & 7) != 7 || (x << 29 < 0)\n");
    x = -1;// 0b1...111111
    printf("x=%d\n", x);
    printf("x & 7=%d\n", x & 7);
    printf("x << 29=%d\n\n", x << 29);

    printf("(x * x) >= 0\n");
    x = (1 << 30)+1;
    printf("x=%d\n", x);
    printf("x*x=%d\n\n", x*x);

    printf("x < 0 || -x <= 0\n");
    printf("-x na pewno zmieści się w zakresie liczb ujemnych,\n");
    printf("więc operacja *-1 dobrze zachowuje się dla liczb dodatnich\n\n");

    printf("x > 0 || -x >= 0\n");
    x = INT32_MIN;
    printf("x=%d\n", x);
    printf("-x=%d\n\n", -x);

    printf("(x | -x) >> 31 == -1\n");
    x = 0;
    printf("x=%d\n", x);
    printf("(x | -x) >> 31 =%d\n\n", (x | -x) >> 31);

    printf("x + y == (uint32_t)y + (uint32_t)x\n");
    x = INT32_MAX;
    y = 1;
    printf("x=%d\n", x);
    printf("y=%d\n", y);
    printf("x+y=%d\n", x+y);
    printf("zawsze prawdziwe, bo rzutowanie w tym przypadku jest zaraźliwe,\n");
    printf("a kolejność wykonania operacji dowolna\n");
    printf("x + y == (uint32_t)y + (uint32_t)x=%s\n\n",
        (x + y == (uint32_t)y + (uint32_t)x)?"true":"false");

    printf("x * ~y + (uint32_t)y * (uint32_t)x == -x\n");
    x = 5;
    y = 5;
    printf("x=%d\n", x);
    printf("y=%d\n", y);
    printf("~y=%d\n", ~y);
    printf("x*~y=%d\n", x*~y);
    printf("x+y=%d\n", x+y);
    printf("(x * ~y + (uint32_t)y * (uint32_t)x == -x)=%s\n\n",
        (x * ~y + (uint32_t)y * (uint32_t)x == -x)?"true":"false");
    /* ~y = -y-1
     * x * (-y-1) = -x -xy
     * y * x = xy
     * -x -xy + xy = -x
     */

    return 0;
}