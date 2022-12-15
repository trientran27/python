
def sx(n):
    return -1*n.tb

class nv():
    def __init__(self) -> None:
        self.id="TS0"
        self.name=input()
        self.lt=float(input())
        if self.lt>10: self.lt/=10
        self.th=float(input())
        if self.th>10: self.th/=10
        self.tb=(self.lt+self.th)/2

        if self.tb<5: self.xl="TRUOT"
        elif self.tb<8: self.xl="CAN NHAC"
        elif self.tb<=9.5: self.xl="DAT"
        else: self.xl="XUAT SAC"

lst=[]
t=int(input())
for i in range(t):
    a=nv()
    a.id+=str(i+1)
    lst.append(a)
lst=sorted(lst, key=sx)
for c in lst:
    print(c.id, c.name, format(c.tb, ".2f"), c.xl)

