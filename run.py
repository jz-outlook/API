import os
import time
import pytest

from config.test1 import test_email

if __name__ == '__main__':
    # pytest.main(['-vs'])
    # # # allyre 生成测试报告
    pytest.main(['-vs', '--alluredir', './temps'])
    os.system("allure generate ./temps -o ./reports --clean")
    test_email()
