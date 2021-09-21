"""
Chapter 14 Problem Set
Adam
"""

# Exercise 1
# The built-in function enumerate(iterable) returns 2-tuples of the form (index, item) over items in the iterable.
# Write your own function my_enumerate that returns 2-tuples of the form (item, index).
def my_enumerate(iterable):
    """
    >>> list(my_enumerate("idinsight"))
    [('i', 0), ('d', 1), ('i', 2), ('n', 3), ('s', 4), ('i', 5), ('g', 6), ('h', 7), ('t', 8)]

    >>> list(my_enumerate(["Hello"]))
    [('Hello', 0)]

    >>> list(enumerate(None))
    Traceback (most recent call last):
        ...
    TypeError: 'NoneType' object is not iterable
    """
    for i, j in enumerate(iterable):
        yield (j,i)
    return


# Exercise 2
# The built-in function zip(it_1, ..., it_n) yields n-tuples, taking items from the iterables in parallel. Write your
# own function piz that yields n-tuples that are the reverse order of tuples from zip (i.e., you'd go right-to-left in the
# iterables, not changing the order of the iterables).
def piz(*iterables):
    """
    >>> list(piz([1,2,3], [4,5,6], [7,8,9,10]))
    [(7,4,1), (8,5,2), (9,6,3)]

    >>> list(piz("idinsight", "hnisolnso"))
    [('h', 'i'), ('n', 'd'), ('i', 'i'), ('s', 'n'), ('o', 's'), ('l', 'i'), ('n', 'g'), ('s', 'h'), ('o', 't')]
    """
    zipped_list = zip(*iterables)
    for item in zipped_list:
        yield item[::-1]
    return


if __name__ == "__main__":
    import doctest

    doctest.testmod()
