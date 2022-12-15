
for _ in range(int(input())):
    n= int(input())
    s=[int(x) for x in input().split()]
    s.sort()
    if s.count(s[n//2])>n/2:
        print(s[n//2])
    else:
        print("NO")