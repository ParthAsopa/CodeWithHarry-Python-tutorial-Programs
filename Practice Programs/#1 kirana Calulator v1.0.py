print("Enter the price and press enter to add. Press q to quit.\n")
sum = 0
while True:
    usrInp = input('+')
    try:
        if usrInp != "q":
            sum += int(usrInp)
            print("= ", sum)
        elif usrInp == "q":
            break
    except Exception as x:
        print(x)

print("\nThe total is ", sum)
