
def nt(n):
    if n<2: return 0
    for i in range(2, int(n**0.5)+1):
        if n%i==0: return 0
    return 1

for _ in range(int(input())):
    n=input()
    so=set(n)
    sum=0
    kt=1
    if nt(int(n))==1 and nt(int(n[::-1]))==1:
        for x in so:
            if nt(int(x))==0:
                kt=0
                break
            else:
                sum+=int(x)*n.count(x)
        if nt(sum)==1 and kt==1:
            print("Yes")
        else:
            print("No")
    else:
        print("No")