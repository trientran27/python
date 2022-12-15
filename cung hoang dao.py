#cung ma ket phai chia thanh (22-31)-12 va (01-19)-01
thang=['0101', '0120', '0219', '0321', '0420', '0521', '0621', '0723', '0823', '0923', '1023', '1123', '1222', '1232']
cung = ['Ma Ket','Bao Binh','Song Ngu','Bach Duong','Kim Nguu','Song Tu','Cu Giai','Su Tu','Xu Nu','Thien Binh','Thien Yet','Nhan Ma','Ma Ket']

for _ in range(int(input())):
    s=input().split()
    n=""
    #so sanh thang truoc sau do moi so sanh ngay
    if int(s[1])<=9:
        n="0"+s[1]
    else: n=s[1]
    if int(s[0])<=9:
        n+="0"+s[0]
    else:n+=s[0]

    for i in range(len(thang)):
        if n<thang[i]:
            print(cung[i-1])
            break
