
while 1:
    s=input().split()

    a=[int(x) for x in s]
    if a==[0, 0, 0, 0]: break
    dem=0
    while(1):
        if a[0]==a[1]==a[2]==a[3]: break
        dem+=1
        gt=a[0]
        a[0]=abs(a[0]-a[1])
        a[1]=abs(a[1]-a[2])
        a[2]=abs(a[2]-a[3])
        a[3]=abs(a[3]-gt)
    print(dem)