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

    >>> list(my_enumerate(None))
    Traceback (most recent call last):
        ...
    TypeError: 'NoneType' object is not iterable
    """

    i = 0
    for item in iterable:
        yield item, i
        i += 1


# Exercise 2
# The built-in function zip(it_1, ..., it_n) yields n-tuples, taking items from the iterables in parallel. Write your
# own function piz that yields n-tuples that are the reverse order of tuples from zip (i.e., you'd go right-to-left in the
# iterables, not changing the order of the iterables).
def piz(*iterables):
    """
    >>> list(piz([1,2,3], [4,5,6], [7,8,9,10]))
    [(7, 4, 1), (8, 5, 2), (9, 6, 3)]

    >>> list(piz("idinsight", "hnisolnso"))
    [('h', 'i'), ('n', 'd'), ('i', 'i'), ('s', 'n'), ('o', 's'), ('l', 'i'), ('n', 'g'), ('s', 'h'), ('o', 't')]

    >>> list(piz(range(5), range(10, 5, -1)))
    [(10, 0), (9, 1), (8, 2), (7, 3), (6, 4)]
    """

    iterators = [iter(i) for i in reversed(iterables)]
    while iterators:
        result = []
        sentinel = object()
        for it in iterators:
            elem = next(it, sentinel)
            if elem is sentinel:
                return
            result.append(elem)
        yield (tuple(result))


if __name__ == "__main__":
    import doctest

    doctest.testmod()
