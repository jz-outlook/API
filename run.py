import os
import time
import pytest


if __name__ == '__main__':
    pytest.main(['-vs'])
    # allure 生成测试报告
    # pytest.main(['-vs', '--alluredir', './temps'])
    # os.system("allure generate ./temps -o ./reports --clean")


