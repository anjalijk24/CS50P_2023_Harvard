#Assignment: implement, four or more functions that collectively test your implementation of Jar (PS8/jar.py) thoroughly, each of
#whose names should begin with test_

import pytest
from jar import Jar


def test_init():
    with pytest.raises(ValueError):
        Jar(capacity = -1)

    with pytest.raises(ValueError):
        Jar(capacity = 1.2)

    with pytest.raises(ValueError):
        Jar(capacity = "cat")


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    jar.deposit(2)
    assert str(jar) == "🍪🍪"


def test_withdraw():
    jar = Jar()
    jar.deposit(2)
    jar.withdraw(1)
    assert str(jar) == "🍪"

