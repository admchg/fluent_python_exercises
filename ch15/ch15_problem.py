"""
Chapter 15 Homework
"""


# Problem 1: Precision
# This chapter introduced us to with statements. Many of us are already familiar with
# this for file handlers.
# What about for other use cases?

# Use in PYMC3 for defining a model.

from decimal import Decimal, localcontext, Context

# use the above modules to compute the difference between the representation of 22/7 at
# 50 precision vs 28 precision
# write the difference with 20 precision

with localcontext() as ctx:
    ctx.prec = 50
    prec_50 = Decimal(22) / Decimal(7)

    ctx.prec = 28
    prec_28 = Decimal(22) / Decimal(7)

    ctx.prec = 20
    diff_20 = prec_28 - prec_50

print("using a context manager", diff_20)

# Without a context manager

prec_50 = Context(prec=50).divide(22, 7)
prec_28 = Context(prec=28).divide(22, 7)

diff_20 = Context(prec=20).subtract(prec_28, prec_50)
print("with a context object", diff_20)

# Problem 2: Timeout
# Implement a class that timeouts after some input time
# make this class compatible in a with clause
from time import sleep, time


class Timeout:
    def __init__(self, seconds):
        self.seconds = seconds

    def __enter__(self):
        self.start_time = time()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if (time() - self.start_time) > self.seconds:
            print("Timed out!")


with Timeout(2):
    sleep(4)
