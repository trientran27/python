
class sv():
    def __init__(self):
        self.msv=input()
        self.ten=input()
        self.lop=input()

class diem():
    def __init__(self):
        self.vao=input().split()
        self.msvd=self.vao[0]
        self.ghichu=""
        self.chuyencan=10-2*(self.vao[1].count('v'))-self.vao[1].count('m')
        if self.chuyencan <=0:
            self.chuyencan=0
            self.ghichu='KDDK'
t=int(input())
lst1=[]
lst2=[]
for c in range(t):
    a=sv()
    lst1.append(a)

for c in range(t):
    b= diem()
    lst2.append(b)

for e in lst1:
    for x in lst2:
        if e.msv == x.msvd:
            if x.chuyencan==0:
                print(e.msv, e.ten, e.lop, x.chuyencan, x.ghichu)
            else:
                print(e.msv, e.ten, e.lop, x.chuyencan)   