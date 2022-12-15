import queue

lst=["0", "2", "4", "6", "8"]

t=int(input())

for _ in range(t):
    z=int(input())
    x= queue.Queue()
    for c in lst:
        if c>"0":
            x.put(c)
    
    while True:
        item = x.get()
        if(int(item + item[::-1]) <z):
            print(int(item + item[::-1]), end=" ")
            for c in lst:
                x.put(item+c)
        else:
            break
    print()