import ast
import random
from fractions import Fraction
from pathlib import Path

import pytest

from ZADANIE7.main import Ulamek


@pytest.mark.parametrize("l, m, licznik, mianownik", [
    (1, 2, 1, 2),
    (6, -8, -3, 4),
    (-6, 8, -3, 4),
    (-2, -4, 1, 2),
    (0, 5, 0, 1),
    (0, -3, 0, 1),
    (6, 3, 2, 1),
    (12, 18, 2, 3),
])
def test_postac_skrocona(l, m, licznik, mianownik):
    u = Ulamek(l, m)
    assert (u.licznik, u.mianownik) == (licznik, mianownik)


def test_domyslny_mianownik():
    u = Ulamek(5)
    assert (u.licznik, u.mianownik) == (5, 1)


def test_mianownik_zero():
    with pytest.raises(ZeroDivisionError):
        Ulamek(1, 0)


@pytest.mark.parametrize("l, m, napis", [(3, 4, "3/4"), (6, -8, "-3/4"), (4, 2, "2"), (0, 7, "0"), (-5, 1, "-5")])
def test_str(l, m, napis):
    assert str(Ulamek(l, m)) == napis


def test_dodawanie_i_mnozenie():
    assert str(Ulamek(1, 2) + Ulamek(1, 3)) == "5/6"
    assert str(Ulamek(2, 3) * Ulamek(3, 2)) == "1"
    assert str(Ulamek(1, 2) + Ulamek(1, 2)) == "1"
    assert str(Ulamek(-1, 2) + Ulamek(1, 3)) == "-1/6"
    assert str(Ulamek(-1, 2) * Ulamek(-4, 3)) == "2/3"


def test_nowy_obiekt_argumenty_bez_zmian():
    a, b = Ulamek(1, 2), Ulamek(1, 3)
    s, p = a + b, a * b
    assert isinstance(s, Ulamek) and isinstance(p, Ulamek)
    assert s is not a and p is not a
    assert (a.licznik, a.mianownik, b.licznik, b.mianownik) == (1, 2, 1, 3)


def test_rownosc():
    assert Ulamek(1, 2) == Ulamek(2, 4)
    assert Ulamek(-1, 2) == Ulamek(1, -2)
    assert not Ulamek(1, 2) == Ulamek(1, 3)
    assert Ulamek(1, 2) != Ulamek(2, 3)
    assert Ulamek(0, 3) == Ulamek(0, -7)


def test_losowo_jak_fractions():
    los = random.Random(2026)
    for _ in range(500):
        a, b, c, d = (los.randint(-50, 50) for _ in range(4))
        b, d = b or 1, d or 1
        x, y = Ulamek(a, b), Ulamek(c, d)
        fx, fy = Fraction(a, b), Fraction(c, d)
        assert str(x) == str(fx)
        assert str(x + y) == str(fx + fy)
        assert str(x * y) == str(fx * fy)
        assert (x == y) == (fx == fy)


def test_bez_modulu_fractions():
    zrodlo = (Path(__file__).parent.parent / "main.py").read_text(encoding="utf-8")
    for wezel in ast.walk(ast.parse(zrodlo)):
        if isinstance(wezel, ast.Import):
            assert all(a.name.split(".")[0] != "fractions" for a in wezel.names)
        if isinstance(wezel, ast.ImportFrom):
            assert (wezel.module or "").split(".")[0] != "fractions"
