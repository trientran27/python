
def sx(a):
    return ((-1)*a.diem[0], a.diem[1], a.name)
class sv():
    def __init__(self):
        self.name =input().title()#chuan hoa ho ten
        self.diem = [int(x) for x in input().split()]

lst=[]
for c in range(int(input())):
    a=sv()
    lst.append(a)
lst=sorted(lst, key=sx)
for x in lst:
    print(x.name, x.diem[0], x.diem[1])