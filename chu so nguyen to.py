
def nt(n):
    if n<2: return 0
    for i in range(2, int(n**0.5)+1):
        if(n%i==0):
            return 0
    return 1

for _ in range(int(input())):
    s=input()
    so=set(s)
    if nt(len(s))==1:
        snt, sknt=0, 0
        for x in so:
            if nt(int(x))==1:
                snt+=s.count(x)
            else:
                sknt+=s.count(x)
        if snt>sknt:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")