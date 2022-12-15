def nt(n):
    if n==2: return "1"
    if n<2: return "0"
    for i in range(2,int(n**0.5)+1):
        if n%i==0: return "0"
    return "1"
    
t= [int(x) for x in input().split()]

lst=[]
for i in range(t[0]):
    lst+=[[nt(int(x)) for x in input().split()]]
for c in lst:
    print(" ".join(c) )














