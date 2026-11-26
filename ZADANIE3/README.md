# Zadanie 3. Argumenty funkcji (1 pkt)

Uzupełnij **nagłówki** i treść dwóch funkcji:

- `srednia(*liczby, precyzja=2)` zwraca średnią podanych liczb zaokrągloną przez
  `round(..., precyzja)`. Parametr `precyzja` można podać tylko jako nazwany. Bez liczb: `ValueError`.
- `etykieta(nazwa, /, **cechy)` zwraca napis `nazwa(klucz=wartość, ...)`. Parametr `nazwa`
  można podać tylko pozycyjnie.

```python
srednia(1, 2, 4)                        # 2.33
srednia(1, 2, 4, precyzja=0)            # 2.0
srednia(1, 2, 4, 1)                     # 2.0  (cztery liczby)
etykieta("kot", kolor="bury", wiek=3)   # 'kot(kolor=bury, wiek=3)'
etykieta("kot")                         # 'kot()'
etykieta("pies", nazwa="Burek")         # 'pies(nazwa=Burek)'
```

Testy: `python -m pytest ZADANIE3`
