
p = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."

while 1:
    nhap=[str(i) for i in input().split()]
    k=int(nhap[0])
    if(k==0): break
    s=nhap[1]
    result=""
    for x in s:
        result+=p[(p.index(x)+k)%28]
    
    print(result[::-1])
