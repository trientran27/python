
s=input()
lst=[]
for i in range(0, len(s)-1, 2):
    a= s[i]+s[i+1]
    if int(a)>9 :
        lst.append(int(a))

a=sorted(set(lst), key=lst.index)
for x in a:
    print(x, lst.count(x), sep=" ")