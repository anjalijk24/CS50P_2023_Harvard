# Assignment: In the file twttr.py, from PS2, restructure the code, wherein shorten expects a str as input and
# returns that same str but with all vowels (A, E, I, O, and U) omitted, whether inputted in uppercase or
#lowercase. Implement one or more functions that collectively test your implementation of shorten thoroughly,
# each of whose names should begin with test_ so that you can execute your tests with: pytest test_twttr.py


import pytest
from twttr import shorten


# Check if all vowels in lowercase result in an empty string
def test_lowercase_vowel():
    assert shorten("aeiou") == ""


# Check if all vowels in uppercase result in an empty string
def test_uppercase_vowel():
    assert shorten("AEIOU") == ""


# Check a string with no vowels, should remain the same
def test_novowel_string():
    assert shorten("rhythm") == "rhythm"


# Check a string with vowels, should be shortened with shorten()
def test_string_vowel():
    assert shorten("apple") == "ppl"
    assert shorten("pine")  == "pn"


# Check that special characters are not shortened
def test_special_characters():
    assert shorten("!@#$%^&*") == "!@#$%^&*"


#if the input is a number
def test_number():
    assert shorten("1") == "1"

