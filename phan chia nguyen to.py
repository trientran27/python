def nt(n):
    if n==2: return True
    for c in range(2,int(n**0.5)+1):
        if n%c==0:
            return False
    return True

t=int(input())
s=[int(x) for x in input().split()]
a = sorted(set(s),key=s.index)#tao 1 set sap xep theo thu tu xuat hien
l, r, z=0, sum(a), -1

for x in a:
    l+=x
    r-=x
    z+=1
    if(nt(l) and nt(r)):
        print(z)
        break
if(z==len(a)-1):
    print("NOT FOUND")