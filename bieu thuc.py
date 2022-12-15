import re
n=int(input())
a=[]
for i in range(n):
    x=1
    for j in "".join(re.split("[^\(\)]+",input())):
        if(j=='('):
            print(x,end=' ')
            a.append(x)
            x+=1
        else:
            print(a[len(a)-1],end=' ')
            a.pop()
    print()