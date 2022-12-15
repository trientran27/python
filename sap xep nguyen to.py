def nt(n):
    if n<2: return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0: return False
    return True

n=int(input())
lst= [int(x) for x in input().split()]
b=[]
for c in lst:
    if nt(c): b+=[c]
b.sort()
for c in lst:
    if nt(c):
        print(b[0], end=" ")
        b.pop(0)
    else:  print(c, end=" ")