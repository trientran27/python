
def ucln(a,b):
    if b==0: return a
    return ucln(b, a%b)

for _ in range(int(input())):
    print(ucln(int(input()), int(input())))