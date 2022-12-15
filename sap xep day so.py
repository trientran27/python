
for _ in range(int(input())):
    s=input().split()
    lst=[int(x) for x in input().split()]
    smax=lst.index(max(lst))
    lst= lst[:smax] + [int(s[1])] +  lst[smax:]

    res=""
    for x in lst:
        if x<0: print(x, end=" ")
        else: res+=str(x)+" "
    print(res)