
s=input()
k=int(input())
lst=[]
for i in range(0, len(s)-1, 2):
    a= s[i]+s[i+1]
    if int(a)>9 :
        lst.append(int(a))

a=sorted(set(lst))
kt=0
for x in a:
    if lst.count(x)>=k:
        kt=1
        print(x, lst.count(x), sep=" ")
if kt==0:
    print("NOT FOUND")