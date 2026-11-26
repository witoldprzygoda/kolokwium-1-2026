import random

import pytest

from ZADANIE5.main import rozwin, zwin


@pytest.mark.parametrize("napis, strony", [
    ("1-3, 5, 7-8", [1, 2, 3, 5, 7, 8]),
    ("10, 2-4, 3", [2, 3, 4, 10]),
    ("", []),
    ("7", [7]),
    ("4-4", [4]),
    ("1-3,5,7-8", [1, 2, 3, 5, 7, 8]),
    (" 1 - 3 ,  5 ", [1, 2, 3, 5]),
    ("5, 5, 5", [5]),
    ("1-5, 3-7", [1, 2, 3, 4, 5, 6, 7]),
    ("98-102", [98, 99, 100, 101, 102]),
])
def test_rozwin(napis, strony):
    assert rozwin(napis) == strony


@pytest.mark.parametrize("napis", ["5-2", "a", "1-", "-", "1-2-3", "1,,2", "2.5", "1, x-3"])
def test_rozwin_bledy(napis):
    with pytest.raises(ValueError):
        rozwin(napis)


@pytest.mark.parametrize("strony, napis", [
    ([8, 1, 2, 3, 5, 7, 2], "1-3, 5, 7-8"),
    ([4], "4"),
    ([], ""),
    ([1, 2], "1-2"),
    ([1, 3], "1, 3"),
    ([5, 4, 3, 2, 1], "1-5"),
    ([10, 9, 1, 11, 3, 2, 20], "1-3, 9-11, 20"),
    ([7, 7, 7], "7"),
    ([99, 100, 101, 103], "99-101, 103"),
])
def test_zwin(strony, napis):
    assert zwin(strony) == napis


def test_zwin_nie_zmienia_listy():
    strony = [3, 1, 2, 2]
    zwin(strony)
    assert strony == [3, 1, 2, 2]


def test_tam_i_z_powrotem():
    los = random.Random(2026)
    for _ in range(300):
        strony = [los.randint(1, 40) for _ in range(los.randint(0, 25))]
        napis = zwin(strony)
        assert rozwin(napis) == sorted(set(strony))
        assert zwin(rozwin(napis)) == napis
