
for _ in range(int(input())):
    n=int(input())
    s=[int(x) for x in input().split()]
    a=set(s)
    for x in a:
        if s.count(x)%2==1:
            print(x)
            break