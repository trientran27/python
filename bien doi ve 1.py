
while 1:
    n=int(input())
    if n==0: break
    if n==1:
        print(n)
    else:
        dem=1
        while n!=1:
            if n%2==0:
                n=int(n/2)
            else:
                n= n*3 + 1
            dem+=1
        print(dem)