# # Ch 7 Problem

# At a fictional company, you have way too many meetings
# (labeled $0, \dots, n-1$) scheduled this week.
#
# The meetings take time given by meeting_hours = $[h_0, \dots, h_{n-1}]$.
# There are too many, so you can't attend all of them, but many are useful,
# with value given by array meeting_useful = $[u_0, \dots, u_{n-1}]$.
#
# If you start with total hours $t=20$, what's the maximum amount of
# usefulness you can get from your meetings?

# ## Part 1

# Fill in the function recursive_solution, to return the maximum usefulness
# you can get from your meetings, starting with total hours t
#
# Your function should be purely recursive, meaning:
# - There should not be any inner functions
# - There should not be any data structures
#
# Don't change the function signature! Avoid list splicing; use index instead.
# Also, we need to use keyword arguments here - you'll see why.

meeting_hours = [1, 1.5, 1.5, 1.5, 2, 2, 2.5, 2.5, 3] * 3
meeting_useful = [1, 0, 2, 1, 4, 2, 2, 3, 3] * 3


def recursive_solution(*, t, index):  # DON'T CHANGE FUNCTION SIGNATURE
    pass


recursive_solution(t=20, index=0)


# ## Part 2 - Write a decorator!
#
# Write a decorator count_calls to count the total number of times that your
# recursive_solution is called.
# Hint: since functions are objects, you can add attributes!
#
# Add it to your function above.
# Don't change anything else in the original function!
#
# How many times was recursive_solution called for the inputs above?


def count_calls(func):
    return func


recursive_solution(t=20, index=0)
print(recursive_solution.call_count)


# ## Part 3 - Write another decorator!
#
# Now write a decorator memoize to memoize recursive_solution!
#
# Add it to your function above. Again, do not modify anything in
# recursive_solution. And don't just use lru_cache!
#
# How many calls, if you memoize?


def memoize(func):
    return func


recursive_solution(t=20, index=0)
print(recursive_solution.call_count)
