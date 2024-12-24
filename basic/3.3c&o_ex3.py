class teacher:
    def __init__(self, name, regno):
        self.name= name
        self.regno= regno
    def display(self):
        print("Name: ", self.name)
        print("Regno: ", self.regno)

t1 = teacher("satheeth", "1")
t2 = teacher("mohamed", "2")

t1.display()
t2.display()

