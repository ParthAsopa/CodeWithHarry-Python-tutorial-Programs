def sum_n(n):
    if n==1:
        return 1
    elif n==0:
        return 0
    else:
        return n+sum_n(n-1)
n=int(input("Enter number of natural nubers:\n"))
print(f"Sum of first {n} naturaal numbers = {sum_n(n)}")
