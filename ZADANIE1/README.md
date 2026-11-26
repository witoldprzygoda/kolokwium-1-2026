# Zadanie 1. Szyfr Cezara (1 pkt)

Napisz funkcję `szyfruj(tekst, k)`, która przesuwa każdą literę `A-Z` i `a-z` o `k` pozycji
w alfabecie, cyklicznie (po `z` jest `a`). Wielkość liter zostaje, inne znaki się nie zmieniają.
`k` może być ujemne i większe od 26.

```python
szyfruj("Abc, xyz!", 3)    # 'Def, abc!'
szyfruj("Def", -3)         # 'Abc'
szyfruj("Zebra 7", 27)     # 'Afcsb 7'
```

Testy: `python -m pytest ZADANIE1`
