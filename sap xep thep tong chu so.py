
def sx(n):
    tong = sum([int(x) for x in n])
    #sap xep tong cac chu so tu nho toi lon, neu bang thi xep theo gia tri n
    return(tong, int(n))
for _ in range(int(input())):
    a=int(input())
    b= input().split()
    b=sorted(b, key=sx)
    print(" ".join(b))#noi cac phan tu trong a bang " "