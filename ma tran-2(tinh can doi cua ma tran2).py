
tren, duoi= 0, 0
t=int(input())
for i in range(t):
    s= input().split()
    for j in range(t):
        if j<t-i-1: tren+=int(s[j])
        if j>t-i-1: duoi+=int(s[j])
k=int(input())
if abs(tren-duoi) <=k:
    print("YES")
else: print("NO")
print(abs(tren - duoi))