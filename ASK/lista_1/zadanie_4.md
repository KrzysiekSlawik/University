# Zadanie 4
## Volatile
Modyfikator volatile dodany do zmiennej jest informacją dla kompilatora, że jej zawartość może się zmienić w nieznanych momentach nawet jeśli kod danej funkcji jej nie zmienia. Kompilator wyłącza optymalizacje dla zmiennej volatile. Oznacza to, że kompilator przy każdym użyciu odczytuje jej wartość bezpośrednio z pamięci zamiast z rejestru jeśli wykonuje na niej kilka operacji.  
Wyłączenie tych optymalizacji pozwala na korzystanie ze zmiennej:
* występującej pomiędzy `setjump` i `longjump` (obiekty nie oznaczone jako `volatile` mogły zmienić swoją wartość w między czasie i zapisana w rejestrze wartość będzie nieokreślona)
* współdzielonej pomiędzy wątkami (pozwala na współdzielenie zmiennej pomiędzy wątkami, UWAGA na jednoczesny dostęp!!!)
## Static
### Zmienne globalne
Pozwala na ograniczenie dostępu do danej zmiennej dla danego pliku. (nie pozwala odnosić się do tej zmiennej z pozostałych plików źródłowych)
Takie działanie może być wprost wykorzystane do wprowadzenia zmiennych prywatnych (per plik)
### Zmienne lokalne
Statyczna zmienna lokalna inicjalizowana jest jedynie przy pierwszym wywołaniu funkcji, w której się znajduje. W każdym kolejnym wywołaniu wykorzystywana jest ta sama pamięć.
```c
void Foo()
{
    static int i = 0;
    i++;
    printf("Foo() było wywołane %d\n",i);
    //...
}
```
### Procedury
Podobnie jak w przypadku zmiennych globalnych.
## Restrict wskaźniki
Słowo kluczowe restrict pozwala na poinformowanie kompilatora, że dostęp do obiektu wskazywanego przez dany wskaźnik będzie uzyskiwany jedynie poprzez dany wskaźnik lub wskaźnik powiększony o liczbę. (np `pointer + 1`)  
