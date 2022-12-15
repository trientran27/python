dx=[-1,-1,-1,0,1,1,1,0]
dy=[-1,0,1,1,1,0,-1,-1]
sum=0
n,m=map(int,input().split())
a=[]
check=[]



for i in range(n):
    b=list(map(int,input().split()))
    a.append(b)
    c=[True]*m
# print(a)
    check.append(c)
for i in range(n):
    for j in range(m):
        if(a[i][j]==-1):
            for k in range(8):
                inew=i+dx[k]
                jnew=j+dy[k]
                if(inew>=0 and jnew >=0 and inew <n and jnew <m and check[inew][jnew]):
                    sum+=a[inew][jnew]
                    check[inew][jnew]=False
print(sum)


