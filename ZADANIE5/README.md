# Zadanie 5. Zakresy stron (2 pkt)

Jak w oknie drukowania: napis `"1-3, 5, 7-8"` oznacza strony 1, 2, 3, 5, 7, 8.
Elementy są rozdzielone przecinkami, spacje nie mają znaczenia.

Napisz dwie funkcje:

- `rozwin(napis)` zwraca posortowaną listę numerów stron bez powtórzeń. Element, który nie jest
  liczbą ani zakresem `a-b` z `a <= b`, zgłasza `ValueError`.
- `zwin(strony)` robi odwrotnie: z listy numerów (dowolna kolejność, możliwe powtórzenia) tworzy
  napis, w którym kolejne numery są połączone w zakres.

```python
rozwin("1-3, 5, 7-8")          # [1, 2, 3, 5, 7, 8]
rozwin("10, 2-4, 3")           # [2, 3, 4, 10]
rozwin("")                     # []
rozwin("5-2")                  # ValueError
zwin([8, 1, 2, 3, 5, 7, 2])    # '1-3, 5, 7-8'
zwin([4])                      # '4'
zwin([])                       # ''
```

Testy: `python -m pytest ZADANIE5`
