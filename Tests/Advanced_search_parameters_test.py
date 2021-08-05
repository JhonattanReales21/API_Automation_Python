import allure
from assertpy import *
import pytest
from requests import *
from jsonpath import jsonpath

# Verify the advanced search parameters
# Verify that the API allows to use several advanced search parameters at once

@pytest.mark.usefixtures("BaseUrl")
class TestAdvancedParameters:

    @allure.title("Verifying status filter")
    @allure.description("If the user specify a status, the response should have only results with that specific "
                        "status. This is verified by looking each status in airing field for Anime searches")
    @allure.feature("Advanced search parameters")
    @allure.story("As a costumer i want to filter and order the results by specific parameters")
    def test_status_parameter(self,BaseUrl):
        path = "anime?q=jujutsu&status=to_be_aired&limit=100"
        resp = get(BaseUrl + path)
        resJson = resp.json()
        assert_that(resp.status_code).is_equal_to(200)
        assert_that(resp.headers["Connection"]).is_equal_to("keep-alive")
        assert_that(resp.headers["Content-Type"]).is_equal_to("application/json")
        bool_airing=[False==air for air in jsonpath(resJson, "$.results.[:].airing")]
        assert_that(bool_airing).contains_only(True)

    @allure.title("Verifying rated filter")
    @allure.description("If the user specify a rated, the response should have only results with that specific rated. "
                        "This is verified by looking each rate in rated field for Anime searches")
    @allure.feature("Advanced search parameters")
    @allure.story("As a costumer i want to filter and order the results by specific parameters")
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
    @allure.title("Verifying order the results by score")
    @allure.description("If the user specify the results to be order by the scores, the response should be order by "
                        "this. This is check by looking each score and verifying that they respect the specified order")
    @allure.feature("Advanced search parameters")
    @allure.story("As a costumer i want to filter and order the results by specific parameters")
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
    @allure.title("Verifying several filters at the same time")
    @allure.description("If the user specify several filters, orders and sorts, the results should take in consideration all this ones. "
                        "This is check by looking and verifying that each condition/parameter is accomplishing")
    @allure.feature("Advanced search parameters")
    @allure.story("As a costumer i want to filter and order the results by specific parameters")
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

