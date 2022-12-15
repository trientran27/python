
def nt(n):
    if n<2: return 0
    for i in range(2, int(n**0.5)+1):
        if n%i==0: return 0
    return 1
def ucln(a, b):
    if b==0: return a
    return ucln(b, a%b)


for _ in range(int(input())):
    n, dem= int(input()), 1
    for i in range(2, n):
        if ucln(i, n)==1: dem+=1
    print("YES" if nt(dem)==1 else "NO")