#!/usr/bin/env python
# coding: utf-8

# # Chapter 1 Exercises
#
# (Adam)
#
# Nothing too complex or interesting, but good practice with the Python data/object model.

# ## Problem 1
#
# Write a Binary class that can be called with Binary(n), where n is an integer. The only
# attribute the class may have is a text representation of n in binary, so you should not
# save n except as a string representing n in binary.
#
# The representation of Binary(n) should be the string, e.g. str(Binary(7)) = "111".
#
# Finally, the class must support addition with another Binary object,
# and multiplication with an integer. All operations should be done without needing to
# convert anything; int("0") or int("1") is fine. In both cases, you should return a Binary object.
#
# No libraries are needed.
#
# Don't worry about dealing with zero!

# In[ ]:


class Binary:
    def __init__(self, n):
        str_n = ""
        while n > 0:
            str_n = f"{n % 2}{str_n}"
            n = n // 2
        self.n = str_n

    def __repr__(self):
        return f"{self.n}"

    def __add__(self, other):
        max_length = max(len(self.n), len(other.n))
        self_binary_str = self.n.zfill(max_length)
        other_binary_str = other.n.zfill(max_length)
        carry = "0"
        binary_sum = ""
        for i, j in zip(self_binary_str[::-1], other_binary_str[::-1]):
            if i == j:
                binary_sum = carry + binary_sum
                carry = i
            else:
                binary_sum = _not(carry) + binary_sum

        if carry == "1":
            binary_sum = carry + binary_sum

        sum_ = Binary(0)
        sum_.n = binary_sum

        return sum_

    def __mul__(self, integer):
        if integer == 0:
            return 0
        elif integer == 1:
            return self
        else:
            return self + self * (integer - 1)


def binary_to_int(bin_str):
    if len(bin_str) == 1:
        return int(bin_str)
    else:
        return 2 ** (len(bin_str) - 1) * int(bin_str[0]) + binary_to_int(bin_str[1:])


def _not(x):
    if x == "0":
        return "1"
    else:
        return "0"


# ## Problem 1 Test Cases

# In[ ]:


import numpy as np


def test():
    x = np.random.randint(1, 1000, size=500)
    y = np.random.randint(1, 1000, size=500)
    z = x + y
    w = x * y

    if not all([str(Binary(i)) == np.binary_repr(i) for i in x]):
        return "Failed repr"

    if not all(
        [str(Binary(x[k]) + Binary(y[k])) == np.binary_repr(z[k]) for k in range(500)]
    ):
        return "Failed addition"

    if not all([str(Binary(x[k]) * y[k]) == np.binary_repr(w[k]) for k in range(500)]):
        return "Failed multiplication"

    return "Passed"
