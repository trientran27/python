
for _ in range(int(input())):
    n, m, k=[int(x) for x in input().split()]
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]
    c = [int(x) for x in input().split()]

    i, j, l, kt=0, 0, 0, 0

    while i<n and j<m and l<k:
        if a[i]==b[j]==c[l]:
            print(a[i], end=" ")
            kt=1
            i, j, l = i+1, j+1, l+1
        elif a[i]<b[j]: i+=1
        elif b[j]<c[l]: j+=1
        else: l+=1

    if kt==0: print("NO")
    else: print()