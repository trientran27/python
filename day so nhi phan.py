
n=int(input())
lst= input().split()
dem=0
for i in range(n-1):
    if lst[i]!=lst[i+1]:
        dem+=1
print(dem)