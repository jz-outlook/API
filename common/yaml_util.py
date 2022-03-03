import os
import yaml


# 获取项目跟目录
def get_object_path():
    os.getcwd()
    return os.getcwd()


# 读取extract.yaml
def read_extract_yaml(key):
    with open(get_object_path() + '/extract.yaml', mode='r', encoding='utf-8') as f:  # mode默认read
        value = yaml.load(f, Loader=yaml.FullLoader)
        return value[key]


# 写入extract.yaml
def write_extract_yaml(data):
    with open(get_object_path() + '/extract.yaml', mode='a', encoding='utf-8') as f:  # mode未w时会清除已有key数据，a进行追加
        value = yaml.dump(data=data, stream=f, allow_unicode=True)
        return value


# 清空extract.yaml
def clear_extract_yaml():
    with open(get_object_path() + '/extract.yaml', mode='w', encoding='utf-8') as f:  # mode未w时会清除上次key数据，a进行追加
        f.truncate()


# 读取config.yaml
def read_config_yaml(portal, app):
    with open(get_object_path() + '/config.yaml', mode='r', encoding='utf-8') as f:  # mode默认read
        value = yaml.load(f, Loader=yaml.FullLoader)
        return value[portal][app]


# 读取yaml数据
def read_data_yaml(yaml_path):
    with open(get_object_path() + yaml_path, mode='r', encoding='utf-8') as f:  # mode默认read
        value = yaml.load(f, Loader=yaml.FullLoader)
        return value
