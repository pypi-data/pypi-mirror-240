import sys, os, re
from loguru import logger as loguer

loguercor = loguer.opt(colors=True)

level_dict = {
    'CRITICAL': {"level": "1"},
    'Print': {"level": "1", "color": "<green>"},
    'Traceback': {"level": "2", "color": "<red>"},
    'Exception': {"level": "2", "color": "<red>"},
    'Crawl Fasle': {"level": "2", "color": "<yellow>"},
    'ERROR': {"level": "2"},
    'WARNING': {"level": "3"},
    "SUCCESS": {"level": "3"},
    'Crawl': {"level": "4", "color": "<green>"},
    'Yield': {"level": "4", "color": "<yellow>"},
    'Return': {"level": "4", "color": "<yellow>"},
    'Start': {"level": "4", "color": "<yellow>"},
    'Close': {"level": "4", "color": "<red>"},
    "INFO": {"level": "4"},
    "DEBUG": {"level": "5"},
}


def get_level(level):
    level_list = []
    for k, v in level_dict.items():
        if level >= int(v.get("level")):
            level_list.append(k)
    return level_list


class Log():
    def __init__(self, log_stdout=True, log_level='INFO', log_file=False, format=None) -> None:
        self.level_dict = {
            "warn": 'WARNING',
            "info": 'INFO',
            "debug": 'DEBUG',
            "error": 'ERROR',
            "critical": 'CRITICAL',
            "success": 'SUCCESS',
        }
        self.level_stdout = {
            "critical": get_level(1),
            "error": get_level(2),
            "success": get_level(3),
            "warn": get_level(3),
            "info": get_level(4),
            "debug": get_level(5),
        }
        self.log_stdout, self.log_level, self.log_file = log_stdout, log_level, log_file
        self.format = format
        loguer.level("DEBUG", color="<green>")
        loguer.level("INFO", color="<cyan>")
        loguer.level("SUCCESS", color="<light-green>")
        loguer.level("WARNING", color="<yellow>")
        loguer.level("ERROR", color="<red>")
        loguer.level("CRITICAL", color="<red>")
        for k, v in level_dict.items():
            color = v.get("color")
            level = v.get("level")
            if color:
                loguer.level(k, no=int(level) * 10, color=color)

    def loggering(self):
        levels = self.level_dict.get(self.log_level.lower())
        slevel = self.level_stdout.get(self.log_level.lower())
        format = self.format
        stdout_handler = {
            "sink": sys.stdout,
            "colorize": True,
            "filter": lambda record: record["level"].name in slevel,
            "format": format
        }
        loguer.configure(handlers=[stdout_handler])
        if self.log_stdout:
            sys.stdout = InterceptHandler()
        if self.log_file:
            file_log = os.path.basename(__file__) if self.log_file is True else self.log_file
            file_log = (
                re.sub("\..*", ".log", file_log)
                if "." in file_log
                else file_log + ".log"
            )
            filename = f"./{file_log}"
            loguer.add(filename, level=levels, format=format)
        return loguer


class InterceptHandler():
    def write(self, message):
        if message.strip():
            loguer.log("Print", message.strip())

    def flush(self):
        pass


class loging:
    def __init__(self, log):
        self.loger = log

    def print(self, msg):
        self.loger.log('Print', msg)

    def info(self, msg):
        self.loger.info(self.repl(msg))

    def exception(self, msg):
        self.loger.exception(self.repl(msg))

    def warn(self, msg):
        self.loger.warning(self.repl(msg))

    def error(self, msg):
        self.loger.error(self.repl(msg))

    def debug(self, msg):
        self.loger.debug(self.repl(msg))

    def success(self, msg):
        self.loger.success(self.repl(msg))

    def critical(self, msg):
        self.loger.critical(self.repl(msg))

    def repl(self, msg):
        msg = msg.replace('<', '\<').replace('>', '\>')
        return msg
