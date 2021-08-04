from assertpy import *
import pytest
from requests import *
from jsonpath import jsonpath

@pytest.mark.usefixtures("BaseUrl")
class TestTypeParameter:

    def test_anime_type_parameter(self,BaseUrl):
        path="anime?q=Hero&limit=30"
        resp=get(BaseUrl+path)
        rJson=resp.json()
        assert_that(resp.status_code).is_equal_to(200)
        assert_that(jsonpath(rJson,"$.results.[:].type")).does_not_contain(["manga","novel","oneshot","doujin","manhwa","manhua"])
        print(jsonpath(rJson,"$.results.[:].type"))

