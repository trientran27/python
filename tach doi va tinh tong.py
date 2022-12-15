
n=input()
while len(n)>1:
    k=int(len(n)/2)
    n=str(int(n[:k]) + int(n[k:]))
    print(n)