
lst=[]
for _ in range(int(input())):
    s=input()
    for x in s:
        if x.isalpha():
            s=s.replace(x, " ")
    s=s.split()
    for x in s:
        lst.append(int(x))

lst=sorted(lst)
for x in lst:
    print(x)