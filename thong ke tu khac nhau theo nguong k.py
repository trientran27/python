


def sapxep(n):
    return (0-n[1], n[0])#sap xep theo thu tu xuat hien giam dan
t, k=[int(x) for x in input().split()]
dic= dict()
for _ in range(t):
    s=input().lower()
    tu=""
    for c in s:
        if c.isalpha() or c.isnumeric():
            tu+=c
        else:
            if len(tu)>0:
                if tu not in dic:
                    dic[tu]=1
                else: dic[tu]+=1
            tu=""
    if len(tu)>0:
        if tu not in dic:
            dic[tu]=1
        else: dic[tu]+=1

dic= sorted(dic.items())
dic= sorted(dic, key=sapxep)

for c in dic:
    if(c[1]>=k):
        print(c[0], c[1])
        