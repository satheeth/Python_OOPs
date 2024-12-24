class Animal():
    def sound(self):
        print("Animal makes sound")

class dog(Animal):
    def sound(self):
        print("Dog bark's")

class bird(Animal):
    def sound(self):
        print("Bird's sound")


d1 = dog()
d1.sound()
b1 = bird()
b1.sound()
