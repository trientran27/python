
def sapxep(n):
    return (0-n[1], n[0])#sort theo value giam dan
dic=dict()
for _ in range(int(input())):
    s=input().lower()
    tu=""
    for c in s:
        if c.isalpha():
            tu+=c
        else:
            if len(tu)>0:
                if tu not in dic:
                   dic[tu]=1
                else: dic[tu]+=1
            tu=""
    if len(tu)>0:#tu cuoi cung
        if tu not in dic:
            dic[tu]=1
        else: dic[tu]+=1 
dic= sorted(dic.items())#xep theo tu dien
dic=sorted(dic, key=sapxep)

for c in dic:
    print(c[0],c[1])
