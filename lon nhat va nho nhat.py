
while(1):
    n =int(input())
    if n==0: break
    lst=[]
    for i in range(n):
        lst.append(int(input()))
    smin=min(lst)
    smax=max(lst)
    if smax==smin: print("BANG NHAU")
    else: print(smin, smax, sep=" ")