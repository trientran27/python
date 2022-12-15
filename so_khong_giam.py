
for x in range(int(input())):
    s= str(input())
    kt=1
    for i in range(len(s)-1):
        if(s[i] > s[i+1]):
            print("NO")
            kt=0
            break
    if kt==1:
        print("YES")