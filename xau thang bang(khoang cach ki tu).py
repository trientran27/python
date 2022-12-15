
for _ in range(int(input())):
    s=input()
    a=s[::-1]
    kt=1
    for i in range(1, len(s)):
        if( abs(ord(s[i]) - ord(s[i-1])) != abs(ord(a[i]) - ord(a[i-1]))):
            kt=0
            break
    print("YES" if kt==1 else "NO")