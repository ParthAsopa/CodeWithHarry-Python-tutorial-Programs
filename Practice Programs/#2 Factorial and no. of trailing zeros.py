class factorial_and_no_of_trailing_zeros():
    def Factorial(self, n):
        if n == 0 or n == 1:
            self.factorial = 1
        else:
            self.factorial = n*factorial_and_no_of_trailing_zeros.Factorial(self, n-1)
        return self.factorial

    def No_of_trailing_zeros(self, n):
        self.no_of_trailing_zeros = 0
        while True:
            if n % 5 == 0:
                self.no_of_trailing_zeros += 1
            elif n == 1:
                break
            else:
                pass
            n -= 1
        return self.no_of_trailing_zeros


if __name__ == "__Factorial_and_no_of_trailing_zeros__":
    n = int(input("Enter the number to find its factorial and number of trailing zeros:\n"))
    num = factorial_and_no_of_trailing_zeros()
    print(f"{n}! = {num.Factorial(n)}")
    print(f"Number of trailing zeros is {num.No_of_trailing_zeros(n)}")
