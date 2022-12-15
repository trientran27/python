
for _ in range(int(input())):
    s=input()
    if len(set(s))!=2:
        print("NO")
    else:
        kt=1
        for i in range(len(s)-2):
            if s[i]!=s[i+2]:
                kt=0
                print("NO")
                break
        if kt==1:
            print("YES")
            