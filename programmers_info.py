class Programmers:
    company="Microsoft"
    def getName(self,name):
        self.name=name
    def getSalary(self,salary):
        self.salary=salary
    def getOrigin(self,origin):
        self.origin=origin

parth=Programmers()

parth.getName("Parth")
parth.getSalary("₹100")
parth.getOrigin("India")

print(f'Welcome {parth.name}')
print(f'Your salary is {parth.salary}')
print(f'You are from {parth.origin}')
