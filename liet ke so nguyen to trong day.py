
def nt(n):
    if n<2: return 0
    for i in range(2, int(n**0.5)+1):
        if n%i==0: return 0
    return 1
t=int(input())

s=[int(x) for x in input().split()]

a=sorted(set(s), key=s.index)
for x in a:
    if nt(x):
        print(x, s.count(x))