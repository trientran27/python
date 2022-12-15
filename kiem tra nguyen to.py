
def nt(n):
    if(n<2): return 0
    for i in range(2, int(n**0.5)+1):
        if n%i==0: return 0
    return 1
for _ in range(int(input())):
    s=input()
    n=s[-4:]
    print("YES" if nt(int(n))==1 else "NO")