
x, y, z= [x for x in input().split()]
x, y = int(x), int(y)
if x<=0 or y<=0:
    print("INVALID")
else:
    print((x+y)*2, x*y, z.title())