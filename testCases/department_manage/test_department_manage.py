import allure
import pytest

from common.parameterize_util import read_case_yaml
from common.requests_util import RequestsUtil

from Hotloads.debug_talk import DebugTalk

@allure.epic("接口自动化测试")
@allure.feature("部门管理模块")
class TestDepartment:

    @allure.story("获取部门列表")
    @pytest.mark.parametrize('caseinfo', read_case_yaml('./testCases/department_manage/get_department_list.yaml'))
    def test_get_department_list(self, caseinfo):
        RequestsUtil('base_api_url', DebugTalk()).standard_yaml(caseinfo)

    @allure.story("保存部门")
    @pytest.mark.parametrize('caseinfo', read_case_yaml('./testCases/department_manage/save_department.yaml'))
    def test_save_department(self, caseinfo):
        RequestsUtil('base_api_url', DebugTalk()).standard_yaml(caseinfo)

    @allure.story("修改部门")
    @pytest.mark.parametrize('caseinfo', read_case_yaml('./testCases/department_manage/edit_department.yaml'))
    def test_edit_department(self, caseinfo):
        RequestsUtil('base_api_url', DebugTalk()).standard_yaml(caseinfo)

    @allure.story("查询部门")
    @pytest.mark.parametrize('caseinfo', read_case_yaml('./testCases/department_manage/get_department.yaml'))
    def test_get_department(self, caseinfo):
        RequestsUtil('base_api_url', DebugTalk()).standard_yaml(caseinfo)

    @allure.story("删除部门")
    @pytest.mark.parametrize('caseinfo', read_case_yaml('./testCases/department_manage/delete_department.yaml'))
    def test_delete_department(self, caseinfo):
        RequestsUtil('base_api_url', DebugTalk()).standard_yaml(caseinfo)