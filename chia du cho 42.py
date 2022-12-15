
lst, ptu=[],0

while ptu<10:
    s= input().split()
    ptu+=len(s)
    lst+=[int(x)%42 for x in s]
print(len(set(lst)))