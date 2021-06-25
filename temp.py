class Employee:
    salary = 10000
    increment=1000
    @property
    def totalSalary(self):
        return self.salary+ self.increment
    @totalSalary.setter
    def totalSalary(self, totalSalary):
        self.increment= totalSalary - self.salary

Parth=Employee()
Parth.totalSalary=10500
print(Parth.salary)
print(Parth.increment)
