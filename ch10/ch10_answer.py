# In the reading, we saw a multi-dimensional vector (Vector) that could take a list of floats
# Now, let's create a list of complex numbers called ComplexList and make it Pythonic.
# We will use Python's built-in support for complex numbers.

import reprlib
import functools
import operator
import numbers
import math


class ComplexList:

    # Q1: Initialize a list of complex numbers
    def __init__(self, components):
        self._components = [complex(el) for el in components]
        # self._components = np.array(components,dtype=complex)

    def __iter__(self):
        return iter(self._components)

    # Q2: Use the reprlib to provide size limits for the representations of the list
    # such that only the first 4 complex numbers in the list are fully visible
    def __repr__(self):
        myRept = reprlib.Repr()  # Create Repr object
        myRept.maxlist = 4  # This limit is used to control the size of list
        components = myRept.repr(self._components)
        components = components[1:-1]
        return "ComplexList({})".format(components)

    def __str__(self):
        return str(tuple(self))

    def __len__(self):
        return len(self._components)

    # Q3: Write the condition for equality between elements of 2 ComplexLists
    def __eq__(self, other):
        return (
            len(self) == len(other)
            and all(a.real == b.real for a, b in zip(self, other))
            and all(a.imag == b.imag for a, b in zip(self, other))
        )

    def __hash__(self):
        hashes = (hash(x) for x in self)
        return functools.reduce(operator.xor, hashes, 0)

    # Q4: Let's define the abs of ComplexList as the sum of individual distances from origin
    def __abs__(self):
        return sum(abs(x) for x in self)

    def __bool__(self):
        return bool(abs(self))

    # Q5: Just like Vector(), ComplexList __getitem__ should support indexing and slicing.
    # In addition, it should optionally take another argument as 'real', 'imag', 'abs'
    # and should be able to return real, imaginary and origin-distance lists.
    def __getitem__(self, index):
        if isinstance(index, tuple):
            index, part = index
        else:
            part = None

        if part == "real":
            lst = [el.real for el in self._components]
        elif part == "imag":
            lst = [el.imag for el in self._components]
        elif part == "abs":
            lst = [abs(el) for el in self._components]
        elif part is None:
            lst = self._components
        else:
            raise TypeError("'part' not recognized.")
        cls = type(self)
        if isinstance(index, slice):
            if part is None:
                return cls(lst[index])
            else:
                return lst[index]
        elif isinstance(index, numbers.Integral):
            return lst[index]
        else:
            msg = "{.__name__} indices must be integers"
            raise TypeError(msg.format(cls))

    # Q6. Write functions to return list of phases and conjugates
    def phase(self):
        r = [math.atan(num.imag / num.real) for num in self]
        return r

    def conjugate(self):
        r = [num.conjugate() for num in self]
        return r

    # Bonus Q: Generate byte representation of complex numbers and write the bytes constructor.
    def __bytes__(self):
        return bytes(self._components)

    @classmethod
    def frombytes(cls, octets):
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(memv)


"""
A list of complex numbers ``Complex`` class

Expected behavior:
Q1: Initialization

 >>> ComplexList([3.1, 4.2])
 ComplexList([(3.1+0j), (4.2+0j))
 
 >>> ComplexList((3, 4, 5))
 ComplexList([(3+0j), (4+0j), (5+0j))

 >>> ComplexList([1+2j, 3+4j, 6-7j])
 ComplexList([(1+2j), (3+4j), (6-7j))
 
Q2: Show only first 4 items upon print
 >>> ComplexList(range(10))
 ComplexList([0j, (1+0j), (2+0j), (3+0j), ...)
 
 
Q3: Equality between lists
 >>> ComplexList([1+2j, 3+4j, 6-7j]) == ComplexList([1+2j, 3+4j, 6-7j])
 True
 
 >>> ComplexList([1+2j, 3+4j, 6-7j]) == ComplexList([3+4j, 1+2j, 6-7j])
 False
 
Q4: abs
 >>> abs(ComplexList([1+2j, 3+4j, 6-7j]))
 16.455612434792677

Q5: __getitem__

 >>> vec = ComplexList([1+2j, 3+4j, 6-7j])
 >>> vec[2]
 (6-7j)
 >>> vec[1:2]
 ComplexList([(3+4j))
 >>> vec[0, 'real']
 1.0
 >>> vec[2, 'imag']
 -7.0
 >>> vec[1,'abs']
 5.0
 >>> vec[0:2, 'abs']
 [2.23606797749979, 5.0]

Q6: phase and conjugate

 >>> ComplexList([1+2j, 3+4j, 6-7j]).phase()
 [1.1071487177940904, 0.9272952180016122, -0.8621700546672264]
 
 >>> ComplexList([1+2j, 3+4j, 6-7j]).conjugate()
 [(1-2j), (3-4j), (6+7j)]
"""
