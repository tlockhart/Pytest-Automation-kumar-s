import pytest
from ..my_fixtures.block_fixtures import block01, block02

def pytest_configure():
    pytest.weekdays1 = ['mon', 'tue', 'wed']
    pytest.weekdays2 = ['fri', 'sat', 'sun']
    pytest.filename = 'file1.txt'
    
@pytest.fixture(scope="module")
def setup01():
    pytest.weekdays1.append("thur")
    yield pytest.weekdays1
    print("\n After yield in setup01 fixture")
    pytest.weekdays1.pop()


@pytest.fixture(scope="session")
def setup02():
    wk2 = pytest.weekdays2.copy()
    wk2.insert(0,'thur')
    yield wk2
    print("\n Fixture setup02 closing \n")

@pytest.fixture()
def setup04(request):
    mon = getattr(request.module, "months")
    print("\n in Fixture setup04")
    print("\n Fixture Scope: " + str(request.scope))
    print("\n Calling function: " + str(request.function.__name__))
    print("\n Calling module: " + str(request.module.__name__))
    mon.append("April")
    yield mon

@pytest.fixture()
def setup05():
    def get_structure(name):
        if name == 'list':
            return [1, 2, 3]
        elif name == 'tuple':
            return (1, 3, 4)
    return get_structure