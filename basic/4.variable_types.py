class phone:
    charger_type = "C-type" #charger_type is class variable
    def __init__(self, brand, price,):
        self.brand = brand #self.brand is instance variable
        self.price = price
    def display(self):
        print("Brand: ", self.brand)
        print("Price: ", self.price)
        print("Charger Type", self.charger_type)

phone.charger_type = "B-type"
samsung = phone("samsung", "10000")
samsung.display()

redmi = phone("redmi", "8000")
redmi.display()

vivo = phone("vivo", "9000")
redmi.display()