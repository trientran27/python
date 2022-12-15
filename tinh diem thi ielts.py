diem=[3, 5, 7, 10, 13, 16, 20, 23, 27, 30, 33, 35, 37, 39, 41]

for _ in range(int(input())):
    ktr, ktl=0, 0
    s= [float (x) for x in input().split()]
    for i in range(len(diem)):
        if s[0]<diem[i] and ktr==0:
            s[0]= 2+0.5*i
            ktr=1
        if s[1]<diem[i] and ktl==0:
            s[1]=2+0.5*i
            ktl=1
    tb=sum(s)/4
    if tb- int(tb)<0.25: tb=int(tb)+0.0
    elif tb- int(tb)<0.75: tb=int(tb)+0.5
    else:
        tb=int(tb)+1.0
    print(tb)