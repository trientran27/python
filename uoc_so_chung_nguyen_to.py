
def ucln(a, b):
    if b==0: return a
    return ucln(b, a%b)

def nt(n):
    if n<2: return 0
    for i in range(2, int(n**0.5)+1):
        if n%i==0: return 0
    return 1

def tcs(a, b):
    s= str(ucln(a, b))
    sum=0
    for c in s:
        sum+=int(c)
    return sum

for _ in range(int(input())):
    m, n = [int(x) for x in input().split()]
    print("YES" if nt(tcs(m, n))==1 else "NO")
        
