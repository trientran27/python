
for _ in range(int(input())):
    s = input()
    so = set(s)
    tich = 1
    for x in so:
        if int(x) != 0:
            tich *= int(x)**s.count(x)
    print(tich)
