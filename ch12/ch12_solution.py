## Q1: Here are a bunch of classes. Refactor them taking into account the 8 principles
##     under "Coping with Multiple Inheritance" on page 362. You are welcome to change
##     anything you like and add additional classes etc. - I'm hoping this
##     makes for a healty discussion on inheritance and design choices.

from abc import ABC, abstractmethod


class LivingThing(ABC):
    def __init__(self, name):
        self.name = name

    def birth(self):
        print("f{self} is born")

    def death(self):
        print("f{self} is dead")

    def __repr__(self):
        return self.name

    @abstractmethod
    def give_birth(self):
        pass


class ThingsThatMove2dMixin:
    def move_left(self):
        print(f"{self} moves left")

    def move_right(self):
        print(f"{self} moves right")

    def move_forward(self):
        print(f"{self} moves forward")

    def move_backward(self):
        print(f"{self} moves backward")


class ThingsThatMove3dMixin(ThingsThatMove2dMixin):
    def move_up(self):
        print(f"{self} moves up")

    def move_down(self):
        print(f"{self} moves up")


class ThingsThatBirthYoungMixin:
    def give_birth(self):
        print(f"{self} birthed a baby")

    def suckle_young(self):
        print(f"{self} suckled young")


class ThingsThatLayEggsMixin:
    def give_birth(self):
        print(f"{self} laid an egg")


## Q2: create the following subclasses
### Q2.1
class Peacock(ThingsThatMove3dMixin, ThingsThatLayEggsMixin, LivingThing):
    # Shoukd also dance in the rain
    pass


### Q2.2
class Bat(ThingsThatMove3dMixin, ThingsThatBirthYoungMixin, LivingThing):
    # It's a weird mammal
    pass


### Q2.3
class Platypus(
    ThingsThatMove3dMixin,
    ThingsThatLayEggsMixin,
    ThingsThatBirthYoungMixin,
    LivingThing,
):
    # Lol. Good luck.
    pass


### Q2.4
class Whale(ThingsThatMove3dMixin, ThingsThatBirthYoungMixin, LivingThing):
    # Can move in all directions in water
    pass


### Q2.5
class Human(ThingsThatMove2dMixin, ThingsThatBirthYoungMixin, LivingThing):
    # Should also pay taxes
    def pay_taxes(self):
        print("$$ ->")
