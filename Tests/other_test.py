import pytest
import allure

#This tests dont have any reason in particular, only like examples for reports
@allure.feature("Others")
def test_to_fail():
    assert False == True

@allure.feature("Others")
def test_to_fail():
    assert True == False

@allure.feature("Others")
@pytest.mark.skip
def test_to_skip1():
    return ""

@allure.feature("Others")
@pytest.mark.skip
def test_to_skip2():
    return ""

@allure.feature("Others")
@pytest.mark.skip
def test_to_skip3():
    return ""