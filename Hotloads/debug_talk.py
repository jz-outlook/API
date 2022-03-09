import base64
import hashlib
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
    def base64_str(self, base):
        bytes = base.encode("utf-8")
        str_url = base64.b64encode(bytes)
        return str_url

    def MD5(self, args):
        utf8_str = str(args).encode('utf-8')
        md5_str = hashlib.md5(utf8_str).hexdigest()
        # md5_str.upper() 大写
        return md5_str

    def base64(self, base):
        utf8_str = str(base).encode('utf-8')
        base64_str = base64.b64encode(utf8_str).decode('utf-8')
        return base64_str

if __name__ == '__main__':
    print(DebugTalk().get_random_time())
