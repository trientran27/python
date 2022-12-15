import math

class point():
    def __init__(self, x1, y1):
        self.x=x1
        self.y=y1
    def distance(self, point):
        x = math.sqrt((self.x - point.x)**2 + (self.y - point.y)**2)
        return x

class Triangle():
    def __init__(self, a1, b1, c1) -> None:
        self.a=a1
        self.b=b1
        self.c=c1
    def Valid(self):
        A= self.a.distance(self.b)
        B= self.b.distance(self.c)
        C= self.c.distance(self.a)
        if A<=0 or B<=0 or C<=0 or A+B<=C or A+C<=B or B+C<=A:
            return False
        return True
    
    def Chuvi(self):
        A= self.a.distance(self.b)
        B= self.b.distance(self.c)
        C= self.c.distance(self.a)
        return "%.3f"%(A+B+C)

s=[]
n=int(input())
for _ in range(n):
    s+=[float(x) for x in input().split()]
i=0
while n>0:
    n-=1
    t= Triangle(point(s[i], s[i+1]), point(s[i+2], s[i+3]), point(s[i+4], s[i+5]))
    i+=6
    if t.Valid():
        print(t.Chuvi())
    else:
        print("INVALID")


