
n, m=[int(x) for x in input().split()]

lst, maxn, minn=[], 0, 10000000
for i in range(n):
    s=[int(x) for x in input().split()]
    if max(s)>maxn: maxn=max(s)
    if min(s)<minn: minn=min(s)
    lst.append(s)
mayman=maxn-minn
inra=[]
for i in range(n):
    for j in range(m):
        if lst[i][j]==mayman:
            inra += ["[" + str(i) + "]" + "[" + str(j) + "]"]
        
if len(inra)==0:
    print("NOT FOUND")
else:
    print(mayman)
    for x in inra:
        print("Vi tri " + x)