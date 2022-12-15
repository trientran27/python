
def ucln(a,b):
    if b==0: return a
    return ucln(b, a%b)

for _ in range(int(input())):
    s=input()
    a=int(s)
    b=int(s[::-1])
    if ucln(a,b)==1:
        print("YES")
    else:
        print("NO")
