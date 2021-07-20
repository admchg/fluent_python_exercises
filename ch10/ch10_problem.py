# In the reading, we saw a multi-dimensional vector (Vector) that could take a list of floats
# Now, let's create a list of complex numbers called ComplexList and make it Pythonic.
# We will use Python's built-in support for complex numbers.

import reprlib
import functools
import operator
import numbers
import math
import numpy as np
from functools import reduce

"""
A list of complex numbers ``ComplexList`` class

Expected behavior:

Q1: Initialization


Q2: Show only first 4 items upon print

Q3: Equality between lists

Q4: abs: sum of individual magnitudes
Q5: __getitem__ should support 'real', 'imag' and 'abs'


Q6: phase and conjugate


"""


class ComplexList:

    r = reprlib.Repr()
    r.maxlist = 4

    # Q1: Initialize a list of complex numbers
    def __init__(self, components):
        """
        >>> ComplexList([3.1, 4.2])
        ComplexList((3.1+0j), (4.2+0j))

        >>> ComplexList((3, 4, 5))
        ComplexList((3+0j), (4+0j), (5+0j))

        >>> ComplexList([1+2j, 3+4j, 6-7j])
        ComplexList((1+2j), (3+4j), (6-7j))

        >>> ComplexList([1+2j, 4, 2-2j, 5.0j, 2-5j])
        ComplexList((1+2j), (4+0j), (2-2j), 5j, ...)

        >>> ComplexList(range(10))
        ComplexList(0j, (1+0j), (2+0j), (3+0j), ...)

        """
        self._components = [complex(c) for c in components]

    def __iter__(self):
        return iter(self._components)

    # Q2: Use the reprlib to provide size limits for the representations of the list
    # such that only the first 4 complex numbers in the list are fully visible
    def __repr__(self):
        components = self.r.repr(list(self))
        components = components[components.find("[") + 1 : components.find("]")]
        return "ComplexList({})".format(components)

    def __str__(self):
        return str(tuple(self))

    def __len__(self):
        return len(self._components)

    # Q3: Write the condition for equality between elements of 2 ComplexLists
    def __eq__(self, other):
        """
        >>> ComplexList([1+2j, 3+4j, 6-7j]) == ComplexList([1+2j, 3+4j, 6-7j])
        True

        >>> ComplexList([1+2j, 3+4j, 6-7j]) == ComplexList([3+4j, 1+2j, 6-7j])
        False
        """
        return self._components == other._components

    def __hash__(self):
        hashes = (hash(x) for x in self)
        return functools.reduce(operator.xor, hashes, 0)

    # Q4: Let's define the abs of ComplexList as the sum of individual distances from origin
    def __abs__(self):
        """
        >>> abs(ComplexList([1+2j, 3+4j, 6-7j]))
        16.455612434792677
        """
        return reduce(operator.add, map(abs, self), 0)

    def __bool__(self):
        return bool(abs(self))

    # Q5: Just like Vector(), ComplexList __getitem__ should support indexing and slicing.
    # In addition, it should optionally take another argument as 'real', 'imag', 'abs'
    # and should be able to return real, imaginary and origin-distance lists.
    def __getitem__(self, index):
        """
        >>> vec = ComplexList([1+2j, 3+4j, 6-7j])
        >>> vec[2]
        (6-7j)
        >>> vec[1:2]
        ComplexList((3+4j))
        >>> vec[0, 'real']
        1.0
        >>> vec[2, 'imag']
        -7.0
        >>> vec[1,'abs']
        5.0
        >>> vec[0:2, 'abs']
        [2.23606797749979, 5.0]
        """
        cls = type(self)
        if isinstance(index, tuple):
            slice_obj, op = index
            op = getattr(np, op)
        else:
            slice_obj = index
            op = None

        if isinstance(slice_obj, slice):
            if op is None:
                return cls(self._components[slice_obj])
            else:
                return [op(c) for c in self._components[slice_obj]]
        elif isinstance(slice_obj, numbers.Integral):
            if op is None:
                return self._components[slice_obj]
            else:
                return op(self._components[slice_obj])
        else:
            msg = "{cls.__name__} indices must be integral"
            raise TypeError(msg.format(cls=cls))

    # Q6. Write functions to return list of phases and conjugates
    def phase(self):
        """
        >>> ComplexList([1+2j, 3+4j, 6-7j]).phase()
        [1.1071487177940904, 0.9272952180016122, -0.8621700546672264]
        """
        return [math.atan2(x.imag, x.real) for x in self]

    def conjugate(self):
        """
        >>> ComplexList([1+2j, 3+4j, 6-7j]).conjugate()
        [(1-2j), (3-4j), (6+7j)]
        """
        return [x.conjugate() for x in self]

    # Bonus Q: Generate byte representation of complex numbers and write the bytes constructor.
    def __bytes__(self):
        return [bytes([x.real, x.imag]) for x in self._components]

    @classmethod
    def frombytes(cls, octets):
        return 0  ##


if __name__ == "__main__":
    import doctest

    doctest.testmod()
