# zadanie 4 mnożenie po rosyjsku
## algorytm
### Wejście:
`a` liczba całkowita  
`b` liczba całkowita

### Wyjście:
`a * b`

### Kroki:
```c
a^ = a
b^ = b
c^ = 0
while b^ > 0 do
    if b^ is odd
        c^ += a^
    a^ *= 2
    b^ /= 2
return c^
```
### Niezmienniki
`a^ * b^ + c^` daje wynik działania `a * b`

## Dowód poprawności
Poprawność algorytmu wynika wprost z niezmiennika pętli.  
Pokażmy, że niezmiennik jest prawdziwy.
Zauważmy, że na początku `a^ = a && b^ = b && c = 0`, czyli `a^ * b^ + c^` daje wynik działania `a * b`  
Rozważmy dwa przypadki:  
#### `b^` parzyste  
Załóżmy, że `a^ * b^ + c^` daje wynik działania `a * b`.
```
(a^ * 2) * (b^ / 2) + c^ == 
a^ * b^ + c^
```
#### `b^` nieparzyste
Załóżmy, że `a^ * b^ + c^` daje wynik działania `a * b`.
```c
(b^ - 1) / 2 == b^ / 2 //gdzie / oznacza dzielenie całkowite
(a^ * 2) * ((b^ - 1) / 2) + (c^ + a^) ==
a^ * (b^ - 1) + c^ + a^ ==
a^ * b^ - a^ + c^ + a^ ==
a^ * b^ + c^
```
Pokazaliśmy, że niezmiennik jest prawdziwy, więc `a^ * b^ + c^ == a * b` jest prawdziwe w każdym kroku pętli.  
Pokażmy, że algorytm kończy działanie.
Algorytm kończy działanie, gdy `b^ <= 0`.
Wartość `b` maleje w każdym kroku conajmniej dwukrotnie, (czyli nie mniej niż o 1).

## jednorodne kryterium kosztów
### czas
Algorytm zwraca wynik, gdy `b^ == 0`, do takiego stanu dochodzi po `log(b)` krokach (wynika wprost z dowodu). Innymi słowy złożoność czasowa to logarytm z długości zapisu `b` w systemie dwójkowym.
### pamięć
Algorytm wykorzystuje 3 zmienne całkowitoliczbowe.
## logarytmiczne kryterium kosztów
### czas
Warto zauważyć, że algorytm wykonuje proste operacje. (sprowadzalne do pojedyńczych operacji binnarnych)
Przypomnijmy operacje wykonywane w pętli:
```c
while b^ > 0 do  //porównanie z zerem log(b^)
    if b^ is odd //sprawdzenie 1 bitu
        c^ += a^ //dodawanie log(c^) + log(a^)
    a^ *= 2      //przesunięcie bitowe log(a^)
    b^ /= 2      //przesunięcie bitowe log(b^)
```
W uproszczeniu daje to złożoność `log(b) * (log(b) * 2 + log(a) * 2 + log(c))`
Zwracając uwagę na zmienną wartość `a^`, `b^` i `c^`:  
`log(b)` kroków   
długość zapisu `a^` zwiększa się o `1` w każdym kroku  
`log(a)` w pierwszym kroku `log(a)+log(b)` w ostatnim  
razem `log(b) * 2 * log(a*b)`  

długość zapisu `b^` zmniejsza się o `1` w każdym kroku  
`log(b)` w pierwszym kroku,  `log(b)+log(b)` w ostatnim  
razem `3 * log(b)^2`

Sumując wszystko `3 * log(b)^2 + 2 * log(a*b) * log(b)
### pamięć
`a^` nie przekracza `log(a)+log(b)`  
`b^` nie przekracza `2*log(b)`  
`c^` nie przekracza `log(a)+log(b)`

