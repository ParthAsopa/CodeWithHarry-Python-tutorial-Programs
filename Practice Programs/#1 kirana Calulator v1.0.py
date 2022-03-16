sum = 0
l = []
while True:
    usrInp = input(
        "Enter the price and press enter to add. Press q to quit.\n")
    try:
        if usrInp != "q":
            sum += int(usrInp)
            l.append(int(usrInp))
            print("Your bill so far is ", sum)
        elif usrInp == "q":
            break
    except Exception as x:
        print(x)
print("\nRadhavalabh Super Market")
for index, item in enumerate(l):
    print(f"{index+1}. {item}")
print("\nYour total is ", sum, "\nThanks for visiting, do visit again!\n")
