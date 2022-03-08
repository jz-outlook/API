import allure
import pytest

from Hotloads.test import Test
from common.parameterize_util import read_case_yaml
from common.requests_util import RequestsUtil

from Hotloads.debug_talk import DebugTalk


@allure.epic("接口自动化测试平台")
@allure.feature("用户组管理模块")
class TestUserGroups:

    @allure.story("获取用户组列表")
    @pytest.mark.parametrize('caseinfo', read_case_yaml('./testCases/user_group_manage/get_group_list.yaml'))
    def test_get_group_list(self, caseinfo):
        RequestsUtil('base_api_url', DebugTalk()).standard_yaml(caseinfo)

    @allure.story("新增用户组")
    @pytest.mark.parametrize('caseinfo', read_case_yaml('./testCases/user_group_manage/save_group.yaml'))
    def test_save_group(self, caseinfo):
        RequestsUtil('base_api_url', DebugTalk()).standard_yaml(caseinfo)

    @allure.story("修改用户组")
    @pytest.mark.parametrize('caseinfo', read_case_yaml('./testCases/user_group_manage/edit_group.yaml'))
    def test_edit_group(self, caseinfo):
        RequestsUtil('base_api_url', DebugTalk()).standard_yaml(caseinfo)

    @allure.story("查询用户组")
    @pytest.mark.parametrize('caseinfo', read_case_yaml('./testCases/user_group_manage/get_group.yaml'))
    def test_get_group(self, caseinfo):
        RequestsUtil('base_api_url', DebugTalk()).standard_yaml(caseinfo)

    @allure.story("删除用户组")
    @pytest.mark.parametrize('caseinfo', read_case_yaml('./testCases/user_group_manage/delete_group.yaml'))
    def test_delete_group(self, caseinfo):
        RequestsUtil('base_api_url', DebugTalk()).standard_yaml(caseinfo)
