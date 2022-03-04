import json
import traceback

import yaml

from common.logger_util import error_log
from common.yaml_util import read_data_yaml, get_object_path


# 读取测试用例yaml
def read_case_yaml(yaml_path):
    try:
        with open(get_object_path() + yaml_path, mode='r', encoding='utf-8') as f:  # mode默认read
            caseinfo = yaml.load(f, Loader=yaml.FullLoader)
            if len(caseinfo) >= 2:
                return caseinfo
            else:
                if 'parameterize' in dict(*caseinfo).keys():
                    new_caseinfo = ddt(*caseinfo)
                    return new_caseinfo
                else:
                    return caseinfo
    except Exception as e:
        error_log("读取测试用例方法read_case_yaml异常: %s" % str(traceback.format_exc()))


def ddt(caseinfo):
    try:
        if 'parameterize' in caseinfo.keys():
            caseinfo_str = json.dumps(caseinfo)
            for param_key, param_value in caseinfo['parameterize'].items():
                key_list = param_key.split("-")
                # 规范yaml数据文件的写法
                new_caseinfo = []
                length_flag = True
                data_list = read_data_yaml(param_value)
                for data in data_list:
                    if len(data) != len(key_list):
                        length_flag = False
                        break
                # 替换值
                if length_flag:
                    for x in range(1, len(data_list)):  # 循环数据行数
                        temp_caseinfo = caseinfo_str
                        for y in range(0, len(data_list[x])):  # 循环数据列
                            if data_list[0][y] in key_list:
                                # 替换原始的yaml文件中$ddt{}
                                # 如果说数据是一个整形或浮点型，要加""
                                if isinstance(data_list[x][y], int) or isinstance(data_list[x][y], float):
                                    temp_caseinfo = temp_caseinfo.replace('"$ddt{' + data_list[0][y] + '}"',
                                                                          str(data_list[x][y]))
                                else:
                                    temp_caseinfo = temp_caseinfo.replace("$ddt{" + data_list[0][y] + "}",
                                                                          str(data_list[x][y]))
                        new_caseinfo.append(json.loads(temp_caseinfo))
                return new_caseinfo
        else:
            print("不需要做数据驱动")
            return caseinfo
    except Exception as e:
        error_log("数据驱动方法ddt异常: %s" % str(traceback.format_exc()))