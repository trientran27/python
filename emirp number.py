def nt(n):
    if n<2: return 0
    for i in range(2,int(n**0.5)+1):
        if(n%i==0): return 0
    return 1
def tn(n):
    if n < int(str(n)[::-1]): return 1
    return 0
for _ in range(int(input())):
    n=int(input())
    for i in range(3, n, 2):
        if tn(i)==1 and nt(i)==1:
            k=int(str(i)[::-1])
            if(nt(k)==1 and k<n):
                print(i, k, sep=" ", end=" ")
    print()
