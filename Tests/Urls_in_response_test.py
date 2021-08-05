import re
import allure
from assertpy import *
import pytest
from requests import *
from jsonpath import jsonpath

# Verify the url pattern for the fields link and image-link
# in every search result

@allure.severity(allure.severity_level.MINOR)
@pytest.mark.usefixtures("BaseUrl")
class TestUrlFields:

    @allure.title("Link and image-link for Anime responses")
    @allure.description("The Anime responses must have 2 fields with a url pattern, this fields are link and "
                        "image-link. Moreover, the image-link must have a .jpg in the url")
    @allure.feature("Anime search")
    @allure.story("As a customer i want to be able to go to the Anime´s info website from the search result")
    def test_anime_Urls(self,BaseUrl):
        path = "anime?q=Sword&limit=100"
        resp = get(BaseUrl + path)
        rJson_anime = resp.json()
        assert_that(resp.status_code).is_equal_to(200)
        assert_that(resp.headers["Connection"]).is_equal_to("keep-alive")
        assert_that(resp.headers["Content-Type"]).is_equal_to("application/json")
        bool_url_anime=[bool(re.search(r"^https://myanimelist.net/anime",link)) for link in
                        jsonpath(rJson_anime, "$.results.[:].url")]
        bool_imageUrl_anime=[bool(re.search(r"^https://cdn.myanimelist.net/images/anime",jpglink)) for jpglink in
                             jsonpath(rJson_anime, "$.results.[:].image_url")]
        bool_image=[bool(re.search(r".jpg",jpglink)) for jpglink in jsonpath(rJson_anime, "$.results.[:].image_url")]
        assert_that(bool_url_anime).contains_only(True)
        assert_that(bool_imageUrl_anime).contains_only(True)
        assert_that(bool_image).contains_only(True)

    @allure.title("Link and image-link for Anime responses")
    @allure.description("The Manga responses must have 2 fields with a url pattern, this fields are link and "
                        "image-link. Moreover, the image-link must have a .jpg in the url")
    @allure.feature("Manga search")
    @allure.story("As a customer i want to be able to go to the Manga´s info website from the search result")
    def test_manga_Urls(self,BaseUrl):
        path = "manga?q=Sword&limit=100"
        resp = get(BaseUrl + path)
        rJson_manga = resp.json()
        assert_that(resp.status_code).is_equal_to(200)
        assert_that(resp.headers["Connection"]).is_equal_to("keep-alive")
        assert_that(resp.headers["Content-Type"]).is_equal_to("application/json")
        bool_url_manga = [bool(re.search(r"^https://myanimelist.net/manga", link)) for link in
                          jsonpath(rJson_manga, "$.results.[:].url")]
        bool_imageUrl_manga = [bool(re.search(r"^https://cdn.myanimelist.net/images/manga", jpglink)) for jpglink in
                               jsonpath(rJson_manga, "$.results.[:].image_url")]
        bool_image = [bool(re.search(r".jpg", jpglink)) for jpglink in jsonpath(rJson_manga, "$.results.[:].image_url")]
        assert_that(bool_url_manga).contains_only(True)
        assert_that(bool_imageUrl_manga).contains_only(True)
        assert_that(bool_image).contains_only(True)