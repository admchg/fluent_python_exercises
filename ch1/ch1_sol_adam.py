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
# Finally, the class must support addition with another Binary object, and multiplication with an integer. All operations should be done without needing to convert anything. In both cases, you should return a Binary object.
# 
# No libraries are needed.
# 
# Don't worry about dealing with zero!

# In[ ]:


class Binary:
    def __init__(self, n):
        self.text = ""
        
        while n:
            quotient = int(n / 2)
            remainder = str(n % 2)
            
            self.text = remainder + self.text
            n = quotient
        
    def __repr__(self):
        return self.text
    
    def __add__(self, other):
        a = self.text
        b = other.text
        
        result = ""
        carry = 0
        
        while a and b:
            digit = int(a[-1]) + int(b[-1]) + carry
            result = str(digit % 2) + result
            carry = int(digit / 2)
            
            a = a[:-1]
            b = b[:-1]
            
        while a:
            digit = int(a[-1]) + carry
            result = str(digit % 2) + result
            carry = int(digit / 2)
            
            a = a[:-1]
        while b:
            digit = int(b[-1]) + carry
            result = str(digit % 2) + result
            carry = int(digit / 2)
            
            b = b[:-1]
        if carry:
            result = str(carry) + result
        
        return result
    
    def __mul__(self, integer):
        a = self.text
        result = ""
        carry = 0
        
        while a:
            digit = integer * int(a[-1]) + carry
            result = str(digit % 2) + result
            carry = int(digit / 2)
            
            a = a[:-1]
            
        while carry:
            result = str(carry % 2) + result
            carry = int(carry / 2)
                
        return result


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

