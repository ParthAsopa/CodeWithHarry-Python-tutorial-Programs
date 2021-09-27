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
            if index==0:
                unitvec="i"
            elif index==1:
                unitvec="j"
            elif index==2:
                unitvec="k"
            str1 += f"+({x}){unitvec}"
            index += 1
        return str1[1:]
         

    def __add__(self, other):
        list=[]
        for x in range(len(self.vec)):
            list.append(self.vec[x]+other.vec[x])
        return Vector(list)
    
    def __mul__(self, other):
        mulsum=0
        for x in range(len(self.vec)):
            mulsum+=self.vec[x]+other.vec[x]
        return mulsum


vec1=Vector([1,2, 3])
vec2=Vector([4,3,2])
print(f"vec1 = {vec1}")
print(f"vec2 = {vec2}")
print(f"vec1 + vec2 = {vec1+vec2}")
print(f"vec1 . vec2 = {vec1*vec2}")