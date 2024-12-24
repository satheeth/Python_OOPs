class company():
    def __init__(self):
        self._company_name = "google" #private

    def companyname(self):
        print(self._company_name)

class b(company):
    pass

b1 = b()
print(b1._company_name)

c1 = company()
c1.companyname()
print(c1._company_name)