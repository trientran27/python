class Phong:
    def __init__(self,ma,ten) -> None:
        self.ma=ma
        self.ten=ten

class NV:
    def __init__(self,ma,ten,luong,snc) -> None:
        self.ma=ma
        self.ten=ten
        self.luong=luong
        self.snc=snc
    def getNhom(self):
        return self.ma[0]
    def getNam(self):
        return int(self.ma[1:3])
    def getMaP(self):
        return self.ma[3:]
    def getHeSo(self):
        if(self.getNhom()=='A'):
            if(self.getNam()<=3):
                return 10
            elif self.getNam()<=8:
                return 12
            elif self.getNam()<=15:
                return 14
            else:
                return 20
        elif(self.getNhom()=='B'):
            if(self.getNam()<=3):
                return 10
            elif self.getNam()<=8:
                return 11
            elif self.getNam()<=15:
                return 13
            else:
                return 16
        elif(self.getNhom()=='C'):
            if(self.getNam()<=3):
                return 9
            elif self.getNam()<=8:
                return 10
            elif self.getNam()<=15:
                return 12
            else:
                return 14
        else:
            if(self.getNam()<=3):
                return 8
            elif self.getNam()<=8:
                return 9
            elif self.getNam()<=15:
                return 11
            else:
                return 13
    def getLuong(self):
        return self.getHeSo()*self.luong*self.snc*1000

phong=[]
nv=[]

n=int(input())
for i in range(n):
    a=list(input().split())
    res=''
    for j in range(1,len(a)):
        res+=a[j]+' '
    x=Phong(a[0],res.strip())
    phong.append(x)
m=int(input())
for i in range(m):
    x=NV(input(),input(),int(input()),int(input()))
    nv.append(x)

for n in nv:
    print(n.ma,n.ten,end=' ')
    for p in phong:
        if(n.getMaP()==p.ma):
            print(p.ten,end=' ')
    print(n.getLuong())


