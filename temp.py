"""
0+1
1+2 3+2
5+3 8+3 11+3
14+4 18+4 22+4 26+4
30
"""

x = 0

for i in range(1, 5):
    for j in range(i):
        print(f"{x}+{i}", end=" ")

        x += i
    if i == 1:
        print("First iteration completed.")
    elif i == 2:
        print("Second iteration completed.")
    elif i == 3:
        print("Third iteration completed.")
    elif i == 4:
        print("Fourth iteration completed.")

print(x)
