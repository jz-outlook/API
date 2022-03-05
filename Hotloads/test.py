# 调用多个方法
import base64
import random
import time

from common.yaml_util import read_extract_yaml


class Test:

    # 获得当前时间戳
    def get_random_time(self):
        return int(time.time() * 1000)

    # 判断字符串是否是数字
    def is_number(self, s):
        try:
            float(s)
            if s:
                s = int(s)
                print(type(s))
            return s
        except ValueError:
            return False

    def base64(self, base):
        bytes = base.encode("utf-8")
        str_url = base64.b64encode(bytes)
        return str_url


if __name__ == '__main__':
    s = 'Hy123!!!'
    print(Test().base64(s))

# MD5分支提交测试
# 改变MD5分支会不会影响主干
