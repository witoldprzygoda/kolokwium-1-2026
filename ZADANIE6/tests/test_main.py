import copy
import random

import pytest

from ZADANIE6.main import jednostkowa, pomnoz, transponuj


def losowa(w, k, los):
    return [[los.randint(-9, 9) for _ in range(k)] for _ in range(w)]


# ------------------------------------------------------------------ jednostkowa

def test_jednostkowa():
    assert jednostkowa(1) == [[1]]
    assert jednostkowa(2) == [[1, 0], [0, 1]]
    assert jednostkowa(3) == [[1, 0, 0], [0, 1, 0], [0, 0, 1]]


def test_jednostkowa_wiersze_niezalezne():
    m = jednostkowa(3)
    m[0][1] = 5
    assert m == [[1, 5, 0], [0, 1, 0], [0, 0, 1]]


# ------------------------------------------------------------------ transponuj

@pytest.mark.parametrize("m, wynik", [
    ([[1, 2, 3], [4, 5, 6]], [[1, 4], [2, 5], [3, 6]]),
    ([[1]], [[1]]),
    ([[1, 2, 3]], [[1], [2], [3]]),
    ([[1], [2], [3]], [[1, 2, 3]]),
    ([[1, 2], [3, 4]], [[1, 3], [2, 4]]),
])
def test_transponuj(m, wynik):
    assert transponuj(m) == wynik


def test_transponuj_dwa_razy():
    los = random.Random(3)
    for _ in range(50):
        m = losowa(los.randint(1, 5), los.randint(1, 5), los)
        assert transponuj(transponuj(m)) == m


def test_transponuj_wynik_to_listy():
    wynik = transponuj([[1, 2], [3, 4]])
    assert all(type(w) is list for w in wynik)


# ------------------------------------------------------------------ pomnoz

@pytest.mark.parametrize("a, b, wynik", [
    ([[1, 2], [3, 4]], [[5], [6]], [[17], [39]]),
    ([[1, 2], [3, 4]], [[5, 6], [7, 8]], [[19, 22], [43, 50]]),
    ([[1, 2, 3]], [[4], [5], [6]], [[32]]),
    ([[4], [5], [6]], [[1, 2, 3]], [[4, 8, 12], [5, 10, 15], [6, 12, 18]]),
    ([[2]], [[3]], [[6]]),
])
def test_pomnoz(a, b, wynik):
    assert pomnoz(a, b) == wynik


def test_pomnoz_niezgodne_wymiary():
    with pytest.raises(ValueError):
        pomnoz([[1, 2]], [[1, 2]])
    with pytest.raises(ValueError):
        pomnoz([[1, 2], [3, 4]], [[1], [2], [3]])


def test_pomnoz_przez_jednostkowa():
    los = random.Random(5)
    for _ in range(50):
        w, k = los.randint(1, 5), los.randint(1, 5)
        m = losowa(w, k, los)
        assert pomnoz(m, jednostkowa(k)) == m
        assert pomnoz(jednostkowa(w), m) == m


def test_transpozycja_iloczynu():
    los = random.Random(11)
    for _ in range(50):
        w, k, s = los.randint(1, 4), los.randint(1, 4), los.randint(1, 4)
        a, b = losowa(w, k, los), losowa(k, s, los)
        iloczyn = pomnoz(a, b)
        assert len(iloczyn) == w and all(len(wiersz) == s for wiersz in iloczyn)
        assert transponuj(pomnoz(a, b)) == pomnoz(transponuj(b), transponuj(a))


def test_argumenty_bez_zmian():
    a, b = [[1, 2], [3, 4]], [[5, 6], [7, 8]]
    a0, b0 = copy.deepcopy(a), copy.deepcopy(b)
    pomnoz(a, b)
    transponuj(a)
    assert a == a0 and b == b0
    wynik = transponuj(a)
    wynik[0][0] = 99
    assert a == a0
