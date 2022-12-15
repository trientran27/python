n=int(input())
a=list(map(int,input().split()))
res=10000000
ind=-1
for i in range(len(a)):
    sum=0
    for j in range(len(a)):
        sum+=abs(a[i]-a[j])
    if(res>sum):
        res=sum
        ind=i
print(res,a[ind])

