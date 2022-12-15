
def nt(n):
    if n<2: return 0
    for i in range(2, int(n**0.5)+1):
        if n%i==0: return 0
    return 1

n, x=map(int, input().split())
lst=[]
lst.append(x)
x+=2
lst.append(x)
#set tu so 3 de cong khoang cach 2
c=3
while n>1:
    if nt(c)==1:
        x+=c
        lst.append(x)
        n-=1
    c+=2
for i in lst:
   print(i, end=" ") 