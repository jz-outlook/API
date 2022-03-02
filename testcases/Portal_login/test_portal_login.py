import random
import pytest
import requests
from common.requests_util import RequestsUtil
from common.yaml_util import write_extract_yaml, read_extract_yaml, read_case_yaml, get_object_path
from debug_talk import DebugTalk


class TestPortalApi:

    # @pytest.mark.skip(reason='不执行登录portal用例')
    @pytest.mark.run(order=1)  # 表示该用例第一个执行
    @pytest.mark.parametrize('caseinfo', read_case_yaml('./testcases/Portal_login/test_portal_login.yaml'))
    def test_get_token(self, caseinfo):
        RequestsUtil('base_portal_url', DebugTalk()).standard_yaml(caseinfo)

