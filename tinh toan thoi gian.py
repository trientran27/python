
def sapxep(n):
    return n.tg

class gamethu():
    def __init__(self):
        self.id=input()
        self.name=input()
        self.bd=input().split(":")
        self.kt=input().split(":")
        self.tg= int(self.kt[0])*60 + int(self.kt[1]) - int(self.bd[0])*60 - int(self.bd[1])
        self.ttg=[self.tg//60 , self.tg - (self.tg//60)*60]


lst=[]
for _ in range(int(input())):
    a=gamethu()
    lst.append(a)
lst=sorted(lst, key=sapxep, reverse=True)
for c in lst:
    print(c.id, c.name, str(c.ttg[0]), "gio", str(c.ttg[1]), "phut")
