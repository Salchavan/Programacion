class Animal:
    def eat(self):
        print("The animal is eating")
class Mammal(Animal):
    def breastfeed(self):
        print("The animal is nursing her calf")
class Bird(Animal):
    def fly(self):
        print("The bird is flying")
class Bat(Mammal, Bird):
    pass

n = Bat()

n.breastfeed()