class a():
    def __init__(self):
        print("A")

    def display(self):
        print("You are in a class a")

class b():
    def __init__(self):
        super().__init__()
        print("B")
    def display(self):
        print("you are in a class b")

class c(b,a):
    def __init__(self):
        super().__init__()
        print("C")
    def display(self):
        print("you are in a class C")

obj = c()
