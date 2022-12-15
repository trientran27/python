import math

def binS(ham,l,r,n):
    if l>r:
        return 'Not in sequence'
    m=(l+r)//2
    if n==ham[m]:
        return m+1
    else:
        if n<ham[m]:
            return binS(ham,l,m-1,n)
        else:
            return binS(ham,m+1,r,n)

t = int(input())
ham=[]
s = int(math.pow(10,18))
a = int(math.log(s,2))
b = int(math.log(s,3))
c = int(math.log(s,5))
for i in range(0,a+1):
    for j in range(0,b+1):
        for k in range(0,c+1):
            x = int(pow(2,i))*int(pow(3,j))*int(pow(5,k))
            ham.append(x)
ham = sorted(ham)
while t > 0:
    n = int(input())
    print(binS(ham,0,10917,n))
    t-=1