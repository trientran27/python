
for _ in range(int(input())):
    s=input()
    if len(s)%2==0:
        print("NO")
    else:
        if(s[0]==s[1]):
            print("NO")
        else:
            kt=1
            for i in range(0, len(s)-2, 2):
                if(s[i]!=s[i+2]):
                    kt=0
                    break
            if(kt==1):
                print("YES")
            else:
                print("NO")