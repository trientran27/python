
for i in range(int(input())):
    a=input()
    b=input()
    print("Test " + str(i+1) + ":" , end=" ")
    if sorted(list(a))==sorted(list(b)): print("YES")
    else: print("NO")