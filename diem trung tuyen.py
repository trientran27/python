def chuanHoa(s):
    s=s.strip()
    a=s.split()
    res=''
    for i in a:
        res+=i.title()+' '
    return res.strip()
class TS:
    def __init__(self,ma,ten,diem,danToc,kv) -> None:
        self.ma='TS'+str(ma).rjust(2,'0')
        self.ten=chuanHoa(ten)
        self.diem=diem
        self.danToc=danToc
        self.kv=kv
    def getDiem(self):
        d=self.diem
        if(self.kv==1):
            d+=1.5
        elif self.kv==2:
            d+=1
        if self.danToc!='Kinh':
            d+=1.5
        return d
    def getTT(self):
        if self.getDiem()>=20.5:
            return 'Do'
        else:
            return 'Truot'
    def __str__(self) -> str:
        return f'{self.ma} {self.ten} {self.getDiem()} {self.getTT()}'


t=int(input())
a=[]
for i in range(1,t+1):
    x=TS(i,input(),float(input()),input(),int(input()))
    a.append(x)
a.sort(key=lambda x:(-x.getDiem(),x.ma))
for i in a:
    print(i)
