
s=input().split()

a=input().split()
b=input().split()

x=set(a)
y=set(b)
print(" ".join(sorted(x & y)))
print(" ".join(sorted(x - y)))
print(" ".join(sorted(y - x)))