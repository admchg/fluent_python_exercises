from ch8_problem import DeckardCain, smooth_vector

import pytest
import numpy as np


class TestQuestionA:
    @pytest.fixture
    def a_np(self):
        return np.array([1, 2, 3, 4])

    @pytest.fixture
    def b_list(self):
        return [1, 2, 3, 4]

    def test_numpy_not_in_place(self, a_np):
        output = smooth_vector(a_np)
        assert not np.allclose(output, a_np)

    def test_numpy_in_place(self, a_np):
        output = smooth_vector(a_np, inplace=True)
        assert np.allclose(output, a_np)
        assert type(output) == type(a_np)

    def test_list_not_in_place(self, b_list):
        output = smooth_vector(b_list)
        assert not np.allclose(output, b_list)

    def test_list_in_place(self, b_list):
        output = smooth_vector(b_list, inplace=True)
        assert np.allclose(output, b_list)
        assert type(output) == type(b_list)


class TestQuestionB:
    def test_same_object_returned(self):
        """
        Subsequent calls return the same object if the 1st one is alive
        """
        dc1 = DeckardCain()
        dc2 = DeckardCain()

        assert dc1 is dc2

    def test_creates_new_obj(self):
        """
        Subsequent calls return a new object if there are no proxies
        """
        dc1 = DeckardCain()
        dc2 = DeckardCain()

        age1, gender1 = dc1.age, dc1.gender

        del dc1
        del dc2

        dc3 = DeckardCain()

        assert (dc3.gender != gender1) or (dc3.age != age1)

    def test_make_copy_new_obj(self):
        """
        Making a copy and deleting the original references still
        maintains the proxy
        """

        dc1 = DeckardCain()
        dc2 = DeckardCain()

        dc3 = dc2

        del dc1
        del dc2

        dc4 = DeckardCain()

        assert dc4 is dc3

    def test_delete_copy_new_obj(self):
        """
        Deleting the instance and copies leads to new instance being
        created
        """
        dc1 = DeckardCain()
        dc2 = DeckardCain()

        dc3 = dc2

        age1, gender1 = dc1.age, dc1.gender

        del dc1
        del dc2
        del dc3

        dc4 = DeckardCain()

        assert (dc4.gender != gender1) or (dc4.age != age1)
