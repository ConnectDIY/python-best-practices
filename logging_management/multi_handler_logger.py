import logging

"""
The snippet of writing logs to both
- terminal 
- file

"""


def get_log_level_int(level: str) -> int:
    numeric_level = getattr(logging, level.upper(), None)
    if not isinstance(numeric_level, int):
        raise ValueError('Invalid log level: %s' % level)
    else:
        return numeric_level


cfg = {
    "TERMINAL_LOG_FORMAT": "%(processName)s: %(message)s",

    "TERMINAL2_LOG_FORMAT": "%(message)s",
    "TERMINAL2_LOG_LVL": "INFO",
    "FILE2_LOG_LVL": "DEBUG",
    "FILE_LOG_FORMAT": '%(asctime)s | %(levelname)-7s | in \'%(module)s\' | %(message)s',

}

terminal_logger1 = logging.getLogger('you_tool_name')
terminal_and_file_logger2 = logging.getLogger('you_tool_name.wp')
terminal_and_file_logger2.propagate = False

# That is highly important that logger also has Log level!
#   Otherwise, logger will have default level = Warning and you loggers won't
#   print messages even if they have DEBUG level
terminal_and_file_logger2.setLevel(logging.DEBUG)

# Configure Logger1
log_level = logging.INFO
terminal_logger1.setLevel(log_level)
formatter = logging.Formatter(cfg['TERMINAL_LOG_FORMAT'])
ch = logging.StreamHandler()
ch.setFormatter(formatter)
terminal_logger1.addHandler(ch)  # Users logger


# Configure Logger2
file_formatter = logging.Formatter(cfg['FILE_LOG_FORMAT'])
console_formatter = logging.Formatter(cfg['TERMINAL2_LOG_FORMAT'])
ch = logging.StreamHandler()
fh = logging.FileHandler(filename='my_tool.log')
# If we want to add separate log levels for every handler
ch.setLevel(get_log_level_int(cfg['TERMINAL2_LOG_LVL']))
fh.setLevel(get_log_level_int(cfg['FILE2_LOG_LVL']))
ch.setFormatter(console_formatter)
fh.setFormatter(file_formatter)
terminal_and_file_logger2.addHandler(ch)
terminal_and_file_logger2.addHandler(fh)
