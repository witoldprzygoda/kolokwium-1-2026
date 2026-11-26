from ZADANIE4.main import kwadrat, licz_wywolania


def test_kwadrat():
    przed = kwadrat.wywolania
    assert kwadrat(3) == 9
    assert kwadrat(x=4) == 16
    assert kwadrat.wywolania == przed + 2
    assert kwadrat.__name__ == "kwadrat"


def test_na_poczatku_zero():
    @licz_wywolania
    def f():
        pass

    assert f.wywolania == 0


def test_argumenty_i_wynik():
    @licz_wywolania
    def zbierz(*args, **kwargs):
        return args, kwargs

    assert zbierz(1, "a", x=2) == ((1, "a"), {"x": 2})
    assert zbierz() == ((), {})
    assert zbierz.wywolania == 2


def test_wynik_none():
    @licz_wywolania
    def nic():
        return None

    assert nic() is None
    assert nic.wywolania == 1


def test_osobne_liczniki():
    @licz_wywolania
    def f(x):
        return x + 1

    @licz_wywolania
    def g(x):
        return x * 2

    for i in range(5):
        f(i)
    assert g(3) == 6
    assert (f.wywolania, g.wywolania) == (5, 1)


def test_nazwa_zachowana():
    def moja_funkcja(a, b=1):
        return a - b

    opakowana = licz_wywolania(moja_funkcja)
    assert opakowana.__name__ == "moja_funkcja"
    assert opakowana(5, b=2) == 3
    assert opakowana.wywolania == 1
