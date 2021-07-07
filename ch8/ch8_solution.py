import random
import weakref
import numpy as np

# Qa: Write a function that takes a 1d array or list and returns the weighted average
# of each term and its immediate neighbours. Neighbours are given half the weight.
# - If `inplace` is True, then it should update the argument variable.
# - Output should be the same length as input
# - First and last terms only have 1 neighbour
#
# E.g. If a = [1, 2, 3, 4], smooth_vector(a) => [1.3333, 2, 3, 3.6667]
#
# Hint: see np.convolve


def smooth_vector(a, inplace=False):
    if len(a) < 3:
        raise ValueError("`a` should be at least of length 3")

    denominator = np.full_like(a, 2.0, dtype="float")
    denominator[-1] = 1.5
    denominator[0] = 1.5
    numerator = np.convolve([0.5, 1, 0.5], a, "same")

    if inplace:
        a[:] = numerator / denominator
    else:
        a = numerator / denominator
    return a


# Qb: You are writing a MMORPG called Fiablo. You boss wants the following functionality
# 1. We want to create an NPC called Deckard Cain.
# 2. This character can have a random age between 20 and 80, and can be either male or
#    female
# 3. Every user should see the same Deckard Cain. So if user1 and user2 are both
#    interacting with Deckard Cain, they should both see the same age and gender.
# 4. If no one is interacting with Deckard Cain, we should use this opportunity to
#    change his appearance - next user interacting should get a new age and
#    gender.
#
# After some thinking, you realise that this calls for a Singleton design pattern with
# a twist. You remember reading about `weakref` as part of this really good looking
# reading group while at IDinsight and feel that might make sense here.


class DeckardCain:
    class _DeckardCain:
        def __init__(self):
            self.age = random.randint(a=20, b=80)
            self.gender = random.choice(["m", "f"])

        def __repr__(self):
            return f"DeckardCain({self.age}, {self.gender})"

    instance = None

    def __new__(cls):
        DeckardCain.users_referencing = weakref.getweakrefcount(DeckardCain.instance)
        if (not DeckardCain.instance) or (DeckardCain.users_referencing == 0):
            DeckardCain.instance = DeckardCain._DeckardCain()
        return weakref.proxy(DeckardCain.instance)

    def __getattr__(self, name):
        return __getattr__(self.instance, name)

    def __setattr__(self, name):
        return __setattr__(self.instance, name)

    def __repr__(self):
        return self.instance.__repr__()
