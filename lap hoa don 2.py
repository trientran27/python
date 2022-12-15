from datetime import date

def sapxep(n):
    return n.dichvu

class hoadon():
    def __init__(self):
        self.id="KH"
        self.name=input()
        self.phong=input()
        self.nhan=[int(x) for x in input().split("/")]
        self.tra=[int(x) for x in input().split("/")]
        self.dichvu=int(input())
        self.ngay=(date(self.tra[2], self.tra[1], self.tra[0]) - (date(self.nhan[2], self.nhan[1], self.nhan[0]) )).days + 1
        if self.phong[0]=='1': self.dichvu += self.ngay*25
        elif self.phong[0]=='2': self.dichvu += self.ngay*34
        elif self.phong[0]=="3": self.dichvu += self.ngay*50
        else: self.dichvu += self.ngay*80

lst=[]
for i in range(int(input())):
    a=hoadon()
    if i<9: a.id+="0"+str(i+1)
    else: a.id+=str(i+1)
    lst.append(a)

lst=sorted(lst, key=sapxep, reverse=True)
for c in lst:
    print(c.id, c.name, c.phong, c.ngay, c.dichvu)