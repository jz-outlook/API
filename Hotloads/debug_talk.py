import random
import time

import yaml

from common.yaml_util import read_extract_yaml, get_object_path


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
        with open(get_object_path() + '/extract.yaml', mode='r', encoding='utf-8') as f:  # mode默认read
            value = yaml.load(f, Loader=yaml.FullLoader)
            return value[key]


if __name__ == '__main__':
    print(DebugTalk().read_extract_data("Cookie"))
