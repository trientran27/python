
def ucln(a,b):
    if b==0: return a
    return ucln(b, a%b)

t= int(input())
s= sorted([int(x) for x in input().split()])

for i in range(t-1):
    for j in range(i+1, t):
        if(ucln(s[i], s[j])==1):
            print(s[i],s[j])