import re
import allure
from assertpy import *
import pytest
from requests import *
from jsonpath import jsonpath

@pytest.mark.usefixtures("BaseUrl")
class TestUrlFields:
    # There are 2 important fields in each response that contains url info
    # This fields are ulr and image_url, which are important for any app

    # All the anime results must have valid links and valid image links with .jpg format
    @allure.feature("Anime_search")
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

    # All the manga results must have valid links and valid image links with .jpg format
    @allure.feature("Manga_search")
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