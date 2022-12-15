import math
from traceback import print_tb


a=[True]*100001
def sang():
    a[0]=False
    a[1]=False
    for i in range(2,math.isqrt(100000)+1):
        if(a[i]):
            j=i*i
            while(j<=100000):
                a[j]=False
                j+=i
sang()
n=int(input())
b=list(map(int,input().split()))
res=0
for i in b:
    if(not a[i]):
        for j in range(1000):
            if(a[i-j] or a[i+j]):
                res=max(res,j)
                break
print(res)

