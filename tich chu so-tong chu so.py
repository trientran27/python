
for _ in range(int(input())):
    n=input()
    tong, tich=0, 1
    for i in range(len(n)):
        if i%2==1:
            tong+=int(n[i])
        else:
            if int(n[i])!=0:
                tich*=int(n[i])
    
    print(tich, tong)