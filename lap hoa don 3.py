
def sapxep(n):
    return n.tongtien

class mathang():
    def __init__(self):
        self.id=input()
        self.name=input()
        self.sl=int(input())
        self.dongia=int(input())
        self.chietkhau=int(input())
        self.tongtien= self.sl*self.dongia - self.chietkhau

lst=[]
for _ in range(int(input())):
    a=mathang()
    lst.append(a)

lst= sorted(lst, key= sapxep, reverse=True)
for c in lst:
    print(c.id, c.name, c.sl, c.dongia, c.chietkhau, c.tongtien)
