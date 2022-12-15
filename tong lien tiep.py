import math
t = int(input())
while t > 0:
    n = 2 * int(input())
    cnt = 0
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            a, b = n/i, i
            k = a - b + 1
            if k % 2 == 0:
                l = (a - b + 1) / 2
                r = a - l
                if r >= 1 and r > l:
                    cnt += 1
    print(cnt)
    t -= 1