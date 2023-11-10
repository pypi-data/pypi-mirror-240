import time
import requests
import inspect
import traceback
import threading
from .log import *
from .utils import *
from .pyconn import PrMysql
from .requestXpath import prequest
from .settion import _IT, settions
from concurrent.futures import ThreadPoolExecutor, as_completed

author = """
 ____
|  _ \ ___ _ __  _ __
| |_) / _ \ '_ \| '__|
|  __/  __/ | | | |
|_|   \___|_| |_|_|
"""


class PrSpiders(settions):

    def __init__(self, **kwargs):
        if self.custom_settings:
            for key, value in self.custom_settings.items():
                if not isinstance(value, int):
                    if value.isdigit():
                        value = int(value)
                setattr(settions, key.lower(), value)
        assert self.thread_num > 0, 'thread_num must be > 0'
        settions.init += 1
        if settions.init <= 1:
            Log(self.log_stdout, self.log_level, self.logger, format=self.log_format).loggering()
        self.loging = loging(loguercor)
        self.executor = ThreadPoolExecutor(self.thread_num)
        self.Request = requests.session() if self.session else requests
        loguercor.log('Start', Start
                      % (self.thread_num, self.retry, self.pid, self.download_delay, self.download_num,
                         self.log_level.upper()))
        self.spider_run()

    def spider_run(self):
        """
        线程一: 爬虫业务代码（请求入队列）
        线程二: 监听队列
        """
        self.thread_requests = threading.Thread(target=self.start_call)
        self.thread_queue = threading.Thread(target=self.start_queue)

        # 启动线程
        self.thread_requests.start()
        self.thread_queue.start()

        # 等待线程结束
        self.thread_requests.join()
        self.thread_queue.join()

    def start_queue(self):
        while True:
            qlist = []
            qsize = self.Queues.qsize()
            # 检查队列是否为空
            if not self.Queues.empty():
                queue_list = []
                num_to_download = min(self.download_num, qsize)
                for _ in range(num_to_download):
                    data = settions.Queues.get().data
                    wait = data.get('wait')
                    queue_list.append(data)
                    del data['wait']
                    if wait:
                        break
                qlist.append(queue_list)

                for qdata in qlist:
                    for item in qdata:
                        task = self.executor.submit(self.make_request, **item)
                        self.futures.add(task)
                    for future in as_completed(self.futures):
                        worker_exception = future.exception()
                        self.futures.remove(future)
                        if worker_exception:
                            if self.traceback:
                                formatted_traceback = traceback.format_exception(type(worker_exception),
                                                                                 worker_exception,
                                                                                 worker_exception.__traceback__)
                                formatted_traceback = ''.join(formatted_traceback)
                                loguercor.log('Traceback', formatted_traceback)
                            else:
                                loguercor.log('Exception', f"<red>%s</red>" % worker_exception)
                        else:
                            future_result = future.result()
                            if future_result.__class__.__name__ == 'generator':
                                for item in future_result:
                                    loguercor.log('Yield', item)
                            else:
                                if future_result:
                                    loguercor.log('Return', future_result)

                    time.sleep(self.download_delay)
            else:
                if self.thread_requests.is_alive():
                    pass
                else:
                    break

    def start_call(self, *args, **kwargs):
        self.open_spider()
        self.start_requests(*args, **kwargs)
        while True:
            if not settions.futures and not self.Queues.qsize():
                break
            time.sleep(0.314)
        self.close_spider()

    def open_spider(self):
        pass

    def close_spider(self):
        pass

    def start_requests(self, *args, **kwargs):
        if self.start_urls is None:
            raise AttributeError("Crawling could not start: 'start_urls' not found ")
        if isinstance(self.start_urls, list):
            for url in self.start_urls:
                self.Requests(url=url, callback=self.parse)
        else:
            self.Requests(url=self.start_urls, callback=self.parse)

    def parse(self, response):
        pass

    @staticmethod
    def Requests(url, headers=None, method="GET", meta=None, retry=True, callback=None, retry_num=3,
                 encoding="utf-8", retry_time=3, timeout=30, priority=0, wait=False, **kwargs):
        query = {
            "url": url,
            "headers": headers,
            "method": method,
            "meta": meta,
            "retry": retry,
            "callback": callback,
            "retry_num": retry_num,
            "encoding": encoding,
            "retry_time": retry_time,
            "timeout": timeout,
            "wait": wait,
        }
        frame = inspect.currentframe().f_back
        caller_name = frame.f_code.co_name
        if caller_name == 'start_requests':
            deep = priority
        else:
            if priority != 0:
                deep = priority
            else:
                if caller_name not in settions.deep_func:
                    settions.deep_func.append(caller_name)
                deep = -(settions.deep_func.index(caller_name)) - 1
        query.update(**kwargs)
        item = _IT(deep, query)
        settions.Queues.put(item)

    def make_request(self, url, callback, headers=None, retry_num=3, method="GET", meta=None, retry=True,
                     encoding="utf-8", retry_time=1, timeout=30, **kwargs):
        self.request_num += 1
        loguercor.log('Crawl',
                      f"<red>{method.upper()}</red> <blue>{url}</blue>")
        response = prequest(self, self.Request).get(url, headers=headers, retry_time=retry_num, method=method,
                                                    meta=meta, retry=retry, encoding=encoding,
                                                    retry_interval=retry_time, timeout=timeout, settion=settions,
                                                    **kwargs)
        self.retry_num += int(response.meta.get("retry_num"))
        if response and response.ok:
            self.success_num += 1
        else:
            self.false_num += 1
        return callback(response)

    def error(self, response):
        pass

    def process_timestamp(self, t):
        timeArray = time.localtime(int(t))
        formatTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
        return formatTime

    def __del__(self):
        end_time = time.time()
        spend_time = end_time - self.start_time
        try:
            average_time = spend_time / self.request_num
        except ZeroDivisionError:
            average_time = 0
        data = [
            ('Thread Num', self.thread_num),
            ('Download Delay', self.download_delay),
            ('Download Num', self.download_num),
            ('Request Num', self.request_num),
            ('Success Num', self.success_num),
            ('False Num', self.false_num),
            ('Retry Num', self.retry_num),
            ('Start Time', self.process_timestamp(self.start_time)),
            ('End Time', self.process_timestamp(end_time)),
            ('Spend Time', '%.3fs' % spend_time),
            ('Average Time', '%.3fs' % average_time)
        ]
        m = close_sign(data)
        loguercor.log('Close', m)
