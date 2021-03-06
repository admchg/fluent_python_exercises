#!/usr/bin/env python
# coding: utf-8

# # Chapter 1 Exercises
# 
# (Adam)
# 
# Nothing too complex or interesting, but good practice with the Python data/object model.

# ## Problem 1
# 
# Write a Binary class that can be called with Binary(n), where n is an integer. The only attribute the class may have is a text representation of n in binary, so you should not save n except as a string representing n in binary. 
# 
# The representation of Binary(n) should be the string, e.g. str(Binary(7)) = "111".
# 
# Finally, the class must support addition with another Binary object, and multiplication with an integer. All operations should be done without needing to convert anything; int("0") or int("1") is fine. In both cases, you should return a Binary object.
# 
# No libraries are needed.
# 
# Don't worry about dealing with zero!

# In[ ]:


class Binary:
    def __init__(self, n):
        pass
        
    def __repr__(self):
        pass
    
    def __add__(self, other):
        pass
    
    def __mul__(self, integer):
        pass


# ## Problem 1 Test Cases

# In[ ]:


import numpy as np

def test():
    x = np.random.randint(1, 1000, size=500)
    y = np.random.randint(1, 1000, size=500)
    z = x + y
    w = x * y
    
    if not all([str(Binary(i)) == np.binary_repr(i) for i in x]):
        return "Failed"
    
    if not all([str(Binary(x[k]) + Binary(y[k])) == np.binary_repr(z[k]) for k in range(500)]):
        return "Failed"
    
    if not all([str(Binary(x[k]) * y[k]) == np.binary_repr(w[k]) for k in range(500)]):
        return "Failed"
    
    return "Passed"

