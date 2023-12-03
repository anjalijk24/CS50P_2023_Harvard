#Assignment: implement, in a file called test_numb3rs.py, two or more functions that collectively test your implementation of
#validate (in numb3rs.py of PS7) thoroughly, each of whose names should begin with test_.


import pytest
from numb3rs import validate

def test_validate_digits():
    assert validate("255.255.255.255") == True
    assert validate("1.300.270.500")   == False


def test_validate_other_character():
     assert validate("cat") == False





