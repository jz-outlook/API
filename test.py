
# 调用多个方法
import random
import time

from common.yaml_util import read_extract_yaml


class Test:

    # 获得当前时间戳
    def get_random_time(self):
        return int(time.time() * 1000)


if __name__ == '__main__':
    print(Test().get_random_time())


# master分支 