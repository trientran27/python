#sap xep theo so lan xuat hien nhieu nhat va tu so nho toi lon
def sx(n):
    return n[0]*(-1), n[1]

for _ in range(int(input())):
    s, lst, c= int(input()), [], []
    for x in range(s):
        a= int(input())
        c+=[a]
        lst+=[[c.count(a), a]]
        #sap xep lst theo key
    lst = sorted(lst, key=sx)
    #in ra phan tu thu 2 trong lst con dau tien
    print(lst[0][1])
