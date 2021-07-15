import numpy as np

# This homework problem focuses on some new decorators introduced: property, staticmethod, and classmethod
# In particular, addressing the author's comments, I thought about reasons why staticmethods might be useful and this is what I got

# In the readings, the main example is the vect class. Let's build on this.
# A vector is an element of a vector space.
# Instead of just creating a class for vectors, we will create a category of vector spaces
# Each object in this category will be a vector space and morphisms will be linear maps (matrices). We can compose maps by multiplying matrices
# Vector spaces are essentially the same up to dimension (any two real vector spaces are "isomorphic" is they have the same dimension)
# This means the category FinVect can be specified just by specifying matrices


class FinVect(np.ndarray):
    def __new__(cls, input_array, info=None):

        obj = np.asarray(input_array).view(cls)
        assert len(obj.shape) == 2

        return obj

    @property
    def dom(self):
        """ Return the domain of the matrix (cols)"""
        return self.shape[1]

    @property
    def cod(self):
        """ Return the codomain of the matrix (rows)"""
        return self.shape[0]

    # Add two staticmethods to FinVect.
    # The first should take an integer n (representing a vector space of dimension n)
    # It should return a matrix which takes any vector space of dimension n to itself
    # i.e. some M such that Mx = x for x in some n dimensional vector space

    @staticmethod
    def idd(n):
        return FinVect(np.eye(n))

    # The second should implement matrix multiplication
    # i.e. take two matrices f and g then multiply them together

    @staticmethod
    def compose(f, g):
        return f @ g

    # A matrix is injective if the rank is the same dimension as the domain (this means if M*x = 0, then x =  0)
    # A matrix is surjective if the rank is the same dimension as the codomain
    # (this means for each y in the target space, there exists an x in the source space such that Mx = y)
    # Create a Boolean attribute for indicating whether the matrix is injective

    @property
    def monic(self):
        return np.linalg.matrix_rank(self) == self.dom

    # Create a Boolean attribute for indicating whether the matrix is surjective

    @property
    def epi(self):
        return np.linalg.matrix_rank(self) == self.cod

    # An initial object is a vector space which has a unique map to every other vector space
    # A terminal object is a vector space which has a unique map from every other vector space
    # In finite dimensional vector spaces, the initial and terminal objects are the same.
    # What is this vector space?

    # Create a classmethod which return the dimension of this vector space as well as the unique map to (matrix)
    @classmethod
    def initial(cls):
        return 0, lambda x: FinVect(np.ones((0, x)))

    # Create a classmethod which return the dimension of this vector space as well as the unique map from (matrix)
    @classmethod
    def terminal(cls):
        return 0, lambda x: FinVect(np.ones((x, 0)))

    # Challenge
    # If I have two vector spaces U, V with dimensions m and n respectively
    # We can create a new product vector space:
    # U x V = {(u,v) | u \in U and v \in V}
    # There are matrices p: U x V -> U such that p(u,v) = u and q: U x V -> V such that q(u,v) = v
    # This product space has the special property that:
    # For any other vector space X with dimension k with a map f:X -> U and g:X -> V (f is a k x m matrix, g is a k x n matrix)
    # Then there is a unique matrix s such that:
    # f = p @ s and g = q @ s
    # Write a staticmethod which returns the dimension of U x V and a function which generates the unique map s

    @staticmethod
    def product(m, n):
        d = m + n  # dimension
        p = FinVect(np.hstack([np.eye(m), np.zeros((m, n))]))
        q = FinVect(np.hstack([np.zeros((n, m)), np.eye(n)]))

        def universal_property(f, g):
            assert f.dom == g.dom

            s = np.vstack([f, g])

            assert np.allclose(p @ s, f)
            assert np.allclose(q @ s, g)
            return s

        return d, universal_property
