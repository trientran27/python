
for _ in range(int(input())):
    n=input()
    so=set(n)
    sum=0
    for x in so:
        sum+=int(x)*n.count(x)
    if sum%3==0:
        print("YES")
    else:
        print("NO")