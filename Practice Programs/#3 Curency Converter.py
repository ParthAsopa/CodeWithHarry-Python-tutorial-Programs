with open("Currency.txt") as f:
    # reading all the lines in the txt file and storing each line as a string in a list.
    lines = f.readlines()


currency = {}

for line in lines:  # accessing each line separately from the list
    # splitting the lines from the places where \t is there...this separates the currency names with there value.
    parsed = line.split("\t")
    # storing the name of currency with there corresponding values in INR
    currency[parsed[0]] = parsed[1]


# Ammount to be converted currency to be converted to
usr_input1 = int(input("Enter the ammount:\n"))
usr_input2 = input("Enter name of currency to convert to:\n")
# converting the value of currency in INR to a float
factor = float(currency[usr_input2])
answer = usr_input1*factor
print(f"₹{usr_input1} = {answer} {usr_input2}")
