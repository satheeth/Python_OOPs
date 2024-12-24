class laptop():
    charger_type = "C_type"

    def __init__(self):
        self.brand = ""
        self.price = 34

    def setPrice(self,price):
        self.price = price

    def getPrice(self): # instance method
        print(self.price)

    @classmethod
    def changecharger_type(cls): # class method
        cls.charger_type = "B-type"
        print("Charger type changed to B")

    @staticmethod
    def info(): # static method
        print("This is laptop class")

hp = laptop()
hp.setPrice(20000)
hp.getPrice()
laptop.changecharger_type()

hp.info()