
import pytest

from common.parameterize_util import read_case_yaml
from common.requests_util import RequestsUtil
from debug_talk import DebugTalk


class TestPortalApi:

    @pytest.mark.skip(reason='不执行登录portal用例')
    @pytest.mark.run(order=1)  # 表示该用例第一个执行
    @pytest.mark.parametrize('caseinfo', read_case_yaml('./testcases/Portal_login/test_portal_login.yaml'))
    def test_get_token(self, caseinfo):
        RequestsUtil('base_portal_url', DebugTalk()).standard_yaml(caseinfo)
