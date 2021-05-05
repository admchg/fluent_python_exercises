#!/usr/bin/env python
# coding: utf-8

# # Chapter 3 Exercises
# By: Vic

import numpy as np
import requests
import pandas as pd

# ---------------------------------
# ## Problem 0
# For testing, you should use the numbers.txt in the git repo
# Write a function to download that data and read it into memory


def get_data():
    with open("ch3/numbers.txt") as fp:
        numbers = fp.read()

    numbers = iter(numbers.split("\n"))
    return numbers


# ---------------------------------
# ## Problem 1
# Let m be a natural number and [m] := {1, ..., m}
# Suppose you have a sequence s of length n, n \in \mathbb{N} in [m]
# and that there exist some x \in s which occurs at least n/2 times in s
# Find x

# method 1: use a dict to keep track of counts
# O(n) time, O(n) space
def frequent_dict(s):
    s = list(s)

    d = {}

    for item in s:
        d[item] = d.get(item, 0) + 1

    for item, count in d.items():
        if count > len(s) / 2:
            return item


# method 2: Boyer Moore majority vote algorithm
# Drawback: does not return correct solution if the n/2 guarantee is not met
# Space complexity:
# Only a single counter and item is stored so it's O(1)
# however in bit complexity, it would be log(n) + log(m)
# See general case: http://theory.stanford.edu/~trevisan/cs154-12/notestream.pdf


def frequent(s):
    held = next(s)
    counter = 1

    for item in s:
        if item == held:
            counter += 1
        elif counter == 0:
            held = item
            counter = 1
        else:
            counter -= 1
    return held


# ---------------------------------
# ## Problem 2

k = 4
g_k = np.random.randint(100)
N = 10000000


def generate_data(g, k, N):
    selection = [g for x in range(round(N / k) + 1)]
    s_1 = np.concatenate(
        (
            selection,
            np.random.randint(100, size=N - len(selection)),
        )
    )
    np.random.shuffle(s_1)
    return s_1


def frequent_k(s, k):
    s = list(s)

    d = {}

    for item in s:
        d[item] = d.get(item, 0) + 1

    for item, count in d.items():
        if count > len(s) / k:
            return item


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
