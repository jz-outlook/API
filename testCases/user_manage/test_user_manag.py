import allure
import pytest

from Hotloads.test import Test
from common.parameterize_util import read_case_yaml
from common.requests_util import RequestsUtil

from Hotloads.debug_talk import DebugTalk


@allure.epic("接口自动化测试平台")
@allure.feature("用户管理模块")
class TestDepartment:

    @allure.story("获取用户列表")
    @pytest.mark.parametrize('caseinfo', read_case_yaml('./testCases/user_manage/get_user_list.yaml'))
    def test_get_user_list(self, caseinfo):
        RequestsUtil('base_api_url', DebugTalk()).standard_yaml(caseinfo)

    # @pytest.mark.parametrize('caseinfo', read_case_yaml('./testCases/user_manage/save_user.yaml'))
    # def test_save_user_list(self, caseinfo):
    #     RequestsUtil('base_api_url', Test()).standard_yaml(caseinfo)