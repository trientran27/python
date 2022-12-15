
class sv():
    def __init__(self):
        self.ma=input()
        self.name=input()
        self.hinhthuc=input()
lst=[]
for _ in range(int(input())):
    a=sv()
    lst.append(a)

lst= sorted(lst, key=lambda x:x.ma)
for c in lst:
    print(c.ma, c.name, c.hinhthuc)