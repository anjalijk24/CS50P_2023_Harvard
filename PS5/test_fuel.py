#Assignment: In a file called fuel.py, reimplement Fuel Gauge from PS3, restructuring your code per the below, wherein:

    #convert expects a str in X/Y format as input, wherein each of X and Y is an integer, and returns that fraction as a
    #percentage rounded to the nearest int between 0 and 100, inclusive. If X and/or Y is not an integer, or if X is greater
    #than Y, then convert should raise a ValueError. If Y is 0, then convert should raise a ZeroDivisionError.
    #gauge expects an int and returns a str that is:
       #"E" if that int is less than or equal to 1,
       #"F" if that int is greater than or equal to 99,
       #and "Z%" otherwise, wherein Z is that same int.

#Then, in a file called test_fuel.py, implement two or more functions that collectively test your implementations of
#convert and gauge thoroughly, each of whose names should begin with test_


import pytest
from fuel import convert, gauge


def test_zero_division():
    with pytest.raises(ZeroDivisionError):
         convert("3/0")


def test_value_error():
    with pytest.raises(ValueError):
        convert("cat/4")
    with pytest.raises(ValueError):
        convert("3/2")


def test_convert():
    assert convert("3/4") == 75


def test_gauge():
    assert gauge(1)  == "E"
    assert gauge(70) == "70%"
    assert gauge(99) == "F"

