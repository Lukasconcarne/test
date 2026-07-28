"""Roemische Zahlen. Fuelle beide Funktionen so, dass test_roman_numerals.py besteht.
Aendere NUR diese Datei."""


def to_roman(n: int) -> str:
    """Ganze Zahl 1..3999 -> roemische Ziffern (Grossbuchstaben).
    ValueError bei n < 1, n > 3999 oder keiner Ganzzahl."""
    if not isinstance(n, int) or n < 1 or n > 3999:
        raise ValueError(f"Ungueltige Eingabe: {n}")
    
    # Mapping of values to Roman numerals (subtractive notation)
    val_map = [
        (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
        (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
        (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
    ]
    
    result = []
    for value, numeral in val_map:
        while n >= value:
            result.append(numeral)
            n -= value
    
    return "".join(result)


def from_roman(s: str) -> int:
    """Gueltige (kanonische) roemische Zahl -> ganze Zahl.
    ValueError bei ungueltiger oder nicht-kanonischer Eingabe (z.B. 'IIII', 'VV')."""
    if not s or not isinstance(s, str):
        raise ValueError("Leere oder ungueltige Eingabe")
    
    # Single character values
    single_vals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    
    # Valid subtractive pairs (canonical)
    subtractive_pairs = {'IV', 'IX', 'XL', 'XC', 'CD', 'CM'}
    
    # Check for invalid characters
    for char in s:
        if char not in single_vals:
            raise ValueError(f"Ungueltiges Zeichen: {char}")
    
    # Parse the Roman numeral
    total = 0
    i = 0
    while i < len(s):
        # Look for subtractive pair first
        if i < len(s) - 1:
            pair = s[i:i+2]
            if pair in subtractive_pairs:
                total += single_vals[s[i+1]] - single_vals[s[i]]
                i += 2
                continue
        
        # Single numeral
        total += single_vals[s[i]]
        i += 1
    
    # Validate canonical form by round-trip check
    if to_roman(total) != s:
        raise ValueError("Nicht-kanonische roemische Zahl")
    
    return total
