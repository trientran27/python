
def nt(n):
    if n<2: return 0
    for i in range(2, int(n**0.5)+1):
        if n%i==0: return 0
    return 1

for _ in range(int(input())):
    s=input()
    kt1, kt2=1, 1
    for i in range(len(s)):
        if i%2==0 and int(s[i])%2!=0:
            kt1=0
            break
        if i%2==1 and int(s[i])%2==0:
            kt2=0
            break
    
    so=set(s)
    sum=0
    for x in so:
        sum+=int(x)*s.count(x)
    if kt1==1 and kt2==1 and nt(sum)==1:
        print("YES")
    else:
        print("NO")