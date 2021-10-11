# Chapter 17

from concurrent import futures
import math
import os
import time
import random

# 1: Complete the functions `create_folders` using the function `create_each_folder_sleepily` and 
# concurrent.futures
# Compare this with a sequential execution to check if you are getting any performance gains 

def create_each_folder_sleepily(path):
    """
    Function to create a folder in the given path
    """
    time.sleep(5)
    os.mkdir(path)


def create_folders(path_array):
    """
    Function to create the folders parallely
    """
    return len(path_array)


# Exercise 2: Write a function `count_primes` to count the number of prime numbers in a given list 
# and return that count, using concurrent.futures
# Compare this with a sequential execution to check if you are getting any performance gains 

def count_primes(n_array):
    """
    >>> count_primes([10, 11, 39, 101])
    2
    
    >>> count_primes([10, 13, 39, 113, 1087, 2209, 9409, 36481, 78233])
    4
    
    >>> count_primes([112272535095293, 9985805041, 1099726899285419])
    1
    
    """
    pass


if __name__ == "__main__":

	# 1
	parent_folder = os.getcwd() + '/test' + str(random.randint(0, 10000))
	os.mkdir(parent_folder)
	path_array = [parent_folder + '/' + str(x) for x in range(0, 10)]

	t0 = time.time()
	create_folders(path_array)
	elapsed = time.time() - t0
	print(f"""Function create_folders run in {round(elapsed, 2)} seconds.""")

    # 2
    t0 = time.time()
    count = count_primes([112272535095293, 9985805041, 1099726899285419])
    elapsed = time.time() - t0
    print(f"""Function count_primes run in {round(elapsed, 2)} seconds.""")
    assert(count == 1)

    
