import pytest

from common.parameterize_util import read_case_yaml
from common.requests_util import RequestsUtil

from debug_talk import DebugTalk


class TestDepartment:

    @pytest.mark.parametrize('caseinfo', read_case_yaml('./testcases/department_manage/get_department_list.yaml'))
    def test_get_department_list(self, caseinfo):
        RequestsUtil('base_api_url', DebugTalk()).standard_yaml(caseinfo)

    @pytest.mark.parametrize('caseinfo', read_case_yaml('./testcases/department_manage/save_department.yaml'))
    def test_save_department(self, caseinfo):
        RequestsUtil('base_api_url', DebugTalk()).standard_yaml(caseinfo)

    @pytest.mark.parametrize('caseinfo', read_case_yaml('./testcases/department_manage/edit_department.yaml'))
    def test_edit_department(self, caseinfo):
        RequestsUtil('base_api_url', DebugTalk()).standard_yaml(caseinfo)

    @pytest.mark.parametrize('caseinfo', read_case_yaml('./testcases/department_manage/get_department.yaml'))
    def test_get_department(self, caseinfo):
        RequestsUtil('base_api_url', DebugTalk()).standard_yaml(caseinfo)

    @pytest.mark.parametrize('caseinfo', read_case_yaml('./testcases/department_manage/delete_department.yaml'))
    def test_delete_department(self, caseinfo):
        RequestsUtil('base_api_url', DebugTalk()).standard_yaml(caseinfo)