import itertools

n, k= map(int, input().split())
s=input()
#tao 1 list duoc sap xep gom cac chu so khac nhau co trong s
lst= list(set(int(i) for i in s.split()))
# tao list b gom cac list to hop 
lst.sort()
b=list(itertools.combinations(lst, k))
for c in b:
    for i in c:
        print(i, end=" ")
    print()