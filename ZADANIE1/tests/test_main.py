import random
import string

import pytest

from ZADANIE1.main import szyfruj


@pytest.mark.parametrize("tekst, k, wynik", [
    ("Abc, xyz!", 3, "Def, abc!"),
    ("Def", -3, "Abc"),
    ("Zebra 7", 27, "Afcsb 7"),
    ("abc", 0, "abc"),
    ("abc", 26, "abc"),
    ("abc", -26, "abc"),
    ("xyz", 1, "yza"),
    ("ABC", -1, "ZAB"),
    ("Hello, World!", 13, "Uryyb, Jbeyq!"),
    ("abc", 1000, "mno"),
    ("abc", -1000, "opq"),
    ("", 5, ""),
])
def test_szyfruj(tekst, k, wynik):
    assert szyfruj(tekst, k) == wynik


def test_inne_znaki_bez_zmian():
    tekst = "0123456789 ,.;:!?-_()[]\n\tżółć ĄĘ ść"
    assert szyfruj(tekst, 5) == tekst


def test_wielkosc_liter_zostaje():
    wynik = szyfruj(string.ascii_letters, 7)
    assert wynik[:26].islower() and wynik[26:].isupper()


def test_szyfruj_i_odszyfruj():
    los = random.Random(1)
    znaki = string.ascii_letters + string.digits + " .,żź"
    for _ in range(300):
        tekst = "".join(los.choice(znaki) for _ in range(los.randint(0, 30)))
        k = los.randint(-100, 100)
        zaszyfrowany = szyfruj(tekst, k)
        assert len(zaszyfrowany) == len(tekst)
        assert szyfruj(zaszyfrowany, -k) == tekst


def test_przesuniecie_kazdej_litery():
    for k in range(-30, 31):
        for i, litera in enumerate(string.ascii_lowercase):
            assert szyfruj(litera, k) == string.ascii_lowercase[(i + k) % 26]
            assert szyfruj(litera.upper(), k) == string.ascii_uppercase[(i + k) % 26]
