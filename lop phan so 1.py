from fractions import Fraction as F
x= input().split()
if(int(x[0])%int(x[1])==0):
    print(str(int(x[0])//int(x[1])) + "/1")
else:
    print(F(int(x[0]), int(x[1])))#ham thu gon va xu ly phan so