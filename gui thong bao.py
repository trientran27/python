
for i in range(int(input())):
    s=input()
    if len(s)<=100:
        print(s)
    else:
        if s[100]==" ":
            print(s[:100])#ki tu 100 khong phai la chu cai
        else:
            s=s[:100].split()
            print(" ".join(s[0:-1])) 