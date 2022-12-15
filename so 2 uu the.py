import queue

for _ in range(int(input())):
    n=int(input())
    qe=queue.Queue()
    lst=["0", "1", "2"]
    for c in lst:
        if c!="0": qe.put(c)
    s=[]
    while n>0:
        a=qe.get()
        if a.count("2") > a.count("0") + a.count("1"):
            s+=[a]
            n-=1
        for c in lst:
            qe.put(a+c)
    print(" ".join(s))