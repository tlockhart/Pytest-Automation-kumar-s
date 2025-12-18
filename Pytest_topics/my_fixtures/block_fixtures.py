import pytest


@pytest.fixture(scope="module")
def block01():
    pytest.weekdays1.append("thur")
    yield pytest.weekdays1
    print("\n After yield in setup01 fixture")
    pytest.weekdays1.pop()


@pytest.fixture()
def block02():
    # pytest.weekdays2.insert(0, "thur")
    yield pytest.weekdays2
