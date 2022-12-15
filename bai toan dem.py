
n=int(input())

s=[]
while len(s)<n:
    s+=[int(x) for x in input().split()]
smax=max(s)
kt=1
for i in range(1, smax):
    if i not in s:
        print(i)
        kt=0
if kt==1: print("Excellent!")