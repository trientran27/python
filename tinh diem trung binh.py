
t=int(input())

s= sorted([float(x) for x in input().split()])
tong, dem=0,0
for i in range (1, t-1):
    if s[i]!=s[0] and s[i]!=s[t-1]:
        tong+=s[i]
        dem+=1
print(format(tong/dem, '.2f'))