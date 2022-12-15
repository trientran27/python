
n=int(input())
lst=sorted([int(x) for x in input().split()])

print(max(lst[-1]*lst[-2]*lst[-3], lst[-1]*lst[-2], lst[0]*lst[1]*lst[-1], lst[0]*lst[1]))
