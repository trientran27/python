
import itertools
s=input().split()
a=input().split()
lst=sorted(list(set(a)))
b = list(itertools.combinations(lst, int(s[1])))

for c in b:
    print(" ".join(c))
