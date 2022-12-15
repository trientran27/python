
for x in range (int(input())):
    s= input()
    sum=int(s[0])
    check=1
    for i in range(len(s)-1):
        if abs( int(s[i]) - int(s[i+1])) !=2:
            check=0
            break
        else:
            sum+=int(s[i+1])
    if check==1 and sum%10==0:
        print("YES")
    else:
        print("NO")