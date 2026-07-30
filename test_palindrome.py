import pytest
from palindrome import is_palindrome


def test_empty():
    assert is_palindrome("") is True


def test_simple_palindrome():
    assert is_palindrome("aba") is True
    assert is_palindrome("abba") is True


def test_not_palindrome():
    assert is_palindrome("abc") is False


def test_ignore_case():
    assert is_palindrome("Aba") is True
    assert is_palindrome("AbBa") is True


def test_ignore_non_alphanumeric():
    assert is_palindrome("A man, a plan, a canal: Panama") is True
    assert is_palindrome("race a car") is False


def test_only_non_alphanumeric():
    assert is_palindrome("!!!") is True
    assert is_palindrome("  ") is True


def test_ignore_digits():
    assert is_palindrome("1a2") is True
    assert is_palindrome("1ab2") is False
    assert is_palindrome("123") is True
