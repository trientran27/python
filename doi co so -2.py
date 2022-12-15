
def doicoso(cs,np):
    tp=int(np,2)
    res=""
    while tp!=0:
        du=tp%cs
        tp//=cs
        if du>=10: res= chr(du-10 + ord('A'))+res
        else:
            res=chr(du + ord('0'))+res
    return res
for _ in range(int(input())):
    cs=int(input())
    np=input()
    print(doicoso(cs,np))
