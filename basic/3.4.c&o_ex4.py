"""
class calculator:
    def __init__(self, a, b):
        self.num1 = a
        self.num2 = b
    def add(self):
        print(f"Addition of {self.num1} and {self.num2} is"+ str(self.num1 + self.num2))
    def sub(self):
        print(f"subraction of {self.num1} and {self.num2} is "+ str(self.num1 - self.num2))
    def mul(self):
        print(f"multiplication of {self.num1} and {self.num2} is "+ str(self.num1 * self.num2))
    def div(self):
        print(f"division of {self.num1} and {self.num2} is "+ str(self.num1 / self.num2))

number = calculator(4, 2)

number.add()
number.sub()
number.div()
number.mul()

"""
class calculator:
    def add(self,a, b):
        print("Add", a+b)

obj1=calculator()

obj1.add(5, 4)