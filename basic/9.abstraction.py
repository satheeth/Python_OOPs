# Abstract class: A class that cannot be installed on its own; Meant to be subclassed.
#                 They can contain abstract methods, which are declared but have no implementation
#                 Abstracct classes benefits:
#                 1. Prevents instantiation of the class itself
#                 2. Rrequires children to use inherited abstract methods

from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):
    def go(self):
        print("You drive the car")

    def stop(self):
        print("you stop the car")

class Motorcycle(Vehicle):

    def go(self):
        print("you ride the motorcycle")

    def stop(self):
        print("You stop the motorCycle")

class Boat(Vehicle):
    def go(self):
        print("you sail the boat")

    def stop(self):
        print("You anchor boat")

boat = Boat()
boat.go()
boat.stop()

boat = Boat()