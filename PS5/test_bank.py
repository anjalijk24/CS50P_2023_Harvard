#Assignment: In the file called bank.py, from PS1, restructure your code, wherein value expects a str as input
#and returns 0 if that str starts with “hello”, 20 if that str starts with an “h” (but not “hello”) or 100
#otherwise, treating the str case-insensitively. You can assume that the string passed to the value function
#will not contain any leading spaces. Only main should call print.

#implement three or more functions that collectively test your implementation of value thoroughly, each of
#whose names should begin with test_


import pytest
from bank import value


def test_zero_dollar():
    assert value("hello") == 0
    assert value("Hello, world") == 0

def test_twenty_dollar():
    assert value("hi") == 20
    assert value("How are you") == 20

def test_hundred_dollar():
    assert value("what") == 100
    assert value("wow, you are back") == 100





