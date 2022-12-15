for _ in range(int(input())):
    n, dem, kq = int(input()), 0, -1
    while dem < 1000:
        if n % 7 == 0:
            kq = n
            break
        n = n + int(str(n)[::-1])
        dem += 1
    print(kq)
