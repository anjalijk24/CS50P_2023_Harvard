 #Assignment: implement, one or more functions that test your implementation of any functions besides main in seasons.py
 #(PS8/seasons.py) thoroughly, each of whose names should begin with test_


import pytest
import sys
from seasons import get_time_in_minutes, convert_to_words


def test_time_in_minutes():
    assert get_time_in_minutes("1999-01-01") == 13102560
    with pytest.raises(SystemExit):
        get_time_in_minutes("February 6th, 1998")

def test_convert_to_words():
    assert convert_to_words(1234) == "One thousand, two hundred thirty-four"
