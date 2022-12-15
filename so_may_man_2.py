n= int(input())

while n>0:
    n-=1
    s= str(input())
    kt=1
    for x in s:
        if(x!='4' and x!='7'):
            kt=0
            print("NO")
            break
    if(kt==1):
        print("YES")