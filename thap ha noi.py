
def kq(n, a, b):
    print(a +" -> " + b)
    
def thaphanoi(n, a, b, c):
    if(n==1):
        kq(n, a, c)
    else:
        thaphanoi(n-1, a, c, b)
        kq(n, a, c)
        thaphanoi(n-1, b, a, c)

n=int(input())
a, b, c= "A", "B", "C"
thaphanoi(n, a, b, c)
