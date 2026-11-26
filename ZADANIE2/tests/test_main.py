import random

import pytest

from ZADANIE2.main import przesun


@pytest.mark.parametrize("k, wynik", [
    (0, [1, 2, 3, 4, 5]),
    (1, [5, 1, 2, 3, 4]),
    (2, [4, 5, 1, 2, 3]),
    (5, [1, 2, 3, 4, 5]),
    (7, [4, 5, 1, 2, 3]),
    (-1, [2, 3, 4, 5, 1]),
    (-2, [3, 4, 5, 1, 2]),
    (-6, [2, 3, 4, 5, 1]),
    (123, [3, 4, 5, 1, 2]),
])
def test_przesun(k, wynik):
    assert przesun([1, 2, 3, 4, 5], k) == wynik


def test_zmienia_podana_liste_i_ja_zwraca():
    L = [1, 2, 3]
    druga_nazwa = L
    assert przesun(L, 1) is L
    assert L == [3, 1, 2]
    assert druga_nazwa == [3, 1, 2]


def test_lista_pusta_i_jednoelementowa():
    pusta = []
    assert przesun(pusta, 3) is pusta and pusta == []
    jedna = ["x"]
    assert przesun(jedna, -4) is jedna and jedna == ["x"]


def test_rozne_elementy():
    a = [1]
    L = ["a", None, a, 2.5]
    assert przesun(L, 1) == [2.5, "a", None, a]
    assert L[3] is a


def test_tam_i_z_powrotem():
    los = random.Random(2026)
    for _ in range(200):
        L = [los.randint(0, 9) for _ in range(los.randint(0, 12))]
        kopia = L[:]
        k = los.randint(-30, 30)
        assert przesun(L, k) is L
        assert sorted(L) == sorted(kopia)
        przesun(L, -k)
        assert L == kopia


def test_k_razy_o_jeden():
    los = random.Random(7)
    for _ in range(50):
        L = [los.randint(0, 99) for _ in range(los.randint(1, 10))]
        k = los.randint(0, 15)
        po_jednym = L[:]
        for _ in range(k):
            ostatni = po_jednym[-1]
            assert przesun(po_jednym, 1)[0] == ostatni
        assert przesun(L, k) == po_jednym
