from assertpy import *
import pytest
from requests import *
from jsonpath import jsonpath
import time

@pytest.mark.usefixtures("BaseUrl")
class TestTypeParameter:
    #Verify the 'type' path parameter that specify where to search
    #Verify the specific fields for both types of results (anime & manga)

    # The anime search should not have any manga result
    def test_anime_type_parameter(self,BaseUrl):
        path="anime?q=Hero&limit=100"
        resp=get(BaseUrl+path)
        rJson_anime=resp.json()
        assert_that(resp.status_code).is_equal_to(200)
        assert_that(resp.headers["Connection"]).is_equal_to("keep-alive")
        assert_that(jsonpath(rJson_anime,"$.results.[:].type")).\
            does_not_contain("Manga","Light Novel","One-shot","Doujin","Manhwa","Manhua") #This are the different types of manga
        #print(jsonpath(rJson_anime,"$.results.[:].type"))

    # The manga search should not have any anime result
    def test_manga_type_parameter(self,BaseUrl):
        path = "manga?q=Hero&limit=100"
        resp = get(BaseUrl + path)
        rJson_manga = resp.json()
        assert_that(resp.status_code).is_equal_to(200)
        assert_that(resp.headers["Content-Type"]).is_equal_to("application/json")
        assert_that(jsonpath(rJson_manga, "$.results.[:].type")).\
            does_not_contain("OVA","TV","Movie","ONA","Special","Music") #This are the different types of anime
        #print(jsonpath(rJson_manga, "$.results.[:].type"))

    # The anime results have 2 specific fields/keys that manga results dont have
    def test_anime_keys(self,BaseUrl):
        path = "anime?q=Hero&limit=1"
        resp = get(BaseUrl + path)
        rJson_anime = resp.json()
        assert_that(resp.status_code).is_equal_to(200)
        assert_that(resp.headers["Content-Type"]).is_equal_to("application/json")
        assert_that(jsonpath(rJson_anime,"$.results.[:].airing")[0]).is_type_of(bool)
        assert_that(jsonpath(rJson_anime,"$.results.[:].episodes")[0]).is_type_of(int)
        time.sleep(1) #Is important to send requests minimum with 1 second of difference


    # The manga results have 3 specific fields/keys that anime results dont have
    def test_manga_keys(self,BaseUrl):
        path = "manga?q=Hero&limit=1"
        resp = get(BaseUrl + path)
        rJson_anime = resp.json()
        assert_that(resp.status_code).is_equal_to(200)
        assert_that(resp.headers["Content-Type"]).is_equal_to("application/json")
        assert_that(jsonpath(rJson_anime,"$.results.[:].publishing")[0]).is_type_of(bool)
        assert_that(jsonpath(rJson_anime,"$.results.[:].chapters")[0]).is_type_of(int)
        assert_that(jsonpath(rJson_anime,"$.results.[:].volumes")[0]).is_type_of(int)
        time.sleep(1) #Is important to send requests minimum with 1 second of difference

