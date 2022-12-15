
a, k, n = [int(x) for x in input().split()]

n= int(n/k)+1
kt=0
for i in range(1, n):
    x= i*k-a
    if x>0:
        print(x, end=" ")
        kt=1

if kt==0: print(-1)