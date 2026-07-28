"""Roemische Zahlen. Fuelle beide Funktionen so, dass test_roman_numerals.py besteht.
Aendere NUR diese Datei."""


def to_roman(n: int) -> str:
    """Ganze Zahl 1..3999 -> roemische Ziffern (Grossbuchstaben).
    ValueError bei n < 1, n > 3999 oder keiner Ganzzahl."""
    if not isinstance(n, int) or n < 1 or n > 3999:
        raise ValueError("n must be an integer between 1 and 3999")
    
    values = [
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
        (1, "I")
    ]
    
    result = []
    for value, numeral in values:
        while n >= value:
            result.append(numeral)
            n -= value
    return "".join(result)


def from_roman(s: str) -> int:
    """Gueltige (kanonische) roemische Zahl -> ganze Zahl.
    ValueError bei ungueltiger oder nicht-kanonischer Eingabe (z.B. 'IIII', 'VV')."""
    if not isinstance(s, str):
        raise ValueError("Input must be a string")
    if not s:
        raise ValueError("Input cannot be empty")
    
    # Valid characters
    valid_chars = set("IVXLCDM")
    for char in s:
        if char not in valid_chars:
            raise ValueError(f"Invalid Roman numeral character: {char}")
    
    # Map characters to values
    roman_map = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    
    # Validate the Roman numeral is canonical
    # Rules:
    # - I can be placed before V and X
    # - X can be placed before L and C
    # - C can be placed before D and M
    # - V, L, D cannot be repeated
    # - I, X, C can be repeated up to 3 times
    # - Subtractive combinations are only allowed for specific pairs
    
    # Check for invalid repetitions
    for i in range(len(s) - 1):
        current = roman_map[s[i]]
        next_val = roman_map[s[i + 1]]
        if current < next_val:
            # This is a subtractive pair, check if valid
            if not ((current == 1 and next_val in (5, 10)) or
                    (current == 10 and next_val in (50, 100)) or
                    (current == 100 and next_val in (500, 1000))):
                raise ValueError(f"Invalid subtractive pair: {s[i]}{s[i+1]}")
        elif current == next_val:
            # Check repetition limit
            if s[i] in "VLD" or s[i:i+4] in ["VV", "LL", "DD"]:
                raise ValueError(f"Invalid repetition: {s[i]}")
            if s[i] in "IXC" and s[i:i+4] in ["IIII", "XXXX", "CCCC"]:
                raise ValueError(f"Invalid repetition: {s[i]}")
    
    # Calculate the value
    total = 0
    prev_value = 0
    for char in reversed(s):
        value = roman_map[char]
        if value < prev_value:
            total -= value
        else:
            total += value
            prev_value = value
    
    return total