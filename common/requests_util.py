import json
import re
import time
import traceback

import jsonpath
import requests

from common.Md5 import MD5
from common.logger_util import error_log, logs
from common.yaml_util import read_config_yaml, write_extract_yaml, get_object_path
from Hotloads.debug_talk import DebugTalk


class RequestsUtil:
    # 关联会话
    session = requests.session()

    def __init__(self, app, obj):
        self.base_url = read_config_yaml('base', app)
        self.obj = obj

    # 替换值的方法(替换url,params,data,json,headers)
    def replace_value(self, data):
        if data:
            # 保存数据类型
            data_type = type(data)
            if isinstance(data, dict) or isinstance(data, list):
                str_data = json.dumps(data)
            else:
                str_data = str(data)
            # 替换操作
            for cs in range(1, str_data.count('${') + 1):
                if "${" in str_data and "}" in str_data:
                    start_index = str_data.index("${")
                    end_index = str_data.index("}", start_index)
                    old_value = str_data[start_index:end_index + 1]
                    # 反射：通过类的对象和方法字符串调用方法
                    func_name = old_value[2:old_value.index("(")]  # 获取调用方法的名称
                    args_value = old_value[old_value.index('(') + 1:old_value.index(')')]  # 获取调用方法的内容
                    if args_value != "":
                        args_value1 = args_value.split(',')
                        new_value = getattr(DebugTalk(), func_name)(*args_value1)
                    else:
                        new_value = getattr(DebugTalk(), func_name)()
                    # replace函数替换
                    if isinstance(new_value, int) or isinstance(new_value, float):
                        # print("第一种替换方式")
                        str_data = str_data.replace('"' + old_value + '"', str(new_value))
                    else:
                        str_data = str_data.replace(old_value, str(new_value))
                        # print("第二种替换方式")
                    # print('替换后的字段' + str_data)

            # 还原数据类型
            if isinstance(data, dict) or isinstance(data, list):
                data = json.loads(str_data)
            else:
                data = data_type(str_data)
        return data

    # 规范YAML测试用例
    def standard_yaml(self, caseinfo):
        try:
            logs('------------测试开始------------')
            caseinfo_keys = caseinfo.keys()
            # 判断一级关键字是否包含有：name,request,validate
            if 'name' in caseinfo_keys and 'request' in caseinfo_keys and 'validate' in caseinfo_keys:
                # 判断request下面是否包含：method,url
                requests_keys = caseinfo['request'].keys()
                if 'method' in requests_keys and 'url' in requests_keys:
                    # print('yaml基本架构检查通过')
                    # 发送请求
                    name = caseinfo.pop("name")
                    logs('接口名称: %s' % name)
                    method = caseinfo['request'].pop("method")
                    url = caseinfo['request'].pop("url")
                    # 调用send_request发起请求
                    req = self.send_request(method, url, **caseinfo['request'])
                    return_text = req.text
                    return_code = req.status_code
                    results_json = None
                    try:
                        results_json = req.json()
                    except Exception as e:
                        error_log('返回的格式不是JSON格式，不能使用jsonPath提取')
                    # 提取Cookie值写入到extract.yaml
                    # 判断extract是不是在caseInfo_keys下
                    if "extract" in caseinfo_keys:
                        # 遍历extract中的值，如果有则使用re正则方式进行提取写入
                        for key, value in caseinfo['extract'].items():
                            if "(.*?)" in value or "(.+?)" in value:
                                re_value = re.search(value, return_text)
                                if re_value:
                                    extract_value = {key: re_value.group(1)}
                                    write_extract_yaml(extract_value)
                            else:
                                # jsonPath方式提取
                                jsonvalue = jsonpath.jsonpath(results_json, value)
                                if jsonvalue:
                                    extract_value = {key: jsonvalue[0]}
                                    write_extract_yaml(extract_value)
                    # 断言
                    # 预期结果caseinfo['validate']，实际结果results_json
                    self.assert_result(caseinfo['validate'], results_json, return_code)
                else:
                    error_log('request下必须包含method,url')
            else:
                pass
                error_log("一级关键字必须包含：name,request,validate")
        except Exception as e:
            error_log("规范yaml测试用例standard_yaml异常: %s" % str(traceback.format_exc()))

    # 统一请求封装
    def send_request(self, method, url, **kwargs):
        try:
            # 对请求方式进行处理转小写
            method = str(method).lower()
            # 基础路径拼接+替换
            url = self.base_url + self.replace_value(url)
            # print(url)
            # 请求头和参数的替换
            for key, value in kwargs.items():
                if key in ['params', 'data', 'json', 'headers']:
                    kwargs[key] = self.replace_value(value)
                # 文件上传
                elif key == "files":
                    for files_key, flies_path in value.items():
                        value[files_key] = open(get_object_path() + flies_path, 'rb')
            # 输出信息日志
            # logs('接口名称: %s' % name)
            logs('请求方式: %s' % method)
            logs('请求路径: %s' % url)
            if 'headers' in kwargs.keys():
                logs('请求头: %s' % kwargs['headers'])
            else:
                logs('请求头为空')
            if 'params' in kwargs.keys():
                logs('请求params参数: %s' % kwargs['params'])
            elif 'data' in kwargs.keys():
                logs('请求data参数: %s' % kwargs['data'])
            elif 'json' in kwargs.keys():
                logs('请求json参数: %s' % kwargs['json'])
            else:
                logs('请求参数为空')
            if 'files' in kwargs.keys():
                logs('文件上传: %s' % kwargs['files'])
            # 请求
            req = RequestsUtil.session.request(method, url, **kwargs, verify=False)
            return req
        except Exception as e:
            error_log("发送请求send_request异常: %s" % str(traceback.format_exc()))

    # 校验字段获取方法
    def get_text(self, res, key):
        if res is not None:
            try:
                # 将res文本转换为json，通过jsonpath解析获取到指定的key的value值，默认是list类型
                text = json.loads(res)
                value = jsonpath.jsonpath(text, '$..{0}'.format(key))
                # jsonpath获取的结果是list类型的值，如果获取失败则是False
                if value:
                    # 将list转换为string格式类型
                    if len(value) == 1:
                        return value[0]
                return value
            except Exception as e:
                return e
        else:
            return None

    # 断言判断
    def assert_result(self, yq_result, sj_result, return_code):
        try:
            logs('预取结果: %s' % yq_result)
            logs('实际结果: %s' % sj_result)
            all_flag = 0
            for yq_result in yq_result:
                for key, value in yq_result.items():
                    if key == "equals":
                        flag = self.equals_assert(value, sj_result, return_code)
                        all_flag = all_flag + flag
                    elif key == "contains":
                        flag = self.contains_assert(value, sj_result)
                        all_flag = all_flag + flag
                    else:
                        print("不支持该断言方式")
            assert all_flag == 0
            logs('请求接口成功')
            logs('------------测试结束------------\n')
        except Exception as e:
            logs('请求接口失败')
            logs('------------测试结束------------\n')
            error_log("判断断言assert_result异常: %s" % str(traceback.format_exc()))

    # 相等断言
    def equals_assert(self, value, sj_result, return_code):
        flag = 0
        for assert_key, assert_value in value.items():
            if assert_key == "code":  # 状态码断言
                if assert_value != return_code:
                    flag = flag + 1
                    error_log("断言失败：状态码不等于%s" % return_code)
            else:
                lists = jsonpath.jsonpath(sj_result, "$..%s" % assert_key)
                if lists:
                    if assert_value not in lists:
                        flag = flag + 1
                        error_log("断言失败：" + assert_key + "不等于" + str(assert_value))
                else:
                    flag = flag + 1
                    error_log("断言失败:返回的结果中不存在:" + assert_key)
        return flag

    # 包含断言
    def contains_assert(self, value, sj_result):
        flag = 0
        if str(value) not in str(sj_result):
            flag = flag + 1
            error_log("断言失败：返回的结果中不包含" + str(value))
        return flag


    def md5_yaml(self, caseinfo):
        try:
            logs('------------测试开始------------')
            caseinfo_keys = caseinfo.keys()
            # 判断一级关键字是否包含有：name,request,validate
            ###########
            logs('------------测试开始------------')
            caseinfo_keys = caseinfo.keys()
            # 判断request下面是否包含：method,url
            requests_keys = caseinfo['request']
            requests_keys = requests_keys['data']
            clientId = requests_keys['clientId']
            ClientSecret = requests_keys['ClientSecret']
            timestamp = str(int(time.time() * 1000))
            requests_keys['timestamp'] = timestamp
            requests_keys['sign'] = MD5(clientId + ClientSecret + timestamp)
            # 发送请求
            name = caseinfo.pop("name")
            logs('接口名称: %s' % name)
            method = caseinfo['request'].pop("method")
            url = caseinfo['request'].pop("url")
            # 调用send_request发起请求
            req = self.send_request(method, url, **caseinfo['request'])

            #################
            return_text = req.text
            return_code = req.status_code
            results_json = None
            try:
                results_json = req.json()
            except Exception as e:
                error_log('返回的格式不是JSON格式，不能使用jsonPath提取')
            # 提取Cookie值写入到extract.yaml
            # 判断extract是不是在caseInfo_keys下
            if "extract" in caseinfo_keys:
                # 遍历extract中的值，如果有则使用re正则方式进行提取写入
                for key, value in caseinfo['extract'].items():
                    if "(.*?)" in value or "(.+?)" in value:
                        re_value = re.search(value, return_text)
                        if re_value:
                            extract_value = {key: re_value.group(1)}
                            write_extract_yaml(extract_value)
                    else:
                        # jsonPath方式提取
                        jsonvalue = jsonpath.jsonpath(results_json, value)
                        if jsonvalue:
                            extract_value = {key: jsonvalue[0]}
                            write_extract_yaml(extract_value)
                    # 断言
                    # 预期结果caseinfo['validate']，实际结果results_json
                    self.assert_result(caseinfo['validate'], results_json, return_code)
        except Exception as e:
            error_log("规范yaml测试用例standard_yaml异常: %s" % str(traceback.format_exc()))


