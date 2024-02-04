class Complex:
    def __init__(self,r,i):
        self.r = r
        self.i = i 
    def __add__(o1,o2):
        o3.r = o1.r + o2.r 
        o3.i = o1.i + o2.i 
        return o3
    def __sub__(o1,o2):
        o3.r = o1.r - o2.r 
        o3.i = o1.i - o2.i 
        return o3
    def __mul__(o1,o2):
        o3.r = (o1.r * o2.r) - (o1.i * o2.i)
        o3.i = (o1.r * o2.i) + (o1.i * o2.r)
        return o3

o1 = Complex(3,2)
o2 = Complex(1,7)
o3 = Complex(0,0)
o3 = o1+o2
print(o3.r,'+ i',o3.i)
o3 = o1-o2
print(o3.r,'+ i',o3.i)
o3 = o1*o2
print(o3.r,'+ i',o3.i)