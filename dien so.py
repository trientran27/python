
for _ in range(int(input())):
    n=int(input())
    a=sorted([int(x) for x in input().split()])
    print(a[n-1]-a[0]+1-len(set(a)))