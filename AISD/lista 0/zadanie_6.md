# Zadanie 6 czytanie cudzego kodu
## Działanie algorytmu
Algorytm oblicza parzystość zbioru `A`
## Niezmiennik pętli
Parzystość zbioru `A^` == Parzystość zbioru `A`  
Zauważmy, że przed pierwszym krokiem pętli `A^` == `A`.    
Rozważmy przypadek `{a, b}` jest zbiorem parzystym, wtedy `{a-b}` też jest zbiorem parzystym i `(A^ / {a,b}) suma {a-b} mod 2` == `A^ mod 2`  
Rozważmy przypadek `{a, b}` jest zbiorem nieparzystym, wtedy `{a-b}` też jest zbiorem nieparzystym. `A^ / {a,b} mod 2` != `A mod 2`, ponieważ po usunięciu `{a,b}` ze zbioru `A^` parzystość ilości elementów nieparzystych się zmieni. Dodając nieparzysty element `{a-b}` do zbioru `A^ / {a,b}` przywracamy tę parzystość.
## uproszczony algorytm
```c
bit = 0
for a in A
    bit = bit xor a
return bit & 1
```
Parzystość liczby zapisana jest w pierwszym bicie (najmniej znaczącym).
Algorytm z zadania mówi nam, o parzystości nieparzystych liczb w zbiorze `A`. Operacja xor na dwóch liczbach parzystych zwraca liczbę parzystą, na dwóch nieparzystych zwraca liczbę parzystą, dla liczb o różnej parzystości zwróci liczbę nieparzystą. Dzięki temu możemy uzyskać wynik poprzez agregację zbioru funkcją xor. na końcu wykonujemy operację & by pozbyć się nieinteresujących nas bitów.