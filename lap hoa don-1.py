

import math
def sapxep(n):
    return n.tien

class dongia():
    def __init__(self):
        self.ten=input()
        self.money= -1*int(input())+ int(input())
        self.ma="KH"
        self.tien=0
        if self.money<=50:
            self.tien = self.money*100
            self.tien +=self.tien*0.02
        elif self.money<=100:
            self.tien = (self.money-50)*150+50*100
            self.tien +=self.tien*0.03
        else:
            self.tien = (self.money-100)*200+50*100+50*150
            self.tien +=self.tien*0.05
        self.tien= math.ceil(self.tien)
            
lst=[]        
for i in range(int(input())):
    a=dongia()
    if i<9: a.ma +="0"+str(i+1)
    else: a.ma+=str(i+1)
    lst.append(a)
lst= sorted(lst, key=sapxep, reverse=True)
for c in lst:
    print(c.ma, c.ten, c.tien)


