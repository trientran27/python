import math

def chuanHoa(s):
    s=s.strip()
    a=s.split()
    res=''
    for i in a:
        res+=i.title()+' '
    return res.strip()


class SV:
    def __init__(self,ma,ten,d1,d2,d3) -> None:
        self.ma='SV'+str(ma).rjust(2,'0')
        self.ten=chuanHoa(ten)
        self.d1=d1
        self.d2=d2
        self.d3=d3
    def getTB(self):
        d=(self.d1*3 + self.d2*3 + self.d3*2)/8
        d=d*1000
        q=d%10
        d=math.floor(d/10)
        if q>=5:
            d+=1
        d=d/100
        return d
t=int(input())
a=[]
for i in range(1,t+1):
    x=SV(i,input(),int(input()),int(input()),int(input()))
    a.append(x)
a.sort(key=lambda x:(-x.getTB(),x.ma))

tt=1
th=1

print(a[0].ma,a[0].ten,'%.2f'%a[0].getTB(),tt)




for i in range(1,t):
    th+=1
    if(a[i-1].getTB()!=a[i].getTB()):
        tt=th
        
    print(a[i].ma,a[i].ten,'%.2f'%a[i].getTB(),tt)

