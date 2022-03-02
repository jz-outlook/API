import os
import pytest
from common.yaml_util import clear_extract_yaml


# 会话开始前清空extract——yaml文件
@pytest.fixture(scope="session", autouse=True)
def clear_extract():
    clear_extract_yaml()
