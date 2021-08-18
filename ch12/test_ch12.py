import pytest

from ch12_solution import Peacock, Bat, Platypus, Whale, Human


@pytest.fixture
def peacock():
    return Peacock("P")


@pytest.fixture
def bat():
    return Bat("B")


@pytest.fixture
def platypus():
    return Platypus("PL")


@pytest.fixture
def whale():
    return Whale("Moby Dick")


@pytest.fixture
def human():
    return Human("Ahab")


@pytest.mark.parametrize(
    "three_d_mover", pytest.lazy_fixture(("peacock", "bat", "whale"))
)
def test_objects_can_move_up_down(three_d_mover):
    assert hasattr(three_d_mover, "move_up")
    assert hasattr(three_d_mover, "move_down")


def test_human_can_only_move_2d(human):
    assert not hasattr(human, "move_up")
    assert not hasattr(human, "move_down")


def test_human_pay_taxes(human):
    assert hasattr(human, "pay_taxes")


@pytest.mark.parametrize(
    "non_human", pytest.lazy_fixture(("peacock", "bat", "whale", "platypus"))
)
def test_nonhumans_dont_pay_taxes(non_human):
    assert not hasattr(non_human, "pay_taxes")


@pytest.mark.parametrize(
    "two_d_mover", pytest.lazy_fixture(("peacock", "bat", "whale", "platypus", "human"))
)
def test_objects_can_move2d(two_d_mover):
    assert hasattr(two_d_mover, "move_backward")
    assert hasattr(two_d_mover, "move_forward")
    assert hasattr(two_d_mover, "move_right")
    assert hasattr(two_d_mover, "move_left")


def test_weird_platypus(platypus):
    assert hasattr(platypus, "suckle_young")
    assert platypus.give_birth() == "PL laid an egg"
