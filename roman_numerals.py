"""Roemische Zahlen. Fuelle beide Funktionen so, dass test_roman_numerals.py besteht.
Aendere NUR diese Datei."""


def to_roman(n: int) -> str:
    """Ganze Zahl 1..3999 -> roemische Ziffern (Grossbuchstaben).
    ValueError bei n < 1, n > 3999 oder keiner Ganzzahl."""
    if not isinstance(n, int) or n < 1 or n > 3999:
        raise ValueError("Ungültiger Wert fuer to_roman(n)")
    values = [
        (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
        (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
        (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I"),
    ]
    result = []
    for val, sym in values:
        count = n // val
        if count:
            result.append(sym * count)
            n -= val * count
    return "".join(result)


def from_roman(s: str) -> int:
    """Gueltige (kanonische) roemische Zahl -> ganze Zahl.
    ValueError bei ungueltiger oder nicht-kanonischer Eingabe (z.B. 'IIII', 'VV')."""
    if not isinstance(s, str) or not s:
        raise ValueError("Ungültiger Wert fuer from_roman(s)")
    roman_map = {
        "M": 1000, "CM": 900, "D": 500, "CD": 400,
        "C": 100, "XC": 90, "L": 50, "XL": 40,
        "X": 10, "IX": 9, "V": 5, "IV": 4, "I": 1,
    }
    i = 0
    total = 0
    while i < len(s):
        if i + 1 < len(s) and s[i:i+2] in roman_map:
            total += roman_map[s[i:i+2]]
            i += 2
        elif s[i] in roman_map:
            total += roman_map[s[i]]
            i += 1
        else:
            raise ValueError(f"Ungültige roemische Zahl: {s}")
    # verify canonical form
    if to_roman(total) != s:
        raise ValueError(f"Nicht-kanonische roemische Zahl: {s}")
    return total
