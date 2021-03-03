# Zadanie 7 droga na drzewo
## Algorytm
```c
Tree: tablica list dzieci
Tin: tablica czasów
Tout: tablica czasów
R: tablica wyników
isRoot: tablica inicjalizowana na true
t = 0
def DFS(v)
    t++
    Tin[v] = t
    for child in Tree[v]
        DFS(child)
    t++
    Tout[v] = t
for e in E
    Tree[e.p].add(e.a)
    isRoot[e.a] = false
root = isRoot.find_index(value==true)
DFS(root)
for r in R[i], v in V[i], u in U[i]
    r = Tin[v] < Tin[u] && Tout[v] > Tout[u]
return R
```
## Intuicja
Zadana struktura reprezentująca drzewo jest skrajnie nie wygodna do obliczeń, które musimy wykonać, dlatego dokonujemy konwersji w czasie O(n-1) do postaci tablicy list, gdzie kluczem jest rodzic a wartości w liście to dzieci. Pozwala nam to na wykonywanie kroków DFS w czasie stałym. (zamiast w czasie O(n))

DFS używamy do otagowania wierzchołków czasem wejścia i wyjścia. Zauważmy, że dla poddrzewa takiego, że korzeń to `vi`, a `ui` jest jednym z węzłów tego poddrzewa, to `vi` leży na ścieżce do korzenia z `ui`.  
Zauważmy, że łatwo jest zidentyfikować, czy wierzchołek `u` należy do poddrzewa o korzeniu w `v`. DFS wchodził do danego poddrzewa o czasie `Tin[v]` i wychodził o czasie `Tout[v]`. Czas wejścia do wierzchołka `u` musi być większy niż `Tin[v]`, ponieważ `u` jest głębszym elementem. Dodatkowo czas wyjścia z `u` musi być mniejszy niż `Tout[v]`, bo tak długo jak nie opuścimy `u`, to nie opuścimy `v`.

Jeżeli `u` nie należy do poddrzewa z korzeniem w `v`, to `v` nie leży na ścieżce z `u` do korzenia.   
Istnieją dwa przypadki:  
* poddrzewo z korzeniem `u` zawiera poddrzewo z korzeniem `v` => relacja jest `u` z `v` jest odwrotne niż porządana i widoczne jest to w warunku Tin[v] < Tin[u] && Tout[v] > Tout[u] (wartość tego wyrażenia w tym przypadku to false, bo czas wejścia do `u` jest mniejszy niż czas wejścia do `v`)
* poddrzewo z korzeniem `u` jest rozłączne z poddrzewem z korzeniem `v`. Przedziały czasowe `Tin[v] Tout[v]` i `Tin[u] Tout[u]` również są rozłączne.  

