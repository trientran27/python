from re import ASCII
from string import ascii_letters


t = int(input())
for i in range(t):
    cnt = 0
    n, k = [int(x) for x in input().split()]
    while k % 2 == 0:
        cnt += 1
        k = int(k / 2)
    print(chr(65 + cnt))