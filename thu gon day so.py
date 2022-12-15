n = int(input())

lst=[int(x) for x in input().split()]
check=1
while check==1:
    check=0
    j=0
    for i in range(len(lst)-1):
        if(i<len(lst)-1-j):
            if (lst[i] + lst[i+1])%2==0:
                lst.pop(i)
                lst.pop(i)
                j+=2
                check=1
    if check==0: break
print(len(lst))
