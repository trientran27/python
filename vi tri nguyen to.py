
def nt(n):
    if n<2: return 0
    for i in range(2, int(n**0.5)+1):
        if(n%i==0): return 0
    return 1
for _ in range(int(input())):
    n= input()
    kt=1
    for i in range(len(n)):
        if nt(i)==1 and nt(int(n[i]))==0:
            kt=0
            break
        if nt(i)==0 and nt(int(n[i]))==1:
            kt=0
            break
    if kt==1:
        print("YES")
    else:
        print("NO")
