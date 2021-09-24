class Employee:
    salary=200
    increment=0
    @property
    def salaryafterincrement(self):#making salaryafterincrement a property
        return self.salary + self.increment
    @salaryafterincrement.setter#makeing a setter so that if salaryafterincrementis force fully changed, increment is fixed automatically
    def salaryafterincrement(self, val):
        self.increment = val-self.salary

e=Employee()
print(f"e.salary= {e.salary}")
print(f"e.increment= {+e.increment}")
print(f"e.salaryafterincrement= {e.salaryafterincrement}")
print(f'class increment = {Employee.increment}\n')

e.salaryafterincrement=500

print("after setting salary after increment= 500\n")

print(f"e.salary= {e.salary}")
print(f"e.increment= {+e.increment}")
print(f"e.salaryafterincrement= {e.salaryafterincrement}")

print(f'class increment = {Employee.increment}')