
a=[0]*1000009
for i in range(2, 1000009):
    if a[i]==0:
        for j in range(i*2, 1000009, i):
            a[j]=1
for _ in range(int(input())):
    n= int(input())
    dem=0
    for i in range(3, n-5, 2):
        if a[i]==0 and a[i+6]==0:
            if a[i+2]==0 or a[i+4]==0:
                dem+=1
    print(dem)