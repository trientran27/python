for _ in range(int(input())):
    n, x, m= [float(i) for i in input().split()]
    for a in range(1,10000):
        if(n*(1+x/100)**a >=m):
            print(a)
            break