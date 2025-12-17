#Parameterization with fixtures
import pytest

@pytest.fixture(params=[(3,4), [3,5]], ids=['tuple', 'list'])
def fixture01(request):
    return request.param

@pytest.fixture(params=["access", "slice", "assign", "len"])
def fixture02(request):
    return request.param

# Passing fixtue01 which passes request.param (first time tuple, second time list)
def test_fix_param01(fixture01):
    assert (type(fixture01)) in [tuple, list]

def test_fix_param02(fixture01, fixture02):
    if (fixture02 == "access"):
        assert (fixture01[0])
    elif (fixture02 == 'slice'):
        assert fixture01[::-1]
    elif (fixture02 == 'assign'):
        if isinstance(fixture01, tuple):
            pytest.xfail("tuples are immutable")
        fixture01[0] = 99
        assert True
    elif (fixture02 == 'len'):
        assert len(fixture01)