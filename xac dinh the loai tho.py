t=int(input())
dem =0
lst=[0]
for i in range(t):
    n=len(input().split())
    if(n==6 and lst[-1]!=1):#the tho trong lst k phai luc bat
        lst+=[1]
        dem=0
    if(n==7):
        dem+=1
        if(dem==4):
            lst+=[2]
            dem=0
print(len(lst)-1)
for c in lst[1:]:
    print(c)