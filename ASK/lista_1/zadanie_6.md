# Zadanie 6
## `vs->d = us[1].a + us[j].c;`
przyjmujemy 32 bitowe wskaźniki
```c
struct A {
    int8_t a; //1+3
    void *b;  //4
    int8_t c; //1+1
    int16_t d;//2
};
```
```c
t1 := j * 4; 
t2 := us + t1; //us[j]
t3 := t2 + 8;  //t2 + 8
t4 := *t3;     //us[j].c

t5 := us + 4;  //us[1]
t6 := *t5;     //us[1].a;

t7 := t4+t6;   

t8 := vs + 10;
*t8 := t7;
```