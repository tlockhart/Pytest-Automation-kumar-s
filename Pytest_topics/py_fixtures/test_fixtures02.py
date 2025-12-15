import pytest
import os

# pytest.weekdays1 = ['mon', 'tue', 'wed']
# pytest.weekdays2 = ['fri', 'sat', 'sun']
# pytest.filename = 'file1.txt'

@pytest.fixture(scope="module")
def setup01():
    pytest.pytest.weekdays1.append('thur')
    yield pytest.pytest.weekdays1
    print ("\n After yield in setup01 fixture")
    pytest.pytest.weekdays1.pop()

@pytest.fixture()
def setup02():
    pytest.weekdays2.insert(0,'thur')
    yield pytest.weekdays2

@pytest.fixture()
def setup03():
    f = open(pytest.filename, 'w')
    f.write("Pytest is good")
    f.close()
    f = open(pytest.filename, 'r+')
    yield f
    f.close()
    os.remove(pytest.filename)


def test_extendList(setup01):
    setup01.extend(pytest.weekdays2)
    assert setup01 == ['mon', 'tue', 'wed', 'thur', 'fri', 'sat', 'sun']

def test_len(setup01, setup02):
    assert len(pytest.weekdays1 + setup02) == len(setup01 + pytest.weekdays2)

def test_filetest(setup03):
    assert (setup03.readline()) == 'Pytest is good'