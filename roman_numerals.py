"""Roemische Zahlen. Fuelle beide Funktionen so, dass test_roman_numerals.py besteht.
Aendere NUR diese Datei."""


_VALUES = [
    (1000, "M"),
    (900, "CM"),
    (500, "D"),
    (400, "CD"),
    (100, "C"),
    (90, "XC"),
    (50, "L"),
    (40, "XL"),
    (10, "X"),
    (9, "IX"),
    (5, "V"),
    (4, "IV"),
    (1, "I"),
]

_SYMBOLS = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}


def to_roman(n: int) -> str:
    """Ganze Zahl 1..3999 -> roemische Ziffern (Grossbuchstaben).
    ValueError bei n < 1, n > 3999 oder keiner Ganzzahl."""
    if not isinstance(n, int) or isinstance(n, bool):
        raise ValueError("n must be an integer")
    if n < 1 or n > 3999:
        raise ValueError("n out of range")

    result = []
    remaining = n
    for value, symbol in _VALUES:
        count, remaining = divmod(remaining, value)
        if count:
            result.append(symbol * count)
        if remaining == 0:
            break
    return "".join(result)


def from_roman(s: str) -> int:
    """Gueltige (kanonische) roemische Zahl -> ganze Zahl.
    ValueError bei ungueltiger oder nicht-kanonischer Eingabe (z.B. 'IIII', 'VV')."""
    if not isinstance(s, str) or not s:
        raise ValueError("s must be a non-empty string")
    if any(ch not in _SYMBOLS for ch in s):
        raise ValueError("invalid roman numeral")

    total = 0
    i = 0
    while i < len(s):
        value = _SYMBOLS[s[i]]
        if i + 1 < len(s) and _SYMBOLS[s[i + 1]] > value:
            total += _SYMBOLS[s[i + 1]] - value
            i += 2
        else:
            total += value
            i += 1

    try:
        if to_roman(total) != s:
            raise ValueError("non-canonical roman numeral")
    except ValueError as exc:
        raise ValueError("invalid roman numeral") from exc

    return total
