n=int(input("Enter number to check:\n"))
prime=True
for i in range (2, n):
    if n%i ==0:
        prime = False
        break
if prime:
    print(f"{n} is a prime number.")
elif not prime:
    print(f"{n} is not a prime number.")