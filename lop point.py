
import math
class Point():
    def __init__(self, x1, y1):
        self.x= x1
        self.y= y1
    def distance(self, Point):
        x = math.sqrt((self.x - Point.x)**2 + (self.y - Point.y)**2)
        return "%.4f"%x

def Decimal(a):
    return float(a)

if __name__ == '__main__':
    t = int(input())
    while t > 0:
        arr = input().split()
        p1 = Point(Decimal(arr[0]), Decimal(arr[1]))
        p2 = Point(Decimal(arr[2]), Decimal(arr[3]))
        print(p1.distance(p2))
        t -= 1