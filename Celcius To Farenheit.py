#9C/5 = F-32
def cel_to_far(C):
    F = ((9*C)/5 ) + 32
    return F
c= int(input("Enter temperature in Celcius:\n"))
print(f"{c}℃ = {cel_to_far(c)}℉")
