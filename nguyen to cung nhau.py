
def ucln(a,b):
    if b==0: return a
    return ucln(b,a%b)

s=input().split()
n,k,dem = int(s[0]), int(s[1]), 0
for i in range(10**(k-1), 10**k):
    if ucln(n,i)==1:
        print(i, end=" ")
        dem+=1
        if dem%10==0: print("\n")