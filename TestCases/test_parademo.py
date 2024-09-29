import pytest


# @pytest.fixture(params=["a","b"])
#
# def demo_fixture(request):
#     print(request.param)
# def testlogin(demo_fixture):
#     print("Login siccessfull")

@pytest.mark.parametrize("a,b,final",[(2,6,8),(1,2,31)])
def test_addno(a,b,final):
    assert a+b==final





# def testlogoff():
#     print("Log out from the system")
#
#
# def testcalculation():
#     assert 2+2 == 4
