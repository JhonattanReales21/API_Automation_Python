import pytest

#This tests dont have any reason in particular, only like examples for reports

def test_to_fail():
    assert False == True

@pytest.mark.skip
def test_to_skip1():
    return ""

@pytest.mark.skip
def test_to_skip12():
    return ""
