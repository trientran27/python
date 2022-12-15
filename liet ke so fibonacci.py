
for _ in range(int(input())):
    s= input().split()
    a, b, c, dem= 1, 0, 0, 0
    while dem<int(s[1]):
        c=a+b
        a=b
        b=c
        dem+=1
        if dem>= int(s[0]): print(c, end=" ")
    print()