
def sx(n):
    return n.tong*(-1)

class gv():
    def __init__(self) -> None:
        self.id="GV"
        self.name=input()
        self.ma=input()
        self.tong=float(input())*2 + float(input())
        if self.ma[1]=="1": self.tong+=2
        elif self.ma[1]=="2": self.tong+=1.5
        elif self.ma[1]=="3": self.tong+=1

        if self.tong>=18: self.xl="TRUNG TUYEN"
        else: self.xl="LOAI"

        if self.ma[0]=="A": self.mon="TOAN"
        elif self.ma[0]=="B": self.mon="LY"
        else: self.mon="HOA"

lst=[]
t=int(input())
for i in range(t):
    a=gv()
    if i<9:
        a.id+="0"+str(i+1)
    else:
        a.id+=str(i+1)
    lst.append(a)
lst=sorted(lst, key=sx)
for c in lst:
    print(c.id, c.name, c.mon, format(c.tong, ".1f"), c.xl)




