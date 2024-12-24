class employee():
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class manager(employee):
    def __init__(self,name, salary, department):
        super().__init__(name, salary)
        self.department = department

    def display(self):
        print("Name: ", self.name)
        print("Salary: ", self.salary)
        print("Department: ", self.department)

m1 = manager("Satheeth", "10000", "MCA")
m1.display()