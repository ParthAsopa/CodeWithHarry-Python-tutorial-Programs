def star_pattern(n):
    for i  in range(n):
        print("*" * (n-i))
n=int(input("Enter any number:\n"))
star_pattern(n)