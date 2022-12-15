from fractions import Fraction as F
x=input().split()
a=F(int(x[0]), int(x[1]))
b=F(int(x[2]), int(x[3]))

c=a+b
if c==int(c):
    print(str(c)+"/1")
else:
    print(c)