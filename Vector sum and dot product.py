#vec = [i, j, k]
#       0  1  2
#      -3 -2 -1

class Vector:
    def __init__(self,vec):
        self.vec=vec
    def __str__(self):
        str1=""
        index=0
        for x in self.vec:
#           index=0  --> will set index to 0 every time loop runs....hence need to keep this command outside the loop.
            if index==0:
                unitvec="i"
            elif index==1:
                unitvec="j"
            elif index==2:
                unitvec="k"
            str1 += f"+({x}){unitvec}"
            index += 1
        return str1[1:] # will exclude the "+" in the starting of the string.
         

    def __add__(self, other):
        list=[]
        for x in range(len(self.vec)): # will add icap with icap and similarly for jcap and kcap and arange them in a list.
            list.append(self.vec[x]+other.vec[x])
        return Vector(list)# will execute the list of added vectors to be a new vector
    
    def __mul__(self, other):
        mulsum=0
        for x in range(len(self.vec)):# will multiply icap with icap and similarly for jcap and kcap and add them to get the dot product.
            mulsum+=self.vec[x]+other.vec[x]
        return mulsum
    
    def __len__(self):#display dimention if vector.
        return f"Vector is of {len(self.vec)} dimensions."

print('''**********************Welcome to Vector addition and dot product!!**********************''')
x1=int(input("Enter magnitude of vector1 in x direction:"))
y1=int(input("Enter magnitude of vector1 in y direction:"))
z1=int(input("Enter magnitude of vector1 in z direction:"))
vec1=Vector([x1,y1, z1])
print(f"\nVector1 = {vec1}\n\n")

x2=int(input("Enter magnitude of vector2 in x direction:"))
y2=int(input("Enter magnitude of vector2 in y direction:"))
z2=int(input("Enter magnitude of vector2 in z direction:"))
vec2=Vector([x2,y2,z2])
print(f"\nVector2 = {vec2}\n\n")


print(f"\nVector1 + Vector2 = {vec1+vec2}\n")
print(f"Vector1 . Vector2 = {vec1*vec2}\n")


print("Thank for using my program!!!")

#all "\n" used in line 36 to 54 are for better appearance.



'''
for vector  of n dimentions:

def __str__(self):
    str1=""
    index=0
    for i in self.vec:
        str1+=f"({i}) a{index} + "
        index+=1
    return str1[:-3]
'''
