
def tinhtien(s):
    s=s.split()
    xe, ghe, huong, ngay= s[1], s[2], s[3], s[4]
    if huong=="OUT": return ngay, 0
    if xe=="Xe_con":
        if ghe=="5": return ngay, 10000
        return ngay, 15000
    elif xe=="Xe_tai": return ngay, 20000
    else:
        if ghe=="29": return ngay, 50000
        return ngay, 70000

lst=[]
for _ in range(int(input())):
    s=input()
    kt=0
    ngay, tien=tinhtien(s)
    for c in lst:
        if c[0]==ngay:
            c[1]+=tien
            kt=1
    if kt==0: lst.append([ngay, tien])

for c in lst:
    print(c[0]+": "+str(c[1]))
