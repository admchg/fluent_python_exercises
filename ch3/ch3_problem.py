#!/usr/bin/env python
# coding: utf-8

# # Chapter 3 Exercises
# By: Vic

import numpy as np
import requests

# ---------------------------------
# ## Problem 0
# For testing, you should use the numbers.txt in the git repo
# Write a function to download that data and read it into memory


def get_data(url: str) -> str:
    return 0


# ---------------------------------
# ## Problem 1
# Let m be a natural number and [m] := {1, ..., m}
# Suppose you have a sequence s of length n, n \in \mathbb{N} in [m]
# and that there exist some x \in s which occurs at least n/2 times in s
# Find x


def frequent(s: str) -> int:
    return 0


# ---------------------------------
# ## Problem 2
# For the previous problem, what if the frequency was instead some n/k for some k a natural number?

k = 4
g_k = np.random.randint(100)
N = 10000000


def generate_data(g, k, N):
    s_1 = np.concatenate(([g for x in range(N)], np.random.randint(100, size=N)))
    np.random.shuffle(s_1)
    return s_1


def frequent_k(s: str) -> int:
    return 0


# ---------------------------------
# ## Problem 3
# Go back to Problem 1 and 2 and evaluate your time complexity.
# Is it possible to do better than O(log(n) + log(m))? Why / why not?
# Challenge: What is the probability that your algorithm runs in constant time?

# ---------------------------------
# ## Optional Problem 4
# What if instead you merely want to determine the number with frequency n/k with probability > p?

if __name__ == "__main__":
    # Problem 1
    url = "https://raw.githubusercontent.com/admchg/fluent_python_exercises/main/ch3/numbers.txt"
    assert frequent(get_data(url)) == 52

    # Problem 2
    assert frequent_k(generate_data(g_k, k, N)) == g_k
