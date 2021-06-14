# Chapter 5 Exercises
# By: Jeenu

# Note: All required libraries have been imported
import numpy as np
import random
from functools import partial

# ---------------------------------
# 1.a Write a function 'sum_n_integers' to find the sum of N integers.
# 1.b Write another function 'sum_n_lists' to find the elementwise sum of N lists using Python map and 
# the 'sum_n_integers' function you created in 1.a.

def sum_n_integers(
	# fill
):


def sum_n_lists(
	# fill
):


# ---------------------------------
# 2.a Create your own callable `random_fibonacci_generator` object which gives you a random fibonacci number 
# in the range (0, N) where N is an argument passed into the object.

class random_fibonacci_generator:
    """
    Generate a random fibonacci number in 0 to N
    """
    
    def __init__(self, N):



# ---------------------------------
# 3.a Create function 'power' using lambda. Arguments: x and n. Returns: x^n.
# 3.b Create partial functions 'square' and 'cube' using the 'power' function you created in 3.a to return 
# square and cube of a number respectively.
# 3.c Write a function 'calculate' with arguments: function name (square/cube) and a number (N). Returns 
# the result of N^2 or N^3 depending on function name argument.

power = 
square =
cube = 

def calculate(
	# fill
):


# ---------------------------------
# 4.a Create function 'create_group' with:
#   - one required argument: 'name', 
#   - one keyword argument: 'created_on' with default set to None
#   - optional positional arguments: 'founders'
#   - optional keyword arguments 'tags'
# Returns a dictionary with keys: 'name', 'founders', 'created_on' and other passed in keyword arguments 

def create_group(
	# fill
):



if __name__ == "__main__":

	# ---------------------------------
	# Test 1
	N = 10
	list_1 = np.random.randint(0, 100, N)
	list_2 = np.random.randint(0, 100, N)
	list_3 = np.random.randint(0, 100, N)

	summed_list = [x + y for x, y in zip(list_1, list_2)]
	assert(list(sum_n_lists(list_1, list_2)) == summed_list)

	summed_list = [x + y + z for x, y, z in zip(list_1, list_2, list_3)]
	assert(list(sum_n_lists(list_1, list_2, list_3)) == summed_list)

	# ---------------------------------
	# Test 2
	random_fib = random_fibonacci_generator(80)
	assert(random_fib() in [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55])

	# ---------------------------------
	# Test 3
	assert(calculate(square, 30) == 900)
	assert(calculate(cube, 10) == 1000)

	# ---------------------------------
	# Test 4
	result = {'name': "Dumbledore's Army",'founders': ('Harry Potter', 'Hermoine Granger', 'Ron Weasley'),'created_on': None, 'group_type': 'secret', 'purpose': 'PD','location': 'Room of Requirement'}
	assert(create_group("Dumbledore's Army", 'Harry Potter', 'Hermoine Granger', 'Ron Weasley', group_type='secret', purpose='PD', location='Room of Requirement') == result)


