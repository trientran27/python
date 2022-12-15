
def doiso(k, a, b):
  return int(k.replace(a, b))

for _ in range(int(input())):
    p, q= map(int, input().split())
    s=input()
    a1=s.split()
    if len(a1)==2:
        s1=a1[0]
        s2=a1[1]
    else:
        s1=s
        s2=input()
    smax= str(max(p, q))
    smin= str(min(p, q))
    resmax= doiso(s1, smin, smax) + doiso(s2, smin, smax)
    resmin= doiso(s1, smax, smin) + doiso(s2, smax, smin)
    print(resmin, resmax, sep=" ")