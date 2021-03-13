#include <stdio.h>
#include <stdint.h>
#include <limits.h>
int main()
{
    uint32_t x = 0;
    uint32_t y = 5;
    //swap
    printf("x = %d\n",x);
    printf("y = %d\n",y);

    printf("SWAP\n");
    x = x ^ y; //zapisz pod x maskę różnic pomiędzy 'x' a 'y'
    y = x ^ y; //wyłuskaj oryginalne 'x' na podstawie oryginalnego 'y' i maski różnic
    x = x ^ y; //wyłuskaj oryginalne 'y' na podstawie oryginalnego 'x' i maski różnic
    printf("x = %d\n",x);
    printf("y = %d\n",y);
    /* możemy o tym myśleć w perspektywie 1 bitu, bo wykonywane działania są lokalne dla par bitów x[i] i y[i]
     * niech x, y oznacza bit
     * rozpatrzmy trzy sytuacje:
     *  x == y = 0
     *      maska = 0
     *      y = origY ^ maska
     *      y = 0
     *      x = origX ^ maska
     *      x = 0
     *  x == y = 1
     *      maska = 0
     *      y = origY ^ maska
     *      y = 1
     *      x = origX ^ maska
     *      x = 1
     *  x = 0, y = 1
     *      maska = 1
     *      y = origY ^ maska
     *      y = 0
     *      x = origX ^ maska
     *      x = 1    
     */
    return 0;
}