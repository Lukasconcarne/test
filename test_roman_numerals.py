import pytest
from roman_numerals import to_roman, from_roman


@pytest.mark.parametrize("n,s", [
    (1, "I"), (4, "IV"), (9, "IX"), (14, "XIV"), (40, "XL"),
    (90, "XC"), (400, "CD"), (900, "CM"), (2024, "MMXXIV"), (3999, "MMMCMXCIX"),
])
def test_to_roman(n, s):
    assert to_roman(n) == s


@pytest.mark.parametrize("n,s", [
    (1, "I"), (4, "IV"), (58, "LVIII"), (1994, "MCMXCIV"), (3999, "MMMCMXCIX"),
])
def test_from_roman(n, s):
    assert from_roman(s) == n


def test_roundtrip():
    for n in range(1, 4000):
        assert from_roman(to_roman(n)) == n


@pytest.mark.parametrize("bad", [0, -5, 4000, 10000])
def test_to_roman_invalid(bad):
    with pytest.raises(ValueError):
        to_roman(bad)


@pytest.mark.parametrize("bad", ["", "IIII", "VV", "abc", "IL"])
def test_from_roman_invalid(bad):
    with pytest.raises(ValueError):
        from_roman(bad)
