# Zadanie 6. Macierze (2 pkt)

Macierz to lista wierszy równej długości, np. `[[1, 2, 3], [4, 5, 6]]` (2 wiersze, 3 kolumny).
Napisz trzy funkcje. Każda zwraca **nową** macierz i nie zmienia argumentów.

- `jednostkowa(n)` - macierz n x n z jedynkami na przekątnej i zerami poza nią.
- `transponuj(m)` - wiersze zamienione z kolumnami.
- `pomnoz(a, b)` - iloczyn macierzy: element `[i][j]` to suma `a[i][k] * b[k][j]` po wszystkich `k`.
  Gdy liczba kolumn `a` jest inna niż liczba wierszy `b`: `ValueError`.

```python
jednostkowa(2)                          # [[1, 0], [0, 1]]
transponuj([[1, 2, 3], [4, 5, 6]])      # [[1, 4], [2, 5], [3, 6]]
pomnoz([[1, 2], [3, 4]], [[5], [6]])    # [[17], [39]]
pomnoz([[1, 2]], [[1, 2]])              # ValueError
```

Testy: `python -m pytest ZADANIE6`
