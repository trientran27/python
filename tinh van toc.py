
def sx(n):
    return n.vt*(-1)
class ts():
    def __init__(self) -> None:
        self.name=input()
        a=self.name.split()
        self.dvi=input()
        b=self.dvi.split()
        self.id=""
        for c in b:
            self.id+=c[0].upper()
        for c in a:
            self.id+=c[0].upper()
        self.kt=input().split(":")
        self.vt=(120/(int(self.kt[0])-6 + int(self.kt[1])/60))

lst=[]
n=int(input())
for _ in range(n):
    a=ts()
    lst.append(a)
lst=sorted(lst, key=sx)
for c in lst:
    print(c.id, c.name, c.dvi, format(c.vt, ".0f") +" Km/h")