from assertpy import *
import pytest
from requests import *
from jsonpath import jsonpath

@pytest.mark.usefixtures("BaseUrl")
class TestAdvancedParameters:
    #Verify the advanced search parameters
    #Verify that the API allows to use several advanced search parameters at once

    # If the user specify a status, the results should be only animes of that specific rated
    def test_status_parameter(self,BaseUrl):
        path = "anime?q=jujutsu&status=to_be_aired&limit=100"
        resp = get(BaseUrl + path)
        resJson = resp.json()
        assert_that(resp.status_code).is_equal_to(200)
        assert_that(resp.headers["Connection"]).is_equal_to("keep-alive")
        assert_that(resp.headers["Content-Type"]).is_equal_to("application/json")
        bool_airing=[False==air for air in jsonpath(resJson, "$.results.[:].airing")]
        assert_that(bool_airing).contains_only(True)

    # if the user specify a rated, the results should be only animes of that specific rated
    def test_rated_parameter(self,BaseUrl):
        path = "anime?q=jujutsu&rated=r17&limit=100"
        resp = get(BaseUrl + path)
        resJson = resp.json()
        assert_that(resp.status_code).is_equal_to(200)
        assert_that(resp.headers["Connection"]).is_equal_to("keep-alive")
        assert_that(resp.headers["Content-Type"]).is_equal_to("application/json")
        bool_rated=["R"==rate for rate in jsonpath(resJson, "$.results.[:].rated")]
        assert_that(bool_rated).contains_only(True)

    # The user should be able to filter the results according to a desired field
    def test_orderBy_parameter(self,BaseUrl):
        path = "anime?q=jujutsu&order_by=score&limit=100"
        resp = get(BaseUrl + path)
        resJson = resp.json()
        assert_that(resp.status_code).is_equal_to(200)
        assert_that(resp.headers["Connection"]).is_equal_to("keep-alive")
        assert_that(resp.headers["Content-Type"]).is_equal_to("application/json")
        scores=jsonpath(resJson, "$.results.[:].score")
        assert_that(scores).is_sorted(reverse=True)
        #print(scores)

    # The user should be able to filter the results using multiple filters at the same time
    def test_adv_parameters_at_the_same_time(self,BaseUrl):
        path = "anime?q=jujutsu&order_by=members&rated=pg13&status=complete&sort=asc&limit=100"
        resp = get(BaseUrl + path)
        resJson = resp.json()
        assert_that(resp.status_code).is_equal_to(200)
        assert_that(resp.headers["Connection"]).is_equal_to("keep-alive")
        assert_that(resp.headers["Content-Type"]).is_equal_to("application/json")
        members_score = jsonpath(resJson, "$.results.[:].members")
        bool_airing = [False == air for air in jsonpath(resJson, "$.results.[:].airing")]
        bool_rated = ["PG-13" == rate for rate in jsonpath(resJson, "$.results.[:].rated")]
        assert_that(members_score).is_sorted()
        assert_that(bool_airing).contains_only(True)
        assert_that(bool_rated).contains_only(True)

