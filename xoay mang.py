for _ in range(int(input())):
    n,k=map(int, input().split())
    lst=[int(x) for x in input().split()]
    result= lst[k:]+lst[:k]
    for i in result:
        print(i, end=" ")
    print()
