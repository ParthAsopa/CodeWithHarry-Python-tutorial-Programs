import math
class Calculator:
    @staticmethod
    def __init__():
        print("Hello User!")
    def Sqrt(self, num):
        self.sqrt=math.sqrt(num)
    def Sqr(self, num):
        self.sqr= num*num
    def Cube(self, num):
        self.cube= num*num*num
calculator = Calculator()
num=int(input("Enter number:\n"))
operations =input("Enter operation (Cube , Sqrt, Sqr ):\n").lower()
if operations=="cube":
    calculator.Cube(num)
    print(f"Cube of {num} = {calculator.cube} ")
elif operations=="sqr":
    calculator.Sqr(num)
    print(f"Square of {num} = {calculator.sqr} ")
elif operations=="sqrt":
    calculator.Sqrt(num)
    print(f"Square root of {num} = {calculator.sqrt} ")
