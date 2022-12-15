

class Team:
    def __init__(self,i,ten,truong) -> None:
        self.ma='Team'+str(i).rjust(2,'0')
        self.ten=ten
        self.truong=truong

    def getMa(self):
        return self.ma
    def getTen(self):
        return self.ten
    def getTruong(self):
        return self.truong
    
class ThiSinh:
    def __init__(self,ma,ten,mateam) -> None:
        self.ma='C'+str(i).rjust(3,'0')
        self.ten=ten
        self.mateam=mateam

    def getTen(self):
        return self.ten
    def getMa(self):
        return self.ma
    def getMaTeam(self):
        return self.mateam

    
team=[]
thisinh=[]

t=int(input())
for i in range(1,t+1):
    ten=input()
    truong=input()
    x=Team(i,ten,truong)
    team.append(x)
t=int(input())
for i in range(1,t+1):
    ten=input()
    mateam=input()
    x=ThiSinh(i,ten,mateam)
    thisinh.append(x)


# for ts in thisinh:
#     print(ts.getMa())
# for te in team:
#     print(te.getMaTeam())

thisinh.sort(key=lambda a:a.getTen())
for ts in thisinh:
    print(ts.getMa(),ts.getTen(),end=' ')
    for te in team:
        if(te.getMa()==ts.getMaTeam()):
            print(te.getTen(),te.getTruong())
            break

