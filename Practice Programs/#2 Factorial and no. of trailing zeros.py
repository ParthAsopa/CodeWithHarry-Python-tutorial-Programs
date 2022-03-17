class factorial_and_no_of_trailing_zeros():
    def Factorial(self, n):
        if n == 0 or n == 1:
            self.factorial = 1
        else:
            self.factorial = n * factorial_and_no_of_trailing_zeros.Factorial(self, n-1)
        return self.factorial

    def No_of_trailing_zeros(self, n):
        '''
100!=100*99*98*97*96*...*5*4*3*2*1
=> Let n be a natural number, then,
   n=(5*a)+b
   and n-5=((5*(a-1))+b) 
Therefore, if we find the number of times 5 is multiplied in n then we can tell the number of 5s in n! as no. of times
5 is multiplied increases by 1 in every 5 natural numbers. So if 5 is multiplied 10 times in n then 5 is multiplied
11 times in n+5, so then in n!,we can write it as =>

            n!=1*2*3*4*(5+0)*(5+1)*(5+2)*(5+3)*(5+4)*(5*2+0)*(5*2+1)....(5*10+b) where (5*10+b) = n
        So clearly here we can see that 5 will be multiplied 10 times, hence we can get no. of 5s in n! 
        by counting the number of times 5 is multiplied in n.

'''
        self.no_of_trailing_zeros = 0
        i = 5
        while (n//i != 0):  # while n >=i
            self.no_of_trailing_zeros += int(n/i)# quotient of n/i will be no of times i is multiplied in n
            i *= 5  # because if we just divide with 5 then we will miss the other 5s in other powers of 5 so we divide n by every power of 5 till i>n, this way if we misss one 5 in 5^2 it will be counted in n/25 and if we miss 2 5s in 5^3 the one will be counted in n/25 and the other will be counted in n/125.
        return self.no_of_trailing_zeros


if __name__ == "__main__":
    n = int(
        input("Enter the number to find its factorial and number of trailing zeros:\n"))
    num = factorial_and_no_of_trailing_zeros()
    print(f"{n}! = {num.Factorial(n)}")
    print(f"Number of trailing zeros is {num.No_of_trailing_zeros(n)}")
