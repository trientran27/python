def cnt_sum(st, n, a):
    cnt = 0
    for i in range(n-3):
        l = i + 1
        r = n - 1
        x = a[i]
        while l < r:
            if x + a[l] + a[r] == 0:
                cnt += 1
                l += 1
            elif x + a[l] + a[r] < 0:
                l += 1
            else:
                r -= 1
    return cnt



t = int(input())
while t > 0:
    n = int(input())
    a = list(map(int, input().split()))
    a = sorted(a)
    rs = cnt_sum(0, n, a)
    print(rs)
    t-=1