n=2
while n<=20:
    two = open(f"Table of {n}.txt" , "a")
    for i in range(11):
        two.write(f'{i} X {n} = {i*n}\n')
    n+=1
