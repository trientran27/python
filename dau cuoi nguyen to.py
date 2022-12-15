
def nt(n):
    if n<2: return 0
    for i in range(2, int(n**0.5)+1):
        if n%i==0:
            return 0
    return 1
    
for _ in range(int(input())):
    n=input()
    dau=n[:3]
    cuoi=n[-3:]
    if nt(int(dau))==1 and nt(int(cuoi))==1:
        print("YES")
    else:
        print("NO")