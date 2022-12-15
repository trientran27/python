
def doicoso(a,b):
    res=""
    while a>0:
        t=a%b
        a//=b
        if t>=10: res+= chr(55+t)
        else: res+=str(t)
    return res[::-1]
for _ in range(int(input())):
    s=input().split()
    a, b = int(s[0]), int(s[1])
    print(doicoso(a,b))