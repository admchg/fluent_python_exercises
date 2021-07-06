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

    # Write code here
    # I REFUSE to use convolve
    z = np.array(a)
    ahead = np.concatenate([z[1:], [0]])
    ahead = np.concatenate([[ahead[0] * (1 / 3)], ahead[1:] * 0.25])
    behind = np.concatenate([[0], z[:-1]])
    behind = np.concatenate([behind[:-1] * 0.25, [behind[-1] * (1 / 3)]])
    z = np.concatenate([[(2 / 3) * z[0]], 0.5 * z[1:-1], [(2 / 3) * z[-1]]])
    smoothed = z + ahead + behind

    if inplace:
        a[:] = smoothed
        return a
    else:
        return smoothed


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

    instance = weakref.WeakValueDictionary()  # None

    def __new__(cls):

        # # Write code here
        if cls not in cls.instance.keys():
            instance = cls._DeckardCain()
            cls.instance[cls] = instance
        return weakref.ref(cls.instance[cls])()
        # if cls.instance is None:
        #     cls.instance = weakref.ref(cls._DeckardCain())
        # return cls.instance()()

    def __getattr__(self, name):
        return __getattr__(self.instance, name)

    def __setattr__(self, name):
        return __setattr__(self.instance, name)

    def __repr__(self):
        return self.instance.__repr__()


a = DeckardCain()