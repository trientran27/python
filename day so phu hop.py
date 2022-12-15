
for _ in range(int(input())):
    n=int(input())
    lst1=[int(i) for i in input().split()]
    lst2=[int(i) for i in input().split()]

    lst1.sort()
    lst2.sort()
    kt=1
    for i in range(n):
        if int(lst1[i]) > int(lst2[i]):
            kt=0
            break
    print("YES" if kt==1 else "NO")