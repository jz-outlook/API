import time
import pytest
from common.Md5 import MD5
from common.parameterize_util import read_case_yaml
from common.requests_util import RequestsUtil
from common.yaml_util import write_extract_yaml
from debug_talk import DebugTalk


class TestApiLogin:

    # @pytest.mark.skip()
    @pytest.mark.parametrize('args_name', read_case_yaml('./testCases/api_login/test_api_login.yaml'))
    def test_get_app(self, args_name):
        url = args_name['request']['url']
        data = args_name['request']['data']

        time_str = int(round(time.time() * 1000))
        data['timestamp'] = time_str
        data['clientId'] + data['ClientSecret'] + str(time_str)
        sign = MD5(data['clientId'] + data['ClientSecret'] + str(time_str))
        data['sign'] = sign
        req = RequestsUtil('base_api_url', DebugTalk()).send_request('post', url=url, data=data)
        token = RequestsUtil('base_api_url', DebugTalk()).get_text(req.text, 'accessToken')
        write_extract_yaml({'accessToken': token})
