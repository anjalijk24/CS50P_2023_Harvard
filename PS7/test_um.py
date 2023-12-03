#Assignment: implement, in a file called test_um.py, three or more functions that collectively test your implementation of
#count (from PS7/um.py) thoroughly, each of whose names should begin with test_.

import pytest
from um import count

def test_count():
    assert count("Hello, um, world") == 1
    assert count("Um...") == 1
    assert count("yummy") == 0


