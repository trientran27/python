
for i in range (int(input())):
    n= int(input())
    print("1", end="")
    cnt=0
    while n%2==0:
        n//=2
        cnt+=1
    if cnt>0:
        print(" * " + str(2) + "^" + str(cnt), end="")
        cnt=0
    for i in range(3, n+1, 2):
        if n<=0:
            break
        while(n>0 and n%i==0):
            n//=i
            cnt+=1
        if cnt>0:
            print(" * " + str(i) + "^" + str(cnt), end="")
            cnt=0
    print()