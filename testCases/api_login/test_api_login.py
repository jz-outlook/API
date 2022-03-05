import pytest
from common.parameterize_util import read_case_yaml
from common.requests_util import RequestsUtil
from Hotloads.debug_talk import DebugTalk


class TestApiLogin:
    @pytest.mark.parametrize('caseinfo', read_case_yaml('./testCases/api_login/test_api_login.yaml'))
    def test_get_department_list(self, caseinfo):
        RequestsUtil('base_api_url', DebugTalk()).md5_yaml(caseinfo)