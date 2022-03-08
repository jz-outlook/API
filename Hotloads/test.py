# 调用多个方法
import base64
import hashlib
import time

import rsa as rsa


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

    # RSA双钥加密生成方式
    # 生成密钥写入到指定的pem文件
    def create_key(self):
        # 根据密钥长度生成公钥和私钥
        (public_key, private_key) = rsa.newkeys(1024)
        print()
        # 保存公钥
        with open('public.pem', 'w') as f:
            f.write(public_key.save_pkcs1().decode())
        # 保存私钥
        with open('private.pem', 'w') as f:
            f.write(private_key.save_pkcs1().decode())

    # 通过公钥加密
    def public_key_encryption(self, args):
        # 导入公钥
        with open('public.pem') as f:
            pubkey = rsa.PublicKey.load_pkcs1(f.read().encode())
        # 加密
        byte_str = rsa.encrypt(str(args).encode('utf-8'), pubkey)
        print(byte_str)
        # 把二进制转换成16进制，base64
        miwen = base64.b64encode(byte_str).decode('utf-8')
        return miwen

    # 通过私钥解密
    def private_key_decode(self, args):
        # 导入私钥
        with open('private.pem') as f:
            private = rsa.PrivateKey.load_pkcs1(f.read().encode())
        # 字符串准换字符串格式
        byte_str = base64.b64decode(args)
        # 解密
        mingwen = rsa.decrypt(byte_str, private).decode()
        return mingwen


if __name__ == '__main__':
    print(Test().create_key())
    # print(Test().public_key_encryption('admin'))
    # print(Test().private_key_decode('c3fuuILtI49JW1O0J+qSzhT6u4YJ85E4NxdYwCzuc5cFIFCLDxE6T9zIqpIzGB9E1+vlm0ktQ1ZPbyOKYxMdYOjcTM5tlc2qN3DTfHxJokZXvLTwoe5MNi12LrTd2VGBOa5L81kAyLafpmAxjxx9BzaMS6eNgVI49gfz5Joe9Fk='))

    # a = {'tag': {'id': 197, 'name': '\\u7801\\u5c1a\\u6559\\u80b273321'}}
    # print(json.loads(json.dumps(a).replace(r"\\", '\\')))
    # print(a)
