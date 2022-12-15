
def nt(n):
    if n<2: return 0
    for i in range(2, int(n**0.5)+1):
        if n%i==0:
            return 0
    return 1

for _ in range(int(input())):
    s=input();
    if nt(len(s))==0:
        print("NO")
    else:
        so=set(s)
        dem=0
        for x in so:
            if(nt(int(x))==1):
                dem+=s.count(x)
        if(dem>len(s)-dem):
            print("YES")
        else:
            print("NO")