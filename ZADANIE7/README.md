# Zadanie 7. Klasa Ulamek (2 pkt)

Napisz klasę `Ulamek` (bez modułu `fractions`):

- `Ulamek(licznik, mianownik=1)` zapisuje ułamek w atrybutach `licznik` i `mianownik`
  w postaci skróconej (`math.gcd`), z dodatnim mianownikiem. Mianownik 0: `ZeroDivisionError`.
- `str()` daje `"licznik/mianownik"`, a przy mianowniku 1 sam licznik.
- `+` i `*` dwóch ułamków dają nowy `Ulamek`.
- `==` porównuje dwa ułamki.

```python
u = Ulamek(6, -8)
u.licznik, u.mianownik              # (-3, 4)
str(u)                              # '-3/4'
str(Ulamek(1, 2) + Ulamek(1, 3))    # '5/6'
str(Ulamek(2, 3) * Ulamek(3, 2))    # '1'
Ulamek(1, 2) == Ulamek(2, 4)        # True
```

Testy: `python -m pytest ZADANIE7`
