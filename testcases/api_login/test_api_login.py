import time
import pytest
import requests
from common.Md5 import MD5
from common.requests_util import RequestsUtil
from common.yaml_util import read_extract_yaml, get_object_path, read_case_yaml, write_extract_yaml


class TestApiLogin:

    # @pytest.mark.skip()
    # @pytest.mark.parametrize('args_name', read_case_yaml('./testcases/api_login/test_api_login.yaml'))
    # def test_get_app(self, args_name):
        pass

        # RequestsUtil('base_portal_url').standard_yaml(caseinfo)

        # url = args_name['request']['url']
        # data = args_name['request']['data']
        #
        # time_str = int(round(time.time() * 1000))
        # data['timestamp'] = time_str
        # data['clientId'] + data['ClientSecret'] + str(time_str)
        # sign = MD5(data['clientId'] + data['ClientSecret'] + str(time_str))
        # data['sign'] = sign
        # headers = {
        #     'Cookie': read_extract_yaml('Cookie')
        # }
        # req = RequestsUtil('base_app_url').send_request('post', url=url, headers=headers, data=data)
        # token = RequestsUtil('base_portal_url').get_text(req.text, 'accessToken')
        # write_extract_yaml({'accessToken': token})
