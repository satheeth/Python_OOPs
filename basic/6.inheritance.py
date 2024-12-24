class dad():
    def phone(self):
        print("Dad's phone")

class mom():
    def sweet(self):
        print("mom's sweet")

class son(dad, mom): #multiple inheritance
    def laptop(self):
        print("Son's laptop")

ram = son()
ram.phone()
ram.sweet()