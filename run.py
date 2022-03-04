import os
import time
import pytest

from common.logger_util import LoggerUtil, error_log

if __name__ == '__main__':
    pytest.main(['-s']) # vs显示详细信息
    # allyre 生成测试报告
    # pytest.main(['-vs', '--alluredir', './temps'])
    # os.system("allure generate ./temps -o ./reports --clean")


