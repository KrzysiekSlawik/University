# Zadanie 3 Bubble sort i inne
| Bubble sort | Select sort | Insert sort | Kryteria |
|--|--|--|--|
| O(n^2) | O(n^2) | O(n^2) | zł. czasowa |
| Tak | Tak | Tak | zamiana w miejscu |
| Tak | Nie | Tak | czy stabilny |
| najlepsza gdy posortowane | najlepsza gdy posortowane | O(n^2) | złożoność gdy kryterium jednorodne |
| O(n^2) | O(n^2) | O(n) | best-case złożoność |  |  |  |             |

```c
bubbleSort(arr)    
    int i, j;  
    for i = 0; i < arr.len()-1; i++  
    	for j = 0; j < arr.len()-i-1; j++  
    		if arr[j] > arr[j+1]  
    			swap(arr[j], arr[j+1])
```
* Dla prawie uporządkowanych danych *insert* będzie lepszy niż *bubble* i *select*. Bo select sort zawsze przeszukuje cala tablice w szukaniu minimum(w przypadku **PRAWIE** posortowanej tablicy - nadmiarowa praca). Bubble sort jest prymitywny i wiemy ze zawsze wykona O(n^2) iteracji. Insert natomiast będzie brał kolejne elementy, i juz po 1 porównaniu będzie wiedział że nie musi dalej szukać i element jest posortowany.
* *insert* dla niektórych danych jest rzędu O(n^2), a dla niektórych O(n) (zależy od początkowego uporządkowania tablicy).
* *bubble* jest stabilny, bo zawsze zamieniamy elementy gdy są mniejsze/większe (ostra nierówność).
* wielkość rekordów:
    * Jeśli rekordy są duże to operacja przestawienia elementów jest kosztowna. *Select* wykonuje O(n) przestawień, a *insert* O(n^2), a *bubble* O(n^2).

* **stabilność selection sorta**:
![](https://i.imgur.com/zUwvUvr.png)