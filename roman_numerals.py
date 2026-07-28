"""Roemische Zahlen. Fuelle beide Funktionen so, dass test_roman_numerals.py besteht.
Aendere NUR diese Datei."""


def to_roman(n: int) -> str:
    """Ganze Zahl 1..3999 -> roemische Ziffern (Grossbuchstaben).
    ValueError bei n < 1, n > 3999 oder keiner Ganzzahl."""
    if not isinstance(n, int):
        raise ValueError("Input must be an integer")
    if n < 1 or n > 3999:
        raise ValueError("Number must be between 1 and 3999")
    
    roman_numerals = [
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
    
    result = ""
    for value, numeral in roman_numerals:
        while n >= value:
            result += numeral
            n -= value
    return result


def from_roman(s: str) -> int:
    """Gueltige (kanonische) roemische Zahl -> ganze Zahl.
    ValueError bei ungueltiger oder nicht-kanonischer Eingabe (z.B. 'IIII', 'VV')."""
    if not isinstance(s, str):
        raise ValueError("Input must be a string")
    
    s = s.strip().upper()
    if not s:
        raise ValueError("Empty string")
    
    # Valid characters
    valid_chars = set("MDCLXVI")
    if not all(c in valid_chars for c in s):
        raise ValueError("Invalid characters in Roman numeral")
    
    # Mapping of Roman numerals to values
    roman_map = {
        'M': 1000,
        'D': 500,
        'C': 100,
        'L': 50,
        'X': 10,
        'V': 5,
        'I': 1
    }
    
    # Check for invalid repetitions
    # Rules: I, X, C, M can repeat up to 3 times
    #        V, L, D cannot repeat
    for char, max_repeat in [('I', 3), ('X', 3), ('C', 3), ('M', 3), ('V', 1), ('L', 1), ('D', 1)]:
        if char * (max_repeat + 1) in s:
            raise ValueError(f"Invalid repetition of '{char}'")
    
    # Check for valid subtractive pairs only
    # Valid subtractive pairs: IV, IX, XL, XC, CD, CM
    valid_subtractive = {
        'IV': 4,
        'IX': 9,
        'XL': 40,
        'XC': 90,
        'CD': 400,
        'CM': 900
    }
    
    # Check for invalid subtractive patterns
    invalid_patterns = ['IL', 'IC', 'ID', 'IM', 'XD', 'XM', 'VX', 'VL', 'VC', 'VD', 'VM', 
                       'LC', 'LD', 'LM', 'DM']
    for pattern in invalid_patterns:
        if pattern in s:
            raise ValueError(f"Invalid subtractive pattern '{pattern}'")
    
    # Convert to integer
    total = 0
    i = 0
    while i < len(s):
        # Check for subtractive pair
        if i + 1 < len(s):
            pair = s[i:i+2]
            if pair in valid_subtractive:
                total += valid_subtractive[pair]
                i += 2
                continue
        
        # Single character
        total += roman_map[s[i]]
        i += 1
    
    # Additional validation: check that the number is canonical
    # by converting back and comparing
    canonical = to_roman(total)
    if canonical != s:
        raise ValueError("Non-canonical Roman numeral")
    
    return total