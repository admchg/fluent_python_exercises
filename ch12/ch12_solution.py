## Q1: Here are a bunch of classes. Refactor them taking into account the 8 principles
##     under "Coping with Multiple Inheritance" on page 362. You are welcome to change
##     anything you like and add additional classes etc. - I'm hoping this
##     makes for a healty discussion on inheritance and design choices.


class LivingThing:
    def __init__(self, name):
        self.name = name

    def birth(self):
        print("f{self} is born")

    def death(self):
        print("f{self} is dead")


class ThingsThatMove:
    def move_left(self):
        print(f"{self} moves left")

    def move_right(self):
        print(f"{self} moves right")

    def move_forward(self):
        print(f"{self} moves forward")

    def move_backward(self):
        print(f"{self} moves backward")


class ThingsThatFly(ThingsThatMove):
    def move_up(self):
        print(f"{self} moves up")

    def move_down(self):
        print(f"{self} moves up")


class ThingsThatBirthYoung:
    def give_birth(self):
        print("f{self} birthed a baby")

    def suckle_young(self):
        print("f{self} suckled young")


class ThingsThatLayEggs:
    def give_birth(self):
        print(f"{self} laid an egg")


class Mammal(LivingThing, ThingsThatMove):
    def __repr__(self):
        return f"Animal[{self.name}]"


class Bird(LivingThing, ThingsThatFly, ThingsThatLayEggs):
    def __repr__(self):
        return f"Bird[{self.name}]"


## Q2: create the following subclasses
### Q2.1
class Peacock(Bird):
    # Shoukd also dance in the rain
    pass


### Q2.2
class Bat(Mammal):
    # It's a weird mammal
    pass


### Q2.3
class Platypus(Mammal):
    # Lol. Good luck.
    pass


### Q2.4
class Whale(Mammal):
    # Can move in all directions in water
    pass


### Q2.5
class Human(Mammalbe):
    # Should also pay taxes
    pass
