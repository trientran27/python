from email.mime import image


import itertools

s=input()

lst= list(itertools.permutations(list(s)))
for c in lst:
    print("".join(list(c)))