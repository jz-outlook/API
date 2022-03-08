import allure
import pytest
from common.parameterize_util import read_case_yaml
from common.requests_util import RequestsUtil
from Hotloads.debug_talk import DebugTalk

@allure.epic("码尚教育接口自动化测试平台")
@allure.feature("商品管理模块")
class TestApiLogin:

    @allure.story("获取统一鉴权码接口")
    @pytest.mark.parametrize('caseinfo', read_case_yaml('./testCases/api_login/test_api_login.yaml'))
    def test_get_department_list(self, caseinfo):
        RequestsUtil('base_api_url', DebugTalk()).md5_yaml(caseinfo)