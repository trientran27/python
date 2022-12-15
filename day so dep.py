import time
if __name__ == "__main__":
    t = int(input())
    while (t > 0):
        n = int(input())
        a = [int(x) for x in input().split()]
        m = n
        dem = 0
        i = 0
        while (i < n-1):
            x = max(a[i], a[i+1])
            y = min(a[i], a[i+1])
            if (x > 2*y):
                dem += 1
                n += 1
                if (x % 2 == 0):
                    a.insert(i+1, int(x/2))
                else:
                    a.insert(i+1, int(x/2)+1)
                i -= 1
            i += 1
        print(n-m)
        t -= 1
# tim nhung so sao cho max>2min sau đo lay 1/2 cua no
