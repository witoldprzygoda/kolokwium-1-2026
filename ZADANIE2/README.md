# Zadanie 2. Przesunięcie listy (1 pkt)

Napisz funkcję `przesun(lista, k)`, która przesuwa cyklicznie elementy listy o `k` pozycji
w prawo (dla `k < 0` w lewo). Funkcja zmienia **podaną listę** (nie tworzy nowej) i ją zwraca.

```python
przesun([1, 2, 3, 4, 5], 2)    # [4, 5, 1, 2, 3]
przesun([1, 2, 3, 4, 5], -1)   # [2, 3, 4, 5, 1]
przesun([1, 2, 3, 4, 5], 7)    # [4, 5, 1, 2, 3]
przesun([], 3)                 # []

L = [1, 2, 3]
przesun(L, 1) is L             # True, a L to teraz [3, 1, 2]
```

Testy: `python -m pytest ZADANIE2`
