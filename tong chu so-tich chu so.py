
for _ in range(int(input())):
    n=input()
    tong, tich=0, 1
    for i in range(len(n)):
        if i%2==0:
            tong+=int(n[i])
        else:
            if int(n[i])!=0:
                tich*=int(n[i])
    print(tong, end=" ")
    if tich==1:
        print(0)
    else:
        print(tich)