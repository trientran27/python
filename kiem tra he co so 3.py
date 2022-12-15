
lst=["0", "1", "2"]

for _ in range(int(input())):
    s=input()
    kt=1
    for c in s:
        if lst.count(c)==0:
            kt=0
            print("NO")
            break
    if kt==1:
        print("YES")
