
for _ in range(int(input())):
    n=int(input())
    lst=[int(x) for x in input().split()]
    a=[1]*n
    for i in range(1,n):
        j=i-1
        while(j>=0):
            if lst[j]<=lst[i]:
                a[i]+=a[j]
                j-=a[j]#xet ve phia truoc
            else: break
    for x in a:
        print(x, end=" ")
    print()