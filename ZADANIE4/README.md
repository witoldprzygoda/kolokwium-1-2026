# Zadanie 4. Dekorator liczący wywołania (1 pkt)

Napisz dekorator `licz_wywolania`. Udekorowana funkcja działa jak przedtem (te same argumenty
i wynik), a jej atrybut `wywolania` podaje, ile razy ją wywołano (na początku 0). Nazwa funkcji
(`__name__`) ma się nie zmienić: użyj `functools.wraps`.

```python
@licz_wywolania
def kwadrat(x):
    return x * x

kwadrat(3)           # 9
kwadrat(x=4)         # 16
kwadrat.wywolania    # 2
kwadrat.__name__     # 'kwadrat'
```

Testy: `python -m pytest ZADANIE4`
