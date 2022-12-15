
n, m=[int(x) for x in input().split()]

chan, le= [], []
lst=[]
if n>m: 
    chan=[x*2 for x in range(n-m)]#cac hang chan tinh tu 0
elif m>n:
    le=[x*2+1 for x in range(m-n)]#cac hang le tinh tu 0

for c in range(n):
    s=input().split()
    lst.append(s)
#loai bo hang chan tinh tu 0
if n>m:
    for i in range(n):
        if i not in chan:
            for j in range(m):
                print(lst[i][j], end=" ")
            print()
#loại bo cot le tinh tu 0
if m>n:
    for i in range(n):
        for j in range(m):
            if j not in le:
                print(lst[i][j], end=" ")
        print()
if m==n:
    for i in range(n):
        for j in range(m):
            print(lst[i][j],end=" ")
        print()
