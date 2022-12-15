# vi so phuc tra ve dang a+bj , nen ta chi lay phan thuc, phan ao cua no ra
def inra(a, b):
    if b >= 0:
        return '{} + {}i'.format(a, b)
    else:
        return '{} - {}i'.format(a, b)


for _ in range(int(input())):
    s = [int(x) for x in input().split()]

    a = complex(s[0], s[1])
    b = complex(s[2], s[3])

    c, d = (a+b)*a, (a+b)**2
    # real phan thuc, imag phan ao
    print(inra(int(c.real), int(c.imag)), end=", ")
    print(inra(int(d.real), int(d.imag)))
