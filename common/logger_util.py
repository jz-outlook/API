import logging
import time

from common.yaml_util import get_object_path, read_config_yaml


class LoggerUtil:

    def create_log(self, logger_name="log"):
        # 创建一个日志对象
        self.logger = logging.getLogger(logger_name)
        # 设置全局的日志级别(debug<info<warning<error<critical)
        self.logger.setLevel(logging.DEBUG)

        if not self.logger.handlers:
            # --------文件日志----------------------------------------------
            # 创建文件日志路径
            time_stamp = time.strftime('%Y-%m-%d', time.localtime(time.time()))
            # self.filt_log_path = get_object_path() + '/logs/' + read_config_yaml("log", 'log_name') + str(int(time.time())) + ".log"
            self.filt_log_path = get_object_path() + '/logs/' + read_config_yaml("log", 'log_name') + str(time_stamp) + ".log"
            # 创建文件日志的控制器
            self.file_hander = logging.FileHandler(self.filt_log_path, encoding='utf-8')
            # 设置文件日志的日志级别
            file_log_level = str(read_config_yaml('log', 'log_level')).lower()
            if file_log_level == 'debug':
                self.file_hander.setLevel(logging.DEBUG)
            elif file_log_level == 'info':
                self.file_hander.setLevel(logging.INFO)
            elif file_log_level == 'warning':
                self.file_hander.setLevel(logging.WARNING)
            elif file_log_level == 'error':
                self.file_hander.setLevel(logging.ERROR)
            elif file_log_level == 'critical':
                self.file_hander.setLevel(logging.CRITICAL)
            else:
                self.file_hander.setLevel(logging.DEBUG)
            # 设置日志文件的格式
            self.file_hander.setFormatter(logging.Formatter(read_config_yaml('log', 'log_format')))
            # 将文件日志的控制器加入到日志对象
            self.logger.addHandler(self.file_hander)

            # --------控制台日志-------------------------------------------------
            # 创建控制器日志的控制器
            self.console_hander = logging.StreamHandler()
            # 设置控制台的日志级别
            console_log_level = str(read_config_yaml('log', 'log_level')).lower()
            if console_log_level == 'debug':
                self.console_hander.setLevel(logging.DEBUG)
            elif console_log_level == 'info':
                self.console_hander.setLevel(logging.INFO)
            elif console_log_level == 'warning':
                self.console_hander.setLevel(logging.WARNING)
            elif console_log_level == 'error':
                self.console_hander.setLevel(logging.ERROR)
            elif console_log_level == 'critical':
                self.console_hander.setLevel(logging.CRITICAL)
            else:
                self.console_hander.setLevel(logging.DEBUG)
            # 设置控制台的格式
            self.console_hander.setFormatter(logging.Formatter(read_config_yaml('log', 'log_format')))
            # 将控制台日志的控制器加入到日志对象
            self.logger.addHandler(self.console_hander)

        # 返回包含有文件日志控制器和控制台日志控制器的日志对象
        return self.logger

# 错误日志方法
def error_log(message):
    LoggerUtil().create_log().error(message)
    raise Exception(message)

def logs(message):
    LoggerUtil().create_log().info(message)


if __name__ == '__main__':
    time_stamp = time.strftime('%Y-%m-%d',time.localtime(time.time()))
    print(time_stamp)