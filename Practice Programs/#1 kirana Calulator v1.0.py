sum = 0
while True:
    usrInp = input("Enter the price and press enter to add. Press q to quit.\n")
    try:
        if usrInp != "q":
            sum += int(usrInp)
            print("Your bill so far is ", sum)
        elif usrInp == "q":
            break
    except Exception as x:
        print(x)

print("\nYour total is ", sum,"\nThanks for visiting, do visit again!\n")
