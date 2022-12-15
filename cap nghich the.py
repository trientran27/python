
n=int(input())

lst=input().split()
dem=0
for i in range(n-1):
    for j in range(i+1, n):
        if int(lst[i]) > int(lst[j]):
            dem+=1
print(dem)