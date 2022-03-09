# import allure
# import pytest
#
# from Hotloads.test import Test
# from common.parameterize_util import read_case_yaml
# from common.requests_util import RequestsUtil
#
# from Hotloads.debug_talk import DebugTalk
#
#
# @allure.epic("接口自动化测试")
# @allure.feature("WEB应用管理模块")
# class TestUserGroups:
#
#     @allure.story("获取WEB应用列表")
#     @pytest.mark.parametrize('caseinfo', read_case_yaml('./testCases/web_app_manage/get_web_list.yaml'))
#     def test_get_web_list(self, caseinfo):
#         RequestsUtil('base_api_url', DebugTalk()).standard_yaml(caseinfo)
#
#     @allure.story("添加WEB应用")
#     @pytest.mark.parametrize('caseinfo', read_case_yaml('./testCases/web_app_manage/save_web.yaml'))
#     def test_save_web(self, caseinfo):
#         RequestsUtil('base_api_url', DebugTalk()).standard_yaml(caseinfo)
#
#     @allure.story("修改WEB应用")
#     @pytest.mark.parametrize('caseinfo', read_case_yaml('./testCases/web_app_manage/edit_web.yaml'))
#     def test_edit_web(self, caseinfo):
#         RequestsUtil('base_api_url', DebugTalk()).standard_yaml(caseinfo)
#
#     @allure.story("删除WEB应用")
#     @pytest.mark.parametrize('caseinfo', read_case_yaml('./testCases/web_app_manage/delete_web.yaml'))
#     def test_delete_web(self, caseinfo):
#         RequestsUtil('base_api_url', DebugTalk()).standard_yaml(caseinfo)