import math
print('''Variables allowed:
v: Final velocity
u: Initial velocity
a: Acceleration
t: Time taken
S: Displacement
NOTE: ONLY INTEGERS ALLOWED AS INPUT!!
NOTE: PROVIDE ONLY ONE VARIABLE, OTHERWISE YOU ARE HITTING AN AXE ON YOUR OWN LEG BY CRASHING THE PROGRAM!!
Also don't type the unit.
''')
variables=input("Mention the variables you have value of and you want value of (v,u,a,t,s):\n")
to_find= input("Enter the variable you want value of (v,u,a,t,s):\n")
formula=""
v=""
u=""
a=""
t=""
s=""
if variables.count("v")>=1:
    if variables.count("s")>=1: #formula => v^2 = u^2 +2as
        formula= "(v*v) = (u*u)+ 2(a*s)"
        if to_find.count("v")>=1:
            u=int(input("Enter value of u:"))
            a=int(input("Enter value of a:"))
            s=int(input("Enter value of s:"))
            x=(u*u) + 2*(a*s)
            v= math.sqrt(x)
            print(f"v = {v}")
        elif to_find.count("u")>=1:
            a=int(input("Enter value of a:"))
            s=int(input("Enter value of s:"))
            v=int(input("Enter value of v:"))
            x=((v*v) - (2*(a*s)))
            u=math.sqrt(x)
            print(f"u = {u}")
        elif to_find.count("a")>=1:
            u=int(input("Enter value of u:"))
            v=int(input("Enter value of v:"))
            s=int(input("Enter value of s:"))
            a=((v*v) - (u*u)) / (2*s)
            print(f"a = {a}")
        elif to_find.count("s")>=1:
            u=int(input("Enter value of u:"))
            v=int(input("Enter value of v:"))
            a=int(input("Enter value of a:"))
            s=((v*v) - (u*u)) / (2*a)
            print(f"s = {s}")
        elif to_find.count("t")>=1:
            print("The variable was not mentioned when asked.")
    elif variables.count("t")>=1: #formula => v=u+at
        formula="v = u + at"
        if to_find.count("v")>=1:
            u=int(input("Enter value of u:"))
            a=int(input("Enter value of a:"))
            t=int(input("Enter value of t:"))
            v = u + (a*t)
            print(f'v = {v}')
        elif to_find.count("u")>=1:
            v=int(input("Enter value of v:"))
            a=int(input("Enter value of a:"))
            t=int(input("Enter value of t:"))
            u = v - (a*t)
            print(f'u = {u}')
        elif to_find.count("a")>=1:
            v=int(input("Enter value of v:"))
            u=int(input("Enter value of u:"))
            t=int(input("Enter value of t:"))
            a = (v-u)/t
            print(f'a = {a}')
        elif to_find.count("t")>=1:
            v=int(input("Enter value of v:"))
            u=int(input("Enter value of u:"))
            a=int(input("Enter value of a:"))
            t = (v-u)/a
            print(f't = {t}')
        elif to_find.count("s")>=1:
            print("The variable was not mentioned when asked.")
elif variables.count("s")>=1:
    if variables.count("t")>=1: #formula => s = (ut) + (1/2)(at^2)
        formula = "s = (ut) + (1/2)(at^2)"
        if to_find.count("s")>=1:
            u=int(input("Enter value of u:"))
            a=int(input("Enter value of a:"))
            t=int(input("Enter value of t:"))
            s = (u*t) + (a*t*t)/2
            print(f's = {s}')
        elif to_find.count("u")>=1:
            s=int(input("Enter value of s:"))
            a=int(input("Enter value of a:"))
            t=int(input("Enter value of t:"))
            u = (s/t) - ((a*t)/2)
            print(f'u = {u}')
        elif to_find.count("t")>=1:
            s=int(input("Enter value of s:"))
            a=int(input("Enter value of a:"))
            u=int(input("Enter value of u:"))
            d= (u*u) + (2*a*s)
            t_1 = (-u) + math.sqrt(d)
            t_2 = (-u) - math.sqrt(d)
            print(f'''t_1 = {t_1}
t_2 = {t_2}''')
        elif to_find.count("a")>=1:
            s=int(input("Enter value of s:"))
            t=int(input("Enter value of t:"))
            u=int(input("Enter value of u:"))
            a = 2*(s - (u*t)) / (t*t)
            print(f'a = {a}')
        elif to_find.count("v")>=1:
            print("The variable was not mentioned when asked.")
else:
    print("I can solve only one equation at a time.")
print(f"Formula => {formula}")
