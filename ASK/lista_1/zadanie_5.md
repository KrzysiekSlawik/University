# Zadanie 5
## `s += b[j+1] + b[--j];`
```c
t1 := j + 1;
t1 := t1 * 4;  //ponieważ b to tablica elementów długości 4 bajtów
t2 := b + t1;  //pozyskanie odpowiedniego adresu
l := *t2;      //wyłuskanie wartości
j  := j - 1;   //dekrementacja
t3 := 4 * j;   //analogicznie
t4 := b + t3;  //analogicznie
r := *t4;      //analogicznie
t5 := l + r;   //dodanie wyłuskanych z tablic wartości
s  := s + t5;  //inkrementacja o wyliczoną wartość
```
## `a[i++] -= *b * (c[j*2] + 1);`
```c
l := *b;      //1:1 kod c

t1 := j * 2;  //1:1 kod c
t2 := t1 * 4; //ponieważ to tablica elementów długości 4 bajtów
t3 := c + t1; //1:1 kod c
t4 := *t3;    //wyłuskanie wartości z tablicy
r := t4+1;    
t5 := l * r;  
t6 := i * 4;  //i++ zwraca wartość i a następnie inkrementuje
i := i + 1;
t7 := a + t6; 
*t7 := t5;    //przypisanie wartości 
```