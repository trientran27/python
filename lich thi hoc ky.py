class Mon:
    def __init__(self,ma,ten) -> None:
        self.ma=ma
        self.ten=ten

class Lich:
    def __init__(self,ma,maMon,ngay,gio,soca) -> None:
        self.ma='T'+str(ma).rjust(3,'0')
        self.maMon=maMon
        self.ngay=ngay
        self.gio=gio
        self.soca=soca
    def sx1(self):
        a=self.ngay.split('/')
        return a[2]+a[1]+a[0]
    def sx2(self):
        a=self.gio.split(':')
        return  int(a[0])*60+int(a[1])
    
    
n,m=map(int,input().split())
mon=[]
lich=[]
for i in range(n):
    x=Mon(input(),input())
    mon.append(x)
for i in range(1,m+1):
    a=list(input().split())
    x=Lich(i,a[0],a[1],a[2],a[3])
    lich.append(x)
lich.sort(key=lambda x:(x.sx1(),x.sx2(),x.maMon))
for p in lich:
    print(p.ma,end=' ')
    print(p.maMon,end=' ')
    for m in mon:
        if(m.ma==p.maMon):
            print(m.ten,end=' ')
    print(p.ngay,p.gio,p.soca)

