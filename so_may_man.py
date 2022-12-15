s= str(input())

dem=0;

for x in s:
    if(x=='4' or x=='7'):
        dem+=1

if(dem==4 or dem==7):
    print("YES")
else:
    print("NO")