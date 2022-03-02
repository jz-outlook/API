import pytest
from common.requests_util import RequestsUtil
from common.yaml_util import write_extract_yaml, read_extract_yaml, read_case_yaml, get_object_path
from debug_talk import DebugTalk


class TestDepartment:


    @pytest.mark.parametrize('caseinfo', read_case_yaml('./testcases/department_manage/get_department.yaml'))
    def test_get_token(self, caseinfo):
        RequestsUtil('base_api_url', DebugTalk()).standard_yaml(caseinfo)