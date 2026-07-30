"""Palindrome pruefen. Fuelle is_palindrome so, dass test_palindrome.py besteht.
Aendere NUR diese Datei."""


def is_palindrome(s: str) -> bool:
    """Prueft, ob s ein Palindrom ist (ignoriert Nicht-Buchstaben und Gross-/Kleinschreibung).
    Leere Zeichenkette oder nur Nicht-Buchstaben gelten als Palindrom."""
    cleaned = "".join(char.lower() for char in s if char.isalpha())
    return cleaned == cleaned[::-1]
