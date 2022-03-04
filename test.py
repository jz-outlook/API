# 调用多个方法
import random
import time

from common.yaml_util import read_extract_yaml


class Test:

    # 获得当前时间戳
    def get_random_time(self):
        return int(time.time() * 1000)

    def is_number(self, s):
        try:
            float(s)
            if s:
                s = int(s)
                print(type(s))
            return s
        except ValueError:
            return False


if __name__ == '__main__':
    # s = '1496393241355599873'
    s = '22baf927467b57426e98fa464cea2ccdc1'
    print(Test().is_number(s))

# MD5分支提交测试
# 改变MD5分支会不会影响主干
