
class luongmua():
    def __init__(self):
        self.ten = input()
        self.bd = [int(x) for x in input().split(":")]
        self.kt = [int(x) for x in input().split(":")]
        self.lm = int(input())
        self.tg = self.kt[0]*60 + self.kt[1] - self.bd[0]*60-self.bd[1]
        self.ma = "T"


lst = []  # luu tru thong tin cac vung
ten = []  # luu tru ten
for i in range(int(input())):
    a = luongmua()
    if i < 9:
        a.ma += "0"+str(i+1)
    else:
        a.ma += str(i+1)
    if a.ten not in ten:
        ten.append(a.ten)
        a.tlm = a.lm
        a.tgm = a.tg
        lst.append(a)
    else:
        for c in lst:
            if a.ten == c.ten:
                c.tlm += a.lm
                c.tgm += a.tg

for c in lst:
    print(c.ma, c.ten, format(c.tlm/(c.tgm/60), ".2f"))
