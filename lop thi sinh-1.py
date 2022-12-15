class ts():
    def __init__(self):
        self.name=input()
        self.date=input()
        self.dtb=sum([float(input()) for x in range(0,3)])
        self.dtb= "{:.1f}".format(self.dtb)
a=ts()
print(a.name, a.date, a.dtb)