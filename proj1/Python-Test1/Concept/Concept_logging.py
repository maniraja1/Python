'''
Concept
    The logging module in Python is a ready-to-use and powerful module that is designed to meet the needs of beginners
    as well as enterprise teams

Module
    import logging, logging.handler

Methods
    basicConfig, critical, error, warning, info, debug

Notes

    You need to set the right level in basicConfig. You need to choose DEBUG to log everything or CRITICAL for logging
    just the critical errors

    There are 2 ways to initialize a logger
    1. using logging.basicconfig see function demologging
    2. using logging.getlogger(name) see function demokogging2

    Default format & level
    See Example 1.0

    Log all Events by setting the level to debug
    See Example 2.0

    Change the format using format level using logging.Formatter and also print logger.__dict__
    See Example 3.0

    You can print the logger and handler level
    see Example 4.0

    You can have one logger and multiple handlers and log messages depending on the looger and handler levels
    You could have one log for all messages and one for critical messages
    see Example 5.0

    Use rotating file handler
    If you use FileHandler for writing logs, the size of the log file will grow with time. Someday, it will occupy all of your disk space. To avoid that situation.
    you should use RotatingFileHandler instead of FileHandler in the production environment.
    See Example 6.0

    Note that you can also write your own customer handlers if you don't find what you need.

    Always use __name__ for logger name
    This names the logger the same as module from where the logger is created

    You can capture excptions with traceback
    logger.error('Failed to open file', exc_info=True)

    Do not get logger at the module level unless disable_existing_loggers is False

    logging.propagate
    If this attribute evaluates to true, events logged to this logger will be passed to the handlers of higher level (ancestor) loggers


Additional reading
    https://fangpenlin.com/posts/2012/08/26/good-logging-practice-in-python/
    https://docs.python.org/3/howto/logging-cookbook.html
    https://docs.python.org/3/library/logging.html
    https://docs.python.org/3/library/logging.handlers.html

***********************************************************************************************
    When implementing logging use code from demologging2 function below instead of demologging.
    Its a lot more flexible and behaves when you change logging level
************************************************************************************************


'''


import logging
import logging.handlers

def demologging(example, logginlevel=None, format=None):
    if logginlevel is None:
        logginlevel=logging.WARNING
    logging.basicConfig(filename='app.log', level=logginlevel, format=format)

    hostname = 'www.python.org'
    item = 'spam'
    filename = 'data.csv'
    mode = 'r'

    # Example logging calls (insert into your program)
    logging.critical('#'*20)
    logging.critical(f'{example}')
    logging.critical(f'Inside Demologging')
    logging.critical('Host %s unknown', hostname)
    logging.error("Couldn't find %r", item)
    logging.warning('Feature is deprecated')
    logging.info('Opening file %r, mode = %r', filename, mode)
    logging.debug('Got here')

def demologging2(example,logginlevel=None, format=None, printdict=False, printlogginglevel=False):
    if logginlevel is None:
        logginlevel=logging.WARNING

    logger = logging.getLogger(__name__)

    handler = logging.FileHandler("app2.log")
    formatter = logging.Formatter(format)
    handler.setFormatter(formatter)
    logger.setLevel(logging.DEBUG)
    handler.setLevel(logginlevel)
    logger.addHandler(handler)
    logger.propagate=False

    # Print logger and handler logging levels
    if printlogginglevel:
        print(f"Logger Level: {logger.level}")
        print(f"Handler Level: {handler.level}")
    # Print logger dict
    if printdict:
        print(f"Logger.Dict: {logger.__dict__}")

    hostname = 'www.python.org'
    item = 'spam'
    filename = 'data.csv'
    mode = 'r'

    # Example logging calls (insert into your program)
    logger.critical('#'*20)
    logger.critical(f'{example}')
    logger.critical(f'Inside Demologging2')
    logger.critical('Host %s unknown', hostname)
    logger.error("Couldn't find %r", item)
    logger.warning('Feature is deprecated')
    logger.info('Opening file %r, mode = %r', filename, mode)
    logger.debug('Got here')
    logger.removeHandler(handler)

def demologging3(example,logginlevel=None, format=None, printdict=False, printlogginglevel=False):
    if logginlevel is None:
        logginlevel=logging.WARNING

    logger = logging.getLogger('demologging2')

    handler = logging.FileHandler("app2.log")
    formatter = logging.Formatter(format)
    handler.setFormatter(formatter)
    logger.setLevel(logging.DEBUG)
    handler.setLevel(logginlevel)
    logger.addHandler(handler)
    logger.propagate=False

    handler2 = logging.FileHandler("app3.log")
    formatter = logging.Formatter(format)
    handler2.setFormatter(formatter)
    logger.setLevel(logging.DEBUG)
    handler2.setLevel(logging.CRITICAL)
    logger.addHandler(handler2)
    logger.propagate = False

    # Print logger and handler logging levels
    if printlogginglevel:
        print(f"Logger Level: {logger.level}")
        print(f"Handler Level: {handler.level}")
    # Print logger dict
    if printdict:
        print(f"Logger.Dict: {logger.__dict__}")

    hostname = 'www.python.org'
    item = 'spam'
    filename = 'data.csv'
    mode = 'r'

    # Example logging calls (insert into your program)
    logger.critical('#'*20)
    logger.critical(f'{example}')
    logger.critical(f'Inside Demologging2')
    logger.critical('Host %s unknown', hostname)
    logger.error("Couldn't find %r", item)
    logger.warning('Feature is deprecated')
    logger.info('Opening file %r, mode = %r', filename, mode)
    logger.debug('Got here')
    logger.removeHandler(handler)
    logger.removeHandler(handler2)

def demologging4(example,logginlevel=None, format=None, printdict=False, printlogginglevel=False):
    if logginlevel is None:
        logginlevel=logging.WARNING

    logger = logging.getLogger(__name__)

    handler = logging.handlers.RotatingFileHandler("app4.log",maxBytes=1024*1024*50, backupCount=5)
    formatter = logging.Formatter(format)
    handler.setFormatter(formatter)
    logger.setLevel(logging.DEBUG)
    handler.setLevel(logginlevel)
    logger.addHandler(handler)
    logger.propagate=False

    # Print logger and handler logging levels
    if printlogginglevel:
        print(f"Logger Level: {logger.level}")
        print(f"Handler Level: {handler.level}")
    # Print logger dict
    if printdict:
        print(f"Logger.Dict: {logger.__dict__}")

    hostname = 'www.python.org'
    item = 'spam'
    filename = 'data.csv'
    mode = 'r'

    # Example logging calls (insert into your program)
    logger.critical('#'*20)
    logger.critical(f'{example}')
    logger.critical(f'Inside Demologging2')
    logger.critical('Host %s unknown', hostname)
    logger.error("Couldn't find %r", item)
    logger.warning('Feature is deprecated')
    logger.info('Opening file %r, mode = %r', filename, mode)
    logger.debug('Got here')
    logger.removeHandler(handler)

open('app.log', 'w').close() ### Clean the file before you run
open('app2.log', 'w').close() ### Clean the file before you run
open('app3.log', 'w').close() ### Clean the file before you run
open('app4.log', 'w').close() ### Clean the file before you run

print('#'*20)
print('Example 1.0')
demologging('Example 1.0')
demologging2('Example 1.0')


print('#'*20)
print('Example 2.0')
demologging('Example 2.0', logging.DEBUG)
demologging2('Example 2.0', logging.DEBUG)

print('#'*20)
print('Example 3.0')
demologging('Example 3.0', logging.DEBUG, "%(asctime)s - %(levelname)s - %(message)s")
demologging2('Example 3.0', logging.DEBUG, "%(asctime)s - %(levelname)s - %(message)s", True)

print('#'*20)
print('Example 4.0')
demologging('Example 4.0', logging.DEBUG, "%(asctime)s - %(levelname)s - %(message)s")
demologging2('Example 4.0', logging.DEBUG, "%(asctime)s - %(levelname)s - %(message)s",False,True)

print('#'*20)
print('Example 5.0')
demologging3('Example 5.0', logging.DEBUG, "%(asctime)s - %(levelname)s - %(message)s",True,True)

print('#'*20)
print('Example 6.0')
demologging4('Example 6.0', logging.DEBUG, "%(asctime)s - %(levelname)s - %(message)s",True,True)

'''
logger = logging.getLogger(__name__)

handler = logging.FileHandler("app2.log")
handler.setLevel(logging.CRITICAL)

formatter = logging.Formatter("%(asctime)s - %(message)s")
handler.setFormatter(formatter)

logger.addHandler(handler)
'''