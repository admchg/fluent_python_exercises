"""
Chapter 15 Homework    
"""


# Problem 1: Precision
# This chapter introduced us to with statements. Many of us are already familiar with this for file handlers.
# What about for other use cases?

from decimal import Decimal, localcontext, Context

# use the above modules to compute the difference between the representation of 22/7 at 50 precision vs 28 precision
# write the difference with 20 precision

with localcontext(Context(prec=28)):
    x = Decimal(22) / Decimal(7)

with localcontext(Context(prec=50)):
    y = Decimal(22) / Decimal(7)

with localcontext(Context(prec=20)):
    print(x - y)

# Problem 2: Timeout
# Implement a class that timeouts after some input time
# make this class compatible in a with clause
from time import sleep


# Solution 1: Signal
# The standard solution is to use signal

import signal


class Timeout:
    def __init__(self, seconds, message=""):
        self.seconds = seconds
        self.message = message

    def _timeout_handler(self, signum, frame):
        raise TimeoutError(self.message)

    def __enter__(self):
        signal.signal(signal.SIGALRM, self._timeout_handler)
        signal.alarm(self.seconds)

    def __exit__(self, exc_type, exc_val, exc_tb):
        signal.alarm(0)


with Timeout(2, "Ran out of time!"):
    sleep(10)


# Solution 2: threads
# Basically we can rewrite the threading.Timer class
# We rewrite so that it works in a with clause

import threading


class Timeout(threading.Thread):
    def __init__(self, seconds, message=""):

        # init the thread
        threading.Thread.__init__(self)

        self.seconds = seconds
        self.message = message

        # This event will let us terminate the thread
        self.finished = threading.Event()

    def __enter__(self):
        #
        self.finished.wait(self.seconds)  # wait required time
        if not self.finished.is_set():
            self._timed_out()  # call timeout function
        self.finished.set()  # terminate thread

    def __exit__(self):
        self.finished.set()  # terminate thread

    def _timed_out(self):
        raise TimeoutError(self.message)


with Timeout(2, "Ran out of time!"):
    sleep(10)
