import os
import time
from typing import Optional
from queue import PriorityQueue
from .utils import *


class _IT:
    def __init__(self, level, data):
        self.level = level
        self.data = data

    def __lt__(self, other):
        if self.level == other.level:
            return len(self.data) < len(other.data)
        return self.level < other.level


class settions(object):
    """设置"""
    thread_num: Optional[int] = 10  # 线程数
    request_num: Optional[int] = 0  # 请求数
    retry_num: Optional[int] = 0  # 重试数
    success_num: Optional[int] = 0  # 成功请求数
    false_num: Optional[int] = 0  # 失败请求数
    start_urls: Optional[list] = None  # 默认请求起始url
    executor: Optional[object] = object  # 线程池处理器
    retry: Optional[bool] = True  # 重试开关，默认开启
    retry_xpath: Optional[str] = None  # 重试开关，默认开启
    pid: Optional[int] = os.getppid()  # 程序进程id
    start_time: Optional[int] = time.time()  # 开始时间
    download_delay: Optional[int] = 0  # 请求下载周期 默认 0s
    download_num: Optional[int] = 5  # 请求下载数量 默认 5/次
    logger: Optional[bool or str] = False  # 日志存储开关，默认关闭；可选（bool|文件名）
    log_level: Optional[str] = 'info'  # 日志等级，默认info
    log_stdout: Optional[bool] = False  # 日志控制台重定向，默认关闭
    futures: Optional[list] = set()  # 线程池对象
    init: Optional[int] = 0  # 日志初始化
    Queues: Optional[object] = PriorityQueue()  # 优先级队列
    deep_func: Optional[list] = []  # 深度函数
    custom_settings: Optional[dict] = {}  # 通用设置
    Request: Optional[object] = object
    session: Optional[bool] = True  # 请求是否开启session;默认开启
    traceback: Optional[bool] = False  # 当程序发生异常时，是否显示堆栈;默认关闭
    log_format: Optional[str] = log_format  # 日志格式 文件utils.log_format
