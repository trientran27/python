
def gt(n):
    if n==0: return 1
    return n*gt(n-1)

for _ in range(int(input())):
    dem=0
    s=str(input())
    for c in s:
        dem+=gt(int(c))
    print("Yes" if dem==int(s) else "No")
