class Complex:
    def __init__(self, r, i):
        self.imaginary=i
        self.real=r

    def __add__(self, other):#(a+bi)+(c+di)=(a+c)+(b+d)i
        addreal=self.real+other.real #(a+c)
        addimaginary=self.imaginary+other.imaginary#(b+d)
        return Complex(addreal, addimaginary)
    
    def __mul__(self, other):# (a+bi)(c+di) = (ac−bd) + (ad+bc)i
        mulimaginary=(self.real*other.imaginary) + (self.imaginary*other.real)#(ad+bc)
        mulreal=(self.real*other.real) - (self.imaginary*other.imaginary)#(ac−bd)
        return Complex(mulreal, mulimaginary)
    
    def __str__(self):
        if self.imaginary<0:#if magnitude of imaginary no. is negative, there will be a -ve sign b/w real part and imaginary part(and here magnitude of imaginary part already has a "-" sign so no need of sign in the string.)
            return f"{self.real}{self.imaginary}i" 
        else:#if magnitude of imaginary no. is positive, there will be a +ve sign b/w real part and imaginary part.
            return f"{self.real}+{self.imaginary}i"

c1=Complex(500,-500)
c2=Complex(100,100)
print(c1+c2)
print(c1*c2)

