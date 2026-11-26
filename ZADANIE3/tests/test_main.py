import inspect

import pytest

from ZADANIE3.main import etykieta, srednia

P = inspect.Parameter


def test_srednia():
    assert srednia(1, 2, 4) == pytest.approx(2.33)
    assert srednia(1, 2, 4, precyzja=0) == 2.0
    assert srednia(1, 2, 4, 1) == 2.0
    assert srednia(5) == 5
    assert srednia(1, 2, precyzja=1) == 1.5
    assert srednia(-1, 2.5, 0.25, precyzja=3) == pytest.approx(0.583)
    assert srednia(*[2, 4, 9]) == 5


def test_srednia_bez_liczb():
    with pytest.raises(ValueError):
        srednia()
    with pytest.raises(ValueError):
        srednia(precyzja=3)


def test_srednia_naglowek():
    parametry = list(inspect.signature(srednia).parameters.values())
    assert [p.kind for p in parametry] == [P.VAR_POSITIONAL, P.KEYWORD_ONLY]
    assert parametry[1].name == "precyzja" and parametry[1].default == 2


def test_etykieta():
    assert etykieta("kot", kolor="bury", wiek=3) == "kot(kolor=bury, wiek=3)"
    assert etykieta("kot") == "kot()"
    assert etykieta("pies", nazwa="Burek") == "pies(nazwa=Burek)"
    assert etykieta("auto", rok=2020, marka="Fiat") == "auto(rok=2020, marka=Fiat)"
    assert etykieta("x", **{"a": [1, 2], "b": None}) == "x(a=[1, 2], b=None)"


def test_etykieta_naglowek():
    parametry = list(inspect.signature(etykieta).parameters.values())
    assert [p.kind for p in parametry] == [P.POSITIONAL_ONLY, P.VAR_KEYWORD]
    assert parametry[0].name == "nazwa"
