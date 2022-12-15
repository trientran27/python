
class hs():
    def __init__(self):
        self.name=input()
        self.diem=input().split()
        self.tb= (float(self.diem[0])+float(self.diem[1]))*2 +sum([float(x) for x in self.diem[2:]])
        self.tb=round(self.tb/10/1.2, 1)#lam tron
        self.ma="HS"
        if self.tb<5: self.xl="YEU"
        elif self.tb <7: self.xl="TB"
        elif self.tb<8: self.xl = "KHA"
        elif self.tb<9: self.xl="GIOI"
        else: self.xl="XUAT SAC" 

def sx(n):
    return (n.tb, 0-int(n.ma[2:]))#diem tang, ma giam
lst=[]
for i in range(int(input())):
    a=hs()
    if i<9: a.ma+="0"+str(i+1)
    else: a.ma+=str(i+1)
    lst.append(a)
lst=sorted(lst, key=sx, reverse=True)
for x in lst:
    print(x.ma, x.name, x.tb, x.xl)