from assertpy import *
import pytest
from requests import *
from jsonpath import jsonpath
import time
import allure

#Verify the 'type' path parameter that specify what kind of observation to search
#Verify the specific fields for both types of results (anime & manga)

@pytest.mark.usefixtures("BaseUrl")
class TestTypePathParameter:

    @allure.title("Anime responses with none Manga observations")
    @allure.description("The Anime responses must not have any Manga result. We can validate this"
                        " by comparing several Manga types with the 'type' field of each result for an Anime search ")
    @allure.feature("Anime search")
    @allure.story("As a customer i want to be able to search only Anime results")
    def test_anime_type_parameter(self,BaseUrl):
        path="anime?q=Hero&limit=100"
        resp=get(BaseUrl+path)
        rJson_anime=resp.json()
        assert_that(resp.status_code).is_equal_to(200)
        assert_that(resp.headers["Connection"]).is_equal_to("keep-alive")
        assert_that(jsonpath(rJson_anime,"$.results.[:].type")).\
            does_not_contain("Manga","Light Novel","One-shot","Doujin","Manhwa","Manhua") #This are the different types of manga

    @allure.title("Data type for specific fields in Anime responses")
    @allure.description("The Anime results should have (2) specific fields called airing and episodes. This fields "
                        "have a specific data type, boolean and integer respectively. ")
    @allure.feature("Anime search")
    @allure.story("As a customer i want to be able to search only Anime results")
    def test_anime_keys(self,BaseUrl):
        path = "anime?q=Hero&limit=1"
        resp = get(BaseUrl + path)
        rJson_anime = resp.json()
        assert_that(resp.status_code).is_equal_to(200)
        assert_that(resp.headers["Content-Type"]).is_equal_to("application/json")
        assert_that(jsonpath(rJson_anime,"$.results.[:].airing")[0]).is_type_of(bool)
        assert_that(jsonpath(rJson_anime,"$.results.[:].episodes")[0]).is_type_of(int)
        time.sleep(0.5) #Is important to send requests minimum with 0.5 seconds of difference


    @allure.title("Manga responses with none Anime observations")
    @allure.description("The Manga responses should not have any Anime result. We can validate this"
                        " by comparing several Anime types with the 'type' field of each result for an Manga search ")
    @allure.feature("Manga search")
    @allure.story("As a customer i want to be able to search only Manga results")
    def test_manga_type_parameter(self,BaseUrl):
        path = "manga?q=Hero&limit=100"
        resp = get(BaseUrl + path)
        rJson_manga = resp.json()
        assert_that(resp.status_code).is_equal_to(200)
        assert_that(resp.headers["Content-Type"]).is_equal_to("application/json")
        assert_that(jsonpath(rJson_manga, "$.results.[:].type")).\
            does_not_contain("OVA","TV","Movie","ONA","Special","Music") #This are the different types of anime

    @allure.title("Data type for specific fields in Manga responses")
    @allure.description("The Manga results should have (3) specific fields called publishing, chapters "
                        "and volumes. This fields have specific data types, boolean, integer and integer respectively.")
    @allure.feature("Manga search")
    @allure.story("As a customer i want to be able to search only Manga results")
    def test_manga_keys(self,BaseUrl):
        path = "manga?q=Hero&limit=1"
        resp = get(BaseUrl + path)
        rJson_anime = resp.json()
        assert_that(resp.status_code).is_equal_to(200)
        assert_that(resp.headers["Content-Type"]).is_equal_to("application/json")
        assert_that(jsonpath(rJson_anime,"$.results.[:].publishing")[0]).is_type_of(bool)
        assert_that(jsonpath(rJson_anime,"$.results.[:].chapters")[0]).is_type_of(int)
        assert_that(jsonpath(rJson_anime,"$.results.[:].volumes")[0]).is_type_of(int)
        time.sleep(0.5) #Is important to send requests minimum with 1 second of difference

