t=int(input())
while(t>0):
    n=list(input())
    c=True
    for i in range(len(n)-1,0,-1):
        if(int(n[i-1])>int(n[i])):
            c=False
            for j in range(len(n)-1,i-1,-1):
                if(int(n[j])<int(n[i-1])):
                    if(j!=0 and n[j]==n[j-1]):
                        continue
                    x=n[j]
                    n[j]=n[i-1]
                    n[i-1]=x
                    break
            break
    if(c or n[0]=='0'):
        print(-1)
    else:
        print("".join(n))
    t-=1