import pytest
import


@pytest.mark.regression
def testLogin():
    print("Login ")


def testsearch():
    print("hello")
    print("This is search")

@pytest.mark.xfail
def testcalculation():
    assert 2+2==4


def testtexcollection():
    assert 2 + 2 == 4


@pytest.mark.skip
def testslider():
    print("")
