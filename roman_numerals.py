"""Roemische Zahlen. Fuelle beide Funktionen so, dass test_roman_numerals.py besteht.
Aendere NUR diese Datei."""

_VALUES = [
    (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
    (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
    (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I"),
]

_LETTERS = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}


def to_roman(n: int) -> str:
    """Ganze Zahl 1..3999 -> roemische Ziffern (Grossbuchstaben).
    ValueError bei n < 1, n > 3999 oder keiner Ganzzahl."""
    if isinstance(n, bool) or not isinstance(n, int):
        raise ValueError(f"keine Ganzzahl: {n!r}")
    if not 1 <= n <= 3999:
        raise ValueError(f"ausserhalb 1..3999: {n!r}")
    out = []
    for value, numeral in _VALUES:
        while n >= value:
            out.append(numeral)
            n -= value
    return "".join(out)


def from_roman(s: str) -> int:
    """Gueltige (kanonische) roemische Zahl -> ganze Zahl.
    ValueError bei ungueltiger oder nicht-kanonischer Eingabe (z.B. 'IIII', 'VV')."""
    if not isinstance(s, str) or not s:
        raise ValueError(f"leere oder keine Zeichenkette: {s!r}")
    total = 0
    prev = 0
    for ch in reversed(s):
        try:
            v = _LETTERS[ch]
        except KeyError:
            raise ValueError(f"ungueltiges Zeichen: {ch!r}") from None
        if v < prev:
            total -= v
        else:
            total += v
            prev = v
    # Kanonizitaets-Check: nur die kanonische Form darf zurueckkommen
    # (verwirft z.B. 'IIII', 'VV', 'IL'; to_roman wirft ValueError bei > 3999).
    if to_roman(total) != s:
        raise ValueError(f"nicht-kanonische roemische Zahl: {s!r}")
    return total
