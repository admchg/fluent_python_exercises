"""
Chapter 15 Homework    
"""


# Problem 1: Precision
# This chapter introduced us to with statements. Many of us are already familiar with this for file handlers. 
# What about for other use cases?

from decimal import Decimal, localcontext, Context

# use the above modules to compute the difference between the representation of 22/7 at 50 precision vs 28 precision
# write the difference with 20 precision


# Problem 2: Timeout
# Implement a class that timeouts after some input time 
# make this class compatible in a with clause
from time import sleep


class Timeout:

    def __init__(self, seconds, *):
        return 0

    def __enter__(self):
        return 0

    def __exist__(self, *):
        return 0


with Timeout(2):
    sleep(10)
    