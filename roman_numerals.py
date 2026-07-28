"""Roemische Zahlen. Fuelle beide Funktionen so, dass test_roman_numerals.py besteht.
Aendere NUR diese Datei."""


_VALUES = [
    (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
    (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
    (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I"),
]


def to_roman(n: int) -> str:
    """Ganze Zahl 1..3999 -> roemische Ziffern (Grossbuchstaben).
    ValueError bei n < 1, n > 3999 oder keiner Ganzzahl."""
    if not isinstance(n, int) or isinstance(n, bool):
        raise ValueError("n must be an integer")
    if n < 1 or n > 3999:
        raise ValueError("n must be in range 1..3999")
    result = []
    for value, symbol in _VALUES:
        while n >= value:
            result.append(symbol)
            n -= value
    return "".join(result)


def from_roman(s: str) -> int:
    """Gueltige (kanonische) roemische Zahl -> ganze Zahl.
    ValueError bei ungueltiger oder nicht-kanonischer Eingabe (z.B. 'IIII', 'VV')."""
    if not isinstance(s, str) or s == "":
        raise ValueError("s must be a non-empty string")
    # Validate characters
    valid_chars = set("MDCLXVI")
    if any(c not in valid_chars for c in s):
        raise ValueError("invalid characters")
    # Convert by summing symbol values, then verify canonical form via roundtrip
    _map = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}
    total = 0
    prev = 0
    for c in reversed(s):
        cur = _map[c]
        if cur < prev:
            total -= cur
        else:
            total += cur
        prev = cur
    # Canonical check: round-trip must reproduce the input exactly
    if to_roman(total) != s:
        raise ValueError("non-canonical Roman numeral")
    return total
