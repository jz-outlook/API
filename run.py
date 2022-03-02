import os
import time
import pytest


if __name__ == '__main__':
    pytest.main(['-vs'])
    # allyre 生成测试报告
    # pytest.main(['-vs', '--alluredir', './temps'])
    # os.system("allure generate ./temps -o ./reports --clean")




    # 单元测试
    # head = "Cookie': 'TSID='+${Cookie}"
    # if "${" in head and "}" in head:
    #     start_index = head.index("${")
    #     end_index = head.index("}", start_index)
    #     old_value = head[start_index:end_index+1]
    #     new_value = read_extract_yaml(old_value[2:-1])
    #     # replace替换
    #     head = head.replace(old_value, new_value)
    #     print(old_value, new_value)
    #     print(head)