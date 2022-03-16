def Factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n*Factorial(n-1)


n = int(input("Enter the number to find its factorial:\n"))
fac_n = Factorial(n)
print(f"{n}! = {fac_n}")
no_of_zeros = 0
while True:
    if fac_n % 10 == 0:
        no_of_zeros += 1
        fac_n = fac_n/10
    else:
        break
print(f"Number of trainling zeros in {n}! = {no_of_zeros}")
