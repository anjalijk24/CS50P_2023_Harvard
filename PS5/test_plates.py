#Assignment: In the file called plates.py, from PS2, restructure your code per the below, wherein is_valid
#still expects a str as input and returns True if that str meets all requirements and False if it does not,
#but main is only called if the value of __name__ is "__main__".

#implement four or more functions that collectively test your implementation of is_valid thoroughly, each of
#whose names should begin with test_.


import pytest
from plates import is_valid


def test_length():
    assert is_valid("H")       == False
    assert is_valid("PAP4565") == False


def test_special_character():
    assert is_valid("CS20.!") == False


def test_alphabets():
    assert is_valid("APPLES") == True


def test_numerals():
    assert is_valid("122")  == False


def test_alphanumeric():
    assert is_valid("PA02")  == False
    assert is_valid("PI31F") == False


