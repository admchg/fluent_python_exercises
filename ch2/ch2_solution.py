#!/usr/bin/env python
# coding: utf-8

# # Chapter 2 Exercises
# By: Sid
# Description: Tuples, bisect, deque - All the libraries you need have been imported
#
# To run: python ch2_problem.py

import bisect
from collections import deque

# ---------------------------------
# ## Problem 1
# Use tuple unpacking to complete this function
def check_brackets(input_string):
    """
    Take an input string and return True if brackets are matching and False
    if they are not.

    Parameters
    ----------
    input_array: str
        A string with mathematical operations using brackets

    Returns
    -------
    bool
        True if input has matching brackets

    Examples:
    ---------
    >>> check_brackets("{9 - [{2 * (1 + 2) + 4} + 5 / 5] * 9}")
    True
    >>> check_brackets("[[{[3 + 4}*2]] + 6")
    False
    """

    bracket_starts = "{[("
    bracket_ends = "}])"
    bracket_map = dict(zip(bracket_starts, bracket_ends))

    if len(input_string) == 0:
        return True
    if len(input_string) == 1:
        return input_string not in (bracket_starts + bracket_ends)

    head, *mid, tail = input_string
    if head in bracket_ends:
        return False
    if head in bracket_starts:
        if tail in bracket_starts:
            return False
        if tail == bracket_map[head]:
            return check_brackets("".join(mid))
        else:
            return check_brackets("".join((head, *mid)))
    else:
        return check_brackets("".join((*mid, tail)))


# -------------------------
# ## Problem 2
# Use bisect to create a historgram
def my_histogram(input_array, bins, include=False):
    """
    Returns a histogram of `input_array` with `bins` as the cut points.

    Parameters
    ----------
    input_array: list
        An array of floats
    bins: list
        A sorted list of INTERNAL bin edges
    include: bool
        If True, include bin edge value as part of bin

    Returns
    -------
    list
        A list of counts of length `len(bins) + 1`

    Examples
    --------
    >>> my_histogram([10, 2, 2, 1, 5, 6, 11, 12], [3, 6, 9], True)
    [3, 2, 0, 3]
    >>> my_histogram([10, 2, 2, 1, 5, 6, 11, 12], [3, 6, 9], False)
    [3, 1, 1, 3]
    >>> my_histogram(range(5), [2, 3])
    [2, 1, 2]
    """
    counter = [0] * (len(bins) + 1)

    if include:
        bisect_fnc = bisect.bisect_left
    else:
        bisect_fnc = bisect.bisect

    for i in input_array:
        idx = bisect_fnc(bins, i)
        counter[idx] += 1

    return counter


# ---------------------
# ## Problem 3
# Search breadth first through a nested dictionary to
# find a key that matches key
def search_dictionary(dict_to_search, key):
    """
    Searches for `key` in `dict_to_search` and returns
    the shallowest value for `key`

    Parameters
    ----------
    dict_to_search: dict
        A dictionary
    key: hashable
        The key to search for

    Returns
    -------
    any
        Value matching key

    Raises
    ------
    KeyError
        if key not found in dictionary

    Examples
    --------
    >>> test_dict1 = {'a': {'n': {'d': 2, 'q': 3}}, 'b': {'m': {'e': 9}, 'q': 4}}
    >>> search_dictionary(test_dict1, 'q')
    4
    >>> search_dictionary(test_dict1, 'e')
    9
    >>> test_dict2 = {'a': {'n': {'d': 2, 'q': 3}}, 'b': {'m': {'e': 9}, 'u': 4}}
    >>> search_dictionary(test_dict2, 'q')
    3
    """

    dq = deque()
    dq.append(dict_to_search)

    while len(dq) > 0:
        dict_item = dq.popleft()
        if key in dict_item:
            return dict_item[key]
        for key_, value in dict_item.items():
            if isinstance(value, dict):
                dq.append(value)

    raise KeyError(f"{key} not found")


if __name__ == "__main__":
    import doctest

    doctest.testmod()