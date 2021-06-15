def game():
    return input("Enter a score: ")
y=int(game())
with open("high_score.txt") as f:
    n=int(f.read())
    if n < y:
        high_score=y
    elif n >= y:
        high_score=n
    print(f'High score = {high_score}')

x=str(high_score)

with open("high_score.txt" , "w") as f:
    f.write(x)