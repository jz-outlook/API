import random
import time

from common.yaml_util import read_extract_yaml


class DebugTalk:

    # 获得当前时间戳
    def get_random_time(self):
        return int(time.time() * 1000)

    # 获取随机数
    def get_random_number(self, min, max):
        rm = random.randint(int(min), int(max))
        return str(rm)

    # 读取extract文件中的值
    def read_extract_data(self, key):
        return read_extract_yaml(key)


if __name__ == '__main__':
    print(DebugTalk().read_extract_data("Cookie"))
