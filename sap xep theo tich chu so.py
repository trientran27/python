def sx(n):
    tich=1
    for x in n:
        tich *=int(x)
    #sap xep tich cac chu so tu nho toi lon, neu bang thi xep theo gia tri n
    return(tich, int(n))
for _ in range(int(input())):
    a=int(input())
    b= input().split()
    b=sorted(b, key=sx)
    print(" ".join(b))#noi cac phan tu trong a bang " "