import allure
import pytest
from common.parameterize_util import read_case_yaml
from common.requests_util import RequestsUtil
from Hotloads.debug_talk import DebugTalk

@allure.epic("接口自动化测试")
@allure.feature("获取统一鉴权码")
class TestApiLogin:

    @allure.story("获取统一鉴权码接口")
    @pytest.mark.parametrize('caseinfo', read_case_yaml('./testCases/api_login/test_api_login.yaml'))
    def test_api_login(self, caseinfo):
        RequestsUtil('base_api_url', DebugTalk()).md5_yaml(caseinfo)