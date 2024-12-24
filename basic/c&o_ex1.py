class laptop:
    price = 0
    processor = ""
    ram = ""

    def perfomance(self):
        print("perfomance based on processor and ram")

HP = laptop()
DELL = laptop()
LENOVO = laptop()

HP.price = 45000
HP.processor = "i5"
HP.ram = "4GB"
HP.perfomance()
print(HP.price)
print(HP.processor)
print(HP.ram)

