
def nt(n):
    if n<2: return 0
    for i in range(2, int(n**0.5)+1):
        if n%i==0: return 0
    return 1

for _ in range(int(input())):
    n=input()
    so=set(n)
    sum=0
    for x in so:
        sum+=int(x)*n.count(x)
    if nt(sum)==1:
        print("YES")
    else:
        print("NO")