
s=input()
lst=[]
for i in range(0, len(s)-1, 2):
    a= s[i]+s[i+1]
    if int(a)>9 and int(a) not in lst:
        lst.append(int(a))
lst.sort()
for i in lst:
    print(i, end=" ")