import pytest
@pytest.fixture(scope="session",autouse=True)
def setup():
    # print("Lanch browser")
    print("Login ********************")
    yield
    print("Logout from application")

