import allure
import pytest

from Hotloads.test import Test
from common.parameterize_util import read_case_yaml
from common.requests_util import RequestsUtil

from Hotloads.debug_talk import DebugTalk


@allure.epic("接口自动化测试平台")
@allure.feature("证书管理模块")
class TestUserGroups:

    @allure.story("获取证书列表")
    @pytest.mark.parametrize('caseinfo', read_case_yaml('./testCases/cert_manage/get_cert_list.yaml'))
    def test_get_cert_list(self, caseinfo):
        RequestsUtil('base_api_url', DebugTalk()).standard_yaml(caseinfo)

    @allure.story("新增证书")
    @pytest.mark.parametrize('caseinfo', read_case_yaml('./testCases/cert_manage/save_cert_list.yaml'))
    def test_save_cert_list(self, caseinfo):
        RequestsUtil('base_api_url', DebugTalk()).standard_yaml(caseinfo)