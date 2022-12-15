
t=input().split()
s=input().split()

lst= [0]*int(t[1]) #tao 1 list co so luong phan tu la int(t[1])

for c in s:
    lst[int(c)-1]+=1
#sap xep lai so luong phieu tren 1 cu tri
z= list(set(lst))
z.sort()
if len(z)>=2:
    for c in s:
        if lst[int(c)-1]==z[-2]:
            print(c)
            break
    else:print("NONE")#nguoi nhieu thu 2 co 0 phieu bau , con toan bo cac nguoi khac phieu bau bang nhau
else: print("NONE")