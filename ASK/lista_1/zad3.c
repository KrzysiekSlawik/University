#include <stdio.h>
#include <stdint.h>
#include <assert.h>
struct A
{
    int8_t a; //1
              //7 padding
    void *b;  //8
    int8_t c; //1
              //1 padding
    int16_t d;//2
              //4 padding
              //==
              //20
}A;
struct Ap
{
    void *b;  //8
    int8_t a; //1
    int8_t c; //1
    int16_t d;//2
              //4 padding
              //==
              //16
}Ap;

struct B
{
    uint16_t a;//2
               //6 padding
    double b;  //8
    void *c;   //8
               //==
               //24
}B;

int main()
{
    printf("%d\n", sizeof(A));
    printf("%d\n", sizeof(Ap));
    printf("%d\n", sizeof(B));

    return 0;
}