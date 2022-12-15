
for _ in range(int(input())):
    s=input().split()
    lst=[]
    for i in range(int(s[0])):
        lst.append([int(x) for x in input().split()])

    for i in lst:
        hang=""
        for j in lst:
            a=0
            for k in range(int(s[1])):
                a+=i[k]*j[k]
            hang+=str(a)+" "
        print(hang)