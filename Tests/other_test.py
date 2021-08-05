import pytest
import allure

#This tests dont have any reason in particular, only like examples for reports

@allure.severity(allure.severity_level.MINOR)
@allure.feature("Others")
def test_to_fail():
    assert False == True

@allure.severity(allure.severity_level.BLOCKER)
@allure.feature("Others")
def test_to_fail_2():
    assert False == True


@allure.severity(allure.severity_level.MINOR)
@allure.feature("Others")
@pytest.mark.skip
def test_to_skip2():
    return ""

@allure.severity(allure.severity_level.TRIVIAL)
@allure.feature("Others")
@pytest.mark.skip
def test_to_skip3():
    return ""

@allure.severity(allure.severity_level.MINOR)
@allure.feature("Others")
def test_to_pass_1():
    assert True == True

@allure.severity(allure.severity_level.TRIVIAL)
@allure.feature("Others")
def test_to_pass_2():
    assert True == True