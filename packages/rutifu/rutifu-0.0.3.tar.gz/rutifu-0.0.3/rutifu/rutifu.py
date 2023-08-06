# RUTIFU - Random Utilities That I Find Useful

import syslog
import os
import time
import threading
import traceback
import executor

sysLogging = True

# optionally import app specific configuration
try:
    from debugConf import *
except ImportError:
    pass

# log a message to syslog or stdout
def log(*args):
    message = ""
    for arg in args:
        message += arg.__str__()+" "
    if sysLogging:
        syslog.syslog(message)
    else:
        print(time.strftime("%b %d %H:%M:%S")+" "+message)

# log the traceback for an exception
def logException(name, ex):
    tracebackLines = traceback.format_exception(None, ex, ex.__traceback__)
    log(name+":")
    for tracebackLine in tracebackLines:
        log(tracebackLine)

# log a debug message conditioned on a specified global variable
def debug(*args):
    if (args[0] in globals()) and globals()[args[0]]:  # only log if the specified debug variable is True
        log(*args[1:])

# thread object that logs a stack trace if there is an uncaught exception
class LogThread(threading.Thread):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.runTarget = self.run
        self.run = self.logThread

    def logThread(self):
        try:
            self.runTarget()
        except Exception as ex:
            logException("thread "+threading.currentThread().name, ex)

# convenience function to create and start a thread
def startThread(name, target, **kwargs):
    thread = LogThread(name=name, target=target, **kwargs)
    thread.start()

# execute an external OS command
def osCommand(cmd):
    try:
        executor.execute(cmd)
    except Exception as ex:
        log("osCommand", "Command failed:", str(ex), cmd)
