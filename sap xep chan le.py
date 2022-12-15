
n=int(input())
s=[]
while 1:
    s+=[int(x) for x in input().split()]
    if len(s)==n: break

a= sorted(list(filter(lambda x: (x%2)!=0, s)), reverse=True)
b= sorted(list(filter(lambda x: (x%2)==0, s)))

for x in s:
    if x%2==0:
        print(b[0], end=" ")
        b.pop(0)
    else:
        print(a[0], end=" ")
        a.pop(0)