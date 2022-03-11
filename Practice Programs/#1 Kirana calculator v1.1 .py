from functools import reduce
expression = input("Enter the prices separated by spaces or commas.\n")#take the expression
l1 = []
expression=expression.replace(" ", ",")#replace the spaces with commas so that the terms can be separated.

while expression.find(",") != -1:#while loop till there are no more commas in the string, which means till we don't reach the last term.
    commaindex = expression.find(",")#finding the index of first comma so that we can append the terms that are separated by commas in a list.
    l1.append(expression[0:commaindex])#appending the first term that ends at the comma.
    expression = expression.replace(expression[0:commaindex+1], "")#replacing the first term and first comma with a empty string because when the loop runs, it only appends the first term so we are making the second term, the first term.
l1.append(expression)#after the loop ends, we are left with the last term which is not separated by a comma so it wasn't considered in the loop, hence we are adding it separately.

l2 = []
for i in l1:#converting the terms of our expression into integers and appending them to another list so that we can perform arithmetic operation on them.
    try:
        l2.append(int(i))
    except Exception as x:
        pass


def sum(a, b): return a+b


print("Terms you entered = ", l1)
print("Terms that are considered for sumation = ", l2)

print("sum = ", reduce(sum, l2))#using reduce to apply rolling compution.
