import queue

t=int(input())

lst=["0", "2", "4", "6", "8"]

for e in range(t):
    z=int(input())
    x=queue.Queue()
    for c in lst:
        if c>"0" : x.put(c)
    while True:
        item1 =x.get()
        if int(item1 +item1[::-1])<z :
            print(int(item1 +item1[::-1]), end=" ")
            for c in lst:
                x.put(item1+c)
        else: break
    print("\t")