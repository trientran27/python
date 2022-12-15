for _ in range(int(input())):
    s=input()
    n=len(s)
    a,kt=s[::-1],1
    for i in range(1,n):
        if abs(ord(s[i])-ord(s[i-1])) != abs(ord(a[i])-ord(a[i-1])):
            kt=0
            break
    print("YES" if kt==1 else "NO")