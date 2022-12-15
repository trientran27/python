class Phim:
    def __init__(self,ma,matl,ngay,ten,tap) -> None:
        self.ma='P'+str(ma).rjust(3,'0')
        self.matl=matl
        self.ngay=ngay
        self.ten=ten
        self.tap=tap
    def sx(self):
        a=self.ngay.split('/')
        return a[2]+a[1]+a[0]

n,m=map(int,input().split())
tl=[]
phim=[]
for i in range(n):
    tl.append(input())
for i in range(1,m+1):
    x=Phim(i,input(),input(),input(),int(input()))
    phim.append(x)
phim.sort(key=lambda x:(x.sx(),x.ten,-x.tap))
for p in phim:
    print(p.ma,end=' ')
    so=int(p.matl[2:])
    print(tl[so-1],end=' ')
    print(p.ngay,p.ten,p.tap)
