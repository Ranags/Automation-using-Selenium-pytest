import pytest


def testLogin():
    print("Login ")


def testsearch():
    print("hello")
    print("This is search")

@pytest.mark.sanity
def testcalculation():
    assert 2+2 == 4
