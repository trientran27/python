
import itertools


for _ in range(int(input())):
    n=int(input())
    lst= [str(x) for x in range(1, n+1)]
    hoanvi= list(itertools.permutations(lst))
    print(len(hoanvi))
    for c in hoanvi[::-1]:
        print("".join(c), end=" ")
    print()